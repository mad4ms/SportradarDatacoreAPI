from enum import Enum


class VideoSubscriptionInsertVideoSubscriptionPostBodyOutputFormat(str, Enum):
    HLS = "HLS"
    RTMP = "RTMP"
    RTMP_PULL = "RTMP_PULL"
    SRT = "SRT"

    def __str__(self) -> str:
        return str(self.value)
