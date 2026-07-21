# Getting started

## Prerequisites

You need:

- Python 3.13 or newer;
- the HTTP or HTTPS root URL of a Time Messenger server;
- a Time bearer token for the account that will run the bot;
- membership in every private channel from which the account must receive
  events;
- the destination channel ID for channel-based messages.

Token creation and bot-account provisioning may be restricted by the Time
deployment administrator. The SDK accepts an existing bearer token; it does not
create accounts or tokens.

Store credentials outside source code:

```bash
export TIME_BASE_URL="https://time.example.com"
export TIME_TOKEN="replace-with-a-Time-bearer-token"
export TIME_CHANNEL_ID="replace-with-a-test-channel-id"
```

`aiotimebot` deliberately does not load `.env` files. Use the configuration
system of your application or deployment platform.

## Installation

From a published release:

```bash
python -m pip install aiotimebot
```

From a downloaded wheel:

```bash
python -m pip install ./vendor/aiotimebot-0.1.0-py3-none-any.whl
```

With uv:

```bash
uv add ./vendor/aiotimebot-0.1.0-py3-none-any.whl
```

## Verify the credentials

Run a read-only request before starting the event loop:

```python
import asyncio
import os

from aiotimebot import TimeClient


async def main() -> None:
    client = TimeClient(
        base_url=os.environ["TIME_BASE_URL"],
        token=os.environ["TIME_TOKEN"],
    )
    async with client:
        current_user = await client.raw_request("GET", "/api/v4/users/me")
        print(current_user)


asyncio.run(main())
```

An authentication or permission failure is raised as
[`APIError`](errors-and-retries.md#high-level-client-errors).

## Create a command bot

Save this as `bot.py`:

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


@router.command("ping", ignore_case=True)
async def ping(event: PostedEvent, context: HandlerContext) -> None:
    client = context.client
    if client is None:
        raise RuntimeError("This handler requires an Application client")
    await client.send_message(channel_id=event.channel_id, text="pong")


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

Start it:

```bash
python bot.py
```

Send `/ping` in a channel shared with the bot account. The expected response is
`pong`.

Some Time clients first interpret slash-prefixed text as a server command. If
the UI reports that `/ping` is unknown, use its action for sending the text as a
normal message. REST-created posts do not have this UI interception.

## Where to continue

- Add arguments and feature routers in [Routing and events](routing-and-events.md).
- Learn the message and REST APIs in [Client and REST API](client-and-rest.md).
- Add service-friendly termination from [Lifecycle](lifecycle.md).
- Review failure contracts in [Errors and retries](errors-and-retries.md).
