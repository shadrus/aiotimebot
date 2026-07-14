from __future__ import annotations

import json

import pytest

from aiotimebot.context import HandlerContext
from aiotimebot.events import PostedEvent, parse_event
from aiotimebot.filters import Command
from aiotimebot.routing import Propagation, Router
from aiotimebot.storage import MemoryStateStorage

from .conftest import post_payload


def posted(message: str = "/ping") -> PostedEvent:
    event = parse_event(
        {
            "event": "posted",
            "data": {"post": json.dumps(post_payload(message=message))},
            "broadcast": {"channel_id": "channel-1"},
            "seq": 1,
        }
    )
    assert isinstance(event, PostedEvent)
    return event


@pytest.mark.parametrize(
    ("text", "expected_arguments"),
    [
        ("/deploy", ()),
        ("  /deploy production", ("production",)),
        ('/deploy production "release candidate"', ("production", "release candidate")),
        ("/DEPLOY production", None),
        ("/deployment production", None),
        ('/deploy "unterminated', None),
        ("ordinary message", None),
    ],
)
def test_command_filter_has_strict_shell_like_parsing(
    text: str, expected_arguments: tuple[str, ...] | None
) -> None:
    match = Command("deploy").match(posted(text))

    if expected_arguments is None:
        assert match is None
    else:
        assert match is not None
        assert match.arguments == expected_arguments


async def test_router_dispatches_typed_command_and_stops_propagation() -> None:
    router = Router()
    calls: list[str] = []

    @router.command("ping")
    async def command_handler(
        event: PostedEvent, context: HandlerContext
    ) -> Propagation:
        assert context.command is not None
        calls.append(f"command:{','.join(context.command.arguments)}")
        return Propagation.STOP

    @router.on()
    async def fallback_handler(event: object, context: HandlerContext) -> None:
        calls.append("fallback")

    context = HandlerContext(client=None, storage=MemoryStateStorage())
    result = await router.dispatch(posted("/ping one two"), context)

    assert result is Propagation.STOP
    assert calls == ["command:one,two"]


async def test_router_supports_direct_registration_and_nested_routers() -> None:
    root = Router()
    feature = Router()
    calls: list[str] = []

    async def handler(event: object, context: HandlerContext) -> None:
        calls.append("nested")

    feature.register(handler, Command("ping"))
    root.include_router(feature)

    await root.dispatch(
        posted("/ping"),
        HandlerContext(client=None, storage=MemoryStateStorage()),
    )

    assert calls == ["nested"]


async def test_router_middleware_wraps_handler_in_registration_order() -> None:
    router = Router()
    calls: list[str] = []

    async def outer(
        event: object, context: HandlerContext, call_next: object
    ) -> object:
        calls.append("outer:before")
        result = await call_next(event, context)  # type: ignore[operator]
        calls.append("outer:after")
        return result

    async def inner(
        event: object, context: HandlerContext, call_next: object
    ) -> object:
        calls.append("inner:before")
        result = await call_next(event, context)  # type: ignore[operator]
        calls.append("inner:after")
        return result

    router.use(outer)
    router.use(inner)

    @router.on()
    async def handler(event: object, context: HandlerContext) -> None:
        calls.append("handler")

    await router.dispatch(
        posted(), HandlerContext(client=None, storage=MemoryStateStorage())
    )

    assert calls == [
        "outer:before",
        "inner:before",
        "handler",
        "inner:after",
        "outer:after",
    ]
