from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationTokens")


@_attrs_define
class ApplicationTokens:
    """Generated Time Messenger API v4 model."""

    bot_token: str | Unset = UNSET
    command_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot_token = self.bot_token

        command_token = self.command_token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bot_token is not UNSET:
            field_dict["bot_token"] = bot_token
        if command_token is not UNSET:
            field_dict["command_token"] = command_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bot_token = d.pop("bot_token", UNSET)

        command_token = d.pop("command_token", UNSET)

        application_tokens = cls(
            bot_token=bot_token,
            command_token=command_token,
        )

        application_tokens.additional_properties = d
        return application_tokens

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
