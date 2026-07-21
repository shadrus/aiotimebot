from __future__ import annotations

import json

import pytest

from aiotimebot.errors import WebSocketAuthenticationError, WebSocketProtocolError
from aiotimebot.websocket import (
    WebSocketAuthenticator,
    WebSocketEventSource,
    build_websocket_url,
)


class FakeSocket:
    def __init__(self, incoming: list[str | bytes]) -> None:
        self.incoming = iter(incoming)
        self.sent: list[str] = []

    async def send(self, data: str) -> None:
        self.sent.append(data)

    async def recv(self) -> str | bytes:
        return next(self.incoming)

    def __aiter__(self) -> FakeSocket:
        return self

    async def __anext__(self) -> str | bytes:
        try:
            return next(self.incoming)
        except StopIteration as error:
            raise StopAsyncIteration from error


class FakeConnections:
    def __init__(self, sockets: list[FakeSocket]) -> None:
        self.sockets = iter(sockets)

    def __aiter__(self) -> FakeConnections:
        return self

    async def __anext__(self) -> FakeSocket:
        try:
            return next(self.sockets)
        except StopIteration as error:
            raise StopAsyncIteration from error


@pytest.mark.parametrize(
    ("base_url", "expected"),
    [
        ("https://time.example", "wss://time.example/api/v4/websocket"),
        ("http://time.example/", "ws://time.example/api/v4/websocket"),
        (
            "https://time.example/api/v4",
            "wss://time.example/api/v4/websocket",
        ),
    ],
)
def test_websocket_url_is_derived_from_server_url(base_url: str, expected: str) -> None:
    assert build_websocket_url(base_url) == expected


@pytest.mark.parametrize("base_url", ["time.example", "ftp://time.example", ""])
def test_websocket_url_requires_absolute_http_url(base_url: str) -> None:
    with pytest.raises(ValueError, match="absolute HTTP"):
        build_websocket_url(base_url)


async def test_authentication_challenge_uses_sequence_and_checks_reply() -> None:
    socket = FakeSocket([json.dumps({"status": "OK", "seq_reply": 41})])
    authenticator = WebSocketAuthenticator(token="secret", initial_sequence=41)

    result = await authenticator.authenticate(socket)

    assert json.loads(socket.sent[0]) == {
        "seq": 41,
        "action": "authentication_challenge",
        "data": {"token": "secret"},
    }
    assert result.next_sequence == 42
    assert result.pending_events == ()


async def test_authentication_failure_is_typed() -> None:
    socket = FakeSocket(
        [
            json.dumps(
                {
                    "status": "FAIL",
                    "seq_reply": 1,
                    "error": {"id": "auth.failed", "message": "bad token"},
                }
            )
        ]
    )

    with pytest.raises(WebSocketAuthenticationError, match="bad token"):
        await WebSocketAuthenticator("secret").authenticate(socket)


async def test_mismatched_authentication_sequence_is_protocol_error() -> None:
    socket = FakeSocket([json.dumps({"status": "OK", "seq_reply": 99})])

    with pytest.raises(WebSocketProtocolError, match="sequence"):
        await WebSocketAuthenticator("secret").authenticate(socket)


async def test_event_before_authentication_response_is_preserved(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    hello = {
        "event": "hello",
        "data": {"server_version": "7.8.0"},
        "broadcast": {"user_id": "user-id"},
        "seq": 0,
    }
    typing = {
        "event": "typing",
        "data": {"user_id": "other-user"},
        "broadcast": {"channel_id": "channel-id"},
        "seq": 1,
    }
    socket = FakeSocket(
        [
            json.dumps(hello),
            json.dumps({"status": "OK", "seq_reply": 1}),
            json.dumps(typing),
        ]
    )
    monkeypatch.setattr(
        "aiotimebot.websocket.connect",
        lambda _url: FakeConnections([socket]),
    )
    events = WebSocketEventSource("https://time.example", "secret").events()

    first = await anext(events)
    second = await anext(events)
    await events.aclose()

    assert first.raw == hello
    assert second.raw == typing


async def test_authentication_failure_after_early_event_is_typed() -> None:
    socket = FakeSocket(
        [
            json.dumps({"event": "hello", "data": {}, "seq": 0}),
            json.dumps(
                {
                    "status": "FAIL",
                    "seq_reply": 1,
                    "error": {"message": "invalid token"},
                }
            ),
        ]
    )

    with pytest.raises(WebSocketAuthenticationError, match="invalid token"):
        await WebSocketAuthenticator("secret").authenticate(socket)


async def test_unexpected_message_during_authentication_is_protocol_error() -> None:
    socket = FakeSocket([json.dumps({"status": "OK"})])

    with pytest.raises(WebSocketProtocolError, match="unexpected message"):
        await WebSocketAuthenticator("secret").authenticate(socket)


@pytest.mark.parametrize("payload", [b"\xff", json.dumps([])])
async def test_invalid_authentication_payload_is_protocol_error(
    payload: str | bytes,
) -> None:
    socket = FakeSocket([payload])

    with pytest.raises(WebSocketProtocolError, match="authentication response"):
        await WebSocketAuthenticator("secret").authenticate(socket)


async def test_event_source_ignores_non_events_and_rejects_invalid_json(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    socket = FakeSocket(
        [
            json.dumps({"status": "OK", "seq_reply": 1}),
            json.dumps({"status": "ignored"}),
            "not-json",
        ]
    )
    monkeypatch.setattr(
        "aiotimebot.websocket.connect",
        lambda _url: FakeConnections([socket]),
    )
    events = WebSocketEventSource("https://time.example", "secret").events()

    with pytest.raises(WebSocketProtocolError, match="invalid event JSON"):
        await anext(events)
    await events.aclose()


async def test_event_source_reauthenticates_after_connection_closes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    first_hello = {"event": "hello", "data": {"connection_id": "first"}, "seq": 0}
    first_event = {"event": "typing", "data": {}, "seq": 1}
    second_hello = {
        "event": "hello",
        "data": {"connection_id": "second"},
        "seq": 0,
    }
    second_event = {"event": "status_change", "data": {}, "seq": 1}
    sockets = [
        FakeSocket(
            [
                json.dumps(first_hello),
                json.dumps({"status": "OK", "seq_reply": 1}),
                json.dumps(first_event),
            ]
        ),
        FakeSocket(
            [
                json.dumps(second_hello),
                json.dumps({"status": "OK", "seq_reply": 1}),
                json.dumps(second_event),
            ]
        ),
    ]
    monkeypatch.setattr(
        "aiotimebot.websocket.connect",
        lambda _url: FakeConnections(sockets),
    )
    events = WebSocketEventSource("https://time.example", "secret").events()

    received = [await anext(events) for _ in range(4)]
    await events.aclose()

    assert [event.raw for event in received] == [
        first_hello,
        first_event,
        second_hello,
        second_event,
    ]
    assert all(len(socket.sent) == 1 for socket in sockets)
