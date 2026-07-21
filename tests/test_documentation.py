from __future__ import annotations

import ast
import re
from pathlib import Path

import aiotimebot
from aiotimebot.api.operation_registry import OPERATION_MODULES

ROOT = Path(__file__).parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^]]+\]\(([^)]+)\)")
OPERATION_ROW = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \|$", re.MULTILINE)
PYTHON_FENCE = re.compile(r"```python\n(.*?)```", re.DOTALL)


def markdown_files() -> list[Path]:
    return [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]


def test_documentation_has_no_broken_relative_links() -> None:
    broken: list[str] = []
    for document in markdown_files():
        for raw_target in MARKDOWN_LINK.findall(document.read_text()):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "/")):
                continue
            resolved = (document.parent / target).resolve()
            if not resolved.exists():
                broken.append(f"{document.relative_to(ROOT)} -> {target}")

    assert broken == []


def test_public_facade_is_covered_by_api_reference() -> None:
    reference = (ROOT / "docs" / "api-reference.md").read_text()
    missing = [name for name in aiotimebot.__all__ if f"`{name}`" not in reference]

    assert missing == []


def test_generated_operation_catalog_covers_registry() -> None:
    catalog = (ROOT / "docs" / "api-operations.md").read_text()
    documented = dict(OPERATION_ROW.findall(catalog))

    assert documented == OPERATION_MODULES


def test_readme_links_to_documentation_index() -> None:
    readme = (ROOT / "README.md").read_text()

    assert "[User documentation](docs/README.md)" in readme


def test_documented_python_snippets_are_syntactically_valid() -> None:
    invalid: list[str] = []
    for document in markdown_files():
        for index, snippet in enumerate(PYTHON_FENCE.findall(document.read_text()), 1):
            try:
                ast.parse(snippet)
            except SyntaxError as error:
                invalid.append(
                    f"{document.relative_to(ROOT)} block {index}: {error.msg}"
                )

    assert invalid == []
