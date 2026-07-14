"""Application lifecycle tying WebSocket events to a Router."""

from __future__ import annotations

from collections.abc import AsyncIterator
from types import TracebackType
from typing import Protocol

from .client import TimeClient
from .context import HandlerContext
from .dispatcher import OrderedEventDispatcher
from .events import TimeEvent
from .routing import Router
from .storage import MemoryStateStorage


class EventSource(Protocol):
    """An inbound source capable of yielding Time events."""

    def events(self) -> AsyncIterator[TimeEvent]:
        """Yield events until the source is stopped or disconnected."""
        ...


class Application:
    """Own the client, event source, dispatcher, and graceful lifecycle."""

    def __init__(
        self,
        client: TimeClient,
        *,
        router: Router | None = None,
        storage: MemoryStateStorage | None = None,
        event_source: EventSource | None = None,
        max_concurrency: int = 100,
        queue_size: int = 1_000,
    ) -> None:
        self.client = client
        self.router = router or Router()
        self.storage = storage or MemoryStateStorage()
        self.event_source = event_source or client.websocket_events()
        self._dispatcher = OrderedEventDispatcher(
            self._dispatch,
            max_concurrency=max_concurrency,
            queue_size=queue_size,
            error_handler=self._raise_handler_error,
        )

    def include_router(self, router: Router) -> Router:
        """Attach a feature router to the application's root router."""
        return self.router.include_router(router)

    async def __aenter__(self) -> Application:
        """Open HTTP resources and event dispatch capacity."""
        await self.client.__aenter__()
        await self._dispatcher.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Drain accepted events before closing network resources."""
        try:
            await self._dispatcher.aclose()
        finally:
            await self.client.__aexit__(exc_type, exc_value, traceback)

    async def run(self) -> None:
        """Consume the configured WebSocket source until cancelled."""
        async for event in self.event_source.events():
            await self._dispatcher.submit(event)

    async def feed_event(self, event: TimeEvent) -> None:
        """Submit a synthetic event for tests or external integrations."""
        await self._dispatcher.submit(event)

    async def join(self) -> None:
        """Wait for all accepted events to finish."""
        await self._dispatcher.join()

    async def _dispatch(self, event: TimeEvent) -> None:
        await self.router.dispatch(
            event,
            HandlerContext(client=self.client, storage=self.storage),
        )

    @staticmethod
    async def _raise_handler_error(error: BaseException, event: TimeEvent) -> None:
        raise error
