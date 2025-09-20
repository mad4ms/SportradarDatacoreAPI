from enum import Enum


class VideoFileInsertVideoFilePostBodyOriginType3Type1(str, Enum):
    STREAM = "STREAM"
    UPLOAD = "UPLOAD"
    VENUE = "VENUE"

    def __str__(self) -> str:
        return str(self.value)
