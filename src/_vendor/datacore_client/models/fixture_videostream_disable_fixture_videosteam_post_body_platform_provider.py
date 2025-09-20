from enum import Enum


class FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider(str, Enum):
    AV_SPORTRADAR = "AV_SPORTRADAR"
    VALUE_0 = "5STREAM"

    def __str__(self) -> str:
        return str(self.value)
