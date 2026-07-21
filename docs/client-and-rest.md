# Client and REST API

## Client lifecycle

Use one `TimeClient` for related operations so HTTP connections and the current
user lookup can be reused:

```python
from aiotimebot import TimeClient

client = TimeClient("https://time.example.com", "Time bearer token")
async with client:
    profile = await client.raw_request("GET", "/api/v4/users/me")
```

Call `await client.aclose()` when a context manager is inconvenient. Do not use
the client after it has been closed.

## Sending messages

Exactly one destination is required:

```python
post = await client.send_message(
    channel_id="channel-id",
    text="Deployment completed",
)
```

or:

```python
post = await client.send_message(
    peer="@alice",
    text="Hello",
)
```

The complete high-level parameters are:

| Parameter | Meaning |
|---|---|
| `text` | Post message. |
| `channel_id` | Destination channel; mutually exclusive with `peer`. |
| `peer` | Time peer syntax such as `@alice`; mutually exclusive with `channel_id`. |
| `root_id` | Root post ID for a thread reply. |
| `file_ids` | Up to five already-uploaded Time file IDs. |
| `idempotency_key` | Explicit Time-compatible key for correlating a retry. |

Reply in a thread:

```python
reply = await client.send_message(
    channel_id=root.channel_id,
    root_id=root.id,
    text="Acknowledged",
)
```

Attach uploaded files:

```python
post = await client.send_message(
    channel_id="channel-id",
    text="Build artifacts",
    file_ids=[first_file_id, second_file_id],
)
```

File upload itself is available through the generated REST layer because its
typed request depends on the selected Time endpoint. Find it in the
[operation catalog](api-operations.md).

## Idempotency behavior

Without an explicit key or custom factory, `send_message()` resolves
`/api/v4/users/me` once and creates keys in this form:

```text
<current_user_id>:<millisecond_timestamp>
```

Timestamps are strictly increasing within one client. This is the format
confirmed to deduplicate posts on the target Time 7.8 deployment. See
[Errors and retries](errors-and-retries.md#unsafe-requests-and-idempotency).

## Generated REST operations

`client.api` is the authenticated generated client. Import endpoint modules and
body models directly:

```python
from aiotimebot.api.api.posts import patch_post
from aiotimebot.api.models.app_error import AppError
from aiotimebot.api.models.patch_post_body import PatchPostBody
from aiotimebot.api.models.post import Post

result = await patch_post.asyncio(
    post_id="post-id",
    client=client.api,
    body=PatchPostBody(message="Corrected message"),
)

if isinstance(result, AppError):
    raise RuntimeError(result.message)
if isinstance(result, Post):
    print(result.message)
```

Each generated module exposes:

- `asyncio(...)` for the parsed response;
- `asyncio_detailed(...)` for status, headers, raw bytes, and parsed data.

```python
response = await patch_post.asyncio_detailed(
    post_id="post-id",
    client=client.api,
    body=PatchPostBody(message="Corrected message"),
)

print(response.status_code)
print(response.headers)
print(response.parsed)
```

Documented error statuses normally parse to the generated `AppError` model.
An undocumented status raises `aiotimebot.api.errors.UnexpectedStatus` because
the authenticated generated client enables strict unexpected-status handling.

Use the [generated operation catalog](api-operations.md) to map Time
`operationId` values to import modules.

## Generated models and forward compatibility

Optional fields use `UNSET` to distinguish omission from an explicit value:

```python
from aiotimebot.api.types import UNSET

if post.participants is not UNSET:
    print(post.participants)
```

Unknown model properties remain in `additional_properties`. Generated model
instances support access to those properties through mapping-like methods such
as `model["future_field"]`.

## Raw request escape hatch

Use `raw_request()` for a server extension or a schema defect, not as the
default API:

```python
result = await client.raw_request(
    "POST",
    "/api/v4/plugin/example/action",
    params={"dry_run": "true"},
    json_body={"value": 42},
)
```

The result is:

- decoded JSON for a JSON response;
- `str` for a non-JSON response body;
- `None` for an empty response.

HTTP error statuses raise `APIError`. Raw POST requests without an
`idempotency_key` are not retried because repeating them could duplicate an
effect.
