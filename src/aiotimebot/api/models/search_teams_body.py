from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchTeamsBody")


@_attrs_define
class SearchTeamsBody:
    """Generated Time Messenger API v4 model."""

    term: str | Unset = UNSET
    page: str | Unset = UNSET
    per_page: str | Unset = UNSET
    allow_open_invite: bool | Unset = UNSET
    group_constrained: bool | Unset = UNSET
    exclude_policy_constrained: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        page = self.page

        per_page = self.per_page

        allow_open_invite = self.allow_open_invite

        group_constrained = self.group_constrained

        exclude_policy_constrained = self.exclude_policy_constrained

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if allow_open_invite is not UNSET:
            field_dict["allow_open_invite"] = allow_open_invite
        if group_constrained is not UNSET:
            field_dict["group_constrained"] = group_constrained
        if exclude_policy_constrained is not UNSET:
            field_dict["exclude_policy_constrained"] = exclude_policy_constrained

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term", UNSET)

        page = d.pop("page", UNSET)

        per_page = d.pop("per_page", UNSET)

        allow_open_invite = d.pop("allow_open_invite", UNSET)

        group_constrained = d.pop("group_constrained", UNSET)

        exclude_policy_constrained = d.pop("exclude_policy_constrained", UNSET)

        search_teams_body = cls(
            term=term,
            page=page,
            per_page=per_page,
            allow_open_invite=allow_open_invite,
            group_constrained=group_constrained,
            exclude_policy_constrained=exclude_policy_constrained,
        )

        search_teams_body.additional_properties = d
        return search_teams_body

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
