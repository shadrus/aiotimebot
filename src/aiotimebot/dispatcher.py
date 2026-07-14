"""Bounded event dispatch with strict per-channel ordering."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from types import TracebackType

from .events import TimeEvent


class OrderedEventDispatcher[EventT: TimeEvent]:
    """Run different ordering keys concurrently without reordering one key."""

    def __init__(
        self,
        handler: Callable[[EventT], Awaitable[None]],
        *,
        max_concurrency: int = 100,
        queue_size: int = 1_000,
        error_handler: Callable[[BaseException, EventT], Awaitable[None]] | None = None,
    ) -> None:
        if max_concurrency < 1 or queue_size < 1:
            raise ValueError("concurrency and queue size must be positive")
        self._handler = handler
        self._error_handler = error_handler
        self._concurrency = asyncio.Semaphore(max_concurrency)
        self._capacity = asyncio.Semaphore(queue_size)
        self._tails: dict[str, asyncio.Task[None]] = {}
        self._tasks: set[asyncio.Task[None]] = set()
        self._started = False
        self._closed = False

    async def __aenter__(self) -> OrderedEventDispatcher[EventT]:
        """Open the dispatcher for submissions."""
        if self._started:
            raise RuntimeError("dispatcher is already started")
        self._started = True
        self._closed = False
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Drain accepted events and close the dispatcher."""
        await self.aclose()

    async def submit(self, event: EventT) -> None:
        """Accept an event, applying backpressure when capacity is exhausted."""
        if not self._started or self._closed:
            raise RuntimeError("dispatcher is closed")
        await self._capacity.acquire()
        predecessor = self._tails.get(event.ordering_key)

        async def run() -> None:
            if predecessor is not None:
                await predecessor
            async with self._concurrency:
                try:
                    await self._handler(event)
                except asyncio.CancelledError:
                    raise
                except BaseException as error:
                    if self._error_handler is None:
                        raise
                    await self._error_handler(error, event)

        task = asyncio.create_task(run(), name=f"aiotimebot:{event.ordering_key}")
        self._tasks.add(task)
        self._tails[event.ordering_key] = task

        def completed(finished: asyncio.Task[None]) -> None:
            self._tasks.discard(finished)
            if self._tails.get(event.ordering_key) is finished:
                self._tails.pop(event.ordering_key, None)
            self._capacity.release()

        task.add_done_callback(completed)

    async def join(self) -> None:
        """Wait until every accepted event has finished processing."""
        while self._tasks:
            await asyncio.gather(*tuple(self._tasks))

    async def aclose(self) -> None:
        """Reject new submissions and drain all accepted events."""
        if self._closed:
            return
        self._closed = True
        await self.join()
