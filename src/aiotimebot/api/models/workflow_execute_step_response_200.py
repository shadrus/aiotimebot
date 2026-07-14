from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkflowExecuteStepResponse200")


@_attrs_define
class WorkflowExecuteStepResponse200:
    """
    Attributes:
        status (int | Unset):
        user_id (str | Unset):
        channel_id (str | Unset):
        id (str | Unset):
    """

    status: int | Unset = UNSET
    user_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        user_id = self.user_id

        channel_id = self.channel_id

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status", UNSET)

        user_id = d.pop("user_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        id = d.pop("id", UNSET)

        workflow_execute_step_response_200 = cls(
            status=status,
            user_id=user_id,
            channel_id=channel_id,
            id=id,
        )

        workflow_execute_step_response_200.additional_properties = d
        return workflow_execute_step_response_200

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
