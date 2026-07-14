from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetGroupsByNamesBody")


@_attrs_define
class GetGroupsByNamesBody:
    """
    Attributes:
        names (list[str]):
        filter_allow_reference (bool | Unset):  Default: True.
        include_member_count (bool | Unset):  Default: False.
    """

    names: list[str]
    filter_allow_reference: bool | Unset = True
    include_member_count: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        names = self.names

        filter_allow_reference = self.filter_allow_reference

        include_member_count = self.include_member_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "names": names,
            }
        )
        if filter_allow_reference is not UNSET:
            field_dict["filter_allow_reference"] = filter_allow_reference
        if include_member_count is not UNSET:
            field_dict["include_member_count"] = include_member_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        names = cast(list[str], d.pop("names"))

        filter_allow_reference = d.pop("filter_allow_reference", UNSET)

        include_member_count = d.pop("include_member_count", UNSET)

        get_groups_by_names_body = cls(
            names=names,
            filter_allow_reference=filter_allow_reference,
            include_member_count=include_member_count,
        )

        get_groups_by_names_body.additional_properties = d
        return get_groups_by_names_body

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
