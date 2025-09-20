from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StandingPostBodyPointsAdditionalProperty")


@_attrs_define
class StandingPostBodyPointsAdditionalProperty:
    """Type of points

    Example:
        default

    Attributes:
        bonus_standing_points (Union[Unset, float]): Bonus Standing points
        penalty_standing_points (Union[Unset, float]): Penalty Standing points
        bye_standing_points (Union[Unset, float]): Bye Standing points
        team_differential (Union[Unset, float]): Differential of Won-Lost
        team_differential_home (Union[Unset, float]): Differential of Won-Lost
        team_differential_away (Union[Unset, float]): Differential of Won-Lost
        games_behind (Union[Unset, float]): Games behind leading competitor
        standing_points (Union[Unset, float]): Standing Points for competitor
        standing_points_home (Union[Unset, float]): Standing Points for competitor at Home
        standing_points_away (Union[Unset, float]): Standing Points for competitor away
        standing_points_given (Union[Unset, float]): Standing Points Given away for this competitor
    """

    bonus_standing_points: Union[Unset, float] = UNSET
    penalty_standing_points: Union[Unset, float] = UNSET
    bye_standing_points: Union[Unset, float] = UNSET
    team_differential: Union[Unset, float] = UNSET
    team_differential_home: Union[Unset, float] = UNSET
    team_differential_away: Union[Unset, float] = UNSET
    games_behind: Union[Unset, float] = UNSET
    standing_points: Union[Unset, float] = UNSET
    standing_points_home: Union[Unset, float] = UNSET
    standing_points_away: Union[Unset, float] = UNSET
    standing_points_given: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        bonus_standing_points = self.bonus_standing_points

        penalty_standing_points = self.penalty_standing_points

        bye_standing_points = self.bye_standing_points

        team_differential = self.team_differential

        team_differential_home = self.team_differential_home

        team_differential_away = self.team_differential_away

        games_behind = self.games_behind

        standing_points = self.standing_points

        standing_points_home = self.standing_points_home

        standing_points_away = self.standing_points_away

        standing_points_given = self.standing_points_given

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if bonus_standing_points is not UNSET:
            field_dict["bonusStandingPoints"] = bonus_standing_points
        if penalty_standing_points is not UNSET:
            field_dict["penaltyStandingPoints"] = penalty_standing_points
        if bye_standing_points is not UNSET:
            field_dict["byeStandingPoints"] = bye_standing_points
        if team_differential is not UNSET:
            field_dict["teamDifferential"] = team_differential
        if team_differential_home is not UNSET:
            field_dict["teamDifferentialHome"] = team_differential_home
        if team_differential_away is not UNSET:
            field_dict["teamDifferentialAway"] = team_differential_away
        if games_behind is not UNSET:
            field_dict["gamesBehind"] = games_behind
        if standing_points is not UNSET:
            field_dict["standingPoints"] = standing_points
        if standing_points_home is not UNSET:
            field_dict["standingPointsHome"] = standing_points_home
        if standing_points_away is not UNSET:
            field_dict["standingPointsAway"] = standing_points_away
        if standing_points_given is not UNSET:
            field_dict["standingPointsGiven"] = standing_points_given

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bonus_standing_points = d.pop("bonusStandingPoints", UNSET)

        penalty_standing_points = d.pop("penaltyStandingPoints", UNSET)

        bye_standing_points = d.pop("byeStandingPoints", UNSET)

        team_differential = d.pop("teamDifferential", UNSET)

        team_differential_home = d.pop("teamDifferentialHome", UNSET)

        team_differential_away = d.pop("teamDifferentialAway", UNSET)

        games_behind = d.pop("gamesBehind", UNSET)

        standing_points = d.pop("standingPoints", UNSET)

        standing_points_home = d.pop("standingPointsHome", UNSET)

        standing_points_away = d.pop("standingPointsAway", UNSET)

        standing_points_given = d.pop("standingPointsGiven", UNSET)

        standing_post_body_points_additional_property = cls(
            bonus_standing_points=bonus_standing_points,
            penalty_standing_points=penalty_standing_points,
            bye_standing_points=bye_standing_points,
            team_differential=team_differential,
            team_differential_home=team_differential_home,
            team_differential_away=team_differential_away,
            games_behind=games_behind,
            standing_points=standing_points,
            standing_points_home=standing_points_home,
            standing_points_away=standing_points_away,
            standing_points_given=standing_points_given,
        )

        return standing_post_body_points_additional_property
