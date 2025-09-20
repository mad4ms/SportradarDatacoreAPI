import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.video_stream_outputs_model_content import VideoStreamOutputsModelContent
from ..models.video_stream_outputs_model_feed_type import (
    VideoStreamOutputsModelFeedType,
)
from ..models.video_stream_outputs_model_input_resolution import (
    VideoStreamOutputsModelInputResolution,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.video_stream_outputs_model_competition import (
        VideoStreamOutputsModelCompetition,
    )
    from ..models.video_stream_outputs_model_fixture import (
        VideoStreamOutputsModelFixture,
    )
    from ..models.video_stream_outputs_model_organization import (
        VideoStreamOutputsModelOrganization,
    )
    from ..models.video_stream_outputs_model_venue import VideoStreamOutputsModelVenue


T = TypeVar("T", bound="VideoStreamOutputsModel")


@_attrs_define
class VideoStreamOutputsModel:
    """
    Attributes:
        video_input_id (Union[Unset, UUID]): The unique identifier of the video input Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        master_venue_id (Union[Unset, UUID]): The unique identifier of the master venue Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, VideoStreamOutputsModelOrganization]): The organization that this Video Stream
            Outputs belongs to
        venue_id (Union[Unset, UUID]): The unique identifier of the venue Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        venue (Union[Unset, VideoStreamOutputsModelVenue]): The venue that this match belongs to
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, VideoStreamOutputsModelCompetition]): The competition that this season belongs to
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, VideoStreamOutputsModelFixture]): The match
        provider (Union[Unset, str]): The code for the provider of the file Example: Test Provider.
        locale (Union[Unset, str]): The locale of the video Example: fr-FR.
        source_number (Union[Unset, int]): Unique identifier for the video source. This is unique for the
            provider/fixtureId/locale combination.  Unless the provider is supplying multiple sources per fixture/locale
            then this is normally 1. Default: 1. Example: 1.
        feed_type (Union[Unset, VideoStreamOutputsModelFeedType]): Type of video input
            >- `ADDITIONAL_ANGLE` Additional angle
            >- `LOW_LATENCY` Low Latency
            >- `PRIMARY` Primary
             Example: PRIMARY.
        input_resolution (Union[Unset, VideoStreamOutputsModelInputResolution]): The resolution of the video input
            >- `1080` 1920 x 1080
            >- `288` 512 x 288
            >- `720` 1280 x 720
             Example: 720.
        name (Union[Unset, str]): The name of the video source Example: Automated Capture Feed.
        content (Union[Unset, VideoStreamOutputsModelContent]): Content of the stream
            >- `CLEAN` Output signal is the same as the input signal
            >- `PROGRAM` Score overlays and other enhancements have been added to the stream
             Default: VideoStreamOutputsModelContent.CLEAN. Example: CLEAN.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        audio_ambience (Union[Unset, bool]): Audio Ambience Example: True.
        audio_commentary (Union[Unset, bool]): Audio Commentary Example: True.
    """

    video_input_id: Union[Unset, UUID] = UNSET
    master_venue_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "VideoStreamOutputsModelOrganization"] = UNSET
    venue_id: Union[Unset, UUID] = UNSET
    venue: Union[Unset, "VideoStreamOutputsModelVenue"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "VideoStreamOutputsModelCompetition"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "VideoStreamOutputsModelFixture"] = UNSET
    provider: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    source_number: Union[Unset, int] = 1
    feed_type: Union[Unset, VideoStreamOutputsModelFeedType] = UNSET
    input_resolution: Union[Unset, VideoStreamOutputsModelInputResolution] = UNSET
    name: Union[Unset, str] = UNSET
    content: Union[Unset, VideoStreamOutputsModelContent] = (
        VideoStreamOutputsModelContent.CLEAN
    )
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    audio_ambience: Union[Unset, bool] = UNSET
    audio_commentary: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        video_input_id: Union[Unset, str] = UNSET
        if not isinstance(self.video_input_id, Unset):
            video_input_id = str(self.video_input_id)

        master_venue_id: Union[Unset, str] = UNSET
        if not isinstance(self.master_venue_id, Unset):
            master_venue_id = str(self.master_venue_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        venue_id: Union[Unset, str] = UNSET
        if not isinstance(self.venue_id, Unset):
            venue_id = str(self.venue_id)

        venue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        competition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

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

        input_resolution: Union[Unset, str] = UNSET
        if not isinstance(self.input_resolution, Unset):
            input_resolution = self.input_resolution.value

        name = self.name

        content: Union[Unset, str] = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.value

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        audio_ambience = self.audio_ambience

        audio_commentary = self.audio_commentary

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if video_input_id is not UNSET:
            field_dict["videoInputId"] = video_input_id
        if master_venue_id is not UNSET:
            field_dict["masterVenueId"] = master_venue_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id
        if venue is not UNSET:
            field_dict["venue"] = venue
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
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
        if input_resolution is not UNSET:
            field_dict["inputResolution"] = input_resolution
        if name is not UNSET:
            field_dict["name"] = name
        if content is not UNSET:
            field_dict["content"] = content
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if audio_ambience is not UNSET:
            field_dict["audioAmbience"] = audio_ambience
        if audio_commentary is not UNSET:
            field_dict["audioCommentary"] = audio_commentary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.video_stream_outputs_model_competition import (
            VideoStreamOutputsModelCompetition,
        )
        from ..models.video_stream_outputs_model_fixture import (
            VideoStreamOutputsModelFixture,
        )
        from ..models.video_stream_outputs_model_organization import (
            VideoStreamOutputsModelOrganization,
        )
        from ..models.video_stream_outputs_model_venue import (
            VideoStreamOutputsModelVenue,
        )

        d = dict(src_dict)
        _video_input_id = d.pop("videoInputId", UNSET)
        video_input_id: Union[Unset, UUID]
        if isinstance(_video_input_id, Unset):
            video_input_id = UNSET
        else:
            video_input_id = UUID(_video_input_id)

        _master_venue_id = d.pop("masterVenueId", UNSET)
        master_venue_id: Union[Unset, UUID]
        if isinstance(_master_venue_id, Unset):
            master_venue_id = UNSET
        else:
            master_venue_id = UUID(_master_venue_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, VideoStreamOutputsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = VideoStreamOutputsModelOrganization.from_dict(_organization)

        _venue_id = d.pop("venueId", UNSET)
        venue_id: Union[Unset, UUID]
        if isinstance(_venue_id, Unset):
            venue_id = UNSET
        else:
            venue_id = UUID(_venue_id)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, VideoStreamOutputsModelVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = VideoStreamOutputsModelVenue.from_dict(_venue)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, VideoStreamOutputsModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = VideoStreamOutputsModelCompetition.from_dict(_competition)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, VideoStreamOutputsModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = VideoStreamOutputsModelFixture.from_dict(_fixture)

        provider = d.pop("provider", UNSET)

        locale = d.pop("locale", UNSET)

        source_number = d.pop("sourceNumber", UNSET)

        _feed_type = d.pop("feedType", UNSET)
        feed_type: Union[Unset, VideoStreamOutputsModelFeedType]
        if isinstance(_feed_type, Unset):
            feed_type = UNSET
        else:
            feed_type = VideoStreamOutputsModelFeedType(_feed_type)

        _input_resolution = d.pop("inputResolution", UNSET)
        input_resolution: Union[Unset, VideoStreamOutputsModelInputResolution]
        if isinstance(_input_resolution, Unset):
            input_resolution = UNSET
        else:
            input_resolution = VideoStreamOutputsModelInputResolution(_input_resolution)

        name = d.pop("name", UNSET)

        _content = d.pop("content", UNSET)
        content: Union[Unset, VideoStreamOutputsModelContent]
        if isinstance(_content, Unset):
            content = UNSET
        else:
            content = VideoStreamOutputsModelContent(_content)

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

        audio_ambience = d.pop("audioAmbience", UNSET)

        audio_commentary = d.pop("audioCommentary", UNSET)

        video_stream_outputs_model = cls(
            video_input_id=video_input_id,
            master_venue_id=master_venue_id,
            organization_id=organization_id,
            organization=organization,
            venue_id=venue_id,
            venue=venue,
            competition_id=competition_id,
            competition=competition,
            fixture_id=fixture_id,
            fixture=fixture,
            provider=provider,
            locale=locale,
            source_number=source_number,
            feed_type=feed_type,
            input_resolution=input_resolution,
            name=name,
            content=content,
            updated=updated,
            added=added,
            audio_ambience=audio_ambience,
            audio_commentary=audio_commentary,
        )

        return video_stream_outputs_model
