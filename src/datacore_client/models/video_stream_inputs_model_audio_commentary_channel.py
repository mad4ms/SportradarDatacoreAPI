from enum import Enum


class VideoStreamInputsModelAudioCommentaryChannel(str, Enum):
    CHANNEL_BOTH = "CHANNEL_BOTH"
    CHANNEL_LEFT = "CHANNEL_LEFT"
    CHANNEL_RIGHT = "CHANNEL_RIGHT"
    NONE = "NONE"

    def __str__(self) -> str:
        return str(self.value)
