from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchChannelsForRetentionPolicyBody")


@_attrs_define
class SearchChannelsForRetentionPolicyBody:
    """Generated Time Messenger API v4 model."""

    term: str | Unset = UNSET
    team_ids: list[str] | Unset = UNSET
    public: bool | Unset = UNSET
    private: bool | Unset = UNSET
    deleted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        public = self.public

        private = self.private

        deleted = self.deleted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if term is not UNSET:
            field_dict["term"] = term
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if public is not UNSET:
            field_dict["public"] = public
        if private is not UNSET:
            field_dict["private"] = private
        if deleted is not UNSET:
            field_dict["deleted"] = deleted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term", UNSET)

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

        public = d.pop("public", UNSET)

        private = d.pop("private", UNSET)

        deleted = d.pop("deleted", UNSET)

        search_channels_for_retention_policy_body = cls(
            term=term,
            team_ids=team_ids,
            public=public,
            private=private,
            deleted=deleted,
        )

        search_channels_for_retention_policy_body.additional_properties = d
        return search_channels_for_retention_policy_body

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
