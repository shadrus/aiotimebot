from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelUnreadAt")


@_attrs_define
class ChannelUnreadAt:
    """Generated Time Messenger API v4 model."""

    team_id: str
    channel_id: str
    msg_count: int
    msg_count_root: int
    mention_count: int
    mention_count_root: int
    last_viewed_at: int
    user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        channel_id = self.channel_id

        msg_count = self.msg_count

        msg_count_root = self.msg_count_root

        mention_count = self.mention_count

        mention_count_root = self.mention_count_root

        last_viewed_at = self.last_viewed_at

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "channel_id": channel_id,
                "msg_count": msg_count,
                "msg_count_root": msg_count_root,
                "mention_count": mention_count,
                "mention_count_root": mention_count_root,
                "last_viewed_at": last_viewed_at,
            }
        )
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        channel_id = d.pop("channel_id")

        msg_count = d.pop("msg_count")

        msg_count_root = d.pop("msg_count_root")

        mention_count = d.pop("mention_count")

        mention_count_root = d.pop("mention_count_root")

        last_viewed_at = d.pop("last_viewed_at")

        user_id = d.pop("user_id", UNSET)

        channel_unread_at = cls(
            team_id=team_id,
            channel_id=channel_id,
            msg_count=msg_count,
            msg_count_root=msg_count_root,
            mention_count=mention_count,
            mention_count_root=mention_count_root,
            last_viewed_at=last_viewed_at,
            user_id=user_id,
        )

        channel_unread_at.additional_properties = d
        return channel_unread_at

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
