from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_components import ApplicationComponents


T = TypeVar("T", bound="ApplicationManifest")


@_attrs_define
class ApplicationManifest:
    """Schema for Time Application manifest

    Attributes:
        name (str): Human-readable name of the application.
        description (str): Detailed description of what the application does.
        components (ApplicationComponents):
        icon (str | Unset): Icon for the application (URL).
    """

    name: str
    description: str
    components: ApplicationComponents
    icon: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        components = self.components.to_dict()

        icon = self.icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "components": components,
            }
        )
        if icon is not UNSET:
            field_dict["icon"] = icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_components import ApplicationComponents

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        components = ApplicationComponents.from_dict(d.pop("components"))

        icon = d.pop("icon", UNSET)

        application_manifest = cls(
            name=name,
            description=description,
            components=components,
            icon=icon,
        )

        application_manifest.additional_properties = d
        return application_manifest

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
