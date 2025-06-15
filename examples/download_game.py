import os
import argparse
import pandas as pd
from dotenv import load_dotenv
from sportradar_datacore_api import HandballAPI


def initialize_api() -> HandballAPI:
    """
    Load credentials from .env and instantiate HandballAPI client.
    """
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


def flatten_events(events: list) -> pd.DataFrame:
    """
    Flatten the nested event structure from the play-by-play export.
    """
    records = []
    for evt in events:
        base = {k: v for k, v in evt.items() if k not in ("data", "scores")}
        base.update({f"data.{k}": v for k, v in evt.get("data", {}).items()})
        base.update(
            {
                f"data.options.{k}": v
                for k, v in evt.get("data", {}).get("options", {}).items()
            }
        )
        base["raw_scores"] = evt.get("scores", {})
        records.append(base)
    return pd.DataFrame(records)


def enrich_dataframe(
    df: pd.DataFrame, df_entities: pd.DataFrame, df_persons: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge entity and person data into the main event dataframe.
    """
    if not df_entities.empty:
        df = df.merge(
            df_entities[["entityId", "nameFullLocal", "abbreviation"]],
            left_on="data.entityId",
            right_on="entityId",
            how="left",
        )
    if not df_persons.empty:
        df = df.merge(
            df_persons[["personId", "nameFullLocal"]],
            left_on="data.personId",
            right_on="personId",
            how="left",
            suffixes=("_entity", "_person"),
        )

    return df


def normalize_entity_id(eid):
    """
    Strip any prefix from an entityId (e.g., 'h1s44:xxxx' -> 'xxxx').
    """
    if isinstance(eid, str) and ":" in eid:
        return eid.split(":", 1)[1]
    return eid


def extract_team_metadata(
    df_fixture: pd.DataFrame, df_entities: pd.DataFrame
) -> dict:
    """
    Identify home/away teams and extract key metadata. Handles entityId prefixes.
    """
    competitors = df_fixture.at[0, "competitors"]
    home_team = next(c for c in competitors if c.get("isHome"))
    away_team = next(c for c in competitors if not c.get("isHome"))

    # Add a normalized column for matching
    df_entities = df_entities.copy()
    df_entities["entityIdNorm"] = df_entities["entityId"].apply(
        normalize_entity_id
    )

    def entity_value(eid: str, col: str) -> str:
        eid_norm = normalize_entity_id(eid)
        mask = df_entities["entityIdNorm"] == eid_norm
        if not mask.any():
            raise ValueError(
                f"Entity '{eid_norm}' not found in df_entities for column '{col}'. "
                f"Available normalized entityIds: {df_entities['entityIdNorm'].tolist()}"
            )
        value = df_entities.loc[mask, col]
        if value.empty:
            raise ValueError(
                f"Column '{col}' missing for entity '{eid_norm}'."
            )
        return value.iloc[0]

    return {
        "home_id": str(home_team["entityId"]),
        "away_id": str(away_team["entityId"]),
        "home_name": entity_value(home_team["entityId"], "nameFullLocal"),
        "away_name": entity_value(away_team["entityId"], "nameFullLocal"),
        "home_abbr": entity_value(home_team["entityId"], "abbreviation"),
        "away_abbr": entity_value(away_team["entityId"], "abbreviation"),
    }


def process_scores(
    df: pd.DataFrame, home_id: str, away_id: str
) -> pd.DataFrame:
    """
    Add home/away scores and classify attacking side per event.
    """
    df["score_home"] = df["raw_scores"].apply(
        lambda s: s.get(home_id) if isinstance(s, dict) else None
    )
    df["score_away"] = df["raw_scores"].apply(
        lambda s: s.get(away_id) if isinstance(s, dict) else None
    )
    df["attacking_side"] = df["data.entityId"].apply(
        lambda eid: (
            "home"
            if eid == home_id
            else ("away" if eid == away_id else "unknown")
        )
    )
    return df


def format_output_filename(
    date: str, gameday: int, fixture_id: str, home_abbr: str, away_abbr: str
) -> str:
    """
    Generate standardized output filename.
    """
    abbr = f"{home_abbr}_{away_abbr}".replace("-", "_")
    return f"{date}_gameday_{gameday:02}_id_{fixture_id}_{abbr}.csv"


def download_fixture_events(fixture_id: str, out_dir: str = "../data") -> None:
    """
    Main execution pipeline for downloading and exporting game data for a single fixture.
    """
    api = initialize_api()

    # --- Fetch core fixture info and included resources
    fixture = api.get_fixture(
        fixture_id,
        params={
            "include": "entities,organizations,persons",
            "external": "entityId,personId",
        },
    )
    df_fixture = pd.json_normalize(fixture["data"], sep="_")
    includes = fixture.get("includes", {}).get("resources", {})
    df_entities = pd.DataFrame.from_dict(
        includes.get("entities", {}), orient="index"
    )
    if not df_entities.empty:
        df_entities["entityId"] = df_entities.index
        df_entities["abbreviation"] = df_entities["codeLocal"]

    # --- Retrieve play-by-play export and raw play-by-play for full enrichment
    playbyplay_export = api.get_match_events_export(
        fixture_id,
        params={
            "include": "entities,organizations,persons,fixtures,competitions,seasons",
            "external": "entityId,personId",
            "withScores": "true",
        },
    )
    playbyplay = api.get_playbyplay(
        fixture_id,
        params={
            "include": "entities,organizations,persons,fixtures,competitions,seasons",
            "external": "entityId,personId",
        },
    )
    events = playbyplay_export.get("data", [{}])
    df = flatten_events(events)

    # --- Retrieve person metadata (if available)
    persons = (
        playbyplay.get("includes", {}).get("resources", {}).get("persons", {})
    )
    df_persons = pd.DataFrame.from_dict(persons, orient="index")
    if not df_persons.empty:
        df_persons["personId"] = df_persons.index

    # --- Merge and enrich main dataframe
    df = enrich_dataframe(df, df_entities, df_persons)
    meta = extract_team_metadata(df_fixture, df_entities)
    for key, value in {
        "team_home_abbr": meta["home_abbr"],
        "team_away_abbr": meta["away_abbr"],
        "team_home_id": meta["home_id"],
        "team_home_name": meta["home_name"],
        "team_away_id": meta["away_id"],
        "team_away_name": meta["away_name"],
    }.items():
        df[key] = value
    df["team_attacking_id"] = df["data.entityId"]
    df["team_attacking_name"] = df["team_name"]

    df = process_scores(df, meta["home_id"], meta["away_id"])

    # --- Construct output file path and persist result
    fixture_date = df_fixture.at[0, "startTimeLocal"].split("T")[0]
    gameday = int(df_fixture.at[0, "roundNumber"])
    filename = format_output_filename(
        fixture_date, gameday, fixture_id, meta["home_abbr"], meta["away_abbr"]
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)
    df.to_csv(path, index=False)
    print(f"Fixture data saved to {path}")


def main():
    parser = argparse.ArgumentParser(
        description="Download and export enriched handball fixture data by fixture_id."
    )
    parser.add_argument("fixture_id", type=str, help="Fixture ID")
    parser.add_argument(
        "--out-dir",
        type=str,
        default="../data",
        help="Output directory for exported CSV",
    )
    args = parser.parse_args()
    download_fixture_events(args.fixture_id, args.out_dir)


if __name__ == "__main__":
    main()
