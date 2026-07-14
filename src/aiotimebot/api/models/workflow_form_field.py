from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_form_field_data_source import WorkflowFormFieldDataSource
from ..models.workflow_form_field_type import WorkflowFormFieldType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_option import WorkflowOption


T = TypeVar("T", bound="WorkflowFormField")


@_attrs_define
class WorkflowFormField:
    """
    Attributes:
        display_name (str):
        name (str):
        type_ (WorkflowFormFieldType):
        optional (bool):
        subtype (str | Unset):
        default (str | Unset):
        placeholder (str | Unset):
        help_text (str | Unset):
        min_length (int | Unset):
        max_length (int | Unset):
        data_source (WorkflowFormFieldDataSource | Unset):
        options (list[WorkflowOption] | Unset):
    """

    display_name: str
    name: str
    type_: WorkflowFormFieldType
    optional: bool
    subtype: str | Unset = UNSET
    default: str | Unset = UNSET
    placeholder: str | Unset = UNSET
    help_text: str | Unset = UNSET
    min_length: int | Unset = UNSET
    max_length: int | Unset = UNSET
    data_source: WorkflowFormFieldDataSource | Unset = UNSET
    options: list[WorkflowOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_name = self.display_name

        name = self.name

        type_ = self.type_.value

        optional = self.optional

        subtype = self.subtype

        default = self.default

        placeholder = self.placeholder

        help_text = self.help_text

        min_length = self.min_length

        max_length = self.max_length

        data_source: str | Unset = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.value

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "name": name,
                "type": type_,
                "optional": optional,
            }
        )
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if default is not UNSET:
            field_dict["default"] = default
        if placeholder is not UNSET:
            field_dict["placeholder"] = placeholder
        if help_text is not UNSET:
            field_dict["help_text"] = help_text
        if min_length is not UNSET:
            field_dict["min_length"] = min_length
        if max_length is not UNSET:
            field_dict["max_length"] = max_length
        if data_source is not UNSET:
            field_dict["data_source"] = data_source
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_option import WorkflowOption

        d = dict(src_dict)
        display_name = d.pop("display_name")

        name = d.pop("name")

        type_ = WorkflowFormFieldType(d.pop("type"))

        optional = d.pop("optional")

        subtype = d.pop("subtype", UNSET)

        default = d.pop("default", UNSET)

        placeholder = d.pop("placeholder", UNSET)

        help_text = d.pop("help_text", UNSET)

        min_length = d.pop("min_length", UNSET)

        max_length = d.pop("max_length", UNSET)

        _data_source = d.pop("data_source", UNSET)
        data_source: WorkflowFormFieldDataSource | Unset
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = WorkflowFormFieldDataSource(_data_source)

        _options = d.pop("options", UNSET)
        options: list[WorkflowOption] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = WorkflowOption.from_dict(options_item_data)

                options.append(options_item)

        workflow_form_field = cls(
            display_name=display_name,
            name=name,
            type_=type_,
            optional=optional,
            subtype=subtype,
            default=default,
            placeholder=placeholder,
            help_text=help_text,
            min_length=min_length,
            max_length=max_length,
            data_source=data_source,
            options=options,
        )

        workflow_form_field.additional_properties = d
        return workflow_form_field

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
