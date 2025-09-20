from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.fesp_insert_update_match_team_period_statistics_post_body_period_id import (
    FespInsertUpdateMatchTeamPeriodStatisticsPostBodyPeriodId,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fesp_insert_update_match_team_period_statistics_post_body_statistics import (
        FespInsertUpdateMatchTeamPeriodStatisticsPostBodyStatistics,
    )


T = TypeVar("T", bound="FespInsertUpdateMatchTeamPeriodStatisticsPostBody")


@_attrs_define
class FespInsertUpdateMatchTeamPeriodStatisticsPostBody:
    """
    Attributes:
        entity_id (UUID): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        statistics (Union[Unset, FespInsertUpdateMatchTeamPeriodStatisticsPostBodyStatistics]):
        period_id (Union[Unset, FespInsertUpdateMatchTeamPeriodStatisticsPostBodyPeriodId]): The identifier for the
            period
            >- `1` Period 1
            >- `2` Period 2
            >- `10` Extra time 1 period 1
            >- `11` Extra time 1 period 2
            >- `12` Extra time 2 period 1
            >- `13` Extra time 2 period 2
            >- `14` Shoot Out
        section (Union[Unset, str]): The section of the period (sub-period)
    """

    entity_id: UUID
    fixture_id: UUID
    statistics: Union[
        Unset, "FespInsertUpdateMatchTeamPeriodStatisticsPostBodyStatistics"
    ] = UNSET
    period_id: Union[
        Unset, FespInsertUpdateMatchTeamPeriodStatisticsPostBodyPeriodId
    ] = UNSET
    section: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id = str(self.entity_id)

        fixture_id = str(self.fixture_id)

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        period_id: Union[Unset, int] = UNSET
        if not isinstance(self.period_id, Unset):
            period_id = self.period_id.value

        section = self.section

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entityId": entity_id,
                "fixtureId": fixture_id,
            }
        )
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if period_id is not UNSET:
            field_dict["periodId"] = period_id
        if section is not UNSET:
            field_dict["section"] = section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fesp_insert_update_match_team_period_statistics_post_body_statistics import (
            FespInsertUpdateMatchTeamPeriodStatisticsPostBodyStatistics,
        )

        d = dict(src_dict)
        entity_id = UUID(d.pop("entityId"))

        fixture_id = UUID(d.pop("fixtureId"))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[
            Unset, FespInsertUpdateMatchTeamPeriodStatisticsPostBodyStatistics
        ]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = (
                FespInsertUpdateMatchTeamPeriodStatisticsPostBodyStatistics.from_dict(
                    _statistics
                )
            )

        _period_id = d.pop("periodId", UNSET)
        period_id: Union[
            Unset, FespInsertUpdateMatchTeamPeriodStatisticsPostBodyPeriodId
        ]
        if isinstance(_period_id, Unset):
            period_id = UNSET
        else:
            period_id = FespInsertUpdateMatchTeamPeriodStatisticsPostBodyPeriodId(
                _period_id
            )

        section = d.pop("section", UNSET)

        fesp_insert_update_match_team_period_statistics_post_body = cls(
            entity_id=entity_id,
            fixture_id=fixture_id,
            statistics=statistics,
            period_id=period_id,
            section=section,
        )

        return fesp_insert_update_match_team_period_statistics_post_body
