from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateMaintenanceJobBodyData")


@_attrs_define
class CreateMaintenanceJobBodyData:
    """Generated Time Messenger API v4 model."""

    channels: str | Unset = UNSET
    posts: str | Unset = UNSET
    users: str | Unset = UNSET
    files: str | Unset = UNSET
    emojis: str | Unset = UNSET
    hashtags: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        channels = self.channels

        posts = self.posts

        users = self.users

        files = self.files

        emojis = self.emojis

        hashtags = self.hashtags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if channels is not UNSET:
            field_dict["channels"] = channels
        if posts is not UNSET:
            field_dict["posts"] = posts
        if users is not UNSET:
            field_dict["users"] = users
        if files is not UNSET:
            field_dict["files"] = files
        if emojis is not UNSET:
            field_dict["emojis"] = emojis
        if hashtags is not UNSET:
            field_dict["hashtags"] = hashtags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channels = d.pop("channels", UNSET)

        posts = d.pop("posts", UNSET)

        users = d.pop("users", UNSET)

        files = d.pop("files", UNSET)

        emojis = d.pop("emojis", UNSET)

        hashtags = d.pop("hashtags", UNSET)

        create_maintenance_job_body_data = cls(
            channels=channels,
            posts=posts,
            users=users,
            files=files,
            emojis=emojis,
            hashtags=hashtags,
        )

        create_maintenance_job_body_data.additional_properties = d
        return create_maintenance_job_body_data

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
