# Sportradar DataCore API – Handball Edition

_“Because sometimes you just need to know who scored and exactly when.”_

## Overview

**Sportradar DataCore API** is a lightweight, OAuth2-authenticated Python wrapper for accessing handball data from the [Sportradar DataCore API](https://developer.connect.sportradar.com/datacore/handball_rest.html). It supports token management, request handling, and provides high-level access to handball-specific resources like organizations, competitions, seasons, teams, players, and play-by-play data.

Built for engineers who need structure, clarity, and just the right amount of sarcasm.

---

## Features

- 🔐 OAuth2 authentication (handled automatically)
- 🏢 Organizations, leagues, and competitions
- 📅 Seasons, fixtures, and team rosters
- 🧍 Persons and appearances per season
- 📈 Full play-by-play event access
- 🧰 Consistent request patterns via `.get_*` methods
- 🧼 Clean API design with test scaffolding

---

## Installation

```bash
git clone https://github.com/mad4ms/SportradarDatacoreAPI.git
cd SportradarDatacoreAPI
poetry install
```
You'll need Python 3.10+ and an active Sportradar DataCore account with proper credentials.

## Setup

Create a `.env` file at the root with your access credentials:
You'll need Python 3.10+ and an active Sportradar DataCore account with proper credentials.

```bash
BASE_URL = "https://api.dc.connect.sportradar.com/v1" 
AUTH_URL = "https://token.connect.sportradar.com/v1/oauth2/rest/token" 
CLIENT_ID = your_client_id
CLIENT_SECRET = your_client_secret
CLIENT_ORGANIZATION_ID = your_org_id
```

## Usage

```python
from sportradar_datacore_api.handball import HandballAPI

api = HandballAPI(
    base_url=os.getenv("BASE_URL", ""),
    auth_url=os.getenv("AUTH_URL", ""),
    client_id=os.getenv("CLIENT_ID", ""),
    client_secret=os.getenv("CLIENT_SECRET", ""),
    org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
    scopes=["read:organization"],
    sport="handball",
)

# Fetch competitions
competitions = api.get_competitions()
print(competitions["data"])
```

## Example Test Flow

Run the provided test script for an end-to-end data extraction journey:

```bash
python tests/test_handball_api.py
```

This will:

1. Authenticate and fetch organizations.
2. Get Bundesliga competitions.
3. Select current seasons and fixtures.
4. Lookup team and player data.
5. Extract play-by-play events with coordinates, timestamps, and score deltas.

All results are logged as formatted JSON in the /log directory for inspection.