from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_reaction import TopReaction


T = TypeVar("T", bound="TopReactionList")


@_attrs_define
class TopReactionList:
    """Generated Time Messenger API v4 model."""

    has_next: bool | Unset = UNSET
    items: list[TopReaction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_next = self.has_next

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_next is not UNSET:
            field_dict["has_next"] = has_next
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_reaction import TopReaction

        d = dict(src_dict)
        has_next = d.pop("has_next", UNSET)

        _items = d.pop("items", UNSET)
        items: list[TopReaction] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = TopReaction.from_dict(items_item_data)

                items.append(items_item)

        top_reaction_list = cls(
            has_next=has_next,
            items=items,
        )

        top_reaction_list.additional_properties = d
        return top_reaction_list

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
