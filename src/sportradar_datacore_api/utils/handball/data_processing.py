"""
Handball Data Processing Module
Utilities for ingesting and processing handball data.

Copyright (c) 2025 Michael Adams
Licensed under the MIT License.
"""

import os
import argparse
import pandas as pd
from dotenv import load_dotenv
from sportradar_datacore_api import HandballAPI
from typing import Optional, Dict, Any, List


def initialize_api() -> HandballAPI:
    """Load credentials from .env and instantiate HandballAPI client."""
    load_dotenv(".env", override=True)
    return HandballAPI(
        base_url=os.getenv("BASE_URL", ""),
        auth_url=os.getenv("AUTH_URL", ""),
        client_id=os.getenv("CLIENT_ID", ""),
        client_secret=os.getenv("CLIENT_SECRET", ""),
        org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
        scopes=["read:organization"],
        sport="handball",
    )


def get_competitions(
    api: HandballAPI, competition_name: Optional[str] = None
) -> pd.DataFrame:
    """Retrieve all competitions, optionally filtered by name."""
    params = (
        {"nameLatinContains": competition_name} if competition_name else {}
    )
    competitions = api.get_competitions(params=params)
    if not competitions.get("data"):
        raise ValueError(f"No competitions found for '{competition_name}'")
    return pd.DataFrame(competitions["data"])


def get_competition_id_by_name(api: HandballAPI, competition_name: str) -> str:
    """Get competitionId for a given competition name."""
    competitions = get_competitions(api)
    if (
        competitions.empty
        or competition_name not in competitions["nameLocal"].values
    ):
        raise ValueError(f"Competition '{competition_name}' not found.")
    return competitions.loc[
        competitions["nameLocal"] == competition_name, "competitionId"
    ].values[0]


def get_seasons(api: HandballAPI, competition_id: str) -> pd.DataFrame:
    """Retrieve all seasons for a competition."""
    if not competition_id:
        raise ValueError("Competition ID required.")
    seasons = api.get_seasons(
        competition_id=competition_id, params={"limit": 1000}
    )
    if not seasons.get("data"):
        raise ValueError(
            f"No seasons found for competition ID '{competition_id}'"
        )
    return pd.DataFrame(seasons["data"])


def get_season_id_by_name(
    api: HandballAPI, competition_id: str, season_name: str
) -> str:
    """Get seasonId for a given season name."""
    seasons = get_seasons(api, competition_id)
    if seasons.empty or season_name not in seasons["nameLocal"].values:
        raise ValueError(f"Season '{season_name}' not found.")
    return seasons.loc[seasons["nameLocal"] == season_name, "seasonId"].values[
        0
    ]


def get_fixture_ids_for_season(
    api: HandballAPI, season_id: str
) -> pd.DataFrame:
    """Retrieve all fixtures for a given season ID."""
    if not season_id:
        raise ValueError("Season ID must be provided.")
    fixtures = api.get_season_fixtures(
        season_id=season_id, params={"limit": 1000}
    )
    if not fixtures.get("data"):
        raise ValueError(f"No fixtures found for season ID '{season_id}'")
    return pd.DataFrame(fixtures["data"])


def remove_fields_recursively(data: Any, fields: List[str]) -> None:
    """Remove specified fields from a nested dict/list."""
    if isinstance(data, dict):
        for field in fields:
            data.pop(field, None)
        for value in data.values():
            remove_fields_recursively(value, fields)
    elif isinstance(data, list):
        for item in data:
            remove_fields_recursively(item, fields)


