from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_manifest import PluginManifest


T = TypeVar("T", bound="GetPluginsResponse200")


@_attrs_define
class GetPluginsResponse200:
    """
    Attributes:
        active (list[PluginManifest] | Unset):
        inactive (list[PluginManifest] | Unset):
    """

    active: list[PluginManifest] | Unset = UNSET
    inactive: list[PluginManifest] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        active: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.active, Unset):
            active = []
            for active_item_data in self.active:
                active_item = active_item_data.to_dict()
                active.append(active_item)

        inactive: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inactive, Unset):
            inactive = []
            for inactive_item_data in self.inactive:
                inactive_item = inactive_item_data.to_dict()
                inactive.append(inactive_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if inactive is not UNSET:
            field_dict["inactive"] = inactive

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_manifest import PluginManifest

        d = dict(src_dict)
        _active = d.pop("active", UNSET)
        active: list[PluginManifest] | Unset = UNSET
        if _active is not UNSET:
            active = []
            for active_item_data in _active:
                active_item = PluginManifest.from_dict(active_item_data)

                active.append(active_item)

        _inactive = d.pop("inactive", UNSET)
        inactive: list[PluginManifest] | Unset = UNSET
        if _inactive is not UNSET:
            inactive = []
            for inactive_item_data in _inactive:
                inactive_item = PluginManifest.from_dict(inactive_item_data)

                inactive.append(inactive_item)

        get_plugins_response_200 = cls(
            active=active,
            inactive=inactive,
        )

        get_plugins_response_200.additional_properties = d
        return get_plugins_response_200

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
