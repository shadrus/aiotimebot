from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateOutgoingWebhookBody")


@_attrs_define
class CreateOutgoingWebhookBody:
    """Generated Time Messenger API v4 model."""

    team_id: str
    display_name: str
    trigger_words: list[str]
    callback_urls: list[str]
    channel_id: str | Unset = UNSET
    creator_id: str | Unset = UNSET
    description: str | Unset = UNSET
    trigger_when: int | Unset = UNSET
    content_type: str | Unset = "application/x-www-form-urlencoded"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        display_name = self.display_name

        trigger_words = self.trigger_words

        callback_urls = self.callback_urls

        channel_id = self.channel_id

        creator_id = self.creator_id

        description = self.description

        trigger_when = self.trigger_when

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "display_name": display_name,
                "trigger_words": trigger_words,
                "callback_urls": callback_urls,
            }
        )
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if description is not UNSET:
            field_dict["description"] = description
        if trigger_when is not UNSET:
            field_dict["trigger_when"] = trigger_when
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        team_id = d.pop("team_id")

        display_name = d.pop("display_name")

        trigger_words = cast(list[str], d.pop("trigger_words"))

        callback_urls = cast(list[str], d.pop("callback_urls"))

        channel_id = d.pop("channel_id", UNSET)

        creator_id = d.pop("creator_id", UNSET)

        description = d.pop("description", UNSET)

        trigger_when = d.pop("trigger_when", UNSET)

        content_type = d.pop("content_type", UNSET)

        create_outgoing_webhook_body = cls(
            team_id=team_id,
            display_name=display_name,
            trigger_words=trigger_words,
            callback_urls=callback_urls,
            channel_id=channel_id,
            creator_id=creator_id,
            description=description,
            trigger_when=trigger_when,
            content_type=content_type,
        )

        create_outgoing_webhook_body.additional_properties = d
        return create_outgoing_webhook_body

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
