from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sort_option import SortOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="FileExtendedSearchParameters")


@_attrs_define
class FileExtendedSearchParameters:
    """Generated Time Messenger API v4 model."""

    is_or_search: bool | Unset = UNSET
    time_zone_offset: int | Unset = 0
    sort_by: SortOption | Unset = UNSET
    size: int | Unset = 60
    offset: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_or_search = self.is_or_search

        time_zone_offset = self.time_zone_offset

        sort_by: str | Unset = UNSET
        if not isinstance(self.sort_by, Unset):
            sort_by = self.sort_by.value

        size = self.size

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_or_search is not UNSET:
            field_dict["is_or_search"] = is_or_search
        if time_zone_offset is not UNSET:
            field_dict["time_zone_offset"] = time_zone_offset
        if sort_by is not UNSET:
            field_dict["sort_by"] = sort_by
        if size is not UNSET:
            field_dict["size"] = size
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_or_search = d.pop("is_or_search", UNSET)

        time_zone_offset = d.pop("time_zone_offset", UNSET)

        _sort_by = d.pop("sort_by", UNSET)
        sort_by: SortOption | Unset
        if isinstance(_sort_by, Unset):
            sort_by = UNSET
        else:
            sort_by = SortOption(_sort_by)

        size = d.pop("size", UNSET)

        offset = d.pop("offset", UNSET)

        file_extended_search_parameters = cls(
            is_or_search=is_or_search,
            time_zone_offset=time_zone_offset,
            sort_by=sort_by,
            size=size,
            offset=offset,
        )

        file_extended_search_parameters.additional_properties = d
        return file_extended_search_parameters

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
