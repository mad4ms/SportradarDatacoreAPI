# Sportradar DataCore API (Handball)

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A Python wrapper for the Sportradar DataCore REST API (Handball).

The package also includes a separate client for the DataCore Streaming API, keeping the REST and MQTT/WebSocket surfaces isolated.

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

### Using uv (Recommended)
If you use [uv](https://github.com/astral-sh/uv) for fast package management:

```bash
git clone https://github.com/mad4ms/SportradarDatacoreAPI.git
cd SportradarDatacoreAPI
uv sync
```

If you prefer an editable install instead of syncing a lockfile:

```bash
uv pip install -e "."
```

To enable the streaming client as well:

```bash
uv pip install -e ".[stream]"
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
STREAM_TOKEN_BASE_URL=https://token.connect.sportradar.com/v1
STREAM_FIXTURE_ID=your_fixture_id
STREAM_VENUE_ID=your_venue_id
```

`STREAM_TOKEN_BASE_URL` is the token service base for the streaming API. If you already have `AUTH_URL` set to `/oauth2/rest/token`, the streaming client can derive the base URL from it automatically.

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
fixtures = api.list_matches_by_season(season_id)
print(f"Found {len(fixtures)} matches.")

# Fetch match details and events
match = api.get_match_by_id(fixtures[0].fixture_id)
events = api.get_match_events(match.fixture_id, setup_only=False, with_scores=True)
players = api.list_players_by_match(match.fixture_id)
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

  ## Streaming API

  The streaming API is intentionally exposed via separate classes so the REST and MQTT clients stay independent.

  ### Connect To A Fixture Stream

  ```python
  import os

  from sportradar_datacore_api.streaming import HandballStreamingAPI


  def handle_message(message) -> None:
    print(message.topic)
    print(message.message_type)
    print(message.payload)


  stream_api = HandballStreamingAPI(
    client_id=os.getenv("CLIENT_ID", ""),
    client_secret=os.getenv("CLIENT_SECRET", ""),
    sport="handball",
    token_base_url=os.getenv("STREAM_TOKEN_BASE_URL"),
    auth_url=os.getenv("AUTH_URL"),
  )

  client = stream_api.create_fixture_stream(
    fixture_id=os.getenv("STREAM_FIXTURE_ID", ""),
    scopes=[
      "read:stream_events",
      "read:stream_status",
      "read:stream_statistics",
      "read:stream_play_by_play",
      "read:stream_persons",
    ],
    on_message=handle_message,
  )

  with client:
    input("Press Enter to stop listening...\n")
  ```

  ### Publish To A Granted Topic

  ```python
  stream_api = HandballStreamingAPI(
    client_id=os.getenv("CLIENT_ID", ""),
    client_secret=os.getenv("CLIENT_SECRET", ""),
    sport="handball",
    token_base_url=os.getenv("STREAM_TOKEN_BASE_URL"),
  )

  client = stream_api.create_fixture_stream(
    fixture_id=os.getenv("STREAM_FIXTURE_ID", ""),
    scopes=["write:stream_events", "read:response"],
  )

  event_message = {
    "type": "event",
    "fixtureId": os.getenv("STREAM_FIXTURE_ID", ""),
    "clientType": "MyApp:1.0.0",
    "data": {
      "eventId": "11111111-1111-1111-1111-111111111111",
      "class": "heartbeat",
      "eventType": "client",
    },
  }

  with client:
    result = client.publish_to_scope("write:stream_events", event_message)
    print(result)
  ```

  Messages containing `compressedData` are decoded automatically and exposed as `decodedCompressedData` in the parsed payload.

## Architecture

This project uses a **Wrapper Pattern** around a generated OpenAPI client.

- **`src/sportradar_datacore_api/`**: The public-facing code. Contains the `HandballAPI` class, authentication logic, and user-friendly helpers.
- **`src/sportradar_datacore_api/streaming.py`**: Separate streaming access and MQTT client.
- **`src/_vendor/datacore_client/`**: The low-level client code generated from the Sportradar OpenAPI specification.
  - *Note*: This directory allows us to ship the generated code without external dependencies or versioning conflicts.
  - **Do not edit files in `_vendor` manually.** They are overwritten during code generation.

## Repository Layout

- **`src/sportradar_datacore_api/`**: Hand-written wrapper and helper APIs.
- **`src/_vendor/datacore_client/`**: Generated OpenAPI client (do not edit by hand).
- **`scripts/`**: Code generation helpers for the OpenAPI client.
- **`test/`**: Test suite executed with `pytest`.

## AI Assistance

AI coding assistants should read [AGENTS.md](AGENTS.md) for project-specific guidance and rules.

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

Note: The test suite uses live API calls and will be skipped if required
environment variables are not set.

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
