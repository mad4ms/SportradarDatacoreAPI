from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_streak import (
    StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationStreak,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_identification import (
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentification,
    )
    from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_identification_for_subsequent_checks import (
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentificationForSubsequentChecks,
    )
    from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_resolution import (
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolution,
    )
    from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_resolution_for_extra_depth_h2_hs import (
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2Hs,
    )
    from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_sorting import (
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationSorting,
    )


T = TypeVar(
    "T",
    bound="StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration",
)


@_attrs_define
class StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration:
    """Configuration definitions

    Attributes:
        losses_secondary_score_home_points (Union[Unset, float]): Points for Home Loss by Secondary Score
        losses_secondary_score_away_points (Union[Unset, float]): Points for Away Loss by Secondary Score
        wins_secondary_score_home_points (Union[Unset, float]): Points for Home Win by Secondary Score
        wins_secondary_score_away_points (Union[Unset, float]): Points for Away Win by Secondary Score
        wins_home_points (Union[Unset, float]): Points for Home Win
        losses_home_points (Union[Unset, float]): Points for Home Loss
        draws_home_scored_points (Union[Unset, float]): Points for Home Draw where team scored
        draws_home_zero_points (Union[Unset, float]): Points for Home Draw with zero score
        forfeit_won_by_home_points (Union[Unset, float]): Points for won by Forfeit at home
        forfeits_won_by_home_points (Union[Unset, float]): Points for won by Forfeit at home
        forfeit_given_home_points (Union[Unset, float]): Points for giving a forfeit at home
        wins_away_points (Union[Unset, float]): Points for Away Win
        losses_away_points (Union[Unset, float]): Points for Away Loss
        draws_away_scored_points (Union[Unset, float]): Points for Away Draw where team scored
        draws_away_zero_points (Union[Unset, float]): Points for Away Draw with zero score
        forfeit_won_by_away_points (Union[Unset, float]): Points for won by Forfeit at away
        forfeit_given_away_points (Union[Unset, float]): Points for giving a forfeit at away
        secondary_score_draw_as_result (Union[Unset, bool]): Is a secondary Score result a game result (resultPlace was
            a Draw)?
        check_secondary_scores (Union[Unset, bool]): Check Secondary Score for calculations
        bye_points (Union[Unset, float]): Points for bye
        bye_is_played (Union[Unset, bool]): Is a Bye added to played ?
        bye_added_wins (Union[Unset, bool]): Is a Bye added to won count?
        forfeit_won_by_added_wins (Union[Unset, bool]): Is a forfeit won by (received) included in won count ?
        forfeit_won_by_added_played (Union[Unset, bool]): Is a forfeit won by (received) included in played count ?
        forfeit_given_added_losses (Union[Unset, bool]): Is a forfeit given included in losses count ?
        forfeit_given_added_played (Union[Unset, bool]): Is a forfeit given included in played count ?
        streak (Union[Unset, StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationStreak]): How
            is a streak calculated ?
        sorts (Union[Unset,
            list['StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationSorting']]): Sortings
        head_to_head_identification (Union[Unset, list['StandingConfigurationsUpdateStandingConfigurationsPutBodyStandin
            gConfigurationHeadToHeadIdentification']]): Head to head identifications
        head_to_head_identification_subsequent (Union[Unset, list['StandingConfigurationsUpdateStandingConfigurationsPut
            BodyStandingConfigurationHeadToHeadIdentificationForSubsequentChecks']]): Head to head identifications for
            subsequent checks
        head_to_head_use_all_fixtures (Union[Unset, bool]): Use all fixtures in Head to head resolutions regardless of
            Stage & Pool?
        head_to_head_use_adjustments (Union[Unset, bool]): Apply Standing Adjustments when performing Head to head
            resolutions?
        head_to_head_single_round (Union[Unset, bool]): Only use single round for Head to head resolutions?
        head_to_head_resolutions (Union[Unset,
            list['StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolution']]):
            Head to head resolutions
        head_to_head_resolutions_subsequent (Union[Unset, list['StandingConfigurationsUpdateStandingConfigurationsPutBod
            yStandingConfigurationHeadToHeadResolutionForExtraDepthH2Hs']]): Head to head resolutions for extra depth h2h's
    """

    losses_secondary_score_home_points: Union[Unset, float] = UNSET
    losses_secondary_score_away_points: Union[Unset, float] = UNSET
    wins_secondary_score_home_points: Union[Unset, float] = UNSET
    wins_secondary_score_away_points: Union[Unset, float] = UNSET
    wins_home_points: Union[Unset, float] = UNSET
    losses_home_points: Union[Unset, float] = UNSET
    draws_home_scored_points: Union[Unset, float] = UNSET
    draws_home_zero_points: Union[Unset, float] = UNSET
    forfeit_won_by_home_points: Union[Unset, float] = UNSET
    forfeits_won_by_home_points: Union[Unset, float] = UNSET
    forfeit_given_home_points: Union[Unset, float] = UNSET
    wins_away_points: Union[Unset, float] = UNSET
    losses_away_points: Union[Unset, float] = UNSET
    draws_away_scored_points: Union[Unset, float] = UNSET
    draws_away_zero_points: Union[Unset, float] = UNSET
    forfeit_won_by_away_points: Union[Unset, float] = UNSET
    forfeit_given_away_points: Union[Unset, float] = UNSET
    secondary_score_draw_as_result: Union[Unset, bool] = UNSET
    check_secondary_scores: Union[Unset, bool] = UNSET
    bye_points: Union[Unset, float] = UNSET
    bye_is_played: Union[Unset, bool] = UNSET
    bye_added_wins: Union[Unset, bool] = UNSET
    forfeit_won_by_added_wins: Union[Unset, bool] = UNSET
    forfeit_won_by_added_played: Union[Unset, bool] = UNSET
    forfeit_given_added_losses: Union[Unset, bool] = UNSET
    forfeit_given_added_played: Union[Unset, bool] = UNSET
    streak: Union[
        Unset,
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationStreak,
    ] = UNSET
    sorts: Union[
        Unset,
        list[
            "StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationSorting"
        ],
    ] = UNSET
    head_to_head_identification: Union[
        Unset,
        list[
            "StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentification"
        ],
    ] = UNSET
    head_to_head_identification_subsequent: Union[
        Unset,
        list[
            "StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentificationForSubsequentChecks"
        ],
    ] = UNSET
    head_to_head_use_all_fixtures: Union[Unset, bool] = UNSET
    head_to_head_use_adjustments: Union[Unset, bool] = UNSET
    head_to_head_single_round: Union[Unset, bool] = UNSET
    head_to_head_resolutions: Union[
        Unset,
        list[
            "StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolution"
        ],
    ] = UNSET
    head_to_head_resolutions_subsequent: Union[
        Unset,
        list[
            "StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2Hs"
        ],
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        losses_secondary_score_home_points = self.losses_secondary_score_home_points

        losses_secondary_score_away_points = self.losses_secondary_score_away_points

        wins_secondary_score_home_points = self.wins_secondary_score_home_points

        wins_secondary_score_away_points = self.wins_secondary_score_away_points

        wins_home_points = self.wins_home_points

        losses_home_points = self.losses_home_points

        draws_home_scored_points = self.draws_home_scored_points

        draws_home_zero_points = self.draws_home_zero_points

        forfeit_won_by_home_points = self.forfeit_won_by_home_points

        forfeits_won_by_home_points = self.forfeits_won_by_home_points

        forfeit_given_home_points = self.forfeit_given_home_points

        wins_away_points = self.wins_away_points

        losses_away_points = self.losses_away_points

        draws_away_scored_points = self.draws_away_scored_points

        draws_away_zero_points = self.draws_away_zero_points

        forfeit_won_by_away_points = self.forfeit_won_by_away_points

        forfeit_given_away_points = self.forfeit_given_away_points

        secondary_score_draw_as_result = self.secondary_score_draw_as_result

        check_secondary_scores = self.check_secondary_scores

        bye_points = self.bye_points

        bye_is_played = self.bye_is_played

        bye_added_wins = self.bye_added_wins

        forfeit_won_by_added_wins = self.forfeit_won_by_added_wins

        forfeit_won_by_added_played = self.forfeit_won_by_added_played

        forfeit_given_added_losses = self.forfeit_given_added_losses

        forfeit_given_added_played = self.forfeit_given_added_played

        streak: Union[Unset, str] = UNSET
        if not isinstance(self.streak, Unset):
            streak = self.streak.value

        sorts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sorts, Unset):
            sorts = []
            for sorts_item_data in self.sorts:
                sorts_item = sorts_item_data.to_dict()
                sorts.append(sorts_item)

        head_to_head_identification: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.head_to_head_identification, Unset):
            head_to_head_identification = []
            for (
                head_to_head_identification_item_data
            ) in self.head_to_head_identification:
                head_to_head_identification_item = (
                    head_to_head_identification_item_data.to_dict()
                )
                head_to_head_identification.append(head_to_head_identification_item)

        head_to_head_identification_subsequent: Union[Unset, list[dict[str, Any]]] = (
            UNSET
        )
        if not isinstance(self.head_to_head_identification_subsequent, Unset):
            head_to_head_identification_subsequent = []
            for (
                head_to_head_identification_subsequent_item_data
            ) in self.head_to_head_identification_subsequent:
                head_to_head_identification_subsequent_item = (
                    head_to_head_identification_subsequent_item_data.to_dict()
                )
                head_to_head_identification_subsequent.append(
                    head_to_head_identification_subsequent_item
                )

        head_to_head_use_all_fixtures = self.head_to_head_use_all_fixtures

        head_to_head_use_adjustments = self.head_to_head_use_adjustments

        head_to_head_single_round = self.head_to_head_single_round

        head_to_head_resolutions: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.head_to_head_resolutions, Unset):
            head_to_head_resolutions = []
            for head_to_head_resolutions_item_data in self.head_to_head_resolutions:
                head_to_head_resolutions_item = (
                    head_to_head_resolutions_item_data.to_dict()
                )
                head_to_head_resolutions.append(head_to_head_resolutions_item)

        head_to_head_resolutions_subsequent: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.head_to_head_resolutions_subsequent, Unset):
            head_to_head_resolutions_subsequent = []
            for (
                head_to_head_resolutions_subsequent_item_data
            ) in self.head_to_head_resolutions_subsequent:
                head_to_head_resolutions_subsequent_item = (
                    head_to_head_resolutions_subsequent_item_data.to_dict()
                )
                head_to_head_resolutions_subsequent.append(
                    head_to_head_resolutions_subsequent_item
                )

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if losses_secondary_score_home_points is not UNSET:
            field_dict["lossesSecondaryScoreHomePoints"] = (
                losses_secondary_score_home_points
            )
        if losses_secondary_score_away_points is not UNSET:
            field_dict["lossesSecondaryScoreAwayPoints"] = (
                losses_secondary_score_away_points
            )
        if wins_secondary_score_home_points is not UNSET:
            field_dict["winsSecondaryScoreHomePoints"] = (
                wins_secondary_score_home_points
            )
        if wins_secondary_score_away_points is not UNSET:
            field_dict["winsSecondaryScoreAwayPoints"] = (
                wins_secondary_score_away_points
            )
        if wins_home_points is not UNSET:
            field_dict["winsHomePoints"] = wins_home_points
        if losses_home_points is not UNSET:
            field_dict["lossesHomePoints"] = losses_home_points
        if draws_home_scored_points is not UNSET:
            field_dict["drawsHomeScoredPoints"] = draws_home_scored_points
        if draws_home_zero_points is not UNSET:
            field_dict["drawsHomeZeroPoints"] = draws_home_zero_points
        if forfeit_won_by_home_points is not UNSET:
            field_dict["forfeitWonByHomePoints"] = forfeit_won_by_home_points
        if forfeits_won_by_home_points is not UNSET:
            field_dict["forfeitsWonByHomePoints"] = forfeits_won_by_home_points
        if forfeit_given_home_points is not UNSET:
            field_dict["forfeitGivenHomePoints"] = forfeit_given_home_points
        if wins_away_points is not UNSET:
            field_dict["winsAwayPoints"] = wins_away_points
        if losses_away_points is not UNSET:
            field_dict["lossesAwayPoints"] = losses_away_points
        if draws_away_scored_points is not UNSET:
            field_dict["drawsAwayScoredPoints"] = draws_away_scored_points
        if draws_away_zero_points is not UNSET:
            field_dict["drawsAwayZeroPoints"] = draws_away_zero_points
        if forfeit_won_by_away_points is not UNSET:
            field_dict["forfeitWonByAwayPoints"] = forfeit_won_by_away_points
        if forfeit_given_away_points is not UNSET:
            field_dict["forfeitGivenAwayPoints"] = forfeit_given_away_points
        if secondary_score_draw_as_result is not UNSET:
            field_dict["secondaryScoreDrawAsResult"] = secondary_score_draw_as_result
        if check_secondary_scores is not UNSET:
            field_dict["checkSecondaryScores"] = check_secondary_scores
        if bye_points is not UNSET:
            field_dict["byePoints"] = bye_points
        if bye_is_played is not UNSET:
            field_dict["byeIsPlayed"] = bye_is_played
        if bye_added_wins is not UNSET:
            field_dict["byeAddedWins"] = bye_added_wins
        if forfeit_won_by_added_wins is not UNSET:
            field_dict["forfeitWonByAddedWins"] = forfeit_won_by_added_wins
        if forfeit_won_by_added_played is not UNSET:
            field_dict["forfeitWonByAddedPlayed"] = forfeit_won_by_added_played
        if forfeit_given_added_losses is not UNSET:
            field_dict["forfeitGivenAddedLosses"] = forfeit_given_added_losses
        if forfeit_given_added_played is not UNSET:
            field_dict["forfeitGivenAddedPlayed"] = forfeit_given_added_played
        if streak is not UNSET:
            field_dict["streak"] = streak
        if sorts is not UNSET:
            field_dict["sorts"] = sorts
        if head_to_head_identification is not UNSET:
            field_dict["headToHeadIdentification"] = head_to_head_identification
        if head_to_head_identification_subsequent is not UNSET:
            field_dict["headToHeadIdentificationSubsequent"] = (
                head_to_head_identification_subsequent
            )
        if head_to_head_use_all_fixtures is not UNSET:
            field_dict["headToHeadUseAllFixtures"] = head_to_head_use_all_fixtures
        if head_to_head_use_adjustments is not UNSET:
            field_dict["headToHeadUseAdjustments"] = head_to_head_use_adjustments
        if head_to_head_single_round is not UNSET:
            field_dict["headToHeadSingleRound"] = head_to_head_single_round
        if head_to_head_resolutions is not UNSET:
            field_dict["headToHeadResolutions"] = head_to_head_resolutions
        if head_to_head_resolutions_subsequent is not UNSET:
            field_dict["headToHeadResolutionsSubsequent"] = (
                head_to_head_resolutions_subsequent
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_identification import (
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentification,
        )
        from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_identification_for_subsequent_checks import (
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentificationForSubsequentChecks,
        )
        from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_resolution import (
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolution,
        )
        from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_resolution_for_extra_depth_h2_hs import (
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2Hs,
        )
        from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_sorting import (
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationSorting,
        )

        d = dict(src_dict)
        losses_secondary_score_home_points = d.pop(
            "lossesSecondaryScoreHomePoints", UNSET
        )

        losses_secondary_score_away_points = d.pop(
            "lossesSecondaryScoreAwayPoints", UNSET
        )

        wins_secondary_score_home_points = d.pop("winsSecondaryScoreHomePoints", UNSET)

        wins_secondary_score_away_points = d.pop("winsSecondaryScoreAwayPoints", UNSET)

        wins_home_points = d.pop("winsHomePoints", UNSET)

        losses_home_points = d.pop("lossesHomePoints", UNSET)

        draws_home_scored_points = d.pop("drawsHomeScoredPoints", UNSET)

        draws_home_zero_points = d.pop("drawsHomeZeroPoints", UNSET)

        forfeit_won_by_home_points = d.pop("forfeitWonByHomePoints", UNSET)

        forfeits_won_by_home_points = d.pop("forfeitsWonByHomePoints", UNSET)

        forfeit_given_home_points = d.pop("forfeitGivenHomePoints", UNSET)

        wins_away_points = d.pop("winsAwayPoints", UNSET)

        losses_away_points = d.pop("lossesAwayPoints", UNSET)

        draws_away_scored_points = d.pop("drawsAwayScoredPoints", UNSET)

        draws_away_zero_points = d.pop("drawsAwayZeroPoints", UNSET)

        forfeit_won_by_away_points = d.pop("forfeitWonByAwayPoints", UNSET)

        forfeit_given_away_points = d.pop("forfeitGivenAwayPoints", UNSET)

        secondary_score_draw_as_result = d.pop("secondaryScoreDrawAsResult", UNSET)

        check_secondary_scores = d.pop("checkSecondaryScores", UNSET)

        bye_points = d.pop("byePoints", UNSET)

        bye_is_played = d.pop("byeIsPlayed", UNSET)

        bye_added_wins = d.pop("byeAddedWins", UNSET)

        forfeit_won_by_added_wins = d.pop("forfeitWonByAddedWins", UNSET)

        forfeit_won_by_added_played = d.pop("forfeitWonByAddedPlayed", UNSET)

        forfeit_given_added_losses = d.pop("forfeitGivenAddedLosses", UNSET)

        forfeit_given_added_played = d.pop("forfeitGivenAddedPlayed", UNSET)

        _streak = d.pop("streak", UNSET)
        streak: Union[
            Unset,
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationStreak,
        ]
        if isinstance(_streak, Unset):
            streak = UNSET
        else:
            streak = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationStreak(
                _streak
            )

        sorts = []
        _sorts = d.pop("sorts", UNSET)
        for sorts_item_data in _sorts or []:
            sorts_item = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationSorting.from_dict(
                sorts_item_data
            )

            sorts.append(sorts_item)

        head_to_head_identification = []
        _head_to_head_identification = d.pop("headToHeadIdentification", UNSET)
        for head_to_head_identification_item_data in _head_to_head_identification or []:
            head_to_head_identification_item = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentification.from_dict(
                head_to_head_identification_item_data
            )

            head_to_head_identification.append(head_to_head_identification_item)

        head_to_head_identification_subsequent = []
        _head_to_head_identification_subsequent = d.pop(
            "headToHeadIdentificationSubsequent", UNSET
        )
        for head_to_head_identification_subsequent_item_data in (
            _head_to_head_identification_subsequent or []
        ):
            head_to_head_identification_subsequent_item = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadIdentificationForSubsequentChecks.from_dict(
                head_to_head_identification_subsequent_item_data
            )

            head_to_head_identification_subsequent.append(
                head_to_head_identification_subsequent_item
            )

        head_to_head_use_all_fixtures = d.pop("headToHeadUseAllFixtures", UNSET)

        head_to_head_use_adjustments = d.pop("headToHeadUseAdjustments", UNSET)

        head_to_head_single_round = d.pop("headToHeadSingleRound", UNSET)

        head_to_head_resolutions = []
        _head_to_head_resolutions = d.pop("headToHeadResolutions", UNSET)
        for head_to_head_resolutions_item_data in _head_to_head_resolutions or []:
            head_to_head_resolutions_item = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolution.from_dict(
                head_to_head_resolutions_item_data
            )

            head_to_head_resolutions.append(head_to_head_resolutions_item)

        head_to_head_resolutions_subsequent = []
        _head_to_head_resolutions_subsequent = d.pop(
            "headToHeadResolutionsSubsequent", UNSET
        )
        for head_to_head_resolutions_subsequent_item_data in (
            _head_to_head_resolutions_subsequent or []
        ):
            head_to_head_resolutions_subsequent_item = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2Hs.from_dict(
                head_to_head_resolutions_subsequent_item_data
            )

            head_to_head_resolutions_subsequent.append(
                head_to_head_resolutions_subsequent_item
            )

        standing_configurations_update_standing_configurations_put_body_standing_configuration = cls(
            losses_secondary_score_home_points=losses_secondary_score_home_points,
            losses_secondary_score_away_points=losses_secondary_score_away_points,
            wins_secondary_score_home_points=wins_secondary_score_home_points,
            wins_secondary_score_away_points=wins_secondary_score_away_points,
            wins_home_points=wins_home_points,
            losses_home_points=losses_home_points,
            draws_home_scored_points=draws_home_scored_points,
            draws_home_zero_points=draws_home_zero_points,
            forfeit_won_by_home_points=forfeit_won_by_home_points,
            forfeits_won_by_home_points=forfeits_won_by_home_points,
            forfeit_given_home_points=forfeit_given_home_points,
            wins_away_points=wins_away_points,
            losses_away_points=losses_away_points,
            draws_away_scored_points=draws_away_scored_points,
            draws_away_zero_points=draws_away_zero_points,
            forfeit_won_by_away_points=forfeit_won_by_away_points,
            forfeit_given_away_points=forfeit_given_away_points,
            secondary_score_draw_as_result=secondary_score_draw_as_result,
            check_secondary_scores=check_secondary_scores,
            bye_points=bye_points,
            bye_is_played=bye_is_played,
            bye_added_wins=bye_added_wins,
            forfeit_won_by_added_wins=forfeit_won_by_added_wins,
            forfeit_won_by_added_played=forfeit_won_by_added_played,
            forfeit_given_added_losses=forfeit_given_added_losses,
            forfeit_given_added_played=forfeit_given_added_played,
            streak=streak,
            sorts=sorts,
            head_to_head_identification=head_to_head_identification,
            head_to_head_identification_subsequent=head_to_head_identification_subsequent,
            head_to_head_use_all_fixtures=head_to_head_use_all_fixtures,
            head_to_head_use_adjustments=head_to_head_use_adjustments,
            head_to_head_single_round=head_to_head_single_round,
            head_to_head_resolutions=head_to_head_resolutions,
            head_to_head_resolutions_subsequent=head_to_head_resolutions_subsequent,
        )

        return standing_configurations_update_standing_configurations_put_body_standing_configuration
