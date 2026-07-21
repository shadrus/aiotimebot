# Routing and events

## Event model

Every inbound WebSocket envelope becomes a `TimeEvent` with:

- `name`: original Time event name;
- `type`: matching `EventType`, or `None` for an unknown name;
- `data`: event-specific mapping;
- `broadcast`: routing metadata such as channel and user IDs;
- `seq`: server sequence number from the envelope;
- `raw`: complete original envelope;
- `ordering_key`: deterministic dispatcher partition.

Current specialized models are:

| Time event | Python model | Additional fields |
|---|---|---|
| `posted` with a valid post | `PostedEvent` | Typed generated `post` model |
| `posted` with an invalid post | `RawEvent` | `decode_error` describes the parse failure |
| Other known event names | `RawEvent` | Event-specific content remains in `data` and `raw` |
| Future event name | `RawEvent` | `type` is `None`; no payload is discarded |

Register a known non-post event:

```python
from aiotimebot import EventType, HandlerContext, RawEvent, Router

router = Router()


@router.on(EventType.REACTION_ADDED)
async def reaction_added(event: RawEvent, context: HandlerContext) -> None:
    print(event.data)
```

Use `raw` when the server adds fields before the SDK gains a specialized
model. Code reading `data` should tolerate missing and additional keys.

## Slash commands

```python
from aiotimebot import HandlerContext, PostedEvent, Router

router = Router()


@router.command("deploy", ignore_case=True)
async def deploy(event: PostedEvent, context: HandlerContext) -> None:
    command = context.command
    if command is None:
        return
    environment, *labels = command.arguments
    print(environment, labels)
```

The filter requires an exact first token. `/deploy-now` does not match
`deploy`. Arguments use shell-like parsing:

```text
/deploy production "release candidate"
```

produces `("production", "release candidate")`. An unmatched quote causes the
filter not to match.

## Direct registration and custom filters

Decorators are optional:

```python
from aiotimebot import Command, Router

router = Router()
router.register(deploy, Command("deploy", ignore_case=True))
```

A custom filter implements `match(event)`. Return `None` to reject the event or
any other object to accept it. Only `CommandMatch` is automatically copied into
`context.command`.

## Feature routers

Split a large bot by feature:

```python
root = Router()
deployments = Router()
alerts = Router()

root.include_router(deployments)
root.include_router(alerts)
```

Registrations in the current router run before child routers. A router cannot
include itself.

`Application.include_router()` is shorthand for attaching a feature router to
the application's root router.

## Propagation

Handlers return `None` to continue or `Propagation.STOP` to prevent remaining
handlers and child routers from seeing the event:

```python
from aiotimebot import Propagation


@router.command("private")
async def private_command(event, context) -> Propagation:
    await handle_private_command(event, context)
    return Propagation.STOP
```

## Middleware

Middleware wraps each matching handler. The first registered middleware is the
outermost:

```python
import time

from aiotimebot import HandlerContext, TimeEvent
from aiotimebot.routing import HandlerResult, NextHandler


@router.use
async def timing(
    event: TimeEvent,
    context: HandlerContext,
    call_next: NextHandler,
) -> HandlerResult:
    started = time.monotonic()
    try:
        return await call_next(event, context)
    finally:
        print(event.name, time.monotonic() - started)
```

Middleware is useful for structured logging, metrics, authorization, and
dependency scopes. It should re-raise `asyncio.CancelledError`.

## Ordering and concurrency

Dispatcher partitions are:

```text
channel event -> channel:<channel_id>
user event    -> user:<user_id>
global event  -> global
```

Events in one partition run strictly in arrival order. Different partitions may
run concurrently up to `Application.max_concurrency`. `queue_size` bounds
accepted work and applies backpressure to ingestion.

Ordering is in-memory and applies to one `Application` process. Multiple bot
processes need external coordination if they must preserve a global order.
