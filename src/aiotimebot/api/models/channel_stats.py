from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChannelStats")


@_attrs_define
class ChannelStats:
    """
    Attributes:
        channel_id (str):
        member_count (int):
        guest_count (int):
        restricted_guest_count (int):
        pinnedpost_count (int):
        files_count (int):
    """

    channel_id: str
    member_count: int
    guest_count: int
    restricted_guest_count: int
    pinnedpost_count: int
    files_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        member_count = self.member_count

        guest_count = self.guest_count

        restricted_guest_count = self.restricted_guest_count

        pinnedpost_count = self.pinnedpost_count

        files_count = self.files_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "member_count": member_count,
                "guest_count": guest_count,
                "restricted_guest_count": restricted_guest_count,
                "pinnedpost_count": pinnedpost_count,
                "files_count": files_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        member_count = d.pop("member_count")

        guest_count = d.pop("guest_count")

        restricted_guest_count = d.pop("restricted_guest_count")

        pinnedpost_count = d.pop("pinnedpost_count")

        files_count = d.pop("files_count")

        channel_stats = cls(
            channel_id=channel_id,
            member_count=member_count,
            guest_count=guest_count,
            restricted_guest_count=restricted_guest_count,
            pinnedpost_count=pinnedpost_count,
            files_count=files_count,
        )

        channel_stats.additional_properties = d
        return channel_stats

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
