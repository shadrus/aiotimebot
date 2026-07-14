from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.migrate_auth_to_open_id_body_from import MigrateAuthToOpenIDBodyFrom

T = TypeVar("T", bound="MigrateAuthToOpenIDBody")


@_attrs_define
class MigrateAuthToOpenIDBody:
    """Generated Time Messenger API v4 model."""

    from_: MigrateAuthToOpenIDBodyFrom
    update_auth_data: bool
    dry_run: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from_ = self.from_.value

        update_auth_data = self.update_auth_data

        dry_run = self.dry_run

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "from": from_,
                "update_auth_data": update_auth_data,
                "dry_run": dry_run,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        from_ = MigrateAuthToOpenIDBodyFrom(d.pop("from"))

        update_auth_data = d.pop("update_auth_data")

        dry_run = d.pop("dry_run")

        migrate_auth_to_open_id_body = cls(
            from_=from_,
            update_auth_data=update_auth_data,
            dry_run=dry_run,
        )

        migrate_auth_to_open_id_body.additional_properties = d
        return migrate_auth_to_open_id_body

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
