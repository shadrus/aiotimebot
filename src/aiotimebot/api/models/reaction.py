from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Reaction")


@_attrs_define
class Reaction:
    """Generated Time Messenger API v4 model."""

    user_id: str
    post_id: str
    emoji_name: str
    create_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        post_id = self.post_id

        emoji_name = self.emoji_name

        create_at = self.create_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "post_id": post_id,
                "emoji_name": emoji_name,
                "create_at": create_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        post_id = d.pop("post_id")

        emoji_name = d.pop("emoji_name")

        create_at = d.pop("create_at")

        reaction = cls(
            user_id=user_id,
            post_id=post_id,
            emoji_name=emoji_name,
            create_at=create_at,
        )

        reaction.additional_properties = d
        return reaction

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
