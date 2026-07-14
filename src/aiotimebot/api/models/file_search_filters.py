from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileSearchFilters")


@_attrs_define
class FileSearchFilters:
    """Generated Time Messenger API v4 model."""

    in_channels: list[str] | Unset = UNSET
    excluded_channels: list[str] | Unset = UNSET
    from_users: list[str] | Unset = UNSET
    excluded_users: list[str] | Unset = UNSET
    after_date: datetime.date | Unset = UNSET
    excluded_after_date: datetime.date | Unset = UNSET
    before_date: datetime.date | Unset = UNSET
    excluded_before_date: datetime.date | Unset = UNSET
    on_date: datetime.date | Unset = UNSET
    excluded_date: datetime.date | Unset = UNSET
    extensions: list[str] | Unset = UNSET
    excluded_extensions: list[str] | Unset = UNSET
    include_deleted_channels: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_channels: list[str] | Unset = UNSET
        if not isinstance(self.in_channels, Unset):
            in_channels = self.in_channels

        excluded_channels: list[str] | Unset = UNSET
        if not isinstance(self.excluded_channels, Unset):
            excluded_channels = self.excluded_channels

        from_users: list[str] | Unset = UNSET
        if not isinstance(self.from_users, Unset):
            from_users = self.from_users

        excluded_users: list[str] | Unset = UNSET
        if not isinstance(self.excluded_users, Unset):
            excluded_users = self.excluded_users

        after_date: str | Unset = UNSET
        if not isinstance(self.after_date, Unset):
            after_date = self.after_date.isoformat()

        excluded_after_date: str | Unset = UNSET
        if not isinstance(self.excluded_after_date, Unset):
            excluded_after_date = self.excluded_after_date.isoformat()

        before_date: str | Unset = UNSET
        if not isinstance(self.before_date, Unset):
            before_date = self.before_date.isoformat()

        excluded_before_date: str | Unset = UNSET
        if not isinstance(self.excluded_before_date, Unset):
            excluded_before_date = self.excluded_before_date.isoformat()

        on_date: str | Unset = UNSET
        if not isinstance(self.on_date, Unset):
            on_date = self.on_date.isoformat()

        excluded_date: str | Unset = UNSET
        if not isinstance(self.excluded_date, Unset):
            excluded_date = self.excluded_date.isoformat()

        extensions: list[str] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions

        excluded_extensions: list[str] | Unset = UNSET
        if not isinstance(self.excluded_extensions, Unset):
            excluded_extensions = self.excluded_extensions

        include_deleted_channels = self.include_deleted_channels

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_channels is not UNSET:
            field_dict["in_channels"] = in_channels
        if excluded_channels is not UNSET:
            field_dict["excluded_channels"] = excluded_channels
        if from_users is not UNSET:
            field_dict["from_users"] = from_users
        if excluded_users is not UNSET:
            field_dict["excluded_users"] = excluded_users
        if after_date is not UNSET:
            field_dict["after_date"] = after_date
        if excluded_after_date is not UNSET:
            field_dict["excluded_after_date"] = excluded_after_date
        if before_date is not UNSET:
            field_dict["before_date"] = before_date
        if excluded_before_date is not UNSET:
            field_dict["excluded_before_date"] = excluded_before_date
        if on_date is not UNSET:
            field_dict["on_date"] = on_date
        if excluded_date is not UNSET:
            field_dict["excluded_date"] = excluded_date
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if excluded_extensions is not UNSET:
            field_dict["excluded_extensions"] = excluded_extensions
        if include_deleted_channels is not UNSET:
            field_dict["include_deleted_channels"] = include_deleted_channels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_channels = cast(list[str], d.pop("in_channels", UNSET))

        excluded_channels = cast(list[str], d.pop("excluded_channels", UNSET))

        from_users = cast(list[str], d.pop("from_users", UNSET))

        excluded_users = cast(list[str], d.pop("excluded_users", UNSET))

        _after_date = d.pop("after_date", UNSET)
        after_date: datetime.date | Unset
        if isinstance(_after_date, Unset):
            after_date = UNSET
        else:
            after_date = datetime.date.fromisoformat(_after_date)

        _excluded_after_date = d.pop("excluded_after_date", UNSET)
        excluded_after_date: datetime.date | Unset
        if isinstance(_excluded_after_date, Unset):
            excluded_after_date = UNSET
        else:
            excluded_after_date = datetime.date.fromisoformat(_excluded_after_date)

        _before_date = d.pop("before_date", UNSET)
        before_date: datetime.date | Unset
        if isinstance(_before_date, Unset):
            before_date = UNSET
        else:
            before_date = datetime.date.fromisoformat(_before_date)

        _excluded_before_date = d.pop("excluded_before_date", UNSET)
        excluded_before_date: datetime.date | Unset
        if isinstance(_excluded_before_date, Unset):
            excluded_before_date = UNSET
        else:
            excluded_before_date = datetime.date.fromisoformat(_excluded_before_date)

        _on_date = d.pop("on_date", UNSET)
        on_date: datetime.date | Unset
        if isinstance(_on_date, Unset):
            on_date = UNSET
        else:
            on_date = datetime.date.fromisoformat(_on_date)

        _excluded_date = d.pop("excluded_date", UNSET)
        excluded_date: datetime.date | Unset
        if isinstance(_excluded_date, Unset):
            excluded_date = UNSET
        else:
            excluded_date = datetime.date.fromisoformat(_excluded_date)

        extensions = cast(list[str], d.pop("extensions", UNSET))

        excluded_extensions = cast(list[str], d.pop("excluded_extensions", UNSET))

        include_deleted_channels = d.pop("include_deleted_channels", UNSET)

        file_search_filters = cls(
            in_channels=in_channels,
            excluded_channels=excluded_channels,
            from_users=from_users,
            excluded_users=excluded_users,
            after_date=after_date,
            excluded_after_date=excluded_after_date,
            before_date=before_date,
            excluded_before_date=excluded_before_date,
            on_date=on_date,
            excluded_date=excluded_date,
            extensions=extensions,
            excluded_extensions=excluded_extensions,
            include_deleted_channels=include_deleted_channels,
        )

        file_search_filters.additional_properties = d
        return file_search_filters

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
