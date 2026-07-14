from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchUsersBody")


@_attrs_define
class SearchUsersBody:
    """Generated Time Messenger API v4 model."""

    term: str
    team_id: str | Unset = UNSET
    not_in_team_id: str | Unset = UNSET
    in_channel_id: str | Unset = UNSET
    not_in_channel_id: str | Unset = UNSET
    in_group_id: str | Unset = UNSET
    group_constrained: bool | Unset = UNSET
    allow_inactive: bool | Unset = UNSET
    without_team: bool | Unset = UNSET
    limit: int | Unset = 100
    with_profiles: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        team_id = self.team_id

        not_in_team_id = self.not_in_team_id

        in_channel_id = self.in_channel_id

        not_in_channel_id = self.not_in_channel_id

        in_group_id = self.in_group_id

        group_constrained = self.group_constrained

        allow_inactive = self.allow_inactive

        without_team = self.without_team

        limit = self.limit

        with_profiles = self.with_profiles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if not_in_team_id is not UNSET:
            field_dict["not_in_team_id"] = not_in_team_id
        if in_channel_id is not UNSET:
            field_dict["in_channel_id"] = in_channel_id
        if not_in_channel_id is not UNSET:
            field_dict["not_in_channel_id"] = not_in_channel_id
        if in_group_id is not UNSET:
            field_dict["in_group_id"] = in_group_id
        if group_constrained is not UNSET:
            field_dict["group_constrained"] = group_constrained
        if allow_inactive is not UNSET:
            field_dict["allow_inactive"] = allow_inactive
        if without_team is not UNSET:
            field_dict["without_team"] = without_team
        if limit is not UNSET:
            field_dict["limit"] = limit
        if with_profiles is not UNSET:
            field_dict["with_profiles"] = with_profiles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term")

        team_id = d.pop("team_id", UNSET)

        not_in_team_id = d.pop("not_in_team_id", UNSET)

        in_channel_id = d.pop("in_channel_id", UNSET)

        not_in_channel_id = d.pop("not_in_channel_id", UNSET)

        in_group_id = d.pop("in_group_id", UNSET)

        group_constrained = d.pop("group_constrained", UNSET)

        allow_inactive = d.pop("allow_inactive", UNSET)

        without_team = d.pop("without_team", UNSET)

        limit = d.pop("limit", UNSET)

        with_profiles = d.pop("with_profiles", UNSET)

        search_users_body = cls(
            term=term,
            team_id=team_id,
            not_in_team_id=not_in_team_id,
            in_channel_id=in_channel_id,
            not_in_channel_id=not_in_channel_id,
            in_group_id=in_group_id,
            group_constrained=group_constrained,
            allow_inactive=allow_inactive,
            without_team=without_team,
            limit=limit,
            with_profiles=with_profiles,
        )

        search_users_body.additional_properties = d
        return search_users_body

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
