from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_data import JobData


T = TypeVar("T", bound="Job")


@_attrs_define
class Job:
    """Generated Time Messenger API v4 model."""

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    create_at: int | Unset = UNSET
    start_at: int | Unset = UNSET
    last_activity_at: int | Unset = UNSET
    status: str | Unset = UNSET
    progress: int | Unset = UNSET
    data: JobData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        create_at = self.create_at

        start_at = self.start_at

        last_activity_at = self.last_activity_at

        status = self.status

        progress = self.progress

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at
        if status is not UNSET:
            field_dict["status"] = status
        if progress is not UNSET:
            field_dict["progress"] = progress
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.job_data import JobData

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        create_at = d.pop("create_at", UNSET)

        start_at = d.pop("start_at", UNSET)

        last_activity_at = d.pop("last_activity_at", UNSET)

        status = d.pop("status", UNSET)

        progress = d.pop("progress", UNSET)

        _data = d.pop("data", UNSET)
        data: JobData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = JobData.from_dict(_data)

        job = cls(
            id=id,
            type_=type_,
            create_at=create_at,
            start_at=start_at,
            last_activity_at=last_activity_at,
            status=status,
            progress=progress,
            data=data,
        )

        job.additional_properties = d
        return job

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
