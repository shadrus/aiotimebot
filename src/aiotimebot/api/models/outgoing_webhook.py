from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutgoingWebhook")


@_attrs_define
class OutgoingWebhook:
    """Generated Time Messenger API v4 model."""

    id: str | Unset = UNSET
    create_at: int | Unset = UNSET
    update_at: int | Unset = UNSET
    delete_at: int | Unset = UNSET
    creator_id: str | Unset = UNSET
    team_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    trigger_words: list[str] | Unset = UNSET
    trigger_when: int | Unset = UNSET
    callback_urls: list[str] | Unset = UNSET
    content_type: str | Unset = "application/x-www-form-urlencoded"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        create_at = self.create_at

        update_at = self.update_at

        delete_at = self.delete_at

        creator_id = self.creator_id

        team_id = self.team_id

        channel_id = self.channel_id

        description = self.description

        display_name = self.display_name

        trigger_words: list[str] | Unset = UNSET
        if not isinstance(self.trigger_words, Unset):
            trigger_words = self.trigger_words

        trigger_when = self.trigger_when

        callback_urls: list[str] | Unset = UNSET
        if not isinstance(self.callback_urls, Unset):
            callback_urls = self.callback_urls

        content_type = self.content_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if update_at is not UNSET:
            field_dict["update_at"] = update_at
        if delete_at is not UNSET:
            field_dict["delete_at"] = delete_at
        if creator_id is not UNSET:
            field_dict["creator_id"] = creator_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if trigger_words is not UNSET:
            field_dict["trigger_words"] = trigger_words
        if trigger_when is not UNSET:
            field_dict["trigger_when"] = trigger_when
        if callback_urls is not UNSET:
            field_dict["callback_urls"] = callback_urls
        if content_type is not UNSET:
            field_dict["content_type"] = content_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        create_at = d.pop("create_at", UNSET)

        update_at = d.pop("update_at", UNSET)

        delete_at = d.pop("delete_at", UNSET)

        creator_id = d.pop("creator_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        trigger_words = cast(list[str], d.pop("trigger_words", UNSET))

        trigger_when = d.pop("trigger_when", UNSET)

        callback_urls = cast(list[str], d.pop("callback_urls", UNSET))

        content_type = d.pop("content_type", UNSET)

        outgoing_webhook = cls(
            id=id,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
            creator_id=creator_id,
            team_id=team_id,
            channel_id=channel_id,
            description=description,
            display_name=display_name,
            trigger_words=trigger_words,
            trigger_when=trigger_when,
            callback_urls=callback_urls,
            content_type=content_type,
        )

        outgoing_webhook.additional_properties = d
        return outgoing_webhook

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
