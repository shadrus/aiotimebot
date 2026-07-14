from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TeamMember")


@_attrs_define
class TeamMember:
    """Generated Time Messenger API v4 model."""

    team_id: str
    user_id: str
    roles: str
    delete_at: int
    scheme_restricted_guest: bool
    scheme_guest: bool
    scheme_user: bool
    scheme_admin: bool
    explicit_roles: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        user_id = self.user_id

        roles = self.roles

        delete_at = self.delete_at

        scheme_restricted_guest = self.scheme_restricted_guest

        scheme_guest = self.scheme_guest

        scheme_user = self.scheme_user

        scheme_admin = self.scheme_admin

        explicit_roles = self.explicit_roles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "user_id": user_id,
                "roles": roles,
                "delete_at": delete_at,
                "scheme_restricted_guest": scheme_restricted_guest,
                "scheme_guest": scheme_guest,
                "scheme_user": scheme_user,
                "scheme_admin": scheme_admin,
                "explicit_roles": explicit_roles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        user_id = d.pop("user_id")

        roles = d.pop("roles")

        delete_at = d.pop("delete_at")

        scheme_restricted_guest = d.pop("scheme_restricted_guest")

        scheme_guest = d.pop("scheme_guest")

        scheme_user = d.pop("scheme_user")

        scheme_admin = d.pop("scheme_admin")

        explicit_roles = d.pop("explicit_roles")

        team_member = cls(
            team_id=team_id,
            user_id=user_id,
            roles=roles,
            delete_at=delete_at,
            scheme_restricted_guest=scheme_restricted_guest,
            scheme_guest=scheme_guest,
            scheme_user=scheme_user,
            scheme_admin=scheme_admin,
            explicit_roles=explicit_roles,
        )

        team_member.additional_properties = d
        return team_member

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
