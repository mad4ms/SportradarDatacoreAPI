from enum import Enum


class ImagesForFixtureListRating(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
