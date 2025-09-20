from enum import Enum


class VideoFileInsertVideoFilePostBodyStorageProviderType1(str, Enum):
    AV_SPORTRADAR = "AV_SPORTRADAR"
    KEEMOTION = "KEEMOTION"
    SYNERGY = "SYNERGY"
    VALUE_0 = "5STREAM"

    def __str__(self) -> str:
        return str(self.value)
