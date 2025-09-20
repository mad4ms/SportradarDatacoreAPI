import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.video_stream_local_model_format import VideoStreamLocalModelFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_stream_local_model_fixture import VideoStreamLocalModelFixture
    from ..models.video_stream_local_model_organization import (
        VideoStreamLocalModelOrganization,
    )


T = TypeVar("T", bound="VideoStreamLocalModel")


@_attrs_define
class VideoStreamLocalModel:
    """
    Attributes:
        url_id (Union[Unset, UUID]): The unique identifier of the video Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, VideoStreamLocalModelOrganization]): The organization that this Video Stream Local
            belongs to
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, VideoStreamLocalModelFixture]): The match
        provider (Union[Unset, str]): The code for the provider of the file Example: Test Provider.
        source_number (Union[Unset, int]): Unique identifier for the video source. This is unique for the
            provider/fixtureId/locale combination.  Unless the provider is supplying multiple sources per fixture/locale
            then this is normally 1. Default: 1. Example: 1.
        format_ (Union[Unset, VideoStreamLocalModelFormat]): The format of the video file
            >- `HLS` A HLS play list
            >- `MP4` One MP4 file
             Example: HLS.
        url (Union[Unset, str]): The URL where the file can be found Example: https://hls.host.com/video/index.m3u8.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    url_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "VideoStreamLocalModelOrganization"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "VideoStreamLocalModelFixture"] = UNSET
    provider: Union[Unset, str] = UNSET
    source_number: Union[Unset, int] = 1
    format_: Union[Unset, VideoStreamLocalModelFormat] = UNSET
    url: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        url_id: Union[Unset, str] = UNSET
        if not isinstance(self.url_id, Unset):
            url_id = str(self.url_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

        provider = self.provider

        source_number = self.source_number

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        url = self.url

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if url_id is not UNSET:
            field_dict["urlId"] = url_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if provider is not UNSET:
            field_dict["provider"] = provider
        if source_number is not UNSET:
            field_dict["sourceNumber"] = source_number
        if format_ is not UNSET:
            field_dict["format"] = format_
        if url is not UNSET:
            field_dict["url"] = url
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_stream_local_model_fixture import (
            VideoStreamLocalModelFixture,
        )
        from ..models.video_stream_local_model_organization import (
            VideoStreamLocalModelOrganization,
        )

        d = dict(src_dict)
        _url_id = d.pop("urlId", UNSET)
        url_id: Union[Unset, UUID]
        if isinstance(_url_id, Unset):
            url_id = UNSET
        else:
            url_id = UUID(_url_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, VideoStreamLocalModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = VideoStreamLocalModelOrganization.from_dict(_organization)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, VideoStreamLocalModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = VideoStreamLocalModelFixture.from_dict(_fixture)

        provider = d.pop("provider", UNSET)

        source_number = d.pop("sourceNumber", UNSET)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, VideoStreamLocalModelFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = VideoStreamLocalModelFormat(_format_)

        url = d.pop("url", UNSET)

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

        video_stream_local_model = cls(
            url_id=url_id,
            organization_id=organization_id,
            organization=organization,
            fixture_id=fixture_id,
            fixture=fixture,
            provider=provider,
            source_number=source_number,
            format_=format_,
            url=url,
            updated=updated,
            added=added,
        )

        return video_stream_local_model
