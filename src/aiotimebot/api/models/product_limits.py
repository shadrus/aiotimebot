from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boards_limits import BoardsLimits
    from ..models.files_limits import FilesLimits
    from ..models.integrations_limits import IntegrationsLimits
    from ..models.messages_limits import MessagesLimits
    from ..models.teams_limits import TeamsLimits


T = TypeVar("T", bound="ProductLimits")


@_attrs_define
class ProductLimits:
    """
    Attributes:
        boards (BoardsLimits | Unset):
        files (FilesLimits | Unset):
        integrations (IntegrationsLimits | Unset):
        messages (MessagesLimits | Unset):
        teams (TeamsLimits | Unset):
    """

    boards: BoardsLimits | Unset = UNSET
    files: FilesLimits | Unset = UNSET
    integrations: IntegrationsLimits | Unset = UNSET
    messages: MessagesLimits | Unset = UNSET
    teams: TeamsLimits | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        boards: dict[str, Any] | Unset = UNSET
        if not isinstance(self.boards, Unset):
            boards = self.boards.to_dict()

        files: dict[str, Any] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = self.files.to_dict()

        integrations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integrations, Unset):
            integrations = self.integrations.to_dict()

        messages: dict[str, Any] | Unset = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages.to_dict()

        teams: dict[str, Any] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if boards is not UNSET:
            field_dict["boards"] = boards
        if files is not UNSET:
            field_dict["files"] = files
        if integrations is not UNSET:
            field_dict["integrations"] = integrations
        if messages is not UNSET:
            field_dict["messages"] = messages
        if teams is not UNSET:
            field_dict["teams"] = teams

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.boards_limits import BoardsLimits
        from ..models.files_limits import FilesLimits
        from ..models.integrations_limits import IntegrationsLimits
        from ..models.messages_limits import MessagesLimits
        from ..models.teams_limits import TeamsLimits

        d = dict(src_dict)
        _boards = d.pop("boards", UNSET)
        boards: BoardsLimits | Unset
        if isinstance(_boards, Unset):
            boards = UNSET
        else:
            boards = BoardsLimits.from_dict(_boards)

        _files = d.pop("files", UNSET)
        files: FilesLimits | Unset
        if isinstance(_files, Unset):
            files = UNSET
        else:
            files = FilesLimits.from_dict(_files)

        _integrations = d.pop("integrations", UNSET)
        integrations: IntegrationsLimits | Unset
        if isinstance(_integrations, Unset):
            integrations = UNSET
        else:
            integrations = IntegrationsLimits.from_dict(_integrations)

        _messages = d.pop("messages", UNSET)
        messages: MessagesLimits | Unset
        if isinstance(_messages, Unset):
            messages = UNSET
        else:
            messages = MessagesLimits.from_dict(_messages)

        _teams = d.pop("teams", UNSET)
        teams: TeamsLimits | Unset
        if isinstance(_teams, Unset):
            teams = UNSET
        else:
            teams = TeamsLimits.from_dict(_teams)

        product_limits = cls(
            boards=boards,
            files=files,
            integrations=integrations,
            messages=messages,
            teams=teams,
        )

        product_limits.additional_properties = d
        return product_limits

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
