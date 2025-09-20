from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.season_series_insert_series_post_body_season_series_competitor_series_result import (
    SeasonSeriesInsertSeriesPostBodySeasonSeriesCompetitorSeriesResult,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonSeriesInsertSeriesPostBodySeasonSeriesCompetitor")


@_attrs_define
class SeasonSeriesInsertSeriesPostBodySeasonSeriesCompetitor:
    """
    Attributes:
        entity_id (Union[Unset, str]): The uuid of the entity
        person_id (Union[Unset, str]): The uuid of the person
        conference_id (Union[Unset, str]): The uuid of the conference the competitor represents
        division_id (Union[Unset, str]): The uuid of the conference the competitor represents
        pre_series_ranking (Union[Unset, float]): The rank of the competitor coming into the series
        string_record (Union[Unset, float]): String record of the competitor
        series_wins (Union[Unset, float]): Number of wins in the series for the competitor
        series_losses (Union[Unset, float]): Number of losses in the series for the competitor
        series_draws (Union[Unset, float]): Number of draws in the series for the competitor
        series_result (Union[Unset, SeasonSeriesInsertSeriesPostBodySeasonSeriesCompetitorSeriesResult]): Result for the
            competitor in the series
    """

    entity_id: Union[Unset, str] = UNSET
    person_id: Union[Unset, str] = UNSET
    conference_id: Union[Unset, str] = UNSET
    division_id: Union[Unset, str] = UNSET
    pre_series_ranking: Union[Unset, float] = UNSET
    string_record: Union[Unset, float] = UNSET
    series_wins: Union[Unset, float] = UNSET
    series_losses: Union[Unset, float] = UNSET
    series_draws: Union[Unset, float] = UNSET
    series_result: Union[
        Unset, SeasonSeriesInsertSeriesPostBodySeasonSeriesCompetitorSeriesResult
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        person_id = self.person_id

        conference_id = self.conference_id

        division_id = self.division_id

        pre_series_ranking = self.pre_series_ranking

        string_record = self.string_record

        series_wins = self.series_wins

        series_losses = self.series_losses

        series_draws = self.series_draws

        series_result: Union[Unset, str] = UNSET
        if not isinstance(self.series_result, Unset):
            series_result = self.series_result.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if pre_series_ranking is not UNSET:
            field_dict["preSeriesRanking"] = pre_series_ranking
        if string_record is not UNSET:
            field_dict["stringRecord"] = string_record
        if series_wins is not UNSET:
            field_dict["seriesWins"] = series_wins
        if series_losses is not UNSET:
            field_dict["seriesLosses"] = series_losses
        if series_draws is not UNSET:
            field_dict["seriesDraws"] = series_draws
        if series_result is not UNSET:
            field_dict["seriesResult"] = series_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entityId", UNSET)

        person_id = d.pop("personId", UNSET)

        conference_id = d.pop("conferenceId", UNSET)

        division_id = d.pop("divisionId", UNSET)

        pre_series_ranking = d.pop("preSeriesRanking", UNSET)

        string_record = d.pop("stringRecord", UNSET)

        series_wins = d.pop("seriesWins", UNSET)

        series_losses = d.pop("seriesLosses", UNSET)

        series_draws = d.pop("seriesDraws", UNSET)

        _series_result = d.pop("seriesResult", UNSET)
        series_result: Union[
            Unset, SeasonSeriesInsertSeriesPostBodySeasonSeriesCompetitorSeriesResult
        ]
        if isinstance(_series_result, Unset):
            series_result = UNSET
        else:
            series_result = (
                SeasonSeriesInsertSeriesPostBodySeasonSeriesCompetitorSeriesResult(
                    _series_result
                )
            )

        season_series_insert_series_post_body_season_series_competitor = cls(
            entity_id=entity_id,
            person_id=person_id,
            conference_id=conference_id,
            division_id=division_id,
            pre_series_ranking=pre_series_ranking,
            string_record=string_record,
            series_wins=series_wins,
            series_losses=series_losses,
            series_draws=series_draws,
            series_result=series_result,
        )

        return season_series_insert_series_post_body_season_series_competitor
