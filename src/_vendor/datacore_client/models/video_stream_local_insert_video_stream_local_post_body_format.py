from enum import Enum


class VideoStreamLocalInsertVideoStreamLocalPostBodyFormat(str, Enum):
    HLS = "HLS"
    MP4 = "MP4"

    def __str__(self) -> str:
        return str(self.value)
