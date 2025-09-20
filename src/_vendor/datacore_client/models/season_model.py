import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_model_age_group import SeasonModelAgeGroup
from ..models.season_model_discipline_type_1 import SeasonModelDisciplineType1
from ..models.season_model_discipline_type_2_type_1 import SeasonModelDisciplineType2Type1
from ..models.season_model_discipline_type_3_type_1 import SeasonModelDisciplineType3Type1
from ..models.season_model_event_type import SeasonModelEventType
from ..models.season_model_gender import SeasonModelGender
from ..models.season_model_representation import SeasonModelRepresentation
from ..models.season_model_season_type import SeasonModelSeasonType
from ..models.season_model_standard import SeasonModelStandard
from ..models.season_model_status import SeasonModelStatus
from ..models.season_model_video_production import SeasonModelVideoProduction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images_model import ImagesModel
    from ..models.season_model_competition import SeasonModelCompetition
    from ..models.season_model_fixture_profile import SeasonModelFixtureProfile
    from ..models.season_model_leaders_criteria import SeasonModelLeadersCriteria
    from ..models.season_model_organization import SeasonModelOrganization
    from ..models.season_model_promotion_relegation_rules_type_0_item import (
        SeasonModelPromotionRelegationRulesType0Item,
    )
    from ..models.season_model_season_configuration import SeasonModelSeasonConfiguration
    from ..models.season_model_seasonroster_configuration import SeasonModelSEASONROSTERConfiguration
    from ..models.season_model_social_media import SeasonModelSocialMedia
    from ..models.season_model_standing_configuration import SeasonModelStandingConfiguration


T = TypeVar("T", bound="SeasonModel")


