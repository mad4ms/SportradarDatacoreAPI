import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.video_file_post_body_content import VideoFilePostBodyContent
from ..models.video_file_post_body_feed_type import VideoFilePostBodyFeedType
from ..models.video_file_post_body_format import VideoFilePostBodyFormat
from ..models.video_file_post_body_origin_type_1 import VideoFilePostBodyOriginType1
from ..models.video_file_post_body_origin_type_2_type_1 import VideoFilePostBodyOriginType2Type1
from ..models.video_file_post_body_origin_type_3_type_1 import VideoFilePostBodyOriginType3Type1
from ..models.video_file_post_body_resolution import VideoFilePostBodyResolution
from ..models.video_file_post_body_status_type_1 import VideoFilePostBodyStatusType1
from ..models.video_file_post_body_status_type_2_type_1 import VideoFilePostBodyStatusType2Type1
from ..models.video_file_post_body_status_type_3_type_1 import VideoFilePostBodyStatusType3Type1
from ..models.video_file_post_body_storage_provider_type_1 import VideoFilePostBodyStorageProviderType1
from ..models.video_file_post_body_storage_provider_type_2_type_1 import VideoFilePostBodyStorageProviderType2Type1
from ..models.video_file_post_body_storage_provider_type_3_type_1 import VideoFilePostBodyStorageProviderType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoFilePostBody")


