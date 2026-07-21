# Lifecycle and shutdown

## Resource ownership

`TimeClient` owns the HTTP connection pool. `Application` owns accepted handler
tasks and coordinates the client, event source, router, and state storage.

The library never creates an event loop. Call it from an existing asyncio
application:

```python
async with Application(client, router=router) as application:
    await application.run()
```

## Normal shutdown

When the application context exits it:

1. rejects new event submissions;
2. drains accepted handlers for up to `shutdown_timeout` seconds;
3. cancels and awaits unfinished handlers;
4. closes shared HTTP resources.

The default deadline is 30 seconds. Use `shutdown_timeout=None` only when an
unbounded shutdown is acceptable.

## SIGTERM and service managers

`Application` does not install process signal handlers. A service entry point
can translate SIGTERM into cancellation of its root task:

```python
import asyncio
import os
import signal
from contextlib import suppress

from aiotimebot import Application, Router, TimeClient


async def serve() -> None:
    current = asyncio.current_task()
    if current is None:
        raise RuntimeError("serve() must run inside an asyncio task")

    loop = asyncio.get_running_loop()

    def cancel() -> None:
        current.cancel()

    loop.add_signal_handler(signal.SIGTERM, cancel)
    try:
        client = TimeClient(os.environ["TIME_BASE_URL"], os.environ["TIME_TOKEN"])
        application = Application(client, router=Router())
        async with application:
            await application.run()
    finally:
        loop.remove_signal_handler(signal.SIGTERM)


with suppress(KeyboardInterrupt, asyncio.CancelledError):
    asyncio.run(serve())
```

`loop.add_signal_handler()` is Unix-specific. On platforms without it, use the
shutdown callback provided by the process host and cancel the root task.

## Cancellation contract

Handlers may use `finally` blocks for cleanup:

```python
@router.command("work")
async def work(event, context) -> None:
    resource = await acquire_resource()
    try:
        await perform_work(resource)
    finally:
        await release_resource(resource)
```

`asyncio.CancelledError` is propagated after runtime cleanup. Do not swallow it
inside handlers. If cleanup must ignore ordinary exceptions, catch `Exception`,
not `BaseException`.

## Handler failures

An ordinary handler exception does not prevent the next event in the same
channel from running. The first stored failure is raised by `Application.join()`
or while draining the application context. Production entry points should log
that exception and exit non-zero according to their service policy.

## WebSocket reconnect

The WebSocket source uses the reconnect iteration provided by `websockets`.
Each new connection performs a fresh authentication challenge. Authentication
and protocol failures are typed and are not silently converted to events; see
[Errors and retries](errors-and-retries.md).

The runtime does not persist an event cursor. Handlers that trigger external
effects should be idempotent because a network boundary can always make event
delivery outcome uncertain.
