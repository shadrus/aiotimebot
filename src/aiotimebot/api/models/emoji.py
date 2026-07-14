from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Emoji")


@_attrs_define
class Emoji:
    """Generated Time Messenger API v4 model."""

    id: str
    creator_id: str
    name: str
    create_at: int
    update_at: int
    delete_at: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        creator_id = self.creator_id

        name = self.name

        create_at = self.create_at

        update_at = self.update_at

        delete_at = self.delete_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "creator_id": creator_id,
                "name": name,
                "create_at": create_at,
                "update_at": update_at,
                "delete_at": delete_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        creator_id = d.pop("creator_id")

        name = d.pop("name")

        create_at = d.pop("create_at")

        update_at = d.pop("update_at")

        delete_at = d.pop("delete_at")

        emoji = cls(
            id=id,
            creator_id=creator_id,
            name=name,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
        )

        emoji.additional_properties = d
        return emoji

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
