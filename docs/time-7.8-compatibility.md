# Time 7.8 compatibility

The vendored OpenAPI document is authoritative for generated coverage, but
deployed Time 7.8 servers have confirmed protocol differences. The SDK applies
narrow compatibility corrections without modifying the vendored schema.

## WebSocket authentication ordering

A Time 7.8 server may send `hello` before replying to
`authentication_challenge`. The SDK buffers early event envelopes, waits for the
response with the matching `seq_reply`, and only then exposes buffered events.

Applications do not need to special-case this order.

## Nullable post participants

Real post payloads may contain:

```json
{"participants": null}
```

The schema describes an array or an omitted field. The generated `Post` model is
corrected to accept `None`, an array, or `UNSET`.

## Reaction creation status

Saving a reaction may return HTTP 200, while the schema documents HTTP 201. The
generated endpoint accepts both success statuses.

## Post idempotency keys

The confirmed deduplicating form is:

```text
<current_user_id>:<millisecond_timestamp>
```

The high-level `send_message()` method creates this form by default. Random
UUIDs and arbitrary `UUID:timestamp` values did not deduplicate posts on the
tested deployment.

Adding `pending_post_id` can disable server-side post deduplication. The
high-level method therefore sends `idempotency_key` without adding
`pending_post_id`.

## Generated schema workarounds

Compatibility transformations live in `scripts/generate_api.py` and are applied
to an in-memory copy of `schema/time-api-v4.yaml`. Generated files must never be
edited manually.

CI verifies that regeneration is reproducible and that all documented
`operationId` values still map to async endpoint modules.

## Forward compatibility

For a future server field:

- generated models preserve it in `additional_properties`;
- handwritten events preserve the complete envelope in `raw`;
- unknown event names become `RawEvent`;
- `TimeClient.raw_request()` can call an endpoint not yet represented by the
  vendored schema.

When reporting a compatibility issue, retain the HTTP status and request ID,
but redact tokens, message content, and sensitive event data.
