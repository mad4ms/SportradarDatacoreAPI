import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.video_subscription_model_audio import VideoSubscriptionModelAudio
from ..models.video_subscription_model_content import VideoSubscriptionModelContent
from ..models.video_subscription_model_feed_type import VideoSubscriptionModelFeedType
from ..models.video_subscription_model_output_format import (
    VideoSubscriptionModelOutputFormat,
)
from ..models.video_subscription_model_output_resolution import (
    VideoSubscriptionModelOutputResolution,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_subscription_model_fixture import VideoSubscriptionModelFixture
    from ..models.video_subscription_model_organization import (
        VideoSubscriptionModelOrganization,
    )


T = TypeVar("T", bound="VideoSubscriptionModel")


@_attrs_define
class VideoSubscriptionModel:
    """
    Attributes:
        subscription_id (Union[Unset, UUID]): The unique identifier of the video stream subscription Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, VideoSubscriptionModelOrganization]): The organization that this video subscription
            belongs to
        customer_id (Union[None, Unset, int]): Customer of the subscription Example: 1.
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, VideoSubscriptionModelFixture]): The match
        provider (Union[Unset, str]): The code for the provider of the file Example: Test Provider.
        locale (Union[Unset, str]): The locale of the video Example: fr-FR.
        source_number (Union[Unset, int]): Unique identifier for the video source. This is unique for the
            provider/fixtureId/locale combination.  Unless the provider is supplying multiple sources per fixture/locale
            then this is normally 1. Default: 1. Example: 1.
        feed_type (Union[Unset, VideoSubscriptionModelFeedType]): Type of video input
            >- `ADDITIONAL_ANGLE` Additional angle
            >- `LOW_LATENCY` Low Latency
            >- `PRIMARY` Primary
             Example: PRIMARY.
        output_resolution (Union[Unset, VideoSubscriptionModelOutputResolution]): The resolution that you want to
            receive the video in.  This is only valid if outputFormat is `RTMP`.  If outputFormat is not `RTMP` then the
            output resolution is the same as the input resolution.  If specified the output resolution cannot be higher than
            the input resolution. You must have specific permission to chose anything other than 720p or 1080p.
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
        output_format (Union[Unset, VideoSubscriptionModelOutputFormat]): The output format
            >- `HLS` HLS
            >- `RTMP` RTMP
            >- `RTMP_PULL` RTMP Pull
            >- `SRT` SRT
             Example: RTMP.
        stream_name (Union[Unset, str]): The name/stream key of the RTMP stream. This is an optional part of the RTMP
            url - not a text description.
        subscription_name (Union[Unset, str]): The name of the subscription
        output_url (Union[Unset, str]): The URL to send the output to. Only valid if outputFormat is 'RTMP' or 'SRT'
            Example: rtmp://rtmp-api.facebook.com:80/rtmp/?340ur0JHKJ0398hjkh387HKJD9.
        audio (Union[Unset, VideoSubscriptionModelAudio]): Audio
            >- `AMBIENCE` Only ambience / crowd noise
            >- `BOTH` Both combined
            >- `BOTH_SPLIT_LR` Both (Ambience left channel, Commentary right channel)
            >- `COMMENTARY` Only commentary
             Default: VideoSubscriptionModelAudio.BOTH. Example: COMMENTARY.
        content (Union[Unset, VideoSubscriptionModelContent]): Content of the stream
            >- `CLEAN` Output signal is the same as the input signal
            >- `PROGRAM` Score overlays and other enhancements have been added to the stream
             Example: CLEAN.
        mux_rate (Union[Unset, int]): The muxRate of the stream. Required for SRT outputFormat only. Example: 1200000.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    subscription_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "VideoSubscriptionModelOrganization"] = UNSET
    customer_id: Union[None, Unset, int] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "VideoSubscriptionModelFixture"] = UNSET
    provider: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    source_number: Union[Unset, int] = 1
    feed_type: Union[Unset, VideoSubscriptionModelFeedType] = UNSET
    output_resolution: Union[Unset, VideoSubscriptionModelOutputResolution] = UNSET
    output_format: Union[Unset, VideoSubscriptionModelOutputFormat] = UNSET
    stream_name: Union[Unset, str] = UNSET
    subscription_name: Union[Unset, str] = UNSET
    output_url: Union[Unset, str] = UNSET
    audio: Union[Unset, VideoSubscriptionModelAudio] = VideoSubscriptionModelAudio.BOTH
    content: Union[Unset, VideoSubscriptionModelContent] = UNSET
    mux_rate: Union[Unset, int] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        subscription_id: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_id, Unset):
            subscription_id = str(self.subscription_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        customer_id: Union[None, Unset, int]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

        provider = self.provider

        locale = self.locale

        source_number = self.source_number

        feed_type: Union[Unset, str] = UNSET
        if not isinstance(self.feed_type, Unset):
            feed_type = self.feed_type.value

        output_resolution: Union[Unset, str] = UNSET
        if not isinstance(self.output_resolution, Unset):
            output_resolution = self.output_resolution.value

        output_format: Union[Unset, str] = UNSET
        if not isinstance(self.output_format, Unset):
            output_format = self.output_format.value

        stream_name = self.stream_name

        subscription_name = self.subscription_name

        output_url = self.output_url

        audio: Union[Unset, str] = UNSET
        if not isinstance(self.audio, Unset):
            audio = self.audio.value

        content: Union[Unset, str] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.value

        mux_rate = self.mux_rate

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if subscription_id is not UNSET:
            field_dict["subscriptionId"] = subscription_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if customer_id is not UNSET:
            field_dict["customerId"] = customer_id
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if provider is not UNSET:
            field_dict["provider"] = provider
        if locale is not UNSET:
            field_dict["locale"] = locale
        if source_number is not UNSET:
            field_dict["sourceNumber"] = source_number
        if feed_type is not UNSET:
            field_dict["feedType"] = feed_type
        if output_resolution is not UNSET:
            field_dict["outputResolution"] = output_resolution
        if output_format is not UNSET:
            field_dict["outputFormat"] = output_format
        if stream_name is not UNSET:
            field_dict["streamName"] = stream_name
        if subscription_name is not UNSET:
            field_dict["subscriptionName"] = subscription_name
        if output_url is not UNSET:
            field_dict["outputURL"] = output_url
        if audio is not UNSET:
            field_dict["audio"] = audio
        if content is not UNSET:
            field_dict["content"] = content
        if mux_rate is not UNSET:
            field_dict["muxRate"] = mux_rate
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_subscription_model_fixture import (
            VideoSubscriptionModelFixture,
        )
        from ..models.video_subscription_model_organization import (
            VideoSubscriptionModelOrganization,
        )

        d = dict(src_dict)
        _subscription_id = d.pop("subscriptionId", UNSET)
        subscription_id: Union[Unset, UUID]
        if isinstance(_subscription_id, Unset):
            subscription_id = UNSET
        else:
            subscription_id = UUID(_subscription_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, VideoSubscriptionModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = VideoSubscriptionModelOrganization.from_dict(_organization)

        def _parse_customer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        customer_id = _parse_customer_id(d.pop("customerId", UNSET))

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, VideoSubscriptionModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = VideoSubscriptionModelFixture.from_dict(_fixture)

        provider = d.pop("provider", UNSET)

        locale = d.pop("locale", UNSET)

        source_number = d.pop("sourceNumber", UNSET)

        _feed_type = d.pop("feedType", UNSET)
        feed_type: Union[Unset, VideoSubscriptionModelFeedType]
        if isinstance(_feed_type, Unset):
            feed_type = UNSET
        else:
            feed_type = VideoSubscriptionModelFeedType(_feed_type)

        _output_resolution = d.pop("outputResolution", UNSET)
        output_resolution: Union[Unset, VideoSubscriptionModelOutputResolution]
        if isinstance(_output_resolution, Unset):
            output_resolution = UNSET
        else:
            output_resolution = VideoSubscriptionModelOutputResolution(
                _output_resolution
            )

        _output_format = d.pop("outputFormat", UNSET)
        output_format: Union[Unset, VideoSubscriptionModelOutputFormat]
        if isinstance(_output_format, Unset):
            output_format = UNSET
        else:
            output_format = VideoSubscriptionModelOutputFormat(_output_format)

        stream_name = d.pop("streamName", UNSET)

        subscription_name = d.pop("subscriptionName", UNSET)

        output_url = d.pop("outputURL", UNSET)

        _audio = d.pop("audio", UNSET)
        audio: Union[Unset, VideoSubscriptionModelAudio]
        if isinstance(_audio, Unset):
            audio = UNSET
        else:
            audio = VideoSubscriptionModelAudio(_audio)

        _content = d.pop("content", UNSET)
        content: Union[Unset, VideoSubscriptionModelContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = VideoSubscriptionModelContent(_content)

        mux_rate = d.pop("muxRate", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        video_subscription_model = cls(
            subscription_id=subscription_id,
            organization_id=organization_id,
            organization=organization,
            customer_id=customer_id,
            fixture_id=fixture_id,
            fixture=fixture,
            provider=provider,
            locale=locale,
            source_number=source_number,
            feed_type=feed_type,
            output_resolution=output_resolution,
            output_format=output_format,
            stream_name=stream_name,
            subscription_name=subscription_name,
            output_url=output_url,
            audio=audio,
            content=content,
            mux_rate=mux_rate,
            updated=updated,
            added=added,
        )

        return video_subscription_model
