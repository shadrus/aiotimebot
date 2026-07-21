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


@pytest.mark.parametrize(
    ("max_concurrency", "queue_size"),
    [(0, 1), (1, 0)],
)
def test_dispatcher_requires_positive_limits(
    max_concurrency: int, queue_size: int
) -> None:
    async def handler(item: RawEvent) -> None:
        return None

    with pytest.raises(ValueError, match="positive"):
        OrderedEventDispatcher(
            handler,
            max_concurrency=max_concurrency,
            queue_size=queue_size,
        )


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


async def test_raised_handler_error_is_surfaced_after_channel_drains() -> None:
    handled: list[int] = []

    async def handler(item: RawEvent) -> None:
        if item.seq == 1:
            raise ValueError("broken event")
        handled.append(item.seq)

    async def raise_error(error: BaseException, item: RawEvent) -> None:
        raise error

    async with OrderedEventDispatcher(
        handler, max_concurrency=2, error_handler=raise_error
    ) as dispatcher:
        await dispatcher.submit(event("same", 1))
        await dispatcher.submit(event("same", 2))
        with pytest.raises(ValueError, match="broken event"):
            await dispatcher.join()

    assert handled == [2]


async def test_submit_after_close_is_rejected() -> None:
    async def handler(item: RawEvent) -> None:
        return None

    dispatcher = OrderedEventDispatcher(handler)
    await dispatcher.__aenter__()
    await dispatcher.aclose()

    with pytest.raises(RuntimeError, match="closed"):
        await dispatcher.submit(event("one", 1))

    await dispatcher.aclose()


async def test_dispatcher_rejects_second_start_and_negative_close_timeout() -> None:
    async def handler(item: RawEvent) -> None:
        return None

    dispatcher = OrderedEventDispatcher(handler)
    await dispatcher.__aenter__()

    with pytest.raises(RuntimeError, match="already started"):
        await dispatcher.__aenter__()
    with pytest.raises(ValueError, match="shutdown timeout"):
        await dispatcher.aclose(drain_timeout=-1)

    await dispatcher.aclose()


async def test_queue_capacity_applies_backpressure() -> None:
    started = asyncio.Event()
    release = asyncio.Event()

    async def handler(item: RawEvent) -> None:
        started.set()
        await release.wait()

    async with OrderedEventDispatcher(handler, queue_size=1) as dispatcher:
        await dispatcher.submit(event("one", 1))
        await started.wait()

        blocked_submit = asyncio.create_task(dispatcher.submit(event("two", 2)))
        await asyncio.sleep(0)
        assert not blocked_submit.done()

        release.set()
        await asyncio.wait_for(blocked_submit, timeout=1)


async def test_close_rejects_submit_waiting_for_capacity() -> None:
    started = asyncio.Event()
    release = asyncio.Event()

    async def handler(item: RawEvent) -> None:
        started.set()
        await release.wait()

    dispatcher = OrderedEventDispatcher(handler, queue_size=1)
    await dispatcher.__aenter__()
    await dispatcher.submit(event("one", 1))
    await started.wait()

    blocked_submit = asyncio.create_task(dispatcher.submit(event("two", 2)))
    await asyncio.sleep(0)
    close = asyncio.create_task(dispatcher.aclose())
    await asyncio.sleep(0)
    release.set()

    with pytest.raises(RuntimeError, match="closed"):
        await blocked_submit
    await close


async def test_close_timeout_cancels_and_awaits_remaining_handlers() -> None:
    started = asyncio.Event()
    cancelled = asyncio.Event()

    async def handler(item: RawEvent) -> None:
        started.set()
        try:
            await asyncio.Event().wait()
        finally:
            cancelled.set()

    dispatcher = OrderedEventDispatcher(handler)
    await dispatcher.__aenter__()
    await dispatcher.submit(event("one", 1))
    await started.wait()

    await dispatcher.aclose(drain_timeout=0.01)

    assert cancelled.is_set()
    with pytest.raises(RuntimeError, match="closed"):
        await dispatcher.submit(event("two", 2))


async def test_cancellation_during_close_cleans_up_and_propagates() -> None:
    started = asyncio.Event()
    cancelled = asyncio.Event()

    async def handler(item: RawEvent) -> None:
        started.set()
        try:
            await asyncio.Event().wait()
        finally:
            cancelled.set()

    dispatcher = OrderedEventDispatcher(handler)
    await dispatcher.__aenter__()
    await dispatcher.submit(event("one", 1))
    await started.wait()

    close = asyncio.create_task(dispatcher.aclose())
    await asyncio.sleep(0)
    close.cancel()

    with pytest.raises(asyncio.CancelledError):
        await close
    assert cancelled.is_set()
