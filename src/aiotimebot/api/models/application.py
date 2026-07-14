from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_manifest import ApplicationManifest


T = TypeVar("T", bound="Application")


@_attrs_define
class Application:
    """
    Attributes:
        id (str):
        create_at (int):
        update_at (int):
        delete_at (int):
        name (str):
        description (str):
        creator_id (str):
        manifest (ApplicationManifest): Schema for Time Application manifest
        icon (str | Unset):
    """

    id: str
    create_at: int
    update_at: int
    delete_at: int
    name: str
    description: str
    creator_id: str
    manifest: ApplicationManifest
    icon: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        create_at = self.create_at

        update_at = self.update_at

        delete_at = self.delete_at

        name = self.name

        description = self.description

        creator_id = self.creator_id

        manifest = self.manifest.to_dict()

        icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "create_at": create_at,
                "update_at": update_at,
                "delete_at": delete_at,
                "name": name,
                "description": description,
                "creator_id": creator_id,
                "manifest": manifest,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_manifest import ApplicationManifest

        d = dict(src_dict)
        id = d.pop("id")

        create_at = d.pop("create_at")

        update_at = d.pop("update_at")

        delete_at = d.pop("delete_at")

        name = d.pop("name")

        description = d.pop("description")

        creator_id = d.pop("creator_id")

        manifest = ApplicationManifest.from_dict(d.pop("manifest"))

        icon = d.pop("icon", UNSET)

        application = cls(
            id=id,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
            name=name,
            description=description,
            creator_id=creator_id,
            manifest=manifest,
            icon=icon,
        )

        application.additional_properties = d
        return application

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
