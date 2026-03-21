# AI Coding Agent Instructions

Guidance for AI assistants (Claude Code, GitHub Copilot, Cursor, etc.) working in this repository.

## Project Overview

Python 3.12+ wrapper around the Sportradar DataCore REST API (Handball).

- Public API: `src/sportradar_datacore_api/` — centered on `HandballAPI`
- Generated OpenAPI client: `src/_vendor/datacore_client/` (mirrors `build/`)
- Full architecture: [docs/architecture.md](docs/architecture.md)

## Hard Rules

- **Never edit `src/_vendor/` or `build/` by hand.** These are fully generated. Regenerate via `scripts/codegen.sh` (Linux/Mac) or `scripts/codegen.ps1` (Windows).
- **Never commit `.env` or credential files.** Credentials are managed through environment variables only. See [README.md](README.md#configuration) for required variable names.
- **Never add `# type: ignore` or `Any` casts in `src/sportradar_datacore_api/`.** Maintain full type safety in hand-written code. Vendor code is excluded from mypy via config.

## Code Style

- Target Python 3.12+. Use built-in generics (`list[X]`, `dict[K, V]`, `X | Y`) — no `from __future__ import annotations`.
- Formatter and linter: `ruff` (line length 88, config in `pyproject.toml`). Run `ruff check --fix` and `ruff format` before committing.
- Static typing: `mypy --strict` (applied to `src/sportradar_datacore_api/` only).
- Pre-commit hooks enforce all of the above automatically. Install with `pre-commit install`.

## Adding Functionality

1. Add high-level helpers to `HandballAPI` in `src/sportradar_datacore_api/handball.py`.
2. Use generated models from `datacore_client.models` for all typed returns.
3. Raise typed errors from `src/sportradar_datacore_api/errors.py` — never raise bare `Exception`.
4. Write tests in `test/` using `pytest`. Tests use live API calls and are skipped when env vars are absent.
5. Update [README.md](README.md) examples if the public surface changes.

## Testing

```bash
pytest
```

Live API calls require env vars. Tests are skipped automatically when credentials are not set. Do not mock the HTTP transport layer — tests validate real API contract behaviour.

## Code Generation

When the upstream OpenAPI spec changes, regenerate the vendor client:

```bash
# Linux / Mac
./scripts/codegen.sh

# Windows (PowerShell)
./scripts/codegen.ps1
```

The generator fetches the spec from the Sportradar developer portal, runs `openapi-python-client`, and moves the output into `src/_vendor/datacore_client/`.

## Repository Layout

```
src/
  sportradar_datacore_api/   # Hand-written public API (edit here)
    api.py                   # DataCoreAPI base: OAuth2 auth, token refresh
    handball.py              # HandballAPI: high-level helpers
    errors.py                # Typed exception hierarchy
    __init__.py
  _vendor/
    datacore_client/         # Generated OpenAPI client (do not edit)
scripts/
  codegen.sh                 # Client regeneration (Linux/Mac)
  codegen.ps1                # Client regeneration (Windows)
openapi/
  config.yaml                # openapi-python-client generator config
test/
  test_handball.py           # Integration tests (live API)
docs/                        # Extended documentation
```

## Further Reading

- [docs/architecture.md](docs/architecture.md) — design decisions, layering, auth flow
- [docs/api-reference.md](docs/api-reference.md) — `HandballAPI` public method reference
- [docs/development.md](docs/development.md) — setup, CI, releasing
- [docs/errors.md](docs/errors.md) — exception hierarchy
