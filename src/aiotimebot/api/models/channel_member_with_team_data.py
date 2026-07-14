from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.channel_notify_props import ChannelNotifyProps


T = TypeVar("T", bound="ChannelMemberWithTeamData")


@_attrs_define
class ChannelMemberWithTeamData:
    """Generated Time Messenger API v4 model."""

    channel_id: str
    user_id: str
    roles: str
    last_viewed_at: int
    msg_count: int
    mention_count: int
    mention_count_root: int
    msg_count_root: int
    notify_props: ChannelNotifyProps
    last_update_at: int
    scheme_restricted_guest: bool
    scheme_guest: bool
    scheme_user: bool
    scheme_admin: bool
    explicit_roles: str
    team_display_name: str
    team_name: str
    team_update_at: int
    last_react_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channel_id = self.channel_id

        user_id = self.user_id

        roles = self.roles

        last_viewed_at = self.last_viewed_at

        msg_count = self.msg_count

        mention_count = self.mention_count

        mention_count_root = self.mention_count_root

        msg_count_root = self.msg_count_root

        notify_props = self.notify_props.to_dict()

        last_update_at = self.last_update_at

        scheme_restricted_guest = self.scheme_restricted_guest

        scheme_guest = self.scheme_guest

        scheme_user = self.scheme_user

        scheme_admin = self.scheme_admin

        explicit_roles = self.explicit_roles

        team_display_name = self.team_display_name

        team_name = self.team_name

        team_update_at = self.team_update_at

        last_react_at = self.last_react_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "channel_id": channel_id,
                "user_id": user_id,
                "roles": roles,
                "last_viewed_at": last_viewed_at,
                "msg_count": msg_count,
                "mention_count": mention_count,
                "mention_count_root": mention_count_root,
                "msg_count_root": msg_count_root,
                "notify_props": notify_props,
                "last_update_at": last_update_at,
                "scheme_restricted_guest": scheme_restricted_guest,
                "scheme_guest": scheme_guest,
                "scheme_user": scheme_user,
                "scheme_admin": scheme_admin,
                "explicit_roles": explicit_roles,
                "team_display_name": team_display_name,
                "team_name": team_name,
                "team_update_at": team_update_at,
            }
        )
        if last_react_at is not UNSET:
            field_dict["last_react_at"] = last_react_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_notify_props import ChannelNotifyProps

        d = dict(src_dict)
        channel_id = d.pop("channel_id")

        user_id = d.pop("user_id")

        roles = d.pop("roles")

        last_viewed_at = d.pop("last_viewed_at")

        msg_count = d.pop("msg_count")

        mention_count = d.pop("mention_count")

        mention_count_root = d.pop("mention_count_root")

        msg_count_root = d.pop("msg_count_root")

        notify_props = ChannelNotifyProps.from_dict(d.pop("notify_props"))

        last_update_at = d.pop("last_update_at")

        scheme_restricted_guest = d.pop("scheme_restricted_guest")

        scheme_guest = d.pop("scheme_guest")

        scheme_user = d.pop("scheme_user")

        scheme_admin = d.pop("scheme_admin")

        explicit_roles = d.pop("explicit_roles")

        team_display_name = d.pop("team_display_name")

        team_name = d.pop("team_name")

        team_update_at = d.pop("team_update_at")

        last_react_at = d.pop("last_react_at", UNSET)

        channel_member_with_team_data = cls(
            channel_id=channel_id,
            user_id=user_id,
            roles=roles,
            last_viewed_at=last_viewed_at,
            msg_count=msg_count,
            mention_count=mention_count,
            mention_count_root=mention_count_root,
            msg_count_root=msg_count_root,
            notify_props=notify_props,
            last_update_at=last_update_at,
            scheme_restricted_guest=scheme_restricted_guest,
            scheme_guest=scheme_guest,
            scheme_user=scheme_user,
            scheme_admin=scheme_admin,
            explicit_roles=explicit_roles,
            team_display_name=team_display_name,
            team_name=team_name,
            team_update_at=team_update_at,
            last_react_at=last_react_at,
        )

        channel_member_with_team_data.additional_properties = d
        return channel_member_with_team_data

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
