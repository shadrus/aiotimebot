from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_props import PostProps


T = TypeVar("T", bound="UpdatePostBody")


@_attrs_define
class UpdatePostBody:
    """Generated Time Messenger API v4 model."""

    id: str
    is_pinned: bool | Unset = UNSET
    message: str | Unset = UNSET
    has_reactions: bool | Unset = UNSET
    props: PostProps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_pinned = self.is_pinned

        message = self.message

        has_reactions = self.has_reactions

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if is_pinned is not UNSET:
            field_dict["is_pinned"] = is_pinned
        if message is not UNSET:
            field_dict["message"] = message
        if has_reactions is not UNSET:
            field_dict["has_reactions"] = has_reactions
        if props is not UNSET:
            field_dict["props"] = props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_props import PostProps

        d = dict(src_dict)
        id = d.pop("id")

        is_pinned = d.pop("is_pinned", UNSET)

        message = d.pop("message", UNSET)

        has_reactions = d.pop("has_reactions", UNSET)

        _props = d.pop("props", UNSET)
        props: PostProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = PostProps.from_dict(_props)

        update_post_body = cls(
            id=id,
            is_pinned=is_pinned,
            message=message,
            has_reactions=has_reactions,
            props=props,
        )

        update_post_body.additional_properties = d
        return update_post_body

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
