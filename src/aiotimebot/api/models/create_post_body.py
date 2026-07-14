from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_props import PostProps


T = TypeVar("T", bound="CreatePostBody")


@_attrs_define
class CreatePostBody:
    """Generated Time Messenger API v4 model."""

    message: str
    idempotency_key: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    peer: str | Unset = UNSET
    root_id: str | Unset = UNSET
    file_ids: list[str] | Unset = UNSET
    props: PostProps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        idempotency_key = self.idempotency_key

        channel_id = self.channel_id

        peer = self.peer

        root_id = self.root_id

        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "message": message,
            }
        )
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if peer is not UNSET:
            field_dict["peer"] = peer
        if root_id is not UNSET:
            field_dict["root_id"] = root_id
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if props is not UNSET:
            field_dict["props"] = props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_props import PostProps

        d = dict(src_dict)
        message = d.pop("message")

        idempotency_key = d.pop("idempotency_key", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        peer = d.pop("peer", UNSET)

        root_id = d.pop("root_id", UNSET)

        file_ids = cast(list[str], d.pop("file_ids", UNSET))

        _props = d.pop("props", UNSET)
        props: PostProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = PostProps.from_dict(_props)

        create_post_body = cls(
            message=message,
            idempotency_key=idempotency_key,
            channel_id=channel_id,
            peer=peer,
            root_id=root_id,
            file_ids=file_ids,
            props=props,
        )

        create_post_body.additional_properties = d
        return create_post_body

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
