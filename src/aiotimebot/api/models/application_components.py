from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.application_bot import ApplicationBot
    from ..models.application_command import ApplicationCommand


T = TypeVar("T", bound="ApplicationComponents")


@_attrs_define
class ApplicationComponents:
    """
    Attributes:
        bot (ApplicationBot):
        slash_commands (list[ApplicationCommand] | Unset): List of slash commands exposed by the application.
    """

    bot: ApplicationBot
    slash_commands: list[ApplicationCommand] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bot = self.bot.to_dict()

        slash_commands: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.slash_commands, Unset):
            slash_commands = []
            for slash_commands_item_data in self.slash_commands:
                slash_commands_item = slash_commands_item_data.to_dict()
                slash_commands.append(slash_commands_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bot": bot,
            }
        )
        if slash_commands is not UNSET:
            field_dict["slash_commands"] = slash_commands

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application_bot import ApplicationBot
        from ..models.application_command import ApplicationCommand

        d = dict(src_dict)
        bot = ApplicationBot.from_dict(d.pop("bot"))

        _slash_commands = d.pop("slash_commands", UNSET)
        slash_commands: list[ApplicationCommand] | Unset = UNSET
        if _slash_commands is not UNSET:
            slash_commands = []
            for slash_commands_item_data in _slash_commands:
                slash_commands_item = ApplicationCommand.from_dict(
                    slash_commands_item_data
                )

                slash_commands.append(slash_commands_item)

        application_components = cls(
            bot=bot,
            slash_commands=slash_commands,
        )

        application_components.additional_properties = d
        return application_components

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
