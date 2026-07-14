from __future__ import annotations

import asyncio

from aiotimebot.storage import MemoryStateStorage, StateKey


async def test_memory_storage_isolated_copies_from_callers() -> None:
    storage = MemoryStateStorage()
    key = StateKey(user_id="user", channel_id="channel")
    original = {"step": 1, "nested": {"answer": 42}}

    await storage.set_data(key, original)
    original["nested"]["answer"] = 0
    loaded = await storage.get_data(key)
    loaded["nested"]["answer"] = -1

    assert await storage.get_data(key) == {"step": 1, "nested": {"answer": 42}}


async def test_memory_storage_update_is_atomic_under_key_lock() -> None:
    storage = MemoryStateStorage()
    key = StateKey(user_id="user", channel_id="channel")
    await storage.set_data(key, {"count": 0})

    async def increment() -> None:
        async with storage.lock(key):
            data = await storage.get_data(key)
            await asyncio.sleep(0)
            data["count"] += 1
            await storage.set_data(key, data)

    await asyncio.gather(*(increment() for _ in range(20)))

    assert await storage.get_data(key) == {"count": 20}


async def test_clear_removes_state_and_data() -> None:
    storage = MemoryStateStorage()
    key = StateKey(user_id="user", channel_id="channel")
    await storage.set_state(key, "waiting_for_name")
    await storage.set_data(key, {"name": "Alice"})

    await storage.clear(key)

    assert await storage.get_state(key) is None
    assert await storage.get_data(key) == {}
