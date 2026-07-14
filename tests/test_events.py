from __future__ import annotations

import json

from aiotimebot.events import EventType, PostedEvent, RawEvent, parse_event

from .conftest import post_payload


def test_posted_event_parses_embedded_post_and_preserves_unknown_fields() -> None:
    raw = {
        "event": "posted",
        "data": {
            "post": json.dumps(
                post_payload(extra={"future_post_field": {"enabled": True}})
            ),
            "sender_name": "alice",
            "future_data_field": 42,
        },
        "broadcast": {
            "channel_id": "channel-1",
            "team_id": "team-1",
            "user_id": "",
            "omit_users": None,
            "future_broadcast_field": "kept",
        },
        "seq": 7,
        "future_envelope_field": [1, 2, 3],
    }

    event = parse_event(raw)

    assert isinstance(event, PostedEvent)
    assert event.type is EventType.POSTED
    assert event.post.id == "post-1"
    assert event.post.message == "hello"
    assert event.post.additional_properties["future_post_field"] == {"enabled": True}
    assert event.channel_id == "channel-1"
    assert event.ordering_key == "channel:channel-1"
    assert event.raw is raw
    assert event.data["future_data_field"] == 42


def test_unknown_event_is_forward_compatible() -> None:
    raw = {
        "event": "a_future_time_event",
        "data": {"value": 1},
        "broadcast": {"user_id": "user-1"},
        "seq": 9,
    }

    event = parse_event(raw)

    assert isinstance(event, RawEvent)
    assert event.name == "a_future_time_event"
    assert event.data == {"value": 1}
    assert event.ordering_key == "user:user-1"
    assert event.raw is raw


def test_event_without_channel_or_user_has_stable_global_ordering_key() -> None:
    event = parse_event(
        {"event": "config_changed", "data": {}, "broadcast": {}, "seq": 1}
    )

    assert event.ordering_key == "global"


def test_malformed_posted_payload_falls_back_to_raw_event() -> None:
    raw = {
        "event": "posted",
        "data": {"post": "not-json"},
        "broadcast": {"channel_id": "channel-1"},
        "seq": 1,
    }

    event = parse_event(raw)

    assert isinstance(event, RawEvent)
    assert event.name == "posted"
    assert event.decode_error is not None
    assert event.raw is raw
