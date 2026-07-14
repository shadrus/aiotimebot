"""Typed parsing for Time WebSocket event envelopes."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

from .api.models.post import Post


class EventType(StrEnum):
    """WebSocket event names documented by Time API v4."""

    ADDED_TO_TEAM = "added_to_team"
    AUTHENTICATION_CHALLENGE = "authentication_challenge"
    CHANNEL_CONVERTED = "channel_converted"
    CHANNEL_CREATED = "channel_created"
    CHANNEL_DELETED = "channel_deleted"
    CHANNEL_MEMBER_UPDATED = "channel_member_updated"
    CHANNEL_UPDATED = "channel_updated"
    CHANNEL_VIEWED = "channel_viewed"
    CONFIG_CHANGED = "config_changed"
    DELETE_TEAM = "delete_team"
    DIALOG_OPENED = "dialog_opened"
    DIRECT_ADDED = "direct_added"
    EMOJI_ADDED = "emoji_added"
    EPHEMERAL_MESSAGE = "ephemeral_message"
    FILE_DELETED = "file_deleted"
    GROUP_ADDED = "group_added"
    HELLO = "hello"
    LEAVE_TEAM = "leave_team"
    LICENSE_CHANGED = "license_changed"
    MEMBERROLE_UPDATED = "memberrole_updated"
    NEW_USER = "new_user"
    PLUGIN_DISABLED = "plugin_disabled"
    PLUGIN_ENABLED = "plugin_enabled"
    PLUGIN_STATUSES_CHANGED = "plugin_statuses_changed"
    POST_DELETED = "post_deleted"
    POST_EDITED = "post_edited"
    POST_UNREAD = "post_unread"
    POSTED = "posted"
    PREFERENCE_CHANGED = "preference_changed"
    PREFERENCES_CHANGED = "preferences_changed"
    PREFERENCES_DELETED = "preferences_deleted"
    REACTION_ADDED = "reaction_added"
    REACTION_REMOVED = "reaction_removed"
    RESPONSE = "response"
    ROLE_UPDATED = "role_updated"
    STATUS_CHANGE = "status_change"
    THREAD_FOLLOW_CHANGED = "thread_follow_changed"
    THREAD_READ_CHANGED = "thread_read_changed"
    THREAD_UPDATED = "thread_updated"
    TYPING = "typing"
    UPDATE_TEAM = "update_team"
    USER_ADDED = "user_added"
    USER_REMOVED = "user_removed"
    USER_ROLE_UPDATED = "user_role_updated"
    USER_UPDATED = "user_updated"


@dataclass(frozen=True, slots=True)
class Broadcast:
    """Routing metadata attached to a Time WebSocket event."""

    channel_id: str = ""
    team_id: str = ""
    user_id: str = ""
    omit_users: tuple[str, ...] | None = None
    raw: Mapping[str, Any] | None = None

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any]) -> Broadcast:
        """Parse known fields while retaining unknown broadcast metadata."""
        omitted = payload.get("omit_users")
        omit_users = (
            tuple(str(item) for item in omitted) if isinstance(omitted, list) else None
        )
        return cls(
            channel_id=str(payload.get("channel_id") or ""),
            team_id=str(payload.get("team_id") or ""),
            user_id=str(payload.get("user_id") or ""),
            omit_users=omit_users,
            raw=payload,
        )


@dataclass(frozen=True, slots=True)
class TimeEvent:
    """Base event containing stable routing fields and the original payload."""

    name: str
    data: Mapping[str, Any]
    broadcast: Broadcast
    seq: int
    raw: Mapping[str, Any]

    @property
    def type(self) -> EventType | None:
        """Return a known event enum without rejecting future event names."""
        try:
            return EventType(self.name)
        except ValueError:
            return None

    @property
    def channel_id(self) -> str:
        """Return the channel used for ordered dispatch."""
        return self.broadcast.channel_id

    @property
    def ordering_key(self) -> str:
        """Return a deterministic partition key for ordered processing."""
        if self.broadcast.channel_id:
            return f"channel:{self.broadcast.channel_id}"
        if self.broadcast.user_id:
            return f"user:{self.broadcast.user_id}"
        return "global"


@dataclass(frozen=True, slots=True)
class RawEvent(TimeEvent):
    """A known or future event without a specialized typed data model."""

    decode_error: str | None = None


@dataclass(frozen=True, slots=True)
class PostedEvent(TimeEvent):
    """A new Time post delivered through the `posted` WebSocket event."""

    post: Post


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def parse_event(payload: Mapping[str, Any]) -> TimeEvent:
    """Parse a WebSocket envelope and preserve unsupported payloads as raw."""
    name = str(payload.get("event") or "")
    data = _mapping(payload.get("data"))
    broadcast = Broadcast.from_mapping(_mapping(payload.get("broadcast")))
    raw_sequence = payload.get("seq", 0)
    sequence = raw_sequence if isinstance(raw_sequence, int) else 0
    if name == EventType.POSTED:
        try:
            encoded_post = data["post"]
            post_payload = (
                json.loads(encoded_post)
                if isinstance(encoded_post, str)
                else encoded_post
            )
            if not isinstance(post_payload, Mapping):
                raise TypeError("posted data.post must be an object")
            return PostedEvent(
                name=name,
                data=data,
                broadcast=broadcast,
                seq=sequence,
                raw=payload,
                post=Post.from_dict(post_payload),
            )
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
            return RawEvent(
                name=name,
                data=data,
                broadcast=broadcast,
                seq=sequence,
                raw=payload,
                decode_error=str(error),
            )
    return RawEvent(
        name=name,
        data=data,
        broadcast=broadcast,
        seq=sequence,
        raw=payload,
    )
