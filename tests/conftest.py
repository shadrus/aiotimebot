from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def post_payload(
    *,
    post_id: str = "post-1",
    channel_id: str = "channel-1",
    message: str = "hello",
    extra: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a complete Post payload matching the Time v4 schema."""
    payload: dict[str, Any] = {
        "id": post_id,
        "create_at": 1,
        "update_at": 1,
        "edit_at": 0,
        "delete_at": 0,
        "is_pinned": False,
        "user_id": "user-1",
        "channel_id": channel_id,
        "root_id": "",
        "original_id": "",
        "message": message,
        "type": "",
        "props": {},
        "hashtags": "",
        "pending_post_id": "",
        "idempotency_key": "request-1",
        "reply_count": 0,
        "last_reply_at": 0,
    }
    if extra:
        payload.update(extra)
    return payload
