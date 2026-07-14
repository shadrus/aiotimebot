from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_step_type import WorkflowStepType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_form_field import WorkflowFormField
    from ..models.workflow_template import WorkflowTemplate
    from ..models.workflow_variable import WorkflowVariable


T = TypeVar("T", bound="WorkflowStep")


@_attrs_define
class WorkflowStep:
    """Generated Time Messenger API v4 model."""

    id: str
    type_: WorkflowStepType
    name: str | Unset = UNSET
    form_fields: list[WorkflowFormField] | Unset = UNSET
    channel_id: str | Unset = UNSET
    template: WorkflowTemplate | Unset = UNSET
    variables: list[WorkflowVariable] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_.value

        name = self.name

        form_fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.form_fields, Unset):
            form_fields = []
            for form_fields_item_data in self.form_fields:
                form_fields_item = form_fields_item_data.to_dict()
                form_fields.append(form_fields_item)

        channel_id = self.channel_id

        template: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template, Unset):
            template = self.template.to_dict()

        variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.variables, Unset):
            variables = []
            for variables_item_data in self.variables:
                variables_item = variables_item_data.to_dict()
                variables.append(variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if form_fields is not UNSET:
            field_dict["form_fields"] = form_fields
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if template is not UNSET:
            field_dict["template"] = template
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_form_field import WorkflowFormField
        from ..models.workflow_template import WorkflowTemplate
        from ..models.workflow_variable import WorkflowVariable

        d = dict(src_dict)
        id = d.pop("id")

        type_ = WorkflowStepType(d.pop("type"))

        name = d.pop("name", UNSET)

        _form_fields = d.pop("form_fields", UNSET)
        form_fields: list[WorkflowFormField] | Unset = UNSET
        if _form_fields is not UNSET:
            form_fields = []
            for form_fields_item_data in _form_fields:
                form_fields_item = WorkflowFormField.from_dict(form_fields_item_data)

                form_fields.append(form_fields_item)

        channel_id = d.pop("channel_id", UNSET)

        _template = d.pop("template", UNSET)
        template: WorkflowTemplate | Unset
        if isinstance(_template, Unset):
            template = UNSET
        else:
            template = WorkflowTemplate.from_dict(_template)

        _variables = d.pop("variables", UNSET)
        variables: list[WorkflowVariable] | Unset = UNSET
        if _variables is not UNSET:
            variables = []
            for variables_item_data in _variables:
                variables_item = WorkflowVariable.from_dict(variables_item_data)

                variables.append(variables_item)

        workflow_step = cls(
            id=id,
            type_=type_,
            name=name,
            form_fields=form_fields,
            channel_id=channel_id,
            template=template,
            variables=variables,
        )

        workflow_step.additional_properties = d
        return workflow_step

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
