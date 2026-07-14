from __future__ import annotations

import asyncio

import pytest

from aiotimebot.dispatcher import OrderedEventDispatcher
from aiotimebot.events import RawEvent, parse_event


def event(channel_id: str, seq: int) -> RawEvent:
    parsed = parse_event(
        {
            "event": "future_event",
            "data": {"value": seq},
            "broadcast": {"channel_id": channel_id},
            "seq": seq,
        }
    )
    assert isinstance(parsed, RawEvent)
    return parsed


async def test_events_in_one_channel_are_sequential_and_ordered() -> None:
    active = 0
    max_active = 0
    handled: list[int] = []

    async def handler(item: RawEvent) -> None:
        nonlocal active, max_active
        active += 1
        max_active = max(max_active, active)
        await asyncio.sleep(0)
        handled.append(item.seq)
        active -= 1

    async with OrderedEventDispatcher(handler, max_concurrency=8) as dispatcher:
        for seq in range(10):
            await dispatcher.submit(event("same", seq))
        await dispatcher.join()

    assert handled == list(range(10))
    assert max_active == 1


async def test_different_channels_run_concurrently_up_to_global_limit() -> None:
    both_started = asyncio.Event()
    release = asyncio.Event()
    active = 0
    max_active = 0

    async def handler(item: RawEvent) -> None:
        nonlocal active, max_active
        active += 1
        max_active = max(max_active, active)
        if active == 2:
            both_started.set()
        await release.wait()
        active -= 1

    async with OrderedEventDispatcher(handler, max_concurrency=2) as dispatcher:
        await dispatcher.submit(event("one", 1))
        await dispatcher.submit(event("two", 2))
        await asyncio.wait_for(both_started.wait(), timeout=1)
        release.set()
        await dispatcher.join()

    assert max_active == 2


async def test_handler_failure_is_reported_and_does_not_block_channel() -> None:
    errors: list[BaseException] = []
    handled: list[int] = []

    async def handler(item: RawEvent) -> None:
        if item.seq == 1:
            raise ValueError("broken event")
        handled.append(item.seq)

    async def on_error(error: BaseException, item: RawEvent) -> None:
        errors.append(error)

    async with OrderedEventDispatcher(
        handler, max_concurrency=2, error_handler=on_error
    ) as dispatcher:
        await dispatcher.submit(event("same", 1))
        await dispatcher.submit(event("same", 2))
        await dispatcher.join()

    assert handled == [2]
    assert len(errors) == 1
    assert isinstance(errors[0], ValueError)


async def test_submit_after_close_is_rejected() -> None:
    async def handler(item: RawEvent) -> None:
        return None

    dispatcher = OrderedEventDispatcher(handler)
    await dispatcher.__aenter__()
    await dispatcher.aclose()

    with pytest.raises(RuntimeError, match="closed"):
        await dispatcher.submit(event("one", 1))
