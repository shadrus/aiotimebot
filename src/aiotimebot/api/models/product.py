from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_on import AddOn


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Attributes:
        id (str | Unset):
        name (str | Unset):
        description (str | Unset):
        price_per_seat (str | Unset):
        add_ons (list[AddOn] | Unset):
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    price_per_seat: str | Unset = UNSET
    add_ons: list[AddOn] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        price_per_seat = self.price_per_seat

        add_ons: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.add_ons, Unset):
            add_ons = []
            for add_ons_item_data in self.add_ons:
                add_ons_item = add_ons_item_data.to_dict()
                add_ons.append(add_ons_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if price_per_seat is not UNSET:
            field_dict["price_per_seat"] = price_per_seat
        if add_ons is not UNSET:
            field_dict["add_ons"] = add_ons

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_on import AddOn

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        price_per_seat = d.pop("price_per_seat", UNSET)

        _add_ons = d.pop("add_ons", UNSET)
        add_ons: list[AddOn] | Unset = UNSET
        if _add_ons is not UNSET:
            add_ons = []
            for add_ons_item_data in _add_ons:
                add_ons_item = AddOn.from_dict(add_ons_item_data)

                add_ons.append(add_ons_item)

        product = cls(
            id=id,
            name=name,
            description=description,
            price_per_seat=price_per_seat,
            add_ons=add_ons,
        )

        product.additional_properties = d
        return product

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
