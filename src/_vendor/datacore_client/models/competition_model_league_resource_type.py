from enum import Enum


class CompetitionModelLeagueResourceType(str, Enum):
    LEAGUES = "leagues"

    def __str__(self) -> str:
        return str(self.value)
