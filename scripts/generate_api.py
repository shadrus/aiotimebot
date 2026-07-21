"""Generate the internal typed REST client from the vendored Time schema."""

from __future__ import annotations

import ast
import re
import shutil
import subprocess
import sys
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).parents[1]
SCHEMA_PATH = ROOT / "schema" / "time-api-v4.yaml"
TARGET_PATH = ROOT / "src" / "aiotimebot" / "api"
OPERATION_CATALOG_PATH = ROOT / "docs" / "api-operations.md"

HTTP_METHODS = {"get", "post", "put", "patch", "delete", "head", "options"}
PATH_PARAMETER = re.compile(r"\{[^}]+\}")
CYRILLIC = re.compile(r"[\u0400-\u04ff]")

# These corrections are deliberately narrow and documented. The upstream v4
# schema declares path parameters that do not exist in the corresponding path.
SCHEMA_WORKAROUNDS = {
    "GetTopReactionsForUser",
    "GetTopChannelsForUser",
    "GetInviteBriefInfo",
    "GetRedirectLocation",
    "GetImageByUrl",
}


def _load_and_correct_schema() -> dict[str, Any]:
    schema: dict[str, Any] = yaml.safe_load(SCHEMA_PATH.read_text())

    # Time 7.8 serializes absent post participants as JSON null, while the
    # upstream schema only permits an omitted property or an array.
    post_participants = schema["components"]["schemas"]["Post"]["properties"][
        "participants"
    ]
    post_participants["nullable"] = True

    # Time 7.8 returns 200 for a successfully created reaction, while the
    # upstream schema documents 201. Retain both for cross-version support.
    save_reaction_responses = schema["paths"]["/api/v4/reactions"]["post"][
        "responses"
    ]
    save_reaction_responses["200"] = deepcopy(save_reaction_responses["201"])

    for path in (
        "/api/v4/users/me/top/reactions",
        "/api/v4/users/me/top/channels",
    ):
        operation = schema["paths"][path]["get"]
        operation["parameters"] = [
            parameter
            for parameter in operation["parameters"]
            if not (parameter["name"] == "user_id" and parameter["in"] == "path")
        ]

    invite = schema["paths"]["/api/v4/teams/invite-info"]["get"]
    token = next(item for item in invite["parameters"] if item["name"] == "t")
    token["in"] = "query"

    # The response is described as a channel ranking but references the reaction
    # model in this one operation. The adjacent team endpoint uses TopChannelList.
    channels = schema["paths"]["/api/v4/users/me/top/channels"]["get"]
    channels["responses"]["200"]["content"]["application/json"]["schema"] = {
        "$ref": "#/components/schemas/TopChannelList"
    }

    redirect = schema["paths"]["/api/v4/redirect_location"]["get"]
    redirect_content = redirect["responses"]["200"]["content"]
    redirect_content["application/json"] = redirect_content.pop("image/*")

    image = schema["paths"]["/api/v4/image"]["get"]
    image_content = image["responses"]["200"]["content"]
    image_content["application/octet-stream"] = image_content.pop("image/*")

    translated_tags = {
        "Боты": "Bots",
        "Группы": "Groups",
        "Система": "System",
        "Хранение данных": "Data Retention",
    }
    for path_item in schema["paths"].values():
        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS:
                continue
            operation["tags"] = [
                translated_tags.get(tag, tag) for tag in operation.get("tags", [])
            ]
    return schema


def _render_url(node: ast.expr) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "format"
        and isinstance(node.func.value, ast.Constant)
        and isinstance(node.func.value.value, str)
    ):
        return node.func.value.value
    if not isinstance(node, ast.JoinedStr):
        return None

    result: list[str] = []
    for value in node.values:
        if isinstance(value, ast.Constant) and isinstance(value.value, str):
            result.append(value.value)
        elif isinstance(value, ast.FormattedValue) and isinstance(
            value.value, ast.Name
        ):
            result.append("{" + value.value.id + "}")
        else:
            return None
    return "".join(result)


