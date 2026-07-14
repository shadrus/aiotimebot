from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.activity_feed_items_item_type import ActivityFeedItemsItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_feed_items_item_item import ActivityFeedItemsItemItem


T = TypeVar("T", bound="ActivityFeedItemsItem")


@_attrs_define
class ActivityFeedItemsItem:
    """Generated Time Messenger API v4 model."""

    type_: ActivityFeedItemsItemType | Unset = UNSET
    item: ActivityFeedItemsItemItem | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        item: dict[str, Any] | Unset = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_feed_items_item_item import ActivityFeedItemsItemItem

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: ActivityFeedItemsItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ActivityFeedItemsItemType(_type_)

        _item = d.pop("item", UNSET)
        item: ActivityFeedItemsItemItem | Unset
        if isinstance(_item, Unset):
            item = UNSET
        else:
            item = ActivityFeedItemsItemItem.from_dict(_item)

        activity_feed_items_item = cls(
            type_=type_,
            item=item,
        )

        activity_feed_items_item.additional_properties = d
        return activity_feed_items_item

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
