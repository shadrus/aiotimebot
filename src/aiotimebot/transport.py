"""HTTPX transport middleware implementing Time-aware retries."""

from __future__ import annotations

import asyncio
import json
import time
from collections.abc import Awaitable, Callable, Mapping
from typing import Any

import httpx

from .retry import RetryPolicy

Sleep = Callable[[float], Awaitable[None]]
Clock = Callable[[], float]


class RetryingAsyncTransport(httpx.AsyncBaseTransport):
    """Retry transient failures only when the request is safe to repeat."""

    def __init__(
        self,
        transport: httpx.AsyncBaseTransport,
        *,
        policy: RetryPolicy | None = None,
        sleep: Sleep = asyncio.sleep,
        clock: Clock = time.time,
    ) -> None:
        self._transport = transport
        self._policy = policy or RetryPolicy()
        self._sleep = sleep
        self._clock = clock

    @staticmethod
    def _body(request: httpx.Request) -> Mapping[str, Any] | None:
        try:
            decoded = json.loads(request.content)
        except (httpx.RequestNotRead, UnicodeDecodeError, json.JSONDecodeError):
            return None
        return decoded if isinstance(decoded, Mapping) else None

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        """Send a request with bounded connect and HTTP 429 retries."""
        can_retry = self._policy.allows_retry(request.method, self._body(request))
        for attempt in range(1, self._policy.max_attempts + 1):
            try:
                response = await self._transport.handle_async_request(request)
            except (httpx.ConnectError, httpx.ConnectTimeout):
                if not can_retry or attempt == self._policy.max_attempts:
                    raise
                await self._sleep(self._policy.backoff_delay(attempt))
                continue

            if (
                response.status_code != 429
                or not can_retry
                or attempt == self._policy.max_attempts
            ):
                return response
            delay = self._policy.rate_limit_delay(response.headers, now=self._clock())
            await response.aclose()
            await self._sleep(delay)
        raise AssertionError("retry loop exhausted without returning")

    async def aclose(self) -> None:
        """Close the wrapped connection pool."""
        await self._transport.aclose()
