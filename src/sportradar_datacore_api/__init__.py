"""Initialization file for the sportradar_datacore_api package.

Author: Michael Adams, 2025
"""

from sportradar_datacore_api.config import DataCoreSettings
from sportradar_datacore_api.handball import HandballAPI
from sportradar_datacore_api.stream_models import (
    StreamAccessGrant,
    StreamMessage,
    StreamPublishResult,
    StreamTopicGrant,
)
from sportradar_datacore_api.streaming import HandballStreamClient, HandballStreamingAPI

__all__ = [
    "DataCoreSettings",
    "HandballAPI",
    "HandballStreamClient",
    "HandballStreamingAPI",
    "StreamAccessGrant",
    "StreamMessage",
    "StreamPublishResult",
    "StreamTopicGrant",
]
