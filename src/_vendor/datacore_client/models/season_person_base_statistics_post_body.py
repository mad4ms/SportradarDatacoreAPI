from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.season_person_base_statistics_post_body_competitor_type import (
    SeasonPersonBaseStatisticsPostBodyCompetitorType,
)
from ..models.season_person_base_statistics_post_body_fixture_type import SeasonPersonBaseStatisticsPostBodyFixtureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_person_base_statistics_post_body_statistics import SeasonPersonBaseStatisticsPostBodyStatistics


T = TypeVar("T", bound="SeasonPersonBaseStatisticsPostBody")


@_attrs_define
class SeasonPersonBaseStatisticsPostBody:
    """
    Attributes:
        season_id (UUID): The unique identifier of the season Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id (UUID): The unique identifier of the person Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_type (SeasonPersonBaseStatisticsPostBodyFixtureType): Type of match
            >- `ALL_STAR` All Star
            >- `DEMONSTRATION` Demonstration
            >- `FINAL` Final
            >- `FRIENDLY` Friendly
            >- `PLAYOFF` Playoff
            >- `PRESEASON` Pre Season
            >- `REGULAR` Regular
             Example: REGULAR.
        competitor_type (SeasonPersonBaseStatisticsPostBodyCompetitorType): The type of competitors in this match
            >- `ENTITY` Entity
            >- `PERSON` Person
             Example: ENTITY.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        representing (Union[Unset, str]): Who was being represented for the season base statistics Example: AUSTRALIA.
        statistics (Union[Unset, SeasonPersonBaseStatisticsPostBodyStatistics]):
    """

    season_id: UUID
    person_id: UUID
    fixture_type: SeasonPersonBaseStatisticsPostBodyFixtureType
    competitor_type: SeasonPersonBaseStatisticsPostBodyCompetitorType
    entity_id: Union[Unset, UUID] = UNSET
    representing: Union[Unset, str] = UNSET
    statistics: Union[Unset, "SeasonPersonBaseStatisticsPostBodyStatistics"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id = str(self.season_id)

        person_id = str(self.person_id)

        fixture_type = self.fixture_type.value

        competitor_type = self.competitor_type.value

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        representing = self.representing

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "seasonId": season_id,
                "personId": person_id,
                "fixtureType": fixture_type,
                "competitorType": competitor_type,
            }
        )
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if representing is not UNSET:
            field_dict["representing"] = representing
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_person_base_statistics_post_body_statistics import (
            SeasonPersonBaseStatisticsPostBodyStatistics,
        )

        d = dict(src_dict)
        season_id = UUID(d.pop("seasonId"))

        person_id = UUID(d.pop("personId"))

        fixture_type = SeasonPersonBaseStatisticsPostBodyFixtureType(d.pop("fixtureType"))

        competitor_type = SeasonPersonBaseStatisticsPostBodyCompetitorType(d.pop("competitorType"))

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        representing = d.pop("representing", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SeasonPersonBaseStatisticsPostBodyStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SeasonPersonBaseStatisticsPostBodyStatistics.from_dict(_statistics)

        season_person_base_statistics_post_body = cls(
            season_id=season_id,
            person_id=person_id,
            fixture_type=fixture_type,
            competitor_type=competitor_type,
            entity_id=entity_id,
            representing=representing,
            statistics=statistics,
        )

        return season_person_base_statistics_post_body
