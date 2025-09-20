# Sportradar DataCore API (Handball)

A Python package that authenticates against Sportradar DataCore and provides a convenient, typed interface to Handball data. It wraps a generated OpenAPI client and exposes high-level helpers for common workflows (competitions, seasons, fixtures, play-by-play exports).

- OAuth2 token acquisition, caching, and auto-refresh
- Typed client generated from the official Handball REST OpenAPI spec
- High-level helpers for handball data access
- Example notebook for season downloads
- Simple CSV export of play-by-play events


## Requirements

- Python 3.10+
- Package Manager 'uv': `python -m pip install uv`
- Valid Sportradar DataCore credentials (Client ID, Secret, Organization ID)


## Installation

Clone and install the package:

```bash
git clone https://github.com/mad4ms/SportradarDatacoreAPI.git
cd SportradarDatacoreAPI
uv pip install -U pip   # optional, updates pip inside the environment uv manages
uv pip install .
```


This project vendors the generated client under `src/_vendor/datacore_client`. Import wiring is handled automatically in `sportradar_datacore_api/api.py`.
Vendor was imported using `openapi-python-client` with REST OpenAPI description.


## Configuration

Provide credentials via environment variables (a `.env` file is supported via `python-dotenv`).

Example `.env` placed in the repository root:

```env
BASE_URL=https://api.dc.connect.sportradar.com/v1
AUTH_URL=https://token.connect.sportradar.com/v1/oauth2/rest/token
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
CLIENT_ORGANIZATION_ID=your_org_id
```


## Quickstart

```python
from dotenv import load_dotenv
import os
from sportradar_datacore_api.handball import HandballAPI

# Load .env if present
load_dotenv()

api = HandballAPI(
    base_url=os.getenv("BASE_URL", ""),
    auth_url=os.getenv("AUTH_URL", ""),
    client_id=os.getenv("CLIENT_ID", ""),
    client_secret=os.getenv("CLIENT_SECRET", ""),
    org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
    scopes=["read:organization"],
    sport="handball",
)

competition_name = "1. Handball-Bundesliga"
season_year = 2024  # integer year

comp_id = api.get_competition_id_by_name(competition_name)
print(f"Competition: {competition_name} -> {comp_id}")

season_id = api.get_season_id_by_year(comp_id, season_year)
print(f"Season year {season_year} -> {season_id}")

fixtures = api.get_list_matches_by_season_id(season_id)
print(f"Found {len(fixtures)} fixtures")

first_fixture_id = fixtures[0].fixture_id
print("First fixture id:", first_fixture_id)

# Export play-by-play (PBP) events for one fixture
pbp = api.get_fixture_events_by_id(first_fixture_id)

# Some responses encapsulate events under a key; normalize for CSV helper
if isinstance(pbp, dict) and "events" in pbp:
    events = pbp["events"]
else:
    events = pbp  # already list-like in some cases

api.save_events_to_csv(events, f"fixture_{first_fixture_id}_events.csv")
print("Saved CSV:", f"fixture_{first_fixture_id}_events.csv")
```

Notes:
- The helpers come from `sportradar_datacore_api.handball.HandballAPI`.
- Under the hood, a typed OpenAPI client is used for requests and models.


## Project structure (high level)

- `src/sportradar_datacore_api/`
  - `api.py` — Core OAuth2 client (`DataCoreAPI`)
  - `handball.py` — Handball-specific helpers (`HandballAPI`):
    - `get_competition_id_by_name(name: str) -> str`
    - `get_season_id_by_year(competition_id: str, season_year: int) -> str`
    - `get_list_matches_by_season_id(season_id: str) -> list`
    - `get_fixture_events_by_id(fixture_id: str) -> dict`
    - `save_events_to_csv(events: list[dict], file_path: str) -> None`
- `src/_vendor/datacore_client/` — Generated client (vendored)
- `openapi/` — Handball REST spec (`handball_rest.json` ignored due to size) and generator config
- `scripts/` — Client regeneration scripts for Windows/macOS/Linux
- `notebooks/` — Jupyter examples (see `download_season_events.ipynb`)
- `test/` — Basic tests (`test_handball.py`)
- `log/` — Sample JSONs/CSVs from exploratory runs


## Regenerate the OpenAPI client (optional)

The typed client is generated from `openapi/handball_rest.json` using `openapi-python-client` and then vendored into `src/_vendor/datacore_client`.

Prerequisites:

```bash
# ensure dev tools are installed
pip install -e .[dev]
```

- Windows (PowerShell):

```powershell
# create and activate a virtual env (if you don't already have one)
python -m venv .venv; .\.venv\Scripts\Activate.ps1
# run the generator script
./scripts/codegen.ps1
```

- macOS/Linux (bash):

```bash
python -m venv .venv
source .venv/bin/activate
./scripts/codegen.sh
```

The script will:
- Generate the client into a temporary folder
- Move it into `src/_vendor/datacore_client`
- Clean up the temp output


## Notebooks

`notebooks/download_season_events.ipynb` demonstrates the full flow:
- Load credentials via `.env`
- Resolve competition + season
- List fixtures
- Download play-by-play and export CSV

Open the notebook in VS Code or Jupyter and run cells sequentially.


## Testing

Run tests with pytest:

```bash
pytest -q
```

You can also run a specific test file:

```bash
pytest -q test/test_handball.py
```


## Troubleshooting

- 401/403 errors: verify `CLIENT_ID`, `CLIENT_SECRET`, and organization access for the sport.
- Empty results: confirm organization scope (`read:organization`) and that IDs belong to the same org.
- TLS/SSL: the client enforces SSL verification; ensure certificates are valid on your system.



## License

MIT — see `LICENSE`.


## Disclaimer

This project is an unofficial helper/wrapper and is not affiliated with or endorsed by Sportradar. API access requires a valid contract and credentials from Sportradar.
