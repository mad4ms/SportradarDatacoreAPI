from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_team_statistics_post_body_statistics import MatchTeamStatisticsPostBodyStatistics


T = TypeVar("T", bound="MatchTeamStatisticsPostBody")


@_attrs_define
class MatchTeamStatisticsPostBody:
    """
    Attributes:
        entity_id (UUID): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        statistics (Union[Unset, MatchTeamStatisticsPostBodyStatistics]):
    """

    entity_id: UUID
    fixture_id: UUID
    statistics: Union[Unset, "MatchTeamStatisticsPostBodyStatistics"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id = str(self.entity_id)

        fixture_id = str(self.fixture_id)

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entityId": entity_id,
                "fixtureId": fixture_id,
            }
        )
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_team_statistics_post_body_statistics import MatchTeamStatisticsPostBodyStatistics

        d = dict(src_dict)
        entity_id = UUID(d.pop("entityId"))

        fixture_id = UUID(d.pop("fixtureId"))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, MatchTeamStatisticsPostBodyStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = MatchTeamStatisticsPostBodyStatistics.from_dict(_statistics)

        match_team_statistics_post_body = cls(
            entity_id=entity_id,
            fixture_id=fixture_id,
            statistics=statistics,
        )

        return match_team_statistics_post_body
