from __future__ import annotations

import asyncio
import json
from collections.abc import AsyncIterator

import httpx
import pytest

from aiotimebot import Application, HandlerContext, PostedEvent, Router, TimeClient
from aiotimebot.events import TimeEvent, parse_event

from .conftest import post_payload


async def test_application_feeds_event_through_router_with_client_context() -> None:
    client = TimeClient(
        "https://time.example",
        "secret",
        transport=httpx.MockTransport(
            lambda request: httpx.Response(500, request=request)
        ),
    )
    router = Router()
    handled: list[str] = []

    @router.command("ping")
    async def ping(event: PostedEvent, context: HandlerContext) -> None:
        assert context.client is client
        handled.append(event.post.id)

    event = parse_event(
        {
            "event": "posted",
            "data": {"post": json.dumps(post_payload(message="/ping"))},
            "broadcast": {"channel_id": "channel-1"},
            "seq": 1,
        }
    )

    async with Application(client, router=router) as application:
        await application.feed_event(event)
        await application.join()

    assert handled == ["post-1"]


async def test_application_shutdown_timeout_cancels_slow_handlers() -> None:
    client = TimeClient(
        "https://time.example",
        "secret",
        transport=httpx.MockTransport(
            lambda request: httpx.Response(500, request=request)
        ),
    )
    router = Router()
    started = asyncio.Event()
    cancelled = asyncio.Event()

    @router.command("slow")
    async def slow(event: PostedEvent, context: HandlerContext) -> None:
        started.set()
        try:
            await asyncio.Event().wait()
        finally:
            cancelled.set()

    event = parse_event(
        {
            "event": "posted",
            "data": {"post": json.dumps(post_payload(message="/slow"))},
            "broadcast": {"channel_id": "channel-1"},
            "seq": 1,
        }
    )

    async with Application(
        client,
        router=router,
        shutdown_timeout=0.01,
    ) as application:
        await application.feed_event(event)
        await started.wait()

    assert cancelled.is_set()


def test_application_rejects_negative_shutdown_timeout() -> None:
    client = TimeClient("https://time.example", "secret")

    with pytest.raises(ValueError, match="shutdown timeout"):
        Application(client, shutdown_timeout=-1)


async def test_application_run_consumes_finite_event_source() -> None:
    client = TimeClient(
        "https://time.example",
        "secret",
        transport=httpx.MockTransport(
            lambda request: httpx.Response(500, request=request)
        ),
    )
    feature = Router()
    handled: list[str] = []

    @feature.command("ping")
    async def ping(event: PostedEvent, context: HandlerContext) -> None:
        handled.append(event.post.id)

    event = parse_event(
        {
            "event": "posted",
            "data": {"post": json.dumps(post_payload(message="/ping"))},
            "broadcast": {"channel_id": "channel-1"},
            "seq": 1,
        }
    )

    class FiniteSource:
        async def events(self) -> AsyncIterator[TimeEvent]:
            yield event

    async with Application(client, event_source=FiniteSource()) as application:
        assert application.include_router(feature) is feature
        await application.run()
        await application.join()

    assert handled == ["post-1"]


async def test_application_surfaces_handler_error() -> None:
    client = TimeClient("https://time.example", "secret")
    router = Router()

    @router.on()
    async def fail(event: TimeEvent, context: HandlerContext) -> None:
        raise ValueError("handler failed")

    event = parse_event(
        {
            "event": "future_event",
            "data": {},
            "broadcast": {"channel_id": "channel-1"},
            "seq": 1,
        }
    )

    async with Application(client, router=router) as application:
        await application.feed_event(event)
        with pytest.raises(ValueError, match="handler failed"):
            await application.join()
