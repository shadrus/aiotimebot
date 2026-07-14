from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.sidebar_category_with_channels import SidebarCategoryWithChannels


T = TypeVar("T", bound="OrderedSidebarCategories")


@_attrs_define
class OrderedSidebarCategories:
    """Generated Time Messenger API v4 model."""

    order: list[str]
    categories: list[SidebarCategoryWithChannels]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        categories = []
        for categories_item_data in self.categories:
            categories_item = categories_item_data.to_dict()
            categories.append(categories_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "categories": categories,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sidebar_category_with_channels import SidebarCategoryWithChannels

        d = dict(src_dict)
        order = cast(list[str], d.pop("order"))

        categories = []
        _categories = d.pop("categories")
        for categories_item_data in _categories:
            categories_item = SidebarCategoryWithChannels.from_dict(
                categories_item_data
            )

            categories.append(categories_item)

        ordered_sidebar_categories = cls(
            order=order,
            categories=categories,
        )

        ordered_sidebar_categories.additional_properties = d
        return ordered_sidebar_categories

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
