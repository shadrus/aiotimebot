# aiotimebot user documentation

`aiotimebot` is an asyncio-native Python 3.13+ SDK and bot runtime for Time
Messenger API v4.

Start here:

1. [Getting started](getting-started.md) — credentials, connection check, and a
   first command bot.
2. [Configuration](configuration.md) — `TimeClient`, `Application`, security,
   concurrency, and timeouts.
3. [Routing and events](routing-and-events.md) — commands, raw events,
   middleware, propagation, and ordering.
4. [Client and REST API](client-and-rest.md) — messages, threads, generated
   endpoints, models, and the raw escape hatch.
5. [Errors and retries](errors-and-retries.md) — exception contracts,
   idempotency, rate limits, and transient failures.
6. [Lifecycle](lifecycle.md) — cancellation, SIGTERM, shutdown deadlines, and
   reconnect behavior.
7. [State storage](state-storage.md) — optional in-memory conversation state.

Reference and recipes:

- [Public API reference](api-reference.md)
- [Generated REST operation catalog](api-operations.md)
- [Common recipes](recipes.md)
- [Time 7.8 compatibility](time-7.8-compatibility.md)

The generated REST layer follows the vendored Time OpenAPI schema. Consult the
[Time Messenger API v4 documentation](https://docs.time-messenger.ru/api/v4/введение/)
for endpoint semantics and server-side permission requirements.