@_attrs_define
class VideoFilePostBody:
    """
    Attributes:
        provider (str): The code for the provider of the file Example: Test Provider.
        locale (str): The locale of the video Example: fr-FR.
        source_number (int): Unique identifier for the video source. This is unique for the provider/fixtureId/locale
            combination.  Unless the provider is supplying multiple sources per fixture/locale then this is normally 1.
            Default: 1. Example: 1.
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        resolution (VideoFilePostBodyResolution): The resolution of the video input
            >- `1080` 1920 x 1080
            >- `288` 512 x 288
            >- `720` 1280 x 720
             Example: 720.
        feed_type (VideoFilePostBodyFeedType): Type of video input
            >- `ADDITIONAL_ANGLE` Additional angle
            >- `LOW_LATENCY` Low Latency
            >- `PRIMARY` Primary
             Example: PRIMARY.
        content (VideoFilePostBodyContent): Content of the stream
            >- `CLEAN` Output signal is the same as the input signal
            >- `PROGRAM` Score overlays and other enhancements have been added to the stream
             Example: CLEAN.
        fps (int): fps for the video stream Default: 25. Example: 25.
        url (str): The URL where the file can be found Example: https://hls.host.com/video/index.m3u8.
        start_time (datetime.datetime): The time this recording started (UTC)
        video_id (Union[Unset, UUID]): The unique identifier of the video Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name (Union[Unset, str]): The name/description of the video file
        origin (Union[None, Unset, VideoFilePostBodyOriginType1, VideoFilePostBodyOriginType2Type1,
            VideoFilePostBodyOriginType3Type1]): The origin of the video file
            >- None None
            >- `STREAM` Streamed
            >- `UPLOAD` Uploaded
            >- `VENUE` Recorded in venue
             Example: STREAM.
        format_ (Union[Unset, VideoFilePostBodyFormat]): The format of the video file
            >- `HLS` A HLS play list
            >- `MP4` One MP4 file
             Example: HLS.
        storage_provider (Union[None, Unset, VideoFilePostBodyStorageProviderType1,
            VideoFilePostBodyStorageProviderType2Type1, VideoFilePostBodyStorageProviderType3Type1]): Where the video file
            is stored?
            >- None None
            >- `5STREAM` 5stream
            >- `AV_SPORTRADAR` AV Sportradar
            >- `KEEMOTION` Keemotion
            >- `SYNERGY` Synergy
             Example: KEEMOTION.
        size (Union[None, Unset, float]): Size (Mb) of the video (only given if a single file) Example: 1024.2.
        length (Union[None, Unset, float]): Lenth (mins) of the video Example: 123.4.
        encoding (Union[Unset, str]): How is the video/audio encoded. codecs etc. Example: H.264/AAC.
        status (Union[None, Unset, VideoFilePostBodyStatusType1, VideoFilePostBodyStatusType2Type1,
            VideoFilePostBodyStatusType3Type1]): What is the status of the file?
            >- None None
            >- `AVAILABLE` Available for access
            >- `BUILDABLE` Not currently available - but can be built on request
            >- `PENDING` Being added - some parts may be available
             Example: AVAILABLE.
        expiry (Union[None, Unset, datetime.datetime]): When does this file expire? (UTC)
    """

    provider: str
    locale: str
    fixture_id: UUID
    resolution: VideoFilePostBodyResolution
    feed_type: VideoFilePostBodyFeedType
    content: VideoFilePostBodyContent
    url: str
    start_time: datetime.datetime
    source_number: int = 1
    fps: int = 25
    video_id: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    origin: Union[
        None, Unset, VideoFilePostBodyOriginType1, VideoFilePostBodyOriginType2Type1, VideoFilePostBodyOriginType3Type1
    ] = UNSET
    format_: Union[Unset, VideoFilePostBodyFormat] = UNSET
    storage_provider: Union[
        None,
        Unset,
        VideoFilePostBodyStorageProviderType1,
        VideoFilePostBodyStorageProviderType2Type1,
        VideoFilePostBodyStorageProviderType3Type1,
    ] = UNSET
    size: Union[None, Unset, float] = UNSET
    length: Union[None, Unset, float] = UNSET
    encoding: Union[Unset, str] = UNSET
    status: Union[
        None, Unset, VideoFilePostBodyStatusType1, VideoFilePostBodyStatusType2Type1, VideoFilePostBodyStatusType3Type1
    ] = UNSET
    expiry: Union[None, Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        provider = self.provider

        locale = self.locale

        source_number = self.source_number

        fixture_id = str(self.fixture_id)

        resolution = self.resolution.value

        feed_type = self.feed_type.value

        content = self.content.value

        fps = self.fps

        url = self.url

        start_time = self.start_time.isoformat()

        video_id: Union[Unset, str] = UNSET
        if not isinstance(self.video_id, Unset):
            video_id = str(self.video_id)

        name = self.name

        origin: Union[None, Unset, str]
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif isinstance(self.origin, VideoFilePostBodyOriginType1):
            origin = self.origin.value
        elif isinstance(self.origin, VideoFilePostBodyOriginType2Type1):
            origin = self.origin.value
        elif isinstance(self.origin, VideoFilePostBodyOriginType3Type1):
            origin = self.origin.value
        else:
            origin = self.origin

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        storage_provider: Union[None, Unset, str]
        if isinstance(self.storage_provider, Unset):
            storage_provider = UNSET
        elif isinstance(self.storage_provider, VideoFilePostBodyStorageProviderType1):
            storage_provider = self.storage_provider.value
        elif isinstance(self.storage_provider, VideoFilePostBodyStorageProviderType2Type1):
            storage_provider = self.storage_provider.value
        elif isinstance(self.storage_provider, VideoFilePostBodyStorageProviderType3Type1):
            storage_provider = self.storage_provider.value
        else:
            storage_provider = self.storage_provider

        size: Union[None, Unset, float]
        if isinstance(self.size, Unset):
            size = UNSET
        else:
            size = self.size

        length: Union[None, Unset, float]
        if isinstance(self.length, Unset):
            length = UNSET
        else:
            length = self.length

        encoding = self.encoding

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, VideoFilePostBodyStatusType1):
            status = self.status.value
        elif isinstance(self.status, VideoFilePostBodyStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, VideoFilePostBodyStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        expiry: Union[None, Unset, str]
        if isinstance(self.expiry, Unset):
            expiry = UNSET
        elif isinstance(self.expiry, datetime.datetime):
            expiry = self.expiry.isoformat()
        else:
            expiry = self.expiry

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "provider": provider,
                "locale": locale,
                "sourceNumber": source_number,
                "fixtureId": fixture_id,
                "resolution": resolution,
                "feedType": feed_type,
                "content": content,
                "fps": fps,
                "url": url,
                "startTime": start_time,
            }
        )
        if video_id is not UNSET:
            field_dict["videoId"] = video_id
        if name is not UNSET:
            field_dict["name"] = name
        if origin is not UNSET:
            field_dict["origin"] = origin
        if format_ is not UNSET:
            field_dict["format"] = format_
        if storage_provider is not UNSET:
            field_dict["storageProvider"] = storage_provider
        if size is not UNSET:
            field_dict["size"] = size
        if length is not UNSET:
            field_dict["length"] = length
        if encoding is not UNSET:
            field_dict["encoding"] = encoding
        if status is not UNSET:
            field_dict["status"] = status
        if expiry is not UNSET:
            field_dict["expiry"] = expiry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        provider = d.pop("provider")

        locale = d.pop("locale")

        source_number = d.pop("sourceNumber")

        fixture_id = UUID(d.pop("fixtureId"))

        resolution = VideoFilePostBodyResolution(d.pop("resolution"))

        feed_type = VideoFilePostBodyFeedType(d.pop("feedType"))

        content = VideoFilePostBodyContent(d.pop("content"))

        fps = d.pop("fps")

        url = d.pop("url")

        start_time = isoparse(d.pop("startTime"))

        _video_id = d.pop("videoId", UNSET)
        video_id: Union[Unset, UUID]
        if isinstance(_video_id, Unset):
            video_id = UNSET
        else:
            video_id = UUID(_video_id)

        name = d.pop("name", UNSET)

        def _parse_origin(
            data: object,
        ) -> Union[
            None,
            Unset,
            VideoFilePostBodyOriginType1,
            VideoFilePostBodyOriginType2Type1,
            VideoFilePostBodyOriginType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_1 = VideoFilePostBodyOriginType1(data)

                return origin_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_2_type_1 = VideoFilePostBodyOriginType2Type1(data)

                return origin_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_3_type_1 = VideoFilePostBodyOriginType3Type1(data)

                return origin_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    VideoFilePostBodyOriginType1,
                    VideoFilePostBodyOriginType2Type1,
                    VideoFilePostBodyOriginType3Type1,
                ],
                data,
            )

        origin = _parse_origin(d.pop("origin", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, VideoFilePostBodyFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = VideoFilePostBodyFormat(_format_)

        def _parse_storage_provider(
            data: object,
        ) -> Union[
            None,
            Unset,
            VideoFilePostBodyStorageProviderType1,
            VideoFilePostBodyStorageProviderType2Type1,
            VideoFilePostBodyStorageProviderType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_provider_type_1 = VideoFilePostBodyStorageProviderType1(data)

                return storage_provider_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_provider_type_2_type_1 = VideoFilePostBodyStorageProviderType2Type1(data)

                return storage_provider_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_provider_type_3_type_1 = VideoFilePostBodyStorageProviderType3Type1(data)

                return storage_provider_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    VideoFilePostBodyStorageProviderType1,
                    VideoFilePostBodyStorageProviderType2Type1,
                    VideoFilePostBodyStorageProviderType3Type1,
                ],
                data,
            )

        storage_provider = _parse_storage_provider(d.pop("storageProvider", UNSET))

        def _parse_size(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        size = _parse_size(d.pop("size", UNSET))

        def _parse_length(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        length = _parse_length(d.pop("length", UNSET))

        encoding = d.pop("encoding", UNSET)

        def _parse_status(
            data: object,
        ) -> Union[
            None,
            Unset,
            VideoFilePostBodyStatusType1,
            VideoFilePostBodyStatusType2Type1,
            VideoFilePostBodyStatusType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = VideoFilePostBodyStatusType1(data)

                return status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = VideoFilePostBodyStatusType2Type1(data)

                return status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = VideoFilePostBodyStatusType3Type1(data)

                return status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    VideoFilePostBodyStatusType1,
                    VideoFilePostBodyStatusType2Type1,
                    VideoFilePostBodyStatusType3Type1,
                ],
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_expiry(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiry_type_0 = isoparse(data)

                return expiry_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expiry = _parse_expiry(d.pop("expiry", UNSET))

        video_file_post_body = cls(
            provider=provider,
            locale=locale,
            source_number=source_number,
            fixture_id=fixture_id,
            resolution=resolution,
            feed_type=feed_type,
            content=content,
            fps=fps,
            url=url,
            start_time=start_time,
            video_id=video_id,
            name=name,
            origin=origin,
            format_=format_,
            storage_provider=storage_provider,
            size=size,
            length=length,
            encoding=encoding,
            status=status,
            expiry=expiry,
        )

        return video_file_post_body
