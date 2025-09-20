from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.video_subscription_insert_video_subscription_post_body_audio import (
    VideoSubscriptionInsertVideoSubscriptionPostBodyAudio,
)
from ..models.video_subscription_insert_video_subscription_post_body_content import (
    VideoSubscriptionInsertVideoSubscriptionPostBodyContent,
)
from ..models.video_subscription_insert_video_subscription_post_body_feed_type import (
    VideoSubscriptionInsertVideoSubscriptionPostBodyFeedType,
)
from ..models.video_subscription_insert_video_subscription_post_body_output_format import (
    VideoSubscriptionInsertVideoSubscriptionPostBodyOutputFormat,
)
from ..models.video_subscription_insert_video_subscription_post_body_output_resolution import (
    VideoSubscriptionInsertVideoSubscriptionPostBodyOutputResolution,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoSubscriptionInsertVideoSubscriptionPostBody")


@_attrs_define
class VideoSubscriptionInsertVideoSubscriptionPostBody:
    """
    Attributes:
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        provider (str): The code for the provider of the file Example: Test Provider.
        locale (str): The locale of the video Example: fr-FR.
        source_number (int): Unique identifier for the video source. This is unique for the provider/fixtureId/locale
            combination.  Unless the provider is supplying multiple sources per fixture/locale then this is normally 1.
            Default: 1. Example: 1.
        feed_type (VideoSubscriptionInsertVideoSubscriptionPostBodyFeedType): Type of video input
            >- `ADDITIONAL_ANGLE` Additional angle
            >- `LOW_LATENCY` Low Latency
            >- `PRIMARY` Primary
             Example: PRIMARY.
        output_resolution (VideoSubscriptionInsertVideoSubscriptionPostBodyOutputResolution): The resolution that you
            want to receive the video in.  This is only valid if outputFormat is `RTMP`.  If outputFormat is not `RTMP` then
            the output resolution is the same as the input resolution.  If specified the output resolution cannot be higher
            than the input resolution. You must have specific permission to chose anything other than 720p or 1080p.
            >- `1080` 1920 x 1080
            >- `1080i50@10M` SRT 1080i50@10M
            >- `1080p25@10M` SRT 1080p25@10M
            >- `1080p50@10M` SRT 1080p50@10M
            >- `1280x720@2000k` 1280x720@2000k
            >- `1280x720@3000k` 1280x720@3000k
            >- `1280x720@3000k25fps` 1280x720@3000k25fps
            >- `1920x1080@4000k` 1920x1080@4000k
            >- `1920x1080@4000k25fps` 1920x1080@4000k25fps
            >- `1920x1080@4500k` 1920x1080@4500k
            >- `1920x1080@5000k30fps` 1920x1080@5000k30fps
            >- `2000` 2000
            >- `288` 512 x 288
            >- `640x320@850k` 640x320@850k
            >- `720` 1280 x 720
            >- `DESKTOP_384x216@280k` DESKTOP_384x216@280k
            >- `DESKTOP_512x288@500k` DESKTOP_512x288@500k
            >- `DESKTOP_768x432@1000k` DESKTOP_768x432@1000k
            >- `MOBILE_320x180@102k` MOBILE_320x180@102k
            >- `MOBILE_320x180@102k_BUFFERED` MOBILE_320x180@102k_BUFFERED
            >- `MOBILE_320x180@232k` MOBILE_320x180@232k
            >- `MOBILE_320x180@232k_BUFFERED` MOBILE_320x180@232k_BUFFERED
            >- `MOBILE_480x270@464k` MOBILE_480x270@464k
            >- `MOBILE_480x270@464k_BUFFERED` MOBILE_480x270@464k_BUFFERED
            >- `MOBILE_768x432@1000k` MOBILE_768x432@1000k
            >- `MOBILE_768x432@1000k_BUFFERED` MOBILE_768x432@1000k_BUFFERED
             Example: 720.
        output_format (VideoSubscriptionInsertVideoSubscriptionPostBodyOutputFormat): The output format
            >- `HLS` HLS
            >- `RTMP` RTMP
            >- `RTMP_PULL` RTMP Pull
            >- `SRT` SRT
             Example: RTMP.
        content (VideoSubscriptionInsertVideoSubscriptionPostBodyContent): Content of the stream
            >- `CLEAN` Output signal is the same as the input signal
            >- `PROGRAM` Score overlays and other enhancements have been added to the stream
             Example: CLEAN.
        subscription_id (Union[Unset, UUID]): The unique identifier of the video stream subscription Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        customer_id (Union[None, Unset, int]): Customer of the subscription Example: 1.
        stream_name (Union[Unset, str]): The name/stream key of the RTMP stream. This is an optional part of the RTMP
            url - not a text description.
        subscription_name (Union[Unset, str]): The name of the subscription
        output_url (Union[Unset, str]): The URL to send the output to. Only valid if outputFormat is 'RTMP' or 'SRT'
            Example: rtmp://rtmp-api.facebook.com:80/rtmp/?340ur0JHKJ0398hjkh387HKJD9.
        audio (Union[Unset, VideoSubscriptionInsertVideoSubscriptionPostBodyAudio]): Audio
            >- `AMBIENCE` Only ambience / crowd noise
            >- `BOTH` Both combined
            >- `BOTH_SPLIT_LR` Both (Ambience left channel, Commentary right channel)
            >- `COMMENTARY` Only commentary
             Default: VideoSubscriptionInsertVideoSubscriptionPostBodyAudio.BOTH. Example: COMMENTARY.
        mux_rate (Union[Unset, int]): The muxRate of the stream. Required for SRT outputFormat only. Example: 1200000.
    """

    fixture_id: UUID
    provider: str
    locale: str
    feed_type: VideoSubscriptionInsertVideoSubscriptionPostBodyFeedType
    output_resolution: VideoSubscriptionInsertVideoSubscriptionPostBodyOutputResolution
    output_format: VideoSubscriptionInsertVideoSubscriptionPostBodyOutputFormat
    content: VideoSubscriptionInsertVideoSubscriptionPostBodyContent
    source_number: int = 1
    subscription_id: Union[Unset, UUID] = UNSET
    customer_id: Union[None, Unset, int] = UNSET
    stream_name: Union[Unset, str] = UNSET
    subscription_name: Union[Unset, str] = UNSET
    output_url: Union[Unset, str] = UNSET
    audio: Union[Unset, VideoSubscriptionInsertVideoSubscriptionPostBodyAudio] = (
        VideoSubscriptionInsertVideoSubscriptionPostBodyAudio.BOTH
    )
    mux_rate: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id = str(self.fixture_id)

        provider = self.provider

        locale = self.locale

        source_number = self.source_number

        feed_type = self.feed_type.value

        output_resolution = self.output_resolution.value

        output_format = self.output_format.value

        content = self.content.value

        subscription_id: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        customer_id: Union[None, Unset, int]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        stream_name = self.stream_name

        subscription_name = self.subscription_name

        output_url = self.output_url

        audio: Union[Unset, str] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.value

        mux_rate = self.mux_rate

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fixtureId": fixture_id,
                "provider": provider,
                "locale": locale,
                "sourceNumber": source_number,
                "feedType": feed_type,
                "outputResolution": output_resolution,
                "outputFormat": output_format,
                "content": content,
            }
        )
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if stream_name is not UNSET:
            field_dict["streamName"] = stream_name
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if output_url is not UNSET:
            field_dict["outputURL"] = output_url
        if audio is not UNSET:
            field_dict["audio"] = audio
        if mux_rate is not UNSET:
            field_dict["muxRate"] = mux_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixture_id = UUID(d.pop("fixtureId"))

        provider = d.pop("provider")

        locale = d.pop("locale")

        source_number = d.pop("sourceNumber")

        feed_type = VideoSubscriptionInsertVideoSubscriptionPostBodyFeedType(
            d.pop("feedType")
        )

        output_resolution = (
            VideoSubscriptionInsertVideoSubscriptionPostBodyOutputResolution(
                d.pop("outputResolution")
            )
        )

        output_format = VideoSubscriptionInsertVideoSubscriptionPostBodyOutputFormat(
            d.pop("outputFormat")
        )

        content = VideoSubscriptionInsertVideoSubscriptionPostBodyContent(
            d.pop("content")
        )

        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: Union[Unset, UUID]
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        def _parse_customer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        customer_id = _parse_customer_id(d.pop("customerId", UNSET))

        stream_name = d.pop("streamName", UNSET)

        subscription_name = d.pop("subscriptionName", UNSET)

        output_url = d.pop("outputURL", UNSET)

        _audio = d.pop("audio", UNSET)
        audio: Union[Unset, VideoSubscriptionInsertVideoSubscriptionPostBodyAudio]
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = VideoSubscriptionInsertVideoSubscriptionPostBodyAudio(_audio)

        mux_rate = d.pop("muxRate", UNSET)

        video_subscription_insert_video_subscription_post_body = cls(
            fixture_id=fixture_id,
            provider=provider,
            locale=locale,
            source_number=source_number,
            feed_type=feed_type,
            output_resolution=output_resolution,
            output_format=output_format,
            content=content,
            subscription_id=subscription_id,
            customer_id=customer_id,
            stream_name=stream_name,
            subscription_name=subscription_name,
            output_url=output_url,
            audio=audio,
            mux_rate=mux_rate,
        )

        return video_subscription_insert_video_subscription_post_body
