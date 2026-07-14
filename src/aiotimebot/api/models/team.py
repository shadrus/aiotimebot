from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Team")


@_attrs_define
class Team:
    """Generated Time Messenger API v4 model."""

    id: str
    create_at: int
    update_at: int
    delete_at: int
    display_name: str
    name: str
    description: str
    email: str
    type_: str
    company_name: str
    allowed_domains: str
    invite_id: str
    allow_open_invite: bool
    last_team_icon_update: int | Unset = UNSET
    scheme_id: str | Unset = UNSET
    group_constrained: bool | Unset = UNSET
    policy_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        create_at = self.create_at

        update_at = self.update_at

        delete_at = self.delete_at

        display_name = self.display_name

        name = self.name

        description = self.description

        email = self.email

        type_ = self.type_

        company_name = self.company_name

        allowed_domains = self.allowed_domains

        invite_id = self.invite_id

        allow_open_invite = self.allow_open_invite

        last_team_icon_update = self.last_team_icon_update

        scheme_id = self.scheme_id

        group_constrained = self.group_constrained

        policy_id = self.policy_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "create_at": create_at,
                "update_at": update_at,
                "delete_at": delete_at,
                "display_name": display_name,
                "name": name,
                "description": description,
                "email": email,
                "type": type_,
                "company_name": company_name,
                "allowed_domains": allowed_domains,
                "invite_id": invite_id,
                "allow_open_invite": allow_open_invite,
            }
        )
        if last_team_icon_update is not UNSET:
            field_dict["last_team_icon_update"] = last_team_icon_update
        if scheme_id is not UNSET:
            field_dict["scheme_id"] = scheme_id
        if group_constrained is not UNSET:
            field_dict["group_constrained"] = group_constrained
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        create_at = d.pop("create_at")

        update_at = d.pop("update_at")

        delete_at = d.pop("delete_at")

        display_name = d.pop("display_name")

        name = d.pop("name")

        description = d.pop("description")

        email = d.pop("email")

        type_ = d.pop("type")

        company_name = d.pop("company_name")

        allowed_domains = d.pop("allowed_domains")

        invite_id = d.pop("invite_id")

        allow_open_invite = d.pop("allow_open_invite")

        last_team_icon_update = d.pop("last_team_icon_update", UNSET)

        scheme_id = d.pop("scheme_id", UNSET)

        group_constrained = d.pop("group_constrained", UNSET)

        policy_id = d.pop("policy_id", UNSET)

        team = cls(
            id=id,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
            display_name=display_name,
            name=name,
            description=description,
            email=email,
            type_=type_,
            company_name=company_name,
            allowed_domains=allowed_domains,
            invite_id=invite_id,
            allow_open_invite=allow_open_invite,
            last_team_icon_update=last_team_icon_update,
            scheme_id=scheme_id,
            group_constrained=group_constrained,
            policy_id=policy_id,
        )

        team.additional_properties = d
        return team

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
