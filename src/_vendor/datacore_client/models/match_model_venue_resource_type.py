from enum import Enum


class MatchModelVenueResourceType(str, Enum):
    VENUES = "venues"

    def __str__(self) -> str:
        return str(self.value)
