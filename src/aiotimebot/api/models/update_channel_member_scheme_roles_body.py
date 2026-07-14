from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateChannelMemberSchemeRolesBody")


@_attrs_define
class UpdateChannelMemberSchemeRolesBody:
    """
    Attributes:
        scheme_admin (bool | Unset):
        scheme_user (bool | Unset):
        scheme_guest (bool | Unset):
    """

    scheme_admin: bool | Unset = UNSET
    scheme_user: bool | Unset = UNSET
    scheme_guest: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheme_admin = self.scheme_admin

        scheme_user = self.scheme_user

        scheme_guest = self.scheme_guest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if scheme_admin is not UNSET:
            field_dict["scheme_admin"] = scheme_admin
        if scheme_user is not UNSET:
            field_dict["scheme_user"] = scheme_user
        if scheme_guest is not UNSET:
            field_dict["scheme_guest"] = scheme_guest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheme_admin = d.pop("scheme_admin", UNSET)

        scheme_user = d.pop("scheme_user", UNSET)

        scheme_guest = d.pop("scheme_guest", UNSET)

        update_channel_member_scheme_roles_body = cls(
            scheme_admin=scheme_admin,
            scheme_user=scheme_user,
            scheme_guest=scheme_guest,
        )

        update_channel_member_scheme_roles_body.additional_properties = d
        return update_channel_member_scheme_roles_body

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
