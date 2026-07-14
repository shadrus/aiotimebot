from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_suggestion_type import ChannelSuggestionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel import Channel
    from ..models.user import User


T = TypeVar("T", bound="ChannelSuggestion")


@_attrs_define
class ChannelSuggestion:
    """Generated Time Messenger API v4 model."""

    type_: ChannelSuggestionType
    channel: Channel
    user: User | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        channel = self.channel.to_dict()

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "channel": channel,
            }
        )
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel import Channel
        from ..models.user import User

        d = dict(src_dict)
        type_ = ChannelSuggestionType(d.pop("type"))

        channel = Channel.from_dict(d.pop("channel"))

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        channel_suggestion = cls(
            type_=type_,
            channel=channel,
            user=user,
        )

        channel_suggestion.additional_properties = d
        return channel_suggestion

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
