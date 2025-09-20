from enum import Enum


class ImagesListSecondaryRating(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    UNKNOWN = "UNKNOWN"

    def __str__(self) -> str:
        return str(self.value)
