from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_action import PostAction
    from ..models.slack_attachment_field import SlackAttachmentField


T = TypeVar("T", bound="SlackAttachment")


@_attrs_define
class SlackAttachment:
    """Generated Time Messenger API v4 model."""

    id: int
    fallback: str
    color: str
    pretext: str
    author_name: str
    author_link: str
    author_icon: str
    title: str
    title_link: str
    text: str
    image_url: str
    thumb_url: str
    footer: str
    footer_icon: str
    fields: list[SlackAttachmentField] | Unset = UNSET
    ts: str | Unset = UNSET
    actions: list[PostAction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        fallback = self.fallback

        color = self.color

        pretext = self.pretext

        author_name = self.author_name

        author_link = self.author_link

        author_icon = self.author_icon

        title = self.title

        title_link = self.title_link

        text = self.text

        image_url = self.image_url

        thumb_url = self.thumb_url

        footer = self.footer

        footer_icon = self.footer_icon

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        ts = self.ts

        actions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.actions, Unset):
            actions = []
            for actions_item_data in self.actions:
                actions_item = actions_item_data.to_dict()
                actions.append(actions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "fallback": fallback,
                "color": color,
                "pretext": pretext,
                "author_name": author_name,
                "author_link": author_link,
                "author_icon": author_icon,
                "title": title,
                "title_link": title_link,
                "text": text,
                "image_url": image_url,
                "thumb_url": thumb_url,
                "footer": footer,
                "footer_icon": footer_icon,
            }
        )
        if fields is not UNSET:
            field_dict["fields"] = fields
        if ts is not UNSET:
            field_dict["ts"] = ts
        if actions is not UNSET:
            field_dict["actions"] = actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_action import PostAction
        from ..models.slack_attachment_field import SlackAttachmentField

        d = dict(src_dict)
        id = d.pop("id")

        fallback = d.pop("fallback")

        color = d.pop("color")

        pretext = d.pop("pretext")

        author_name = d.pop("author_name")

        author_link = d.pop("author_link")

        author_icon = d.pop("author_icon")

        title = d.pop("title")

        title_link = d.pop("title_link")

        text = d.pop("text")

        image_url = d.pop("image_url")

        thumb_url = d.pop("thumb_url")

        footer = d.pop("footer")

        footer_icon = d.pop("footer_icon")

        _fields = d.pop("fields", UNSET)
        fields: list[SlackAttachmentField] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = SlackAttachmentField.from_dict(fields_item_data)

                fields.append(fields_item)

        ts = d.pop("ts", UNSET)

        _actions = d.pop("actions", UNSET)
        actions: list[PostAction] | Unset = UNSET
        if _actions is not UNSET:
            actions = []
            for actions_item_data in _actions:
                actions_item = PostAction.from_dict(actions_item_data)

                actions.append(actions_item)

        slack_attachment = cls(
            id=id,
            fallback=fallback,
            color=color,
            pretext=pretext,
            author_name=author_name,
            author_link=author_link,
            author_icon=author_icon,
            title=title,
            title_link=title_link,
            text=text,
            image_url=image_url,
            thumb_url=thumb_url,
            footer=footer,
            footer_icon=footer_icon,
            fields=fields,
            ts=ts,
            actions=actions,
        )

        slack_attachment.additional_properties = d
        return slack_attachment

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
