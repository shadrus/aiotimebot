from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_invite_with_error_error import EmailInviteWithErrorError


T = TypeVar("T", bound="EmailInviteWithError")


@_attrs_define
class EmailInviteWithError:
    """Generated Time Messenger API v4 model."""

    user_id: str | Unset = UNSET
    email: str | Unset = UNSET
    got_invite_earlier: str | Unset = UNSET
    sent: bool | Unset = UNSET
    added: bool | Unset = UNSET
    error: EmailInviteWithErrorError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        email = self.email

        got_invite_earlier = self.got_invite_earlier

        sent = self.sent

        added = self.added

        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if email is not UNSET:
            field_dict["email"] = email
        if got_invite_earlier is not UNSET:
            field_dict["got_invite_earlier"] = got_invite_earlier
        if sent is not UNSET:
            field_dict["sent"] = sent
        if added is not UNSET:
            field_dict["added"] = added
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_invite_with_error_error import EmailInviteWithErrorError

        d = dict(src_dict)
        user_id = d.pop("user_id", UNSET)

        email = d.pop("email", UNSET)

        got_invite_earlier = d.pop("got_invite_earlier", UNSET)

        sent = d.pop("sent", UNSET)

        added = d.pop("added", UNSET)

        _error = d.pop("error", UNSET)
        error: EmailInviteWithErrorError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = EmailInviteWithErrorError.from_dict(_error)

        email_invite_with_error = cls(
            user_id=user_id,
            email=email,
            got_invite_earlier=got_invite_earlier,
            sent=sent,
            added=added,
            error=error,
        )

        email_invite_with_error.additional_properties = d
        return email_invite_with_error

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
