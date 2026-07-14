from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailInviteWithErrorErrorParams")


@_attrs_define
class EmailInviteWithErrorErrorParams:
    """Generated Time Messenger API v4 model."""

    retry_after_second: int | Unset = UNSET
    remaining_sendings: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retry_after_second = self.retry_after_second

        remaining_sendings = self.remaining_sendings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retry_after_second is not UNSET:
            field_dict["retry_after_second"] = retry_after_second
        if remaining_sendings is not UNSET:
            field_dict["remaining_sendings"] = remaining_sendings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retry_after_second = d.pop("retry_after_second", UNSET)

        remaining_sendings = d.pop("remaining_sendings", UNSET)

        email_invite_with_error_error_params = cls(
            retry_after_second=retry_after_second,
            remaining_sendings=remaining_sendings,
        )

        email_invite_with_error_error_params.additional_properties = d
        return email_invite_with_error_error_params

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
