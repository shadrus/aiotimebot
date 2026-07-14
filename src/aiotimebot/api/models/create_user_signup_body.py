from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateUserSignupBody")


@_attrs_define
class CreateUserSignupBody:
    """Generated Time Messenger API v4 model."""

    login: str
    password: str
    first_name: str
    last_name: str
    phone: str
    position: str | Unset = UNSET
    image: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        login = self.login

        password = self.password

        first_name = self.first_name

        last_name = self.last_name

        phone = self.phone

        position = self.position

        image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "login": login,
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
                "phone": phone,
            }
        )
        if position is not UNSET:
            field_dict["position"] = position
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login")

        password = d.pop("password")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        phone = d.pop("phone")

        position = d.pop("position", UNSET)

        image = d.pop("image", UNSET)

        create_user_signup_body = cls(
            login=login,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            position=position,
            image=image,
        )

        create_user_signup_body.additional_properties = d
        return create_user_signup_body

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
