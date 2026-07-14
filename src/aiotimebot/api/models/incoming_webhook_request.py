from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incoming_webhook_request_props import IncomingWebhookRequestProps
    from ..models.slack_attachment import SlackAttachment


T = TypeVar("T", bound="IncomingWebhookRequest")


@_attrs_define
class IncomingWebhookRequest:
    """Generated Time Messenger API v4 model."""

    text: str | Unset = UNSET
    username: str | Unset = UNSET
    icon_url: str | Unset = UNSET
    channel: str | Unset = UNSET
    props: IncomingWebhookRequestProps | Unset = UNSET
    attachments: list[SlackAttachment] | Unset = UNSET
    type_: str | Unset = UNSET
    icon_emoji: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        username = self.username

        icon_url = self.icon_url

        channel = self.channel

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        type_ = self.type_

        icon_emoji = self.icon_emoji

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text is not UNSET:
            field_dict["text"] = text
        if username is not UNSET:
            field_dict["username"] = username
        if icon_url is not UNSET:
            field_dict["icon_url"] = icon_url
        if channel is not UNSET:
            field_dict["channel"] = channel
        if props is not UNSET:
            field_dict["props"] = props
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if type_ is not UNSET:
            field_dict["type"] = type_
        if icon_emoji is not UNSET:
            field_dict["icon_emoji"] = icon_emoji

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incoming_webhook_request_props import IncomingWebhookRequestProps
        from ..models.slack_attachment import SlackAttachment

        d = dict(src_dict)
        text = d.pop("text", UNSET)

        username = d.pop("username", UNSET)

        icon_url = d.pop("icon_url", UNSET)

        channel = d.pop("channel", UNSET)

        _props = d.pop("props", UNSET)
        props: IncomingWebhookRequestProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = IncomingWebhookRequestProps.from_dict(_props)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[SlackAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = SlackAttachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        type_ = d.pop("type", UNSET)

        icon_emoji = d.pop("icon_emoji", UNSET)

        incoming_webhook_request = cls(
            text=text,
            username=username,
            icon_url=icon_url,
            channel=channel,
            props=props,
            attachments=attachments,
            type_=type_,
            icon_emoji=icon_emoji,
        )

        incoming_webhook_request.additional_properties = d
        return incoming_webhook_request

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
