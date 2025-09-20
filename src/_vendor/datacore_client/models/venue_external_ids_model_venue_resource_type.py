from enum import Enum


class VenueExternalIdsModelVenueResourceType(str, Enum):
    VENUES = "venues"

    def __str__(self) -> str:
        return str(self.value)
