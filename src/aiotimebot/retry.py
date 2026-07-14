"""Retry decisions for Time REST requests."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class RetryPolicy:
    """Define bounded retries without duplicating unsafe Time operations."""

    max_attempts: int = 3
    base_delay: float = 0.25
    max_delay: float = 30.0
    default_rate_limit_delay: float = 1.0

    def __post_init__(self) -> None:
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be at least 1")
        if min(self.base_delay, self.max_delay, self.default_rate_limit_delay) < 0:
            raise ValueError("retry delays cannot be negative")

    def allows_retry(self, method: str, body: Mapping[str, Any] | None) -> bool:
        """Return whether repeating a request cannot create duplicate effects."""
        normalized = method.upper()
        if normalized in {"GET", "HEAD", "OPTIONS", "PUT", "DELETE"}:
            return True
        if body is None:
            return False
        key = body.get("idempotency_key")
        return isinstance(key, str) and bool(key)

    def backoff_delay(self, failed_attempt: int) -> float:
        """Return capped exponential backoff after a one-based failed attempt."""
        delay = self.base_delay * (2.0 ** max(failed_attempt - 1, 0))
        return min(delay, self.max_delay)

    def rate_limit_delay(self, headers: Mapping[str, str], *, now: float) -> float:
        """Interpret Time's reset header as relative seconds or an epoch value."""
        raw = next(
            (
                value
                for name, value in headers.items()
                if name.lower() == "x-ratelimit-reset"
            ),
            None,
        )
        try:
            reset = float(raw) if raw is not None else -1
        except ValueError:
            reset = -1
        if reset <= 0:
            return min(self.default_rate_limit_delay, self.max_delay)
        delay = reset - now if reset > now else reset
        return min(max(delay, 0), self.max_delay)
