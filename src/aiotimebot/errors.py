"""Public exception hierarchy for aiotimebot."""

from __future__ import annotations


class AioTimeBotError(Exception):
    """Base class for all library-specific failures."""


class APIError(AioTimeBotError):
    """A structured error returned by the Time REST API."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        error_id: str | None = None,
        request_id: str | None = None,
        detailed_error: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.error_id = error_id
        self.request_id = request_id
        self.detailed_error = detailed_error


class RateLimited(APIError):
    """The server rejected a request because its rate limit was exhausted."""

    def __init__(self, message: str, *, retry_after: float) -> None:
        super().__init__(message, status_code=429)
        self.retry_after = retry_after


class WebSocketError(AioTimeBotError):
    """Base class for Time WebSocket failures."""


class WebSocketProtocolError(WebSocketError):
    """A WebSocket frame violated the documented Time protocol."""


class WebSocketAuthenticationError(WebSocketError):
    """Time rejected the WebSocket authentication challenge."""
