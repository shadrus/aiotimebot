# Common recipes

## Send a one-shot message

```python
import asyncio
import os

from aiotimebot import TimeClient


async def main() -> None:
    client = TimeClient(os.environ["TIME_BASE_URL"], os.environ["TIME_TOKEN"])
    async with client:
        post = await client.send_message(
            channel_id=os.environ["TIME_CHANNEL_ID"],
            text="Deployment completed",
        )
        print(post.id)


asyncio.run(main())
```

## Reply in a thread

```python
@router.command("ack")
async def acknowledge(event: PostedEvent, context: HandlerContext) -> None:
    client = context.client
    if client is None:
        return
    root_id = event.post.root_id or event.post.id
    await client.send_message(
        channel_id=event.channel_id,
        root_id=root_id,
        text="Acknowledged",
    )
```

## Use quoted command arguments

```python
@router.command("announce")
async def announce(event: PostedEvent, context: HandlerContext) -> None:
    if context.command is None:
        return
    if len(context.command.arguments) != 2:
        return
    audience, message = context.command.arguments
    print(f"Audience: {audience}; message: {message}")
```

Input:

```text
/announce engineering "Release starts at 18:00"
```

## Organize feature routers

```python
from aiotimebot import Application, Router

root = Router()
deployments = Router()
support = Router()

# Register feature handlers on deployments and support.
root.include_router(deployments)
root.include_router(support)

application = Application(client, router=root)
```

Return `Propagation.STOP` from an authorization or ownership handler when child
routers must not process the event.

## Inspect a future event safely

```python
from aiotimebot import HandlerContext, RawEvent, Router

router = Router()


@router.on()
async def observe(event: RawEvent, context: HandlerContext) -> None:
    if event.type is None:
        print("New Time event:", event.name)
        print("Available data keys:", sorted(event.data))
```

Avoid logging `event.raw` blindly in production. It may contain message content
or other sensitive data.

## Call an operation with an undocumented field

Generated models retain unknown properties:

```python
from aiotimebot.api.models.patch_post_body import PatchPostBody

body = PatchPostBody(message="Updated")
body["future_option"] = True
```

For an endpoint absent from the schema, use `raw_request()`:

```python
result = await client.raw_request(
    "GET",
    "/api/v4/plugin/example/status",
)
```

## Feed an event in a test

`Application.feed_event()` sends a parsed or synthetic event through the same
dispatcher and router without opening the WebSocket source:

```python
from aiotimebot.events import parse_event

event = parse_event(
    {
        "event": "future_event",
        "data": {"value": 1},
        "broadcast": {"channel_id": "test-channel"},
        "seq": 1,
    }
)

async with application:
    await application.feed_event(event)
    await application.join()
```

Use an HTTPX mock transport with `TimeClient` to keep unit tests offline.