def get_events_for_fixture(
    api: HandballAPI, fixture_id: str, debug: bool = False
) -> pd.DataFrame:
    """Retrieve and flatten all events for a given fixture ID."""
    if not fixture_id:
        raise ValueError("Fixture ID required.")

    fixture = api.get_fixture(
        fixture_id,
        params={
            "include": "entities,organizations,persons",
            "external": "entityId,personId",
        },
    )
    if not fixture or not fixture.get("data"):
        raise ValueError(f"No data for fixture ID '{fixture_id}'")

    fixture_data = fixture["data"][0]
    competitors = fixture_data.get("competitors", [])
    if not competitors:
        raise ValueError(f"No competitors for fixture ID '{fixture_id}'")

    params = {
        "include": "entities,organizations,persons,fixtures,competitions,seasons",
        "external": "entityId,personId",
    }
    playbyplay = api.get_playbyplay(fixture_id=fixture_id, params=params)
    remove_fields_recursively(playbyplay, ["images", "social", "address"])

    playbyplay_data = playbyplay.get("data", [])
    df_data = pd.json_normalize(playbyplay_data)

    includes = playbyplay.get("includes", {}).get("resources", {})
    df_entities = (
        pd.json_normalize(
            list(includes.get("entities", {}).values()), max_level=2
        )
        if "entities" in includes
        else pd.DataFrame()
    )
    df_persons = (
        pd.json_normalize(
            list(includes.get("persons", {}).values()), max_level=2
        )
        if "persons" in includes
        else pd.DataFrame()
    )

    # Merge the DataFrames on their IDs if available
    if not df_entities.empty:
        df_data = df_data.merge(
            df_entities.add_prefix("entity."),
            left_on="entityId",
            right_on="entity.entityId",
            how="left",
        )
    if not df_persons.empty:
        df_data = df_data.merge(
            df_persons.add_prefix("person."),
            left_on="personId",
            right_on="person.personId",
            how="left",
        )

    # Team meta extraction
    home_team = next(c for c in competitors if c.get("isHome"))
    away_team = next(c for c in competitors if not c.get("isHome"))
    home_team_id, away_team_id = home_team["entityId"], away_team["entityId"]

    def lookup(df, eid, col):
        return (
            df.loc[df["entityId"] == eid, col].iloc[0]
            if not df.empty and eid in df["entityId"].values
            else ""
        )

    df_data["team_home_abbr"] = lookup(df_entities, home_team_id, "codeLocal")
    df_data["team_away_abbr"] = lookup(df_entities, away_team_id, "codeLocal")
    df_data["team_home_id"] = home_team_id
    df_data["team_away_id"] = away_team_id
    df_data["team_home_name"] = lookup(
        df_entities, home_team_id, "nameFullLocal"
    )
    df_data["team_away_name"] = lookup(
        df_entities, away_team_id, "nameFullLocal"
    )
    df_data["gameday"] = fixture_data.get("roundNumber", "")

    # Score columns renaming, if available
    score_home_col = f"scores.{home_team_id}"
    score_away_col = f"scores.{away_team_id}"
    if score_home_col in df_data.columns:
        df_data.rename(columns={score_home_col: "score_home"}, inplace=True)
    if score_away_col in df_data.columns:
        df_data.rename(columns={score_away_col: "score_away"}, inplace=True)

    if debug:
        print(df_data.head())

    return df_data


if __name__ == "__main__":

    api = initialize_api()
    # competitions = get_competitions(api)
    # # Assert that we have at least one competition
    # assert not competitions.empty, "No competitions found."
    # print("Competitions retrieved successfully:")
    # print(competitions[["competitionId", "nameLocal"]])
    # # Assert that "1. Handball-Bundesliga" is in the list
    # assert (
    #     "1. Handball-Bundesliga" in competitions["nameLocal"].values
    # ), "1. Handball-Bundesliga not found in competitions."

    # # get the competition ID for "1. Handball-Bundesliga"
    # competition_id = get_competition_id_by_name(api, "1. Handball-Bundesliga")

    # print(f"Competition ID for '1. Handball-Bundesliga': {competition_id}")

    # # Retrieve seasons for the competition
    # seasons = get_seasons(api, competition_id)
    # print("Seasons retrieved successfully:")
    # print(seasons[["seasonId", "nameLocal"]])
    # # Assert that we have at least one season
    # assert not seasons.empty, "No seasons found for the competition."
    # # Assert that "DAIKIN HBL 2024/25" is in the list
    # assert (
    #     "DAIKIN HBL 2024/25" in seasons["nameLocal"].values
    # ), "DAIKIN HBL 2024/25 not found in seasons."
    # # get the season ID for "DAIKIN HBL 2024/25"
    # season_id = get_season_id_by_name(
    #     api, competition_id, "DAIKIN HBL 2024/25"
    # )
    # print(f"Season ID for 'DAIKIN HBL 2024/25': {season_id}")

    season_id = "cabcf509-4373-11ef-a370-9d3c1e90234a"

    # Retrieve fixtures for the season
    fixture_ids = get_fixture_ids_for_season(api, season_id)
    # print all columns in the fixtures DataFrame
    print(fixture_ids.columns.tolist())
    # Assert that we have at least one fixture
    assert not fixture_ids.empty, "No fixtures found for the season."
    print("Fixtures retrieved successfully:")

    for index, row in fixture_ids.iterrows():
        print(
            f"Fixture ID: {row['fixtureId']}, Name: {row['nameLocal']}, Start Time: {row['startTimeLocal']}"
        )
        id_fixture = row["fixtureId"]
        # You can now use id_fixture to download or process the fixture as needed
        # Example: Download fixture events
        # download_fixture_events(id_fixture, out_dir="data/fixtures")
    events_df = get_events_for_fixture(api, id_fixture)
    print(f"Events for fixture {id_fixture}:")

    # name the output file
    output_file = f"events_{id_fixture}.csv"

    # Save the DataFrame to a CSV file
    events_df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"Events saved to {output_file}")
