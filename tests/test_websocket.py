from __future__ import annotations

import json

import pytest

from aiotimebot.errors import WebSocketAuthenticationError, WebSocketProtocolError
from aiotimebot.websocket import (
    WebSocketAuthenticator,
    build_websocket_url,
)


class FakeSocket:
    def __init__(self, incoming: list[str]) -> None:
        self.incoming = iter(incoming)
        self.sent: list[str] = []

    async def send(self, data: str) -> None:
        self.sent.append(data)

    async def recv(self) -> str:
        return next(self.incoming)


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


async def test_authentication_challenge_uses_sequence_and_checks_reply() -> None:
    socket = FakeSocket([json.dumps({"status": "OK", "seq_reply": 41})])
    authenticator = WebSocketAuthenticator(token="secret", initial_sequence=41)

    next_sequence = await authenticator.authenticate(socket)

    assert json.loads(socket.sent[0]) == {
        "seq": 41,
        "action": "authentication_challenge",
        "data": {"token": "secret"},
    }
    assert next_sequence == 42


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
