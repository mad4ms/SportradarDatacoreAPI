from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.sebs_insert_update_season_team_base_statistics_post_body_competitor_type import (
    SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyCompetitorType,
)
from ..models.sebs_insert_update_season_team_base_statistics_post_body_fixture_type import (
    SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyFixtureType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sebs_insert_update_season_team_base_statistics_post_body_statistics import (
        SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyStatistics,
    )


T = TypeVar("T", bound="SebsInsertUpdateSeasonTeamBaseStatisticsPostBody")


@_attrs_define
class SebsInsertUpdateSeasonTeamBaseStatisticsPostBody:
    """
    Attributes:
        season_id (UUID): The unique identifier of the season Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_type (SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyFixtureType): Type of match
            >- `ALL_STAR` All Star
            >- `DEMONSTRATION` Demonstration
            >- `FINAL` Final
            >- `FRIENDLY` Friendly
            >- `PLAYOFF` Playoff
            >- `PRESEASON` Pre Season
            >- `REGULAR` Regular
             Example: REGULAR.
        competitor_type (SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyCompetitorType): The type of competitors in
            this match
            >- `ENTITY` Entity
            >- `PERSON` Person
             Example: ENTITY.
        representing (Union[Unset, str]): Who was being represented for the season base statistics Example: AUSTRALIA.
        statistics (Union[Unset, SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyStatistics]):
    """

    season_id: UUID
    entity_id: UUID
    fixture_type: SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyFixtureType
    competitor_type: SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyCompetitorType
    representing: Union[Unset, str] = UNSET
    statistics: Union[
        Unset, "SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyStatistics"
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id = str(self.season_id)

        entity_id = str(self.entity_id)

        fixture_type = self.fixture_type.value

        competitor_type = self.competitor_type.value

        representing = self.representing

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "seasonId": season_id,
                "entityId": entity_id,
                "fixtureType": fixture_type,
                "competitorType": competitor_type,
            }
        )
        if representing is not UNSET:
            field_dict["representing"] = representing
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sebs_insert_update_season_team_base_statistics_post_body_statistics import (
            SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyStatistics,
        )

        d = dict(src_dict)
        season_id = UUID(d.pop("seasonId"))

        entity_id = UUID(d.pop("entityId"))

        fixture_type = SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyFixtureType(
            d.pop("fixtureType")
        )

        competitor_type = (
            SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyCompetitorType(
                d.pop("competitorType")
            )
        )

        representing = d.pop("representing", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[
            Unset, SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyStatistics
        ]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = (
                SebsInsertUpdateSeasonTeamBaseStatisticsPostBodyStatistics.from_dict(
                    _statistics
                )
            )

        sebs_insert_update_season_team_base_statistics_post_body = cls(
            season_id=season_id,
            entity_id=entity_id,
            fixture_type=fixture_type,
            competitor_type=competitor_type,
            representing=representing,
            statistics=statistics,
        )

        return sebs_insert_update_season_team_base_statistics_post_body
