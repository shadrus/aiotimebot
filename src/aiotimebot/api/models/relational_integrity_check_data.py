from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.orphaned_record import OrphanedRecord


T = TypeVar("T", bound="RelationalIntegrityCheckData")


@_attrs_define
class RelationalIntegrityCheckData:
    """Generated Time Messenger API v4 model."""

    parent_name: str | Unset = UNSET
    child_name: str | Unset = UNSET
    parent_id_attr: str | Unset = UNSET
    child_id_attr: str | Unset = UNSET
    records: list[OrphanedRecord] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_name = self.parent_name

        child_name = self.child_name

        parent_id_attr = self.parent_id_attr

        child_id_attr = self.child_id_attr

        records: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.records, Unset):
            records = []
            for records_item_data in self.records:
                records_item = records_item_data.to_dict()
                records.append(records_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_name is not UNSET:
            field_dict["parent_name"] = parent_name
        if child_name is not UNSET:
            field_dict["child_name"] = child_name
        if parent_id_attr is not UNSET:
            field_dict["parent_id_attr"] = parent_id_attr
        if child_id_attr is not UNSET:
            field_dict["child_id_attr"] = child_id_attr
        if records is not UNSET:
            field_dict["records"] = records

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.orphaned_record import OrphanedRecord

        d = dict(src_dict)
        parent_name = d.pop("parent_name", UNSET)

        child_name = d.pop("child_name", UNSET)

        parent_id_attr = d.pop("parent_id_attr", UNSET)

        child_id_attr = d.pop("child_id_attr", UNSET)

        _records = d.pop("records", UNSET)
        records: list[OrphanedRecord] | Unset = UNSET
        if _records is not UNSET:
            records = []
            for records_item_data in _records:
                records_item = OrphanedRecord.from_dict(records_item_data)

                records.append(records_item)

        relational_integrity_check_data = cls(
            parent_name=parent_name,
            child_name=child_name,
            parent_id_attr=parent_id_attr,
            child_id_attr=child_id_attr,
            records=records,
        )

        relational_integrity_check_data.additional_properties = d
        return relational_integrity_check_data

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
