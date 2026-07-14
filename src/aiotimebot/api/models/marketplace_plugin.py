from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.plugin_manifest import PluginManifest


T = TypeVar("T", bound="MarketplacePlugin")


@_attrs_define
class MarketplacePlugin:
    """Generated Time Messenger API v4 model."""

    homepage_url: str | Unset = UNSET
    icon_data: str | Unset = UNSET
    download_url: str | Unset = UNSET
    release_notes_url: str | Unset = UNSET
    labels: list[str] | Unset = UNSET
    signature: str | Unset = UNSET
    manifest: PluginManifest | Unset = UNSET
    installed_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        homepage_url = self.homepage_url

        icon_data = self.icon_data

        download_url = self.download_url

        release_notes_url = self.release_notes_url

        labels: list[str] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels

        signature = self.signature

        manifest: dict[str, Any] | Unset = UNSET
        if not isinstance(self.manifest, Unset):
            manifest = self.manifest.to_dict()

        installed_version = self.installed_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if homepage_url is not UNSET:
            field_dict["homepage_url"] = homepage_url
        if icon_data is not UNSET:
            field_dict["icon_data"] = icon_data
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if release_notes_url is not UNSET:
            field_dict["release_notes_url"] = release_notes_url
        if labels is not UNSET:
            field_dict["labels"] = labels
        if signature is not UNSET:
            field_dict["signature"] = signature
        if manifest is not UNSET:
            field_dict["manifest"] = manifest
        if installed_version is not UNSET:
            field_dict["installed_version"] = installed_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.plugin_manifest import PluginManifest

        d = dict(src_dict)
        homepage_url = d.pop("homepage_url", UNSET)

        icon_data = d.pop("icon_data", UNSET)

        download_url = d.pop("download_url", UNSET)

        release_notes_url = d.pop("release_notes_url", UNSET)

        labels = cast(list[str], d.pop("labels", UNSET))

        signature = d.pop("signature", UNSET)

        _manifest = d.pop("manifest", UNSET)
        manifest: PluginManifest | Unset
        if isinstance(_manifest, Unset):
            manifest = UNSET
        else:
            manifest = PluginManifest.from_dict(_manifest)

        installed_version = d.pop("installed_version", UNSET)

        marketplace_plugin = cls(
            homepage_url=homepage_url,
            icon_data=icon_data,
            download_url=download_url,
            release_notes_url=release_notes_url,
            labels=labels,
            signature=signature,
            manifest=manifest,
            installed_version=installed_version,
        )

        marketplace_plugin.additional_properties = d
        return marketplace_plugin

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
