from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SystemStatusResponse")


@_attrs_define
class SystemStatusResponse:
    """Generated Time Messenger API v4 model."""

    status: str | Unset = UNSET
    android_latest_version: str | Unset = UNSET
    android_min_version: str | Unset = UNSET
    ios_latest_version: str | Unset = UNSET
    ios_min_version: str | Unset = UNSET
    test_feature_flag: str | Unset = UNSET
    database_status: str | Unset = UNSET
    filestore_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        android_latest_version = self.android_latest_version

        android_min_version = self.android_min_version

        ios_latest_version = self.ios_latest_version

        ios_min_version = self.ios_min_version

        test_feature_flag = self.test_feature_flag

        database_status = self.database_status

        filestore_status = self.filestore_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if android_latest_version is not UNSET:
            field_dict["AndroidLatestVersion"] = android_latest_version
        if android_min_version is not UNSET:
            field_dict["AndroidMinVersion"] = android_min_version
        if ios_latest_version is not UNSET:
            field_dict["IosLatestVersion"] = ios_latest_version
        if ios_min_version is not UNSET:
            field_dict["IosMinVersion"] = ios_min_version
        if test_feature_flag is not UNSET:
            field_dict["TestFeatureFlag"] = test_feature_flag
        if database_status is not UNSET:
            field_dict["database_status"] = database_status
        if filestore_status is not UNSET:
            field_dict["filestore_status"] = filestore_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        android_latest_version = d.pop("AndroidLatestVersion", UNSET)

        android_min_version = d.pop("AndroidMinVersion", UNSET)

        ios_latest_version = d.pop("IosLatestVersion", UNSET)

        ios_min_version = d.pop("IosMinVersion", UNSET)

        test_feature_flag = d.pop("TestFeatureFlag", UNSET)

        database_status = d.pop("database_status", UNSET)

        filestore_status = d.pop("filestore_status", UNSET)

        system_status_response = cls(
            status=status,
            android_latest_version=android_latest_version,
            android_min_version=android_min_version,
            ios_latest_version=ios_latest_version,
            ios_min_version=ios_min_version,
            test_feature_flag=test_feature_flag,
            database_status=database_status,
            filestore_status=filestore_status,
        )

        system_status_response.additional_properties = d
        return system_status_response

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