def _endpoint_key(module_path: Path) -> tuple[str, str] | None:
    tree = ast.parse(module_path.read_text())
    for node in tree.body:
        if not isinstance(node, ast.FunctionDef) or node.name != "_get_kwargs":
            continue
        for child in ast.walk(node):
            if isinstance(child, ast.AnnAssign):
                is_kwargs = (
                    isinstance(child.target, ast.Name) and child.target.id == "_kwargs"
                )
                assigned_value = child.value
            elif isinstance(child, ast.Assign):
                is_kwargs = any(
                    isinstance(target, ast.Name) and target.id == "_kwargs"
                    for target in child.targets
                )
                assigned_value = child.value
            else:
                continue
            if not is_kwargs or assigned_value is None:
                continue
            if not isinstance(assigned_value, ast.Dict):
                continue
            values = {
                key.value: value
                for key, value in zip(
                    assigned_value.keys, assigned_value.values, strict=True
                )
                if isinstance(key, ast.Constant) and isinstance(key.value, str)
            }
            method_node = values.get("method")
            url_node = values.get("url")
            if not (
                isinstance(method_node, ast.Constant)
                and isinstance(method_node.value, str)
                and url_node is not None
            ):
                return None
            url = _render_url(url_node)
            return None if url is None else (method_node.value.lower(), url)
    return None


def _write_operation_registry(schema: dict[str, Any]) -> dict[str, str]:
    operation_by_endpoint: dict[tuple[str, str], str] = {}
    for path, path_item in schema["paths"].items():
        for method, operation in path_item.items():
            if method.lower() in HTTP_METHODS and "operationId" in operation:
                schema_key = (method.lower(), PATH_PARAMETER.sub("{}", path))
                operation_by_endpoint[schema_key] = operation["operationId"]

    module_by_operation: dict[str, str] = {}
    for module_path in (TARGET_PATH / "api").rglob("*.py"):
        generated_key = _endpoint_key(module_path)
        if generated_key is None:
            continue
        normalized_key = (
            generated_key[0],
            PATH_PARAMETER.sub("{}", generated_key[1]),
        )
        operation_id = operation_by_endpoint.get(normalized_key)
        if operation_id is None:
            raise RuntimeError(
                f"Generated endpoint is absent from schema: {generated_key}"
            )
        relative = module_path.relative_to(TARGET_PATH).with_suffix("")
        module_by_operation[operation_id] = "aiotimebot.api." + ".".join(relative.parts)

    expected = set(operation_by_endpoint.values())
    missing = expected - set(module_by_operation)
    if missing:
        raise RuntimeError(f"OpenAPI operations were not generated: {sorted(missing)}")

    lines = [
        '"""Map Time OpenAPI operation IDs to their generated async modules."""',
        "",
        "from typing import Final",
        "",
        "OPERATION_MODULES: Final[dict[str, str]] = {",
    ]
    lines.extend(
        f"    {operation_id!r}: {module_by_operation[operation_id]!r},"
        for operation_id in sorted(module_by_operation)
    )
    lines.extend(["}", ""])
    (TARGET_PATH / "operation_registry.py").write_text("\n".join(lines))
    return module_by_operation


def _write_operation_catalog(module_by_operation: dict[str, str]) -> None:
    """Write the user-facing operation index from the generated registry."""
    lines = [
        "# Generated REST operation catalog",
        "",
        "This file is generated by `scripts/generate_api.py`. Do not edit it",
        "manually. Import an operation module and call its `asyncio()` or",
        "`asyncio_detailed()` function.",
        "See [Client and REST API](client-and-rest.md) for usage and response",
        "handling.",
        "",
        "| Operation ID | Python module |",
        "|---|---|",
    ]
    lines.extend(
        f"| `{operation_id}` | `{module_by_operation[operation_id]}` |"
        for operation_id in sorted(module_by_operation)
    )
    lines.append("")
    OPERATION_CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    OPERATION_CATALOG_PATH.write_text("\n".join(lines))


def _remove_ast_nodes(path: Path, nodes: list[ast.FunctionDef]) -> None:
    """Remove generated source ranges while preserving the remaining template."""
    source_lines = path.read_text().splitlines(keepends=True)
    for node in sorted(nodes, key=lambda item: item.lineno, reverse=True):
        start = node.lineno
        decorators = getattr(node, "decorator_list", [])
        if decorators:
            start = min(start, *(decorator.lineno for decorator in decorators))
        end = node.end_lineno
        if end is None:
            raise RuntimeError(f"AST node has no end line in {path}")
        del source_lines[start - 1 : end]
    path.write_text("".join(source_lines))


