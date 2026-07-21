# Errors and retries

## Exception hierarchy

Import handwritten exceptions from `aiotimebot.errors`:

```text
AioTimeBotError
├── APIError
│   └── RateLimited
└── WebSocketError
    ├── WebSocketAuthenticationError
    └── WebSocketProtocolError
```

Generated REST modules also define their own strict transport exception
`aiotimebot.api.errors.UnexpectedStatus` and return generated `AppError` models
for documented API error responses.

## High-level client errors

`TimeClient.send_message()` and `TimeClient.raw_request()` raise `APIError` for
an HTTP error response:

```python
from aiotimebot.errors import APIError

try:
    await client.send_message(channel_id="channel-id", text="hello")
except APIError as error:
    print(error.status_code)
    print(error.error_id)
    print(error.request_id)
    print(error.detailed_error)
    raise
```

Malformed success responses also raise `APIError`, because returning an invalid
typed model as a success would hide a server incompatibility.

`RateLimited` is part of the exception hierarchy for application-level use, but
the current transport does not synthesize it. After the configured attempts are
exhausted, a final high-level HTTP 429 is normalized as `APIError` with
`status_code == 429`.

## Generated endpoint errors

Generated `asyncio()` functions return a union of documented success and error
models. Always inspect the result:

```python
from aiotimebot.api.api.users import get_user
from aiotimebot.api.models.app_error import AppError
from aiotimebot.api.models.user import User

result = await get_user.asyncio(client=client.api, user_id="me")
if isinstance(result, AppError):
    raise RuntimeError(result.message)
if isinstance(result, User):
    print(result.username)
```

An undocumented status raises `UnexpectedStatus`. Network exceptions after all
retry attempts remain HTTPX transport exceptions.

## Retry defaults

```python
from aiotimebot.retry import RetryPolicy

policy = RetryPolicy(
    max_attempts=3,
    base_delay=0.25,
    max_delay=30.0,
    default_rate_limit_delay=1.0,
)
```

The transport retries:

- HTTPX `TransportError` failures;
- HTTP 429, honoring `X-RateLimit-Reset`;
- HTTP 502, 503, and 504.

Backoff is bounded exponential backoff. A retryable response is closed before
the next attempt.

## Unsafe requests and idempotency

GET, HEAD, OPTIONS, PUT, and DELETE may be retried by default. POST and other
unsafe methods are retried only when their JSON body contains a non-empty
`idempotency_key`.

`send_message()` creates a Time-compatible key automatically. For an external
workflow, an explicit key can correlate retries:

```python
post = await client.send_message(
    channel_id="channel-id",
    text="Release completed",
    idempotency_key="user-id:1784618261882",
)
```

Use a key accepted by the target Time deployment. A random UUID was not enough
to trigger post deduplication on the tested Time 7.8 server.

## WebSocket errors

- `WebSocketAuthenticationError` means Time rejected the challenge. Check the
  token and account state.
- `WebSocketProtocolError` means a frame violated the expected protocol or
  contained invalid JSON.
- ordinary connection closures are handled by the reconnect iterator and cause
  a new authentication challenge.

Do not retry an authentication failure in a tight custom loop. Fix or rotate the
credential first.

## Handler errors

Handler exceptions are retained by the dispatcher and surfaced through
`Application.join()` or application shutdown. Later events in the same channel
are not permanently blocked by one failed handler.

Use middleware for structured error logging, but re-raise errors when service
policy requires the application to fail.
