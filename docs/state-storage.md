# State storage

`MemoryStateStorage` is an optional process-local store for conversation state
and arbitrary JSON-like application data.

## Access from a handler

`Application` places its configured storage in every `HandlerContext`:

```python
from aiotimebot import HandlerContext, PostedEvent, StateKey


@router.command("begin")
async def begin(event: PostedEvent, context: HandlerContext) -> None:
    key = StateKey(user_id=event.post.user_id, channel_id=event.channel_id)
    await context.storage.set_state(key, "waiting_for_name")
    await context.storage.set_data(key, {"attempts": 0})
```

Read it later:

```python
key = StateKey(user_id=event.post.user_id, channel_id=event.channel_id)
state = await context.storage.get_state(key)
data = await context.storage.get_data(key)
```

`get_data()` and `set_data()` use defensive deep copies. Mutating a returned
dictionary does not modify stored data until `set_data()` is called.

## Atomic read-modify-write

Use the per-key lock when a handler reads and updates related values:

```python
key = StateKey(user_id=event.post.user_id, channel_id=event.channel_id)

async with context.storage.lock(key):
    data = await context.storage.get_data(key)
    data["attempts"] = int(data.get("attempts", 0)) + 1
    await context.storage.set_data(key, data)
```

Different keys can be modified concurrently. The same key is serialized.

## Clearing state

```python
await context.storage.set_state(key, None)  # remove only the state name
await context.storage.clear(key)           # remove state and data
```

## Limitations

`MemoryStateStorage`:

- loses all data on process restart;
- is not shared between multiple processes or hosts;
- has no expiration or eviction policy;
- stores data until `clear()` is called;
- is intended for optional small bot workflows, not durable business data.

For durable or distributed state, keep that dependency in application code and
access it through middleware or another explicit application service. The
runtime itself does not require FSM state.
