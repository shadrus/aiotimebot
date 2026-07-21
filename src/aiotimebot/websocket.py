"""Time WebSocket authentication and event streaming."""

from __future__ import annotations

import json
from collections.abc import AsyncIterator, Mapping
from dataclasses import dataclass
from typing import Any, Protocol, cast
from urllib.parse import urlsplit, urlunsplit

from websockets.asyncio.client import connect

from .errors import WebSocketAuthenticationError, WebSocketProtocolError
from .events import TimeEvent, parse_event


class WebSocketLike(Protocol):
    """Minimal socket contract needed for Time authentication."""

    async def send(self, data: str) -> None:
        """Send one text frame."""
        ...

    async def recv(self) -> str | bytes:
        """Receive one frame."""
        ...


@dataclass(frozen=True, slots=True)
class AuthenticationResult:
    """Successful handshake state and events received before its response."""

    next_sequence: int
    pending_events: tuple[TimeEvent, ...]


def build_websocket_url(base_url: str) -> str:
    """Build Time's WebSocket endpoint from a server or API base URL."""
    parsed = urlsplit(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("base_url must be an absolute HTTP or HTTPS URL")
    scheme = "wss" if parsed.scheme == "https" else "ws"
    path = parsed.path.rstrip("/")
    if path.endswith("/api/v4"):
        path = path[: -len("/api/v4")]
    return urlunsplit((scheme, parsed.netloc, f"{path}/api/v4/websocket", "", ""))


@dataclass(frozen=True, slots=True)
class WebSocketAuthenticator:
    """Perform Time's documented authentication challenge exchange."""

    token: str
    initial_sequence: int = 1

    async def authenticate(self, socket: WebSocketLike) -> AuthenticationResult:
        """Authenticate a socket while preserving events sent before the reply."""
        sequence = self.initial_sequence
        await socket.send(
            json.dumps(
                {
                    "seq": sequence,
                    "action": "authentication_challenge",
                    "data": {"token": self.token},
                },
                separators=(",", ":"),
            )
        )
        pending_events: list[TimeEvent] = []
        while True:
            raw_reply = await socket.recv()
            try:
                decoded = json.loads(
                    raw_reply.decode() if isinstance(raw_reply, bytes) else raw_reply
                )
            except (UnicodeDecodeError, json.JSONDecodeError) as error:
                raise WebSocketProtocolError(
                    "invalid authentication response"
                ) from error
            if not isinstance(decoded, Mapping):
                raise WebSocketProtocolError(
                    "authentication response must be an object"
                )
            if "event" in decoded:
                pending_events.append(parse_event(cast(Mapping[str, Any], decoded)))
                continue
            if "seq_reply" not in decoded:
                raise WebSocketProtocolError(
                    "unexpected message while awaiting authentication response"
                )
            if decoded.get("seq_reply") != sequence:
                raise WebSocketProtocolError(
                    "authentication response sequence mismatch"
                )
            if decoded.get("status") != "OK":
                error_payload = decoded.get("error")
                message = (
                    str(error_payload.get("message", "authentication failed"))
                    if isinstance(error_payload, Mapping)
                    else "authentication failed"
                )
                raise WebSocketAuthenticationError(message)
            return AuthenticationResult(
                next_sequence=sequence + 1,
                pending_events=tuple(pending_events),
            )


class WebSocketEventSource:
    """Reconnect to Time and yield authenticated WebSocket events."""

    def __init__(self, base_url: str, token: str) -> None:
        self._url = build_websocket_url(base_url)
        self._authenticator = WebSocketAuthenticator(token)

    async def events(self) -> AsyncIterator[TimeEvent]:
        """Yield events indefinitely, using websockets' reconnect backoff."""
        async for socket in connect(self._url):
            authentication = await self._authenticator.authenticate(
                cast(WebSocketLike, socket)
            )
            for event in authentication.pending_events:
                yield event
            async for raw_message in socket:
                text = (
                    raw_message.decode()
                    if isinstance(raw_message, bytes)
                    else raw_message
                )
                try:
                    payload = json.loads(text)
                except json.JSONDecodeError as error:
                    raise WebSocketProtocolError("invalid event JSON") from error
                if not isinstance(payload, Mapping) or "event" not in payload:
                    continue
                yield parse_event(cast(Mapping[str, Any], payload))
