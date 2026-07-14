from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_command_request import ApplicationCommandRequest


T = TypeVar("T", bound="ApplicationCommand")


@_attrs_define
class ApplicationCommand:
    """
    Attributes:
        trigger_word (str): Command trigger (without leading slash). Must be unique within the application.
        title (str): Command title shown to users.
        list_in_autocomplete (bool): Whether this command should appear in autocomplete.
        request (ApplicationCommandRequest):
        autocomplete_hint (str | Unset): Optional hint describing command parameters for autocomplete.
        autocomplete_description (str | Unset): Additional description shown in autocomplete.
    """

    trigger_word: str
    title: str
    list_in_autocomplete: bool
    request: ApplicationCommandRequest
    autocomplete_hint: str | Unset = UNSET
    autocomplete_description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_word = self.trigger_word

        title = self.title

        list_in_autocomplete = self.list_in_autocomplete

        request = self.request.to_dict()

        autocomplete_hint = self.autocomplete_hint

        autocomplete_description = self.autocomplete_description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trigger_word": trigger_word,
                "title": title,
                "list_in_autocomplete": list_in_autocomplete,
                "request": request,
            }
        )
        if autocomplete_hint is not UNSET:
            field_dict["autocomplete_hint"] = autocomplete_hint
        if autocomplete_description is not UNSET:
            field_dict["autocomplete_description"] = autocomplete_description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_command_request import ApplicationCommandRequest

        d = dict(src_dict)
        trigger_word = d.pop("trigger_word")

        title = d.pop("title")

        list_in_autocomplete = d.pop("list_in_autocomplete")

        request = ApplicationCommandRequest.from_dict(d.pop("request"))

        autocomplete_hint = d.pop("autocomplete_hint", UNSET)

        autocomplete_description = d.pop("autocomplete_description", UNSET)

        application_command = cls(
            trigger_word=trigger_word,
            title=title,
            list_in_autocomplete=list_in_autocomplete,
            request=request,
            autocomplete_hint=autocomplete_hint,
            autocomplete_description=autocomplete_description,
        )

        application_command.additional_properties = d
        return application_command

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
