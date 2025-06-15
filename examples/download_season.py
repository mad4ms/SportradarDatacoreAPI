"""
Download and export play-by-play + event data for every fixture
in a given handball season.
"""

import os
import argparse
import pandas as pd
from dotenv import load_dotenv


from sportradar_datacore_api import HandballAPI
from sportradar_datacore_api.workflows.handball.competitions import (
    # list_competitions_df,
    get_competition_id_by_name,
)
from sportradar_datacore_api.workflows.handball.seasons import (
    list_seasons_df,
    get_season_id_by_name,
)
from sportradar_datacore_api.workflows.handball.games import (
    list_season_fixtures_df,
    fetch_fixture_events_df,
)

# TODO: put in config or something
columns_to_keep = [
    # "clientId",
    # "clientType",
    "fixtureId",
    "organizationId",
    # "received",
    # "sport",
    # "topic",
    "type",
    "data.class",
    "data.eventId",
    "data.eventTime",
    "data.eventType",
    # "data.options.attendance",
    # "data.options.numberOfPeriods",
    # "data.options.periodLength",
    # "data.status",
    "data.subType",
    "data.timestamp",
    "data.entityId",
    # "data.options.active",
    "data.options.bib",
    # "data.options.captain",
    # "data.options.name",
    "data.options.position",
    "data.options.starter",
    # "data.personId",
    # "data.options.number",
    "data.periodId",
    "data.sequence",
    "score_home",
    "score_away",
    "data.playId",
    "data.clock",
    "data.options.goalKeeperId",
    "data.options.location",
    "data.success",
    "data.x",
    "data.y",
    "data.options.failureReason",
    "data.options.attackType",
    "data.options.value",
    "data.options.emptyNet",
    # "team.added",
    # "team.ageGroup",
    # "team.alternateVenueIds",
    # "team.codeLatin",
    "team.codeLocal",
    # "team.defaultVenueId",
    # "team.discipline",
    # "team.entityGroupId",
    "team.entityId",
    "team.externalId",
    # "team.gender",
    # "team.grade",
    # "team.historicalNames",
    # "team.internationalReference",
    # "team.nameFullLatin",
    "team.nameFullLocal",
    # "team.organizationId",
    # "team.representing",
    # "team.standard",
    # "team.status",
    # "team.updated",
    # "team.additionalNames.namePlaceLatin",
    # "team.additionalNames.namePlaceLocal",
    # "team.additionalNames.nameShortLatin",
    # "team.additionalNames.nameShortLocal",
    "team.colors.primary",
    "team.colors.secondary",
    "team.colors.tertiary",
    # "team.contacts.email",
    # "team.contacts.fax",
    # "team.contacts.phone",
    # "team.entityGroup.id",
    # "team.entityGroup.resourceType",
    # "team.organization.id",
    # "team.organization.resourceType",
    # "player.added",
    # "player.deceased",
    "player.dob",
    "player.externalId",
    "player.gender",
    # "player.historicalNames",
    # "player.languageLocal",
    # "player.nameAbbreviated",
    # "player.nameFamilyLatin",
    "player.nameFamilyLocal",
    # "player.nameFullLatin",
    # "player.nameFullLocal",
    # "player.nameGivenLatin",
    "player.nameGivenLocal",
    "player.nationality",
    # "player.organizationId",
    "player.personId",
    # "player.representing",
    # "player.status",
    # "player.updated",
    "player.additionalDetails.height",
    "player.additionalDetails.weight",
    # "player.organization.id",
    # "player.organization.resourceType",
    "team_home_abbr",
    "team_away_abbr",
    "team_home_id",
    "team_away_id",
    "team_home_name",
    "team_away_name",
    "gameday",
    "team_attacking_id",
    "team_attacking_name",
    "team_attacking_side",
]


def initialize_api() -> HandballAPI:
    """Load .env credentials and return an authenticated client."""
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


def main():
    """Main function to download and export fixtures for a handball season."""
    parser = argparse.ArgumentParser(
        description="Download and export all fixtures for a handball season."
    )
    parser.add_argument(
        "--competition",
        required=True,
        help="Competition name (e.g. '1. Handball-Bundesliga')",
    )
    parser.add_argument(
        "--season",
        required=True,
        help="Season name (e.g. 'DAIKIN HBL 2024/25')",
    )
    parser.add_argument(
        "--out-dir",
        default="data",
        help="Directory to save CSV files under (default: data/)",
    )
    args = parser.parse_args()

    api = initialize_api()

    # 1) Identify competition & season UUIDs
    comp_id = get_competition_id_by_name(api, args.competition)
    print(f"→ Competition '{args.competition}' → {comp_id}")

    season_df = list_seasons_df(api, comp_id)
    print("Available seasons:")
    print(season_df[["seasonId", "nameLocal"]])

    season_id = get_season_id_by_name(api, comp_id, args.season)
    print(f"→ Season '{args.season}' → {season_id}")

    # 2) List fixtures
    fixtures_df = list_season_fixtures_df(api, season_id)
    print(f"Found {len(fixtures_df)} fixtures.")
    print(fixtures_df[["fixtureId", "nameLocal", "startTimeLocal"]])

    # 3) Download & export each fixture’s events
    for _, row in fixtures_df.iterrows():
        fid = row["fixtureId"]
        print(f"\nDownloading events for fixture {fid} ...")
        events_df = fetch_fixture_events_df(api, fixture_id=fid, debug=True)
        gameday = row.get("roundNumber", "")
        events_df["gameday"] = gameday

        events_df = events_df[columns_to_keep].copy()

        # write schema based on events_df columns

        date_str = pd.to_datetime(row["startTimeLocal"]).strftime("%Y-%m-%d")
        out_path = os.path.join(
            args.out_dir, f"{date_str}_gd-{gameday}_id-{fid}.csv"
        )

        # create path if it does not exist
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        events_df.to_csv(out_path, index=False, encoding="utf-8-sig")
        print(f"Saved to {os.path.abspath(out_path)}")

    print("\nAll fixtures processed.")


if __name__ == "__main__":
    main()

# python .\examples\download_season.py \
# --competition "1. Handball-Bundesliga" \
# --season "DAIKIN HBL 2024/25" \
# --out-dir "../data"
