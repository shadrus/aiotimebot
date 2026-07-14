from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AppError")


@_attrs_define
class AppError:
    """Generated Time Messenger API v4 model."""

    id: str
    message: str
    detailed_error: str
    request_id: str | Unset = UNSET
    status_code: int | Unset = UNSET
    is_oauth: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        message = self.message

        detailed_error = self.detailed_error

        request_id = self.request_id

        status_code = self.status_code

        is_oauth = self.is_oauth

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "message": message,
                "detailed_error": detailed_error,
            }
        )
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if is_oauth is not UNSET:
            field_dict["is_oauth"] = is_oauth

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        message = d.pop("message")

        detailed_error = d.pop("detailed_error")

        request_id = d.pop("request_id", UNSET)

        status_code = d.pop("status_code", UNSET)

        is_oauth = d.pop("is_oauth", UNSET)

        app_error = cls(
            id=id,
            message=message,
            detailed_error=detailed_error,
            request_id=request_id,
            status_code=status_code,
            is_oauth=is_oauth,
        )

        app_error.additional_properties = d
        return app_error

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
