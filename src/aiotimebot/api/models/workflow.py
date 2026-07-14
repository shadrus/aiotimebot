from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.workflow_trigger import WorkflowTrigger
from ..models.workflow_type import WorkflowType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_step import WorkflowStep


T = TypeVar("T", bound="Workflow")


@_attrs_define
class Workflow:
    """Generated Time Messenger API v4 model."""

    author: str
    channel_id: str
    steps: list[WorkflowStep]
    title: str
    trigger: WorkflowTrigger
    type_: WorkflowType
    id: str
    description: str | Unset = UNSET
    trigger_detail: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        channel_id = self.channel_id

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        title = self.title

        trigger = self.trigger.value

        type_ = self.type_.value

        id = self.id

        description = self.description

        trigger_detail = self.trigger_detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "channel_id": channel_id,
                "steps": steps,
                "title": title,
                "trigger": trigger,
                "type": type_,
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if trigger_detail is not UNSET:
            field_dict["trigger_detail"] = trigger_detail

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_step import WorkflowStep

        d = dict(src_dict)
        author = d.pop("author")

        channel_id = d.pop("channel_id")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = WorkflowStep.from_dict(steps_item_data)

            steps.append(steps_item)

        title = d.pop("title")

        trigger = WorkflowTrigger(d.pop("trigger"))

        type_ = WorkflowType(d.pop("type"))

        id = d.pop("id")

        description = d.pop("description", UNSET)

        trigger_detail = d.pop("trigger_detail", UNSET)

        workflow = cls(
            author=author,
            channel_id=channel_id,
            steps=steps,
            title=title,
            trigger=trigger,
            type_=type_,
            id=id,
            description=description,
            trigger_detail=trigger_detail,
        )

        workflow.additional_properties = d
        return workflow

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
