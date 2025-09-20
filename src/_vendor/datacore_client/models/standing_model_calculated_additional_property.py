from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StandingModelCalculatedAdditionalProperty")


@_attrs_define
class StandingModelCalculatedAdditionalProperty:
    """Type of points

    Example:
        default

    Attributes:
        played (Union[Unset, float]): Fixtures played
        played_home (Union[Unset, float]): Fixtures played at home
        played_away (Union[Unset, float]): Fixtures played away
        washouts (Union[Unset, float]): Number of washed out fixtures
        wins (Union[Unset, float]): Fixtures Won
        wins_home (Union[Unset, float]): Fixtures Won at home
        wins_away (Union[Unset, float]): Fixtures Won away
        wins_secondary_score (Union[Unset, float]): Fixtures Won via Secondary Score
        wins_secondary_score_home (Union[Unset, float]): Fixtures Won at home via Secondary Score
        wins_secondary_score_away (Union[Unset, float]): Fixtures Won away via Secondary Score
        losses (Union[Unset, float]): Fixtures Lost
        losses_home (Union[Unset, float]): Fixtures Lost at home
        losses_away (Union[Unset, float]): Fixtures Lost away
        losses_secondary_score (Union[Unset, float]): Fixtures Lost via Secondary Score
        losses_secondary_score_home (Union[Unset, float]): Fixtures Lost at home via Secondary Score
        losses_secondary_score_away (Union[Unset, float]): Fixtures Lost away via Secondary Score
        draws (Union[Unset, float]): Fixtures Drawn
        draws_home (Union[Unset, float]): Fixtures Drawn at home
        draws_away (Union[Unset, float]): Fixtures Drawn away
        byes (Union[Unset, float]): Fixtures Byes
        forfeits_given (Union[Unset, float]): Fixtures Forfeits Given
        forfeits_won_by (Union[Unset, float]): Fixtures Forfeits Won
        win_percentage_display (Union[Unset, float]): Win Percentage (wins/played) (Display Value)
        win_percentage_home_display (Union[Unset, float]): Win Percentage Home (wins/played) (Display Value)
        win_percentage_away_display (Union[Unset, float]): Win Percentage Away (wins/played) (Display Value)
        win_percentage (Union[Unset, float]): Win Percentage (wins/played)
        win_percentage_home (Union[Unset, float]): Win Percentage Home (wins/played)
        win_percentage_away (Union[Unset, float]): Win Percentage Away (wins/played)
        scored_for (Union[Unset, float]): Scored For
        scored_for_home (Union[Unset, float]): Scored For at home
        scored_for_away (Union[Unset, float]): Scored For away
        scored_for_average (Union[Unset, float]): Scored For Average
        scored_for_home_average (Union[Unset, float]): Scored For Average at home
        scored_for_away_average (Union[Unset, float]): Scored For Average away
        scored_against (Union[Unset, float]): Scored Against
        scored_against_home (Union[Unset, float]): Scored Against at home
        scored_against_away (Union[Unset, float]): Scored Against away
        scored_against_average (Union[Unset, float]): Scored Against Average
        scored_against_home_average (Union[Unset, float]): Scored Against Average at home
        scored_against_away_average (Union[Unset, float]): Scored Against Average away
        percentage_display (Union[Unset, float]): For versus Against (Display Value)
        percentage_home_display (Union[Unset, float]): For versus Against at home (Display Value)
        percentage_away_display (Union[Unset, float]): For versus Against away (Display Value)
        percentage (Union[Unset, float]): For versus Against
        percentage_home (Union[Unset, float]): For versus Against at home
        percentage_away (Union[Unset, float]): For versus Against away
        point_difference (Union[Unset, float]): Point Difference for competitor
        point_difference_home (Union[Unset, float]): Point Difference for competitor at Home
        point_difference_away (Union[Unset, float]): Point Difference for competitor away
        lowest_score_for (Union[None, Unset, float]): Lowest Score for competitor
        lowest_score_for_home (Union[None, Unset, float]): Lowest Score for competitor at Home
        lowest_score_for_away (Union[None, Unset, float]): Lowest Score for competitor away
        highest_score_for (Union[None, Unset, float]): Highest Score for competitor
        highest_score_for_home (Union[None, Unset, float]): Highest Score for competitor at Home
        highest_score_for_away (Union[None, Unset, float]): Highest Score for competitor away
        lowest_score_against (Union[None, Unset, float]): Lowest Score against competitor
        lowest_score_against_home (Union[None, Unset, float]): Lowest Score against competitor at Home
        lowest_score_against_away (Union[None, Unset, float]): Lowest Score against competitor away
        highest_score_against (Union[None, Unset, float]): Highest Score against competitor
        highest_score_against_home (Union[None, Unset, float]): Highest Score against competitor at Home
        highest_score_against_away (Union[None, Unset, float]): Highest Score against competitor away
        streak (Union[Unset, float]): Winning streak for competitor
        streak_home (Union[Unset, float]): Winning streak for competitor at Home
        streak_away (Union[Unset, float]): Winning streak for competitor away
        result_string (Union[Unset, str]): Result string for competitor (W,L,D per match)
        result_string_home (Union[Unset, str]): Result string for competitor at Home (W,L,D per match)
        result_string_away (Union[Unset, str]): Result string for competitor away (W,L,D per match)
    """

    played: Union[Unset, float] = UNSET
    played_home: Union[Unset, float] = UNSET
    played_away: Union[Unset, float] = UNSET
    washouts: Union[Unset, float] = UNSET
    wins: Union[Unset, float] = UNSET
    wins_home: Union[Unset, float] = UNSET
    wins_away: Union[Unset, float] = UNSET
    wins_secondary_score: Union[Unset, float] = UNSET
    wins_secondary_score_home: Union[Unset, float] = UNSET
    wins_secondary_score_away: Union[Unset, float] = UNSET
    losses: Union[Unset, float] = UNSET
    losses_home: Union[Unset, float] = UNSET
    losses_away: Union[Unset, float] = UNSET
    losses_secondary_score: Union[Unset, float] = UNSET
    losses_secondary_score_home: Union[Unset, float] = UNSET
    losses_secondary_score_away: Union[Unset, float] = UNSET
    draws: Union[Unset, float] = UNSET
    draws_home: Union[Unset, float] = UNSET
    draws_away: Union[Unset, float] = UNSET
    byes: Union[Unset, float] = UNSET
    forfeits_given: Union[Unset, float] = UNSET
    forfeits_won_by: Union[Unset, float] = UNSET
    win_percentage_display: Union[Unset, float] = UNSET
    win_percentage_home_display: Union[Unset, float] = UNSET
    win_percentage_away_display: Union[Unset, float] = UNSET
    win_percentage: Union[Unset, float] = UNSET
    win_percentage_home: Union[Unset, float] = UNSET
    win_percentage_away: Union[Unset, float] = UNSET
    scored_for: Union[Unset, float] = UNSET
    scored_for_home: Union[Unset, float] = UNSET
    scored_for_away: Union[Unset, float] = UNSET
    scored_for_average: Union[Unset, float] = UNSET
    scored_for_home_average: Union[Unset, float] = UNSET
    scored_for_away_average: Union[Unset, float] = UNSET
    scored_against: Union[Unset, float] = UNSET
    scored_against_home: Union[Unset, float] = UNSET
    scored_against_away: Union[Unset, float] = UNSET
    scored_against_average: Union[Unset, float] = UNSET
    scored_against_home_average: Union[Unset, float] = UNSET
    scored_against_away_average: Union[Unset, float] = UNSET
    percentage_display: Union[Unset, float] = UNSET
    percentage_home_display: Union[Unset, float] = UNSET
    percentage_away_display: Union[Unset, float] = UNSET
    percentage: Union[Unset, float] = UNSET
    percentage_home: Union[Unset, float] = UNSET
    percentage_away: Union[Unset, float] = UNSET
    point_difference: Union[Unset, float] = UNSET
    point_difference_home: Union[Unset, float] = UNSET
    point_difference_away: Union[Unset, float] = UNSET
    lowest_score_for: Union[None, Unset, float] = UNSET
    lowest_score_for_home: Union[None, Unset, float] = UNSET
    lowest_score_for_away: Union[None, Unset, float] = UNSET
    highest_score_for: Union[None, Unset, float] = UNSET
    highest_score_for_home: Union[None, Unset, float] = UNSET
    highest_score_for_away: Union[None, Unset, float] = UNSET
    lowest_score_against: Union[None, Unset, float] = UNSET
    lowest_score_against_home: Union[None, Unset, float] = UNSET
    lowest_score_against_away: Union[None, Unset, float] = UNSET
    highest_score_against: Union[None, Unset, float] = UNSET
    highest_score_against_home: Union[None, Unset, float] = UNSET
    highest_score_against_away: Union[None, Unset, float] = UNSET
    streak: Union[Unset, float] = UNSET
    streak_home: Union[Unset, float] = UNSET
    streak_away: Union[Unset, float] = UNSET
    result_string: Union[Unset, str] = UNSET
    result_string_home: Union[Unset, str] = UNSET
    result_string_away: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        played = self.played

        played_home = self.played_home

        played_away = self.played_away

        washouts = self.washouts

        wins = self.wins

        wins_home = self.wins_home

        wins_away = self.wins_away

        wins_secondary_score = self.wins_secondary_score

        wins_secondary_score_home = self.wins_secondary_score_home

        wins_secondary_score_away = self.wins_secondary_score_away

        losses = self.losses

        losses_home = self.losses_home

        losses_away = self.losses_away

        losses_secondary_score = self.losses_secondary_score

        losses_secondary_score_home = self.losses_secondary_score_home

        losses_secondary_score_away = self.losses_secondary_score_away

        draws = self.draws

        draws_home = self.draws_home

        draws_away = self.draws_away

        byes = self.byes

        forfeits_given = self.forfeits_given

        forfeits_won_by = self.forfeits_won_by

        win_percentage_display = self.win_percentage_display

        win_percentage_home_display = self.win_percentage_home_display

        win_percentage_away_display = self.win_percentage_away_display

        win_percentage = self.win_percentage

        win_percentage_home = self.win_percentage_home

        win_percentage_away = self.win_percentage_away

        scored_for = self.scored_for

        scored_for_home = self.scored_for_home

        scored_for_away = self.scored_for_away

        scored_for_average = self.scored_for_average

        scored_for_home_average = self.scored_for_home_average

        scored_for_away_average = self.scored_for_away_average

        scored_against = self.scored_against

        scored_against_home = self.scored_against_home

        scored_against_away = self.scored_against_away

        scored_against_average = self.scored_against_average

        scored_against_home_average = self.scored_against_home_average

        scored_against_away_average = self.scored_against_away_average

        percentage_display = self.percentage_display

        percentage_home_display = self.percentage_home_display

        percentage_away_display = self.percentage_away_display

        percentage = self.percentage

        percentage_home = self.percentage_home

        percentage_away = self.percentage_away

        point_difference = self.point_difference

        point_difference_home = self.point_difference_home

        point_difference_away = self.point_difference_away

        lowest_score_for: Union[None, Unset, float]
        if isinstance(self.lowest_score_for, Unset):
            lowest_score_for = UNSET
        else:
            lowest_score_for = self.lowest_score_for

        lowest_score_for_home: Union[None, Unset, float]
        if isinstance(self.lowest_score_for_home, Unset):
            lowest_score_for_home = UNSET
        else:
            lowest_score_for_home = self.lowest_score_for_home

        lowest_score_for_away: Union[None, Unset, float]
        if isinstance(self.lowest_score_for_away, Unset):
            lowest_score_for_away = UNSET
        else:
            lowest_score_for_away = self.lowest_score_for_away

        highest_score_for: Union[None, Unset, float]
        if isinstance(self.highest_score_for, Unset):
            highest_score_for = UNSET
        else:
            highest_score_for = self.highest_score_for

        highest_score_for_home: Union[None, Unset, float]
        if isinstance(self.highest_score_for_home, Unset):
            highest_score_for_home = UNSET
        else:
            highest_score_for_home = self.highest_score_for_home

        highest_score_for_away: Union[None, Unset, float]
        if isinstance(self.highest_score_for_away, Unset):
            highest_score_for_away = UNSET
        else:
            highest_score_for_away = self.highest_score_for_away

        lowest_score_against: Union[None, Unset, float]
        if isinstance(self.lowest_score_against, Unset):
            lowest_score_against = UNSET
        else:
            lowest_score_against = self.lowest_score_against

        lowest_score_against_home: Union[None, Unset, float]
        if isinstance(self.lowest_score_against_home, Unset):
            lowest_score_against_home = UNSET
        else:
            lowest_score_against_home = self.lowest_score_against_home

        lowest_score_against_away: Union[None, Unset, float]
        if isinstance(self.lowest_score_against_away, Unset):
            lowest_score_against_away = UNSET
        else:
            lowest_score_against_away = self.lowest_score_against_away

        highest_score_against: Union[None, Unset, float]
        if isinstance(self.highest_score_against, Unset):
            highest_score_against = UNSET
        else:
            highest_score_against = self.highest_score_against

        highest_score_against_home: Union[None, Unset, float]
        if isinstance(self.highest_score_against_home, Unset):
            highest_score_against_home = UNSET
        else:
            highest_score_against_home = self.highest_score_against_home

        highest_score_against_away: Union[None, Unset, float]
        if isinstance(self.highest_score_against_away, Unset):
            highest_score_against_away = UNSET
        else:
            highest_score_against_away = self.highest_score_against_away

        streak = self.streak

        streak_home = self.streak_home

        streak_away = self.streak_away

        result_string = self.result_string

        result_string_home = self.result_string_home

        result_string_away = self.result_string_away

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if played is not UNSET:
            field_dict["played"] = played
        if played_home is not UNSET:
            field_dict["playedHome"] = played_home
        if played_away is not UNSET:
            field_dict["playedAway"] = played_away
        if washouts is not UNSET:
            field_dict["washouts"] = washouts
        if wins is not UNSET:
            field_dict["wins"] = wins
        if wins_home is not UNSET:
            field_dict["winsHome"] = wins_home
        if wins_away is not UNSET:
            field_dict["winsAway"] = wins_away
        if wins_secondary_score is not UNSET:
            field_dict["winsSecondaryScore"] = wins_secondary_score
        if wins_secondary_score_home is not UNSET:
            field_dict["winsSecondaryScoreHome"] = wins_secondary_score_home
        if wins_secondary_score_away is not UNSET:
            field_dict["winsSecondaryScoreAway"] = wins_secondary_score_away
        if losses is not UNSET:
            field_dict["losses"] = losses
        if losses_home is not UNSET:
            field_dict["lossesHome"] = losses_home
        if losses_away is not UNSET:
            field_dict["lossesAway"] = losses_away
        if losses_secondary_score is not UNSET:
            field_dict["lossesSecondaryScore"] = losses_secondary_score
        if losses_secondary_score_home is not UNSET:
            field_dict["lossesSecondaryScoreHome"] = losses_secondary_score_home
        if losses_secondary_score_away is not UNSET:
            field_dict["lossesSecondaryScoreAway"] = losses_secondary_score_away
        if draws is not UNSET:
            field_dict["draws"] = draws
        if draws_home is not UNSET:
            field_dict["drawsHome"] = draws_home
        if draws_away is not UNSET:
            field_dict["drawsAway"] = draws_away
        if byes is not UNSET:
            field_dict["byes"] = byes
        if forfeits_given is not UNSET:
            field_dict["forfeitsGiven"] = forfeits_given
        if forfeits_won_by is not UNSET:
            field_dict["forfeitsWonBy"] = forfeits_won_by
        if win_percentage_display is not UNSET:
            field_dict["winPercentageDisplay"] = win_percentage_display
        if win_percentage_home_display is not UNSET:
            field_dict["winPercentageHomeDisplay"] = win_percentage_home_display
        if win_percentage_away_display is not UNSET:
            field_dict["winPercentageAwayDisplay"] = win_percentage_away_display
        if win_percentage is not UNSET:
            field_dict["winPercentage"] = win_percentage
        if win_percentage_home is not UNSET:
            field_dict["winPercentageHome"] = win_percentage_home
        if win_percentage_away is not UNSET:
            field_dict["winPercentageAway"] = win_percentage_away
        if scored_for is not UNSET:
            field_dict["scoredFor"] = scored_for
        if scored_for_home is not UNSET:
            field_dict["scoredForHome"] = scored_for_home
        if scored_for_away is not UNSET:
            field_dict["scoredForAway"] = scored_for_away
        if scored_for_average is not UNSET:
            field_dict["scoredForAverage"] = scored_for_average
        if scored_for_home_average is not UNSET:
            field_dict["scoredForHomeAverage"] = scored_for_home_average
        if scored_for_away_average is not UNSET:
            field_dict["scoredForAwayAverage"] = scored_for_away_average
        if scored_against is not UNSET:
            field_dict["scoredAgainst"] = scored_against
        if scored_against_home is not UNSET:
            field_dict["scoredAgainstHome"] = scored_against_home
        if scored_against_away is not UNSET:
            field_dict["scoredAgainstAway"] = scored_against_away
        if scored_against_average is not UNSET:
            field_dict["scoredAgainstAverage"] = scored_against_average
        if scored_against_home_average is not UNSET:
            field_dict["scoredAgainstHomeAverage"] = scored_against_home_average
        if scored_against_away_average is not UNSET:
            field_dict["scoredAgainstAwayAverage"] = scored_against_away_average
        if percentage_display is not UNSET:
            field_dict["percentageDisplay"] = percentage_display
        if percentage_home_display is not UNSET:
            field_dict["percentageHomeDisplay"] = percentage_home_display
        if percentage_away_display is not UNSET:
            field_dict["percentageAwayDisplay"] = percentage_away_display
        if percentage is not UNSET:
            field_dict["percentage"] = percentage
        if percentage_home is not UNSET:
            field_dict["percentageHome"] = percentage_home
        if percentage_away is not UNSET:
            field_dict["percentageAway"] = percentage_away
        if point_difference is not UNSET:
            field_dict["pointDifference"] = point_difference
        if point_difference_home is not UNSET:
            field_dict["pointDifferenceHome"] = point_difference_home
        if point_difference_away is not UNSET:
            field_dict["pointDifferenceAway"] = point_difference_away
        if lowest_score_for is not UNSET:
            field_dict["lowestScoreFor"] = lowest_score_for
        if lowest_score_for_home is not UNSET:
            field_dict["lowestScoreForHome"] = lowest_score_for_home
        if lowest_score_for_away is not UNSET:
            field_dict["lowestScoreForAway"] = lowest_score_for_away
        if highest_score_for is not UNSET:
            field_dict["highestScoreFor"] = highest_score_for
        if highest_score_for_home is not UNSET:
            field_dict["highestScoreForHome"] = highest_score_for_home
        if highest_score_for_away is not UNSET:
            field_dict["highestScoreForAway"] = highest_score_for_away
        if lowest_score_against is not UNSET:
            field_dict["lowestScoreAgainst"] = lowest_score_against
        if lowest_score_against_home is not UNSET:
            field_dict["lowestScoreAgainstHome"] = lowest_score_against_home
        if lowest_score_against_away is not UNSET:
            field_dict["lowestScoreAgainstAway"] = lowest_score_against_away
        if highest_score_against is not UNSET:
            field_dict["highestScoreAgainst"] = highest_score_against
        if highest_score_against_home is not UNSET:
            field_dict["highestScoreAgainstHome"] = highest_score_against_home
        if highest_score_against_away is not UNSET:
            field_dict["highestScoreAgainstAway"] = highest_score_against_away
        if streak is not UNSET:
            field_dict["streak"] = streak
        if streak_home is not UNSET:
            field_dict["streakHome"] = streak_home
        if streak_away is not UNSET:
            field_dict["streakAway"] = streak_away
        if result_string is not UNSET:
            field_dict["resultString"] = result_string
        if result_string_home is not UNSET:
            field_dict["resultStringHome"] = result_string_home
        if result_string_away is not UNSET:
            field_dict["resultStringAway"] = result_string_away

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        played = d.pop("played", UNSET)

        played_home = d.pop("playedHome", UNSET)

        played_away = d.pop("playedAway", UNSET)

        washouts = d.pop("washouts", UNSET)

        wins = d.pop("wins", UNSET)

        wins_home = d.pop("winsHome", UNSET)

        wins_away = d.pop("winsAway", UNSET)

        wins_secondary_score = d.pop("winsSecondaryScore", UNSET)

        wins_secondary_score_home = d.pop("winsSecondaryScoreHome", UNSET)

        wins_secondary_score_away = d.pop("winsSecondaryScoreAway", UNSET)

        losses = d.pop("losses", UNSET)

        losses_home = d.pop("lossesHome", UNSET)

        losses_away = d.pop("lossesAway", UNSET)

        losses_secondary_score = d.pop("lossesSecondaryScore", UNSET)

        losses_secondary_score_home = d.pop("lossesSecondaryScoreHome", UNSET)

        losses_secondary_score_away = d.pop("lossesSecondaryScoreAway", UNSET)

        draws = d.pop("draws", UNSET)

        draws_home = d.pop("drawsHome", UNSET)

        draws_away = d.pop("drawsAway", UNSET)

        byes = d.pop("byes", UNSET)

        forfeits_given = d.pop("forfeitsGiven", UNSET)

        forfeits_won_by = d.pop("forfeitsWonBy", UNSET)

        win_percentage_display = d.pop("winPercentageDisplay", UNSET)

        win_percentage_home_display = d.pop("winPercentageHomeDisplay", UNSET)

        win_percentage_away_display = d.pop("winPercentageAwayDisplay", UNSET)

        win_percentage = d.pop("winPercentage", UNSET)

        win_percentage_home = d.pop("winPercentageHome", UNSET)

        win_percentage_away = d.pop("winPercentageAway", UNSET)

        scored_for = d.pop("scoredFor", UNSET)

        scored_for_home = d.pop("scoredForHome", UNSET)

        scored_for_away = d.pop("scoredForAway", UNSET)

        scored_for_average = d.pop("scoredForAverage", UNSET)

        scored_for_home_average = d.pop("scoredForHomeAverage", UNSET)

        scored_for_away_average = d.pop("scoredForAwayAverage", UNSET)

        scored_against = d.pop("scoredAgainst", UNSET)

        scored_against_home = d.pop("scoredAgainstHome", UNSET)

        scored_against_away = d.pop("scoredAgainstAway", UNSET)

        scored_against_average = d.pop("scoredAgainstAverage", UNSET)

        scored_against_home_average = d.pop("scoredAgainstHomeAverage", UNSET)

        scored_against_away_average = d.pop("scoredAgainstAwayAverage", UNSET)

        percentage_display = d.pop("percentageDisplay", UNSET)

        percentage_home_display = d.pop("percentageHomeDisplay", UNSET)

        percentage_away_display = d.pop("percentageAwayDisplay", UNSET)

        percentage = d.pop("percentage", UNSET)

        percentage_home = d.pop("percentageHome", UNSET)

        percentage_away = d.pop("percentageAway", UNSET)

        point_difference = d.pop("pointDifference", UNSET)

        point_difference_home = d.pop("pointDifferenceHome", UNSET)

        point_difference_away = d.pop("pointDifferenceAway", UNSET)

        def _parse_lowest_score_for(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest_score_for = _parse_lowest_score_for(d.pop("lowestScoreFor", UNSET))

        def _parse_lowest_score_for_home(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest_score_for_home = _parse_lowest_score_for_home(
            d.pop("lowestScoreForHome", UNSET)
        )

        def _parse_lowest_score_for_away(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest_score_for_away = _parse_lowest_score_for_away(
            d.pop("lowestScoreForAway", UNSET)
        )

        def _parse_highest_score_for(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        highest_score_for = _parse_highest_score_for(d.pop("highestScoreFor", UNSET))

        def _parse_highest_score_for_home(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        highest_score_for_home = _parse_highest_score_for_home(
            d.pop("highestScoreForHome", UNSET)
        )

        def _parse_highest_score_for_away(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        highest_score_for_away = _parse_highest_score_for_away(
            d.pop("highestScoreForAway", UNSET)
        )

        def _parse_lowest_score_against(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest_score_against = _parse_lowest_score_against(
            d.pop("lowestScoreAgainst", UNSET)
        )

        def _parse_lowest_score_against_home(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest_score_against_home = _parse_lowest_score_against_home(
            d.pop("lowestScoreAgainstHome", UNSET)
        )

        def _parse_lowest_score_against_away(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        lowest_score_against_away = _parse_lowest_score_against_away(
            d.pop("lowestScoreAgainstAway", UNSET)
        )

        def _parse_highest_score_against(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        highest_score_against = _parse_highest_score_against(
            d.pop("highestScoreAgainst", UNSET)
        )

        def _parse_highest_score_against_home(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        highest_score_against_home = _parse_highest_score_against_home(
            d.pop("highestScoreAgainstHome", UNSET)
        )

        def _parse_highest_score_against_away(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        highest_score_against_away = _parse_highest_score_against_away(
            d.pop("highestScoreAgainstAway", UNSET)
        )

        streak = d.pop("streak", UNSET)

        streak_home = d.pop("streakHome", UNSET)

        streak_away = d.pop("streakAway", UNSET)

        result_string = d.pop("resultString", UNSET)

        result_string_home = d.pop("resultStringHome", UNSET)

        result_string_away = d.pop("resultStringAway", UNSET)

        standing_model_calculated_additional_property = cls(
            played=played,
            played_home=played_home,
            played_away=played_away,
            washouts=washouts,
            wins=wins,
            wins_home=wins_home,
            wins_away=wins_away,
            wins_secondary_score=wins_secondary_score,
            wins_secondary_score_home=wins_secondary_score_home,
            wins_secondary_score_away=wins_secondary_score_away,
            losses=losses,
            losses_home=losses_home,
            losses_away=losses_away,
            losses_secondary_score=losses_secondary_score,
            losses_secondary_score_home=losses_secondary_score_home,
            losses_secondary_score_away=losses_secondary_score_away,
            draws=draws,
            draws_home=draws_home,
            draws_away=draws_away,
            byes=byes,
            forfeits_given=forfeits_given,
            forfeits_won_by=forfeits_won_by,
            win_percentage_display=win_percentage_display,
            win_percentage_home_display=win_percentage_home_display,
            win_percentage_away_display=win_percentage_away_display,
            win_percentage=win_percentage,
            win_percentage_home=win_percentage_home,
            win_percentage_away=win_percentage_away,
            scored_for=scored_for,
            scored_for_home=scored_for_home,
            scored_for_away=scored_for_away,
            scored_for_average=scored_for_average,
            scored_for_home_average=scored_for_home_average,
            scored_for_away_average=scored_for_away_average,
            scored_against=scored_against,
            scored_against_home=scored_against_home,
            scored_against_away=scored_against_away,
            scored_against_average=scored_against_average,
            scored_against_home_average=scored_against_home_average,
            scored_against_away_average=scored_against_away_average,
            percentage_display=percentage_display,
            percentage_home_display=percentage_home_display,
            percentage_away_display=percentage_away_display,
            percentage=percentage,
            percentage_home=percentage_home,
            percentage_away=percentage_away,
            point_difference=point_difference,
            point_difference_home=point_difference_home,
            point_difference_away=point_difference_away,
            lowest_score_for=lowest_score_for,
            lowest_score_for_home=lowest_score_for_home,
            lowest_score_for_away=lowest_score_for_away,
            highest_score_for=highest_score_for,
            highest_score_for_home=highest_score_for_home,
            highest_score_for_away=highest_score_for_away,
            lowest_score_against=lowest_score_against,
            lowest_score_against_home=lowest_score_against_home,
            lowest_score_against_away=lowest_score_against_away,
            highest_score_against=highest_score_against,
            highest_score_against_home=highest_score_against_home,
            highest_score_against_away=highest_score_against_away,
            streak=streak,
            streak_home=streak_home,
            streak_away=streak_away,
            result_string=result_string,
            result_string_home=result_string_home,
            result_string_away=result_string_away,
        )

        return standing_model_calculated_additional_property
