from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LicenseUsage")


@_attrs_define
class LicenseUsage:
    """Generated Time Messenger API v4 model."""

    active_users: int | Unset = UNSET
    license_users: int | Unset = UNSET
    active_restricted_guests: int | Unset = UNSET
    license_restricted_guests: int | Unset = UNSET
    active_guests: int | Unset = UNSET
    license_guests: int | Unset = UNSET
    license_id: str | Unset = UNSET
    system_admins: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active_users = self.active_users

        license_users = self.license_users

        active_restricted_guests = self.active_restricted_guests

        license_restricted_guests = self.license_restricted_guests

        active_guests = self.active_guests

        license_guests = self.license_guests

        license_id = self.license_id

        system_admins = self.system_admins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active_users is not UNSET:
            field_dict["active_users"] = active_users
        if license_users is not UNSET:
            field_dict["license_users"] = license_users
        if active_restricted_guests is not UNSET:
            field_dict["active_restricted_guests"] = active_restricted_guests
        if license_restricted_guests is not UNSET:
            field_dict["license_restricted_guests"] = license_restricted_guests
        if active_guests is not UNSET:
            field_dict["active_guests"] = active_guests
        if license_guests is not UNSET:
            field_dict["license_guests"] = license_guests
        if license_id is not UNSET:
            field_dict["license_id"] = license_id
        if system_admins is not UNSET:
            field_dict["system_admins"] = system_admins

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        active_users = d.pop("active_users", UNSET)

        license_users = d.pop("license_users", UNSET)

        active_restricted_guests = d.pop("active_restricted_guests", UNSET)

        license_restricted_guests = d.pop("license_restricted_guests", UNSET)

        active_guests = d.pop("active_guests", UNSET)

        license_guests = d.pop("license_guests", UNSET)

        license_id = d.pop("license_id", UNSET)

        system_admins = d.pop("system_admins", UNSET)

        license_usage = cls(
            active_users=active_users,
            license_users=license_users,
            active_restricted_guests=active_restricted_guests,
            license_restricted_guests=license_restricted_guests,
            active_guests=active_guests,
            license_guests=license_guests,
            license_id=license_id,
            system_admins=system_admins,
        )

        license_usage.additional_properties = d
        return license_usage

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
