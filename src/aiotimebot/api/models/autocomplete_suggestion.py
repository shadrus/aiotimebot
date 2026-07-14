from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AutocompleteSuggestion")


@_attrs_define
class AutocompleteSuggestion:
    """Generated Time Messenger API v4 model."""

    complete: str
    suggestion: str
    hint: str
    description: str
    icon_data: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        complete = self.complete

        suggestion = self.suggestion

        hint = self.hint

        description = self.description

        icon_data = self.icon_data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Complete": complete,
                "Suggestion": suggestion,
                "Hint": hint,
                "Description": description,
                "IconData": icon_data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        complete = d.pop("Complete")

        suggestion = d.pop("Suggestion")

        hint = d.pop("Hint")

        description = d.pop("Description")

        icon_data = d.pop("IconData")

        autocomplete_suggestion = cls(
            complete=complete,
            suggestion=suggestion,
            hint=hint,
            description=description,
            icon_data=icon_data,
        )

        autocomplete_suggestion.additional_properties = d
        return autocomplete_suggestion

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
