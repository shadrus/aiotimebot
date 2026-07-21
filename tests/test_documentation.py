from __future__ import annotations

import ast
import re
import tomllib
from pathlib import Path

import yaml

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

    assert (
        "[User documentation]"
        "(https://github.com/shadrus/aiotimebot/tree/main/docs)" in readme
    )


def test_readme_has_only_pypi_safe_links() -> None:
    relative_targets: list[str] = []
    for raw_target in MARKDOWN_LINK.findall((ROOT / "README.md").read_text()):
        target = raw_target.strip().strip("<>")
        if target.startswith(("#", "https://", "mailto:")):
            continue
        relative_targets.append(target)

    assert relative_targets == []


def test_release_metadata_is_complete() -> None:
    with (ROOT / "pyproject.toml").open("rb") as pyproject_file:
        project = tomllib.load(pyproject_file)["project"]

    assert project["authors"] == [{"name": "Yury Krylov"}]
    assert project["maintainers"] == [{"name": "Yury Krylov"}]
    assert project["license"] == "MIT"
    assert project["license-files"] == ["LICENSE"]
    assert set(project["keywords"]) >= {"asyncio", "bot", "sdk", "time-messenger"}
    assert set(project["classifiers"]) >= {
        "Development Status :: 3 - Alpha",
        "Framework :: AsyncIO",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Typing :: Typed",
    }


def test_release_documents_exist() -> None:
    with (ROOT / "pyproject.toml").open("rb") as pyproject_file:
        version = tomllib.load(pyproject_file)["project"]["version"]

    license_text = (ROOT / "LICENSE").read_text()
    changelog = (ROOT / "CHANGELOG.md").read_text()
    readme = (ROOT / "README.md").read_text()

    assert "MIT License" in license_text
    assert "Copyright (c) 2026 Yury Krylov" in license_text
    assert f"## [{version}]" in changelog
    assert f"aiotimebot-{version}-py3-none-any.whl" in readme


def test_release_workflow_uses_isolated_trusted_publishing() -> None:
    workflow_path = ROOT / ".github" / "workflows" / "release.yml"
    workflow_text = workflow_path.read_text()
    workflow = yaml.safe_load(workflow_text)

    assert workflow["on"]["push"]["tags"] == ["v*"]
    assert workflow["permissions"] == {"contents": "read"}

    build = workflow["jobs"]["build"]
    publish = workflow["jobs"]["publish"]
    assert publish["needs"] == "build"
    assert publish["environment"]["name"] == "pypi"
    assert publish["permissions"] == {"id-token": "write"}
    assert "permissions" not in build
    assert "actions/checkout" not in str(publish)
    assert "password:" not in workflow_text
    assert "PYPI_TOKEN" not in workflow_text


def test_test_pypi_workflow_is_manual_and_uses_trusted_publishing() -> None:
    workflow_path = ROOT / ".github" / "workflows" / "test-pypi.yml"
    workflow_text = workflow_path.read_text()
    workflow = yaml.safe_load(workflow_text)

    assert workflow["on"] == {"workflow_dispatch": None}
    publish = workflow["jobs"]["publish"]
    assert publish["environment"]["name"] == "testpypi"
    assert publish["permissions"] == {"id-token": "write"}
    assert "https://test.pypi.org/legacy/" in workflow_text
    assert "password:" not in workflow_text
    assert "PYPI_TOKEN" not in workflow_text


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
