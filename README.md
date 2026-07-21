# aiotimebot

`aiotimebot` is a typed, asyncio-native SDK and bot runtime for
[Time Messenger API v4](https://docs.time-messenger.ru/api/v4/введение/). It
targets Python 3.13 or newer and is intentionally specific to Time Messenger.

The package combines:

- generated models and async functions for all 470 documented REST operations;
- a high-level `TimeClient` for common bot actions;
- authenticated real-time events through `/api/v4/websocket`;
- typed event parsing with forward-compatible raw payloads;
- routers, slash-command filters, and middleware;
- bounded concurrency with strict ordering inside one channel;
- optional in-memory conversation state;
- bounded retries for transport errors, HTTP 429, and HTTP 502/503/504,
  guarded by Time idempotency keys for unsafe requests.

## Documentation

[User documentation](https://github.com/shadrus/aiotimebot/tree/main/docs) covers:

- [getting started](https://github.com/shadrus/aiotimebot/blob/main/docs/getting-started.md),
  credentials, and the first bot;
- [configuration](https://github.com/shadrus/aiotimebot/blob/main/docs/configuration.md)
  and security;
- [routing and events](https://github.com/shadrus/aiotimebot/blob/main/docs/routing-and-events.md);
- [messages and the complete REST API](https://github.com/shadrus/aiotimebot/blob/main/docs/client-and-rest.md);
- [errors and retries](https://github.com/shadrus/aiotimebot/blob/main/docs/errors-and-retries.md);
- [lifecycle and graceful shutdown](https://github.com/shadrus/aiotimebot/blob/main/docs/lifecycle.md);
- [state storage](https://github.com/shadrus/aiotimebot/blob/main/docs/state-storage.md);
- [recipes](https://github.com/shadrus/aiotimebot/blob/main/docs/recipes.md) and
  [Time 7.8 compatibility](https://github.com/shadrus/aiotimebot/blob/main/docs/time-7.8-compatibility.md);
- the [public API reference](https://github.com/shadrus/aiotimebot/blob/main/docs/api-reference.md)
  and generated
  [470-operation catalog](https://github.com/shadrus/aiotimebot/blob/main/docs/api-operations.md).

## Installation

Install a published release from the configured package index:

```bash
python -m pip install aiotimebot
```

If no package-index release is available yet, install a wheel from a successful
GitHub CI run as described below.

For local development:

```bash
uv sync --all-groups
```

## Installing from GitHub CI

Every GitHub Actions run that passes tests, Ruff, and strict mypy builds both a
wheel and a source distribution. Open the repository's **Actions** tab, choose a
successful **CI** run, and download the `aiotimebot-dist` artifact.

The downloaded artifact is a ZIP archive. Extract it into the consuming project,
for example under `vendor/`, and add the wheel:

```bash
uv add ./vendor/aiotimebot-0.1.1-py3-none-any.whl
```

With pip:

```bash
python -m pip install ./vendor/aiotimebot-0.1.1-py3-none-any.whl
```

After installation, import the package normally:

```python
from aiotimebot import Application, Router, TimeClient
```

For development snapshots, uv can build directly from the Git repository:

```bash
uv add git+ssh://git@github.com/shadrus/aiotimebot.git --branch main
```

For reproducible production builds, prefer a release tag or immutable commit:

```bash
uv add git+ssh://git@github.com/shadrus/aiotimebot.git \
  --rev COMMIT_SHA
```

## Quick start

```python
import asyncio
import os

from aiotimebot import (
    Application,
    HandlerContext,
    PostedEvent,
    Router,
    TimeClient,
)

router = Router()


@router.command("ping")
async def ping(event: PostedEvent, context: HandlerContext) -> None:
    client = context.client
    if client is None:
        raise RuntimeError("The handler requires an application client")

    await client.send_message(
        channel_id=event.channel_id,
        text="pong",
    )


async def main() -> None:
    client = TimeClient(
        base_url=os.environ["TIME_BASE_URL"],
        token=os.environ["TIME_TOKEN"],
    )
    application = Application(client, router=router)

    async with application:
        await application.run()


asyncio.run(main())
```

`Application` stops event ingestion before draining accepted handler work and
closing its shared HTTP resources. It does not create or control the caller's
event loop. See
[Getting started](https://github.com/shadrus/aiotimebot/blob/main/docs/getting-started.md)
for credential and
channel prerequisites, including the Time UI behavior for unknown slash
commands.

## Sending posts

Send to a channel:

```python
post = await client.send_message(
    channel_id="channel-id",
    text="Deployment completed",
)
```

Send to a user by Time peer syntax:

```python
post = await client.send_message(
    peer="@alice",
    text="Hello",
)
```

The high-level method automatically creates a Time `idempotency_key`. A caller
may supply its own key when it needs to correlate retries with external work.
Time permits at most five files on one post, and the client validates that limit
before network I/O.

Time 7.8 only deduplicates post keys formatted as
`<current_user_id>:<millisecond_timestamp>`. When no key or custom factory is
provided, the client resolves `/api/v4/users/me` once, caches the user ID, and
generates strictly increasing timestamps. Supplying an explicit key or
`idempotency_key_factory` avoids this lookup.

## Complete typed REST API

The `client.api` property is the authenticated generated client. Each operation
has an async module and typed request and response models:

```python
from aiotimebot.api.api.users import get_user
from aiotimebot.api.models.app_error import AppError
from aiotimebot.api.models.user import User

result = await get_user.asyncio(
    client=client.api,
    user_id="me",
)

if isinstance(result, AppError):
    raise RuntimeError(result.message)
if isinstance(result, User):
    print(result.username)
```

Generated endpoint modules also provide `asyncio_detailed()` when status,
headers, and raw content are required. `TimeClient.raw_request()` is the escape
hatch for server extensions and API additions that are not yet present in the
vendored schema. Browse every generated import path in the
[REST operation catalog](https://github.com/shadrus/aiotimebot/blob/main/docs/api-operations.md).

## Routing and middleware

Handlers may be registered with decorators or directly:

```python
from aiotimebot import Router
from aiotimebot.filters import Command

router = Router()
router.register(handler, Command("deploy"))
```

Command arguments support shell-like quoting. For example,
`/deploy production "release candidate"` produces the arguments
`("production", "release candidate")` in `context.command.arguments`.

Middleware wraps matching handlers in registration order:

```python
@router.use
async def tracing(event, context, call_next):
    # Add a trace span or structured logging fields here.
    return await call_next(event, context)
```

Return `Propagation.STOP` from a handler to prevent later handlers and nested
routers from receiving the event. Specialized and raw event behavior is covered
in
[Routing and events](https://github.com/shadrus/aiotimebot/blob/main/docs/routing-and-events.md).

## Event ordering

The dispatcher uses this partition policy:

```text
channel event -> channel:<channel_id>
user event    -> user:<user_id>
global event  -> global
```

Events in one partition execute sequentially in arrival order. Different
partitions execute concurrently up to `Application(max_concurrency=...)`.
Queue capacity is bounded by `queue_size`, so ingestion applies backpressure
instead of creating unlimited background tasks.

On context exit, `Application` rejects new events and drains accepted work for
up to `shutdown_timeout` seconds (30 seconds by default). It then cancels and
awaits unfinished handlers before closing the HTTP client. Set
`shutdown_timeout=None` to wait without a deadline.

Unknown WebSocket event names become `RawEvent` instances. Unknown fields on
generated REST models remain in `additional_properties`, and every handwritten
event retains its complete original envelope in `event.raw`.

## Why WebSocket is the inbound transport

Time documents WebSocket as its real-time delivery mechanism for posts,
reactions, channel changes, typing, and other account events. The client opens
`/api/v4/websocket`, performs the documented `authentication_challenge`, and
uses the REST API for commands. Time webhooks are integration endpoints rather
than the general authenticated event stream, so they are not used as the bot
runtime transport.

Some Time 7.8 deployments send the initial `hello` event before the response to
`authentication_challenge`, although the API document shows the opposite order.
The runtime preserves such early events and waits for the response carrying the
matching `seq_reply` before exposing them to handlers.

For production cancellation, SIGTERM integration, error behavior, retry
configuration, and optional state, use the dedicated user documentation rather
than relying only on this overview.

## Development

The project uses test-first development. Run the complete verification set with:

```bash
uv run pytest
uv run pytest --cov --cov-report=term-missing --cov-fail-under=95
uv run ruff check .
uv run mypy
```

Regenerate the REST layer after intentionally updating the vendored schema:

```bash
uv run python scripts/generate_api.py
```

The generation script corrects a small, documented set of upstream schema
defects in memory. It never changes `schema/time-api-v4.yaml`. A coverage test
then verifies that every one of the schema's 470 `operationId` values imports an
async implementation.

More detailed invariants and contribution rules are recorded in
[`AGENTS.md`](https://github.com/shadrus/aiotimebot/blob/main/AGENTS.md).
