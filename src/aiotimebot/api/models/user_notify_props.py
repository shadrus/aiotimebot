from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_mention_notification_type import UserMentionNotificationType
from ..models.user_reactions_notification_type import UserReactionsNotificationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserNotifyProps")


@_attrs_define
class UserNotifyProps:
    """Generated Time Messenger API v4 model."""

    email: str | Unset = UNSET
    push: UserMentionNotificationType | Unset = UNSET
    desktop: UserMentionNotificationType | Unset = UNSET
    desktop_sound: str | Unset = UNSET
    mention_keys: str | Unset = UNSET
    channel: str | Unset = UNSET
    first_name: str | Unset = UNSET
    desktop_threads: UserMentionNotificationType | Unset = UNSET
    push_threads: UserMentionNotificationType | Unset = UNSET
    desktop_reactions: UserReactionsNotificationType | Unset = UNSET
    push_reactions: UserReactionsNotificationType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        push: str | Unset = UNSET
        if not isinstance(self.push, Unset):
            push = self.push.value

        desktop: str | Unset = UNSET
        if not isinstance(self.desktop, Unset):
            desktop = self.desktop.value

        desktop_sound = self.desktop_sound

        mention_keys = self.mention_keys

        channel = self.channel

        first_name = self.first_name

        desktop_threads: str | Unset = UNSET
        if not isinstance(self.desktop_threads, Unset):
            desktop_threads = self.desktop_threads.value

        push_threads: str | Unset = UNSET
        if not isinstance(self.push_threads, Unset):
            push_threads = self.push_threads.value

        desktop_reactions: str | Unset = UNSET
        if not isinstance(self.desktop_reactions, Unset):
            desktop_reactions = self.desktop_reactions.value

        push_reactions: str | Unset = UNSET
        if not isinstance(self.push_reactions, Unset):
            push_reactions = self.push_reactions.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if push is not UNSET:
            field_dict["push"] = push
        if desktop is not UNSET:
            field_dict["desktop"] = desktop
        if desktop_sound is not UNSET:
            field_dict["desktop_sound"] = desktop_sound
        if mention_keys is not UNSET:
            field_dict["mention_keys"] = mention_keys
        if channel is not UNSET:
            field_dict["channel"] = channel
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if desktop_threads is not UNSET:
            field_dict["desktop_threads"] = desktop_threads
        if push_threads is not UNSET:
            field_dict["push_threads"] = push_threads
        if desktop_reactions is not UNSET:
            field_dict["desktop_reactions"] = desktop_reactions
        if push_reactions is not UNSET:
            field_dict["push_reactions"] = push_reactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        _push = d.pop("push", UNSET)
        push: UserMentionNotificationType | Unset
        if isinstance(_push, Unset):
            push = UNSET
        else:
            push = UserMentionNotificationType(_push)

        _desktop = d.pop("desktop", UNSET)
        desktop: UserMentionNotificationType | Unset
        if isinstance(_desktop, Unset):
            desktop = UNSET
        else:
            desktop = UserMentionNotificationType(_desktop)

        desktop_sound = d.pop("desktop_sound", UNSET)

        mention_keys = d.pop("mention_keys", UNSET)

        channel = d.pop("channel", UNSET)

        first_name = d.pop("first_name", UNSET)

        _desktop_threads = d.pop("desktop_threads", UNSET)
        desktop_threads: UserMentionNotificationType | Unset
        if isinstance(_desktop_threads, Unset):
            desktop_threads = UNSET
        else:
            desktop_threads = UserMentionNotificationType(_desktop_threads)

        _push_threads = d.pop("push_threads", UNSET)
        push_threads: UserMentionNotificationType | Unset
        if isinstance(_push_threads, Unset):
            push_threads = UNSET
        else:
            push_threads = UserMentionNotificationType(_push_threads)

        _desktop_reactions = d.pop("desktop_reactions", UNSET)
        desktop_reactions: UserReactionsNotificationType | Unset
        if isinstance(_desktop_reactions, Unset):
            desktop_reactions = UNSET
        else:
            desktop_reactions = UserReactionsNotificationType(_desktop_reactions)

        _push_reactions = d.pop("push_reactions", UNSET)
        push_reactions: UserReactionsNotificationType | Unset
        if isinstance(_push_reactions, Unset):
            push_reactions = UNSET
        else:
            push_reactions = UserReactionsNotificationType(_push_reactions)

        user_notify_props = cls(
            email=email,
            push=push,
            desktop=desktop,
            desktop_sound=desktop_sound,
            mention_keys=mention_keys,
            channel=channel,
            first_name=first_name,
            desktop_threads=desktop_threads,
            push_threads=push_threads,
            desktop_reactions=desktop_reactions,
            push_reactions=push_reactions,
        )

        user_notify_props.additional_properties = d
        return user_notify_props

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
