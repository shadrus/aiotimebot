from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UpdateExistsPostReminderRequest")


@_attrs_define
class UpdateExistsPostReminderRequest:
    """
    Attributes:
        reminder_id (str):
        note (str):
        scheduled_at (datetime.datetime):
    """

    reminder_id: str
    note: str
    scheduled_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reminder_id = self.reminder_id

        note = self.note

        scheduled_at = self.scheduled_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reminder_id": reminder_id,
                "note": note,
                "scheduled_at": scheduled_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reminder_id = d.pop("reminder_id")

        note = d.pop("note")

        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduled_at"))

        update_exists_post_reminder_request = cls(
            reminder_id=reminder_id,
            note=note,
            scheduled_at=scheduled_at,
        )

        update_exists_post_reminder_request.additional_properties = d
        return update_exists_post_reminder_request

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
