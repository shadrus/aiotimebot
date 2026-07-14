from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.plugin_status_state import PluginStatusState
from ..types import UNSET, Unset

T = TypeVar("T", bound="PluginStatus")


@_attrs_define
class PluginStatus:
    """Generated Time Messenger API v4 model."""

    plugin_id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    version: str | Unset = UNSET
    cluster_id: str | Unset = UNSET
    plugin_path: str | Unset = UNSET
    state: PluginStatusState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        plugin_id = self.plugin_id

        name = self.name

        description = self.description

        version = self.version

        cluster_id = self.cluster_id

        plugin_path = self.plugin_path

        state: int | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plugin_id is not UNSET:
            field_dict["plugin_id"] = plugin_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if plugin_path is not UNSET:
            field_dict["plugin_path"] = plugin_path
        if state is not UNSET:
            field_dict["state"] = state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        plugin_id = d.pop("plugin_id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        version = d.pop("version", UNSET)

        cluster_id = d.pop("cluster_id", UNSET)

        plugin_path = d.pop("plugin_path", UNSET)

        _state = d.pop("state", UNSET)
        state: PluginStatusState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PluginStatusState(_state)

        plugin_status = cls(
            plugin_id=plugin_id,
            name=name,
            description=description,
            version=version,
            cluster_id=cluster_id,
            plugin_path=plugin_path,
            state=state,
        )

        plugin_status.additional_properties = d
        return plugin_status

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
