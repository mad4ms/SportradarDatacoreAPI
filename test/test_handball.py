"""Handball API Pytest Script
This script tests various endpoints of the Sportradar DataCore API for handball.
Author: Michael Adams, 2025
"""

import os
import json
from pathlib import Path
import pytest
from dotenv import load_dotenv
from sportradar_datacore_api import HandballAPI

# ---------------------- Configuration ----------------------


@pytest.fixture(scope="module")
def api():
    """Fixture to initialize the HandballAPI client."""
    load_dotenv(".env_prd", override=True)
    return HandballAPI(
        base_url=os.getenv("BASE_URL", ""),
        auth_url=os.getenv("AUTH_URL", ""),
        client_id=os.getenv("CLIENT_ID", ""),
        client_secret=os.getenv("CLIENT_SECRET", ""),
        org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
        scopes=["read:organization"],
        sport="handball",
    )


@pytest.fixture(scope="module")
def log_dir():
    """Fixture to create a log directory for test outputs."""
    path = Path("log")
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_result(log_dir, title: str, data: dict | list):
    """Utility to save test results to JSON files."""
    path = log_dir / f"{title.lower().replace(' ', '_')}.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


# ---------------------- Test Functions ----------------------


def test_organizations(api, log_dir):
    """Test retrieval of all organizations."""
    orgs = api.get_organizations()
    assert orgs.get("data"), "No organizations found"
    save_result(log_dir, "organizations", orgs.get("data", []))


def test_competitions(api, log_dir):
    """Test retrieval of competitions containing 'Bundesliga'."""
    comps = api.get_competitions(params={"nameLatinContains": "Bundesliga"})
    assert comps.get("data"), "No competitions found"
    save_result(log_dir, "competitions", comps.get("data", []))

    competition_id = comps.get("data", [{}])[0].get("competitionId")
    assert competition_id, f"Expected competition ID, but got {competition_id}"
    # return competition_id


def test_seasons(api, log_dir, competition_id):
    """Retrieve seasons for a given competition."""
    seasons = api.get_seasons(
        competition_id, params={"startDate": "2024-01-01"}
    )
    assert seasons.get("data"), "No seasons found"
    save_result(log_dir, "seasons", seasons.get("data", []))

    season_id = seasons.get("data", [{}])[0].get("seasonId")
    assert season_id, "No season ID found"
    return season_id


def test_season_entities(api, log_dir, season_id):
    """Filter teams in a season by name."""
    params = {
        "external": "entityId,personId",
        "fields": "entity,organization,seasonId,status,added",
        "include": "entities,organizations",
        "limit": "10",
        "entityNameFullLocalContains": "TBV",
    }

    teams = api.get_season_teams(season_id, params)
    assert teams.get("data"), "No teams found"
    save_result(log_dir, "season_teams", teams)

    team_data = teams.get("data", [{}])[0].get("entity")
    team_id = team_data.get("id").split(":")[-1] if team_data else None
    assert team_id, "No team ID found"
    return team_id


def test_season_fixtures(api, log_dir, season_id, competition_id, team_id):
    """Query fixtures by season, competition, and team."""
    params = {
        "include": "entities,organizations,persons",
        "external": "entityId,personId",
    }

    season_fixtures = api.get_season_fixtures(season_id, params)
    assert season_fixtures.get("data"), "No season fixtures found"
    save_result(log_dir, "season_fixtures", season_fixtures)

    competition_fixtures = api.get_competition_fixtures(competition_id, params)
    assert competition_fixtures.get("data"), "No competition fixtures found"
    save_result(log_dir, "competition_fixtures", competition_fixtures)

    season_team_fixtures = api.get_season_team_fixtures(
        season_id, team_id, params={}
    )
    assert season_team_fixtures.get("data"), "No season team fixtures found"
    save_result(log_dir, "season_team_fixtures", season_team_fixtures)

    fixture_id = season_fixtures.get("data", [{}])[0].get("fixtureId")
    assert fixture_id, "No fixture ID found"

    fixture = api.get_fixture(fixture_id, params)
    assert fixture.get("data"), "No fixture data found"
    save_result(log_dir, "fixture", fixture)

    playbyplay = api.get_playbyplay(fixture_id, params)
    assert playbyplay.get("data"), "No play-by-play data found"
    save_result(log_dir, "playbyplay", playbyplay)


def test_static_resources(api, log_dir):
    """Test retrieval of static reference data."""
    clubs = api.get_clubs()
    assert clubs.get("data"), "No clubs found"
    save_result(log_dir, "clubs", clubs.get("data", []))

    conferences = api.get_conferences()
    assert conferences.get("data"), "No conferences found"
    save_result(log_dir, "conferences", conferences.get("data", []))

    all_season_teams = api.get_all_season_teams()
    assert all_season_teams.get("data"), "No season teams found"
    save_result(log_dir, "all_season_teams", all_season_teams.get("data", []))


# ---------------------- Main Test Flow ----------------------


@pytest.mark.run(order=1)
def test_full_flow(api, log_dir):
    """Run the full test flow."""
    test_organizations(api, log_dir)
    test_competitions(api, log_dir)
    competition_id = "4c445e5c-3956-11ef-9d0e-b74f5c057367"
    season_id = test_seasons(api, log_dir, competition_id)
    team_id = test_season_entities(api, log_dir, season_id)
    test_season_fixtures(api, log_dir, season_id, competition_id, team_id)
    test_static_resources(api, log_dir)
