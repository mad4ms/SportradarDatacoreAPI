from enum import Enum


class FixtureInsertBaseRouteMatchPostBodyMatchCompetitorResultStatus(str, Enum):
    CONFIRMED = "CONFIRMED"
    DID_NOT_FINISH = "DID_NOT_FINISH"
    DID_NOT_START = "DID_NOT_START"
    DISQUALIFIED = "DISQUALIFIED"
    FORFEITED = "FORFEITED"
    IN_PROGRESS = "IN_PROGRESS"
    SCHEDULED = "SCHEDULED"
    WITHDRAWN = "WITHDRAWN"
    WON_BY_FORFEIT = "WON_BY_FORFEIT"

    def __str__(self) -> str:
        return str(self.value)
