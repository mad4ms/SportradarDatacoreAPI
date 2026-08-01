from enum import Enum


class AwardsListFixturesAward(str, Enum):
    ALL_TEAM = "ALL_TEAM"
    COACH = "COACH"
    DEFENSIVE = "DEFENSIVE"
    DEFENSIVE_TEAM = "DEFENSIVE_TEAM"
    HALL = "HALL"
    HONOUR = "HONOUR"
    MIP = "MIP"
    MVP = "MVP"
    OTHER = "OTHER"
    ROOKIE = "ROOKIE"
    VALUE_7 = "6th_MAN"

    def __str__(self) -> str:
        return str(self.value)
