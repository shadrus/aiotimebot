from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post import Post
    from ..models.user import User


T = TypeVar("T", bound="UserThread")


@_attrs_define
class UserThread:
    """Generated Time Messenger API v4 model."""

    id: str
    reply_count: int
    last_reply_at: int
    last_viewed_at: int
    participants: list[User]
    post: Post
    unread_replies: int
    unread_mentions: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        reply_count = self.reply_count

        last_reply_at = self.last_reply_at

        last_viewed_at = self.last_viewed_at

        participants = []
        for participants_item_data in self.participants:
            participants_item = participants_item_data.to_dict()
            participants.append(participants_item)

        post = self.post.to_dict()

        unread_replies = self.unread_replies

        unread_mentions = self.unread_mentions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "reply_count": reply_count,
                "last_reply_at": last_reply_at,
                "last_viewed_at": last_viewed_at,
                "participants": participants,
                "post": post,
                "unread_replies": unread_replies,
                "unread_mentions": unread_mentions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post import Post
        from ..models.user import User

        d = dict(src_dict)
        id = d.pop("id")

        reply_count = d.pop("reply_count")

        last_reply_at = d.pop("last_reply_at")

        last_viewed_at = d.pop("last_viewed_at")

        participants = []
        _participants = d.pop("participants")
        for participants_item_data in _participants:
            participants_item = User.from_dict(participants_item_data)

            participants.append(participants_item)

        post = Post.from_dict(d.pop("post"))

        unread_replies = d.pop("unread_replies")

        unread_mentions = d.pop("unread_mentions")

        user_thread = cls(
            id=id,
            reply_count=reply_count,
            last_reply_at=last_reply_at,
            last_viewed_at=last_viewed_at,
            participants=participants,
            post=post,
            unread_replies=unread_replies,
            unread_mentions=unread_mentions,
        )

        user_thread.additional_properties = d
        return user_thread

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
