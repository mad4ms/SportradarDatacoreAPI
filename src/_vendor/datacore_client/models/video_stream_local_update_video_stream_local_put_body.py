from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.video_stream_local_update_video_stream_local_put_body_format import (
    VideoStreamLocalUpdateVideoStreamLocalPutBodyFormat,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoStreamLocalUpdateVideoStreamLocalPutBody")


@_attrs_define
class VideoStreamLocalUpdateVideoStreamLocalPutBody:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        provider (Union[Unset, str]): The code for the provider of the file Example: Test Provider.
        source_number (Union[Unset, int]): Unique identifier for the video source. This is unique for the
            provider/fixtureId/locale combination.  Unless the provider is supplying multiple sources per fixture/locale
            then this is normally 1. Default: 1. Example: 1.
        format_ (Union[Unset, VideoStreamLocalUpdateVideoStreamLocalPutBodyFormat]): The format of the video file
            >- `HLS` A HLS play list
            >- `MP4` One MP4 file
             Example: HLS.
        url (Union[Unset, str]): The URL where the file can be found Example: https://hls.host.com/video/index.m3u8.
    """

    fixture_id: Union[Unset, UUID] = UNSET
    provider: Union[Unset, str] = UNSET
    source_number: Union[Unset, int] = 1
    format_: Union[Unset, VideoStreamLocalUpdateVideoStreamLocalPutBodyFormat] = UNSET
    url: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        provider = self.provider

        source_number = self.source_number

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if source_number is not UNSET:
            field_dict["sourceNumber"] = source_number
        if format_ is not UNSET:
            field_dict["format"] = format_
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        provider = d.pop("provider", UNSET)

        source_number = d.pop("sourceNumber", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, VideoStreamLocalUpdateVideoStreamLocalPutBodyFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = VideoStreamLocalUpdateVideoStreamLocalPutBodyFormat(_format_)

        url = d.pop("url", UNSET)

        video_stream_local_update_video_stream_local_put_body = cls(
            fixture_id=fixture_id,
            provider=provider,
            source_number=source_number,
            format_=format_,
            url=url,
        )

        return video_stream_local_update_video_stream_local_put_body
