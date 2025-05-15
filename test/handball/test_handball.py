import os
import json
from dotenv import load_dotenv
from sportradar_datacore_api.handball import HandballAPI


def print_result(title: str, data: dict | list):
    print(f"{title.upper()} {'*' * (70 - len(title))}")
    print(json.dumps(data, indent=2))
    print(f"END OF {title.upper()} {'*' * (70 - len(title))}")
    print()

    # Write the result to a file
    filename = f"{title.lower().replace(' ', '_')}.json"
    with open("log/" + filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


if __name__ == "__main__":
    load_dotenv(".env_prd", override=True)

    api = HandballAPI(
        base_url=os.getenv("BASE_URL", ""),
        auth_url=os.getenv("AUTH_URL", ""),
        client_id=os.getenv("CLIENT_ID", ""),
        client_secret=os.getenv("CLIENT_SECRET", ""),
        org_id=os.getenv("CLIENT_ORGANIZATION_ID"),
        scopes=["read:organization"],
        sport="handball",
    )

    # # Organizations
    # orgs = api.get_organizations()
    # print_result("organizations", orgs.get("data", []))

    # single_org = api.get_organization()
    # print_result("organization", single_org.get("data", {}))

    # # Leagues
    # leagues = api.get_leagues()
    # print_result("leagues", leagues.get("data", []))

    # # Competitions
    params = {"nameLatinContains": "Bundesliga"}
    comps = api.get_competitions(params)
    print_result("competitions", comps.get("data", []))
    comp_id = comps.get("data", [{}])[0].get("competitionId")
    # comp_id = "4c445e5c-3956-11ef-9d0e-b74f5c057367"
    assert comp_id == "4c445e5c-3956-11ef-9d0e-b74f5c057367"

    # exit()

    if comp_id:
        # comp = api.get_competition(comp_id)
        # print_result("competition", comp.get("data", {}))

        # # Seasons
        seasons = api.get_seasons(comp_id, params={"startDate": "2024-01-01"})
        print_result("seasons", seasons.get("data", []))
        season_id = seasons.get("data", [{}])[0].get("seasonId")
        assert season_id == "cabcf509-4373-11ef-a370-9d3c1e90234a"

        if season_id:

            season = api.get_season(season_id)
            print_result("season", season.get("data", {}))

            season_persons = api.get_season_persons(season_id)
            print_result("season_persons", season_persons.get("data", []))

            params_teams = {
                "external": "entityId,personId",
                "fields": "entity,organization,seasonId,status,added",
                "include": "entities,organizations",
                "limit": "10",
                "entityNameFullLocalContains": "TBV",
            }

            # strip out None values before calling:
            clean_params = {k: v for k, v in params_teams.items() if v is not None}

            season_teams = api.get_season_teams(season_id, params_teams)
            print_result("season_teams", season_teams)
            team_id = (
                season_teams.get("data", [{}])[0].get("entity").get("id").split(":")[-1]
            )
            print("TeamID: " + team_id)
            if team_id:
                params = {
                    # "external": "entityId,personId",
                    # projects only these fields on the season‐team link
                    # "fields":   "entity,organization,seasonId,status,added",
                    # plural resource‐type names per the docs
                    "include":  "entities,organizations,persons",
                    # "hideNull": "false",
                }

                # this path expects only the raw UUID
                season_team = api.get_season_team(season_id, team_id, params)

                # link object (minimal pointers + link‐fields)
                print_result("season_team",     season_team)

                season_fixtures = api.get_season_fixtures(season_id, params)
                print_result("season_fixtures",     season_fixtures)
                # exit()
                # full entity + org records, if any, under "included"
                # print_result("season_team (included)", season_team.get("included"))

            # exit()

    # Persons
    # persons = api.get_persons()
    # print_result("persons", persons.get("data", []))
    # person_id = persons.get("data", [{}])[0].get("personId")
    # if person_id:
    #     person = api.get_person(person_id)
    #     print_result("person", person.get("data", {}))

    #     person_seasons = api.get_person_seasons(person_id)
    #     print_result("person_seasons", person_seasons.get("data", []))

    #     if season_id:
    #         season_person = api.get_season_person(season_id, person_id)
    #         print_result("season_person", season_person.get("data", {}))

    # Teams
    params = {
                    # "external": "entityId,personId",
                    # projects only these fields on the season‐team link
                    # "fields":   "entity,organization,seasonId,status,added",
                    # plural resource‐type names per the docs
                    "nameFullLatinContains":  "TBV Lemgo",
                    # "hideNull": "false",
                }
    teams = api.get_teams(params)
    print_result("teams", teams)
    team_id = teams.get("data", [{}])[0].get("entityId")
    if team_id:
        team = api.get_team(team_id)
        print_result("team", team.get("data", {}))

        team_seasons = api.get_team_seasons(team_id, params)
        print_result("team_seasons", team_seasons.get("data", []))
    exit()
    # Clubs

    clubs = api.get_clubs()
    print_result("clubs", clubs.get("data", []))
    club_id = clubs.get("data", [{}])[0].get("entityGroupId")
    if club_id:
        club = api.get_club(club_id)
        print_result("club", club.get("data", {}))

    # Conferences
    conferences = api.get_conferences()
    print_result("conferences", conferences.get("data", []))

    # All season teams
    all_season_teams = api.get_all_season_teams()
    print_result("all_season_teams", all_season_teams.get("data", []))
