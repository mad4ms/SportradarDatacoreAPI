# API Reference

Public methods on `HandballAPI`. Import path:

```python
from sportradar_datacore_api.handball import HandballAPI
```

Streaming is exposed separately:

```python
from sportradar_datacore_api.streaming import HandballStreamingAPI
```

## Constructor

```python
HandballAPI(
    base_url: str,
    auth_url: str,
    client_id: str,
    client_secret: str,
    sport: str,
    org_id: str | None = None,
    scopes: list[str] | None = None,  # default: ["read:organization"]
    timeout: int = 5,
    connect_on_init: bool = True,
)
```

Authenticates immediately on construction (unless `connect_on_init=False`). Tokens are refreshed automatically on expiry.

### Context Manager

```python
with HandballAPI(...) as api:
    ...
# session is closed on exit
```

---

## Competition & Season Resolution

### `get_competition_id_by_name`

```python
api.get_competition_id_by_name(
    competition_name: str,
    *,
    limit: int = 50,
    offset: int | None = None,
) -> str
```

Resolves a competition UUID by human-readable name. Performs a case-insensitive exact match on `name_local`. Raises `NotFoundError` if no match is found.

### `get_season_id_by_year`

```python
api.get_season_id_by_year(
    competition_id: str | UUID,
    season_year: int,
    *,
    limit: int = 200,
    offset: int | None = None,
) -> str
```

Resolves a season UUID by competition ID and year integer. Raises `NotFoundError` if no matching season exists.

---

## Teams

### `get_teams_by_season_id`

```python
api.get_teams_by_season_id(
    season_id: str | UUID,
    *,
    limit: int = 100,
    offset: int | None = None,
) -> list[SeasonEntitiesModel]
```

Returns all teams registered for the given season.

### `get_team_by_id`

```python
api.get_team_by_id(entity_id: str | UUID) -> TeamModel
```

Returns full team metadata for a given entity UUID. Raises `NotFoundError` if the entity does not exist.

---

## Players

### `get_players_by_season_id`

```python
api.get_players_by_season_id(
    season_id: str | UUID,
    *,
    limit: int = 200,
    offset: int | None = None,
) -> list[SeasonPersonsModel]
```

Returns all players registered for the given season.

### `get_players_by_ids`

```python
api.get_players_by_ids(
    person_ids: str | Sequence[str | UUID],
    *,
    limit: int = 500,
    offset: int | None = None,
) -> list[PersonModel]
```

Returns full player metadata for one or more person UUIDs. Accepts a comma-separated string, a list of strings, or a list of UUIDs.

### `list_players_by_match`

```python
api.list_players_by_match(
    match_id: str | UUID,
    *,
    limit: int = 200,
    offset: int | None = None,
) -> list[MatchPersonsModel]
```

Returns all players associated with a specific match.

---

## Matches

### `list_matches_by_season`

```python
api.list_matches_by_season(
    season_id: str | UUID,
    *,
    limit: int = 500,
    offset: int | None = None,
) -> list[MatchModel]
```

Returns all matches for the given season.

### `get_match_by_id`

```python
api.get_match_by_id(match_id: str | UUID) -> MatchModel
```

Returns full match metadata for a given fixture UUID. Raises `NotFoundError` if not found.

### `get_match_events`

```python
api.get_match_events(
    match_id: str | UUID,
    setup_only: bool,
    with_scores: bool,
) -> list[dict[str, Any]]
```

Returns play-by-play events for a match as a list of plain dicts. Set `setup_only=False` to include all events. Set `with_scores=True` to include running score in each event.

---

## Low-Level Access

For endpoints not covered by the helpers above, use `api.client` directly:

```python
from datacore_client.api.competitions import competition_list

response = competition_list.sync_detailed(
    client=api.client,
    organization_id=api.org_id,
)
```

`api.client` is an `AuthenticatedClient` instance. Tokens are refreshed automatically before each call via `_ensure_client()`.

---

## Streaming API

### `HandballStreamingAPI`

```python
HandballStreamingAPI(
    *,
    client_id: str,
    client_secret: str,
    sport: str,
    token_base_url: str | None = None,
    auth_url: str | None = None,
    timeout: int = 5,
)
```

Separate client for requesting streaming access grants and creating MQTT/WebSocket clients.

### `get_fixture_access`

```python
stream_api.get_fixture_access(
    fixture_id: str,
    scopes: Sequence[str],
    *,
    include_port: bool = False,
) -> StreamAccessGrant
```

Retrieves a signed websocket URL, client identifier, and granted topics for a fixture stream.

### `get_venue_access`

```python
stream_api.get_venue_access(
    venue_id: str,
    scopes: Sequence[str],
    *,
    include_port: bool = False,
) -> StreamAccessGrant
```

Retrieves a signed websocket URL, client identifier, and granted topics for a venue stream.

### `get_specific_fixture_access`

```python
stream_api.get_specific_fixture_access(
    topics: Sequence[str],
    scopes: Sequence[str],
) -> StreamAccessGrant
```

Requests access to specific fixture topics rather than the broader fixture grant.

### `create_fixture_stream`

```python
stream_api.create_fixture_stream(
    fixture_id: str,
    scopes: Sequence[str],
    *,
    include_port: bool = False,
    keepalive: int = 15,
    auto_subscribe: bool = True,
    include_catchup: bool = True,
    include_response: bool = True,
    on_message: Callable[[StreamMessage], None] | None = None,
) -> HandballStreamClient
```

Returns a configured MQTT/WebSocket client for fixture streams.

### `create_venue_stream`

```python
stream_api.create_venue_stream(
    venue_id: str,
    scopes: Sequence[str],
    *,
    include_port: bool = False,
    keepalive: int = 15,
    auto_subscribe: bool = True,
    include_catchup: bool = True,
    include_response: bool = True,
    on_message: Callable[[StreamMessage], None] | None = None,
) -> HandballStreamClient
```

Returns a configured MQTT/WebSocket client for venue streams.

### `HandballStreamClient`

Key operations:

```python
client.connect()
client.loop_start()
client.subscribe_granted_topics()
client.publish_to_scope("write:stream_events", payload)
client.stop()
```

Incoming messages are exposed as `StreamMessage` objects. If the payload contains `compressedData`, it is decoded automatically and attached as `decodedCompressedData` to the parsed payload.

---

## Return Model Packages

All return types come from `src/_vendor/datacore_client/models`. Key models:

| Model | Used by |
|---|---|
| `CompetitionModel` | `get_competition_id_by_name` (internal) |
| `SeasonModel` | `get_season_id_by_year` (internal) |
| `SeasonEntitiesModel` | `get_teams_by_season_id` |
| `SeasonPersonsModel` | `get_players_by_season_id` |
| `TeamModel` | `get_team_by_id` |
| `PersonModel` | `get_players_by_ids` |
| `MatchPersonsModel` | `list_players_by_match` |
| `MatchModel` | `list_matches_by_season`, `get_match_by_id` |
