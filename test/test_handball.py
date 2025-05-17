"""Handball API Test Script
This script tests various endpoints of the Sportradar DataCore API for handball.
It includes functions to retrieve organizations, leagues, competitions, seasons,
fixtures, persons, teams, and static resources.
Author: Michael Adams, 2025
"""

# ---------------------- Imports ----------------------
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from sportradar_datacore_api import HandballAPI

# ---------------------- Configuration ----------------------

# Load credentials from .env_prd file
load_dotenv(".env_prd", override=True)

# Initialize API client with environment-based credentials
api = HandballAPI(
    base_url=os.getenv("BASE_URL", ""),
    auth_url=os.getenv("AUTH_URL", ""),
    client_id=os.getenv("CLIENT_ID", ""),
    client_secret=os.getenv("CLIENT_SECRET", ""),
    org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
    scopes=["read:organization"],
    sport="handball",
)

# ---------------------- Utility ----------------------


def print_result(title: str, data: dict | list):
    """
    Pretty-print and persist test output to JSON file for inspection.
    """
    print(f"{title.upper()} {'*' * (70 - len(title))}")
    print(json.dumps(data, indent=2))
    print(f"END OF {title.upper()} {'*' * (70 - len(title))}\n")

    path = Path("log") / f"{title.lower().replace(' ', '_')}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


# ---------------------- Test Functions ----------------------


def test_organizations():
    """
    Test retrieval of all organizations.
    """
    orgs = api.get_organizations()
    print_result("organizations", orgs.get("data", []))


def test_leagues_and_competitions():
    """
    Test league listing and competition lookup by name.
    Returns a sample competition ID for downstream tests.
    """
    leagues = api.get_leagues()
    print_result("leagues", leagues.get("data", []))

    comps = api.get_competitions(params={"nameLatinContains": "Bundesliga"})
    print_result("competitions", comps.get("data", []))

    return comps.get("data", [{}])[0].get("competitionId")


def test_seasons(id_competition: str):
    """
    Retrieve seasons for a given competition and verify season details.
    Returns a season ID.
    """
    seasons = api.get_seasons(
        id_competition, params={"startDate": "2024-01-01"}
    )
    print_result("seasons", seasons.get("data", []))

    season = api.get_season(seasons.get("data", [{}])[0].get("seasonId"))
    print_result("season", season)

    return seasons.get("data", [{}])[0].get("seasonId")


def test_season_entities(id_season: str):
    """
    Filter teams in a season by name, returning a sample team ID.
    """
    params = {
        "external": "entityId,personId",
        "fields": "entity,organization,seasonId,status,added",
        "include": "entities,organizations",
        "limit": "10",
        "entityNameFullLocalContains": "TBV",
    }

    teams = api.get_season_teams(id_season, params)
    print_result("season_teams", teams)

    team_data = teams.get("data", [{}])[0].get("entity")
    return team_data.get("id").split(":")[-1] if team_data else None


def test_season_fixtures(id_season: str, id_competition: str, team_id: str):
    """
    Query fixtures by season, competition, and team.
    Also tests fixture and play-by-play endpoints.
    """
    params = {
        "include": "entities,organizations,persons",
        "external": "entityId,personId",
    }

    season_fixtures = api.get_season_fixtures(id_season, params)
    print_result("season_fixtures", season_fixtures)

    competition_fixtures = api.get_competition_fixtures(id_competition, params)
    print_result("competition_fixtures", competition_fixtures)

    season_team_fixtures = api.get_season_team_fixtures(
        id_season, team_id, params={}
    )
    print_result("season_team_fixtures", season_team_fixtures)

    fixture_id = season_fixtures.get("data", [{}])[0].get("fixtureId")
    if not fixture_id:
        return

    fixture = api.get_fixture(fixture_id, params)
    print_result("fixture", fixture)

    playbyplay = api.get_playbyplay(fixture_id, params)
    print_result("playbyplay", playbyplay)

    # Extract key fields into a flattened structure for easier inspection
    events = []
    for event in playbyplay.get("data", []):
        ev = {
            "sequence": event.get("sequence"),
            "timestamp": event.get("timestamp"),
            "clock": event.get("clock"),
            "eventType": event.get("eventType"),
            "subType": event.get("subType"),
            "entityId": event.get("entityId"),
            "personId": event.get("personId"),
            "playId": event.get("playId"),
            "x": event.get("x"),
            "y": event.get("y"),
            "score_home": None,
            "score_away": None,
        }

        scores = event.get("scores", {})
        score_keys = list(scores.keys())
        if len(score_keys) == 2:
            ev["score_home"] = scores[score_keys[0]]
            ev["score_away"] = scores[score_keys[1]]

        events.append(ev)

    print_result("playbyplay_flattened", events)


def test_person_lookup(id_season: str):
    """
    Lookup player by name and fetch related season/person metadata.
    """
    persons = api.get_persons(params={"nameFullLocalContains": "Zerbe"})
    print_result("persons", persons.get("data", []))

    person_id = persons.get("data", [{}])[0].get("personId")
    if not person_id:
        return

    person = api.get_person(person_id)
    print_result("person", person.get("data", {}))

    season_persons = api.get_season_persons(
        id_season, params={"include": "entities,organizations"}
    )
    print_result("season_persons", season_persons)

    person_seasons = api.get_person_seasons(person_id)
    print_result("person_seasons", person_seasons)


def test_entity_lookup(id_season: str):
    """
    Lookup team by name and inspect related metadata and season linkage.
    """
    params = {
        "nameFullLatinContains": "TBV Lemgo",
    }

    teams = api.get_teams(params)
    print_result("teams", teams)
    id_entity = teams.get("data", [{}])[0].get("entityId")
    if not id_entity:
        return

    team = api.get_team(
        id_entity, params={"include": "entities,organizations"}
    )
    print_result("team", team)

    team_seasons = api.get_team_seasons(id_entity)
    print_result("team_seasons", team_seasons)

    season_teams = api.get_season_teams(id_season)
    print_result("season_teams", season_teams)

    season_team = api.get_season_team(id_season, id_entity)
    print_result("season_team", season_team)


def test_static_resources():
    """
    Test retrieval of static reference data.
    """
    clubs = api.get_clubs()
    print_result("clubs", clubs.get("data", []))

    conferences = api.get_conferences()
    print_result("conferences", conferences.get("data", []))

    all_season_teams = api.get_all_season_teams()
    print_result("all_season_teams", all_season_teams.get("data", []))


# ---------------------- Main Test Flow ----------------------

if __name__ == "__main__":
    test_organizations()
    competition_id = test_leagues_and_competitions()
    assert competition_id, "No competition ID found"

    season_id = test_seasons(competition_id)
    assert season_id, "No season ID found"

    entity_id = test_season_entities(season_id)
    assert entity_id, "No entity ID found"

    test_season_fixtures(season_id, competition_id, entity_id)
    test_person_lookup(season_id)
    test_entity_lookup(season_id)
    test_static_resources()
