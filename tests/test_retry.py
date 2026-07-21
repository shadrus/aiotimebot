from __future__ import annotations

import httpx
import pytest

from aiotimebot.retry import RetryPolicy
from aiotimebot.transport import RetryingAsyncTransport


@pytest.mark.parametrize("method", ["GET", "HEAD", "OPTIONS", "PUT", "DELETE"])
def test_idempotent_http_methods_can_be_retried(method: str) -> None:
    assert RetryPolicy().allows_retry(method, body=None)


def test_unsafe_request_requires_time_idempotency_key() -> None:
    policy = RetryPolicy()

    assert not policy.allows_retry("POST", body={"message": "hello"})
    assert not policy.allows_retry(
        "POST", body={"message": "hello", "idempotency_key": ""}
    )
    assert policy.allows_retry(
        "POST", body={"message": "hello", "idempotency_key": "request-1"}
    )


def test_rate_limit_reset_supports_relative_seconds_and_epoch_time() -> None:
    policy = RetryPolicy(default_rate_limit_delay=0.5, max_delay=30)

    assert policy.rate_limit_delay({"X-RateLimit-Reset": "3"}, now=1_000) == 3
    assert policy.rate_limit_delay({"X-RateLimit-Reset": "1012"}, now=1_000) == 12


@pytest.mark.parametrize("value", [None, "", "not-a-number", "-10"])
def test_invalid_rate_limit_reset_uses_bounded_default(value: str | None) -> None:
    headers = {} if value is None else {"X-RateLimit-Reset": value}

    assert (
        RetryPolicy(default_rate_limit_delay=0.5).rate_limit_delay(headers, now=1_000)
        == 0.5
    )


async def test_transport_retries_rate_limit_for_idempotent_post() -> None:
    attempts = 0
    delays: list[float] = []

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            return httpx.Response(
                429, headers={"X-RateLimit-Reset": "2"}, request=request
            )
        return httpx.Response(201, json={"ok": True}, request=request)

    async def sleep(delay: float) -> None:
        delays.append(delay)

    transport = RetryingAsyncTransport(
        httpx.MockTransport(respond), sleep=sleep, clock=lambda: 1_000
    )
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.post(
            "https://time.example/api/v4/posts",
            json={"message": "hello", "idempotency_key": "request-1"},
        )

    assert response.status_code == 201
    assert attempts == 2
    assert delays == [2]


async def test_transport_does_not_retry_unsafe_post_without_key() -> None:
    attempts = 0

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(429, request=request)

    transport = RetryingAsyncTransport(httpx.MockTransport(respond))
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.post(
            "https://time.example/api/v4/posts", json={"message": "hello"}
        )

    assert response.status_code == 429
    assert attempts == 1


@pytest.mark.parametrize("status_code", [502, 503, 504])
async def test_transport_retries_transient_server_errors(
    status_code: int,
) -> None:
    attempts = 0
    delays: list[float] = []

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            return httpx.Response(status_code, request=request)
        return httpx.Response(200, json={"ok": True}, request=request)

    async def sleep(delay: float) -> None:
        delays.append(delay)

    transport = RetryingAsyncTransport(
        httpx.MockTransport(respond),
        policy=RetryPolicy(base_delay=0.1),
        sleep=sleep,
    )
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.get("https://time.example/api/v4/users/me")

    assert response.status_code == 200
    assert attempts == 3
    assert delays == [0.1, 0.2]


async def test_transport_retries_transient_error_for_idempotent_post() -> None:
    attempts = 0

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(503 if attempts == 1 else 201, request=request)

    async def sleep(delay: float) -> None:
        return None

    transport = RetryingAsyncTransport(httpx.MockTransport(respond), sleep=sleep)
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.post(
            "https://time.example/api/v4/posts",
            json={"message": "hello", "idempotency_key": "request-1"},
        )

    assert response.status_code == 201
    assert attempts == 2


async def test_transport_does_not_retry_transient_error_for_unsafe_post() -> None:
    attempts = 0

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        return httpx.Response(503, request=request)

    transport = RetryingAsyncTransport(httpx.MockTransport(respond))
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.post(
            "https://time.example/api/v4/posts", json={"message": "hello"}
        )

    assert response.status_code == 503
    assert attempts == 1


async def test_transport_retries_connection_drop_for_safe_request() -> None:
    attempts = 0
    delays: list[float] = []

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise httpx.ReadError("connection reset", request=request)
        return httpx.Response(200, request=request)

    async def sleep(delay: float) -> None:
        delays.append(delay)

    transport = RetryingAsyncTransport(httpx.MockTransport(respond), sleep=sleep)
    async with httpx.AsyncClient(transport=transport) as client:
        response = await client.get("https://time.example/api/v4/users/me")

    assert response.status_code == 200
    assert attempts == 2
    assert delays == [0.25]


async def test_transport_does_not_retry_connection_drop_for_unsafe_post() -> None:
    attempts = 0

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        raise httpx.ReadError("connection reset", request=request)

    transport = RetryingAsyncTransport(httpx.MockTransport(respond))
    async with httpx.AsyncClient(transport=transport) as client:
        with pytest.raises(httpx.ReadError, match="connection reset"):
            await client.post(
                "https://time.example/api/v4/posts", json={"message": "hello"}
            )

    assert attempts == 1


async def test_transport_stops_after_configured_attempt_limit() -> None:
    attempts = 0
    delays: list[float] = []

    def respond(request: httpx.Request) -> httpx.Response:
        nonlocal attempts
        attempts += 1
        raise httpx.ConnectError("offline", request=request)

    async def sleep(delay: float) -> None:
        delays.append(delay)

    transport = RetryingAsyncTransport(
        httpx.MockTransport(respond),
        policy=RetryPolicy(max_attempts=3, base_delay=0.1),
        sleep=sleep,
    )
    async with httpx.AsyncClient(transport=transport) as client:
        with pytest.raises(httpx.ConnectError, match="offline"):
            await client.get("https://time.example/api/v4/users/me")

    assert attempts == 3
    assert delays == [0.1, 0.2]
