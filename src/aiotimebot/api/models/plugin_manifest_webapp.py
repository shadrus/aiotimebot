from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_manifest_webapp_bundle_path_webapp import (
        PluginManifestWebappBundlePathWebapp,
    )


T = TypeVar("T", bound="PluginManifestWebapp")


@_attrs_define
class PluginManifestWebapp:
    """Generated Time Messenger API v4 model."""

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    version: str | Unset = UNSET
    min_server_version: str | Unset = UNSET
    webapp: PluginManifestWebappBundlePathWebapp | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        version = self.version

        min_server_version = self.min_server_version

        webapp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webapp, Unset):
            webapp = self.webapp.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if version is not UNSET:
            field_dict["version"] = version
        if min_server_version is not UNSET:
            field_dict["min_server_version"] = min_server_version
        if webapp is not UNSET:
            field_dict["webapp"] = webapp

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_manifest_webapp_bundle_path_webapp import (
            PluginManifestWebappBundlePathWebapp,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        version = d.pop("version", UNSET)

        min_server_version = d.pop("min_server_version", UNSET)

        _webapp = d.pop("webapp", UNSET)
        webapp: PluginManifestWebappBundlePathWebapp | Unset
        if isinstance(_webapp, Unset):
            webapp = UNSET
        else:
            webapp = PluginManifestWebappBundlePathWebapp.from_dict(_webapp)

        plugin_manifest_webapp = cls(
            id=id,
            name=name,
            version=version,
            min_server_version=min_server_version,
            webapp=webapp,
        )

        plugin_manifest_webapp.additional_properties = d
        return plugin_manifest_webapp

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
