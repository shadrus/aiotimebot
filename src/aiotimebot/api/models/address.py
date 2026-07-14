from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """
    Attributes:
        city (str | Unset):
        country (str | Unset):
        line1 (str | Unset):
        line2 (str | Unset):
        postal_code (str | Unset):
        state (str | Unset):
    """

    city: str | Unset = UNSET
    country: str | Unset = UNSET
    line1: str | Unset = UNSET
    line2: str | Unset = UNSET
    postal_code: str | Unset = UNSET
    state: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        country = self.country

        line1 = self.line1

        line2 = self.line2

        postal_code = self.postal_code

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if line1 is not UNSET:
            field_dict["line1"] = line1
        if line2 is not UNSET:
            field_dict["line2"] = line2
        if postal_code is not UNSET:
            field_dict["postal_code"] = postal_code
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        line1 = d.pop("line1", UNSET)

        line2 = d.pop("line2", UNSET)

        postal_code = d.pop("postal_code", UNSET)

        state = d.pop("state", UNSET)

        address = cls(
            city=city,
            country=country,
            line1=line1,
            line2=line2,
            postal_code=postal_code,
            state=state,
        )

        address.additional_properties = d
        return address

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
