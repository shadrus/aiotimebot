from __future__ import annotations

import json

import httpx

from aiotimebot import Application, HandlerContext, PostedEvent, Router, TimeClient
from aiotimebot.events import parse_event

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
