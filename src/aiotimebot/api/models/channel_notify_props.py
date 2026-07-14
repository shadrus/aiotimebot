from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelNotifyProps")


@_attrs_define
class ChannelNotifyProps:
    """Generated Time Messenger API v4 model."""

    email: str | Unset = UNSET
    push: str | Unset = UNSET
    desktop: str | Unset = UNSET
    mark_unread: str | Unset = UNSET
    ignore_channel_mentions: str | Unset = UNSET
    push_threads: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        push = self.push

        desktop = self.desktop

        mark_unread = self.mark_unread

        ignore_channel_mentions = self.ignore_channel_mentions

        push_threads = self.push_threads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if push is not UNSET:
            field_dict["push"] = push
        if desktop is not UNSET:
            field_dict["desktop"] = desktop
        if mark_unread is not UNSET:
            field_dict["mark_unread"] = mark_unread
        if ignore_channel_mentions is not UNSET:
            field_dict["ignore_channel_mentions"] = ignore_channel_mentions
        if push_threads is not UNSET:
            field_dict["push_threads"] = push_threads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        push = d.pop("push", UNSET)

        desktop = d.pop("desktop", UNSET)

        mark_unread = d.pop("mark_unread", UNSET)

        ignore_channel_mentions = d.pop("ignore_channel_mentions", UNSET)

        push_threads = d.pop("push_threads", UNSET)

        channel_notify_props = cls(
            email=email,
            push=push,
            desktop=desktop,
            mark_unread=mark_unread,
            ignore_channel_mentions=ignore_channel_mentions,
            push_threads=push_threads,
        )

        channel_notify_props.additional_properties = d
        return channel_notify_props

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
