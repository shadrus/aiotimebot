from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_manifest_server_executables import (
        PluginManifestServerExecutables,
    )


T = TypeVar("T", bound="PluginManifestServer")


@_attrs_define
class PluginManifestServer:
    """Generated Time Messenger API v4 model."""

    executables: PluginManifestServerExecutables | Unset = UNSET
    executable: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        executables: dict[str, Any] | Unset = UNSET
        if not isinstance(self.executables, Unset):
            executables = self.executables.to_dict()

        executable = self.executable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if executables is not UNSET:
            field_dict["executables"] = executables
        if executable is not UNSET:
            field_dict["executable"] = executable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_manifest_server_executables import (
            PluginManifestServerExecutables,
        )

        d = dict(src_dict)
        _executables = d.pop("executables", UNSET)
        executables: PluginManifestServerExecutables | Unset
        if isinstance(_executables, Unset):
            executables = UNSET
        else:
            executables = PluginManifestServerExecutables.from_dict(_executables)

        executable = d.pop("executable", UNSET)

        plugin_manifest_server = cls(
            executables=executables,
            executable=executable,
        )

        plugin_manifest_server.additional_properties = d
        return plugin_manifest_server

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
