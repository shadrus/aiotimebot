"""Router, middleware, and explicit event propagation."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from enum import Enum
from typing import Any, TypeVar, cast

from .context import HandlerContext
from .events import EventType, TimeEvent
from .filters import Command, CommandMatch, EventFilter


class Propagation(Enum):
    """Control whether a router should continue to later handlers."""

    CONTINUE = "continue"
    STOP = "stop"


type HandlerResult = Propagation | None
type Handler = Callable[[Any, HandlerContext], Awaitable[HandlerResult]]
type NextHandler = Callable[[TimeEvent, HandlerContext], Awaitable[HandlerResult]]
type Middleware = Callable[
    [TimeEvent, HandlerContext, NextHandler], Awaitable[HandlerResult]
]


@dataclass(frozen=True, slots=True)
class _Registration:
    handler: Handler
    event_type: EventType | None
    event_filter: EventFilter | None


HandlerT = TypeVar("HandlerT", bound=Handler)


class Router:
    """Route typed events through filters, middleware, and nested routers."""

    def __init__(self) -> None:
        self._handlers: list[_Registration] = []
        self._middlewares: list[Middleware] = []
        self._children: list[Router] = []

    def include_router(self, router: Router) -> Router:
        """Attach a feature router and return it for convenient composition."""
        if router is self:
            raise ValueError("a router cannot include itself")
        self._children.append(router)
        return router

    def use(self, middleware: Middleware) -> Middleware:
        """Register middleware; the first middleware is the outermost one."""
        self._middlewares.append(middleware)
        return middleware

    def register(
        self,
        handler: HandlerT,
        event_filter: EventFilter | None = None,
        *,
        event_type: EventType | None = None,
    ) -> HandlerT:
        """Register a handler directly without decorator syntax."""
        self._handlers.append(
            _Registration(
                handler=cast(Handler, handler),
                event_type=event_type,
                event_filter=event_filter,
            )
        )
        return handler

    def on(
        self,
        event_type: EventType | None = None,
        event_filter: EventFilter | None = None,
    ) -> Callable[[HandlerT], HandlerT]:
        """Return a decorator that registers a general event handler."""

        def decorator(handler: HandlerT) -> HandlerT:
            return self.register(handler, event_filter, event_type=event_type)

        return decorator

    def command(
        self, name: str, *, ignore_case: bool = False
    ) -> Callable[[HandlerT], HandlerT]:
        """Return a decorator for an exact slash command in posted events."""
        return self.on(EventType.POSTED, Command(name, ignore_case=ignore_case))

    async def dispatch(self, event: TimeEvent, context: HandlerContext) -> Propagation:
        """Dispatch one event and return its final propagation state."""
        for registration in self._handlers:
            if (
                registration.event_type is not None
                and event.type is not registration.event_type
            ):
                continue

            handler_context = context.with_command(None)
            if registration.event_filter is not None:
                match = registration.event_filter.match(event)
                if match is None:
                    continue
                if isinstance(match, CommandMatch):
                    handler_context = context.with_command(match)

            result = await self._call_with_middleware(
                registration.handler, event, handler_context
            )
            if result is Propagation.STOP:
                return Propagation.STOP

        for child in self._children:
            if await child.dispatch(event, context) is Propagation.STOP:
                return Propagation.STOP
        return Propagation.CONTINUE

    async def _call_with_middleware(
        self, handler: Handler, event: TimeEvent, context: HandlerContext
    ) -> HandlerResult:
        async def terminal(
            current_event: TimeEvent, current_context: HandlerContext
        ) -> HandlerResult:
            return await handler(current_event, current_context)

        call_next = terminal
        for middleware in reversed(self._middlewares):
            downstream = call_next

            async def wrapped(
                current_event: TimeEvent,
                current_context: HandlerContext,
                *,
                current_middleware: Middleware = middleware,
                next_handler: NextHandler = downstream,
            ) -> HandlerResult:
                return await current_middleware(
                    current_event, current_context, next_handler
                )

            call_next = wrapped
        return await call_next(event, context)
