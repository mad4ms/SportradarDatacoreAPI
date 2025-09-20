from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.video_stream_local_insert_video_stream_local_post_body_format import (
    VideoStreamLocalInsertVideoStreamLocalPostBodyFormat,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VideoStreamLocalInsertVideoStreamLocalPostBody")


@_attrs_define
class VideoStreamLocalInsertVideoStreamLocalPostBody:
    """
    Attributes:
        url (str): The URL where the file can be found Example: https://hls.host.com/video/index.m3u8.
        url_id (Union[Unset, UUID]): The unique identifier of the video Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        provider (Union[Unset, str]): The code for the provider of the file Example: Test Provider.
        source_number (Union[Unset, int]): Unique identifier for the video source. This is unique for the
            provider/fixtureId/locale combination.  Unless the provider is supplying multiple sources per fixture/locale
            then this is normally 1. Default: 1. Example: 1.
        format_ (Union[Unset, VideoStreamLocalInsertVideoStreamLocalPostBodyFormat]): The format of the video file
            >- `HLS` A HLS play list
            >- `MP4` One MP4 file
             Example: HLS.
    """

    url: str
    url_id: Union[Unset, UUID] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    provider: Union[Unset, str] = UNSET
    source_number: Union[Unset, int] = 1
    format_: Union[Unset, VideoStreamLocalInsertVideoStreamLocalPostBodyFormat] = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        url_id: Union[Unset, str] = UNSET
        if not isinstance(self.url_id, Unset):
            url_id = str(self.url_id)

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        provider = self.provider

        source_number = self.source_number

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if url_id is not UNSET:
            field_dict["urlId"] = url_id
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if provider is not UNSET:
            field_dict["provider"] = provider
        if source_number is not UNSET:
            field_dict["sourceNumber"] = source_number
        if format_ is not UNSET:
            field_dict["format"] = format_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        _url_id = d.pop("urlId", UNSET)
        url_id: Union[Unset, UUID]
        if isinstance(_url_id, Unset):
            url_id = UNSET
        else:
            url_id = UUID(_url_id)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        provider = d.pop("provider", UNSET)

        source_number = d.pop("sourceNumber", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, VideoStreamLocalInsertVideoStreamLocalPostBodyFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = VideoStreamLocalInsertVideoStreamLocalPostBodyFormat(_format_)

        video_stream_local_insert_video_stream_local_post_body = cls(
            url=url,
            url_id=url_id,
            fixture_id=fixture_id,
            provider=provider,
            source_number=source_number,
            format_=format_,
        )

        return video_stream_local_insert_video_stream_local_post_body
