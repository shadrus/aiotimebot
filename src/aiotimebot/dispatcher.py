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
        self._errors: list[BaseException] = []
        self._close_lock = asyncio.Lock()
        self._started = False
        self._closed = False

    async def __aenter__(self) -> OrderedEventDispatcher[EventT]:
        """Open the dispatcher for submissions."""
        if self._started:
            raise RuntimeError("dispatcher is already started")
        self._started = True
        self._closed = False
        self._errors.clear()
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
        if self._closed:
            self._capacity.release()
            raise RuntimeError("dispatcher is closed")
        predecessor = self._tails.get(event.ordering_key)

        async def run() -> None:
            try:
                if predecessor is not None:
                    try:
                        await predecessor
                    except asyncio.CancelledError:
                        raise
                    except BaseException:
                        pass
                async with self._concurrency:
                    try:
                        await self._handler(event)
                    except asyncio.CancelledError:
                        raise
                    except BaseException as error:
                        if self._error_handler is None:
                            self._errors.append(error)
                        else:
                            try:
                                await self._error_handler(error, event)
                            except asyncio.CancelledError:
                                raise
                            except BaseException as handler_error:
                                self._errors.append(handler_error)
            finally:
                current = asyncio.current_task()
                if current is not None:
                    self._tasks.discard(current)
                    if self._tails.get(event.ordering_key) is current:
                        self._tails.pop(event.ordering_key, None)
                self._capacity.release()

        task = asyncio.create_task(run(), name=f"aiotimebot:{event.ordering_key}")
        self._tasks.add(task)
        self._tails[event.ordering_key] = task

    async def join(self) -> None:
        """Wait until every accepted event has finished processing."""
        while self._tasks:
            await asyncio.gather(*tuple(self._tasks), return_exceptions=True)
        if self._errors:
            error = self._errors[0]
            self._errors.clear()
            raise error

    async def aclose(self, *, drain_timeout: float | None = None) -> None:
        """Reject submissions, drain within timeout, then cancel remaining work."""
        if drain_timeout is not None and drain_timeout < 0:
            raise ValueError("shutdown timeout must not be negative")
        async with self._close_lock:
            if self._closed:
                return
            self._closed = True
            try:
                if drain_timeout is None:
                    await self.join()
                else:
                    try:
                        async with asyncio.timeout(drain_timeout):
                            await self.join()
                    except TimeoutError:
                        await self._cancel_and_wait()
                        self._raise_first_error()
            except asyncio.CancelledError:
                await self._cancel_and_wait()
                raise

    async def _cancel_and_wait(self) -> None:
        tasks = tuple(self._tasks)
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)

    def _raise_first_error(self) -> None:
        if self._errors:
            error = self._errors[0]
            self._errors.clear()
            raise error
