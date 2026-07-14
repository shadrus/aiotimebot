from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app_error import AppError
    from ..models.team_member import TeamMember


T = TypeVar("T", bound="TeamMemberWithError")


@_attrs_define
class TeamMemberWithError:
    """
    Attributes:
        user_id (str):
        member (TeamMember | Unset):
        error (AppError | Unset):
    """

    user_id: str
    member: TeamMember | Unset = UNSET
    error: AppError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        member: dict[str, Any] | Unset = UNSET
        if not isinstance(self.member, Unset):
            member = self.member.to_dict()

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
            }
        )
        if member is not UNSET:
            field_dict["member"] = member
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_error import AppError
        from ..models.team_member import TeamMember

        d = dict(src_dict)
        user_id = d.pop("user_id")

        _member = d.pop("member", UNSET)
        member: TeamMember | Unset
        if isinstance(_member, Unset):
            member = UNSET
        else:
            member = TeamMember.from_dict(_member)

        _error = d.pop("error", UNSET)
        error: AppError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = AppError.from_dict(_error)

        team_member_with_error = cls(
            user_id=user_id,
            member=member,
            error=error,
        )

        team_member_with_error.additional_properties = d
        return team_member_with_error

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
