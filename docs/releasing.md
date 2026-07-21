# Releasing aiotimebot

Releases are built and published by GitHub Actions. PyPI authentication uses
Trusted Publishing, so the repository must not contain a PyPI API token.

## One-time repository setup

Enable two-factor authentication for the PyPI and TestPyPI maintainer accounts.

On PyPI, add a pending GitHub Actions publisher with these values:

```text
PyPI project name: aiotimebot
Owner:             shadrus
Repository:        aiotimebot
Workflow name:     release.yml
Environment name:  pypi
```

On TestPyPI, add a pending publisher with the same owner, repository, and
project name, but use:

```text
Workflow name:     test-pypi.yml
Environment name:  testpypi
```

Create matching `pypi` and `testpypi` environments in the GitHub repository.
Require a maintainer approval for both. Restrict the `pypi` environment to
protected release tags matching `v*`. Neither environment needs a PyPI secret.

A pending publisher does not reserve the project name. Configure it immediately
before the first publication.

## Prepare a release

1. Update `project.version` in `pyproject.toml` and refresh `uv.lock`.
2. Move completed entries from `Unreleased` into a dated section in
   `CHANGELOG.md`.
3. Run the required verification set:

   ```bash
   uv run pytest --cov --cov-report=term-missing --cov-fail-under=95
   uv run ruff check .
   uv run mypy
   uv build --no-sources
   uv run twine check --strict dist/*
   ```

4. Merge the release commit into `main` and wait for CI to pass.

Package-index versions and Git tags are immutable. Never reuse a version or
move an existing release tag.

## TestPyPI dry run

Run the `TestPyPI` workflow manually for the release commit. Each TestPyPI dry
run needs a version that has not already been uploaded there. After publication,
install the exact artifact without resolving dependencies from TestPyPI:

```bash
python -m pip install \
  --index-url https://test.pypi.org/simple/ \
  --no-deps \
  aiotimebot==0.1.1
```

Resolve runtime dependencies from PyPI separately when testing in an empty
environment.

## Publish to PyPI

Create and push a signed tag whose value matches `project.version`:

```bash
git tag -s v0.1.1 -m "aiotimebot 0.1.1"
git push origin v0.1.1
```

The `Release` workflow verifies that the tag matches the package version and
belongs to `main`, rebuilds and checks both distributions, and pauses for the
`pypi` environment approval before publishing. Create the GitHub Release notes
from the same immutable tag after the workflow succeeds.
