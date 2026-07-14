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
