from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_manifest_backend import PluginManifestBackend
    from ..models.plugin_manifest_bundle_path_webapp import (
        PluginManifestBundlePathWebapp,
    )
    from ..models.plugin_manifest_server import PluginManifestServer
    from ..models.plugin_manifest_settings_schema import PluginManifestSettingsSchema


T = TypeVar("T", bound="PluginManifest")


@_attrs_define
class PluginManifest:
    """Generated Time Messenger API v4 model."""

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    version: str | Unset = UNSET
    min_server_version: str | Unset = UNSET
    backend: PluginManifestBackend | Unset = UNSET
    server: PluginManifestServer | Unset = UNSET
    webapp: PluginManifestBundlePathWebapp | Unset = UNSET
    settings_schema: PluginManifestSettingsSchema | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        description = self.description

        version = self.version

        min_server_version = self.min_server_version

        backend: dict[str, Any] | Unset = UNSET
        if not isinstance(self.backend, Unset):
            backend = self.backend.to_dict()

        server: dict[str, Any] | Unset = UNSET
        if not isinstance(self.server, Unset):
            server = self.server.to_dict()

        webapp: dict[str, Any] | Unset = UNSET
        if not isinstance(self.webapp, Unset):
            webapp = self.webapp.to_dict()

        settings_schema: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings_schema, Unset):
            settings_schema = self.settings_schema.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if version is not UNSET:
            field_dict["version"] = version
        if min_server_version is not UNSET:
            field_dict["min_server_version"] = min_server_version
        if backend is not UNSET:
            field_dict["backend"] = backend
        if server is not UNSET:
            field_dict["server"] = server
        if webapp is not UNSET:
            field_dict["webapp"] = webapp
        if settings_schema is not UNSET:
            field_dict["settings_schema"] = settings_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_manifest_backend import PluginManifestBackend
        from ..models.plugin_manifest_bundle_path_webapp import (
            PluginManifestBundlePathWebapp,
        )
        from ..models.plugin_manifest_server import PluginManifestServer
        from ..models.plugin_manifest_settings_schema import (
            PluginManifestSettingsSchema,
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        version = d.pop("version", UNSET)

        min_server_version = d.pop("min_server_version", UNSET)

        _backend = d.pop("backend", UNSET)
        backend: PluginManifestBackend | Unset
        if isinstance(_backend, Unset):
            backend = UNSET
        else:
            backend = PluginManifestBackend.from_dict(_backend)

        _server = d.pop("server", UNSET)
        server: PluginManifestServer | Unset
        if isinstance(_server, Unset):
            server = UNSET
        else:
            server = PluginManifestServer.from_dict(_server)

        _webapp = d.pop("webapp", UNSET)
        webapp: PluginManifestBundlePathWebapp | Unset
        if isinstance(_webapp, Unset):
            webapp = UNSET
        else:
            webapp = PluginManifestBundlePathWebapp.from_dict(_webapp)

        _settings_schema = d.pop("settings_schema", UNSET)
        settings_schema: PluginManifestSettingsSchema | Unset
        if isinstance(_settings_schema, Unset):
            settings_schema = UNSET
        else:
            settings_schema = PluginManifestSettingsSchema.from_dict(_settings_schema)

        plugin_manifest = cls(
            id=id,
            name=name,
            description=description,
            version=version,
            min_server_version=min_server_version,
            backend=backend,
            server=server,
            webapp=webapp,
            settings_schema=settings_schema,
        )

        plugin_manifest.additional_properties = d
        return plugin_manifest

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
