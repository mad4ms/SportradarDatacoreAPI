from enum import Enum


class VideoSubscriptionModelAudio(str, Enum):
    AMBIENCE = "AMBIENCE"
    BOTH = "BOTH"
    BOTH_SPLIT_LR = "BOTH_SPLIT_LR"
    COMMENTARY = "COMMENTARY"

    def __str__(self) -> str:
        return str(self.value)
