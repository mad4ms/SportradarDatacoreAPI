from enum import Enum


class VideoStreamOutputsModelVenueResourceType(str, Enum):
    VENUES = "venues"

    def __str__(self) -> str:
        return str(self.value)
