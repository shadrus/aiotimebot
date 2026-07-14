from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_info_list_file_infos import FileInfoListFileInfos


T = TypeVar("T", bound="FileInfoList")


@_attrs_define
class FileInfoList:
    """Generated Time Messenger API v4 model."""

    order: list[str]
    file_infos: FileInfoListFileInfos
    next_file_info_id: str
    prev_file_info_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        file_infos = self.file_infos.to_dict()

        next_file_info_id = self.next_file_info_id

        prev_file_info_id = self.prev_file_info_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "file_infos": file_infos,
                "next_file_info_id": next_file_info_id,
                "prev_file_info_id": prev_file_info_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_info_list_file_infos import FileInfoListFileInfos

        d = dict(src_dict)
        order = cast(list[str], d.pop("order"))

        file_infos = FileInfoListFileInfos.from_dict(d.pop("file_infos"))

        next_file_info_id = d.pop("next_file_info_id")

        prev_file_info_id = d.pop("prev_file_info_id")

        file_info_list = cls(
            order=order,
            file_infos=file_infos,
            next_file_info_id=next_file_info_id,
            prev_file_info_id=prev_file_info_id,
        )

        file_info_list.additional_properties = d
        return file_info_list

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
