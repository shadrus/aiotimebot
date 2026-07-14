from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetChannelMemberCountsByGroupIDsBody")


@_attrs_define
class GetChannelMemberCountsByGroupIDsBody:
    """Generated Time Messenger API v4 model."""

    group_ids: list[str]
    include_timezones: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_ids = self.group_ids

        include_timezones = self.include_timezones

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "group_ids": group_ids,
            }
        )
        if include_timezones is not UNSET:
            field_dict["include_timezones"] = include_timezones

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        group_ids = cast(list[str], d.pop("group_ids"))

        include_timezones = d.pop("include_timezones", UNSET)

        get_channel_member_counts_by_group_i_ds_body = cls(
            group_ids=group_ids,
            include_timezones=include_timezones,
        )

        get_channel_member_counts_by_group_i_ds_body.additional_properties = d
        return get_channel_member_counts_by_group_i_ds_body

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
