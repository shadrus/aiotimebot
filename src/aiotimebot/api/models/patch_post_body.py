from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_props import PostProps


T = TypeVar("T", bound="PatchPostBody")


@_attrs_define
class PatchPostBody:
    """Generated Time Messenger API v4 model."""

    is_pinned: bool | Unset = UNSET
    message: str | Unset = UNSET
    file_ids: list[str] | Unset = UNSET
    has_reactions: bool | Unset = UNSET
    props: PostProps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_pinned = self.is_pinned

        message = self.message

        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        has_reactions = self.has_reactions

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned
        if message is not UNSET:
            field_dict["message"] = message
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if has_reactions is not UNSET:
            field_dict["has_reactions"] = has_reactions
        if props is not UNSET:
            field_dict["props"] = props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_props import PostProps

        d = dict(src_dict)
        is_pinned = d.pop("is_pinned", UNSET)

        message = d.pop("message", UNSET)

        file_ids = cast(list[str], d.pop("file_ids", UNSET))

        has_reactions = d.pop("has_reactions", UNSET)

        _props = d.pop("props", UNSET)
        props: PostProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = PostProps.from_dict(_props)

        patch_post_body = cls(
            is_pinned=is_pinned,
            message=message,
            file_ids=file_ids,
            has_reactions=has_reactions,
            props=props,
        )

        patch_post_body.additional_properties = d
        return patch_post_body

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
