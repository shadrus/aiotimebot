from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateNewPostReminderRequest")


@_attrs_define
class CreateNewPostReminderRequest:
    """
    Attributes:
        team_id (str):
        channel_id (str):
        message (str):
        file_ids (list[str]):
        scheduled_at (datetime.datetime):
        day_of_week (list[str]):
        every (str):
        repeats (int):
        till (datetime.datetime):
        root_id (str):
    """

    team_id: str
    channel_id: str
    message: str
    file_ids: list[str]
    scheduled_at: datetime.datetime
    day_of_week: list[str]
    every: str
    repeats: int
    till: datetime.datetime
    root_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        channel_id = self.channel_id

        message = self.message

        file_ids = self.file_ids

        scheduled_at = self.scheduled_at.isoformat()

        day_of_week = self.day_of_week

        every = self.every

        repeats = self.repeats

        till = self.till.isoformat()

        root_id = self.root_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "channel_id": channel_id,
                "message": message,
                "file_ids": file_ids,
                "scheduled_at": scheduled_at,
                "day_of_week": day_of_week,
                "every": every,
                "repeats": repeats,
                "till": till,
                "root_id": root_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        channel_id = d.pop("channel_id")

        message = d.pop("message")

        file_ids = cast(list[str], d.pop("file_ids"))

        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduled_at"))

        day_of_week = cast(list[str], d.pop("day_of_week"))

        every = d.pop("every")

        repeats = d.pop("repeats")

        till = datetime.datetime.fromisoformat(d.pop("till"))

        root_id = d.pop("root_id")

        create_new_post_reminder_request = cls(
            team_id=team_id,
            channel_id=channel_id,
            message=message,
            file_ids=file_ids,
            scheduled_at=scheduled_at,
            day_of_week=day_of_week,
            every=every,
            repeats=repeats,
            till=till,
            root_id=root_id,
        )

        create_new_post_reminder_request.additional_properties = d
        return create_new_post_reminder_request

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
