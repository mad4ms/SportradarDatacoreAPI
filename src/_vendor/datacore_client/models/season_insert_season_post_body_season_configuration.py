from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonInsertSeasonPostBodySeasonConfiguration")


@_attrs_define
class SeasonInsertSeasonPostBodySeasonConfiguration:
    """Season Configuration settings

    Attributes:
        period_break_duration (Union[Unset, float]):
        half_time_duration (Union[Unset, float]):
    """

    period_break_duration: Union[Unset, float] = UNSET
    half_time_duration: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        period_break_duration = self.period_break_duration

        half_time_duration = self.half_time_duration

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if period_break_duration is not UNSET:
            field_dict["periodBreakDuration"] = period_break_duration
        if half_time_duration is not UNSET:
            field_dict["halfTimeDuration"] = half_time_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        period_break_duration = d.pop("periodBreakDuration", UNSET)

        half_time_duration = d.pop("halfTimeDuration", UNSET)

        season_insert_season_post_body_season_configuration = cls(
            period_break_duration=period_break_duration,
            half_time_duration=half_time_duration,
        )

        return season_insert_season_post_body_season_configuration
