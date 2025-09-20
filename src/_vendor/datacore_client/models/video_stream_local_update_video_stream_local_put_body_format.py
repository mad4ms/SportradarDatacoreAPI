from enum import Enum


class VideoStreamLocalUpdateVideoStreamLocalPutBodyFormat(str, Enum):
    HLS = "HLS"
    MP4 = "MP4"

    def __str__(self) -> str:
        return str(self.value)