@_attrs_define
class SeasonModel:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonModelOrganization]): The organization that this season belongs to
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, SeasonModelCompetition]): The competition that this season belongs to
        leader_criteria_id (Union[None, UUID, Unset]): The unique identifier of the ~LeaderCriteria~ Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        leaders_criteria (Union[Unset, SeasonModelLeadersCriteria]): The ~LeaderCriteria~ linked to this record
        international_reference (Union[None, Unset, str]): The international reference for this season given by the
            sport governing body Example: CA3243-3.
        event_type (Union[Unset, SeasonModelEventType]): Primary Type of Matches
            >- `FIXTURE` Fixture
            >- `PRACTICE` Practice
             Default: SeasonModelEventType.FIXTURE. Example: FIXTURE.
        season_type (Union[Unset, SeasonModelSeasonType]): The type of matches added to this season
            >- `MULTI_YEAR_HISTORICAL` Mulit-Year Historical
            >- `ONE_OFF` One off
            >- `PRESEASON` Pre Season
            >- `SEASON` Season
            >- `TOURNAMENT` Tournament
             Example: SEASON.
        year (Union[Unset, int]): Year of the season Example: 2019.
        grade (Union[None, Unset, str]): The playing grade of the matches in this season Example: A.
        status (Union[Unset, SeasonModelStatus]): Status
            >- `ACTIVE` Active
            >- `COMPLETE` Complete
            >- `DRAFT` Draft
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        include_in_statistics (Union[Unset, bool]): Include this season in calculated statistics? Default: True.
            Example: True.
        live_video_available (Union[Unset, bool]): If no 'liveVideoAvailable' flag passed to a new match this value is
            used Example: True.
        live_data_available (Union[Unset, bool]): If no 'liveDataAvailable' flag passed to a new match this value is
            used Example: True.
        duration_full (Union[None, Unset, int]): If no 'durationFull' is passed to a new match this value is used
            Default: 180. Example: 180.
        discipline (Union[None, SeasonModelDisciplineType1, SeasonModelDisciplineType2Type1,
            SeasonModelDisciplineType3Type1, Unset]): If no 'discipline' is passed to a new match this value is used
            >- None None
            >- `INDOOR` Indoor
            >- `OUTDOOR` Outdoor
             Example: INDOOR.
        name_local (Union[Unset, str]): The name of the season in the [local](#section/Introduction/Character-Sets-and-
            Names) language Example: Test season.
        name_latin (Union[None, Unset, str]): The name of the season in [latin](#section/Introduction/Character-Sets-
            and-Names) characters Example: Test season.
        name_short_local (Union[None, Unset, str]): The abbreviated name of the season in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Test short local.
        name_short_latin (Union[None, Unset, str]): The abbreviated name of the season in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Test short latin.
        start_date (Union[Unset, datetime.date]): Season start date Example: 2016-09-08.
        end_date (Union[None, Unset, datetime.date]): Season end date Example: 2016-09-08.
        gender (Union[Unset, SeasonModelGender]): The gender of the participants in the season
            >- `FEMALE` Female
            >- `MALE` Male
            >- `MIXED` Mixed
            >- `UNKNOWN` Unknown
             Example: MALE.
        age_group (Union[Unset, SeasonModelAgeGroup]): The age group of the season
            >- `JUNIOR` Junior
            >- `MASTERS` Masters
            >- `SENIOR` Senior
            >- `UNDER_15` Under 15
            >- `UNDER_16` Under 16
            >- `UNDER_17` Under 17
            >- `UNDER_18` Under 18
            >- `UNDER_19` Under 19
            >- `UNDER_20` Under 20
            >- `UNDER_21` Under 21
            >- `UNDER_22` Under 22
            >- `UNDER_23` Under 23
            >- `YOUTH` Youth
             Example: SENIOR.
        standard (Union[Unset, SeasonModelStandard]): The playing standard of the season
            >- `ELITE` Professional/elite organisation
            >- `FRIENDLY` International Friendly
            >- `GRASS_ROOT` Normal
            >- `HISTORICAL_BASELINE` Historical Baseline
            >- `INTERNATIONAL` International
            >- `NONCONTINENTAL_CHAMPIONSHIP` Non-continental Championship
            >- `OLYMPIC` Olympics
            >- `REGION` Regional
            >- `TIER2` lesser standard than elite
            >- `TIER3` lesser standard than tier 2
            >- `WORLD_CHAMPIONSHIP` World Championship
            >- `ZONE_CHAMPIONSHIP` International Zone Championship
             Example: ELITE.
        representation (Union[Unset, SeasonModelRepresentation]): What level are the competitors representing
            >- `CLUB` Club
            >- `COUNTRY` Country
            >- `PERSON` Person
            >- `REGION` Region
            >- `STATE` State
             Example: CLUB.
        standing_configuration_id (Union[None, UUID, Unset]): The unique identifier of the ~standingConfiguration~
            Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        standing_configuration (Union[Unset, SeasonModelStandingConfiguration]): The ~standingConfiguration~ that this
            season belongs to
        lock_standings (Union[Unset, bool]): Is the standings generation locked ? Example: True.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        social (Union['SeasonModelSocialMedia', None, Unset]): Social Media contacts
        configuration (Union['SeasonModelSeasonConfiguration', None, Unset]): Season Configuration settings
        profile_id (Union[None, UUID, Unset]): The profile that this season belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_profile (Union[Unset, SeasonModelFixtureProfile]): The profile that this season belongs to
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        images (Union[Unset, list['ImagesModel']]):
        video_production (Union[Unset, SeasonModelVideoProduction]): Data synchronization strategy with video production
            systems
            >- `AUTOMATED` Automated
            >- `MANUAL` Manual
            >- `NONE` None
             Default: SeasonModelVideoProduction.NONE. Example: AUTOMATED.
        promotion_relegation_rules (Union[None, Unset, list['SeasonModelPromotionRelegationRulesType0Item']]):
        roster_configuration (Union['SeasonModelSEASONROSTERConfiguration', None, Unset]): Configuration for the SEASON
            ROSTER
    """

    season_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonModelOrganization"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "SeasonModelCompetition"] = UNSET
    leader_criteria_id: Union[None, UUID, Unset] = UNSET
    leaders_criteria: Union[Unset, "SeasonModelLeadersCriteria"] = UNSET
    international_reference: Union[None, Unset, str] = UNSET
    event_type: Union[Unset, SeasonModelEventType] = SeasonModelEventType.FIXTURE
    season_type: Union[Unset, SeasonModelSeasonType] = UNSET
    year: Union[Unset, int] = UNSET
    grade: Union[None, Unset, str] = UNSET
    status: Union[Unset, SeasonModelStatus] = UNSET
    include_in_statistics: Union[Unset, bool] = True
    live_video_available: Union[Unset, bool] = UNSET
    live_data_available: Union[Unset, bool] = UNSET
    duration_full: Union[None, Unset, int] = 180
    discipline: Union[
        None, SeasonModelDisciplineType1, SeasonModelDisciplineType2Type1, SeasonModelDisciplineType3Type1, Unset
    ] = UNSET
    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    name_short_local: Union[None, Unset, str] = UNSET
    name_short_latin: Union[None, Unset, str] = UNSET
    start_date: Union[Unset, datetime.date] = UNSET
    end_date: Union[None, Unset, datetime.date] = UNSET
    gender: Union[Unset, SeasonModelGender] = UNSET
    age_group: Union[Unset, SeasonModelAgeGroup] = UNSET
    standard: Union[Unset, SeasonModelStandard] = UNSET
    representation: Union[Unset, SeasonModelRepresentation] = UNSET
    standing_configuration_id: Union[None, UUID, Unset] = UNSET
    standing_configuration: Union[Unset, "SeasonModelStandingConfiguration"] = UNSET
    lock_standings: Union[Unset, bool] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    social: Union["SeasonModelSocialMedia", None, Unset] = UNSET
    configuration: Union["SeasonModelSeasonConfiguration", None, Unset] = UNSET
    profile_id: Union[None, UUID, Unset] = UNSET
    fixture_profile: Union[Unset, "SeasonModelFixtureProfile"] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    images: Union[Unset, list["ImagesModel"]] = UNSET
    video_production: Union[Unset, SeasonModelVideoProduction] = SeasonModelVideoProduction.NONE
    promotion_relegation_rules: Union[None, Unset, list["SeasonModelPromotionRelegationRulesType0Item"]] = UNSET
    roster_configuration: Union["SeasonModelSEASONROSTERConfiguration", None, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.season_model_season_configuration import SeasonModelSeasonConfiguration
        from ..models.season_model_seasonroster_configuration import SeasonModelSEASONROSTERConfiguration
        from ..models.season_model_social_media import SeasonModelSocialMedia

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        competition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        leader_criteria_id: Union[None, Unset, str]
        if isinstance(self.leader_criteria_id, Unset):
            leader_criteria_id = UNSET
        elif isinstance(self.leader_criteria_id, UUID):
            leader_criteria_id = str(self.leader_criteria_id)
        else:
            leader_criteria_id = self.leader_criteria_id

        leaders_criteria: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.leaders_criteria, Unset):
            leaders_criteria = self.leaders_criteria.to_dict()

        international_reference: Union[None, Unset, str]
        if isinstance(self.international_reference, Unset):
            international_reference = UNSET
        else:
            international_reference = self.international_reference

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        season_type: Union[Unset, str] = UNSET
        if not isinstance(self.season_type, Unset):
            season_type = self.season_type.value

        year = self.year

        grade: Union[None, Unset, str]
        if isinstance(self.grade, Unset):
            grade = UNSET
        else:
            grade = self.grade

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        include_in_statistics = self.include_in_statistics

        live_video_available = self.live_video_available

        live_data_available = self.live_data_available

        duration_full: Union[None, Unset, int]
        if isinstance(self.duration_full, Unset):
            duration_full = UNSET
        else:
            duration_full = self.duration_full

        discipline: Union[None, Unset, str]
        if isinstance(self.discipline, Unset):
            discipline = UNSET
        elif isinstance(self.discipline, SeasonModelDisciplineType1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, SeasonModelDisciplineType2Type1):
            discipline = self.discipline.value
        elif isinstance(self.discipline, SeasonModelDisciplineType3Type1):
            discipline = self.discipline.value
        else:
            discipline = self.discipline

        name_local = self.name_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        name_short_local: Union[None, Unset, str]
        if isinstance(self.name_short_local, Unset):
            name_short_local = UNSET
        else:
            name_short_local = self.name_short_local

        name_short_latin: Union[None, Unset, str]
        if isinstance(self.name_short_latin, Unset):
            name_short_latin = UNSET
        else:
            name_short_latin = self.name_short_latin

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        gender: Union[Unset, str] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.value

        age_group: Union[Unset, str] = UNSET
        if not isinstance(self.age_group, Unset):
            age_group = self.age_group.value

        standard: Union[Unset, str] = UNSET
        if not isinstance(self.standard, Unset):
            standard = self.standard.value

        representation: Union[Unset, str] = UNSET
        if not isinstance(self.representation, Unset):
            representation = self.representation.value

        standing_configuration_id: Union[None, Unset, str]
        if isinstance(self.standing_configuration_id, Unset):
            standing_configuration_id = UNSET
        elif isinstance(self.standing_configuration_id, UUID):
            standing_configuration_id = str(self.standing_configuration_id)
        else:
            standing_configuration_id = self.standing_configuration_id

        standing_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.standing_configuration, Unset):
            standing_configuration = self.standing_configuration.to_dict()

        lock_standings = self.lock_standings

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, SeasonModelSocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        configuration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, SeasonModelSeasonConfiguration):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

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

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        video_production: Union[Unset, str] = UNSET
        if not isinstance(self.video_production, Unset):
            video_production = self.video_production.value

        promotion_relegation_rules: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.promotion_relegation_rules, Unset):
            promotion_relegation_rules = UNSET
        elif isinstance(self.promotion_relegation_rules, list):
            promotion_relegation_rules = []
            for promotion_relegation_rules_type_0_item_data in self.promotion_relegation_rules:
                promotion_relegation_rules_type_0_item = promotion_relegation_rules_type_0_item_data.to_dict()
                promotion_relegation_rules.append(promotion_relegation_rules_type_0_item)

        else:
            promotion_relegation_rules = self.promotion_relegation_rules

        roster_configuration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.roster_configuration, Unset):
            roster_configuration = UNSET
        elif isinstance(self.roster_configuration, SeasonModelSEASONROSTERConfiguration):
            roster_configuration = self.roster_configuration.to_dict()
        else:
            roster_configuration = self.roster_configuration

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
        if leader_criteria_id is not UNSET:
            field_dict["leaderCriteriaId"] = leader_criteria_id
        if leaders_criteria is not UNSET:
            field_dict["leadersCriteria"] = leaders_criteria
        if international_reference is not UNSET:
            field_dict["internationalReference"] = international_reference
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if season_type is not UNSET:
            field_dict["seasonType"] = season_type
        if year is not UNSET:
            field_dict["year"] = year
        if grade is not UNSET:
            field_dict["grade"] = grade
        if status is not UNSET:
            field_dict["status"] = status
        if include_in_statistics is not UNSET:
            field_dict["includeInStatistics"] = include_in_statistics
        if live_video_available is not UNSET:
            field_dict["liveVideoAvailable"] = live_video_available
        if live_data_available is not UNSET:
            field_dict["liveDataAvailable"] = live_data_available
        if duration_full is not UNSET:
            field_dict["durationFull"] = duration_full
        if discipline is not UNSET:
            field_dict["discipline"] = discipline
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if name_short_local is not UNSET:
            field_dict["nameShortLocal"] = name_short_local
        if name_short_latin is not UNSET:
            field_dict["nameShortLatin"] = name_short_latin
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if gender is not UNSET:
            field_dict["gender"] = gender
        if age_group is not UNSET:
            field_dict["ageGroup"] = age_group
        if standard is not UNSET:
            field_dict["standard"] = standard
        if representation is not UNSET:
            field_dict["representation"] = representation
        if standing_configuration_id is not UNSET:
            field_dict["standingConfigurationId"] = standing_configuration_id
        if standing_configuration is not UNSET:
            field_dict["standingConfiguration"] = standing_configuration
        if lock_standings is not UNSET:
            field_dict["lockStandings"] = lock_standings
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if social is not UNSET:
            field_dict["social"] = social
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if fixture_profile is not UNSET:
            field_dict["fixtureProfile"] = fixture_profile
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if images is not UNSET:
            field_dict["images"] = images
        if video_production is not UNSET:
            field_dict["videoProduction"] = video_production
        if promotion_relegation_rules is not UNSET:
            field_dict["promotionRelegationRules"] = promotion_relegation_rules
        if roster_configuration is not UNSET:
            field_dict["rosterConfiguration"] = roster_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.images_model import ImagesModel
        from ..models.season_model_competition import SeasonModelCompetition
        from ..models.season_model_fixture_profile import SeasonModelFixtureProfile
        from ..models.season_model_leaders_criteria import SeasonModelLeadersCriteria
        from ..models.season_model_organization import SeasonModelOrganization
        from ..models.season_model_promotion_relegation_rules_type_0_item import (
            SeasonModelPromotionRelegationRulesType0Item,
        )
        from ..models.season_model_season_configuration import SeasonModelSeasonConfiguration
        from ..models.season_model_seasonroster_configuration import SeasonModelSEASONROSTERConfiguration
        from ..models.season_model_social_media import SeasonModelSocialMedia
        from ..models.season_model_standing_configuration import SeasonModelStandingConfiguration

        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonModelOrganization.from_dict(_organization)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, SeasonModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = SeasonModelCompetition.from_dict(_competition)

        def _parse_leader_criteria_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                leader_criteria_id_type_0 = UUID(data)

                return leader_criteria_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        leader_criteria_id = _parse_leader_criteria_id(d.pop("leaderCriteriaId", UNSET))

        _leaders_criteria = d.pop("leadersCriteria", UNSET)
        leaders_criteria: Union[Unset, SeasonModelLeadersCriteria]
        if isinstance(_leaders_criteria, Unset):
            leaders_criteria = UNSET
        else:
            leaders_criteria = SeasonModelLeadersCriteria.from_dict(_leaders_criteria)

        def _parse_international_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        international_reference = _parse_international_reference(d.pop("internationalReference", UNSET))

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, SeasonModelEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = SeasonModelEventType(_event_type)

        _season_type = d.pop("seasonType", UNSET)
        season_type: Union[Unset, SeasonModelSeasonType]
        if isinstance(_season_type, Unset):
            season_type = UNSET
        else:
            season_type = SeasonModelSeasonType(_season_type)

        year = d.pop("year", UNSET)

        def _parse_grade(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        grade = _parse_grade(d.pop("grade", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, SeasonModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeasonModelStatus(_status)

        include_in_statistics = d.pop("includeInStatistics", UNSET)

        live_video_available = d.pop("liveVideoAvailable", UNSET)

        live_data_available = d.pop("liveDataAvailable", UNSET)

        def _parse_duration_full(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        duration_full = _parse_duration_full(d.pop("durationFull", UNSET))

        def _parse_discipline(
            data: object,
        ) -> Union[
            None, SeasonModelDisciplineType1, SeasonModelDisciplineType2Type1, SeasonModelDisciplineType3Type1, Unset
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_1 = SeasonModelDisciplineType1(data)

                return discipline_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_2_type_1 = SeasonModelDisciplineType2Type1(data)

                return discipline_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_3_type_1 = SeasonModelDisciplineType3Type1(data)

                return discipline_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    SeasonModelDisciplineType1,
                    SeasonModelDisciplineType2Type1,
                    SeasonModelDisciplineType3Type1,
                    Unset,
                ],
                data,
            )

        discipline = _parse_discipline(d.pop("discipline", UNSET))

        name_local = d.pop("nameLocal", UNSET)

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_name_short_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_short_local = _parse_name_short_local(d.pop("nameShortLocal", UNSET))

        def _parse_name_short_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_short_latin = _parse_name_short_latin(d.pop("nameShortLatin", UNSET))

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.date]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date).date()

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, SeasonModelGender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = SeasonModelGender(_gender)

        _age_group = d.pop("ageGroup", UNSET)
        age_group: Union[Unset, SeasonModelAgeGroup]
        if isinstance(_age_group, Unset):
            age_group = UNSET
        else:
            age_group = SeasonModelAgeGroup(_age_group)

        _standard = d.pop("standard", UNSET)
        standard: Union[Unset, SeasonModelStandard]
        if isinstance(_standard, Unset):
            standard = UNSET
        else:
            standard = SeasonModelStandard(_standard)

        _representation = d.pop("representation", UNSET)
        representation: Union[Unset, SeasonModelRepresentation]
        if isinstance(_representation, Unset):
            representation = UNSET
        else:
            representation = SeasonModelRepresentation(_representation)

        def _parse_standing_configuration_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standing_configuration_id_type_0 = UUID(data)

                return standing_configuration_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        standing_configuration_id = _parse_standing_configuration_id(d.pop("standingConfigurationId", UNSET))

        _standing_configuration = d.pop("standingConfiguration", UNSET)
        standing_configuration: Union[Unset, SeasonModelStandingConfiguration]
        if isinstance(_standing_configuration, Unset):
            standing_configuration = UNSET
        else:
            standing_configuration = SeasonModelStandingConfiguration.from_dict(_standing_configuration)

        lock_standings = d.pop("lockStandings", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_social(data: object) -> Union["SeasonModelSocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = SeasonModelSocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SeasonModelSocialMedia", None, Unset], data)

        social = _parse_social(d.pop("social", UNSET))

        def _parse_configuration(data: object) -> Union["SeasonModelSeasonConfiguration", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = SeasonModelSeasonConfiguration.from_dict(data)

                return configuration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SeasonModelSeasonConfiguration", None, Unset], data)

        configuration = _parse_configuration(d.pop("configuration", UNSET))

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
        fixture_profile: Union[Unset, SeasonModelFixtureProfile]
        if isinstance(_fixture_profile, Unset):
            fixture_profile = UNSET
        else:
            fixture_profile = SeasonModelFixtureProfile.from_dict(_fixture_profile)

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

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ImagesModel.from_dict(images_item_data)

            images.append(images_item)

        _video_production = d.pop("videoProduction", UNSET)
        video_production: Union[Unset, SeasonModelVideoProduction]
        if isinstance(_video_production, Unset):
            video_production = UNSET
        else:
            video_production = SeasonModelVideoProduction(_video_production)

        def _parse_promotion_relegation_rules(
            data: object,
        ) -> Union[None, Unset, list["SeasonModelPromotionRelegationRulesType0Item"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                promotion_relegation_rules_type_0 = []
                _promotion_relegation_rules_type_0 = data
                for promotion_relegation_rules_type_0_item_data in _promotion_relegation_rules_type_0:
                    promotion_relegation_rules_type_0_item = SeasonModelPromotionRelegationRulesType0Item.from_dict(
                        promotion_relegation_rules_type_0_item_data
                    )

                    promotion_relegation_rules_type_0.append(promotion_relegation_rules_type_0_item)

                return promotion_relegation_rules_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SeasonModelPromotionRelegationRulesType0Item"]], data)

        promotion_relegation_rules = _parse_promotion_relegation_rules(d.pop("promotionRelegationRules", UNSET))

        def _parse_roster_configuration(data: object) -> Union["SeasonModelSEASONROSTERConfiguration", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                roster_configuration_type_0 = SeasonModelSEASONROSTERConfiguration.from_dict(data)

                return roster_configuration_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SeasonModelSEASONROSTERConfiguration", None, Unset], data)

        roster_configuration = _parse_roster_configuration(d.pop("rosterConfiguration", UNSET))

        season_model = cls(
            season_id=season_id,
            organization_id=organization_id,
            organization=organization,
            competition_id=competition_id,
            competition=competition,
            leader_criteria_id=leader_criteria_id,
            leaders_criteria=leaders_criteria,
            international_reference=international_reference,
            event_type=event_type,
            season_type=season_type,
            year=year,
            grade=grade,
            status=status,
            include_in_statistics=include_in_statistics,
            live_video_available=live_video_available,
            live_data_available=live_data_available,
            duration_full=duration_full,
            discipline=discipline,
            name_local=name_local,
            name_latin=name_latin,
            name_short_local=name_short_local,
            name_short_latin=name_short_latin,
            start_date=start_date,
            end_date=end_date,
            gender=gender,
            age_group=age_group,
            standard=standard,
            representation=representation,
            standing_configuration_id=standing_configuration_id,
            standing_configuration=standing_configuration,
            lock_standings=lock_standings,
            external_id=external_id,
            social=social,
            configuration=configuration,
            profile_id=profile_id,
            fixture_profile=fixture_profile,
            updated=updated,
            added=added,
            images=images,
            video_production=video_production,
            promotion_relegation_rules=promotion_relegation_rules,
            roster_configuration=roster_configuration,
        )

        return season_model
