"""Initialization file for the sportradar_datacore_api package.

Author: Michael Adams, 2025
"""

from .handball import HandballAPI
from .workflows.handball.competitions import (
    list_competitions_df,
    get_competition_id_by_name,
)
from .workflows.handball.seasons import list_seasons_df, get_season_id_by_name
from .workflows.handball.games import (
    list_season_fixtures_df,
    fetch_fixture_events_df,
)

__all__ = [
    "HandballAPI",
    "list_competitions_df",  # from competitions.py
    "get_competition_id_by_name",
    "list_seasons_df",
    "get_season_id_by_name",
    "list_season_fixtures_df",
    "fetch_fixture_events_df",
]
