from enum import Enum


class VideoStreamInputsModelVenueResourceType(str, Enum):
    VENUES = "venues"

    def __str__(self) -> str:
        return str(self.value)
