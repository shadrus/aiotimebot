from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.upload_session_type import UploadSessionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UploadSession")


@_attrs_define
class UploadSession:
    """Generated Time Messenger API v4 model."""

    id: str | Unset = UNSET
    type_: UploadSessionType | Unset = UNSET
    create_at: int | Unset = UNSET
    user_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    filename: str | Unset = UNSET
    file_size: int | Unset = UNSET
    file_offset: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        create_at = self.create_at

        user_id = self.user_id

        channel_id = self.channel_id

        filename = self.filename

        file_size = self.file_size

        file_offset = self.file_offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if filename is not UNSET:
            field_dict["filename"] = filename
        if file_size is not UNSET:
            field_dict["file_size"] = file_size
        if file_offset is not UNSET:
            field_dict["file_offset"] = file_offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: UploadSessionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UploadSessionType(_type_)

        create_at = d.pop("create_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        filename = d.pop("filename", UNSET)

        file_size = d.pop("file_size", UNSET)

        file_offset = d.pop("file_offset", UNSET)

        upload_session = cls(
            id=id,
            type_=type_,
            create_at=create_at,
            user_id=user_id,
            channel_id=channel_id,
            filename=filename,
            file_size=file_size,
            file_offset=file_offset,
        )

        upload_session.additional_properties = d
        return upload_session

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
