from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopChannel")


@_attrs_define
class TopChannel:
    """Generated Time Messenger API v4 model."""

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    display_name: str | Unset = UNSET
    name: str | Unset = UNSET
    team_id: str | Unset = UNSET
    message_count: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        display_name = self.display_name

        name = self.name

        team_id = self.team_id

        message_count = self.message_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if name is not UNSET:
            field_dict["name"] = name
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if message_count is not UNSET:
            field_dict["message_count"] = message_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        display_name = d.pop("display_name", UNSET)

        name = d.pop("name", UNSET)

        team_id = d.pop("team_id", UNSET)

        message_count = d.pop("message_count", UNSET)

        top_channel = cls(
            id=id,
            type_=type_,
            display_name=display_name,
            name=name,
            team_id=team_id,
            message_count=message_count,
        )

        top_channel.additional_properties = d
        return top_channel

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
