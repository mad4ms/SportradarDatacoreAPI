from enum import Enum


class VideoSubscriptionsUpdateVideoSubscriptionPutBodyFeedType(str, Enum):
    ADDITIONAL_ANGLE = "ADDITIONAL_ANGLE"
    LOW_LATENCY = "LOW_LATENCY"
    PRIMARY = "PRIMARY"

    def __str__(self) -> str:
        return str(self.value)
