from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_maintenance_job_body_type import CreateMaintenanceJobBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_maintenance_job_body_data import CreateMaintenanceJobBodyData


T = TypeVar("T", bound="CreateMaintenanceJobBody")


@_attrs_define
class CreateMaintenanceJobBody:
    """Generated Time Messenger API v4 model."""

    type_: CreateMaintenanceJobBodyType
    data: CreateMaintenanceJobBodyData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_maintenance_job_body_data import (
            CreateMaintenanceJobBodyData,
        )

        d = dict(src_dict)
        type_ = CreateMaintenanceJobBodyType(d.pop("type"))

        _data = d.pop("data", UNSET)
        data: CreateMaintenanceJobBodyData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateMaintenanceJobBodyData.from_dict(_data)

        create_maintenance_job_body = cls(
            type_=type_,
            data=data,
        )

        create_maintenance_job_body.additional_properties = d
        return create_maintenance_job_body

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