def _make_generated_api_async_only() -> None:
    """Remove sync callables emitted by the dual-mode upstream generator."""
    for endpoint in (TARGET_PATH / "api").rglob("*.py"):
        tree = ast.parse(endpoint.read_text())
        sync_functions = [
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name in {"sync", "sync_detailed"}
        ]
        _remove_ast_nodes(endpoint, sync_functions)

    client_path = TARGET_PATH / "client.py"
    client_tree = ast.parse(client_path.read_text())
    sync_methods: list[ast.FunctionDef] = []
    for node in client_tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        sync_methods.extend(
            child
            for child in node.body
            if isinstance(child, ast.FunctionDef)
            and child.name
            in {"get_httpx_client", "set_httpx_client", "__enter__", "__exit__"}
        )
    _remove_ast_nodes(client_path, sync_methods)


def _replace_non_english_docstrings() -> None:
    """Keep generated Python documentation English without lossy translation."""
    documented_nodes = (
        ast.Module,
        ast.ClassDef,
        ast.FunctionDef,
        ast.AsyncFunctionDef,
    )
    for path in TARGET_PATH.rglob("*.py"):
        source = path.read_text()
        if not CYRILLIC.search(source):
            continue
        tree = ast.parse(source)
        replacements: list[tuple[ast.Expr, str]] = []
        for node in ast.walk(tree):
            if not isinstance(node, documented_nodes) or not node.body:
                continue
            expression = node.body[0]
            if not (
                isinstance(expression, ast.Expr)
                and isinstance(expression.value, ast.Constant)
                and isinstance(expression.value.value, str)
                and CYRILLIC.search(expression.value.value)
            ):
                continue
            if isinstance(node, ast.Module):
                documentation = "Generated Time Messenger API v4 module."
            elif isinstance(node, ast.ClassDef):
                documentation = "Generated Time Messenger API v4 model."
            else:
                documentation = (
                    "Call this Time Messenger API v4 operation asynchronously."
                )
            replacements.append((expression, documentation))

        lines = source.splitlines(keepends=True)
        for expression, documentation in sorted(
            replacements, key=lambda item: item[0].lineno, reverse=True
        ):
            end = expression.end_lineno
            if end is None:
                raise RuntimeError(f"Docstring has no end line in {path}")
            indentation = " " * expression.col_offset
            replacement = f'{indentation}"""{documentation}"""\n'
            lines[expression.lineno - 1 : end] = [replacement]
        path.write_text("".join(lines))


def _apply_generator_workarounds() -> None:
    """Repair known omissions in openapi-python-client 0.29.0 output."""
    no_content_endpoint = (
        TARGET_PATH / "api" / "users" / "permanent_delete_all_users.py"
    )
    source = no_content_endpoint.read_text()
    if "async def asyncio(" not in source:
        source += '''

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> Any | None:
    """Permanently delete all users and return the parsed empty response."""
    return (await asyncio_detailed(client=client)).parsed
'''
        no_content_endpoint.write_text(source)


def generate() -> None:
    """Regenerate the complete internal REST package and operation registry."""
    schema = _load_and_correct_schema()
    generator = Path(sys.executable).with_name("openapi-python-client")

    with tempfile.TemporaryDirectory(prefix="aiotimebot-openapi-") as temporary:
        temporary_path = Path(temporary)
        corrected_schema = temporary_path / "schema.yaml"
        generated_path = temporary_path / "generated"
        corrected_schema.write_text(yaml.safe_dump(schema, sort_keys=False))

        subprocess.run(
            [
                str(generator),
                "generate",
                "--path",
                str(corrected_schema),
                "--meta",
                "none",
                "--output-path",
                str(generated_path),
                "--overwrite",
            ],
            check=True,
        )

        shutil.rmtree(TARGET_PATH, ignore_errors=True)
        shutil.copytree(
            generated_path,
            TARGET_PATH,
            ignore=shutil.ignore_patterns(".ruff_cache", "py.typed"),
        )

    _make_generated_api_async_only()
    _apply_generator_workarounds()
    module_by_operation = _write_operation_registry(schema)
    _write_operation_catalog(module_by_operation)
    _replace_non_english_docstrings()
    (TARGET_PATH / "py.typed").touch()


if __name__ == "__main__":
    generate()
