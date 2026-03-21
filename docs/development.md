# Development Guide

## Prerequisites

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) (recommended) or `pip`

## Setup

```bash
git clone https://github.com/mad4ms/SportradarDatacoreAPI.git
cd SportradarDatacoreAPI

# Install all dependencies including dev tools
uv pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

Create a `.env` file for credentials (see [README.md](../README.md#configuration)):

```env
BASE_URL=https://api.dc.connect.sportradar.com/v1
AUTH_URL=https://token.connect.sportradar.com/v1/oauth2/rest/token
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
CLIENT_ORGANIZATION_ID=your_org_id
```

## Running Tests

```bash
pytest
```

Tests use live API calls. They are skipped automatically when credentials are not set in the environment. Do not mock the HTTP transport — tests validate real API contract behaviour.

Run with coverage:

```bash
pytest --cov=sportradar_datacore_api
```

## Linting & Formatting

```bash
# Lint and auto-fix
ruff check --fix src test

# Format
ruff format src test

# Type check
mypy src/sportradar_datacore_api
```

Pre-commit hooks run all of the above automatically on `git commit`.

## Pre-commit Hooks

The `.pre-commit-config.yaml` enforces:
- Trailing whitespace / end-of-file fixers
- YAML validity check
- Merge conflict marker detection
- `ruff` lint + format + import sort (excluding `src/_vendor/`)
- `mypy` static type checking (excluding `src/_vendor/`)
- `nbstripout` for Jupyter notebooks
- `pytest` on every commit

## Code Generation

When the upstream Sportradar OpenAPI spec changes, regenerate the vendor client:

```bash
# Linux / Mac
./scripts/codegen.sh

# Windows (PowerShell)
./scripts/codegen.ps1
```

The script:
1. Downloads `handball_rest.json` from the Sportradar developer portal (cached in `openapi/`)
2. Runs `openapi-python-client generate` using `openapi/config.yaml`
3. Moves the generated `datacore_client` package into `src/_vendor/`
4. Cleans up the temporary output directory

Never edit `src/_vendor/` manually — changes are overwritten on the next codegen run.

## CI Pipeline

GitHub Actions runs on every push and pull request to `main`:

| Job | Steps |
|---|---|
| `lint-and-test` | `ruff check`, `mypy`, `pytest` — matrix: Python 3.12 + 3.13 |
| `build` | `uv build` (sdist + wheel), uploads `dist/` artifacts |

Configuration: `.github/workflows/ci.yml`

## Releasing

See [RELEASING.md](../RELEASING.md) for the full release process. Summary:

1. Bump `version` in `pyproject.toml`
2. Ensure `main` is green in CI
3. Push a `vX.Y.Z` tag — the `release.yml` workflow handles the rest (build, PyPI publish, GitHub Release, SBOM, provenance attestation)

## Project Structure

```
src/sportradar_datacore_api/
  api.py        # Base auth layer (DataCoreAPI)
  handball.py   # High-level helpers (HandballAPI)
  errors.py     # Typed exception hierarchy
  __init__.py

src/_vendor/datacore_client/   # Generated — do not edit
scripts/
  codegen.sh    # Client regeneration (Linux/Mac)
  codegen.ps1   # Client regeneration (Windows)
openapi/
  config.yaml   # openapi-python-client config
test/
  test_handball.py
docs/
  architecture.md
  api-reference.md
  development.md  (this file)
  errors.md
```
