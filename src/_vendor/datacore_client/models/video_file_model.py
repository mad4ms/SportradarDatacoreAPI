import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.video_file_model_content import VideoFileModelContent
from ..models.video_file_model_feed_type import VideoFileModelFeedType
from ..models.video_file_model_format import VideoFileModelFormat
from ..models.video_file_model_origin_type_1 import VideoFileModelOriginType1
from ..models.video_file_model_origin_type_2_type_1 import (
    VideoFileModelOriginType2Type1,
)
from ..models.video_file_model_origin_type_3_type_1 import (
    VideoFileModelOriginType3Type1,
)
from ..models.video_file_model_resolution import VideoFileModelResolution
from ..models.video_file_model_status_type_1 import VideoFileModelStatusType1
from ..models.video_file_model_status_type_2_type_1 import (
    VideoFileModelStatusType2Type1,
)
from ..models.video_file_model_status_type_3_type_1 import (
    VideoFileModelStatusType3Type1,
)
from ..models.video_file_model_storage_provider_type_1 import (
    VideoFileModelStorageProviderType1,
)
from ..models.video_file_model_storage_provider_type_2_type_1 import (
    VideoFileModelStorageProviderType2Type1,
)
from ..models.video_file_model_storage_provider_type_3_type_1 import (
    VideoFileModelStorageProviderType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_file_model_fixture import VideoFileModelFixture
    from ..models.video_file_model_organization import VideoFileModelOrganization


T = TypeVar("T", bound="VideoFileModel")


@_attrs_define
class VideoFileModel:
    """
    Attributes:
        video_id (Union[Unset, UUID]): The unique identifier of the video Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, VideoFileModelOrganization]): The organization that this video file belongs to
        provider (Union[Unset, str]): The code for the provider of the file Example: Test Provider.
        locale (Union[Unset, str]): The locale of the video Example: fr-FR.
        source_number (Union[Unset, int]): Unique identifier for the video source. This is unique for the
            provider/fixtureId/locale combination.  Unless the provider is supplying multiple sources per fixture/locale
            then this is normally 1. Default: 1. Example: 1.
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, VideoFileModelFixture]): The match
        resolution (Union[Unset, VideoFileModelResolution]): The resolution of the video input
            >- `1080` 1920 x 1080
            >- `288` 512 x 288
            >- `720` 1280 x 720
             Example: 720.
        name (Union[Unset, str]): The name/description of the video file
        feed_type (Union[Unset, VideoFileModelFeedType]): Type of video input
            >- `ADDITIONAL_ANGLE` Additional angle
            >- `LOW_LATENCY` Low Latency
            >- `PRIMARY` Primary
             Example: PRIMARY.
        content (Union[Unset, VideoFileModelContent]): Content of the stream
            >- `CLEAN` Output signal is the same as the input signal
            >- `PROGRAM` Score overlays and other enhancements have been added to the stream
             Example: CLEAN.
        fps (Union[Unset, int]): fps for the video stream Default: 25. Example: 25.
        origin (Union[None, Unset, VideoFileModelOriginType1, VideoFileModelOriginType2Type1,
            VideoFileModelOriginType3Type1]): The origin of the video file
            >- None None
            >- `STREAM` Streamed
            >- `UPLOAD` Uploaded
            >- `VENUE` Recorded in venue
             Example: STREAM.
        format_ (Union[Unset, VideoFileModelFormat]): The format of the video file
            >- `HLS` A HLS play list
            >- `MP4` One MP4 file
             Example: HLS.
        storage_provider (Union[None, Unset, VideoFileModelStorageProviderType1,
            VideoFileModelStorageProviderType2Type1, VideoFileModelStorageProviderType3Type1]): Where the video file is
            stored?
            >- None None
            >- `5STREAM` 5stream
            >- `AV_SPORTRADAR` AV Sportradar
            >- `KEEMOTION` Keemotion
            >- `SYNERGY` Synergy
             Example: KEEMOTION.
        size (Union[None, Unset, float]): Size (Mb) of the video (only given if a single file) Example: 1024.2.
        length (Union[None, Unset, float]): Lenth (mins) of the video Example: 123.4.
        encoding (Union[Unset, str]): How is the video/audio encoded. codecs etc. Example: H.264/AAC.
        status (Union[None, Unset, VideoFileModelStatusType1, VideoFileModelStatusType2Type1,
            VideoFileModelStatusType3Type1]): What is the status of the file?
            >- None None
            >- `AVAILABLE` Available for access
            >- `BUILDABLE` Not currently available - but can be built on request
            >- `PENDING` Being added - some parts may be available
             Example: AVAILABLE.
        start_time (Union[Unset, datetime.datetime]): The time this recording started (UTC)
        expiry (Union[None, Unset, datetime.datetime]): When does this file expire? (UTC)
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    video_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "VideoFileModelOrganization"] = UNSET
    provider: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    source_number: Union[Unset, int] = 1
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "VideoFileModelFixture"] = UNSET
    resolution: Union[Unset, VideoFileModelResolution] = UNSET
    name: Union[Unset, str] = UNSET
    feed_type: Union[Unset, VideoFileModelFeedType] = UNSET
    content: Union[Unset, VideoFileModelContent] = UNSET
    fps: Union[Unset, int] = 25
    origin: Union[
        None,
        Unset,
        VideoFileModelOriginType1,
        VideoFileModelOriginType2Type1,
        VideoFileModelOriginType3Type1,
    ] = UNSET
    format_: Union[Unset, VideoFileModelFormat] = UNSET
    storage_provider: Union[
        None,
        Unset,
        VideoFileModelStorageProviderType1,
        VideoFileModelStorageProviderType2Type1,
        VideoFileModelStorageProviderType3Type1,
    ] = UNSET
    size: Union[None, Unset, float] = UNSET
    length: Union[None, Unset, float] = UNSET
    encoding: Union[Unset, str] = UNSET
    status: Union[
        None,
        Unset,
        VideoFileModelStatusType1,
        VideoFileModelStatusType2Type1,
        VideoFileModelStatusType3Type1,
    ] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    expiry: Union[None, Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        video_id: Union[Unset, str] = UNSET
        if not isinstance(self.video_id, Unset):
            video_id = str(self.video_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        provider = self.provider

        locale = self.locale

        source_number = self.source_number

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

        resolution: Union[Unset, str] = UNSET
        if not isinstance(self.resolution, Unset):
            resolution = self.resolution.value

        name = self.name

        feed_type: Union[Unset, str] = UNSET
        if not isinstance(self.feed_type, Unset):
            feed_type = self.feed_type.value

        content: Union[Unset, str] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.value

        fps = self.fps

        origin: Union[None, Unset, str]
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif isinstance(self.origin, VideoFileModelOriginType1):
            origin = self.origin.value
        elif isinstance(self.origin, VideoFileModelOriginType2Type1):
            origin = self.origin.value
        elif isinstance(self.origin, VideoFileModelOriginType3Type1):
            origin = self.origin.value
        else:
            origin = self.origin

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        storage_provider: Union[None, Unset, str]
        if isinstance(self.storage_provider, Unset):
            storage_provider = UNSET
        elif isinstance(self.storage_provider, VideoFileModelStorageProviderType1):
            storage_provider = self.storage_provider.value
        elif isinstance(self.storage_provider, VideoFileModelStorageProviderType2Type1):
            storage_provider = self.storage_provider.value
        elif isinstance(self.storage_provider, VideoFileModelStorageProviderType3Type1):
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
        elif isinstance(self.status, VideoFileModelStatusType1):
            status = self.status.value
        elif isinstance(self.status, VideoFileModelStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, VideoFileModelStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        expiry: Union[None, Unset, str]
        if isinstance(self.expiry, Unset):
            expiry = UNSET
        elif isinstance(self.expiry, datetime.datetime):
            expiry = self.expiry.isoformat()
        else:
            expiry = self.expiry

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if video_id is not UNSET:
            field_dict["videoId"] = video_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if provider is not UNSET:
            field_dict["provider"] = provider
        if locale is not UNSET:
            field_dict["locale"] = locale
        if source_number is not UNSET:
            field_dict["sourceNumber"] = source_number
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if name is not UNSET:
            field_dict["name"] = name
        if feed_type is not UNSET:
            field_dict["feedType"] = feed_type
        if content is not UNSET:
            field_dict["content"] = content
        if fps is not UNSET:
            field_dict["fps"] = fps
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
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if expiry is not UNSET:
            field_dict["expiry"] = expiry
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_file_model_fixture import VideoFileModelFixture
        from ..models.video_file_model_organization import VideoFileModelOrganization

        d = dict(src_dict)
        _video_id = d.pop("videoId", UNSET)
        video_id: Union[Unset, UUID]
        if isinstance(_video_id, Unset):
            video_id = UNSET
        else:
            video_id = UUID(_video_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, VideoFileModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = VideoFileModelOrganization.from_dict(_organization)

        provider = d.pop("provider", UNSET)

        locale = d.pop("locale", UNSET)

        source_number = d.pop("sourceNumber", UNSET)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, VideoFileModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = VideoFileModelFixture.from_dict(_fixture)

        _resolution = d.pop("resolution", UNSET)
        resolution: Union[Unset, VideoFileModelResolution]
        if isinstance(_resolution, Unset):
            resolution = UNSET
        else:
            resolution = VideoFileModelResolution(_resolution)

        name = d.pop("name", UNSET)

        _feed_type = d.pop("feedType", UNSET)
        feed_type: Union[Unset, VideoFileModelFeedType]
        if isinstance(_feed_type, Unset):
            feed_type = UNSET
        else:
            feed_type = VideoFileModelFeedType(_feed_type)

        _content = d.pop("content", UNSET)
        content: Union[Unset, VideoFileModelContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = VideoFileModelContent(_content)

        fps = d.pop("fps", UNSET)

        def _parse_origin(
            data: object,
        ) -> Union[
            None,
            Unset,
            VideoFileModelOriginType1,
            VideoFileModelOriginType2Type1,
            VideoFileModelOriginType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_1 = VideoFileModelOriginType1(data)

                return origin_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_2_type_1 = VideoFileModelOriginType2Type1(data)

                return origin_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                origin_type_3_type_1 = VideoFileModelOriginType3Type1(data)

                return origin_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    VideoFileModelOriginType1,
                    VideoFileModelOriginType2Type1,
                    VideoFileModelOriginType3Type1,
                ],
                data,
            )

        origin = _parse_origin(d.pop("origin", UNSET))

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, VideoFileModelFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = VideoFileModelFormat(_format_)

        def _parse_storage_provider(
            data: object,
        ) -> Union[
            None,
            Unset,
            VideoFileModelStorageProviderType1,
            VideoFileModelStorageProviderType2Type1,
            VideoFileModelStorageProviderType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_provider_type_1 = VideoFileModelStorageProviderType1(data)

                return storage_provider_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_provider_type_2_type_1 = (
                    VideoFileModelStorageProviderType2Type1(data)
                )

                return storage_provider_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                storage_provider_type_3_type_1 = (
                    VideoFileModelStorageProviderType3Type1(data)
                )

                return storage_provider_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    VideoFileModelStorageProviderType1,
                    VideoFileModelStorageProviderType2Type1,
                    VideoFileModelStorageProviderType3Type1,
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
            VideoFileModelStatusType1,
            VideoFileModelStatusType2Type1,
            VideoFileModelStatusType3Type1,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = VideoFileModelStatusType1(data)

                return status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = VideoFileModelStatusType2Type1(data)

                return status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = VideoFileModelStatusType3Type1(data)

                return status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    VideoFileModelStatusType1,
                    VideoFileModelStatusType2Type1,
                    VideoFileModelStatusType3Type1,
                ],
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

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

        video_file_model = cls(
            video_id=video_id,
            organization_id=organization_id,
            organization=organization,
            provider=provider,
            locale=locale,
            source_number=source_number,
            fixture_id=fixture_id,
            fixture=fixture,
            resolution=resolution,
            name=name,
            feed_type=feed_type,
            content=content,
            fps=fps,
            origin=origin,
            format_=format_,
            storage_provider=storage_provider,
            size=size,
            length=length,
            encoding=encoding,
            status=status,
            start_time=start_time,
            expiry=expiry,
            updated=updated,
            added=added,
        )

        return video_file_model
