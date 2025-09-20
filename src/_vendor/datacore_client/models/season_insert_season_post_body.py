import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_insert_season_post_body_age_group import (
    SeasonInsertSeasonPostBodyAgeGroup,
)
from ..models.season_insert_season_post_body_discipline_type_1 import (
    SeasonInsertSeasonPostBodyDisciplineType1,
)
from ..models.season_insert_season_post_body_discipline_type_2_type_1 import (
    SeasonInsertSeasonPostBodyDisciplineType2Type1,
)
from ..models.season_insert_season_post_body_discipline_type_3_type_1 import (
    SeasonInsertSeasonPostBodyDisciplineType3Type1,
)
from ..models.season_insert_season_post_body_event_type import (
    SeasonInsertSeasonPostBodyEventType,
)
from ..models.season_insert_season_post_body_gender import (
    SeasonInsertSeasonPostBodyGender,
)
from ..models.season_insert_season_post_body_representation import (
    SeasonInsertSeasonPostBodyRepresentation,
)
from ..models.season_insert_season_post_body_season_type import (
    SeasonInsertSeasonPostBodySeasonType,
)
from ..models.season_insert_season_post_body_standard import (
    SeasonInsertSeasonPostBodyStandard,
)
from ..models.season_insert_season_post_body_status import (
    SeasonInsertSeasonPostBodyStatus,
)
from ..models.season_insert_season_post_body_video_production import (
    SeasonInsertSeasonPostBodyVideoProduction,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_insert_season_post_body_promotion_relegation_rules_type_0_item import (
        SeasonInsertSeasonPostBodyPromotionRelegationRulesType0Item,
    )
    from ..models.season_insert_season_post_body_season_configuration import (
        SeasonInsertSeasonPostBodySeasonConfiguration,
    )
    from ..models.season_insert_season_post_body_seasonroster_configuration import (
        SeasonInsertSeasonPostBodySEASONROSTERConfiguration,
    )
    from ..models.season_insert_season_post_body_social_media import (
        SeasonInsertSeasonPostBodySocialMedia,
    )


T = TypeVar("T", bound="SeasonInsertSeasonPostBody")


@_attrs_define
class SeasonInsertSeasonPostBody:
    """
    Attributes:
        competition_id (UUID): The unique identifier of the competition Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_type (SeasonInsertSeasonPostBodySeasonType): The type of matches added to this season
            >- `MULTI_YEAR_HISTORICAL` Mulit-Year Historical
            >- `ONE_OFF` One off
            >- `PRESEASON` Pre Season
            >- `SEASON` Season
            >- `TOURNAMENT` Tournament
             Example: SEASON.
        name_local (str): The name of the season in the [local](#section/Introduction/Character-Sets-and-Names) language
            Example: Test season.
        start_date (datetime.date): Season start date Example: 2016-09-08.
        gender (SeasonInsertSeasonPostBodyGender): The gender of the participants in the season
            >- `FEMALE` Female
            >- `MALE` Male
            >- `MIXED` Mixed
            >- `UNKNOWN` Unknown
             Example: MALE.
        age_group (SeasonInsertSeasonPostBodyAgeGroup): The age group of the season
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
        standard (SeasonInsertSeasonPostBodyStandard): The playing standard of the season
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
        representation (SeasonInsertSeasonPostBodyRepresentation): What level are the competitors representing
            >- `CLUB` Club
            >- `COUNTRY` Country
            >- `PERSON` Person
            >- `REGION` Region
            >- `STATE` State
             Example: CLUB.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        leader_criteria_id (Union[None, UUID, Unset]): The unique identifier of the ~LeaderCriteria~ Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        international_reference (Union[None, Unset, str]): The international reference for this season given by the
            sport governing body Example: CA3243-3.
        event_type (Union[Unset, SeasonInsertSeasonPostBodyEventType]): Primary Type of Matches
            >- `FIXTURE` Fixture
            >- `PRACTICE` Practice
             Default: SeasonInsertSeasonPostBodyEventType.FIXTURE. Example: FIXTURE.
        year (Union[Unset, int]): Year of the season Example: 2019.
        grade (Union[None, Unset, str]): The playing grade of the matches in this season Example: A.
        status (Union[Unset, SeasonInsertSeasonPostBodyStatus]): Status
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
        discipline (Union[None, SeasonInsertSeasonPostBodyDisciplineType1,
            SeasonInsertSeasonPostBodyDisciplineType2Type1, SeasonInsertSeasonPostBodyDisciplineType3Type1, Unset]): If no
            'discipline' is passed to a new match this value is used
            >- None None
            >- `INDOOR` Indoor
            >- `OUTDOOR` Outdoor
             Example: INDOOR.
        name_latin (Union[None, Unset, str]): The name of the season in [latin](#section/Introduction/Character-Sets-
            and-Names) characters Example: Test season.
        name_short_local (Union[None, Unset, str]): The abbreviated name of the season in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Test short local.
        name_short_latin (Union[None, Unset, str]): The abbreviated name of the season in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Test short latin.
        end_date (Union[None, Unset, datetime.date]): Season end date Example: 2016-09-08.
        standing_configuration_id (Union[None, UUID, Unset]): The unique identifier of the ~standingConfiguration~
            Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        lock_standings (Union[Unset, bool]): Is the standings generation locked ? Example: True.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        social (Union['SeasonInsertSeasonPostBodySocialMedia', None, Unset]): Social Media contacts
        configuration (Union['SeasonInsertSeasonPostBodySeasonConfiguration', None, Unset]): Season Configuration
            settings
        profile_id (Union[None, UUID, Unset]): The profile that this season belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        video_production (Union[Unset, SeasonInsertSeasonPostBodyVideoProduction]): Data synchronization strategy with
            video production systems
            >- `AUTOMATED` Automated
            >- `MANUAL` Manual
            >- `NONE` None
             Default: SeasonInsertSeasonPostBodyVideoProduction.NONE. Example: AUTOMATED.
        promotion_relegation_rules (Union[None, Unset,
            list['SeasonInsertSeasonPostBodyPromotionRelegationRulesType0Item']]):
        roster_configuration (Union['SeasonInsertSeasonPostBodySEASONROSTERConfiguration', None, Unset]): Configuration
            for the SEASON ROSTER
    """

    competition_id: UUID
    season_type: SeasonInsertSeasonPostBodySeasonType
    name_local: str
    start_date: datetime.date
    gender: SeasonInsertSeasonPostBodyGender
    age_group: SeasonInsertSeasonPostBodyAgeGroup
    standard: SeasonInsertSeasonPostBodyStandard
    representation: SeasonInsertSeasonPostBodyRepresentation
    season_id: Union[Unset, UUID] = UNSET
    leader_criteria_id: Union[None, UUID, Unset] = UNSET
    international_reference: Union[None, Unset, str] = UNSET
    event_type: Union[Unset, SeasonInsertSeasonPostBodyEventType] = (
        SeasonInsertSeasonPostBodyEventType.FIXTURE
    )
    year: Union[Unset, int] = UNSET
    grade: Union[None, Unset, str] = UNSET
    status: Union[Unset, SeasonInsertSeasonPostBodyStatus] = UNSET
    include_in_statistics: Union[Unset, bool] = True
    live_video_available: Union[Unset, bool] = UNSET
    live_data_available: Union[Unset, bool] = UNSET
    duration_full: Union[None, Unset, int] = 180
    discipline: Union[
        None,
        SeasonInsertSeasonPostBodyDisciplineType1,
        SeasonInsertSeasonPostBodyDisciplineType2Type1,
        SeasonInsertSeasonPostBodyDisciplineType3Type1,
        Unset,
    ] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    name_short_local: Union[None, Unset, str] = UNSET
    name_short_latin: Union[None, Unset, str] = UNSET
    end_date: Union[None, Unset, datetime.date] = UNSET
    standing_configuration_id: Union[None, UUID, Unset] = UNSET
    lock_standings: Union[Unset, bool] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    social: Union["SeasonInsertSeasonPostBodySocialMedia", None, Unset] = UNSET
    configuration: Union[
        "SeasonInsertSeasonPostBodySeasonConfiguration", None, Unset
    ] = UNSET
    profile_id: Union[None, UUID, Unset] = UNSET
    video_production: Union[Unset, SeasonInsertSeasonPostBodyVideoProduction] = (
        SeasonInsertSeasonPostBodyVideoProduction.NONE
    )
    promotion_relegation_rules: Union[
        None, Unset, list["SeasonInsertSeasonPostBodyPromotionRelegationRulesType0Item"]
    ] = UNSET
    roster_configuration: Union[
        "SeasonInsertSeasonPostBodySEASONROSTERConfiguration", None, Unset
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.season_insert_season_post_body_season_configuration import (
            SeasonInsertSeasonPostBodySeasonConfiguration,
        )
        from ..models.season_insert_season_post_body_seasonroster_configuration import (
            SeasonInsertSeasonPostBodySEASONROSTERConfiguration,
        )
        from ..models.season_insert_season_post_body_social_media import (
            SeasonInsertSeasonPostBodySocialMedia,
        )

        competition_id = str(self.competition_id)

        season_type = self.season_type.value

        name_local = self.name_local

        start_date = self.start_date.isoformat()

        gender = self.gender.value

        age_group = self.age_group.value

        standard = self.standard.value

        representation = self.representation.value

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        leader_criteria_id: Union[None, Unset, str]
        if isinstance(self.leader_criteria_id, Unset):
            leader_criteria_id = UNSET
        elif isinstance(self.leader_criteria_id, UUID):
            leader_criteria_id = str(self.leader_criteria_id)
        else:
            leader_criteria_id = self.leader_criteria_id

        international_reference: Union[None, Unset, str]
        if isinstance(self.international_reference, Unset):
            international_reference = UNSET
        else:
            international_reference = self.international_reference

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

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
        elif isinstance(self.discipline, SeasonInsertSeasonPostBodyDisciplineType1):
            discipline = self.discipline.value
        elif isinstance(
            self.discipline, SeasonInsertSeasonPostBodyDisciplineType2Type1
        ):
            discipline = self.discipline.value
        elif isinstance(
            self.discipline, SeasonInsertSeasonPostBodyDisciplineType3Type1
        ):
            discipline = self.discipline.value
        else:
            discipline = self.discipline

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

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        standing_configuration_id: Union[None, Unset, str]
        if isinstance(self.standing_configuration_id, Unset):
            standing_configuration_id = UNSET
        elif isinstance(self.standing_configuration_id, UUID):
            standing_configuration_id = str(self.standing_configuration_id)
        else:
            standing_configuration_id = self.standing_configuration_id

        lock_standings = self.lock_standings

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, SeasonInsertSeasonPostBodySocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        configuration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(
            self.configuration, SeasonInsertSeasonPostBodySeasonConfiguration
        ):
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

        video_production: Union[Unset, str] = UNSET
        if not isinstance(self.video_production, Unset):
            video_production = self.video_production.value

        promotion_relegation_rules: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.promotion_relegation_rules, Unset):
            promotion_relegation_rules = UNSET
        elif isinstance(self.promotion_relegation_rules, list):
            promotion_relegation_rules = []
            for (
                promotion_relegation_rules_type_0_item_data
            ) in self.promotion_relegation_rules:
                promotion_relegation_rules_type_0_item = (
                    promotion_relegation_rules_type_0_item_data.to_dict()
                )
                promotion_relegation_rules.append(
                    promotion_relegation_rules_type_0_item
                )

        else:
            promotion_relegation_rules = self.promotion_relegation_rules

        roster_configuration: Union[None, Unset, dict[str, Any]]
        if isinstance(self.roster_configuration, Unset):
            roster_configuration = UNSET
        elif isinstance(
            self.roster_configuration,
            SeasonInsertSeasonPostBodySEASONROSTERConfiguration,
        ):
            roster_configuration = self.roster_configuration.to_dict()
        else:
            roster_configuration = self.roster_configuration

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "competitionId": competition_id,
                "seasonType": season_type,
                "nameLocal": name_local,
                "startDate": start_date,
                "gender": gender,
                "ageGroup": age_group,
                "standard": standard,
                "representation": representation,
            }
        )
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if leader_criteria_id is not UNSET:
            field_dict["leaderCriteriaId"] = leader_criteria_id
        if international_reference is not UNSET:
            field_dict["internationalReference"] = international_reference
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
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
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if name_short_local is not UNSET:
            field_dict["nameShortLocal"] = name_short_local
        if name_short_latin is not UNSET:
            field_dict["nameShortLatin"] = name_short_latin
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if standing_configuration_id is not UNSET:
            field_dict["standingConfigurationId"] = standing_configuration_id
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
        if video_production is not UNSET:
            field_dict["videoProduction"] = video_production
        if promotion_relegation_rules is not UNSET:
            field_dict["promotionRelegationRules"] = promotion_relegation_rules
        if roster_configuration is not UNSET:
            field_dict["rosterConfiguration"] = roster_configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_insert_season_post_body_promotion_relegation_rules_type_0_item import (
            SeasonInsertSeasonPostBodyPromotionRelegationRulesType0Item,
        )
        from ..models.season_insert_season_post_body_season_configuration import (
            SeasonInsertSeasonPostBodySeasonConfiguration,
        )
        from ..models.season_insert_season_post_body_seasonroster_configuration import (
            SeasonInsertSeasonPostBodySEASONROSTERConfiguration,
        )
        from ..models.season_insert_season_post_body_social_media import (
            SeasonInsertSeasonPostBodySocialMedia,
        )

        d = dict(src_dict)
        competition_id = UUID(d.pop("competitionId"))

        season_type = SeasonInsertSeasonPostBodySeasonType(d.pop("seasonType"))

        name_local = d.pop("nameLocal")

        start_date = isoparse(d.pop("startDate")).date()

        gender = SeasonInsertSeasonPostBodyGender(d.pop("gender"))

        age_group = SeasonInsertSeasonPostBodyAgeGroup(d.pop("ageGroup"))

        standard = SeasonInsertSeasonPostBodyStandard(d.pop("standard"))

        representation = SeasonInsertSeasonPostBodyRepresentation(
            d.pop("representation")
        )

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

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

        def _parse_international_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        international_reference = _parse_international_reference(
            d.pop("internationalReference", UNSET)
        )

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, SeasonInsertSeasonPostBodyEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = SeasonInsertSeasonPostBodyEventType(_event_type)

        year = d.pop("year", UNSET)

        def _parse_grade(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        grade = _parse_grade(d.pop("grade", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, SeasonInsertSeasonPostBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeasonInsertSeasonPostBodyStatus(_status)

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
            None,
            SeasonInsertSeasonPostBodyDisciplineType1,
            SeasonInsertSeasonPostBodyDisciplineType2Type1,
            SeasonInsertSeasonPostBodyDisciplineType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_1 = SeasonInsertSeasonPostBodyDisciplineType1(data)

                return discipline_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_2_type_1 = (
                    SeasonInsertSeasonPostBodyDisciplineType2Type1(data)
                )

                return discipline_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                discipline_type_3_type_1 = (
                    SeasonInsertSeasonPostBodyDisciplineType3Type1(data)
                )

                return discipline_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    SeasonInsertSeasonPostBodyDisciplineType1,
                    SeasonInsertSeasonPostBodyDisciplineType2Type1,
                    SeasonInsertSeasonPostBodyDisciplineType3Type1,
                    Unset,
                ],
                data,
            )

        discipline = _parse_discipline(d.pop("discipline", UNSET))

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

        standing_configuration_id = _parse_standing_configuration_id(
            d.pop("standingConfigurationId", UNSET)
        )

        lock_standings = d.pop("lockStandings", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_social(
            data: object,
        ) -> Union["SeasonInsertSeasonPostBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = SeasonInsertSeasonPostBodySocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["SeasonInsertSeasonPostBodySocialMedia", None, Unset], data
            )

        social = _parse_social(d.pop("social", UNSET))

        def _parse_configuration(
            data: object,
        ) -> Union["SeasonInsertSeasonPostBodySeasonConfiguration", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = (
                    SeasonInsertSeasonPostBodySeasonConfiguration.from_dict(data)
                )

                return configuration_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["SeasonInsertSeasonPostBodySeasonConfiguration", None, Unset],
                data,
            )

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

        _video_production = d.pop("videoProduction", UNSET)
        video_production: Union[Unset, SeasonInsertSeasonPostBodyVideoProduction]
        if isinstance(_video_production, Unset):
            video_production = UNSET
        else:
            video_production = SeasonInsertSeasonPostBodyVideoProduction(
                _video_production
            )

        def _parse_promotion_relegation_rules(
            data: object,
        ) -> Union[
            None,
            Unset,
            list["SeasonInsertSeasonPostBodyPromotionRelegationRulesType0Item"],
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                promotion_relegation_rules_type_0 = []
                _promotion_relegation_rules_type_0 = data
                for (
                    promotion_relegation_rules_type_0_item_data
                ) in _promotion_relegation_rules_type_0:
                    promotion_relegation_rules_type_0_item = SeasonInsertSeasonPostBodyPromotionRelegationRulesType0Item.from_dict(
                        promotion_relegation_rules_type_0_item_data
                    )

                    promotion_relegation_rules_type_0.append(
                        promotion_relegation_rules_type_0_item
                    )

                return promotion_relegation_rules_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    list["SeasonInsertSeasonPostBodyPromotionRelegationRulesType0Item"],
                ],
                data,
            )

        promotion_relegation_rules = _parse_promotion_relegation_rules(
            d.pop("promotionRelegationRules", UNSET)
        )

        def _parse_roster_configuration(
            data: object,
        ) -> Union["SeasonInsertSeasonPostBodySEASONROSTERConfiguration", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                roster_configuration_type_0 = (
                    SeasonInsertSeasonPostBodySEASONROSTERConfiguration.from_dict(data)
                )

                return roster_configuration_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    "SeasonInsertSeasonPostBodySEASONROSTERConfiguration", None, Unset
                ],
                data,
            )

        roster_configuration = _parse_roster_configuration(
            d.pop("rosterConfiguration", UNSET)
        )

        season_insert_season_post_body = cls(
            competition_id=competition_id,
            season_type=season_type,
            name_local=name_local,
            start_date=start_date,
            gender=gender,
            age_group=age_group,
            standard=standard,
            representation=representation,
            season_id=season_id,
            leader_criteria_id=leader_criteria_id,
            international_reference=international_reference,
            event_type=event_type,
            year=year,
            grade=grade,
            status=status,
            include_in_statistics=include_in_statistics,
            live_video_available=live_video_available,
            live_data_available=live_data_available,
            duration_full=duration_full,
            discipline=discipline,
            name_latin=name_latin,
            name_short_local=name_short_local,
            name_short_latin=name_short_latin,
            end_date=end_date,
            standing_configuration_id=standing_configuration_id,
            lock_standings=lock_standings,
            external_id=external_id,
            social=social,
            configuration=configuration,
            profile_id=profile_id,
            video_production=video_production,
            promotion_relegation_rules=promotion_relegation_rules,
            roster_configuration=roster_configuration,
        )

        return season_insert_season_post_body
