"""Composable filters for Time events."""

from __future__ import annotations

import shlex
from dataclasses import dataclass
from typing import Protocol

from .events import PostedEvent, TimeEvent


@dataclass(frozen=True, slots=True)
class CommandMatch:
    """A parsed slash command and its shell-like arguments."""

    name: str
    arguments: tuple[str, ...]


class EventFilter(Protocol):
    """Match an event and optionally return typed match details."""

    def match(self, event: TimeEvent) -> object | None:
        """Return match details, or None when the event is rejected."""
        ...


@dataclass(frozen=True, slots=True)
class Command:
    """Match an exact Time slash command in a posted message."""

    name: str
    ignore_case: bool = False

    def __post_init__(self) -> None:
        normalized = self.name.removeprefix("/")
        if not normalized or any(character.isspace() for character in normalized):
            raise ValueError("command name must be a non-empty token")
        object.__setattr__(self, "name", normalized)

    def match(self, event: TimeEvent) -> CommandMatch | None:
        """Parse a command without accepting prefixes or malformed quotes."""
        if not isinstance(event, PostedEvent):
            return None
        try:
            tokens = shlex.split(event.post.message.strip())
        except ValueError:
            return None
        if not tokens:
            return None
        expected = f"/{self.name}"
        actual = tokens[0]
        equal = (
            actual.casefold() == expected.casefold()
            if self.ignore_case
            else actual == expected
        )
        if not equal:
            return None
        return CommandMatch(name=self.name, arguments=tuple(tokens[1:]))
