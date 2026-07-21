from __future__ import annotations

import importlib
import re
from pathlib import Path
from typing import Any

import yaml

from aiotimebot.api.client import AuthenticatedClient, Client
from aiotimebot.api.operation_registry import OPERATION_MODULES
from scripts.generate_api import _load_and_correct_schema

CYRILLIC = re.compile(r"[\u0400-\u04ff]")


def operation_ids_from_schema() -> set[str]:
    schema_path = Path(__file__).parents[1] / "schema" / "time-api-v4.yaml"
    schema: dict[str, Any] = yaml.safe_load(schema_path.read_text())
    methods = {"get", "post", "put", "patch", "delete", "head", "options"}
    return {
        operation["operationId"]
        for path_item in schema["paths"].values()
        for method, operation in path_item.items()
        if method.lower() in methods and "operationId" in operation
    }


def test_every_openapi_operation_has_an_async_implementation() -> None:
    expected = operation_ids_from_schema()

    assert len(expected) == 470
    assert set(OPERATION_MODULES) == expected

    missing_async_callables: list[str] = []
    for operation_id, module_name in OPERATION_MODULES.items():
        module = importlib.import_module(module_name)
        if not callable(getattr(module, "asyncio", None)):
            missing_async_callables.append(operation_id)

    assert missing_async_callables == []


def test_generated_public_surface_is_async_only() -> None:
    unexpected_sync_callables: list[str] = []
    for operation_id, module_name in OPERATION_MODULES.items():
        module = importlib.import_module(module_name)
        if callable(getattr(module, "sync", None)) or callable(
            getattr(module, "sync_detailed", None)
        ):
            unexpected_sync_callables.append(operation_id)

    assert unexpected_sync_callables == []
    for client_type in (Client, AuthenticatedClient):
        assert not hasattr(client_type, "get_httpx_client")
        assert not hasattr(client_type, "set_httpx_client")
        assert not hasattr(client_type, "__enter__")


def test_generated_python_documentation_is_english_only() -> None:
    generated_root = Path(__file__).parents[1] / "src" / "aiotimebot" / "api"
    files_with_cyrillic = [
        str(path.relative_to(generated_root))
        for path in generated_root.rglob("*.py")
        if CYRILLIC.search(path.read_text())
    ]

    assert files_with_cyrillic == []


def test_schema_workaround_marks_post_participants_nullable() -> None:
    corrected = _load_and_correct_schema()
    participants = corrected["components"]["schemas"]["Post"]["properties"][
        "participants"
    ]

    assert participants["nullable"] is True


def test_schema_workaround_accepts_both_save_reaction_success_statuses() -> None:
    corrected = _load_and_correct_schema()
    responses = corrected["paths"]["/api/v4/reactions"]["post"]["responses"]

    assert responses["200"] == responses["201"]
