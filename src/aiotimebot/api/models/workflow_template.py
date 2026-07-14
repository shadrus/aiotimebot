from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_template_type import WorkflowTemplateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowTemplate")


@_attrs_define
class WorkflowTemplate:
    """
    Attributes:
        template (str | Unset):
        type_ (WorkflowTemplateType | Unset):
        to (str | Unset):
    """

    template: str | Unset = UNSET
    type_: WorkflowTemplateType | Unset = UNSET
    to: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        template = self.template

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if template is not UNSET:
            field_dict["template"] = template
        if type_ is not UNSET:
            field_dict["type"] = type_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        template = d.pop("template", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: WorkflowTemplateType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = WorkflowTemplateType(_type_)

        to = d.pop("to", UNSET)

        workflow_template = cls(
            template=template,
            type_=type_,
            to=to,
        )

        workflow_template.additional_properties = d
        return workflow_template

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
