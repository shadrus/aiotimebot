from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Subscription")


@_attrs_define
class Subscription:
    """
    Attributes:
        id (str | Unset):
        customer_id (str | Unset):
        product_id (str | Unset):
        add_ons (list[str] | Unset):
        start_at (int | Unset):
        end_at (int | Unset):
        create_at (int | Unset):
        seats (int | Unset):
        dns (str | Unset):
    """

    id: str | Unset = UNSET
    customer_id: str | Unset = UNSET
    product_id: str | Unset = UNSET
    add_ons: list[str] | Unset = UNSET
    start_at: int | Unset = UNSET
    end_at: int | Unset = UNSET
    create_at: int | Unset = UNSET
    seats: int | Unset = UNSET
    dns: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        customer_id = self.customer_id

        product_id = self.product_id

        add_ons: list[str] | Unset = UNSET
        if not isinstance(self.add_ons, Unset):
            add_ons = self.add_ons

        start_at = self.start_at

        end_at = self.end_at

        create_at = self.create_at

        seats = self.seats

        dns = self.dns

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if product_id is not UNSET:
            field_dict["product_id"] = product_id
        if add_ons is not UNSET:
            field_dict["add_ons"] = add_ons
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if seats is not UNSET:
            field_dict["seats"] = seats
        if dns is not UNSET:
            field_dict["dns"] = dns

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        customer_id = d.pop("customer_id", UNSET)

        product_id = d.pop("product_id", UNSET)

        add_ons = cast(list[str], d.pop("add_ons", UNSET))

        start_at = d.pop("start_at", UNSET)

        end_at = d.pop("end_at", UNSET)

        create_at = d.pop("create_at", UNSET)

        seats = d.pop("seats", UNSET)

        dns = d.pop("dns", UNSET)

        subscription = cls(
            id=id,
            customer_id=customer_id,
            product_id=product_id,
            add_ons=add_ons,
            start_at=start_at,
            end_at=end_at,
            create_at=create_at,
            seats=seats,
            dns=dns,
        )

        subscription.additional_properties = d
        return subscription

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
