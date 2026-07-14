from __future__ import annotations

import json

import httpx
import pytest

from aiotimebot.client import TimeClient
from aiotimebot.errors import APIError

from .conftest import post_payload


async def test_send_message_is_authenticated_typed_and_idempotent() -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(201, json=post_payload(), request=request)

    client = TimeClient(
        base_url="https://time.example/api/v4",
        token="secret",
        transport=httpx.MockTransport(respond),
        idempotency_key_factory=lambda: "generated-key",
    )

    async with client:
        post = await client.send_message(channel_id="channel-1", text="hello")

    assert post.id == "post-1"
    assert post.message == "hello"
    assert len(requests) == 1
    request = requests[0]
    assert request.url == httpx.URL("https://time.example/api/v4/posts")
    assert request.headers["Authorization"] == "Bearer secret"
    assert json.loads(request.content) == {
        "channel_id": "channel-1",
        "idempotency_key": "generated-key",
        "message": "hello",
    }


@pytest.mark.parametrize(
    "arguments",
    [
        {"text": "hello"},
        {"text": "hello", "channel_id": "channel", "peer": "@alice"},
    ],
)
async def test_send_message_requires_exactly_one_target(
    arguments: dict[str, str],
) -> None:
    client = TimeClient("https://time.example", "secret")

    with pytest.raises(ValueError, match="exactly one"):
        await client.send_message(**arguments)  # type: ignore[arg-type]


async def test_send_message_rejects_more_than_five_files_without_network() -> None:
    called = False

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal called
        called = True
        return httpx.Response(500, request=request)

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    with pytest.raises(ValueError, match="5"):
        await client.send_message(
            channel_id="channel", text="hello", file_ids=[str(i) for i in range(6)]
        )

    assert not called


async def test_api_error_is_not_returned_as_a_successful_model() -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            400,
            headers={"X-Request-Id": "request-id"},
            json={
                "id": "api.context.invalid_param.app_error",
                "message": "invalid channel",
                "detailed_error": "",
                "request_id": "request-id",
                "status_code": 400,
            },
            request=request,
        )

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    async with client:
        with pytest.raises(APIError) as captured:
            await client.send_message(channel_id="missing", text="hello")

    assert captured.value.status_code == 400
    assert captured.value.error_id == "api.context.invalid_param.app_error"
    assert captured.value.request_id == "request-id"
    assert "invalid channel" in str(captured.value)


async def test_raw_request_preserves_forward_compatible_response_data() -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={"known": 1, "future": {"value": True}},
            request=request,
        )

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    async with client:
        response = await client.raw_request("GET", "/api/v4/future-endpoint")

    assert response == {"known": 1, "future": {"value": True}}


async def test_undocumented_error_is_normalized_to_public_api_error() -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            503,
            headers={"X-Request-Id": "request-id"},
            json={"message": "temporarily unavailable"},
            request=request,
        )

    client = TimeClient(
        "https://time.example",
        "secret",
        transport=httpx.MockTransport(respond),
        retry_policy=None,
    )

    async with client:
        with pytest.raises(APIError) as captured:
            await client.send_message(channel_id="channel", text="hello")

    assert captured.value.status_code == 503
    assert captured.value.request_id == "request-id"
    assert "temporarily unavailable" in str(captured.value)
