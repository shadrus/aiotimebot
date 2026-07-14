from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchChannelBody")


@_attrs_define
class PatchChannelBody:
    """Generated Time Messenger API v4 model."""

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    purpose: str | Unset = UNSET
    header: str | Unset = UNSET
    read_receipts: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        purpose = self.purpose

        header = self.header

        read_receipts = self.read_receipts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if header is not UNSET:
            field_dict["header"] = header
        if read_receipts is not UNSET:
            field_dict["read_receipts"] = read_receipts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("display_name", UNSET)

        purpose = d.pop("purpose", UNSET)

        header = d.pop("header", UNSET)

        read_receipts = d.pop("read_receipts", UNSET)

        patch_channel_body = cls(
            name=name,
            display_name=display_name,
            purpose=purpose,
            header=header,
            read_receipts=read_receipts,
        )

        patch_channel_body.additional_properties = d
        return patch_channel_body

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
