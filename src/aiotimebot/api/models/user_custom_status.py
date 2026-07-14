from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status_duration import StatusDuration
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserCustomStatus")


@_attrs_define
class UserCustomStatus:
    """Generated Time Messenger API v4 model."""

    emoji: str
    text: str
    expires_at: str
    duration: StatusDuration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emoji = self.emoji

        text = self.text

        expires_at = self.expires_at

        duration: str | Unset = UNSET
        if not isinstance(self.duration, Unset):
            duration = self.duration.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emoji": emoji,
                "text": text,
                "expires_at": expires_at,
            }
        )
        if duration is not UNSET:
            field_dict["duration"] = duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        emoji = d.pop("emoji")

        text = d.pop("text")

        expires_at = d.pop("expires_at")

        _duration = d.pop("duration", UNSET)
        duration: StatusDuration | Unset
        if isinstance(_duration, Unset):
            duration = UNSET
        else:
            duration = StatusDuration(_duration)

        user_custom_status = cls(
            emoji=emoji,
            text=text,
            expires_at=expires_at,
            duration=duration,
        )

        user_custom_status.additional_properties = d
        return user_custom_status

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
