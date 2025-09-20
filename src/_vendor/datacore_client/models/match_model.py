import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.match_model_competitor_type import MatchModelCompetitorType
from ..models.match_model_discipline_type_1 import MatchModelDisciplineType1
from ..models.match_model_discipline_type_2_type_1 import MatchModelDisciplineType2Type1
from ..models.match_model_discipline_type_3_type_1 import MatchModelDisciplineType3Type1
from ..models.match_model_fixture_type import MatchModelFixtureType
from ..models.match_model_maximum_period_type_used_type_1 import (
    MatchModelMaximumPeriodTypeUsedType1,
)
from ..models.match_model_maximum_period_type_used_type_2_type_1 import (
    MatchModelMaximumPeriodTypeUsedType2Type1,
)
from ..models.match_model_maximum_period_type_used_type_3_type_1 import (
    MatchModelMaximumPeriodTypeUsedType3Type1,
)
from ..models.match_model_practice_drill_type_type_1 import (
    MatchModelPracticeDrillTypeType1,
)
from ..models.match_model_practice_drill_type_type_2_type_1 import (
    MatchModelPracticeDrillTypeType2Type1,
)
from ..models.match_model_practice_drill_type_type_3_type_1 import (
    MatchModelPracticeDrillTypeType3Type1,
)
from ..models.match_model_status import MatchModelStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_model_broadcasts import MatchModelBroadcasts
    from ..models.match_model_environmental_details import (
        MatchModelEnvironmentalDetails,
    )
    from ..models.match_model_fixture_profile import MatchModelFixtureProfile
    from ..models.match_model_match_competitor import MatchModelMatchCompetitor
    from ..models.match_model_organization import MatchModelOrganization
    from ..models.match_model_pool import MatchModelPool
    from ..models.match_model_round import MatchModelRound
    from ..models.match_model_season import MatchModelSeason
    from ..models.match_model_series import MatchModelSeries
    from ..models.match_model_social_media import MatchModelSocialMedia
    from ..models.match_model_stage import MatchModelStage
    from ..models.match_model_venue import MatchModelVenue


T = TypeVar("T", bound="MatchModel")


