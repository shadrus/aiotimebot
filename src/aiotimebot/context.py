"""Explicit dependencies passed to event handlers."""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import TYPE_CHECKING

from .storage import MemoryStateStorage

if TYPE_CHECKING:
    from .client import TimeClient
    from .filters import CommandMatch


@dataclass(frozen=True, slots=True)
class HandlerContext:
    """Dependencies and filter results available to a handler invocation."""

    client: TimeClient | None
    storage: MemoryStateStorage
    command: CommandMatch | None = None

    def with_command(self, command: CommandMatch | None) -> HandlerContext:
        """Create a handler-local context containing a command match."""
        return replace(self, command=command)
