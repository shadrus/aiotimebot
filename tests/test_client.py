from __future__ import annotations

import json
import re

import httpx
import pytest

from aiotimebot.client import TimeClient
from aiotimebot.errors import APIError

from .conftest import post_payload


@pytest.mark.parametrize("base_url", ["time.example", "ftp://time.example", ""])
def test_client_requires_absolute_http_url(base_url: str) -> None:
    with pytest.raises(ValueError, match="absolute HTTP"):
        TimeClient(base_url, "secret")


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


async def test_send_message_accepts_null_participants_in_time_response() -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            201,
            json=post_payload(extra={"participants": None}),
            request=request,
        )

    client = TimeClient(
        base_url="https://time.example",
        token="secret",
        transport=httpx.MockTransport(respond),
    )

    async with client:
        post = await client.send_message(
            channel_id="channel-1",
            text="hello",
            idempotency_key="test-key",
        )

    assert post.participants is None


async def test_default_idempotency_keys_follow_time_server_format() -> None:
    requests: list[httpx.Request] = []
    created_posts = 0

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal created_posts
        requests.append(request)
        if request.method == "GET" and request.url.path == "/api/v4/users/me":
            return httpx.Response(200, json={"id": "user-1"}, request=request)
        created_posts += 1
        body = json.loads(request.content)
        return httpx.Response(
            201,
            json=post_payload(
                post_id=f"post-{created_posts}",
                extra={"idempotency_key": body["idempotency_key"]},
            ),
            request=request,
        )

    client = TimeClient(
        "https://time.example",
        "secret",
        transport=httpx.MockTransport(respond),
    )

    async with client:
        first = await client.send_message(channel_id="channel-1", text="first")
        second = await client.send_message(channel_id="channel-1", text="second")

    assert [request.method for request in requests] == ["GET", "POST", "POST"]
    assert re.fullmatch(r"user-1:\d{13}", first.idempotency_key)
    assert re.fullmatch(r"user-1:\d{13}", second.idempotency_key)
    first_timestamp = int(first.idempotency_key.rpartition(":")[2])
    second_timestamp = int(second.idempotency_key.rpartition(":")[2])
    assert second_timestamp > first_timestamp


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
            await client.send_message(
                channel_id="missing",
                text="hello",
                idempotency_key="test-key",
            )

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
            await client.send_message(
                channel_id="channel",
                text="hello",
                idempotency_key="test-key",
            )

    assert captured.value.status_code == 503
    assert captured.value.request_id == "request-id"
    assert "temporarily unavailable" in str(captured.value)


@pytest.mark.parametrize(
    ("content", "expected"),
    [
        (b"not-json", "non-JSON post response"),
        (b"[]", "invalid post response"),
    ],
)
async def test_send_message_rejects_invalid_success_payload(
    content: bytes, expected: str
) -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(201, content=content, request=request)

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    async with client:
        with pytest.raises(APIError, match=expected):
            await client.send_message(
                channel_id="channel", text="hello", idempotency_key="request-1"
            )


@pytest.mark.parametrize("payload", [b"not-json", b"[]", b"{}"])
async def test_default_idempotency_rejects_invalid_current_user(
    payload: bytes,
) -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, content=payload, request=request)

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    async with client:
        with pytest.raises(APIError, match="current user response"):
            await client.send_message(channel_id="channel", text="hello")


async def test_default_idempotency_surfaces_current_user_api_error() -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(401, text="unauthorized", request=request)

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    async with client:
        with pytest.raises(APIError) as captured:
            await client.send_message(channel_id="channel", text="hello")

    assert captured.value.status_code == 401


async def test_raw_request_supports_empty_text_and_json_body() -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if len(requests) == 1:
            return httpx.Response(204, request=request)
        return httpx.Response(200, text="plain response", request=request)

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    async with client:
        empty = await client.raw_request("DELETE", "/api/v4/future")
        text = await client.raw_request(
            "POST", "/api/v4/future", json_body={"value": True}
        )

    assert empty is None
    assert text == "plain response"
    assert json.loads(requests[1].content) == {"value": True}


async def test_raw_request_normalizes_non_object_error_payload() -> None:
    def respond(request: httpx.Request) -> httpx.Response:
        return httpx.Response(400, json=["error"], request=request)

    client = TimeClient(
        "https://time.example", "secret", transport=httpx.MockTransport(respond)
    )

    async with client:
        with pytest.raises(APIError, match="Bad Request") as captured:
            await client.raw_request("GET", "/api/v4/future")

    assert captured.value.error_id is None


async def test_client_can_be_closed_explicitly() -> None:
    client = TimeClient("https://time.example", "secret")

    await client.aclose()
