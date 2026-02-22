# Sportradar DataCore API (Handball)

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A Python wrapper for the Sportradar DataCore REST API (Handball).

This library simplifies interaction with the Sportradar API by handling OpenID Connect (OIDC) authentication automatically and providing a fully typed interface for all API endpoints.

## Features

- **Automated Authentication**: Handles OAuth2 token acquisition, caching, and transparent refreshing.
- **Fully Typed**: Built on top of a generated OpenAPI client, ensuring 100% type safety for requests and response models.
- **High-Level Helpers**: Convenient methods for common workflows (e.g., resolving `Season IDs` from `Years`, fetching fixtures, players, events, etc.).
- **Hybrid Architecture**:
  - Use high-level helpers in `sportradar_datacore_api` for ease of use.
  - Access the underlying `datacore_client` for raw access to every single API endpoint generated from the official spec.

## Installation

This project requires **Python 3.12+**.

### Standard Installation
Clone the repository and install using pip:

```bash
git clone https://github.com/mad4ms/SportradarDatacoreAPI.git
cd SportradarDatacoreAPI
pip install .
```

### Using uv (Recommended)
If you use [uv](https://github.com/astral-sh/uv) for fast package management:

```bash
git clone https://github.com/mad4ms/SportradarDatacoreAPI.git
cd SportradarDatacoreAPI
uv pip install .
```

## Configuration

The library uses **pydantic** and **python-dotenv** to manage configuration. You can provide credentials via a `.env` file in your project root or via environment variables.

Create a `.env` file:

```env
BASE_URL=https://api.dc.connect.sportradar.com/v1
AUTH_URL=https://token.connect.sportradar.com/v1/oauth2/rest/token
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
CLIENT_ORGANIZATION_ID=your_org_id
```

## Usage

### Basic Example

The main entry point is the `HandballAPI` class.

```python
import os
from dotenv import load_dotenv
from sportradar_datacore_api.handball import HandballAPI

# 1. Load configuration
load_dotenv()

# 2. Initialize the API
api = HandballAPI(
    base_url=os.getenv("BASE_URL", ""),
    auth_url=os.getenv("AUTH_URL", ""),
    client_id=os.getenv("CLIENT_ID", ""),
    client_secret=os.getenv("CLIENT_SECRET", ""),
    org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
    scopes=["read:organization"],
    sport="handball",
)

# 3. Use high-level helpers
# Resolve the ID for "1. Handball-Bundesliga"
comp_id = api.get_competition_id_by_name("1. Handball-Bundesliga")
print(f"Competition ID: {comp_id}")

# Get the season ID for the year 2024
season_id = api.get_season_id_by_year(comp_id, 2024)
print(f"Season ID: {season_id}")

# Fetch fixtures
fixtures = api.get_list_matches_by_season_id(season_id)
print(f"Found {len(fixtures)} matches.")
```

### Advanced: Accessing Raw Client

For endpoints not covered by high-level helpers, accessing the generated client directly is supported and encouraged. The generated client resides in `api.client`.

```python
from datacore_client.api.competitions import competition_list
from datacore_client.models import CompetitionListCompetitionsResponse

# You can access the authenticated low-level client via `api.client`
response = competition_list.sync_detailed(
    client=api.client,
    organization_id=api.org_id
)

if response.status_code == 200:
    # Full type support for the response model
    data: CompetitionListCompetitionsResponse = response.parsed
    print(data.data[0].name_local)
```

## Architecture

This project uses a **Wrapper Pattern** around a generated OpenAPI client.

- **`src/sportradar_datacore_api/`**: The public-facing code. Contains the `HandballAPI` class, authentication logic, and user-friendly helpers.
- **`src/_vendor/datacore_client/`**: The low-level client code generated from the Sportradar OpenAPI specification.
  - *Note*: This directory allows us to ship the generated code without external dependencies or versioning conflicts.
  - **Do not edit files in `_vendor` manually.** They are overwritten during code generation.

## Repository Layout

- **`src/sportradar_datacore_api/`**: Hand-written wrapper and helper APIs.
- **`src/_vendor/datacore_client/`**: Generated OpenAPI client (do not edit by hand).
- **`scripts/`**: Code generation helpers for the OpenAPI client.
- **`test/`**: Test suite executed with `pytest`.
- **`notebooks/`**: Example notebooks for data extraction and analysis.

## AI Assistance

If you are using GitHub Copilot in this repo, see the project-specific guidance in
`.github/copilot-instructions.md`.

## Development

### Setup

```bash
# Install dependencies including dev tools
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

### Code Generation

If the Sportradar OpenAPI specification changes, you can regenerate the client:

**Windows (PowerShell)**:
```powershell
./scripts/codegen.ps1
```

**Linux / Mac**:
```bash
./scripts/codegen.sh
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contributing

Contributions are welcome! Please open issues or pull requests on GitHub.
