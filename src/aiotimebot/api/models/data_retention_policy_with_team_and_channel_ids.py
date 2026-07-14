from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataRetentionPolicyWithTeamAndChannelIds")


@_attrs_define
class DataRetentionPolicyWithTeamAndChannelIds:
    """Generated Time Messenger API v4 model."""

    display_name: str | Unset = UNSET
    post_duration: int | Unset = UNSET
    team_ids: list[str] | Unset = UNSET
    channel_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        post_duration = self.post_duration

        team_ids: list[str] | Unset = UNSET
        if not isinstance(self.team_ids, Unset):
            team_ids = self.team_ids

        channel_ids: list[str] | Unset = UNSET
        if not isinstance(self.channel_ids, Unset):
            channel_ids = self.channel_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if post_duration is not UNSET:
            field_dict["post_duration"] = post_duration
        if team_ids is not UNSET:
            field_dict["team_ids"] = team_ids
        if channel_ids is not UNSET:
            field_dict["channel_ids"] = channel_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        display_name = d.pop("display_name", UNSET)

        post_duration = d.pop("post_duration", UNSET)

        team_ids = cast(list[str], d.pop("team_ids", UNSET))

        channel_ids = cast(list[str], d.pop("channel_ids", UNSET))

        data_retention_policy_with_team_and_channel_ids = cls(
            display_name=display_name,
            post_duration=post_duration,
            team_ids=team_ids,
            channel_ids=channel_ids,
        )

        data_retention_policy_with_team_and_channel_ids.additional_properties = d
        return data_retention_policy_with_team_and_channel_ids

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
