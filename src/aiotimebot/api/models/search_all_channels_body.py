from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchAllChannelsBody")


@_attrs_define
class SearchAllChannelsBody:
    """Generated Time Messenger API v4 model."""

    term: str
    not_associated_to_group: str | Unset = UNSET
    team_ids: list[str] | Unset = UNSET
    group_constrained: bool | Unset = UNSET
    exclude_group_constrained: bool | Unset = UNSET
    public: bool | Unset = UNSET
    private: bool | Unset = UNSET
    deleted: bool | Unset = UNSET
    page: str | Unset = UNSET
    per_page: str | Unset = UNSET
    exclude_policy_constrained: bool | Unset = False
    include_search_by_id: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        not_associated_to_group = self.not_associated_to_group

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        group_constrained = self.group_constrained

        exclude_group_constrained = self.exclude_group_constrained

        public = self.public

        private = self.private

        deleted = self.deleted

        page = self.page

        per_page = self.per_page

        exclude_policy_constrained = self.exclude_policy_constrained

        include_search_by_id = self.include_search_by_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )
        if not_associated_to_group is not UNSET:
            field_dict["not_associated_to_group"] = not_associated_to_group
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if group_constrained is not UNSET:
            field_dict["group_constrained"] = group_constrained
        if exclude_group_constrained is not UNSET:
            field_dict["exclude_group_constrained"] = exclude_group_constrained
        if public is not UNSET:
            field_dict["public"] = public
        if private is not UNSET:
            field_dict["private"] = private
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if page is not UNSET:
            field_dict["page"] = page
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if exclude_policy_constrained is not UNSET:
            field_dict["exclude_policy_constrained"] = exclude_policy_constrained
        if include_search_by_id is not UNSET:
            field_dict["include_search_by_id"] = include_search_by_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term")

        not_associated_to_group = d.pop("not_associated_to_group", UNSET)

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

        group_constrained = d.pop("group_constrained", UNSET)

        exclude_group_constrained = d.pop("exclude_group_constrained", UNSET)

        public = d.pop("public", UNSET)

        private = d.pop("private", UNSET)

        deleted = d.pop("deleted", UNSET)

        page = d.pop("page", UNSET)

        per_page = d.pop("per_page", UNSET)

        exclude_policy_constrained = d.pop("exclude_policy_constrained", UNSET)

        include_search_by_id = d.pop("include_search_by_id", UNSET)

        search_all_channels_body = cls(
            term=term,
            not_associated_to_group=not_associated_to_group,
            team_ids=team_ids,
            group_constrained=group_constrained,
            exclude_group_constrained=exclude_group_constrained,
            public=public,
            private=private,
            deleted=deleted,
            page=page,
            per_page=per_page,
            exclude_policy_constrained=exclude_policy_constrained,
            include_search_by_id=include_search_by_id,
        )

        search_all_channels_body.additional_properties = d
        return search_all_channels_body

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
