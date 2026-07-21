# Public API reference

This page summarizes the handwritten public API. The generated REST layer is
indexed separately in the [operation catalog](api-operations.md).

## Package facade

The following symbols are exported from `aiotimebot`:

| Symbol | Purpose |
|---|---|
| `Application` | Own client and handler lifecycle, consume events, and perform graceful shutdown. |
| `TimeClient` | Authenticated HTTP facade, generated API access, messages, raw requests, and WebSocket source creation. |
| `Router` | Register handlers, filters, middleware, and child routers. |
| `HandlerContext` | Handler dependencies: client, storage, and optional command match. |
| `TimeEvent` | Base immutable WebSocket event. |
| `PostedEvent` | Typed posted-message event containing a generated `Post`. |
| `RawEvent` | Known or future event without a specialized typed model. |
| `EventType` | Enum of documented Time WebSocket event names. |
| `Command` | Exact slash-command filter. |
| `CommandMatch` | Parsed command name and argument tuple. |
| `Propagation` | Continue or stop router propagation. |
| `MemoryStateStorage` | Optional process-local conversation state. |
| `StateKey` | User-and-channel key for state storage. |

## `TimeClient`

```text
TimeClient(
    base_url: str,
    token: str,
    *,
    transport: httpx.AsyncBaseTransport | None = None,
    retry_policy: RetryPolicy | None = None,
    timeout: httpx.Timeout | float = 10.0,
    idempotency_key_factory: Callable[[], str] | None = None,
)
```

Public members:

- `api`: authenticated generated client;
- `base_url`: normalized server root;
- `token`: bearer token supplied by the caller;
- `websocket_events() -> WebSocketEventSource`;
- `send_message(...) -> Post`;
- `raw_request(...) -> JSONValue`;
- `aclose() -> None`;
- asynchronous context-manager methods.

See [Client and REST API](client-and-rest.md).

## `Application`

```text
Application(
    client: TimeClient,
    *,
    router: Router | None = None,
    storage: MemoryStateStorage | None = None,
    event_source: EventSource | None = None,
    max_concurrency: int = 100,
    queue_size: int = 1_000,
    shutdown_timeout: float | None = 30.0,
)
```

Public methods:

- `include_router(router) -> Router`;
- `run() -> None`;
- `feed_event(event) -> None`;
- `join() -> None`;
- asynchronous context-manager methods.

See [Lifecycle](lifecycle.md) and
[Routing and events](routing-and-events.md).

## `Router`

Public registration methods:

- `command(name, *, ignore_case=False)`;
- `on(event_type=None, event_filter=None)`;
- `register(handler, event_filter=None, *, event_type=None)`;
- `use(middleware)`;
- `include_router(router)`;
- `dispatch(event, context)` for advanced direct dispatch.

Decorators return the registered callable. `Propagation.STOP` ends propagation;
`None` continues it.

## Events

`TimeEvent` exposes `name`, `data`, `broadcast`, `seq`, `raw`, `type`,
`channel_id`, and `ordering_key`.

`PostedEvent` adds `post`. `RawEvent` adds an optional `decode_error`.

`Broadcast` is available from `aiotimebot.events` for typed access to
`channel_id`, `team_id`, `user_id`, omitted users, and raw broadcast metadata.

See [Routing and events](routing-and-events.md).

## Commands and handler context

`Command(name, ignore_case=False)` matches exact slash commands and uses
shell-like argument parsing. A successful match produces
`CommandMatch(name, arguments)`.

`HandlerContext` contains:

- `client: TimeClient | None`;
- `storage: MemoryStateStorage`;
- `command: CommandMatch | None`.

## State

`StateKey(user_id, channel_id)` identifies one conversation scope.

`MemoryStateStorage` provides:

- `get_state()` and `set_state()`;
- `get_data()` and `set_data()`;
- `clear()`;
- `lock()` as an async context manager.

See [State storage](state-storage.md).

## Error types

The `aiotimebot.errors` module exposes:

- `AioTimeBotError`;
- `APIError`;
- `RateLimited`;
- `WebSocketError`;
- `WebSocketAuthenticationError`;
- `WebSocketProtocolError`.

See [Errors and retries](errors-and-retries.md).

## Retry policy

`aiotimebot.retry.RetryPolicy` configures `max_attempts`, `base_delay`,
`max_delay`, and `default_rate_limit_delay`.

## Advanced runtime types

These types are public at their modules but are normally used through
`Application` or `TimeClient`:

- `aiotimebot.application.EventSource`;
- `aiotimebot.dispatcher.OrderedEventDispatcher`;
- `aiotimebot.websocket.WebSocketEventSource`;
- `aiotimebot.websocket.WebSocketAuthenticator`;
- routing aliases `HandlerResult`, `NextHandler`, and `Middleware`.

The generated `aiotimebot.api` namespace is intentionally not re-exported from
the package facade.
