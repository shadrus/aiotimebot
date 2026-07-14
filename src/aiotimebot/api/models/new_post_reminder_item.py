from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewPostReminderItem")


@_attrs_define
class NewPostReminderItem:
    """
    Attributes:
        scheduled_at (datetime.datetime):
        id (str | Unset):
        channel_id (str | Unset):
        message (str | Unset):
        file_id (list[str] | Unset):
    """

    scheduled_at: datetime.datetime
    id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    message: str | Unset = UNSET
    file_id: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_at = self.scheduled_at.isoformat()

        id = self.id

        channel_id = self.channel_id

        message = self.message

        file_id: list[str] | Unset = UNSET
        if not isinstance(self.file_id, Unset):
            file_id = self.file_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduled_at": scheduled_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if message is not UNSET:
            field_dict["message"] = message
        if file_id is not UNSET:
            field_dict["file_id"] = file_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduled_at"))

        id = d.pop("id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        message = d.pop("message", UNSET)

        file_id = cast(list[str], d.pop("file_id", UNSET))

        new_post_reminder_item = cls(
            scheduled_at=scheduled_at,
            id=id,
            channel_id=channel_id,
            message=message,
            file_id=file_id,
        )

        new_post_reminder_item.additional_properties = d
        return new_post_reminder_item

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
