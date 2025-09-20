from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.match_person_statistics_periods_post_body_period_id import MatchPersonStatisticsPeriodsPostBodyPeriodId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_person_statistics_periods_post_body_statistics import (
        MatchPersonStatisticsPeriodsPostBodyStatistics,
    )


T = TypeVar("T", bound="MatchPersonStatisticsPeriodsPostBody")


@_attrs_define
class MatchPersonStatisticsPeriodsPostBody:
    """
    Attributes:
        person_id (UUID): The unique identifier of the person Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (MatchPersonStatisticsPeriodsPostBodyPeriodId): The identifier for the period
            >- `1` Period 1
            >- `2` Period 2
            >- `10` Extra time 1 period 1
            >- `11` Extra time 1 period 2
            >- `12` Extra time 2 period 1
            >- `13` Extra time 2 period 2
            >- `14` Shoot Out
        entity_id (Union[None, UUID, Unset]): The unique identifier of the team Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        statistics (Union[Unset, MatchPersonStatisticsPeriodsPostBodyStatistics]):
        section (Union[Unset, str]): The section of the period (sub-period)
    """

    person_id: UUID
    fixture_id: UUID
    period_id: MatchPersonStatisticsPeriodsPostBodyPeriodId
    entity_id: Union[None, UUID, Unset] = UNSET
    statistics: Union[Unset, "MatchPersonStatisticsPeriodsPostBodyStatistics"] = UNSET
    section: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        person_id = str(self.person_id)

        fixture_id = str(self.fixture_id)

        period_id = self.period_id.value

        entity_id: Union[None, Unset, str]
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        section = self.section

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "fixtureId": fixture_id,
                "periodId": period_id,
            }
        )
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if section is not UNSET:
            field_dict["section"] = section

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_person_statistics_periods_post_body_statistics import (
            MatchPersonStatisticsPeriodsPostBodyStatistics,
        )

        d = dict(src_dict)
        person_id = UUID(d.pop("personId"))

        fixture_id = UUID(d.pop("fixtureId"))

        period_id = MatchPersonStatisticsPeriodsPostBodyPeriodId(d.pop("periodId"))

        def _parse_entity_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)

                return entity_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        entity_id = _parse_entity_id(d.pop("entityId", UNSET))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, MatchPersonStatisticsPeriodsPostBodyStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = MatchPersonStatisticsPeriodsPostBodyStatistics.from_dict(_statistics)

        section = d.pop("section", UNSET)

        match_person_statistics_periods_post_body = cls(
            person_id=person_id,
            fixture_id=fixture_id,
            period_id=period_id,
            entity_id=entity_id,
            statistics=statistics,
            section=section,
        )

        return match_person_statistics_periods_post_body
