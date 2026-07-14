"""Ergonomic async facade over the complete generated Time REST client."""

from __future__ import annotations

import json
from collections.abc import Callable, Mapping, Sequence
from types import TracebackType
from typing import Any, cast
from urllib.parse import urlsplit, urlunsplit
from uuid import uuid4

import httpx

from .api.client import AuthenticatedClient
from .api.models.create_post_body import CreatePostBody
from .api.models.post import Post
from .api.types import UNSET
from .errors import APIError
from .retry import RetryPolicy
from .transport import RetryingAsyncTransport
from .websocket import WebSocketEventSource

type JSONValue = (
    None | bool | int | float | str | list["JSONValue"] | dict[str, "JSONValue"]
)


def _server_root(base_url: str) -> str:
    parsed = urlsplit(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("base_url must be an absolute HTTP or HTTPS URL")
    path = parsed.path.rstrip("/")
    if path.endswith("/api/v4"):
        path = path[: -len("/api/v4")]
    return urlunsplit((parsed.scheme, parsed.netloc, path, "", "")).rstrip("/")


class TimeClient:
    """Own HTTP resources and expose typed bot operations for Time API v4."""

    def __init__(
        self,
        base_url: str,
        token: str,
        *,
        transport: httpx.AsyncBaseTransport | None = None,
        retry_policy: RetryPolicy | None = None,
        timeout: httpx.Timeout | float = 10.0,
        idempotency_key_factory: Callable[[], str] | None = None,
    ) -> None:
        self.base_url = _server_root(base_url)
        self.token = token
        base_transport = transport or httpx.AsyncHTTPTransport()
        retrying_transport = RetryingAsyncTransport(base_transport, policy=retry_policy)
        self._http = httpx.AsyncClient(
            base_url=self.base_url,
            headers={"Authorization": f"Bearer {token}"},
            timeout=timeout,
            transport=retrying_transport,
        )
        self.api = AuthenticatedClient(
            base_url=self.base_url,
            token=token,
            raise_on_unexpected_status=True,
        ).set_async_httpx_client(self._http)
        self._idempotency_key_factory = idempotency_key_factory or (
            lambda: str(uuid4())
        )

    async def __aenter__(self) -> TimeClient:
        """Open the shared HTTP connection pool."""
        await self._http.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Close the shared HTTP connection pool."""
        await self._http.__aexit__(exc_type, exc_value, traceback)

    async def aclose(self) -> None:
        """Close the client explicitly when a context manager is inconvenient."""
        await self._http.aclose()

    def websocket_events(self) -> WebSocketEventSource:
        """Create the authenticated real-time event source for this account."""
        return WebSocketEventSource(self.base_url, self.token)

    async def send_message(
        self,
        text: str,
        *,
        channel_id: str | None = None,
        peer: str | None = None,
        root_id: str | None = None,
        file_ids: Sequence[str] = (),
        idempotency_key: str | None = None,
    ) -> Post:
        """Create a Time post with safe retry semantics and a typed response."""
        if (channel_id is None) == (peer is None):
            raise ValueError("exactly one of channel_id or peer is required")
        if len(file_ids) > 5:
            raise ValueError("Time allows at most 5 files per post")

        body = CreatePostBody(
            message=text,
            idempotency_key=idempotency_key or self._idempotency_key_factory(),
            channel_id=channel_id if channel_id is not None else UNSET,
            peer=peer if peer is not None else UNSET,
            root_id=root_id if root_id is not None else UNSET,
            file_ids=list(file_ids) if file_ids else UNSET,
        )
        response = await self._http.post("/api/v4/posts", json=body.to_dict())
        if response.is_error:
            raise self._error_from_response(response)
        try:
            payload = response.json()
        except json.JSONDecodeError as error:
            raise APIError(
                "Time returned a non-JSON post response",
                status_code=response.status_code,
                request_id=response.headers.get("X-Request-Id"),
            ) from error
        if not isinstance(payload, Mapping):
            raise APIError(
                "Time returned an invalid post response",
                status_code=response.status_code,
                request_id=response.headers.get("X-Request-Id"),
            )
        return Post.from_dict(payload)

    async def raw_request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, object] | None = None,
        json_body: JSONValue = None,
    ) -> JSONValue:
        """Call a future or schema-defective endpoint without discarding JSON."""
        kwargs: dict[str, Any] = {"params": params}
        if json_body is not None:
            kwargs["json"] = json_body
        response = await self._http.request(method, path, **kwargs)
        if response.is_error:
            raise self._error_from_response(response)
        if not response.content:
            return None
        try:
            return cast(JSONValue, response.json())
        except json.JSONDecodeError:
            return response.text

    def _error_from_response(self, response: httpx.Response) -> APIError:
        try:
            payload = response.json()
        except json.JSONDecodeError:
            payload = {}
        if isinstance(payload, Mapping):
            message = str(payload.get("message") or response.reason_phrase)
            error_id = payload.get("id")
            request_id = payload.get("request_id")
            detailed = payload.get("detailed_error")
        else:
            message = response.reason_phrase
            error_id = request_id = detailed = None
        return APIError(
            message,
            status_code=response.status_code,
            error_id=str(error_id) if error_id else None,
            request_id=(
                str(request_id) if request_id else response.headers.get("X-Request-Id")
            ),
            detailed_error=str(detailed) if detailed else None,
        )
