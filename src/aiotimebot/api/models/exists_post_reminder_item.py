from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExistsPostReminderItem")


@_attrs_define
class ExistsPostReminderItem:
    """
    Attributes:
        scheduled_at (datetime.datetime):
        id (str | Unset):
        post_id (str | Unset):
        note (str | Unset):
    """

    scheduled_at: datetime.datetime
    id: str | Unset = UNSET
    post_id: str | Unset = UNSET
    note: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_at = self.scheduled_at.isoformat()

        id = self.id

        post_id = self.post_id

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduled_at": scheduled_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheduled_at = datetime.datetime.fromisoformat(d.pop("scheduled_at"))

        id = d.pop("id", UNSET)

        post_id = d.pop("post_id", UNSET)

        note = d.pop("note", UNSET)

        exists_post_reminder_item = cls(
            scheduled_at=scheduled_at,
            id=id,
            post_id=post_id,
            note=note,
        )

        exists_post_reminder_item.additional_properties = d
        return exists_post_reminder_item

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
