from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_moderated_role import ChannelModeratedRole


T = TypeVar("T", bound="ChannelModeratedRoles")


@_attrs_define
class ChannelModeratedRoles:
    """
    Attributes:
        restricted_guests (ChannelModeratedRole | Unset):
        guests (ChannelModeratedRole | Unset):
        members (ChannelModeratedRole | Unset):
    """

    restricted_guests: ChannelModeratedRole | Unset = UNSET
    guests: ChannelModeratedRole | Unset = UNSET
    members: ChannelModeratedRole | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        restricted_guests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restricted_guests, Unset):
            restricted_guests = self.restricted_guests.to_dict()

        guests: dict[str, Any] | Unset = UNSET
        if not isinstance(self.guests, Unset):
            guests = self.guests.to_dict()

        members: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members, Unset):
            members = self.members.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if restricted_guests is not UNSET:
            field_dict["restricted_guests"] = restricted_guests
        if guests is not UNSET:
            field_dict["guests"] = guests
        if members is not UNSET:
            field_dict["members"] = members

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_moderated_role import ChannelModeratedRole

        d = dict(src_dict)
        _restricted_guests = d.pop("restricted_guests", UNSET)
        restricted_guests: ChannelModeratedRole | Unset
        if isinstance(_restricted_guests, Unset):
            restricted_guests = UNSET
        else:
            restricted_guests = ChannelModeratedRole.from_dict(_restricted_guests)

        _guests = d.pop("guests", UNSET)
        guests: ChannelModeratedRole | Unset
        if isinstance(_guests, Unset):
            guests = UNSET
        else:
            guests = ChannelModeratedRole.from_dict(_guests)

        _members = d.pop("members", UNSET)
        members: ChannelModeratedRole | Unset
        if isinstance(_members, Unset):
            members = UNSET
        else:
            members = ChannelModeratedRole.from_dict(_members)

        channel_moderated_roles = cls(
            restricted_guests=restricted_guests,
            guests=guests,
            members=members,
        )

        channel_moderated_roles.additional_properties = d
        return channel_moderated_roles

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
