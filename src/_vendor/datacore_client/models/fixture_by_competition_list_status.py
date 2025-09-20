from enum import Enum


class FixtureByCompetitionListStatus(str, Enum):
    ABANDONED = "ABANDONED"
    ABOUT_TO_START = "ABOUT_TO_START"
    BYE = "BYE"
    CANCELLED = "CANCELLED"
    CONFIRMED = "CONFIRMED"
    DRAFT = "DRAFT"
    FINISHED = "FINISHED"
    IF_NEEDED = "IF_NEEDED"
    IN_PROGRESS = "IN_PROGRESS"
    ON_PITCH = "ON_PITCH"
    PENDING = "PENDING"
    POSTPONED = "POSTPONED"
    SCHEDULED = "SCHEDULED"
    WARM_UP = "WARM_UP"

    def __str__(self) -> str:
        return str(self.value)
