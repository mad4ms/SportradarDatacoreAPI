"""Handball API Pytest Script (for new API)
Tests various endpoints of the Sportradar DataCore API for handball.
Author: Michael Adams, 2025
"""

import json
import os
from pathlib import Path

import pytest
from dotenv import load_dotenv
from sportradar_datacore_api.handball import HandballAPI


@pytest.fixture(scope="module")
def api():
    """Fixture to initialize the HandballAPI client."""
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


@pytest.fixture(scope="module")
def log_dir():
    """Fixture to create a log directory for test outputs."""
    path = Path("log")
    path.mkdir(parents=True, exist_ok=True)
    return path


def save_result(log_dir, title: str, data) -> None:
    """Utility to save test results to JSON files."""
    if os.getenv("SRD_SKIP_TEST_LOGS") == "1":
        return None
    path = log_dir / f"{title.lower().replace(' ', '_')}.json"
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    return None


def _first_fixture_id(fixtures):
    for fixture in fixtures:
        if isinstance(fixture, dict):
            fixture_id = fixture.get("fixture_id") or fixture.get("fixtureId")
        else:
            fixture_id = getattr(fixture, "fixture_id", None)
        if fixture_id:
            return fixture_id
    return None


def test_competition_id(api, log_dir):
    """Test resolving competition ID by name."""
    comp_id = api.get_competition_id_by_name("1. Handball-Bundesliga")
    assert comp_id, "No competition ID found"
    save_result(log_dir, "competition_id", {"competition_id": comp_id})


def test_season_id(api, log_dir):
    """Test resolving season ID by year."""
    comp_id = api.get_competition_id_by_name("1. Handball-Bundesliga")
    season_id = api.get_season_id_by_year(comp_id, 2023)
    assert season_id, "No season ID found"
    save_result(log_dir, "season_id", {"season_id": season_id})


def test_list_fixtures(api, log_dir):
    """Test listing fixtures for a season."""
    comp_id = api.get_competition_id_by_name("1. Handball-Bundesliga")
    season_id = api.get_season_id_by_year(comp_id, 2023)
    fixtures = api.get_list_matches_by_season_id(season_id)
    assert fixtures, "No fixtures found"
    # Convert objects to dicts for JSON serialization
    fixtures_dict = [f.__dict__ if hasattr(f, "__dict__") else f for f in fixtures]
    save_result(log_dir, "fixtures", fixtures_dict)


def test_fixture_events(api, log_dir):
    """Test getting events for a fixture."""
    comp_id = api.get_competition_id_by_name("1. Handball-Bundesliga")
    season_id = api.get_season_id_by_year(comp_id, 2023)
    fixtures = api.get_list_matches_by_season_id(season_id)
    assert fixtures, "No fixtures found"
    fixture_id = _first_fixture_id(fixtures)
    assert fixture_id, "No fixture ID found"
    events = api.get_fixture_events_by_id(
        fixture_id, setup_only=False, with_scores=True
    )
    assert events is not None, "No events found"
    save_result(log_dir, "fixture_events", events)
    if os.getenv("SRD_SKIP_TEST_LOGS") != "1":
        # Optionally test CSV export
        csv_path = log_dir / f"fixture_{fixture_id}_events.csv"
        api.save_events_to_csv(events, str(csv_path))


def test_full_flow(api, log_dir):
    """Run the full test flow."""
    comp_id = api.get_competition_id_by_name("1. Handball-Bundesliga")
    assert comp_id, "No competition ID found"
    season_id = api.get_season_id_by_year(comp_id, 2023)
    assert season_id, "No season ID found"
    fixtures = api.get_list_matches_by_season_id(season_id)
    assert fixtures, "No fixtures found"
    fixture_id = _first_fixture_id(fixtures)
    assert fixture_id, "No fixture ID found"
    events = api.get_fixture_events_by_id(
        fixture_id, setup_only=False, with_scores=True
    )
    assert events is not None, "No events found"
    if os.getenv("SRD_SKIP_TEST_LOGS") != "1":
        csv_path = log_dir / f"fixture_{fixture_id}_events.csv"
        api.save_events_to_csv(events, str(csv_path))


if __name__ == "__main__":
    pytest.main(["-v", __file__])
