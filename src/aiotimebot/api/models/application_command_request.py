from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.application_command_request_method import ApplicationCommandRequestMethod

T = TypeVar("T", bound="ApplicationCommandRequest")


@_attrs_define
class ApplicationCommandRequest:
    """
    Attributes:
        method (ApplicationCommandRequestMethod): HTTP method used when invoking this command.
        url (str): Callback URL invoked when the command is executed.
    """

    method: ApplicationCommandRequestMethod
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        method = self.method.value

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "method": method,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        method = ApplicationCommandRequestMethod(d.pop("method"))

        url = d.pop("url")

        application_command_request = cls(
            method=method,
            url=url,
        )

        application_command_request.additional_properties = d
        return application_command_request

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
