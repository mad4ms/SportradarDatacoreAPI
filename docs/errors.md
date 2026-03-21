# Error Reference

All exceptions raised by the wrapper derive from `APIError`.

```
APIError
├── AuthenticationError
├── DependencyError
├── TransportError
├── UnexpectedResponseError
├── NotFoundError
├── StreamingError
└── ValidationError
```

Import path:

```python
from sportradar_datacore_api.errors import (
    APIError,
    AuthenticationError,
    DependencyError,
    TransportError,
    UnexpectedResponseError,
    NotFoundError,
    StreamingError,
    ValidationError,
)
```

---

## `APIError`

Base class for all errors raised by this library. Catch this to handle any wrapper error generically.

---

## `AuthenticationError`

Raised when the OAuth2 token endpoint returns a response missing the `token` field. This indicates a credentials or configuration problem (wrong `CLIENT_ID`, `CLIENT_SECRET`, or `AUTH_URL`).

```python
try:
    api = HandballAPI(...)
except AuthenticationError as e:
    print(f"Check credentials: {e}")
```

---

## `TransportError`

Raised when the underlying HTTP request fails entirely (network error, timeout, DNS failure). Wraps `httpx.HTTPError`.

---

## `DependencyError`

Raised when an optional dependency required for a feature is not installed. The streaming client uses this when `paho-mqtt` is unavailable.

---

## `UnexpectedResponseError`

Raised when the API returns an HTTP 200 but the response body is:
- Not valid JSON
- A JSON shape the wrapper does not recognise
- A non-success envelope from the API

Also raised by `_unwrap_response` when the parsed type does not match the expected model.

---

## `NotFoundError`

Raised when a lookup succeeds (HTTP 200) but the requested entity is absent in the response data. Examples:

- `get_competition_id_by_name` — no competition matches the given name
- `get_season_id_by_year` — no season with the given year exists under the competition
- `get_match_by_id` — fixture ID not found in response

---

## `ValidationError`

Raised for invalid caller-supplied arguments before any network request is made. Examples:

- Empty or blank string passed where an ID is required
- A string that is not a valid UUID passed where a UUID is expected
- `org_id` is `None` when a method requires it

---

## `StreamingError`

Raised for streaming-specific transport or protocol issues that are not plain HTTP failures.

---

## Example: Full Error Handling

```python
from sportradar_datacore_api.errors import (
    AuthenticationError,
    NotFoundError,
    TransportError,
    UnexpectedResponseError,
    ValidationError,
)

try:
    comp_id = api.get_competition_id_by_name("1. Handball-Bundesliga")
    season_id = api.get_season_id_by_year(comp_id, 2024)
    matches = api.list_matches_by_season(season_id)
except ValidationError as e:
    print(f"Bad argument: {e}")
except AuthenticationError as e:
    print(f"Auth failed: {e}")
except NotFoundError as e:
    print(f"Not found: {e}")
except TransportError as e:
    print(f"Network error: {e}")
except UnexpectedResponseError as e:
    print(f"Unexpected API response: {e}")
```