@_attrs_define
class MatchModel:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, MatchModelOrganization]): The organization that this match belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, MatchModelSeason]): The season linked to this record
        practice_drill_type (Union[MatchModelPracticeDrillTypeType1, MatchModelPracticeDrillTypeType2Type1,
            MatchModelPracticeDrillTypeType3Type1, None, Unset]): Practice types
            >- None None
            >- `DRILL` Drill
            >- `FITNESS` Fitness
            >- `GAME` Practice Game
            >- `OTHER` Other
             Example: DRILL.
        international_reference (Union[None, Unset, str]): The international reference for this match given by the sport
            governing body Example: CA3243-3.
        status (Union[Unset, MatchModelStatus]): Match status
            >- `ABANDONED` Abandoned - Match began but had to be stopped
            >- `ABOUT_TO_START` About to Start - Match is about to start
            >- `BYE` Bye - Team has 'rest'
            >- `CANCELLED` Cancelled - Cancelled - will not be played
            >- `CONFIRMED` Confirmed - Match officially completed
            >- `DRAFT` Draft - Not fully scheduled
            >- `FINISHED` Finished - Match finished by not yet 'official'
            >- `IF_NEEDED` If Needed - Only played if needed
            >- `IN_PROGRESS` In Progress - Currently in play
            >- `ON_PITCH` On Pitch - Players appered on the playing field
            >- `PENDING` Pending - Ready to start
            >- `POSTPONED` Postponed - Will be played at a future time
            >- `SCHEDULED` Scheduled - Yet to be played
            >- `WARM_UP` Warm Up - Players have begun to warm up
             Default: MatchModelStatus.SCHEDULED. Example: SCHEDULED.
        fixture_number (Union[None, Unset, int]): Match number (range of -2147483648 to 2147483647) Example: 123.
        name_local (Union[None, Unset, str]): The name of the match in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: Grand Final.
        name_latin (Union[None, Unset, str]): The name of the match in [latin](#section/Introduction/Character-Sets-and-
            Names) characters Example: Grand Final.
        start_time_local (Union[None, Unset, datetime.datetime]): Local start time Example: 2018-08-16T18:00:00.
        start_time_utc (Union[None, Unset, datetime.datetime]): Start time (UTC). This is automatically generated based
            on the timezone of the venue. Example: 2018-08-16T02:00:00.
        finish_recording_time_utc (Union[Unset, datetime.datetime]): (TO BE REMOVED) Start time (UTC) + durationFull
            Example: 2018-08-16T02:00:00.
        finish_recording_time_local (Union[Unset, datetime.datetime]): (TO BE REMOVED) Start time (Local) + durationFull
            Example: 2018-08-16T02:00:00.
        start_time_actual_utc (Union[None, Unset, datetime.datetime]): Actual start time (UTC) Example:
            2018-08-16T02:02:23.
        end_time_actual_utc (Union[None, Unset, datetime.datetime]): Actual end time (UTC) Example: 2018-08-16T04:02:23.
        times_unconfirmed (Union[Unset, bool]): Is the match time yet to be confirmed ? Example: True.
        locked (Union[Unset, bool]): Is the match locked (to prevent editing)? Example: True.
        placing_if_won (Union[None, Unset, int]): Place if Won? Example: 1.
        placing_if_lost (Union[None, Unset, int]): Place if Lost? Example: 1.
        attendance (Union[None, Unset, int]): Crowd attendance Example: 1123.
        sellout (Union[Unset, bool]): Was the match a sellout? Example: True.
        social (Union['MatchModelSocialMedia', None, Unset]): Social Media contacts
        environmental (Union['MatchModelEnvironmentalDetails', None, Unset]): Details about the environment during the
            fixture
        duration (Union[None, Unset, int]): Length, in minutes, of the match Example: 48.
        duration_full (Union[None, Unset, int]): Full duration including breaks Example: 180.
        ticket_url (Union[None, Unset, str]): Ticket URL
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        stage (Union[Unset, MatchModelStage]): The stage that is related to this record
        series_code (Union[None, Unset, str]): A unique code for the season series. (Unique for season) Example: ST1.
        series (Union[Unset, MatchModelSeries]): The season series that is related to this record
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        pool (Union[Unset, MatchModelPool]): The pool that is related to this record
        round_code (Union[None, Unset, str]): A unique code for the round. (Unique for season) Example: RN1.
        round_ (Union[Unset, MatchModelRound]): The ~ROUND~ that is related to this record
        round_number (Union[None, Unset, str]): The number given to the round Example: 1.
        live_data_available (Union[Unset, bool]): Is live data available? Example: True.
        live_video_available (Union[Unset, bool]): Is live video available ? Example: True.
        fixture_type (Union[Unset, MatchModelFixtureType]): Type of match
            >- `ALL_STAR` All Star
            >- `DEMONSTRATION` Demonstration
            >- `FINAL` Final
            >- `FRIENDLY` Friendly
            >- `PLAYOFF` Playoff
            >- `PRESEASON` Pre Season
            >- `REGULAR` Regular
             Example: REGULAR.
        maximum_period_type_used (Union[MatchModelMaximumPeriodTypeUsedType1, MatchModelMaximumPeriodTypeUsedType2Type1,
            MatchModelMaximumPeriodTypeUsedType3Type1, None, Unset]): Maximum Period Type Used
            >- None None
            >- `EXTRA_TIME` Extra Time
            >- `OVERTIME` Overtime
            >- `REGULAR` Regular
            >- `SHOOTOUT` Shoot-Out
             Example: REGULAR.
        competitor_type (Union[Unset, MatchModelCompetitorType]): The type of competitors in this match
            >- `ENTITY` Entity
            >- `PERSON` Person
             Example: ENTITY.
        competitors (Union[None, Unset, list['MatchModelMatchCompetitor']]): Array of match competitors
        venue_id (Union[None, UUID, Unset]): The unique identifier of the venue Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        venue (Union[Unset, MatchModelVenue]): The venue that this match belongs to
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        profile_id (Union[None, UUID, Unset]): The profile that this match belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_profile (Union[Unset, MatchModelFixtureProfile]): The profile that this match belongs to
        include_in_standings (Union[Unset, bool]): Include the match in the standings calculation? Default: True.
            Example: True.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        estimated_finish_time_utc (Union[Unset, datetime.datetime]): Estimated end of match
        feature_match (Union[Unset, bool]): Is this match a featured match? Example: True.
        series_fixture_number (Union[None, Unset, int]): The number of the match in a series of matches Example: 1.
        discipline (Union[MatchModelDisciplineType1, MatchModelDisciplineType2Type1, MatchModelDisciplineType3Type1,
            None, Unset]): match discipline
            >- None None
            >- `INDOOR` Indoor
            >- `OUTDOOR` Outdoor
             Example: INDOOR.
        broadcasts (Union[Unset, list[Union['MatchModelBroadcasts', None]]]):
    """

    fixture_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "MatchModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "MatchModelSeason"] = UNSET
    practice_drill_type: Union[
        MatchModelPracticeDrillTypeType1,
        MatchModelPracticeDrillTypeType2Type1,
        MatchModelPracticeDrillTypeType3Type1,
        None,
        Unset,
    ] = UNSET
    international_reference: Union[None, Unset, str] = UNSET
    status: Union[Unset, MatchModelStatus] = MatchModelStatus.SCHEDULED
    fixture_number: Union[None, Unset, int] = UNSET
    name_local: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    start_time_local: Union[None, Unset, datetime.datetime] = UNSET
    start_time_utc: Union[None, Unset, datetime.datetime] = UNSET
    finish_recording_time_utc: Union[Unset, datetime.datetime] = UNSET
    finish_recording_time_local: Union[Unset, datetime.datetime] = UNSET
    start_time_actual_utc: Union[None, Unset, datetime.datetime] = UNSET
    end_time_actual_utc: Union[None, Unset, datetime.datetime] = UNSET
    times_unconfirmed: Union[Unset, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    placing_if_won: Union[None, Unset, int] = UNSET
    placing_if_lost: Union[None, Unset, int] = UNSET
    attendance: Union[None, Unset, int] = UNSET
    sellout: Union[Unset, bool] = UNSET
    social: Union["MatchModelSocialMedia", None, Unset] = UNSET
    environmental: Union["MatchModelEnvironmentalDetails", None, Unset] = UNSET
    duration: Union[None, Unset, int] = UNSET
    duration_full: Union[None, Unset, int] = UNSET
    ticket_url: Union[None, Unset, str] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    stage: Union[Unset, "MatchModelStage"] = UNSET
    series_code: Union[None, Unset, str] = UNSET
    series: Union[Unset, "MatchModelSeries"] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    pool: Union[Unset, "MatchModelPool"] = UNSET
    round_code: Union[None, Unset, str] = UNSET
    round_: Union[Unset, "MatchModelRound"] = UNSET
    round_number: Union[None, Unset, str] = UNSET
    live_data_available: Union[Unset, bool] = UNSET
    live_video_available: Union[Unset, bool] = UNSET
    fixture_type: Union[Unset, MatchModelFixtureType] = UNSET
    maximum_period_type_used: Union[
        MatchModelMaximumPeriodTypeUsedType1,
        MatchModelMaximumPeriodTypeUsedType2Type1,
        MatchModelMaximumPeriodTypeUsedType3Type1,
        None,
        Unset,
    ] = UNSET
    competitor_type: Union[Unset, MatchModelCompetitorType] = UNSET
    competitors: Union[None, Unset, list["MatchModelMatchCompetitor"]] = UNSET
    venue_id: Union[None, UUID, Unset] = UNSET
    venue: Union[Unset, "MatchModelVenue"] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    profile_id: Union[None, UUID, Unset] = UNSET
    fixture_profile: Union[Unset, "MatchModelFixtureProfile"] = UNSET
    include_in_standings: Union[Unset, bool] = True
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    estimated_finish_time_utc: Union[Unset, datetime.datetime] = UNSET
    feature_match: Union[Unset, bool] = UNSET
    series_fixture_number: Union[None, Unset, int] = UNSET
    discipline: Union[
        MatchModelDisciplineType1,
        MatchModelDisciplineType2Type1,
        MatchModelDisciplineType3Type1,
        None,
        Unset,
    ] = UNSET
    broadcasts: Union[Unset, list[Union["MatchModelBroadcasts", None]]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.match_model_broadcasts import MatchModelBroadcasts
        from ..models.match_model_environmental_details import (
            MatchModelEnvironmentalDetails,
        )
        from ..models.match_model_social_media import MatchModelSocialMedia

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        practice_drill_type: Union[None, Unset, str]
        if isinstance(self.practice_drill_type, Unset):
            practice_drill_type = UNSET
        elif isinstance(self.practice_drill_type, MatchModelPracticeDrillTypeType1):
            practice_drill_type = self.practice_drill_type.value
        elif isinstance(
            self.practice_drill_type, MatchModelPracticeDrillTypeType2Type1
        ):
            practice_drill_type = self.practice_drill_type.value
        elif isinstance(
            self.practice_drill_type, MatchModelPracticeDrillTypeType3Type1
        ):
            practice_drill_type = self.practice_drill_type.value
        else:
            practice_drill_type = self.practice_drill_type

        international_reference: Union[None, Unset, str]
        if isinstance(self.international_reference, Unset):
            international_reference = UNSET
        else:
            international_reference = self.international_reference

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        fixture_number: Union[None, Unset, int]
        if isinstance(self.fixture_number, Unset):
            fixture_number = UNSET
        else:
            fixture_number = self.fixture_number

        name_local: Union[None, Unset, str]
        if isinstance(self.name_local, Unset):
            name_local = UNSET
        else:
            name_local = self.name_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        start_time_local: Union[None, Unset, str]
        if isinstance(self.start_time_local, Unset):
            start_time_local = UNSET
        elif isinstance(self.start_time_local, datetime.datetime):
            start_time_local = self.start_time_local.isoformat()
        else:
            start_time_local = self.start_time_local

        start_time_utc: Union[None, Unset, str]
        if isinstance(self.start_time_utc, Unset):
            start_time_utc = UNSET
        elif isinstance(self.start_time_utc, datetime.datetime):
            start_time_utc = self.start_time_utc.isoformat()
        else:
            start_time_utc = self.start_time_utc

        finish_recording_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.finish_recording_time_utc, Unset):
            finish_recording_time_utc = self.finish_recording_time_utc.isoformat()

        finish_recording_time_local: Union[Unset, str] = UNSET
        if not isinstance(self.finish_recording_time_local, Unset):
            finish_recording_time_local = self.finish_recording_time_local.isoformat()

        start_time_actual_utc: Union[None, Unset, str]
        if isinstance(self.start_time_actual_utc, Unset):
            start_time_actual_utc = UNSET
        elif isinstance(self.start_time_actual_utc, datetime.datetime):
            start_time_actual_utc = self.start_time_actual_utc.isoformat()
        else:
            start_time_actual_utc = self.start_time_actual_utc

        end_time_actual_utc: Union[None, Unset, str]
        if isinstance(self.end_time_actual_utc, Unset):
            end_time_actual_utc = UNSET
        elif isinstance(self.end_time_actual_utc, datetime.datetime):
            end_time_actual_utc = self.end_time_actual_utc.isoformat()
        else:
            end_time_actual_utc = self.end_time_actual_utc

        times_unconfirmed = self.times_unconfirmed

        locked = self.locked

        placing_if_won: Union[None, Unset, int]
        if isinstance(self.placing_if_won, Unset):
            placing_if_won = UNSET
        else:
            placing_if_won = self.placing_if_won

        placing_if_lost: Union[None, Unset, int]
        if isinstance(self.placing_if_lost, Unset):
            placing_if_lost = UNSET
        else:
            placing_if_lost = self.placing_if_lost

        attendance: Union[None, Unset, int]
        if isinstance(self.attendance, Unset):
            attendance = UNSET
        else:
            attendance = self.attendance

        sellout = self.sellout

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, MatchModelSocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        environmental: Union[None, Unset, dict[str, Any]]
        if isinstance(self.environmental, Unset):
            environmental = UNSET
        elif isinstance(self.environmental, MatchModelEnvironmentalDetails):
            environmental = self.environmental.to_dict()
        else:
            environmental = self.environmental

        duration: Union[None, Unset, int]
        if isinstance(self.duration, Unset):
            duration = UNSET
        else:
            duration = self.duration

        duration_full: Union[None, Unset, int]
        if isinstance(self.duration_full, Unset):
            duration_full = UNSET
        else:
            duration_full = self.duration_full

        ticket_url: Union[None, Unset, str]
        if isinstance(self.ticket_url, Unset):
            ticket_url = UNSET
        else:
            ticket_url = self.ticket_url

        stage_code: Union[None, Unset, str]
        if isinstance(self.stage_code, Unset):
            stage_code = UNSET
        else:
            stage_code = self.stage_code

        stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        series_code: Union[None, Unset, str]
        if isinstance(self.series_code, Unset):
            series_code = UNSET
        else:
            series_code = self.series_code

        series: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.series, Unset):
            series = self.series.to_dict()

        pool_code: Union[None, Unset, str]
        if isinstance(self.pool_code, Unset):
            pool_code = UNSET
        else:
            pool_code = self.pool_code

        pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.to_dict()

        round_code: Union[None, Unset, str]
        if isinstance(self.round_code, Unset):
            round_code = UNSET
        else:
            round_code = self.round_code

        round_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.round_, Unset):
            round_ = self.round_.to_dict()

        round_number: Union[None, Unset, str]
        if isinstance(self.round_number, Unset):
            round_number = UNSET
        else:
            round_number = self.round_number

        live_data_available = self.live_data_available

        live_video_available = self.live_video_available

        fixture_type: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_type, Unset):
            fixture_type = self.fixture_type.value

        maximum_period_type_used: Union[None, Unset, str]
        if isinstance(self.maximum_period_type_used, Unset):
            maximum_period_type_used = UNSET
        elif isinstance(
            self.maximum_period_type_used, MatchModelMaximumPeriodTypeUsedType1
        ):
            maximum_period_type_used = self.maximum_period_type_used.value
        elif isinstance(
            self.maximum_period_type_used, MatchModelMaximumPeriodTypeUsedType2Type1
        ):
            maximum_period_type_used = self.maximum_period_type_used.value
        elif isinstance(
            self.maximum_period_type_used, MatchModelMaximumPeriodTypeUsedType3Type1
        ):
            maximum_period_type_used = self.maximum_period_type_used.value
        else:
            maximum_period_type_used = self.maximum_period_type_used

        competitor_type: Union[Unset, str] = UNSET
        if not isinstance(self.competitor_type, Unset):
            competitor_type = self.competitor_type.value

        competitors: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.competitors, Unset):
            competitors = UNSET
        elif isinstance(self.competitors, list):
            competitors = []
            for competitors_type_0_item_data in self.competitors:
                competitors_type_0_item = competitors_type_0_item_data.to_dict()
                competitors.append(competitors_type_0_item)

        else:
            competitors = self.competitors

        venue_id: Union[None, Unset, str]
        if isinstance(self.venue_id, Unset):
            venue_id = UNSET
        elif isinstance(self.venue_id, UUID):
            venue_id = str(self.venue_id)
        else:
            venue_id = self.venue_id

        venue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        profile_id: Union[None, Unset, str]
        if isinstance(self.profile_id, Unset):
            profile_id = UNSET
        elif isinstance(self.profile_id, UUID):
            profile_id = str(self.profile_id)
        else:
            profile_id = self.profile_id

        fixture_profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture_profile, Unset):
            fixture_profile = self.fixture_profile.to_dict()

        include_in_standings = self.include_in_standings

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        estimated_finish_time_utc: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_finish_time_utc, Unset):
            estimated_finish_time_utc = self.estimated_finish_time_utc.isoformat()

        feature_match = self.feature_match

        series_fixture_number: Union[None, Unset, int]
        if isinstance(self.series_fixture_number, Unset):
            series_fixture_number = UNSET
        else:
            series_fixture_number = self.series_fixture_number

        discipline: Union[None, Unset, str]
        if isinstance(self.discipline, Unset):
            discipline = UNSET
        elif isinstance(self.discipline, MatchModelDisciplineType1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, MatchModelDisciplineType2Type1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, MatchModelDisciplineType3Type1):
            discipline = self.discipline.value
        else:
            discipline = self.discipline

        broadcasts: Union[Unset, list[Union[None, dict[str, Any]]]] = UNSET
        if not isinstance(self.broadcasts, Unset):
            broadcasts = []
            for broadcasts_item_data in self.broadcasts:
                broadcasts_item: Union[None, dict[str, Any]]
                if isinstance(broadcasts_item_data, MatchModelBroadcasts):
                    broadcasts_item = broadcasts_item_data.to_dict()
                else:
                    broadcasts_item = broadcasts_item_data
                broadcasts.append(broadcasts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if practice_drill_type is not UNSET:
            field_dict["practiceDrillType"] = practice_drill_type
        if international_reference is not UNSET:
            field_dict["internationalReference"] = international_reference
        if status is not UNSET:
            field_dict["status"] = status
        if fixture_number is not UNSET:
            field_dict["fixtureNumber"] = fixture_number
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if start_time_local is not UNSET:
            field_dict["startTimeLocal"] = start_time_local
        if start_time_utc is not UNSET:
            field_dict["startTimeUTC"] = start_time_utc
        if finish_recording_time_utc is not UNSET:
            field_dict["finishRecordingTimeUTC"] = finish_recording_time_utc
        if finish_recording_time_local is not UNSET:
            field_dict["finishRecordingTimeLocal"] = finish_recording_time_local
        if start_time_actual_utc is not UNSET:
            field_dict["startTimeActualUTC"] = start_time_actual_utc
        if end_time_actual_utc is not UNSET:
            field_dict["endTimeActualUTC"] = end_time_actual_utc
        if times_unconfirmed is not UNSET:
            field_dict["timesUnconfirmed"] = times_unconfirmed
        if locked is not UNSET:
            field_dict["locked"] = locked
        if placing_if_won is not UNSET:
            field_dict["placingIfWon"] = placing_if_won
        if placing_if_lost is not UNSET:
            field_dict["placingIfLost"] = placing_if_lost
        if attendance is not UNSET:
            field_dict["attendance"] = attendance
        if sellout is not UNSET:
            field_dict["sellout"] = sellout
        if social is not UNSET:
            field_dict["social"] = social
        if environmental is not UNSET:
            field_dict["environmental"] = environmental
        if duration is not UNSET:
            field_dict["duration"] = duration
        if duration_full is not UNSET:
            field_dict["durationFull"] = duration_full
        if ticket_url is not UNSET:
            field_dict["ticketURL"] = ticket_url
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if stage is not UNSET:
            field_dict["stage"] = stage
        if series_code is not UNSET:
            field_dict["seriesCode"] = series_code
        if series is not UNSET:
            field_dict["series"] = series
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if pool is not UNSET:
            field_dict["pool"] = pool
        if round_code is not UNSET:
            field_dict["roundCode"] = round_code
        if round_ is not UNSET:
            field_dict["round"] = round_
        if round_number is not UNSET:
            field_dict["roundNumber"] = round_number
        if live_data_available is not UNSET:
            field_dict["liveDataAvailable"] = live_data_available
        if live_video_available is not UNSET:
            field_dict["liveVideoAvailable"] = live_video_available
        if fixture_type is not UNSET:
            field_dict["fixtureType"] = fixture_type
        if maximum_period_type_used is not UNSET:
            field_dict["maximumPeriodTypeUsed"] = maximum_period_type_used
        if competitor_type is not UNSET:
            field_dict["competitorType"] = competitor_type
        if competitors is not UNSET:
            field_dict["competitors"] = competitors
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id
        if venue is not UNSET:
            field_dict["venue"] = venue
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if fixture_profile is not UNSET:
            field_dict["fixtureProfile"] = fixture_profile
        if include_in_standings is not UNSET:
            field_dict["includeInStandings"] = include_in_standings
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if estimated_finish_time_utc is not UNSET:
            field_dict["estimatedFinishTimeUTC"] = estimated_finish_time_utc
        if feature_match is not UNSET:
            field_dict["featureMatch"] = feature_match
        if series_fixture_number is not UNSET:
            field_dict["seriesFixtureNumber"] = series_fixture_number
        if discipline is not UNSET:
            field_dict["discipline"] = discipline
        if broadcasts is not UNSET:
            field_dict["broadcasts"] = broadcasts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_model_broadcasts import MatchModelBroadcasts
        from ..models.match_model_environmental_details import (
            MatchModelEnvironmentalDetails,
        )
        from ..models.match_model_fixture_profile import MatchModelFixtureProfile
        from ..models.match_model_match_competitor import MatchModelMatchCompetitor
        from ..models.match_model_organization import MatchModelOrganization
        from ..models.match_model_pool import MatchModelPool
        from ..models.match_model_round import MatchModelRound
        from ..models.match_model_season import MatchModelSeason
        from ..models.match_model_series import MatchModelSeries
        from ..models.match_model_social_media import MatchModelSocialMedia
        from ..models.match_model_stage import MatchModelStage
        from ..models.match_model_venue import MatchModelVenue

        d = dict(src_dict)
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, MatchModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = MatchModelOrganization.from_dict(_organization)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, MatchModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = MatchModelSeason.from_dict(_season)

        def _parse_practice_drill_type(
            data: object,
        ) -> Union[
            MatchModelPracticeDrillTypeType1,
            MatchModelPracticeDrillTypeType2Type1,
            MatchModelPracticeDrillTypeType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                practice_drill_type_type_1 = MatchModelPracticeDrillTypeType1(data)

                return practice_drill_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                practice_drill_type_type_2_type_1 = (
                    MatchModelPracticeDrillTypeType2Type1(data)
                )

                return practice_drill_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                practice_drill_type_type_3_type_1 = (
                    MatchModelPracticeDrillTypeType3Type1(data)
                )

                return practice_drill_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    MatchModelPracticeDrillTypeType1,
                    MatchModelPracticeDrillTypeType2Type1,
                    MatchModelPracticeDrillTypeType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        practice_drill_type = _parse_practice_drill_type(
            d.pop("practiceDrillType", UNSET)
        )

        def _parse_international_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        international_reference = _parse_international_reference(
            d.pop("internationalReference", UNSET)
        )

        _status = d.pop("status", UNSET)
        status: Union[Unset, MatchModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MatchModelStatus(_status)

        def _parse_fixture_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fixture_number = _parse_fixture_number(d.pop("fixtureNumber", UNSET))

        def _parse_name_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_local = _parse_name_local(d.pop("nameLocal", UNSET))

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_start_time_local(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_local_type_0 = isoparse(data)

                return start_time_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_time_local = _parse_start_time_local(d.pop("startTimeLocal", UNSET))

        def _parse_start_time_utc(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_utc_type_0 = isoparse(data)

                return start_time_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_time_utc = _parse_start_time_utc(d.pop("startTimeUTC", UNSET))

        _finish_recording_time_utc = d.pop("finishRecordingTimeUTC", UNSET)
        finish_recording_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_finish_recording_time_utc, Unset):
            finish_recording_time_utc = UNSET
        else:
            finish_recording_time_utc = isoparse(_finish_recording_time_utc)

        _finish_recording_time_local = d.pop("finishRecordingTimeLocal", UNSET)
        finish_recording_time_local: Union[Unset, datetime.datetime]
        if isinstance(_finish_recording_time_local, Unset):
            finish_recording_time_local = UNSET
        else:
            finish_recording_time_local = isoparse(_finish_recording_time_local)

        def _parse_start_time_actual_utc(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_time_actual_utc_type_0 = isoparse(data)

                return start_time_actual_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_time_actual_utc = _parse_start_time_actual_utc(
            d.pop("startTimeActualUTC", UNSET)
        )

        def _parse_end_time_actual_utc(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_time_actual_utc_type_0 = isoparse(data)

                return end_time_actual_utc_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_time_actual_utc = _parse_end_time_actual_utc(
            d.pop("endTimeActualUTC", UNSET)
        )

        times_unconfirmed = d.pop("timesUnconfirmed", UNSET)

        locked = d.pop("locked", UNSET)

        def _parse_placing_if_won(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        placing_if_won = _parse_placing_if_won(d.pop("placingIfWon", UNSET))

        def _parse_placing_if_lost(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        placing_if_lost = _parse_placing_if_lost(d.pop("placingIfLost", UNSET))

        def _parse_attendance(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        attendance = _parse_attendance(d.pop("attendance", UNSET))

        sellout = d.pop("sellout", UNSET)

        def _parse_social(data: object) -> Union["MatchModelSocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = MatchModelSocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MatchModelSocialMedia", None, Unset], data)

        social = _parse_social(d.pop("social", UNSET))

        def _parse_environmental(
            data: object,
        ) -> Union["MatchModelEnvironmentalDetails", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                environmental_type_0 = MatchModelEnvironmentalDetails.from_dict(data)

                return environmental_type_0
            except:  # noqa: E722
                pass
            return cast(Union["MatchModelEnvironmentalDetails", None, Unset], data)

        environmental = _parse_environmental(d.pop("environmental", UNSET))

        def _parse_duration(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration = _parse_duration(d.pop("duration", UNSET))

        def _parse_duration_full(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration_full = _parse_duration_full(d.pop("durationFull", UNSET))

        def _parse_ticket_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ticket_url = _parse_ticket_url(d.pop("ticketURL", UNSET))

        def _parse_stage_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage_code = _parse_stage_code(d.pop("stageCode", UNSET))

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, MatchModelStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = MatchModelStage.from_dict(_stage)

        def _parse_series_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        series_code = _parse_series_code(d.pop("seriesCode", UNSET))

        _series = d.pop("series", UNSET)
        series: Union[Unset, MatchModelSeries]
        if isinstance(_series, Unset):
            series = UNSET
        else:
            series = MatchModelSeries.from_dict(_series)

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, MatchModelPool]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = MatchModelPool.from_dict(_pool)

        def _parse_round_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_code = _parse_round_code(d.pop("roundCode", UNSET))

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, MatchModelRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = MatchModelRound.from_dict(_round_)

        def _parse_round_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_number = _parse_round_number(d.pop("roundNumber", UNSET))

        live_data_available = d.pop("liveDataAvailable", UNSET)

        live_video_available = d.pop("liveVideoAvailable", UNSET)

        _fixture_type = d.pop("fixtureType", UNSET)
        fixture_type: Union[Unset, MatchModelFixtureType]
        if isinstance(_fixture_type, Unset):
            fixture_type = UNSET
        else:
            fixture_type = MatchModelFixtureType(_fixture_type)

        def _parse_maximum_period_type_used(
            data: object,
        ) -> Union[
            MatchModelMaximumPeriodTypeUsedType1,
            MatchModelMaximumPeriodTypeUsedType2Type1,
            MatchModelMaximumPeriodTypeUsedType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maximum_period_type_used_type_1 = MatchModelMaximumPeriodTypeUsedType1(
                    data
                )

                return maximum_period_type_used_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maximum_period_type_used_type_2_type_1 = (
                    MatchModelMaximumPeriodTypeUsedType2Type1(data)
                )

                return maximum_period_type_used_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maximum_period_type_used_type_3_type_1 = (
                    MatchModelMaximumPeriodTypeUsedType3Type1(data)
                )

                return maximum_period_type_used_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    MatchModelMaximumPeriodTypeUsedType1,
                    MatchModelMaximumPeriodTypeUsedType2Type1,
                    MatchModelMaximumPeriodTypeUsedType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        maximum_period_type_used = _parse_maximum_period_type_used(
            d.pop("maximumPeriodTypeUsed", UNSET)
        )

        _competitor_type = d.pop("competitorType", UNSET)
        competitor_type: Union[Unset, MatchModelCompetitorType]
        if isinstance(_competitor_type, Unset):
            competitor_type = UNSET
        else:
            competitor_type = MatchModelCompetitorType(_competitor_type)

        def _parse_competitors(
            data: object,
        ) -> Union[None, Unset, list["MatchModelMatchCompetitor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                competitors_type_0 = []
                _competitors_type_0 = data
                for competitors_type_0_item_data in _competitors_type_0:
                    competitors_type_0_item = MatchModelMatchCompetitor.from_dict(
                        competitors_type_0_item_data
                    )

                    competitors_type_0.append(competitors_type_0_item)

                return competitors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MatchModelMatchCompetitor"]], data)

        competitors = _parse_competitors(d.pop("competitors", UNSET))

        def _parse_venue_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                venue_id_type_0 = UUID(data)

                return venue_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        venue_id = _parse_venue_id(d.pop("venueId", UNSET))

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, MatchModelVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = MatchModelVenue.from_dict(_venue)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_profile_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                profile_id_type_0 = UUID(data)

                return profile_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        profile_id = _parse_profile_id(d.pop("profileId", UNSET))

        _fixture_profile = d.pop("fixtureProfile", UNSET)
        fixture_profile: Union[Unset, MatchModelFixtureProfile]
        if isinstance(_fixture_profile, Unset):
            fixture_profile = UNSET
        else:
            fixture_profile = MatchModelFixtureProfile.from_dict(_fixture_profile)

        include_in_standings = d.pop("includeInStandings", UNSET)

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

        _estimated_finish_time_utc = d.pop("estimatedFinishTimeUTC", UNSET)
        estimated_finish_time_utc: Union[Unset, datetime.datetime]
        if isinstance(_estimated_finish_time_utc, Unset):
            estimated_finish_time_utc = UNSET
        else:
            estimated_finish_time_utc = isoparse(_estimated_finish_time_utc)

        feature_match = d.pop("featureMatch", UNSET)

        def _parse_series_fixture_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        series_fixture_number = _parse_series_fixture_number(
            d.pop("seriesFixtureNumber", UNSET)
        )

        def _parse_discipline(
            data: object,
        ) -> Union[
            MatchModelDisciplineType1,
            MatchModelDisciplineType2Type1,
            MatchModelDisciplineType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_1 = MatchModelDisciplineType1(data)

                return discipline_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_2_type_1 = MatchModelDisciplineType2Type1(data)

                return discipline_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_3_type_1 = MatchModelDisciplineType3Type1(data)

                return discipline_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    MatchModelDisciplineType1,
                    MatchModelDisciplineType2Type1,
                    MatchModelDisciplineType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        discipline = _parse_discipline(d.pop("discipline", UNSET))

        broadcasts = []
        _broadcasts = d.pop("broadcasts", UNSET)
        for broadcasts_item_data in _broadcasts or []:

            def _parse_broadcasts_item(
                data: object,
            ) -> Union["MatchModelBroadcasts", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    broadcasts_item_type_0 = MatchModelBroadcasts.from_dict(data)

                    return broadcasts_item_type_0
                except:  # noqa: E722
                    pass
                return cast(Union["MatchModelBroadcasts", None], data)

            broadcasts_item = _parse_broadcasts_item(broadcasts_item_data)

            broadcasts.append(broadcasts_item)

        match_model = cls(
            fixture_id=fixture_id,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            practice_drill_type=practice_drill_type,
            international_reference=international_reference,
            status=status,
            fixture_number=fixture_number,
            name_local=name_local,
            name_latin=name_latin,
            start_time_local=start_time_local,
            start_time_utc=start_time_utc,
            finish_recording_time_utc=finish_recording_time_utc,
            finish_recording_time_local=finish_recording_time_local,
            start_time_actual_utc=start_time_actual_utc,
            end_time_actual_utc=end_time_actual_utc,
            times_unconfirmed=times_unconfirmed,
            locked=locked,
            placing_if_won=placing_if_won,
            placing_if_lost=placing_if_lost,
            attendance=attendance,
            sellout=sellout,
            social=social,
            environmental=environmental,
            duration=duration,
            duration_full=duration_full,
            ticket_url=ticket_url,
            stage_code=stage_code,
            stage=stage,
            series_code=series_code,
            series=series,
            pool_code=pool_code,
            pool=pool,
            round_code=round_code,
            round_=round_,
            round_number=round_number,
            live_data_available=live_data_available,
            live_video_available=live_video_available,
            fixture_type=fixture_type,
            maximum_period_type_used=maximum_period_type_used,
            competitor_type=competitor_type,
            competitors=competitors,
            venue_id=venue_id,
            venue=venue,
            external_id=external_id,
            profile_id=profile_id,
            fixture_profile=fixture_profile,
            include_in_standings=include_in_standings,
            updated=updated,
            added=added,
            estimated_finish_time_utc=estimated_finish_time_utc,
            feature_match=feature_match,
            series_fixture_number=series_fixture_number,
            discipline=discipline,
            broadcasts=broadcasts,
        )

        return match_model
