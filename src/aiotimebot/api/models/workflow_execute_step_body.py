from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_execute_step_body_submission import (
        WorkflowExecuteStepBodySubmission,
    )


T = TypeVar("T", bound="WorkflowExecuteStepBody")


@_attrs_define
class WorkflowExecuteStepBody:
    """Generated Time Messenger API v4 model."""

    url: str | Unset = UNSET
    state: str | Unset = UNSET
    user_id: str | Unset = UNSET
    channel_id: str | Unset = UNSET
    team_id: str | Unset = UNSET
    callback_id: str | Unset = UNSET
    submission: WorkflowExecuteStepBodySubmission | Unset = UNSET
    cancelled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        state = self.state

        user_id = self.user_id

        channel_id = self.channel_id

        team_id = self.team_id

        callback_id = self.callback_id

        submission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.submission, Unset):
            submission = self.submission.to_dict()

        cancelled = self.cancelled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if state is not UNSET:
            field_dict["state"] = state
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if callback_id is not UNSET:
            field_dict["callback_id"] = callback_id
        if submission is not UNSET:
            field_dict["submission"] = submission
        if cancelled is not UNSET:
            field_dict["cancelled"] = cancelled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_execute_step_body_submission import (
            WorkflowExecuteStepBodySubmission,
        )

        d = dict(src_dict)
        url = d.pop("url", UNSET)

        state = d.pop("state", UNSET)

        user_id = d.pop("user_id", UNSET)

        channel_id = d.pop("channel_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        callback_id = d.pop("callback_id", UNSET)

        _submission = d.pop("submission", UNSET)
        submission: WorkflowExecuteStepBodySubmission | Unset
        if isinstance(_submission, Unset):
            submission = UNSET
        else:
            submission = WorkflowExecuteStepBodySubmission.from_dict(_submission)

        cancelled = d.pop("cancelled", UNSET)

        workflow_execute_step_body = cls(
            url=url,
            state=state,
            user_id=user_id,
            channel_id=channel_id,
            team_id=team_id,
            callback_id=callback_id,
            submission=submission,
            cancelled=cancelled,
        )

        workflow_execute_step_body.additional_properties = d
        return workflow_execute_step_body

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
