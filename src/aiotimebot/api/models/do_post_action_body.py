from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DoPostActionBody")


@_attrs_define
class DoPostActionBody:
    """Generated Time Messenger API v4 model."""

    selected_option: str | Unset = UNSET
    cookie: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        selected_option = self.selected_option

        cookie = self.cookie

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if selected_option is not UNSET:
            field_dict["selected_option"] = selected_option
        if cookie is not UNSET:
            field_dict["cookie"] = cookie

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        selected_option = d.pop("selected_option", UNSET)

        cookie = d.pop("cookie", UNSET)

        do_post_action_body = cls(
            selected_option=selected_option,
            cookie=cookie,
        )

        do_post_action_body.additional_properties = d
        return do_post_action_body

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
