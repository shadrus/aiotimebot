from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResetSamlAuthDataToEmailBody")


@_attrs_define
class ResetSamlAuthDataToEmailBody:
    """Generated Time Messenger API v4 model."""

    include_deleted: bool | Unset = False
    dry_run: bool | Unset = False
    user_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        include_deleted = self.include_deleted

        dry_run = self.dry_run

        user_ids: list[str] | Unset = UNSET
        if not isinstance(self.user_ids, Unset):
            user_ids = self.user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if include_deleted is not UNSET:
            field_dict["include_deleted"] = include_deleted
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if user_ids is not UNSET:
            field_dict["user_ids"] = user_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        include_deleted = d.pop("include_deleted", UNSET)

        dry_run = d.pop("dry_run", UNSET)

        user_ids = cast(list[str], d.pop("user_ids", UNSET))

        reset_saml_auth_data_to_email_body = cls(
            include_deleted=include_deleted,
            dry_run=dry_run,
            user_ids=user_ids,
        )

        reset_saml_auth_data_to_email_body.additional_properties = d
        return reset_saml_auth_data_to_email_body

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
