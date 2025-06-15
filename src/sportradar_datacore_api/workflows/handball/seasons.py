"""
Seasons workflows for Handball.

Provides functions to list seasons and look up a season's UUID by name.
"""

import pandas as pd
from sportradar_datacore_api.handball import HandballAPI


def list_seasons_df(api: HandballAPI, competition_id: str) -> pd.DataFrame:
    """
    Return all seasons for the given competition as a DataFrame.

    Raises:
        ValueError: if competition_id is missing or no data is returned.
    """
    if not competition_id:
        raise ValueError("competition_id must be provided.")
    resp = api.get_seasons(
        competition_id=competition_id, params={"limit": 1000}
    )
    data = resp.get("data") or []
    if not data:
        raise ValueError(
            f"No seasons found for competition '{competition_id}'."
        )
    return pd.DataFrame(data)


def get_season_id_by_name(
    api: HandballAPI, competition_id: str, season_name: str
) -> str:
    """
    Lookup and return the UUID of a season by its local name.

    Raises:
        ValueError: if the season_name is not found.
    """
    df = list_seasons_df(api, competition_id)
    matches = df[df["nameLocal"] == season_name]
    if matches.empty:
        raise ValueError(
            f"Season '{season_name}' not found under competition '{competition_id}'."
        )
    return matches["seasonId"].iat[0]
