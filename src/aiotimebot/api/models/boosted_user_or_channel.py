from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel import Channel
    from ..models.user import User


T = TypeVar("T", bound="BoostedUserOrChannel")


@_attrs_define
class BoostedUserOrChannel:
    """
    Attributes:
        index (str | Unset):
        user (User | Unset):
        channel (Channel | Unset):
        last_viewed_at (int | Unset):
        is_boosted (bool | Unset):
    """

    index: str | Unset = UNSET
    user: User | Unset = UNSET
    channel: Channel | Unset = UNSET
    last_viewed_at: int | Unset = UNSET
    is_boosted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        channel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.to_dict()

        last_viewed_at = self.last_viewed_at

        is_boosted = self.is_boosted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if user is not UNSET:
            field_dict["user"] = user
        if channel is not UNSET:
            field_dict["channel"] = channel
        if last_viewed_at is not UNSET:
            field_dict["LastViewedAt"] = last_viewed_at
        if is_boosted is not UNSET:
            field_dict["isBoosted"] = is_boosted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel import Channel
        from ..models.user import User

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _user = d.pop("user", UNSET)
        user: User | Unset
        if isinstance(_user, Unset):
            user = UNSET
        else:
            user = User.from_dict(_user)

        _channel = d.pop("channel", UNSET)
        channel: Channel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = Channel.from_dict(_channel)

        last_viewed_at = d.pop("LastViewedAt", UNSET)

        is_boosted = d.pop("isBoosted", UNSET)

        boosted_user_or_channel = cls(
            index=index,
            user=user,
            channel=channel,
            last_viewed_at=last_viewed_at,
            is_boosted=is_boosted,
        )

        boosted_user_or_channel.additional_properties = d
        return boosted_user_or_channel

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
