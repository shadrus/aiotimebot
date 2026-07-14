from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReminderExistsPostCreateBody")


@_attrs_define
class ReminderExistsPostCreateBody:
    """Generated Time Messenger API v4 model."""

    team_id: str
    channel_id: str
    post_id: str
    scheduled_at: datetime.datetime
    root_id: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        channel_id = self.channel_id

        post_id = self.post_id

        scheduled_at = self.scheduled_at.isoformat()

        root_id = self.root_id

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "channel_id": channel_id,
                "post_id": post_id,
                "scheduled_at": scheduled_at,
            }
        )
        if root_id is not UNSET:
            field_dict["root_id"] = root_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        channel_id = d.pop("channel_id")

        post_id = d.pop("post_id")

        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduled_at"))

        root_id = d.pop("root_id", UNSET)

        note = d.pop("note", UNSET)

        reminder_exists_post_create_body = cls(
            team_id=team_id,
            channel_id=channel_id,
            post_id=post_id,
            scheduled_at=scheduled_at,
            root_id=root_id,
            note=note,
        )

        reminder_exists_post_create_body.additional_properties = d
        return reminder_exists_post_create_body

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
