# Configuration

## `TimeClient`

```python
from aiotimebot import TimeClient
from aiotimebot.retry import RetryPolicy

client = TimeClient(
    base_url="https://time.example.com",
    token="Time bearer token",
    timeout=15.0,
    retry_policy=RetryPolicy(
        max_attempts=3,
        base_delay=0.25,
        max_delay=10.0,
        default_rate_limit_delay=1.0,
    ),
)
```

| Parameter | Default | Meaning |
|---|---:|---|
| `base_url` | required | Absolute HTTP(S) server root; a trailing `/api/v4` is accepted and normalized. |
| `token` | required | Time bearer token used in the `Authorization` header. |
| `timeout` | `10.0` | HTTPX request timeout or an `httpx.Timeout` object. |
| `retry_policy` | `RetryPolicy()` | Bounded retry settings. |
| `idempotency_key_factory` | `None` | Optional factory used by `send_message()` instead of the Time-compatible default. |
| `transport` | HTTPX transport | Advanced injection point for proxies, tests, or a custom HTTP transport. |

The client owns one shared `httpx.AsyncClient`. Prefer `async with client` or
call `await client.aclose()` explicitly.

## `Application`

```python
application = Application(
    client,
    router=router,
    storage=storage,
    max_concurrency=100,
    queue_size=1_000,
    shutdown_timeout=30.0,
)
```

| Parameter | Default | Meaning |
|---|---:|---|
| `router` | new `Router` | Root router for incoming events. |
| `storage` | new `MemoryStateStorage` | Optional process-local state store. |
| `event_source` | authenticated WebSocket | Advanced custom event source, primarily for tests and integrations. |
| `max_concurrency` | `100` | Maximum handlers running across all ordering partitions. |
| `queue_size` | `1000` | Maximum accepted events, including work waiting for capacity. |
| `shutdown_timeout` | `30.0` | Seconds allowed for draining accepted events; `None` waits indefinitely. |

Use lower concurrency when handlers call a tightly rate-limited downstream
service. A full queue applies backpressure to WebSocket ingestion rather than
creating unbounded tasks.

## Environment variables

The library has no required variable names. A conventional application setup is:

```python
import os

from aiotimebot import TimeClient

client = TimeClient(
    base_url=os.environ["TIME_BASE_URL"],
    token=os.environ["TIME_TOKEN"],
)
```

Do not log the token, commit it to a repository, put it in exception messages,
or include it in diagnostic bundles. Rotate a token immediately if it is
exposed.

## Server URL normalization

These values address the same Time server:

```text
https://time.example.com
https://time.example.com/
https://time.example.com/api/v4
```

The WebSocket URL is derived as `wss://time.example.com/api/v4/websocket` for an
HTTPS server and `ws://...` for HTTP.
