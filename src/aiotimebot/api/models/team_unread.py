from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TeamUnread")


@_attrs_define
class TeamUnread:
    """
    Attributes:
        team_id (str):
        msg_count (int):
        mention_count (int):
        mention_count_root (int):
        msg_count_root (int):
        thread_count (int):
        thread_mention_count (int):
    """

    team_id: str
    msg_count: int
    mention_count: int
    mention_count_root: int
    msg_count_root: int
    thread_count: int
    thread_mention_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        msg_count = self.msg_count

        mention_count = self.mention_count

        mention_count_root = self.mention_count_root

        msg_count_root = self.msg_count_root

        thread_count = self.thread_count

        thread_mention_count = self.thread_mention_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "msg_count": msg_count,
                "mention_count": mention_count,
                "mention_count_root": mention_count_root,
                "msg_count_root": msg_count_root,
                "thread_count": thread_count,
                "thread_mention_count": thread_mention_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        msg_count = d.pop("msg_count")

        mention_count = d.pop("mention_count")

        mention_count_root = d.pop("mention_count_root")

        msg_count_root = d.pop("msg_count_root")

        thread_count = d.pop("thread_count")

        thread_mention_count = d.pop("thread_mention_count")

        team_unread = cls(
            team_id=team_id,
            msg_count=msg_count,
            mention_count=mention_count,
            mention_count_root=mention_count_root,
            msg_count_root=msg_count_root,
            thread_count=thread_count,
            thread_mention_count=thread_mention_count,
        )

        team_unread.additional_properties = d
        return team_unread

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
