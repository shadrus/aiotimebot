from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.application_bot_additional_permissions_item import (
    ApplicationBotAdditionalPermissionsItem,
)
from ..models.application_bot_role import ApplicationBotRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ApplicationBot")


@_attrs_define
class ApplicationBot:
    """
    Attributes:
        username (str): Desired username for the bot. Server may add numeric suffix if username is taken.
        display_name (str): Human-readable display name of the bot.
        role (ApplicationBotRole): Role under which bot executes actions.
        additional_permissions (list[ApplicationBotAdditionalPermissionsItem] | Unset): Additional posting permissions
            for the bot.
    """

    username: str
    display_name: str
    role: ApplicationBotRole
    additional_permissions: list[ApplicationBotAdditionalPermissionsItem] | Unset = (
        UNSET
    )
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        username = self.username

        display_name = self.display_name

        role = self.role.value

        additional_permissions: list[str] | Unset = UNSET
        if not isinstance(self.additional_permissions, Unset):
            additional_permissions = []
            for additional_permissions_item_data in self.additional_permissions:
                additional_permissions_item = additional_permissions_item_data.value
                additional_permissions.append(additional_permissions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "username": username,
                "display_name": display_name,
                "role": role,
            }
        )
        if additional_permissions is not UNSET:
            field_dict["additional_permissions"] = additional_permissions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        username = d.pop("username")

        display_name = d.pop("display_name")

        role = ApplicationBotRole(d.pop("role"))

        _additional_permissions = d.pop("additional_permissions", UNSET)
        additional_permissions: (
            list[ApplicationBotAdditionalPermissionsItem] | Unset
        ) = UNSET
        if _additional_permissions is not UNSET:
            additional_permissions = []
            for additional_permissions_item_data in _additional_permissions:
                additional_permissions_item = ApplicationBotAdditionalPermissionsItem(
                    additional_permissions_item_data
                )

                additional_permissions.append(additional_permissions_item)

        application_bot = cls(
            username=username,
            display_name=display_name,
            role=role,
            additional_permissions=additional_permissions,
        )

        application_bot.additional_properties = d
        return application_bot

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
