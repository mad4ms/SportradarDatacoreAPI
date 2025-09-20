from enum import Enum


class CompetitionSeasonStatusModelLeagueResourceType(str, Enum):
    LEAGUES = "leagues"

    def __str__(self) -> str:
        return str(self.value)
