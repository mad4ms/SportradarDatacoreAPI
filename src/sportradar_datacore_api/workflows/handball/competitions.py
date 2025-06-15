"""
Handball Data Processing Module

This module provides utilities for ingesting and processing handball data,
including functions to retrieve and filter competitions data from the HandballAPI.

Copyright (c) 2025 Michael Adams
Licensed under the MIT License.
"""

from typing import Optional
import pandas as pd
from sportradar_datacore_api.handball import HandballAPI


def list_competitions_df(
    api: HandballAPI,
    competition_name: Optional[str] = None,
    competition_id: Optional[str] = None,
) -> pd.DataFrame:
    """Retrieve all competitions, optionally filtered by name or ID."""
    params = {}
    if competition_name:
        params["nameLatinContains"] = competition_name
    if competition_id:
        params["competitionId"] = competition_id
    # add limit to 1000
    params["limit"] = 1000
    competitions = api.get_competitions(params=params)
    if not competitions.get("data"):
        raise ValueError(
            f"No competitions found for '{competition_name or competition_id}'"
        )
    return pd.DataFrame(competitions["data"])


def get_competition_id_by_name(api: HandballAPI, competition_name: str) -> str:
    """Get competitionId for a given competition name."""
    competitions = list_competitions_df(api, competition_name)
    if (
        competitions.empty
        or competition_name not in competitions["nameLocal"].values
    ):
        raise ValueError(f"Competition '{competition_name}' not found.")
    return competitions.loc[
        competitions["nameLocal"] == competition_name, "competitionId"
    ].values[0]
