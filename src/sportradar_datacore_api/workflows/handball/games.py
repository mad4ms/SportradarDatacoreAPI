"""
Fixtures & events workflows for Handball.

Provides functions to list fixtures and flatten play-by-play/event exports.
"""

from typing import Any, List
import pandas as pd
from sportradar_datacore_api.handball import HandballAPI


def list_season_fixtures_df(api: HandballAPI, season_id: str) -> pd.DataFrame:
    """
    Return all fixtures for the given season as a DataFrame.

    Raises:
        ValueError: if season_id is missing or no fixtures are found.
    """
    if not season_id:
        raise ValueError("season_id must be provided.")
    resp = api.get_season_fixtures(season_id=season_id, params={"limit": 1000})
    data = resp.get("data") or []
    if not data:
        raise ValueError(f"No fixtures found for season '{season_id}'.")
    return pd.DataFrame(data)


def fetch_fixture_events_df(
    api: HandballAPI,
    fixture_id: str,
    debug: bool = False,
    fields_to_remove: List[str] = None,
) -> pd.DataFrame:
    """
    Retrieve and flatten the full play-by-play + setup events for a fixture.

    Args:
        api: an authenticated HandballAPI instance.
        fixture_id: UUID of the fixture.
        debug: if True, prints head() and column list.
        fields_to_remove: nested JSON keys to strip
                          (defaults to ["images","social","address"]).

    Raises:
        ValueError: if fixture_id is missing or no competitors found.
    """
    if not fixture_id:
        raise ValueError("fixture_id must be provided.")
    fields_to_remove = fields_to_remove or ["images", "social", "address"]

    # 1) fetch fixture metadata (to get competitors)
    fixture_resp = api.get_fixture(
        fixture_id=fixture_id, params={"include": "competitors"}
    )
    fixture_data = fixture_resp.get("data", [])
    if not fixture_data:
        raise ValueError(f"No fixture data for ID '{fixture_id}'")
    competitors = fixture_data[0].get("competitors", [])
    if not competitors:
        raise ValueError(f"No competitors for fixture '{fixture_id}'")

    # identify home/away IDs
    home = next(c for c in competitors if c.get("isHome"))
    away = next(c for c in competitors if not c.get("isHome"))
    home_id, away_id = home["entityId"], away["entityId"]
    roundNumber = fixture_data[0].get("roundNumber", "")

    # 2) fetch play-by-play to get included metadata & strip fields
    pbp = api.get_playbyplay(
        fixture_id=fixture_id,
        params={
            "include": "entities,persons",
            "external": "entityId,personId",
        },
    )
    _remove_fields(pbp, fields_to_remove)

    resources = pbp.get("includes", {}).get("resources", {})
    df_entities = (
        pd.json_normalize(resources.get("entities", {}).values())
        if "entities" in resources
        else pd.DataFrame()
    )
    df_persons = (
        pd.json_normalize(resources.get("persons", {}).values())
        if "persons" in resources
        else pd.DataFrame()
    )

    # 3) fetch full event export
    export = api.get_match_events_export(
        fixture_id=fixture_id,
        params={"withScores": "true"},
    )
    events = export.get("data", []) or []
    df_events = pd.json_normalize(events)

    # 4) merge metadata
    if not df_entities.empty:
        df_events = df_events.merge(
            df_entities.add_prefix("team."),
            left_on="data.entityId",
            right_on="team.entityId",
            how="left",
        )
    if not df_persons.empty:
        df_events = df_events.merge(
            df_persons.add_prefix("player."),
            left_on="data.personId",
            right_on="player.personId",
            how="left",
        )

    # 5) inject home/away info
    def lookup(df: pd.DataFrame, eid: str, col: str) -> Any:
        if not df.empty and eid in df["entityId"].values:
            return df.loc[df["entityId"] == eid, col].iat[0]
        return ""

    df_events["team_home_abbr"] = lookup(df_entities, home_id, "codeLocal")
    df_events["team_away_abbr"] = lookup(df_entities, away_id, "codeLocal")
    df_events["team_home_id"] = home_id
    df_events["team_away_id"] = away_id
    df_events["team_home_name"] = lookup(df_entities, home_id, "nameFullLocal")
    df_events["team_away_name"] = lookup(df_entities, away_id, "nameFullLocal")
    df_events["gameday"] = roundNumber
    df_events["team_attacking_id"] = df_events["data.entityId"]
    df_events["team_attacking_name"] = df_events["team.nameFullLocal"]
    # insert home or away in team_attacking_side
    df_events["team_attacking_side"] = df_events.apply(
        lambda row: "home" if row["team_attacking_id"] == home_id else "away",
        axis=1,
    )

    # 6) rename score columns if present
    home_col = f"scores.{home_id}"
    away_col = f"scores.{away_id}"
    if home_col in df_events.columns:
        df_events.rename(columns={home_col: "score_home"}, inplace=True)
    if away_col in df_events.columns:
        df_events.rename(columns={away_col: "score_away"}, inplace=True)

    if debug:
        print(df_events.head())
        print("Columns:", df_events.columns.tolist())

    return df_events


def _remove_fields(obj: Any, fields: List[str]) -> None:
    """
    Recursively remove specified keys from nested dicts and lists.
    """
    if isinstance(obj, dict):
        for f in fields:
            obj.pop(f, None)
        for v in obj.values():
            _remove_fields(v, fields)
    elif isinstance(obj, list):
        for item in obj:
            _remove_fields(item, fields)
