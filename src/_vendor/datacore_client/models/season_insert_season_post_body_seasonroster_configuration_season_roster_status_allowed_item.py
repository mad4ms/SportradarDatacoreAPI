from enum import Enum


class SeasonInsertSeasonPostBodySEASONROSTERConfigurationSeasonRosterStatusAllowedItem(
    str, Enum
):
    ACTIVE = "ACTIVE"
    INJURED = "INJURED"
    OTHER_NOT_PARTICIPATING = "OTHER_NOT_PARTICIPATING"
    OUT = "OUT"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
