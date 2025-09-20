from enum import Enum


class VideoFilePostBodyStatusType3Type1(str, Enum):
    AVAILABLE = "AVAILABLE"
    BUILDABLE = "BUILDABLE"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
