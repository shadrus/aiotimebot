from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileInfo")


@_attrs_define
class FileInfo:
    """Generated Time Messenger API v4 model."""

    id: str
    user_id: str
    channel_id: str
    create_at: int
    update_at: int
    delete_at: int
    name: str
    extension: str
    size: int
    mime_type: str
    post_id: str | Unset = UNSET
    width: int | Unset = UNSET
    height: int | Unset = UNSET
    has_preview_image: bool | Unset = UNSET
    mini_preview: str | Unset = UNSET
    remote_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        channel_id = self.channel_id

        create_at = self.create_at

        update_at = self.update_at

        delete_at = self.delete_at

        name = self.name

        extension = self.extension

        size = self.size

        mime_type = self.mime_type

        post_id = self.post_id

        width = self.width

        height = self.height

        has_preview_image = self.has_preview_image

        mini_preview = self.mini_preview

        remote_id = self.remote_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "channel_id": channel_id,
                "create_at": create_at,
                "update_at": update_at,
                "delete_at": delete_at,
                "name": name,
                "extension": extension,
                "size": size,
                "mime_type": mime_type,
            }
        )
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if width is not UNSET:
            field_dict["width"] = width
        if height is not UNSET:
            field_dict["height"] = height
        if has_preview_image is not UNSET:
            field_dict["has_preview_image"] = has_preview_image
        if mini_preview is not UNSET:
            field_dict["mini_preview"] = mini_preview
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        channel_id = d.pop("channel_id")

        create_at = d.pop("create_at")

        update_at = d.pop("update_at")

        delete_at = d.pop("delete_at")

        name = d.pop("name")

        extension = d.pop("extension")

        size = d.pop("size")

        mime_type = d.pop("mime_type")

        post_id = d.pop("post_id", UNSET)

        width = d.pop("width", UNSET)

        height = d.pop("height", UNSET)

        has_preview_image = d.pop("has_preview_image", UNSET)

        mini_preview = d.pop("mini_preview", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        file_info = cls(
            id=id,
            user_id=user_id,
            channel_id=channel_id,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
            name=name,
            extension=extension,
            size=size,
            mime_type=mime_type,
            post_id=post_id,
            width=width,
            height=height,
            has_preview_image=has_preview_image,
            mini_preview=mini_preview,
            remote_id=remote_id,
        )

        file_info.additional_properties = d
        return file_info

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
