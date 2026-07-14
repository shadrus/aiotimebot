from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PushNotificationAck")


@_attrs_define
class PushNotificationAck:
    """Generated Time Messenger API v4 model."""

    id: str
    platform: str
    type_: str
    received_at: int | Unset = UNSET
    post_id: str | Unset = UNSET
    is_id_loaded: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        platform = self.platform

        type_ = self.type_

        received_at = self.received_at

        post_id = self.post_id

        is_id_loaded = self.is_id_loaded

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "platform": platform,
                "type": type_,
            }
        )
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if is_id_loaded is not UNSET:
            field_dict["is_id_loaded"] = is_id_loaded

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        platform = d.pop("platform")

        type_ = d.pop("type")

        received_at = d.pop("received_at", UNSET)

        post_id = d.pop("post_id", UNSET)

        is_id_loaded = d.pop("is_id_loaded", UNSET)

        push_notification_ack = cls(
            id=id,
            platform=platform,
            type_=type_,
            received_at=received_at,
            post_id=post_id,
            is_id_loaded=is_id_loaded,
        )

        push_notification_ack.additional_properties = d
        return push_notification_ack

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
