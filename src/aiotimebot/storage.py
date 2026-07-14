"""Optional in-memory conversation state."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator, Mapping
from contextlib import asynccontextmanager
from copy import deepcopy
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class StateKey:
    """Identify state scoped to one user in one Time channel."""

    user_id: str
    channel_id: str


class MemoryStateStorage:
    """Keep optional FSM data in process memory with per-key locking."""

    def __init__(self) -> None:
        self._states: dict[StateKey, str] = {}
        self._data: dict[StateKey, dict[str, Any]] = {}
        self._locks: dict[StateKey, asyncio.Lock] = {}

    async def get_state(self, key: StateKey) -> str | None:
        """Return the current state name."""
        return self._states.get(key)

    async def set_state(self, key: StateKey, state: str | None) -> None:
        """Set or remove the current state name."""
        if state is None:
            self._states.pop(key, None)
        else:
            self._states[key] = state

    async def get_data(self, key: StateKey) -> dict[str, Any]:
        """Return an isolated copy of stored conversation data."""
        return deepcopy(self._data.get(key, {}))

    async def set_data(self, key: StateKey, data: Mapping[str, Any]) -> None:
        """Replace conversation data with an isolated copy."""
        self._data[key] = deepcopy(dict(data))

    async def clear(self, key: StateKey) -> None:
        """Remove both the state name and associated data."""
        self._states.pop(key, None)
        self._data.pop(key, None)

    @asynccontextmanager
    async def lock(self, key: StateKey) -> AsyncIterator[None]:
        """Serialize a read-modify-write transaction for one state key."""
        lock = self._locks.setdefault(key, asyncio.Lock())
        async with lock:
            yield
