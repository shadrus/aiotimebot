# aiotimebot architecture

## Product scope

`aiotimebot` is a Python 3.12+ asynchronous SDK and bot runtime for Time
Messenger API v4. It is intentionally specific to Time Messenger. Do not add
provider-neutral abstractions or compatibility layers for other chat systems.

The library must expose every REST operation from the vendored Time OpenAPI
document. Most REST code is generated, while handwritten code provides the
ergonomic client facade, WebSocket event runtime, routing, concurrency control,
state storage, retries, and error normalization.

## Architectural boundaries

The package follows these dependency directions:

```text
public facade (TimeClient, Application)
        |                    |
        v                    v
generated REST API     event routing/runtime
        |                    |
        v                    v
HTTPX transport       WebSocket event source
        |                    |
        +----------> Time Messenger API v4
```

- `aiotimebot.api` is generated from `schema/time-api-v4.yaml`. It contains
  typed request bodies, response models, and async endpoint functions.
- `aiotimebot.client.TimeClient` owns authentication, HTTP lifecycle, raw
  access, common bot operations, retry policy, and normalized exceptions.
- `aiotimebot.events` parses Time WebSocket envelopes and preserves unknown
  fields and the complete raw payload.
- `aiotimebot.routing` contains routers, filters, middleware, and explicit
  propagation semantics. Decorators are registration sugar, never the only API.
- `aiotimebot.application.Application` owns all background tasks and performs
  graceful startup and shutdown.
- `aiotimebot.dispatcher` processes events sequentially within one Time channel
  and concurrently across different channels, with bounded global concurrency.
- `aiotimebot.storage` provides optional in-memory state. The runtime itself is
  stateless and must not require FSM state.

## Event transport decision

Use `/api/v4/websocket` as the primary inbound event transport. Time documents
WebSocket as its real-time change delivery mechanism and defines an
`authentication_challenge` exchange. REST remains the command transport.
Webhooks in Time are integration endpoints, not the general authenticated bot
event stream, so they are not the primary runtime transport.

## Public API rules

- Public I/O is async-only and based on `asyncio`.
- Public symbols must be fully annotated and pass strict static checking.
- Prefer immutable, slotted domain event dataclasses.
- Generated models retain unknown fields through `additional_properties`.
- Handwritten event models retain the original payload through `raw`.
- Provide typed high-level methods for common bot actions and expose the full
  generated REST surface for all other operations.
- Keep a documented raw request escape hatch for forward compatibility.
- Never create an event loop inside library internals and never expose or store
  a caller's loop.

## Concurrency and lifecycle

- Events sharing a non-empty `channel_id` are handled in arrival order.
- Events for different channels may run concurrently.
- Events without a channel use a deterministic fallback ordering key.
- Global concurrency and queue size are bounded.
- Every task is owned by `Application`; no fire-and-forget tasks are allowed.
- Shutdown stops ingestion first, drains accepted work within the configured
  timeout, then cancels and awaits remaining owned tasks.
- `CancelledError` must always propagate after cleanup.

## HTTP reliability

- Retry connection failures and server rate limiting with bounded backoff.
- Retry unsafe requests only when they carry a Time `idempotency_key`.
- Honor `X-RateLimit-Reset` on HTTP 429 responses.
- Never silently convert API error payloads into successful return values.
- Authentication uses `Authorization: Bearer <token>`.

## TDD workflow

Development is test-first:

1. Add or change tests describing externally observable behavior and edge cases.
2. Run the focused tests and confirm they fail for the intended reason.
3. Implement the smallest coherent production change.
4. Run the focused tests, then the complete suite, lint, and strict type checks.

Do not weaken assertions or rewrite tests to accommodate an implementation.
Change a test only when the documented product requirement changes or the test
itself is demonstrably incorrect. Generated code is tested through generation
coverage, representative serialization tests, and facade contract tests rather
than by duplicating the generator's own suite.

## Code generation

- The authoritative schema is `schema/time-api-v4.yaml`.
- Generation must be reproducible through `scripts/generate_api.py`.
- Keep generated files separate from handwritten files.
- Do not hand-edit generated files.
- The generation check must prove that every OpenAPI `operationId` is either
  generated or explicitly listed as a manually implemented schema workaround.
- Preserve a raw request method even when the upstream schema is temporarily
  invalid or incomplete.

## Documentation and style

- All code comments, docstrings, public API documentation, and test names are in
  English.
- User-facing README examples may explain concepts in English while keeping the
  API itself language-neutral.
- Use Ruff for formatting and linting, pytest for behavior, and mypy in strict
  mode. Avoid comments that merely restate code; document protocol constraints,
  ownership, invariants, and non-obvious decisions.

