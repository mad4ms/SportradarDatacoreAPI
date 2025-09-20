from enum import Enum


class VideoFileInsertVideoFilePostBodyOriginType1(str, Enum):
    STREAM = "STREAM"
    UPLOAD = "UPLOAD"
    VENUE = "VENUE"

    def __str__(self) -> str:
        return str(self.value)
