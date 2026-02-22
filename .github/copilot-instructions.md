# Copilot Instructions

## Project Overview
- Python 3.12+ wrapper around the Sportradar DataCore REST API (Handball).
- Public API lives in `src/sportradar_datacore_api/` and is centered on `HandballAPI`.
- The generated OpenAPI client lives in `src/_vendor/datacore_client/` (mirrors `build/`).

## Key Rules
- Do not edit anything in `src/_vendor/` or `build/` by hand. Regenerate via `scripts/codegen.sh` or `scripts/codegen.ps1`.
- Keep helpers in `HandballAPI` high-level and typed; prefer using generated models.
- Use `.env` or environment variables for credentials (see README for names).
- Tests are run with `pytest` (tests live under `test/`).

## Development Notes
- Prefer `uv` for local installs: `uv pip install -e ".[dev]"`.
- When adding functionality, update README examples or notes if the public surface changes.
