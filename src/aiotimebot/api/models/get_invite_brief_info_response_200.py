from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_invite_brief_info_response_200_invite_status import (
    GetInviteBriefInfoResponse200InviteStatus,
)
from ..models.get_invite_brief_info_response_200_invite_type import (
    GetInviteBriefInfoResponse200InviteType,
)
from ..models.get_invite_brief_info_response_200_invited_user_status import (
    GetInviteBriefInfoResponse200InvitedUserStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetInviteBriefInfoResponse200")


@_attrs_define
class GetInviteBriefInfoResponse200:
    """Generated Time Messenger API v4 model."""

    invite_type: GetInviteBriefInfoResponse200InviteType
    team_display_name: str
    team_name: str
    email_masked: str
    invite_status: GetInviteBriefInfoResponse200InviteStatus
    invite_id: str | Unset = UNSET
    restricted_guest: bool | Unset = UNSET
    invited_user_status: GetInviteBriefInfoResponse200InvitedUserStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invite_type = self.invite_type.value

        team_display_name = self.team_display_name

        team_name = self.team_name

        email_masked = self.email_masked

        invite_status = self.invite_status.value

        invite_id = self.invite_id

        restricted_guest = self.restricted_guest

        invited_user_status: str | Unset = UNSET
        if not isinstance(self.invited_user_status, Unset):
            invited_user_status = self.invited_user_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invite_type": invite_type,
                "team_display_name": team_display_name,
                "team_name": team_name,
                "email_masked": email_masked,
                "invite_status": invite_status,
            }
        )
        if invite_id is not UNSET:
            field_dict["invite_id"] = invite_id
        if restricted_guest is not UNSET:
            field_dict["restricted_guest"] = restricted_guest
        if invited_user_status is not UNSET:
            field_dict["invited_user_status"] = invited_user_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invite_type = GetInviteBriefInfoResponse200InviteType(d.pop("invite_type"))

        team_display_name = d.pop("team_display_name")

        team_name = d.pop("team_name")

        email_masked = d.pop("email_masked")

        invite_status = GetInviteBriefInfoResponse200InviteStatus(
            d.pop("invite_status")
        )

        invite_id = d.pop("invite_id", UNSET)

        restricted_guest = d.pop("restricted_guest", UNSET)

        _invited_user_status = d.pop("invited_user_status", UNSET)
        invited_user_status: GetInviteBriefInfoResponse200InvitedUserStatus | Unset
        if isinstance(_invited_user_status, Unset):
            invited_user_status = UNSET
        else:
            invited_user_status = GetInviteBriefInfoResponse200InvitedUserStatus(
                _invited_user_status
            )

        get_invite_brief_info_response_200 = cls(
            invite_type=invite_type,
            team_display_name=team_display_name,
            team_name=team_name,
            email_masked=email_masked,
            invite_status=invite_status,
            invite_id=invite_id,
            restricted_guest=restricted_guest,
            invited_user_status=invited_user_status,
        )

        get_invite_brief_info_response_200.additional_properties = d
        return get_invite_brief_info_response_200

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
