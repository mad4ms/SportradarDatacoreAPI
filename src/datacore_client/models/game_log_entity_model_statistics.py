from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GameLogEntityModelStatistics")


@_attrs_define
class GameLogEntityModelStatistics:
    """
    Attributes:
        assists (Union[None, Unset, int]): Total number of assists
        back_court_goals_scored (Union[None, Unset, int]): Total number of goals scored from a back court position
        back_court_missed_shots (Union[None, Unset, int]): Total number of missed shots from a back court position
        back_court_post_hits (Union[None, Unset, int]): Total number of post hits from a back court position
        back_court_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the back court position
        back_court_shots (Union[None, Unset, int]): Total number of back court shots attempted
        back_court_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from a back court position
        back_court_shots_on_goal (Union[None, Unset, int]): Total number of back court shots on goal
        blocks (Union[None, Unset, int]): Total number of blocks
        blue_cards (Union[None, Unset, int]): Total number of blue cards
        break_through_goals_scored (Union[None, Unset, int]): Total number of goals scored from a break through attack
        break_through_missed_shots (Union[None, Unset, int]): Total number of missed shots from a break through attack
        break_through_post_hits (Union[None, Unset, int]): Total number of post hits from a break through attack
        break_through_shooting_accuracy (Union[Unset, float]): Shot rate shots on goal from a break through attack
        break_through_shots (Union[None, Unset, int]): Total number of break through shots attempted
        break_through_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from a break through attack
        break_through_shots_on_goal (Union[None, Unset, int]): Total number of break through shots on goal
        cards (Union[None, Unset, int]): Total number of cards
        empty_net_goals_scored (Union[None, Unset, int]): Total number of goals scored in an empty net
        fast_break_goals_scored (Union[None, Unset, int]): Total number of goals scored from a fast break attack
        fast_break_missed_shots (Union[None, Unset, int]): Total number of missed shots from a fast break attack
        fast_break_post_hits (Union[None, Unset, int]): Total number of post hits from a fast break attack
        fast_break_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from a fast break attack
        fast_break_shots (Union[None, Unset, int]): Total number of fast break shots attempted
        fast_break_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from a fast break attack
        fast_break_shots_on_goal (Union[None, Unset, int]): Total number of fast break shots on goal
        field_goals_scored (Union[None, Unset, int]): Total number of goals scored from the field
        field_missed_shots (Union[None, Unset, int]): Total number of missed shots from the field
        field_post_hits (Union[None, Unset, int]): Total number of post hits from the field
        field_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the field
        field_shots (Union[None, Unset, int]): Total number of field shots attempted
        field_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the field
        field_shots_on_goal (Union[None, Unset, int]): Total number of field shots on goal
        fouls (Union[None, Unset, int]): Total number of fouls committed
        fouls_drawn (Union[None, Unset, int]): Total number of fouls drawn
        four_minute_suspensions (Union[None, Unset, int]): Total number of four minute suspensions
        goal_keeper_back_court_goals_against (Union[None, Unset, int]): Total number of back court goals conceded by the
            goalkeeper
        goal_keeper_back_court_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the back
            court position
        goal_keeper_back_court_shots_against (Union[None, Unset, int]): Total number of back court shots on goal against
            the goalkeeper
        goal_keeper_back_court_shots_saved (Union[None, Unset, int]): Total number of back court shots saved by the
            goalkeeper
        goal_keeper_break_through_goals_against (Union[None, Unset, int]): Total number of break through goals conceded
            by the goalkeeper
        goal_keeper_break_through_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from a
            break through attack
        goal_keeper_break_through_shots_against (Union[None, Unset, int]): Total number of break through shots on goal
            against the goalkeeper
        goal_keeper_break_through_shots_saved (Union[None, Unset, int]): Total number of break through shots saved by
            the goalkeeper
        goal_keeper_fast_break_goals_against (Union[None, Unset, int]): Total number of fast break goals conceded by the
            goalkeeper
        goal_keeper_fast_break_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from a fast
            break attack
        goal_keeper_fast_break_shots_against (Union[None, Unset, int]): Total number of fast break shots on goal against
            the goalkeeper
        goal_keeper_fast_break_shots_saved (Union[None, Unset, int]): Total number of fast break shots saved by the
            goalkeeper
        goal_keeper_field_goals_against (Union[None, Unset, int]): Total number of field goals conceded by the
            goalkeeper
        goal_keeper_field_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper when shooting from
            the field
        goal_keeper_field_shots_against (Union[None, Unset, int]): Total number of field shots on goal against the
            goalkeeper
        goal_keeper_field_shots_saved (Union[None, Unset, int]): Total number of field shots saved by the goalkeeper
        goal_keeper_goals_against (Union[None, Unset, int]): Total number of goals conceded by the goalkeeper
        goal_keeper_nine_metre_centre_goals_against (Union[None, Unset, int]): Total number of nine metre centre goals
            conceded by the goalkeeper
        goal_keeper_nine_metre_centre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from
            the nine metre centre position
        goal_keeper_nine_metre_centre_shots_against (Union[None, Unset, int]): Total number of nine metre centre shots
            on goal against the goalkeeper
        goal_keeper_nine_metre_centre_shots_saved (Union[None, Unset, int]): Total number of nine metre centre shots
            saved by the goalkeeper
        goal_keeper_nine_metre_goals_against (Union[None, Unset, int]): Total number of nine metre goals conceded by the
            goalkeeper
        goal_keeper_nine_metre_left_goals_against (Union[None, Unset, int]): Total number of nine metre left goals
            conceded by the goalkeeper
        goal_keeper_nine_metre_left_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            nine metre left position
        goal_keeper_nine_metre_left_shots_against (Union[None, Unset, int]): Total number of nine metre left shots on
            goal against the goalkeeper
        goal_keeper_nine_metre_left_shots_saved (Union[None, Unset, int]): Total number of nine metre left shots saved
            by the goalkeeper
        goal_keeper_nine_metre_right_goals_against (Union[None, Unset, int]): Total number of nine metre right goals
            conceded by the goalkeeper
        goal_keeper_nine_metre_right_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            nine metre right position
        goal_keeper_nine_metre_right_shots_against (Union[None, Unset, int]): Total number of nine metre right shots on
            goal against the goalkeeper
        goal_keeper_nine_metre_right_shots_saved (Union[None, Unset, int]): Total number of nine metre right shots saved
            by the goalkeeper
        goal_keeper_nine_metre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the nine
            metre position
        goal_keeper_nine_metre_shots_against (Union[None, Unset, int]): Total number of nine metre shots on goal against
            the goalkeeper
        goal_keeper_nine_metre_shots_saved (Union[None, Unset, int]): Total number of nine metre shots saved by the
            goalkeeper
        goal_keeper_pivot_goals_against (Union[None, Unset, int]): Total number of pivot goals conceded by the
            goalkeeper
        goal_keeper_pivot_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the pivot
            position
        goal_keeper_pivot_shots_against (Union[None, Unset, int]): Total number of pivot shots on goal against the
            goalkeeper
        goal_keeper_pivot_shots_saved (Union[None, Unset, int]): Total number of pivot shots saved by the goalkeeper
        goal_keeper_save_accuracy (Union[Unset, float]): Rate of all balls saved by the goalkeeper
        goal_keeper_seconds_played (Union[None, Unset, int]): Total number of seconds played by the goalkeeper
        goal_keeper_seven_metre_goals_against (Union[None, Unset, int]): Total number of seven metre penalty goals
            conceded by the goalkeeper
        goal_keeper_seven_metre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            seven metre position
        goal_keeper_seven_metre_shots_against (Union[None, Unset, int]): Total number of seven metre penalty shots on
            goal against the goalkeeper
        goal_keeper_seven_metre_shots_saved (Union[None, Unset, int]): Total number of seven metre penalty shots saved
            by the goalkeeper
        goal_keeper_shots_against (Union[None, Unset, int]): Total number of shots against the goalkeeper
        goal_keeper_shots_saved (Union[None, Unset, int]): Total number of shots saved by the goalkeeper
        goal_keeper_six_metre_centre_goals_against (Union[None, Unset, int]): Total number of six metre centre goals
            conceded by the goalkeeper
        goal_keeper_six_metre_centre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            six metre centre position
        goal_keeper_six_metre_centre_shots_against (Union[None, Unset, int]): Total number of six metre centre shots on
            goal against the goalkeeper
        goal_keeper_six_metre_centre_shots_saved (Union[None, Unset, int]): Total number of six metre centre shots saved
            by the goalkeeper
        goal_keeper_six_metre_goals_against (Union[None, Unset, int]): Total number of six metre goals conceded by the
            goalkeeper
        goal_keeper_six_metre_left_goals_against (Union[None, Unset, int]): Total number of six metre left goals
            conceded by the goalkeeper
        goal_keeper_six_metre_left_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            six metre left position
        goal_keeper_six_metre_left_shots_against (Union[None, Unset, int]): Total number of six metre left shots on goal
            against the goalkeeper
        goal_keeper_six_metre_left_shots_saved (Union[None, Unset, int]): Total number of six metre left shots saved by
            the goalkeeper
        goal_keeper_six_metre_right_goals_against (Union[None, Unset, int]): Total number of six metre right goals
            conceded by the goalkeeper
        goal_keeper_six_metre_right_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            six metre right position
        goal_keeper_six_metre_right_shots_against (Union[None, Unset, int]): Total number of six metre right shots on
            goal against the goalkeeper
        goal_keeper_six_metre_right_shots_saved (Union[None, Unset, int]): Total number of six metre right shots saved
            by the goalkeeper
        goal_keeper_six_metre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the six
            metre position
        goal_keeper_six_metre_shots_against (Union[None, Unset, int]): Total number of six metre shots on goal against
            the goalkeeper
        goal_keeper_six_metre_shots_saved (Union[None, Unset, int]): Total number of six metre shots saved by the
            goalkeeper
        goal_keeper_wing_goals_against (Union[None, Unset, int]): Total number of wing goals conceded by the goalkeeper
        goal_keeper_wing_left_goals_against (Union[None, Unset, int]): Total number of left wing goals conceded by the
            goalkeeper
        goal_keeper_wing_left_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the wing
            left position
        goal_keeper_wing_left_shots_against (Union[None, Unset, int]): Total number of left wing shots on goal against
            the goalkeeper
        goal_keeper_wing_left_shots_saved (Union[None, Unset, int]): Total number of left wing shots saved by the
            goalkeeper
        goal_keeper_wing_right_goals_against (Union[None, Unset, int]): Total number of right wing goals conceded by the
            goalkeeper
        goal_keeper_wing_right_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the wing
            right position
        goal_keeper_wing_right_shots_against (Union[None, Unset, int]): Total number of right wing shots on goal against
            the goalkeeper
        goal_keeper_wing_right_shots_saved (Union[None, Unset, int]): Total number of right wing shots saved by the
            goalkeeper
        goal_keeper_wing_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the wing
            position
        goal_keeper_wing_shots_against (Union[None, Unset, int]): Total number of wing shots on goal against the
            goalkeeper
        goal_keeper_wing_shots_saved (Union[None, Unset, int]): Total number of wing shots saved by the goalkeeper
        goals_scored (Union[None, Unset, int]): Total number of goals scored
        missed_shots (Union[None, Unset, int]): Total number of missed shots
        nine_metre_centre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre
            centre position
        nine_metre_centre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre
            centre position
        nine_metre_centre_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre centre
            position
        nine_metre_centre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre centre
            position
        nine_metre_centre_shots (Union[None, Unset, int]): Total number of nine metre centre shots
        nine_metre_centre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre
            centre position
        nine_metre_centre_shots_on_goal (Union[None, Unset, int]): Total number of nine metre centre shots on goal
        nine_metre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre position
        nine_metre_left_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre left
            position
        nine_metre_left_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre left
            position
        nine_metre_left_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre left position
        nine_metre_left_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre left
            position
        nine_metre_left_shots (Union[None, Unset, int]): Total number of nine metre left shots attempted
        nine_metre_left_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre left
            position
        nine_metre_left_shots_on_goal (Union[None, Unset, int]): Total number of nine metre left shots on goal
        nine_metre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre position
        nine_metre_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre position
        nine_metre_right_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre right
            position
        nine_metre_right_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre right
            position
        nine_metre_right_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre right
            position
        nine_metre_right_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre right
            position
        nine_metre_right_shots (Union[None, Unset, int]): Total number of nine metre right shots attempted
        nine_metre_right_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre
            right position
        nine_metre_right_shots_on_goal (Union[None, Unset, int]): Total number of nine metre right shots on goal
        nine_metre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre position
        nine_metre_shots (Union[None, Unset, int]): Total number of nine metre shots attempted
        nine_metre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre position
        nine_metre_shots_on_goal (Union[None, Unset, int]): Total number of nine metre shots on goal
        passive_play (Union[None, Unset, int]): Total number of passive play
        pivot_goals_scored (Union[None, Unset, int]): Total number of goals scored from the pivot position
        pivot_missed_shots (Union[None, Unset, int]): Total number of missed shots from the pivot position
        pivot_post_hits (Union[None, Unset, int]): Total number of post hits from the pivot position
        pivot_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the pivot position
        pivot_shots (Union[None, Unset, int]): Total number of pivot shots attempted
        pivot_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the pivot position
        pivot_shots_on_goal (Union[None, Unset, int]): Total number of pivot shots on goal
        post_hits (Union[None, Unset, int]): Total number of post hits
        red_cards (Union[None, Unset, int]): Total number of red cards
        seven_metre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the seven metre penalties
        seven_metre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the seven metre penalties
        seven_metre_penalties_awarded (Union[None, Unset, int]): Total number of seven metre penalties awarded
        seven_metre_penalties_caused (Union[None, Unset, int]): Total number of seven metre penalties caused
        seven_metre_penalty_fouls (Union[None, Unset, int]): Total number of seven metre penalty fouls
        seven_metre_post_hits (Union[None, Unset, int]): Total number of post hits from the seven metre penalties
        seven_metre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from seven metre penalties
        seven_metre_shots (Union[None, Unset, int]): Total number of seven metre penalty shots attempted
        seven_metre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the seven metre
            penalties
        seven_metre_shots_on_goal (Union[None, Unset, int]): Total number of seven metre penalty shots on goal
        shooting_accuracy (Union[Unset, float]): Shot rate for all shots on goal
        shoot_out_attempts (Union[None, Unset, str]): Results of shoot-out attempts (1 or 0 per attempt).
        shoot_outs (Union[None, Unset, int]): Total number of shoot outs
        shoot_outs_made (Union[None, Unset, int]): Total number of goals scored from shoot out shots
        shoot_outs_missed (Union[None, Unset, int]): Total number of shoot out shots missed
        shoot_outs_saved (Union[None, Unset, int]): Total number of shoot out shots saved
        shots (Union[None, Unset, int]): Total number of shots. This is made up of all shots, including shot that are
            blocked, saved, lead to a goal, missed, hit the bar or post.
        shots_blocked (Union[None, Unset, int]): Total number of shots blocked
        shots_on_goal (Union[None, Unset, int]): Total number of shots on target. This is made up of shots that lead to
            goals or a save from the Goalie.
        shots_off_goal (Union[None, Unset, int]): Total number of shots off goal
        shots_saved_by_goal_keeper (Union[None, Unset, int]): The number of shots taken by a player that were saved by
            the opposition goalkeeper
        six_metre_centre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre centre
            position
        six_metre_centre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre centre
            position
        six_metre_centre_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre centre
            position
        six_metre_centre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre centre
            position
        six_metre_centre_shots (Union[None, Unset, int]): Total number of six metre centre shots
        six_metre_centre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre
            centre position
        six_metre_centre_shots_on_goal (Union[None, Unset, int]): Total number of six metre centre shots on goal
        six_metre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre position
        six_metre_left_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre left
            position
        six_metre_left_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre left
            position
        six_metre_left_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre left position
        six_metre_left_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre left
            position
        six_metre_left_shots (Union[None, Unset, int]): Total number of six metre left shots attempted
        six_metre_left_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre left
            position
        six_metre_left_shots_on_goal (Union[None, Unset, int]): Total number of six metre left shots on goal
        six_metre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre position
        six_metre_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre position
        six_metre_right_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre right
            position
        six_metre_right_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre right
            position
        six_metre_right_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre right position
        six_metre_right_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre right
            position
        six_metre_right_shots (Union[None, Unset, int]): Total number of six metre right shots attempted
        six_metre_right_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre right
            position
        six_metre_right_shots_on_goal (Union[None, Unset, int]): Total number of six metre right shots on goal
        six_metre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre position
        six_metre_shots (Union[None, Unset, int]): Total number of six metre shots attempted
        six_metre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre position
        six_metre_shots_on_goal (Union[None, Unset, int]): Total number of six metre shots on goal
        steals (Union[None, Unset, int]): Total number of stolen balls by the player
        substitutions (Union[None, Unset, int]): Total number of substitutions
        suspensions (Union[None, Unset, int]): Total number of suspensions
        technical_ball_faults (Union[None, Unset, int]): Total number of technical ball errors
        technical_faults (Union[None, Unset, int]): Total number of technical errors
        technical_rule_faults (Union[None, Unset, int]): Total number of technical rule errors
        time_played (Union[None, Unset, int]): Total number of minutes the played
        turnovers (Union[None, Unset, int]): Total number of turnovers
        two_minute_suspensions (Union[None, Unset, int]): Total number of two minute suspensions
        wing_goals_scored (Union[None, Unset, int]): Total number of goals scored from the wing position
        wing_left_goals_scored (Union[None, Unset, int]): Total number of goals scored from the left wing position
        wing_left_missed_shots (Union[None, Unset, int]): Total number of missed shots from the left wing position
        wing_left_post_hits (Union[None, Unset, int]): Total number of post hits from the left wing position
        wing_left_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the left wing position
        wing_left_shots (Union[None, Unset, int]): Total number of wing left shots attempted
        wing_left_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the left wing position
        wing_left_shots_on_goal (Union[None, Unset, int]): Total number of left wing shots on goal
        wing_missed_shots (Union[None, Unset, int]): Total number of missed shots from the wing position
        wing_post_hits (Union[None, Unset, int]): Total number of post hits from the wing position
        wing_right_goals_scored (Union[None, Unset, int]): Total number of goals scored from the right wing position
        wing_right_missed_shots (Union[None, Unset, int]): Total number of missed shots from the right wing position
        wing_right_post_hits (Union[None, Unset, int]): Total number of post hits from the right wing position
        wing_right_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the right wing position
        wing_right_shots (Union[None, Unset, int]): Total number of wing right shots attempted
        wing_right_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the right wing position
        wing_right_shots_on_goal (Union[None, Unset, int]): Total number of right wing shots on goal
        wing_shooting_accuracy (Union[Unset, float]): Shot rate of all shots on goal from the wing position
        wing_shots (Union[None, Unset, int]): Total number of wing shots attempted
        wing_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the wing position
        wing_shots_on_goal (Union[None, Unset, int]): Total number of wing shots on goal
        yellow_cards (Union[None, Unset, int]): Total number of yellow cards
    """

    assists: Union[None, Unset, int] = UNSET
    back_court_goals_scored: Union[None, Unset, int] = UNSET
    back_court_missed_shots: Union[None, Unset, int] = UNSET
    back_court_post_hits: Union[None, Unset, int] = UNSET
    back_court_shooting_accuracy: Union[Unset, float] = UNSET
    back_court_shots: Union[None, Unset, int] = UNSET
    back_court_shots_blocked: Union[None, Unset, int] = UNSET
    back_court_shots_on_goal: Union[None, Unset, int] = UNSET
    blocks: Union[None, Unset, int] = UNSET
    blue_cards: Union[None, Unset, int] = UNSET
    break_through_goals_scored: Union[None, Unset, int] = UNSET
    break_through_missed_shots: Union[None, Unset, int] = UNSET
    break_through_post_hits: Union[None, Unset, int] = UNSET
    break_through_shooting_accuracy: Union[Unset, float] = UNSET
    break_through_shots: Union[None, Unset, int] = UNSET
    break_through_shots_blocked: Union[None, Unset, int] = UNSET
    break_through_shots_on_goal: Union[None, Unset, int] = UNSET
    cards: Union[None, Unset, int] = UNSET
    empty_net_goals_scored: Union[None, Unset, int] = UNSET
    fast_break_goals_scored: Union[None, Unset, int] = UNSET
    fast_break_missed_shots: Union[None, Unset, int] = UNSET
    fast_break_post_hits: Union[None, Unset, int] = UNSET
    fast_break_shooting_accuracy: Union[Unset, float] = UNSET
    fast_break_shots: Union[None, Unset, int] = UNSET
    fast_break_shots_blocked: Union[None, Unset, int] = UNSET
    fast_break_shots_on_goal: Union[None, Unset, int] = UNSET
    field_goals_scored: Union[None, Unset, int] = UNSET
    field_missed_shots: Union[None, Unset, int] = UNSET
    field_post_hits: Union[None, Unset, int] = UNSET
    field_shooting_accuracy: Union[Unset, float] = UNSET
    field_shots: Union[None, Unset, int] = UNSET
    field_shots_blocked: Union[None, Unset, int] = UNSET
    field_shots_on_goal: Union[None, Unset, int] = UNSET
    fouls: Union[None, Unset, int] = UNSET
    fouls_drawn: Union[None, Unset, int] = UNSET
    four_minute_suspensions: Union[None, Unset, int] = UNSET
    goal_keeper_back_court_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_back_court_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_back_court_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_back_court_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_break_through_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_break_through_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_break_through_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_break_through_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_fast_break_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_fast_break_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_fast_break_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_fast_break_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_field_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_field_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_field_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_field_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_centre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_centre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_centre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_centre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_left_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_left_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_left_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_left_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_right_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_right_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_right_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_right_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_pivot_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_pivot_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_pivot_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_pivot_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_seconds_played: Union[None, Unset, int] = UNSET
    goal_keeper_seven_metre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_seven_metre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_seven_metre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_seven_metre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_centre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_centre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_centre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_centre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_left_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_left_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_left_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_left_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_right_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_right_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_right_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_right_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_wing_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_left_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_left_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_wing_left_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_left_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_wing_right_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_right_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_wing_right_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_right_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_wing_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_wing_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_shots_saved: Union[None, Unset, int] = UNSET
    goals_scored: Union[None, Unset, int] = UNSET
    missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_centre_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_centre_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_centre_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_centre_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_centre_shots: Union[None, Unset, int] = UNSET
    nine_metre_centre_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_centre_shots_on_goal: Union[None, Unset, int] = UNSET
    nine_metre_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_left_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_left_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_left_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_left_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_left_shots: Union[None, Unset, int] = UNSET
    nine_metre_left_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_left_shots_on_goal: Union[None, Unset, int] = UNSET
    nine_metre_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_right_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_right_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_right_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_right_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_right_shots: Union[None, Unset, int] = UNSET
    nine_metre_right_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_right_shots_on_goal: Union[None, Unset, int] = UNSET
    nine_metre_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_shots: Union[None, Unset, int] = UNSET
    nine_metre_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_shots_on_goal: Union[None, Unset, int] = UNSET
    passive_play: Union[None, Unset, int] = UNSET
    pivot_goals_scored: Union[None, Unset, int] = UNSET
    pivot_missed_shots: Union[None, Unset, int] = UNSET
    pivot_post_hits: Union[None, Unset, int] = UNSET
    pivot_shooting_accuracy: Union[Unset, float] = UNSET
    pivot_shots: Union[None, Unset, int] = UNSET
    pivot_shots_blocked: Union[None, Unset, int] = UNSET
    pivot_shots_on_goal: Union[None, Unset, int] = UNSET
    post_hits: Union[None, Unset, int] = UNSET
    red_cards: Union[None, Unset, int] = UNSET
    seven_metre_goals_scored: Union[None, Unset, int] = UNSET
    seven_metre_missed_shots: Union[None, Unset, int] = UNSET
    seven_metre_penalties_awarded: Union[None, Unset, int] = UNSET
    seven_metre_penalties_caused: Union[None, Unset, int] = UNSET
    seven_metre_penalty_fouls: Union[None, Unset, int] = UNSET
    seven_metre_post_hits: Union[None, Unset, int] = UNSET
    seven_metre_shooting_accuracy: Union[Unset, float] = UNSET
    seven_metre_shots: Union[None, Unset, int] = UNSET
    seven_metre_shots_blocked: Union[None, Unset, int] = UNSET
    seven_metre_shots_on_goal: Union[None, Unset, int] = UNSET
    shooting_accuracy: Union[Unset, float] = UNSET
    shoot_out_attempts: Union[None, Unset, str] = UNSET
    shoot_outs: Union[None, Unset, int] = UNSET
    shoot_outs_made: Union[None, Unset, int] = UNSET
    shoot_outs_missed: Union[None, Unset, int] = UNSET
    shoot_outs_saved: Union[None, Unset, int] = UNSET
    shots: Union[None, Unset, int] = UNSET
    shots_blocked: Union[None, Unset, int] = UNSET
    shots_on_goal: Union[None, Unset, int] = UNSET
    shots_off_goal: Union[None, Unset, int] = UNSET
    shots_saved_by_goal_keeper: Union[None, Unset, int] = UNSET
    six_metre_centre_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_centre_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_centre_post_hits: Union[None, Unset, int] = UNSET
    six_metre_centre_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_centre_shots: Union[None, Unset, int] = UNSET
    six_metre_centre_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_centre_shots_on_goal: Union[None, Unset, int] = UNSET
    six_metre_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_left_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_left_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_left_post_hits: Union[None, Unset, int] = UNSET
    six_metre_left_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_left_shots: Union[None, Unset, int] = UNSET
    six_metre_left_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_left_shots_on_goal: Union[None, Unset, int] = UNSET
    six_metre_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_post_hits: Union[None, Unset, int] = UNSET
    six_metre_right_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_right_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_right_post_hits: Union[None, Unset, int] = UNSET
    six_metre_right_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_right_shots: Union[None, Unset, int] = UNSET
    six_metre_right_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_right_shots_on_goal: Union[None, Unset, int] = UNSET
    six_metre_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_shots: Union[None, Unset, int] = UNSET
    six_metre_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_shots_on_goal: Union[None, Unset, int] = UNSET
    steals: Union[None, Unset, int] = UNSET
    substitutions: Union[None, Unset, int] = UNSET
    suspensions: Union[None, Unset, int] = UNSET
    technical_ball_faults: Union[None, Unset, int] = UNSET
    technical_faults: Union[None, Unset, int] = UNSET
    technical_rule_faults: Union[None, Unset, int] = UNSET
    time_played: Union[None, Unset, int] = UNSET
    turnovers: Union[None, Unset, int] = UNSET
    two_minute_suspensions: Union[None, Unset, int] = UNSET
    wing_goals_scored: Union[None, Unset, int] = UNSET
    wing_left_goals_scored: Union[None, Unset, int] = UNSET
    wing_left_missed_shots: Union[None, Unset, int] = UNSET
    wing_left_post_hits: Union[None, Unset, int] = UNSET
    wing_left_shooting_accuracy: Union[Unset, float] = UNSET
    wing_left_shots: Union[None, Unset, int] = UNSET
    wing_left_shots_blocked: Union[None, Unset, int] = UNSET
    wing_left_shots_on_goal: Union[None, Unset, int] = UNSET
    wing_missed_shots: Union[None, Unset, int] = UNSET
    wing_post_hits: Union[None, Unset, int] = UNSET
    wing_right_goals_scored: Union[None, Unset, int] = UNSET
    wing_right_missed_shots: Union[None, Unset, int] = UNSET
    wing_right_post_hits: Union[None, Unset, int] = UNSET
    wing_right_shooting_accuracy: Union[Unset, float] = UNSET
    wing_right_shots: Union[None, Unset, int] = UNSET
    wing_right_shots_blocked: Union[None, Unset, int] = UNSET
    wing_right_shots_on_goal: Union[None, Unset, int] = UNSET
    wing_shooting_accuracy: Union[Unset, float] = UNSET
    wing_shots: Union[None, Unset, int] = UNSET
    wing_shots_blocked: Union[None, Unset, int] = UNSET
    wing_shots_on_goal: Union[None, Unset, int] = UNSET
    yellow_cards: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        assists: Union[None, Unset, int]
        if isinstance(self.assists, Unset):
            assists = UNSET
        else:
            assists = self.assists

        back_court_goals_scored: Union[None, Unset, int]
        if isinstance(self.back_court_goals_scored, Unset):
            back_court_goals_scored = UNSET
        else:
            back_court_goals_scored = self.back_court_goals_scored

        back_court_missed_shots: Union[None, Unset, int]
        if isinstance(self.back_court_missed_shots, Unset):
            back_court_missed_shots = UNSET
        else:
            back_court_missed_shots = self.back_court_missed_shots

        back_court_post_hits: Union[None, Unset, int]
        if isinstance(self.back_court_post_hits, Unset):
            back_court_post_hits = UNSET
        else:
            back_court_post_hits = self.back_court_post_hits

        back_court_shooting_accuracy = self.back_court_shooting_accuracy

        back_court_shots: Union[None, Unset, int]
        if isinstance(self.back_court_shots, Unset):
            back_court_shots = UNSET
        else:
            back_court_shots = self.back_court_shots

        back_court_shots_blocked: Union[None, Unset, int]
        if isinstance(self.back_court_shots_blocked, Unset):
            back_court_shots_blocked = UNSET
        else:
            back_court_shots_blocked = self.back_court_shots_blocked

        back_court_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.back_court_shots_on_goal, Unset):
            back_court_shots_on_goal = UNSET
        else:
            back_court_shots_on_goal = self.back_court_shots_on_goal

        blocks: Union[None, Unset, int]
        if isinstance(self.blocks, Unset):
            blocks = UNSET
        else:
            blocks = self.blocks

        blue_cards: Union[None, Unset, int]
        if isinstance(self.blue_cards, Unset):
            blue_cards = UNSET
        else:
            blue_cards = self.blue_cards

        break_through_goals_scored: Union[None, Unset, int]
        if isinstance(self.break_through_goals_scored, Unset):
            break_through_goals_scored = UNSET
        else:
            break_through_goals_scored = self.break_through_goals_scored

        break_through_missed_shots: Union[None, Unset, int]
        if isinstance(self.break_through_missed_shots, Unset):
            break_through_missed_shots = UNSET
        else:
            break_through_missed_shots = self.break_through_missed_shots

        break_through_post_hits: Union[None, Unset, int]
        if isinstance(self.break_through_post_hits, Unset):
            break_through_post_hits = UNSET
        else:
            break_through_post_hits = self.break_through_post_hits

        break_through_shooting_accuracy = self.break_through_shooting_accuracy

        break_through_shots: Union[None, Unset, int]
        if isinstance(self.break_through_shots, Unset):
            break_through_shots = UNSET
        else:
            break_through_shots = self.break_through_shots

        break_through_shots_blocked: Union[None, Unset, int]
        if isinstance(self.break_through_shots_blocked, Unset):
            break_through_shots_blocked = UNSET
        else:
            break_through_shots_blocked = self.break_through_shots_blocked

        break_through_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.break_through_shots_on_goal, Unset):
            break_through_shots_on_goal = UNSET
        else:
            break_through_shots_on_goal = self.break_through_shots_on_goal

        cards: Union[None, Unset, int]
        if isinstance(self.cards, Unset):
            cards = UNSET
        else:
            cards = self.cards

        empty_net_goals_scored: Union[None, Unset, int]
        if isinstance(self.empty_net_goals_scored, Unset):
            empty_net_goals_scored = UNSET
        else:
            empty_net_goals_scored = self.empty_net_goals_scored

        fast_break_goals_scored: Union[None, Unset, int]
        if isinstance(self.fast_break_goals_scored, Unset):
            fast_break_goals_scored = UNSET
        else:
            fast_break_goals_scored = self.fast_break_goals_scored

        fast_break_missed_shots: Union[None, Unset, int]
        if isinstance(self.fast_break_missed_shots, Unset):
            fast_break_missed_shots = UNSET
        else:
            fast_break_missed_shots = self.fast_break_missed_shots

        fast_break_post_hits: Union[None, Unset, int]
        if isinstance(self.fast_break_post_hits, Unset):
            fast_break_post_hits = UNSET
        else:
            fast_break_post_hits = self.fast_break_post_hits

        fast_break_shooting_accuracy = self.fast_break_shooting_accuracy

        fast_break_shots: Union[None, Unset, int]
        if isinstance(self.fast_break_shots, Unset):
            fast_break_shots = UNSET
        else:
            fast_break_shots = self.fast_break_shots

        fast_break_shots_blocked: Union[None, Unset, int]
        if isinstance(self.fast_break_shots_blocked, Unset):
            fast_break_shots_blocked = UNSET
        else:
            fast_break_shots_blocked = self.fast_break_shots_blocked

        fast_break_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.fast_break_shots_on_goal, Unset):
            fast_break_shots_on_goal = UNSET
        else:
            fast_break_shots_on_goal = self.fast_break_shots_on_goal

        field_goals_scored: Union[None, Unset, int]
        if isinstance(self.field_goals_scored, Unset):
            field_goals_scored = UNSET
        else:
            field_goals_scored = self.field_goals_scored

        field_missed_shots: Union[None, Unset, int]
        if isinstance(self.field_missed_shots, Unset):
            field_missed_shots = UNSET
        else:
            field_missed_shots = self.field_missed_shots

        field_post_hits: Union[None, Unset, int]
        if isinstance(self.field_post_hits, Unset):
            field_post_hits = UNSET
        else:
            field_post_hits = self.field_post_hits

        field_shooting_accuracy = self.field_shooting_accuracy

        field_shots: Union[None, Unset, int]
        if isinstance(self.field_shots, Unset):
            field_shots = UNSET
        else:
            field_shots = self.field_shots

        field_shots_blocked: Union[None, Unset, int]
        if isinstance(self.field_shots_blocked, Unset):
            field_shots_blocked = UNSET
        else:
            field_shots_blocked = self.field_shots_blocked

        field_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.field_shots_on_goal, Unset):
            field_shots_on_goal = UNSET
        else:
            field_shots_on_goal = self.field_shots_on_goal

        fouls: Union[None, Unset, int]
        if isinstance(self.fouls, Unset):
            fouls = UNSET
        else:
            fouls = self.fouls

        fouls_drawn: Union[None, Unset, int]
        if isinstance(self.fouls_drawn, Unset):
            fouls_drawn = UNSET
        else:
            fouls_drawn = self.fouls_drawn

        four_minute_suspensions: Union[None, Unset, int]
        if isinstance(self.four_minute_suspensions, Unset):
            four_minute_suspensions = UNSET
        else:
            four_minute_suspensions = self.four_minute_suspensions

        goal_keeper_back_court_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_back_court_goals_against, Unset):
            goal_keeper_back_court_goals_against = UNSET
        else:
            goal_keeper_back_court_goals_against = self.goal_keeper_back_court_goals_against

        goal_keeper_back_court_save_accuracy = self.goal_keeper_back_court_save_accuracy

        goal_keeper_back_court_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_back_court_shots_against, Unset):
            goal_keeper_back_court_shots_against = UNSET
        else:
            goal_keeper_back_court_shots_against = self.goal_keeper_back_court_shots_against

        goal_keeper_back_court_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_back_court_shots_saved, Unset):
            goal_keeper_back_court_shots_saved = UNSET
        else:
            goal_keeper_back_court_shots_saved = self.goal_keeper_back_court_shots_saved

        goal_keeper_break_through_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_break_through_goals_against, Unset):
            goal_keeper_break_through_goals_against = UNSET
        else:
            goal_keeper_break_through_goals_against = self.goal_keeper_break_through_goals_against

        goal_keeper_break_through_save_accuracy = self.goal_keeper_break_through_save_accuracy

        goal_keeper_break_through_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_break_through_shots_against, Unset):
            goal_keeper_break_through_shots_against = UNSET
        else:
            goal_keeper_break_through_shots_against = self.goal_keeper_break_through_shots_against

        goal_keeper_break_through_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_break_through_shots_saved, Unset):
            goal_keeper_break_through_shots_saved = UNSET
        else:
            goal_keeper_break_through_shots_saved = self.goal_keeper_break_through_shots_saved

        goal_keeper_fast_break_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_fast_break_goals_against, Unset):
            goal_keeper_fast_break_goals_against = UNSET
        else:
            goal_keeper_fast_break_goals_against = self.goal_keeper_fast_break_goals_against

        goal_keeper_fast_break_save_accuracy = self.goal_keeper_fast_break_save_accuracy

        goal_keeper_fast_break_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_fast_break_shots_against, Unset):
            goal_keeper_fast_break_shots_against = UNSET
        else:
            goal_keeper_fast_break_shots_against = self.goal_keeper_fast_break_shots_against

        goal_keeper_fast_break_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_fast_break_shots_saved, Unset):
            goal_keeper_fast_break_shots_saved = UNSET
        else:
            goal_keeper_fast_break_shots_saved = self.goal_keeper_fast_break_shots_saved

        goal_keeper_field_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_field_goals_against, Unset):
            goal_keeper_field_goals_against = UNSET
        else:
            goal_keeper_field_goals_against = self.goal_keeper_field_goals_against

        goal_keeper_field_save_accuracy = self.goal_keeper_field_save_accuracy

        goal_keeper_field_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_field_shots_against, Unset):
            goal_keeper_field_shots_against = UNSET
        else:
            goal_keeper_field_shots_against = self.goal_keeper_field_shots_against

        goal_keeper_field_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_field_shots_saved, Unset):
            goal_keeper_field_shots_saved = UNSET
        else:
            goal_keeper_field_shots_saved = self.goal_keeper_field_shots_saved

        goal_keeper_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_goals_against, Unset):
            goal_keeper_goals_against = UNSET
        else:
            goal_keeper_goals_against = self.goal_keeper_goals_against

        goal_keeper_nine_metre_centre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_centre_goals_against, Unset):
            goal_keeper_nine_metre_centre_goals_against = UNSET
        else:
            goal_keeper_nine_metre_centre_goals_against = self.goal_keeper_nine_metre_centre_goals_against

        goal_keeper_nine_metre_centre_save_accuracy = self.goal_keeper_nine_metre_centre_save_accuracy

        goal_keeper_nine_metre_centre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_centre_shots_against, Unset):
            goal_keeper_nine_metre_centre_shots_against = UNSET
        else:
            goal_keeper_nine_metre_centre_shots_against = self.goal_keeper_nine_metre_centre_shots_against

        goal_keeper_nine_metre_centre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_centre_shots_saved, Unset):
            goal_keeper_nine_metre_centre_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_centre_shots_saved = self.goal_keeper_nine_metre_centre_shots_saved

        goal_keeper_nine_metre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_goals_against, Unset):
            goal_keeper_nine_metre_goals_against = UNSET
        else:
            goal_keeper_nine_metre_goals_against = self.goal_keeper_nine_metre_goals_against

        goal_keeper_nine_metre_left_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_left_goals_against, Unset):
            goal_keeper_nine_metre_left_goals_against = UNSET
        else:
            goal_keeper_nine_metre_left_goals_against = self.goal_keeper_nine_metre_left_goals_against

        goal_keeper_nine_metre_left_save_accuracy = self.goal_keeper_nine_metre_left_save_accuracy

        goal_keeper_nine_metre_left_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_left_shots_against, Unset):
            goal_keeper_nine_metre_left_shots_against = UNSET
        else:
            goal_keeper_nine_metre_left_shots_against = self.goal_keeper_nine_metre_left_shots_against

        goal_keeper_nine_metre_left_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_left_shots_saved, Unset):
            goal_keeper_nine_metre_left_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_left_shots_saved = self.goal_keeper_nine_metre_left_shots_saved

        goal_keeper_nine_metre_right_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_right_goals_against, Unset):
            goal_keeper_nine_metre_right_goals_against = UNSET
        else:
            goal_keeper_nine_metre_right_goals_against = self.goal_keeper_nine_metre_right_goals_against

        goal_keeper_nine_metre_right_save_accuracy = self.goal_keeper_nine_metre_right_save_accuracy

        goal_keeper_nine_metre_right_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_right_shots_against, Unset):
            goal_keeper_nine_metre_right_shots_against = UNSET
        else:
            goal_keeper_nine_metre_right_shots_against = self.goal_keeper_nine_metre_right_shots_against

        goal_keeper_nine_metre_right_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_right_shots_saved, Unset):
            goal_keeper_nine_metre_right_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_right_shots_saved = self.goal_keeper_nine_metre_right_shots_saved

        goal_keeper_nine_metre_save_accuracy = self.goal_keeper_nine_metre_save_accuracy

        goal_keeper_nine_metre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_shots_against, Unset):
            goal_keeper_nine_metre_shots_against = UNSET
        else:
            goal_keeper_nine_metre_shots_against = self.goal_keeper_nine_metre_shots_against

        goal_keeper_nine_metre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_shots_saved, Unset):
            goal_keeper_nine_metre_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_shots_saved = self.goal_keeper_nine_metre_shots_saved

        goal_keeper_pivot_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_pivot_goals_against, Unset):
            goal_keeper_pivot_goals_against = UNSET
        else:
            goal_keeper_pivot_goals_against = self.goal_keeper_pivot_goals_against

        goal_keeper_pivot_save_accuracy = self.goal_keeper_pivot_save_accuracy

        goal_keeper_pivot_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_pivot_shots_against, Unset):
            goal_keeper_pivot_shots_against = UNSET
        else:
            goal_keeper_pivot_shots_against = self.goal_keeper_pivot_shots_against

        goal_keeper_pivot_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_pivot_shots_saved, Unset):
            goal_keeper_pivot_shots_saved = UNSET
        else:
            goal_keeper_pivot_shots_saved = self.goal_keeper_pivot_shots_saved

        goal_keeper_save_accuracy = self.goal_keeper_save_accuracy

        goal_keeper_seconds_played: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seconds_played, Unset):
            goal_keeper_seconds_played = UNSET
        else:
            goal_keeper_seconds_played = self.goal_keeper_seconds_played

        goal_keeper_seven_metre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seven_metre_goals_against, Unset):
            goal_keeper_seven_metre_goals_against = UNSET
        else:
            goal_keeper_seven_metre_goals_against = self.goal_keeper_seven_metre_goals_against

        goal_keeper_seven_metre_save_accuracy = self.goal_keeper_seven_metre_save_accuracy

        goal_keeper_seven_metre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seven_metre_shots_against, Unset):
            goal_keeper_seven_metre_shots_against = UNSET
        else:
            goal_keeper_seven_metre_shots_against = self.goal_keeper_seven_metre_shots_against

        goal_keeper_seven_metre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seven_metre_shots_saved, Unset):
            goal_keeper_seven_metre_shots_saved = UNSET
        else:
            goal_keeper_seven_metre_shots_saved = self.goal_keeper_seven_metre_shots_saved

        goal_keeper_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_shots_against, Unset):
            goal_keeper_shots_against = UNSET
        else:
            goal_keeper_shots_against = self.goal_keeper_shots_against

        goal_keeper_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_shots_saved, Unset):
            goal_keeper_shots_saved = UNSET
        else:
            goal_keeper_shots_saved = self.goal_keeper_shots_saved

        goal_keeper_six_metre_centre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_centre_goals_against, Unset):
            goal_keeper_six_metre_centre_goals_against = UNSET
        else:
            goal_keeper_six_metre_centre_goals_against = self.goal_keeper_six_metre_centre_goals_against

        goal_keeper_six_metre_centre_save_accuracy = self.goal_keeper_six_metre_centre_save_accuracy

        goal_keeper_six_metre_centre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_centre_shots_against, Unset):
            goal_keeper_six_metre_centre_shots_against = UNSET
        else:
            goal_keeper_six_metre_centre_shots_against = self.goal_keeper_six_metre_centre_shots_against

        goal_keeper_six_metre_centre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_centre_shots_saved, Unset):
            goal_keeper_six_metre_centre_shots_saved = UNSET
        else:
            goal_keeper_six_metre_centre_shots_saved = self.goal_keeper_six_metre_centre_shots_saved

        goal_keeper_six_metre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_goals_against, Unset):
            goal_keeper_six_metre_goals_against = UNSET
        else:
            goal_keeper_six_metre_goals_against = self.goal_keeper_six_metre_goals_against

        goal_keeper_six_metre_left_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_left_goals_against, Unset):
            goal_keeper_six_metre_left_goals_against = UNSET
        else:
            goal_keeper_six_metre_left_goals_against = self.goal_keeper_six_metre_left_goals_against

        goal_keeper_six_metre_left_save_accuracy = self.goal_keeper_six_metre_left_save_accuracy

        goal_keeper_six_metre_left_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_left_shots_against, Unset):
            goal_keeper_six_metre_left_shots_against = UNSET
        else:
            goal_keeper_six_metre_left_shots_against = self.goal_keeper_six_metre_left_shots_against

        goal_keeper_six_metre_left_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_left_shots_saved, Unset):
            goal_keeper_six_metre_left_shots_saved = UNSET
        else:
            goal_keeper_six_metre_left_shots_saved = self.goal_keeper_six_metre_left_shots_saved

        goal_keeper_six_metre_right_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_right_goals_against, Unset):
            goal_keeper_six_metre_right_goals_against = UNSET
        else:
            goal_keeper_six_metre_right_goals_against = self.goal_keeper_six_metre_right_goals_against

        goal_keeper_six_metre_right_save_accuracy = self.goal_keeper_six_metre_right_save_accuracy

        goal_keeper_six_metre_right_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_right_shots_against, Unset):
            goal_keeper_six_metre_right_shots_against = UNSET
        else:
            goal_keeper_six_metre_right_shots_against = self.goal_keeper_six_metre_right_shots_against

        goal_keeper_six_metre_right_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_right_shots_saved, Unset):
            goal_keeper_six_metre_right_shots_saved = UNSET
        else:
            goal_keeper_six_metre_right_shots_saved = self.goal_keeper_six_metre_right_shots_saved

        goal_keeper_six_metre_save_accuracy = self.goal_keeper_six_metre_save_accuracy

        goal_keeper_six_metre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_shots_against, Unset):
            goal_keeper_six_metre_shots_against = UNSET
        else:
            goal_keeper_six_metre_shots_against = self.goal_keeper_six_metre_shots_against

        goal_keeper_six_metre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_shots_saved, Unset):
            goal_keeper_six_metre_shots_saved = UNSET
        else:
            goal_keeper_six_metre_shots_saved = self.goal_keeper_six_metre_shots_saved

        goal_keeper_wing_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_goals_against, Unset):
            goal_keeper_wing_goals_against = UNSET
        else:
            goal_keeper_wing_goals_against = self.goal_keeper_wing_goals_against

        goal_keeper_wing_left_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_left_goals_against, Unset):
            goal_keeper_wing_left_goals_against = UNSET
        else:
            goal_keeper_wing_left_goals_against = self.goal_keeper_wing_left_goals_against

        goal_keeper_wing_left_save_accuracy = self.goal_keeper_wing_left_save_accuracy

        goal_keeper_wing_left_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_left_shots_against, Unset):
            goal_keeper_wing_left_shots_against = UNSET
        else:
            goal_keeper_wing_left_shots_against = self.goal_keeper_wing_left_shots_against

        goal_keeper_wing_left_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_left_shots_saved, Unset):
            goal_keeper_wing_left_shots_saved = UNSET
        else:
            goal_keeper_wing_left_shots_saved = self.goal_keeper_wing_left_shots_saved

        goal_keeper_wing_right_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_right_goals_against, Unset):
            goal_keeper_wing_right_goals_against = UNSET
        else:
            goal_keeper_wing_right_goals_against = self.goal_keeper_wing_right_goals_against

        goal_keeper_wing_right_save_accuracy = self.goal_keeper_wing_right_save_accuracy

        goal_keeper_wing_right_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_right_shots_against, Unset):
            goal_keeper_wing_right_shots_against = UNSET
        else:
            goal_keeper_wing_right_shots_against = self.goal_keeper_wing_right_shots_against

        goal_keeper_wing_right_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_right_shots_saved, Unset):
            goal_keeper_wing_right_shots_saved = UNSET
        else:
            goal_keeper_wing_right_shots_saved = self.goal_keeper_wing_right_shots_saved

        goal_keeper_wing_save_accuracy = self.goal_keeper_wing_save_accuracy

        goal_keeper_wing_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_shots_against, Unset):
            goal_keeper_wing_shots_against = UNSET
        else:
            goal_keeper_wing_shots_against = self.goal_keeper_wing_shots_against

        goal_keeper_wing_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_shots_saved, Unset):
            goal_keeper_wing_shots_saved = UNSET
        else:
            goal_keeper_wing_shots_saved = self.goal_keeper_wing_shots_saved

        goals_scored: Union[None, Unset, int]
        if isinstance(self.goals_scored, Unset):
            goals_scored = UNSET
        else:
            goals_scored = self.goals_scored

        missed_shots: Union[None, Unset, int]
        if isinstance(self.missed_shots, Unset):
            missed_shots = UNSET
        else:
            missed_shots = self.missed_shots

        nine_metre_centre_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_goals_scored, Unset):
            nine_metre_centre_goals_scored = UNSET
        else:
            nine_metre_centre_goals_scored = self.nine_metre_centre_goals_scored

        nine_metre_centre_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_missed_shots, Unset):
            nine_metre_centre_missed_shots = UNSET
        else:
            nine_metre_centre_missed_shots = self.nine_metre_centre_missed_shots

        nine_metre_centre_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_post_hits, Unset):
            nine_metre_centre_post_hits = UNSET
        else:
            nine_metre_centre_post_hits = self.nine_metre_centre_post_hits

        nine_metre_centre_shooting_accuracy = self.nine_metre_centre_shooting_accuracy

        nine_metre_centre_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_shots, Unset):
            nine_metre_centre_shots = UNSET
        else:
            nine_metre_centre_shots = self.nine_metre_centre_shots

        nine_metre_centre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_shots_blocked, Unset):
            nine_metre_centre_shots_blocked = UNSET
        else:
            nine_metre_centre_shots_blocked = self.nine_metre_centre_shots_blocked

        nine_metre_centre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_shots_on_goal, Unset):
            nine_metre_centre_shots_on_goal = UNSET
        else:
            nine_metre_centre_shots_on_goal = self.nine_metre_centre_shots_on_goal

        nine_metre_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_goals_scored, Unset):
            nine_metre_goals_scored = UNSET
        else:
            nine_metre_goals_scored = self.nine_metre_goals_scored

        nine_metre_left_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_goals_scored, Unset):
            nine_metre_left_goals_scored = UNSET
        else:
            nine_metre_left_goals_scored = self.nine_metre_left_goals_scored

        nine_metre_left_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_missed_shots, Unset):
            nine_metre_left_missed_shots = UNSET
        else:
            nine_metre_left_missed_shots = self.nine_metre_left_missed_shots

        nine_metre_left_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_post_hits, Unset):
            nine_metre_left_post_hits = UNSET
        else:
            nine_metre_left_post_hits = self.nine_metre_left_post_hits

        nine_metre_left_shooting_accuracy = self.nine_metre_left_shooting_accuracy

        nine_metre_left_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_shots, Unset):
            nine_metre_left_shots = UNSET
        else:
            nine_metre_left_shots = self.nine_metre_left_shots

        nine_metre_left_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_shots_blocked, Unset):
            nine_metre_left_shots_blocked = UNSET
        else:
            nine_metre_left_shots_blocked = self.nine_metre_left_shots_blocked

        nine_metre_left_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_shots_on_goal, Unset):
            nine_metre_left_shots_on_goal = UNSET
        else:
            nine_metre_left_shots_on_goal = self.nine_metre_left_shots_on_goal

        nine_metre_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_missed_shots, Unset):
            nine_metre_missed_shots = UNSET
        else:
            nine_metre_missed_shots = self.nine_metre_missed_shots

        nine_metre_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_post_hits, Unset):
            nine_metre_post_hits = UNSET
        else:
            nine_metre_post_hits = self.nine_metre_post_hits

        nine_metre_right_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_goals_scored, Unset):
            nine_metre_right_goals_scored = UNSET
        else:
            nine_metre_right_goals_scored = self.nine_metre_right_goals_scored

        nine_metre_right_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_missed_shots, Unset):
            nine_metre_right_missed_shots = UNSET
        else:
            nine_metre_right_missed_shots = self.nine_metre_right_missed_shots

        nine_metre_right_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_post_hits, Unset):
            nine_metre_right_post_hits = UNSET
        else:
            nine_metre_right_post_hits = self.nine_metre_right_post_hits

        nine_metre_right_shooting_accuracy = self.nine_metre_right_shooting_accuracy

        nine_metre_right_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_shots, Unset):
            nine_metre_right_shots = UNSET
        else:
            nine_metre_right_shots = self.nine_metre_right_shots

        nine_metre_right_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_shots_blocked, Unset):
            nine_metre_right_shots_blocked = UNSET
        else:
            nine_metre_right_shots_blocked = self.nine_metre_right_shots_blocked

        nine_metre_right_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_shots_on_goal, Unset):
            nine_metre_right_shots_on_goal = UNSET
        else:
            nine_metre_right_shots_on_goal = self.nine_metre_right_shots_on_goal

        nine_metre_shooting_accuracy = self.nine_metre_shooting_accuracy

        nine_metre_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_shots, Unset):
            nine_metre_shots = UNSET
        else:
            nine_metre_shots = self.nine_metre_shots

        nine_metre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_shots_blocked, Unset):
            nine_metre_shots_blocked = UNSET
        else:
            nine_metre_shots_blocked = self.nine_metre_shots_blocked

        nine_metre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_shots_on_goal, Unset):
            nine_metre_shots_on_goal = UNSET
        else:
            nine_metre_shots_on_goal = self.nine_metre_shots_on_goal

        passive_play: Union[None, Unset, int]
        if isinstance(self.passive_play, Unset):
            passive_play = UNSET
        else:
            passive_play = self.passive_play

        pivot_goals_scored: Union[None, Unset, int]
        if isinstance(self.pivot_goals_scored, Unset):
            pivot_goals_scored = UNSET
        else:
            pivot_goals_scored = self.pivot_goals_scored

        pivot_missed_shots: Union[None, Unset, int]
        if isinstance(self.pivot_missed_shots, Unset):
            pivot_missed_shots = UNSET
        else:
            pivot_missed_shots = self.pivot_missed_shots

        pivot_post_hits: Union[None, Unset, int]
        if isinstance(self.pivot_post_hits, Unset):
            pivot_post_hits = UNSET
        else:
            pivot_post_hits = self.pivot_post_hits

        pivot_shooting_accuracy = self.pivot_shooting_accuracy

        pivot_shots: Union[None, Unset, int]
        if isinstance(self.pivot_shots, Unset):
            pivot_shots = UNSET
        else:
            pivot_shots = self.pivot_shots

        pivot_shots_blocked: Union[None, Unset, int]
        if isinstance(self.pivot_shots_blocked, Unset):
            pivot_shots_blocked = UNSET
        else:
            pivot_shots_blocked = self.pivot_shots_blocked

        pivot_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.pivot_shots_on_goal, Unset):
            pivot_shots_on_goal = UNSET
        else:
            pivot_shots_on_goal = self.pivot_shots_on_goal

        post_hits: Union[None, Unset, int]
        if isinstance(self.post_hits, Unset):
            post_hits = UNSET
        else:
            post_hits = self.post_hits

        red_cards: Union[None, Unset, int]
        if isinstance(self.red_cards, Unset):
            red_cards = UNSET
        else:
            red_cards = self.red_cards

        seven_metre_goals_scored: Union[None, Unset, int]
        if isinstance(self.seven_metre_goals_scored, Unset):
            seven_metre_goals_scored = UNSET
        else:
            seven_metre_goals_scored = self.seven_metre_goals_scored

        seven_metre_missed_shots: Union[None, Unset, int]
        if isinstance(self.seven_metre_missed_shots, Unset):
            seven_metre_missed_shots = UNSET
        else:
            seven_metre_missed_shots = self.seven_metre_missed_shots

        seven_metre_penalties_awarded: Union[None, Unset, int]
        if isinstance(self.seven_metre_penalties_awarded, Unset):
            seven_metre_penalties_awarded = UNSET
        else:
            seven_metre_penalties_awarded = self.seven_metre_penalties_awarded

        seven_metre_penalties_caused: Union[None, Unset, int]
        if isinstance(self.seven_metre_penalties_caused, Unset):
            seven_metre_penalties_caused = UNSET
        else:
            seven_metre_penalties_caused = self.seven_metre_penalties_caused

        seven_metre_penalty_fouls: Union[None, Unset, int]
        if isinstance(self.seven_metre_penalty_fouls, Unset):
            seven_metre_penalty_fouls = UNSET
        else:
            seven_metre_penalty_fouls = self.seven_metre_penalty_fouls

        seven_metre_post_hits: Union[None, Unset, int]
        if isinstance(self.seven_metre_post_hits, Unset):
            seven_metre_post_hits = UNSET
        else:
            seven_metre_post_hits = self.seven_metre_post_hits

        seven_metre_shooting_accuracy = self.seven_metre_shooting_accuracy

        seven_metre_shots: Union[None, Unset, int]
        if isinstance(self.seven_metre_shots, Unset):
            seven_metre_shots = UNSET
        else:
            seven_metre_shots = self.seven_metre_shots

        seven_metre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.seven_metre_shots_blocked, Unset):
            seven_metre_shots_blocked = UNSET
        else:
            seven_metre_shots_blocked = self.seven_metre_shots_blocked

        seven_metre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.seven_metre_shots_on_goal, Unset):
            seven_metre_shots_on_goal = UNSET
        else:
            seven_metre_shots_on_goal = self.seven_metre_shots_on_goal

        shooting_accuracy = self.shooting_accuracy

        shoot_out_attempts: Union[None, Unset, str]
        if isinstance(self.shoot_out_attempts, Unset):
            shoot_out_attempts = UNSET
        else:
            shoot_out_attempts = self.shoot_out_attempts

        shoot_outs: Union[None, Unset, int]
        if isinstance(self.shoot_outs, Unset):
            shoot_outs = UNSET
        else:
            shoot_outs = self.shoot_outs

        shoot_outs_made: Union[None, Unset, int]
        if isinstance(self.shoot_outs_made, Unset):
            shoot_outs_made = UNSET
        else:
            shoot_outs_made = self.shoot_outs_made

        shoot_outs_missed: Union[None, Unset, int]
        if isinstance(self.shoot_outs_missed, Unset):
            shoot_outs_missed = UNSET
        else:
            shoot_outs_missed = self.shoot_outs_missed

        shoot_outs_saved: Union[None, Unset, int]
        if isinstance(self.shoot_outs_saved, Unset):
            shoot_outs_saved = UNSET
        else:
            shoot_outs_saved = self.shoot_outs_saved

        shots: Union[None, Unset, int]
        if isinstance(self.shots, Unset):
            shots = UNSET
        else:
            shots = self.shots

        shots_blocked: Union[None, Unset, int]
        if isinstance(self.shots_blocked, Unset):
            shots_blocked = UNSET
        else:
            shots_blocked = self.shots_blocked

        shots_on_goal: Union[None, Unset, int]
        if isinstance(self.shots_on_goal, Unset):
            shots_on_goal = UNSET
        else:
            shots_on_goal = self.shots_on_goal

        shots_off_goal: Union[None, Unset, int]
        if isinstance(self.shots_off_goal, Unset):
            shots_off_goal = UNSET
        else:
            shots_off_goal = self.shots_off_goal

        shots_saved_by_goal_keeper: Union[None, Unset, int]
        if isinstance(self.shots_saved_by_goal_keeper, Unset):
            shots_saved_by_goal_keeper = UNSET
        else:
            shots_saved_by_goal_keeper = self.shots_saved_by_goal_keeper

        six_metre_centre_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_goals_scored, Unset):
            six_metre_centre_goals_scored = UNSET
        else:
            six_metre_centre_goals_scored = self.six_metre_centre_goals_scored

        six_metre_centre_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_missed_shots, Unset):
            six_metre_centre_missed_shots = UNSET
        else:
            six_metre_centre_missed_shots = self.six_metre_centre_missed_shots

        six_metre_centre_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_post_hits, Unset):
            six_metre_centre_post_hits = UNSET
        else:
            six_metre_centre_post_hits = self.six_metre_centre_post_hits

        six_metre_centre_shooting_accuracy = self.six_metre_centre_shooting_accuracy

        six_metre_centre_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_shots, Unset):
            six_metre_centre_shots = UNSET
        else:
            six_metre_centre_shots = self.six_metre_centre_shots

        six_metre_centre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_shots_blocked, Unset):
            six_metre_centre_shots_blocked = UNSET
        else:
            six_metre_centre_shots_blocked = self.six_metre_centre_shots_blocked

        six_metre_centre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_shots_on_goal, Unset):
            six_metre_centre_shots_on_goal = UNSET
        else:
            six_metre_centre_shots_on_goal = self.six_metre_centre_shots_on_goal

        six_metre_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_goals_scored, Unset):
            six_metre_goals_scored = UNSET
        else:
            six_metre_goals_scored = self.six_metre_goals_scored

        six_metre_left_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_left_goals_scored, Unset):
            six_metre_left_goals_scored = UNSET
        else:
            six_metre_left_goals_scored = self.six_metre_left_goals_scored

        six_metre_left_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_left_missed_shots, Unset):
            six_metre_left_missed_shots = UNSET
        else:
            six_metre_left_missed_shots = self.six_metre_left_missed_shots

        six_metre_left_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_left_post_hits, Unset):
            six_metre_left_post_hits = UNSET
        else:
            six_metre_left_post_hits = self.six_metre_left_post_hits

        six_metre_left_shooting_accuracy = self.six_metre_left_shooting_accuracy

        six_metre_left_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_left_shots, Unset):
            six_metre_left_shots = UNSET
        else:
            six_metre_left_shots = self.six_metre_left_shots

        six_metre_left_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_left_shots_blocked, Unset):
            six_metre_left_shots_blocked = UNSET
        else:
            six_metre_left_shots_blocked = self.six_metre_left_shots_blocked

        six_metre_left_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_left_shots_on_goal, Unset):
            six_metre_left_shots_on_goal = UNSET
        else:
            six_metre_left_shots_on_goal = self.six_metre_left_shots_on_goal

        six_metre_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_missed_shots, Unset):
            six_metre_missed_shots = UNSET
        else:
            six_metre_missed_shots = self.six_metre_missed_shots

        six_metre_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_post_hits, Unset):
            six_metre_post_hits = UNSET
        else:
            six_metre_post_hits = self.six_metre_post_hits

        six_metre_right_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_right_goals_scored, Unset):
            six_metre_right_goals_scored = UNSET
        else:
            six_metre_right_goals_scored = self.six_metre_right_goals_scored

        six_metre_right_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_right_missed_shots, Unset):
            six_metre_right_missed_shots = UNSET
        else:
            six_metre_right_missed_shots = self.six_metre_right_missed_shots

        six_metre_right_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_right_post_hits, Unset):
            six_metre_right_post_hits = UNSET
        else:
            six_metre_right_post_hits = self.six_metre_right_post_hits

        six_metre_right_shooting_accuracy = self.six_metre_right_shooting_accuracy

        six_metre_right_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_right_shots, Unset):
            six_metre_right_shots = UNSET
        else:
            six_metre_right_shots = self.six_metre_right_shots

        six_metre_right_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_right_shots_blocked, Unset):
            six_metre_right_shots_blocked = UNSET
        else:
            six_metre_right_shots_blocked = self.six_metre_right_shots_blocked

        six_metre_right_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_right_shots_on_goal, Unset):
            six_metre_right_shots_on_goal = UNSET
        else:
            six_metre_right_shots_on_goal = self.six_metre_right_shots_on_goal

        six_metre_shooting_accuracy = self.six_metre_shooting_accuracy

        six_metre_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_shots, Unset):
            six_metre_shots = UNSET
        else:
            six_metre_shots = self.six_metre_shots

        six_metre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_shots_blocked, Unset):
            six_metre_shots_blocked = UNSET
        else:
            six_metre_shots_blocked = self.six_metre_shots_blocked

        six_metre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_shots_on_goal, Unset):
            six_metre_shots_on_goal = UNSET
        else:
            six_metre_shots_on_goal = self.six_metre_shots_on_goal

        steals: Union[None, Unset, int]
        if isinstance(self.steals, Unset):
            steals = UNSET
        else:
            steals = self.steals

        substitutions: Union[None, Unset, int]
        if isinstance(self.substitutions, Unset):
            substitutions = UNSET
        else:
            substitutions = self.substitutions

        suspensions: Union[None, Unset, int]
        if isinstance(self.suspensions, Unset):
            suspensions = UNSET
        else:
            suspensions = self.suspensions

        technical_ball_faults: Union[None, Unset, int]
        if isinstance(self.technical_ball_faults, Unset):
            technical_ball_faults = UNSET
        else:
            technical_ball_faults = self.technical_ball_faults

        technical_faults: Union[None, Unset, int]
        if isinstance(self.technical_faults, Unset):
            technical_faults = UNSET
        else:
            technical_faults = self.technical_faults

        technical_rule_faults: Union[None, Unset, int]
        if isinstance(self.technical_rule_faults, Unset):
            technical_rule_faults = UNSET
        else:
            technical_rule_faults = self.technical_rule_faults

        time_played: Union[None, Unset, int]
        if isinstance(self.time_played, Unset):
            time_played = UNSET
        else:
            time_played = self.time_played

        turnovers: Union[None, Unset, int]
        if isinstance(self.turnovers, Unset):
            turnovers = UNSET
        else:
            turnovers = self.turnovers

        two_minute_suspensions: Union[None, Unset, int]
        if isinstance(self.two_minute_suspensions, Unset):
            two_minute_suspensions = UNSET
        else:
            two_minute_suspensions = self.two_minute_suspensions

        wing_goals_scored: Union[None, Unset, int]
        if isinstance(self.wing_goals_scored, Unset):
            wing_goals_scored = UNSET
        else:
            wing_goals_scored = self.wing_goals_scored

        wing_left_goals_scored: Union[None, Unset, int]
        if isinstance(self.wing_left_goals_scored, Unset):
            wing_left_goals_scored = UNSET
        else:
            wing_left_goals_scored = self.wing_left_goals_scored

        wing_left_missed_shots: Union[None, Unset, int]
        if isinstance(self.wing_left_missed_shots, Unset):
            wing_left_missed_shots = UNSET
        else:
            wing_left_missed_shots = self.wing_left_missed_shots

        wing_left_post_hits: Union[None, Unset, int]
        if isinstance(self.wing_left_post_hits, Unset):
            wing_left_post_hits = UNSET
        else:
            wing_left_post_hits = self.wing_left_post_hits

        wing_left_shooting_accuracy = self.wing_left_shooting_accuracy

        wing_left_shots: Union[None, Unset, int]
        if isinstance(self.wing_left_shots, Unset):
            wing_left_shots = UNSET
        else:
            wing_left_shots = self.wing_left_shots

        wing_left_shots_blocked: Union[None, Unset, int]
        if isinstance(self.wing_left_shots_blocked, Unset):
            wing_left_shots_blocked = UNSET
        else:
            wing_left_shots_blocked = self.wing_left_shots_blocked

        wing_left_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.wing_left_shots_on_goal, Unset):
            wing_left_shots_on_goal = UNSET
        else:
            wing_left_shots_on_goal = self.wing_left_shots_on_goal

        wing_missed_shots: Union[None, Unset, int]
        if isinstance(self.wing_missed_shots, Unset):
            wing_missed_shots = UNSET
        else:
            wing_missed_shots = self.wing_missed_shots

        wing_post_hits: Union[None, Unset, int]
        if isinstance(self.wing_post_hits, Unset):
            wing_post_hits = UNSET
        else:
            wing_post_hits = self.wing_post_hits

        wing_right_goals_scored: Union[None, Unset, int]
        if isinstance(self.wing_right_goals_scored, Unset):
            wing_right_goals_scored = UNSET
        else:
            wing_right_goals_scored = self.wing_right_goals_scored

        wing_right_missed_shots: Union[None, Unset, int]
        if isinstance(self.wing_right_missed_shots, Unset):
            wing_right_missed_shots = UNSET
        else:
            wing_right_missed_shots = self.wing_right_missed_shots

        wing_right_post_hits: Union[None, Unset, int]
        if isinstance(self.wing_right_post_hits, Unset):
            wing_right_post_hits = UNSET
        else:
            wing_right_post_hits = self.wing_right_post_hits

        wing_right_shooting_accuracy = self.wing_right_shooting_accuracy

        wing_right_shots: Union[None, Unset, int]
        if isinstance(self.wing_right_shots, Unset):
            wing_right_shots = UNSET
        else:
            wing_right_shots = self.wing_right_shots

        wing_right_shots_blocked: Union[None, Unset, int]
        if isinstance(self.wing_right_shots_blocked, Unset):
            wing_right_shots_blocked = UNSET
        else:
            wing_right_shots_blocked = self.wing_right_shots_blocked

        wing_right_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.wing_right_shots_on_goal, Unset):
            wing_right_shots_on_goal = UNSET
        else:
            wing_right_shots_on_goal = self.wing_right_shots_on_goal

        wing_shooting_accuracy = self.wing_shooting_accuracy

        wing_shots: Union[None, Unset, int]
        if isinstance(self.wing_shots, Unset):
            wing_shots = UNSET
        else:
            wing_shots = self.wing_shots

        wing_shots_blocked: Union[None, Unset, int]
        if isinstance(self.wing_shots_blocked, Unset):
            wing_shots_blocked = UNSET
        else:
            wing_shots_blocked = self.wing_shots_blocked

        wing_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.wing_shots_on_goal, Unset):
            wing_shots_on_goal = UNSET
        else:
            wing_shots_on_goal = self.wing_shots_on_goal

        yellow_cards: Union[None, Unset, int]
        if isinstance(self.yellow_cards, Unset):
            yellow_cards = UNSET
        else:
            yellow_cards = self.yellow_cards

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if assists is not UNSET:
            field_dict["assists"] = assists
        if back_court_goals_scored is not UNSET:
            field_dict["backCourtGoalsScored"] = back_court_goals_scored
        if back_court_missed_shots is not UNSET:
            field_dict["backCourtMissedShots"] = back_court_missed_shots
        if back_court_post_hits is not UNSET:
            field_dict["backCourtPostHits"] = back_court_post_hits
        if back_court_shooting_accuracy is not UNSET:
            field_dict["backCourtShootingAccuracy"] = back_court_shooting_accuracy
        if back_court_shots is not UNSET:
            field_dict["backCourtShots"] = back_court_shots
        if back_court_shots_blocked is not UNSET:
            field_dict["backCourtShotsBlocked"] = back_court_shots_blocked
        if back_court_shots_on_goal is not UNSET:
            field_dict["backCourtShotsOnGoal"] = back_court_shots_on_goal
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if blue_cards is not UNSET:
            field_dict["blueCards"] = blue_cards
        if break_through_goals_scored is not UNSET:
            field_dict["breakThroughGoalsScored"] = break_through_goals_scored
        if break_through_missed_shots is not UNSET:
            field_dict["breakThroughMissedShots"] = break_through_missed_shots
        if break_through_post_hits is not UNSET:
            field_dict["breakThroughPostHits"] = break_through_post_hits
        if break_through_shooting_accuracy is not UNSET:
            field_dict["breakThroughShootingAccuracy"] = break_through_shooting_accuracy
        if break_through_shots is not UNSET:
            field_dict["breakThroughShots"] = break_through_shots
        if break_through_shots_blocked is not UNSET:
            field_dict["breakThroughShotsBlocked"] = break_through_shots_blocked
        if break_through_shots_on_goal is not UNSET:
            field_dict["breakThroughShotsOnGoal"] = break_through_shots_on_goal
        if cards is not UNSET:
            field_dict["cards"] = cards
        if empty_net_goals_scored is not UNSET:
            field_dict["emptyNetGoalsScored"] = empty_net_goals_scored
        if fast_break_goals_scored is not UNSET:
            field_dict["fastBreakGoalsScored"] = fast_break_goals_scored
        if fast_break_missed_shots is not UNSET:
            field_dict["fastBreakMissedShots"] = fast_break_missed_shots
        if fast_break_post_hits is not UNSET:
            field_dict["fastBreakPostHits"] = fast_break_post_hits
        if fast_break_shooting_accuracy is not UNSET:
            field_dict["fastBreakShootingAccuracy"] = fast_break_shooting_accuracy
        if fast_break_shots is not UNSET:
            field_dict["fastBreakShots"] = fast_break_shots
        if fast_break_shots_blocked is not UNSET:
            field_dict["fastBreakShotsBlocked"] = fast_break_shots_blocked
        if fast_break_shots_on_goal is not UNSET:
            field_dict["fastBreakShotsOnGoal"] = fast_break_shots_on_goal
        if field_goals_scored is not UNSET:
            field_dict["fieldGoalsScored"] = field_goals_scored
        if field_missed_shots is not UNSET:
            field_dict["fieldMissedShots"] = field_missed_shots
        if field_post_hits is not UNSET:
            field_dict["fieldPostHits"] = field_post_hits
        if field_shooting_accuracy is not UNSET:
            field_dict["fieldShootingAccuracy"] = field_shooting_accuracy
        if field_shots is not UNSET:
            field_dict["fieldShots"] = field_shots
        if field_shots_blocked is not UNSET:
            field_dict["fieldShotsBlocked"] = field_shots_blocked
        if field_shots_on_goal is not UNSET:
            field_dict["fieldShotsOnGoal"] = field_shots_on_goal
        if fouls is not UNSET:
            field_dict["fouls"] = fouls
        if fouls_drawn is not UNSET:
            field_dict["foulsDrawn"] = fouls_drawn
        if four_minute_suspensions is not UNSET:
            field_dict["fourMinuteSuspensions"] = four_minute_suspensions
        if goal_keeper_back_court_goals_against is not UNSET:
            field_dict["goalKeeperBackCourtGoalsAgainst"] = goal_keeper_back_court_goals_against
        if goal_keeper_back_court_save_accuracy is not UNSET:
            field_dict["goalKeeperBackCourtSaveAccuracy"] = goal_keeper_back_court_save_accuracy
        if goal_keeper_back_court_shots_against is not UNSET:
            field_dict["goalKeeperBackCourtShotsAgainst"] = goal_keeper_back_court_shots_against
        if goal_keeper_back_court_shots_saved is not UNSET:
            field_dict["goalKeeperBackCourtShotsSaved"] = goal_keeper_back_court_shots_saved
        if goal_keeper_break_through_goals_against is not UNSET:
            field_dict["goalKeeperBreakThroughGoalsAgainst"] = goal_keeper_break_through_goals_against
        if goal_keeper_break_through_save_accuracy is not UNSET:
            field_dict["goalKeeperBreakThroughSaveAccuracy"] = goal_keeper_break_through_save_accuracy
        if goal_keeper_break_through_shots_against is not UNSET:
            field_dict["goalKeeperBreakThroughShotsAgainst"] = goal_keeper_break_through_shots_against
        if goal_keeper_break_through_shots_saved is not UNSET:
            field_dict["goalKeeperBreakThroughShotsSaved"] = goal_keeper_break_through_shots_saved
        if goal_keeper_fast_break_goals_against is not UNSET:
            field_dict["goalKeeperFastBreakGoalsAgainst"] = goal_keeper_fast_break_goals_against
        if goal_keeper_fast_break_save_accuracy is not UNSET:
            field_dict["goalKeeperFastBreakSaveAccuracy"] = goal_keeper_fast_break_save_accuracy
        if goal_keeper_fast_break_shots_against is not UNSET:
            field_dict["goalKeeperFastBreakShotsAgainst"] = goal_keeper_fast_break_shots_against
        if goal_keeper_fast_break_shots_saved is not UNSET:
            field_dict["goalKeeperFastBreakShotsSaved"] = goal_keeper_fast_break_shots_saved
        if goal_keeper_field_goals_against is not UNSET:
            field_dict["goalKeeperFieldGoalsAgainst"] = goal_keeper_field_goals_against
        if goal_keeper_field_save_accuracy is not UNSET:
            field_dict["goalKeeperFieldSaveAccuracy"] = goal_keeper_field_save_accuracy
        if goal_keeper_field_shots_against is not UNSET:
            field_dict["goalKeeperFieldShotsAgainst"] = goal_keeper_field_shots_against
        if goal_keeper_field_shots_saved is not UNSET:
            field_dict["goalKeeperFieldShotsSaved"] = goal_keeper_field_shots_saved
        if goal_keeper_goals_against is not UNSET:
            field_dict["goalKeeperGoalsAgainst"] = goal_keeper_goals_against
        if goal_keeper_nine_metre_centre_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreCentreGoalsAgainst"] = goal_keeper_nine_metre_centre_goals_against
        if goal_keeper_nine_metre_centre_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreCentreSaveAccuracy"] = goal_keeper_nine_metre_centre_save_accuracy
        if goal_keeper_nine_metre_centre_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreCentreShotsAgainst"] = goal_keeper_nine_metre_centre_shots_against
        if goal_keeper_nine_metre_centre_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreCentreShotsSaved"] = goal_keeper_nine_metre_centre_shots_saved
        if goal_keeper_nine_metre_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreGoalsAgainst"] = goal_keeper_nine_metre_goals_against
        if goal_keeper_nine_metre_left_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreLeftGoalsAgainst"] = goal_keeper_nine_metre_left_goals_against
        if goal_keeper_nine_metre_left_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreLeftSaveAccuracy"] = goal_keeper_nine_metre_left_save_accuracy
        if goal_keeper_nine_metre_left_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreLeftShotsAgainst"] = goal_keeper_nine_metre_left_shots_against
        if goal_keeper_nine_metre_left_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreLeftShotsSaved"] = goal_keeper_nine_metre_left_shots_saved
        if goal_keeper_nine_metre_right_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreRightGoalsAgainst"] = goal_keeper_nine_metre_right_goals_against
        if goal_keeper_nine_metre_right_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreRightSaveAccuracy"] = goal_keeper_nine_metre_right_save_accuracy
        if goal_keeper_nine_metre_right_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreRightShotsAgainst"] = goal_keeper_nine_metre_right_shots_against
        if goal_keeper_nine_metre_right_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreRightShotsSaved"] = goal_keeper_nine_metre_right_shots_saved
        if goal_keeper_nine_metre_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreSaveAccuracy"] = goal_keeper_nine_metre_save_accuracy
        if goal_keeper_nine_metre_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreShotsAgainst"] = goal_keeper_nine_metre_shots_against
        if goal_keeper_nine_metre_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreShotsSaved"] = goal_keeper_nine_metre_shots_saved
        if goal_keeper_pivot_goals_against is not UNSET:
            field_dict["goalKeeperPivotGoalsAgainst"] = goal_keeper_pivot_goals_against
        if goal_keeper_pivot_save_accuracy is not UNSET:
            field_dict["goalKeeperPivotSaveAccuracy"] = goal_keeper_pivot_save_accuracy
        if goal_keeper_pivot_shots_against is not UNSET:
            field_dict["goalKeeperPivotShotsAgainst"] = goal_keeper_pivot_shots_against
        if goal_keeper_pivot_shots_saved is not UNSET:
            field_dict["goalKeeperPivotShotsSaved"] = goal_keeper_pivot_shots_saved
        if goal_keeper_save_accuracy is not UNSET:
            field_dict["goalKeeperSaveAccuracy"] = goal_keeper_save_accuracy
        if goal_keeper_seconds_played is not UNSET:
            field_dict["goalKeeperSecondsPlayed"] = goal_keeper_seconds_played
        if goal_keeper_seven_metre_goals_against is not UNSET:
            field_dict["goalKeeperSevenMetreGoalsAgainst"] = goal_keeper_seven_metre_goals_against
        if goal_keeper_seven_metre_save_accuracy is not UNSET:
            field_dict["goalKeeperSevenMetreSaveAccuracy"] = goal_keeper_seven_metre_save_accuracy
        if goal_keeper_seven_metre_shots_against is not UNSET:
            field_dict["goalKeeperSevenMetreShotsAgainst"] = goal_keeper_seven_metre_shots_against
        if goal_keeper_seven_metre_shots_saved is not UNSET:
            field_dict["goalKeeperSevenMetreShotsSaved"] = goal_keeper_seven_metre_shots_saved
        if goal_keeper_shots_against is not UNSET:
            field_dict["goalKeeperShotsAgainst"] = goal_keeper_shots_against
        if goal_keeper_shots_saved is not UNSET:
            field_dict["goalKeeperShotsSaved"] = goal_keeper_shots_saved
        if goal_keeper_six_metre_centre_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreCentreGoalsAgainst"] = goal_keeper_six_metre_centre_goals_against
        if goal_keeper_six_metre_centre_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreCentreSaveAccuracy"] = goal_keeper_six_metre_centre_save_accuracy
        if goal_keeper_six_metre_centre_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreCentreShotsAgainst"] = goal_keeper_six_metre_centre_shots_against
        if goal_keeper_six_metre_centre_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreCentreShotsSaved"] = goal_keeper_six_metre_centre_shots_saved
        if goal_keeper_six_metre_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreGoalsAgainst"] = goal_keeper_six_metre_goals_against
        if goal_keeper_six_metre_left_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreLeftGoalsAgainst"] = goal_keeper_six_metre_left_goals_against
        if goal_keeper_six_metre_left_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreLeftSaveAccuracy"] = goal_keeper_six_metre_left_save_accuracy
        if goal_keeper_six_metre_left_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreLeftShotsAgainst"] = goal_keeper_six_metre_left_shots_against
        if goal_keeper_six_metre_left_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreLeftShotsSaved"] = goal_keeper_six_metre_left_shots_saved
        if goal_keeper_six_metre_right_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreRightGoalsAgainst"] = goal_keeper_six_metre_right_goals_against
        if goal_keeper_six_metre_right_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreRightSaveAccuracy"] = goal_keeper_six_metre_right_save_accuracy
        if goal_keeper_six_metre_right_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreRightShotsAgainst"] = goal_keeper_six_metre_right_shots_against
        if goal_keeper_six_metre_right_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreRightShotsSaved"] = goal_keeper_six_metre_right_shots_saved
        if goal_keeper_six_metre_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreSaveAccuracy"] = goal_keeper_six_metre_save_accuracy
        if goal_keeper_six_metre_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreShotsAgainst"] = goal_keeper_six_metre_shots_against
        if goal_keeper_six_metre_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreShotsSaved"] = goal_keeper_six_metre_shots_saved
        if goal_keeper_wing_goals_against is not UNSET:
            field_dict["goalKeeperWingGoalsAgainst"] = goal_keeper_wing_goals_against
        if goal_keeper_wing_left_goals_against is not UNSET:
            field_dict["goalKeeperWingLeftGoalsAgainst"] = goal_keeper_wing_left_goals_against
        if goal_keeper_wing_left_save_accuracy is not UNSET:
            field_dict["goalKeeperWingLeftSaveAccuracy"] = goal_keeper_wing_left_save_accuracy
        if goal_keeper_wing_left_shots_against is not UNSET:
            field_dict["goalKeeperWingLeftShotsAgainst"] = goal_keeper_wing_left_shots_against
        if goal_keeper_wing_left_shots_saved is not UNSET:
            field_dict["goalKeeperWingLeftShotsSaved"] = goal_keeper_wing_left_shots_saved
        if goal_keeper_wing_right_goals_against is not UNSET:
            field_dict["goalKeeperWingRightGoalsAgainst"] = goal_keeper_wing_right_goals_against
        if goal_keeper_wing_right_save_accuracy is not UNSET:
            field_dict["goalKeeperWingRightSaveAccuracy"] = goal_keeper_wing_right_save_accuracy
        if goal_keeper_wing_right_shots_against is not UNSET:
            field_dict["goalKeeperWingRightShotsAgainst"] = goal_keeper_wing_right_shots_against
        if goal_keeper_wing_right_shots_saved is not UNSET:
            field_dict["goalKeeperWingRightShotsSaved"] = goal_keeper_wing_right_shots_saved
        if goal_keeper_wing_save_accuracy is not UNSET:
            field_dict["goalKeeperWingSaveAccuracy"] = goal_keeper_wing_save_accuracy
        if goal_keeper_wing_shots_against is not UNSET:
            field_dict["goalKeeperWingShotsAgainst"] = goal_keeper_wing_shots_against
        if goal_keeper_wing_shots_saved is not UNSET:
            field_dict["goalKeeperWingShotsSaved"] = goal_keeper_wing_shots_saved
        if goals_scored is not UNSET:
            field_dict["goalsScored"] = goals_scored
        if missed_shots is not UNSET:
            field_dict["missedShots"] = missed_shots
        if nine_metre_centre_goals_scored is not UNSET:
            field_dict["nineMetreCentreGoalsScored"] = nine_metre_centre_goals_scored
        if nine_metre_centre_missed_shots is not UNSET:
            field_dict["nineMetreCentreMissedShots"] = nine_metre_centre_missed_shots
        if nine_metre_centre_post_hits is not UNSET:
            field_dict["nineMetreCentrePostHits"] = nine_metre_centre_post_hits
        if nine_metre_centre_shooting_accuracy is not UNSET:
            field_dict["nineMetreCentreShootingAccuracy"] = nine_metre_centre_shooting_accuracy
        if nine_metre_centre_shots is not UNSET:
            field_dict["nineMetreCentreShots"] = nine_metre_centre_shots
        if nine_metre_centre_shots_blocked is not UNSET:
            field_dict["nineMetreCentreShotsBlocked"] = nine_metre_centre_shots_blocked
        if nine_metre_centre_shots_on_goal is not UNSET:
            field_dict["nineMetreCentreShotsOnGoal"] = nine_metre_centre_shots_on_goal
        if nine_metre_goals_scored is not UNSET:
            field_dict["nineMetreGoalsScored"] = nine_metre_goals_scored
        if nine_metre_left_goals_scored is not UNSET:
            field_dict["nineMetreLeftGoalsScored"] = nine_metre_left_goals_scored
        if nine_metre_left_missed_shots is not UNSET:
            field_dict["nineMetreLeftMissedShots"] = nine_metre_left_missed_shots
        if nine_metre_left_post_hits is not UNSET:
            field_dict["nineMetreLeftPostHits"] = nine_metre_left_post_hits
        if nine_metre_left_shooting_accuracy is not UNSET:
            field_dict["nineMetreLeftShootingAccuracy"] = nine_metre_left_shooting_accuracy
        if nine_metre_left_shots is not UNSET:
            field_dict["nineMetreLeftShots"] = nine_metre_left_shots
        if nine_metre_left_shots_blocked is not UNSET:
            field_dict["nineMetreLeftShotsBlocked"] = nine_metre_left_shots_blocked
        if nine_metre_left_shots_on_goal is not UNSET:
            field_dict["nineMetreLeftShotsOnGoal"] = nine_metre_left_shots_on_goal
        if nine_metre_missed_shots is not UNSET:
            field_dict["nineMetreMissedShots"] = nine_metre_missed_shots
        if nine_metre_post_hits is not UNSET:
            field_dict["nineMetrePostHits"] = nine_metre_post_hits
        if nine_metre_right_goals_scored is not UNSET:
            field_dict["nineMetreRightGoalsScored"] = nine_metre_right_goals_scored
        if nine_metre_right_missed_shots is not UNSET:
            field_dict["nineMetreRightMissedShots"] = nine_metre_right_missed_shots
        if nine_metre_right_post_hits is not UNSET:
            field_dict["nineMetreRightPostHits"] = nine_metre_right_post_hits
        if nine_metre_right_shooting_accuracy is not UNSET:
            field_dict["nineMetreRightShootingAccuracy"] = nine_metre_right_shooting_accuracy
        if nine_metre_right_shots is not UNSET:
            field_dict["nineMetreRightShots"] = nine_metre_right_shots
        if nine_metre_right_shots_blocked is not UNSET:
            field_dict["nineMetreRightShotsBlocked"] = nine_metre_right_shots_blocked
        if nine_metre_right_shots_on_goal is not UNSET:
            field_dict["nineMetreRightShotsOnGoal"] = nine_metre_right_shots_on_goal
        if nine_metre_shooting_accuracy is not UNSET:
            field_dict["nineMetreShootingAccuracy"] = nine_metre_shooting_accuracy
        if nine_metre_shots is not UNSET:
            field_dict["nineMetreShots"] = nine_metre_shots
        if nine_metre_shots_blocked is not UNSET:
            field_dict["nineMetreShotsBlocked"] = nine_metre_shots_blocked
        if nine_metre_shots_on_goal is not UNSET:
            field_dict["nineMetreShotsOnGoal"] = nine_metre_shots_on_goal
        if passive_play is not UNSET:
            field_dict["passivePlay"] = passive_play
        if pivot_goals_scored is not UNSET:
            field_dict["pivotGoalsScored"] = pivot_goals_scored
        if pivot_missed_shots is not UNSET:
            field_dict["pivotMissedShots"] = pivot_missed_shots
        if pivot_post_hits is not UNSET:
            field_dict["pivotPostHits"] = pivot_post_hits
        if pivot_shooting_accuracy is not UNSET:
            field_dict["pivotShootingAccuracy"] = pivot_shooting_accuracy
        if pivot_shots is not UNSET:
            field_dict["pivotShots"] = pivot_shots
        if pivot_shots_blocked is not UNSET:
            field_dict["pivotShotsBlocked"] = pivot_shots_blocked
        if pivot_shots_on_goal is not UNSET:
            field_dict["pivotShotsOnGoal"] = pivot_shots_on_goal
        if post_hits is not UNSET:
            field_dict["postHits"] = post_hits
        if red_cards is not UNSET:
            field_dict["redCards"] = red_cards
        if seven_metre_goals_scored is not UNSET:
            field_dict["sevenMetreGoalsScored"] = seven_metre_goals_scored
        if seven_metre_missed_shots is not UNSET:
            field_dict["sevenMetreMissedShots"] = seven_metre_missed_shots
        if seven_metre_penalties_awarded is not UNSET:
            field_dict["sevenMetrePenaltiesAwarded"] = seven_metre_penalties_awarded
        if seven_metre_penalties_caused is not UNSET:
            field_dict["sevenMetrePenaltiesCaused"] = seven_metre_penalties_caused
        if seven_metre_penalty_fouls is not UNSET:
            field_dict["sevenMetrePenaltyFouls"] = seven_metre_penalty_fouls
        if seven_metre_post_hits is not UNSET:
            field_dict["sevenMetrePostHits"] = seven_metre_post_hits
        if seven_metre_shooting_accuracy is not UNSET:
            field_dict["sevenMetreShootingAccuracy"] = seven_metre_shooting_accuracy
        if seven_metre_shots is not UNSET:
            field_dict["sevenMetreShots"] = seven_metre_shots
        if seven_metre_shots_blocked is not UNSET:
            field_dict["sevenMetreShotsBlocked"] = seven_metre_shots_blocked
        if seven_metre_shots_on_goal is not UNSET:
            field_dict["sevenMetreShotsOnGoal"] = seven_metre_shots_on_goal
        if shooting_accuracy is not UNSET:
            field_dict["shootingAccuracy"] = shooting_accuracy
        if shoot_out_attempts is not UNSET:
            field_dict["shootOutAttempts"] = shoot_out_attempts
        if shoot_outs is not UNSET:
            field_dict["shootOuts"] = shoot_outs
        if shoot_outs_made is not UNSET:
            field_dict["shootOutsMade"] = shoot_outs_made
        if shoot_outs_missed is not UNSET:
            field_dict["shootOutsMissed"] = shoot_outs_missed
        if shoot_outs_saved is not UNSET:
            field_dict["shootOutsSaved"] = shoot_outs_saved
        if shots is not UNSET:
            field_dict["shots"] = shots
        if shots_blocked is not UNSET:
            field_dict["shotsBlocked"] = shots_blocked
        if shots_on_goal is not UNSET:
            field_dict["shotsOnGoal"] = shots_on_goal
        if shots_off_goal is not UNSET:
            field_dict["shotsOffGoal"] = shots_off_goal
        if shots_saved_by_goal_keeper is not UNSET:
            field_dict["shotsSavedByGoalKeeper"] = shots_saved_by_goal_keeper
        if six_metre_centre_goals_scored is not UNSET:
            field_dict["sixMetreCentreGoalsScored"] = six_metre_centre_goals_scored
        if six_metre_centre_missed_shots is not UNSET:
            field_dict["sixMetreCentreMissedShots"] = six_metre_centre_missed_shots
        if six_metre_centre_post_hits is not UNSET:
            field_dict["sixMetreCentrePostHits"] = six_metre_centre_post_hits
        if six_metre_centre_shooting_accuracy is not UNSET:
            field_dict["sixMetreCentreShootingAccuracy"] = six_metre_centre_shooting_accuracy
        if six_metre_centre_shots is not UNSET:
            field_dict["sixMetreCentreShots"] = six_metre_centre_shots
        if six_metre_centre_shots_blocked is not UNSET:
            field_dict["sixMetreCentreShotsBlocked"] = six_metre_centre_shots_blocked
        if six_metre_centre_shots_on_goal is not UNSET:
            field_dict["sixMetreCentreShotsOnGoal"] = six_metre_centre_shots_on_goal
        if six_metre_goals_scored is not UNSET:
            field_dict["sixMetreGoalsScored"] = six_metre_goals_scored
        if six_metre_left_goals_scored is not UNSET:
            field_dict["sixMetreLeftGoalsScored"] = six_metre_left_goals_scored
        if six_metre_left_missed_shots is not UNSET:
            field_dict["sixMetreLeftMissedShots"] = six_metre_left_missed_shots
        if six_metre_left_post_hits is not UNSET:
            field_dict["sixMetreLeftPostHits"] = six_metre_left_post_hits
        if six_metre_left_shooting_accuracy is not UNSET:
            field_dict["sixMetreLeftShootingAccuracy"] = six_metre_left_shooting_accuracy
        if six_metre_left_shots is not UNSET:
            field_dict["sixMetreLeftShots"] = six_metre_left_shots
        if six_metre_left_shots_blocked is not UNSET:
            field_dict["sixMetreLeftShotsBlocked"] = six_metre_left_shots_blocked
        if six_metre_left_shots_on_goal is not UNSET:
            field_dict["sixMetreLeftShotsOnGoal"] = six_metre_left_shots_on_goal
        if six_metre_missed_shots is not UNSET:
            field_dict["sixMetreMissedShots"] = six_metre_missed_shots
        if six_metre_post_hits is not UNSET:
            field_dict["sixMetrePostHits"] = six_metre_post_hits
        if six_metre_right_goals_scored is not UNSET:
            field_dict["sixMetreRightGoalsScored"] = six_metre_right_goals_scored
        if six_metre_right_missed_shots is not UNSET:
            field_dict["sixMetreRightMissedShots"] = six_metre_right_missed_shots
        if six_metre_right_post_hits is not UNSET:
            field_dict["sixMetreRightPostHits"] = six_metre_right_post_hits
        if six_metre_right_shooting_accuracy is not UNSET:
            field_dict["sixMetreRightShootingAccuracy"] = six_metre_right_shooting_accuracy
        if six_metre_right_shots is not UNSET:
            field_dict["sixMetreRightShots"] = six_metre_right_shots
        if six_metre_right_shots_blocked is not UNSET:
            field_dict["sixMetreRightShotsBlocked"] = six_metre_right_shots_blocked
        if six_metre_right_shots_on_goal is not UNSET:
            field_dict["sixMetreRightShotsOnGoal"] = six_metre_right_shots_on_goal
        if six_metre_shooting_accuracy is not UNSET:
            field_dict["sixMetreShootingAccuracy"] = six_metre_shooting_accuracy
        if six_metre_shots is not UNSET:
            field_dict["sixMetreShots"] = six_metre_shots
        if six_metre_shots_blocked is not UNSET:
            field_dict["sixMetreShotsBlocked"] = six_metre_shots_blocked
        if six_metre_shots_on_goal is not UNSET:
            field_dict["sixMetreShotsOnGoal"] = six_metre_shots_on_goal
        if steals is not UNSET:
            field_dict["steals"] = steals
        if substitutions is not UNSET:
            field_dict["substitutions"] = substitutions
        if suspensions is not UNSET:
            field_dict["suspensions"] = suspensions
        if technical_ball_faults is not UNSET:
            field_dict["technicalBallFaults"] = technical_ball_faults
        if technical_faults is not UNSET:
            field_dict["technicalFaults"] = technical_faults
        if technical_rule_faults is not UNSET:
            field_dict["technicalRuleFaults"] = technical_rule_faults
        if time_played is not UNSET:
            field_dict["timePlayed"] = time_played
        if turnovers is not UNSET:
            field_dict["turnovers"] = turnovers
        if two_minute_suspensions is not UNSET:
            field_dict["twoMinuteSuspensions"] = two_minute_suspensions
        if wing_goals_scored is not UNSET:
            field_dict["wingGoalsScored"] = wing_goals_scored
        if wing_left_goals_scored is not UNSET:
            field_dict["wingLeftGoalsScored"] = wing_left_goals_scored
        if wing_left_missed_shots is not UNSET:
            field_dict["wingLeftMissedShots"] = wing_left_missed_shots
        if wing_left_post_hits is not UNSET:
            field_dict["wingLeftPostHits"] = wing_left_post_hits
        if wing_left_shooting_accuracy is not UNSET:
            field_dict["wingLeftShootingAccuracy"] = wing_left_shooting_accuracy
        if wing_left_shots is not UNSET:
            field_dict["wingLeftShots"] = wing_left_shots
        if wing_left_shots_blocked is not UNSET:
            field_dict["wingLeftShotsBlocked"] = wing_left_shots_blocked
        if wing_left_shots_on_goal is not UNSET:
            field_dict["wingLeftShotsOnGoal"] = wing_left_shots_on_goal
        if wing_missed_shots is not UNSET:
            field_dict["wingMissedShots"] = wing_missed_shots
        if wing_post_hits is not UNSET:
            field_dict["wingPostHits"] = wing_post_hits
        if wing_right_goals_scored is not UNSET:
            field_dict["wingRightGoalsScored"] = wing_right_goals_scored
        if wing_right_missed_shots is not UNSET:
            field_dict["wingRightMissedShots"] = wing_right_missed_shots
        if wing_right_post_hits is not UNSET:
            field_dict["wingRightPostHits"] = wing_right_post_hits
        if wing_right_shooting_accuracy is not UNSET:
            field_dict["wingRightShootingAccuracy"] = wing_right_shooting_accuracy
        if wing_right_shots is not UNSET:
            field_dict["wingRightShots"] = wing_right_shots
        if wing_right_shots_blocked is not UNSET:
            field_dict["wingRightShotsBlocked"] = wing_right_shots_blocked
        if wing_right_shots_on_goal is not UNSET:
            field_dict["wingRightShotsOnGoal"] = wing_right_shots_on_goal
        if wing_shooting_accuracy is not UNSET:
            field_dict["wingShootingAccuracy"] = wing_shooting_accuracy
        if wing_shots is not UNSET:
            field_dict["wingShots"] = wing_shots
        if wing_shots_blocked is not UNSET:
            field_dict["wingShotsBlocked"] = wing_shots_blocked
        if wing_shots_on_goal is not UNSET:
            field_dict["wingShotsOnGoal"] = wing_shots_on_goal
        if yellow_cards is not UNSET:
            field_dict["yellowCards"] = yellow_cards

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_assists(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assists = _parse_assists(d.pop("assists", UNSET))

        def _parse_back_court_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_goals_scored = _parse_back_court_goals_scored(d.pop("backCourtGoalsScored", UNSET))

        def _parse_back_court_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_missed_shots = _parse_back_court_missed_shots(d.pop("backCourtMissedShots", UNSET))

        def _parse_back_court_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_post_hits = _parse_back_court_post_hits(d.pop("backCourtPostHits", UNSET))

        back_court_shooting_accuracy = d.pop("backCourtShootingAccuracy", UNSET)

        def _parse_back_court_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_shots = _parse_back_court_shots(d.pop("backCourtShots", UNSET))

        def _parse_back_court_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_shots_blocked = _parse_back_court_shots_blocked(d.pop("backCourtShotsBlocked", UNSET))

        def _parse_back_court_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_shots_on_goal = _parse_back_court_shots_on_goal(d.pop("backCourtShotsOnGoal", UNSET))

        def _parse_blocks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        blocks = _parse_blocks(d.pop("blocks", UNSET))

        def _parse_blue_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        blue_cards = _parse_blue_cards(d.pop("blueCards", UNSET))

        def _parse_break_through_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_goals_scored = _parse_break_through_goals_scored(d.pop("breakThroughGoalsScored", UNSET))

        def _parse_break_through_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_missed_shots = _parse_break_through_missed_shots(d.pop("breakThroughMissedShots", UNSET))

        def _parse_break_through_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_post_hits = _parse_break_through_post_hits(d.pop("breakThroughPostHits", UNSET))

        break_through_shooting_accuracy = d.pop("breakThroughShootingAccuracy", UNSET)

        def _parse_break_through_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_shots = _parse_break_through_shots(d.pop("breakThroughShots", UNSET))

        def _parse_break_through_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_shots_blocked = _parse_break_through_shots_blocked(d.pop("breakThroughShotsBlocked", UNSET))

        def _parse_break_through_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_shots_on_goal = _parse_break_through_shots_on_goal(d.pop("breakThroughShotsOnGoal", UNSET))

        def _parse_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cards = _parse_cards(d.pop("cards", UNSET))

        def _parse_empty_net_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        empty_net_goals_scored = _parse_empty_net_goals_scored(d.pop("emptyNetGoalsScored", UNSET))

        def _parse_fast_break_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_goals_scored = _parse_fast_break_goals_scored(d.pop("fastBreakGoalsScored", UNSET))

        def _parse_fast_break_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_missed_shots = _parse_fast_break_missed_shots(d.pop("fastBreakMissedShots", UNSET))

        def _parse_fast_break_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_post_hits = _parse_fast_break_post_hits(d.pop("fastBreakPostHits", UNSET))

        fast_break_shooting_accuracy = d.pop("fastBreakShootingAccuracy", UNSET)

        def _parse_fast_break_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_shots = _parse_fast_break_shots(d.pop("fastBreakShots", UNSET))

        def _parse_fast_break_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_shots_blocked = _parse_fast_break_shots_blocked(d.pop("fastBreakShotsBlocked", UNSET))

        def _parse_fast_break_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_shots_on_goal = _parse_fast_break_shots_on_goal(d.pop("fastBreakShotsOnGoal", UNSET))

        def _parse_field_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_goals_scored = _parse_field_goals_scored(d.pop("fieldGoalsScored", UNSET))

        def _parse_field_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_missed_shots = _parse_field_missed_shots(d.pop("fieldMissedShots", UNSET))

        def _parse_field_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_post_hits = _parse_field_post_hits(d.pop("fieldPostHits", UNSET))

        field_shooting_accuracy = d.pop("fieldShootingAccuracy", UNSET)

        def _parse_field_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_shots = _parse_field_shots(d.pop("fieldShots", UNSET))

        def _parse_field_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_shots_blocked = _parse_field_shots_blocked(d.pop("fieldShotsBlocked", UNSET))

        def _parse_field_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_shots_on_goal = _parse_field_shots_on_goal(d.pop("fieldShotsOnGoal", UNSET))

        def _parse_fouls(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fouls = _parse_fouls(d.pop("fouls", UNSET))

        def _parse_fouls_drawn(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fouls_drawn = _parse_fouls_drawn(d.pop("foulsDrawn", UNSET))

        def _parse_four_minute_suspensions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        four_minute_suspensions = _parse_four_minute_suspensions(d.pop("fourMinuteSuspensions", UNSET))

        def _parse_goal_keeper_back_court_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_back_court_goals_against = _parse_goal_keeper_back_court_goals_against(
            d.pop("goalKeeperBackCourtGoalsAgainst", UNSET)
        )

        goal_keeper_back_court_save_accuracy = d.pop("goalKeeperBackCourtSaveAccuracy", UNSET)

        def _parse_goal_keeper_back_court_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_back_court_shots_against = _parse_goal_keeper_back_court_shots_against(
            d.pop("goalKeeperBackCourtShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_back_court_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_back_court_shots_saved = _parse_goal_keeper_back_court_shots_saved(
            d.pop("goalKeeperBackCourtShotsSaved", UNSET)
        )

        def _parse_goal_keeper_break_through_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_break_through_goals_against = _parse_goal_keeper_break_through_goals_against(
            d.pop("goalKeeperBreakThroughGoalsAgainst", UNSET)
        )

        goal_keeper_break_through_save_accuracy = d.pop("goalKeeperBreakThroughSaveAccuracy", UNSET)

        def _parse_goal_keeper_break_through_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_break_through_shots_against = _parse_goal_keeper_break_through_shots_against(
            d.pop("goalKeeperBreakThroughShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_break_through_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_break_through_shots_saved = _parse_goal_keeper_break_through_shots_saved(
            d.pop("goalKeeperBreakThroughShotsSaved", UNSET)
        )

        def _parse_goal_keeper_fast_break_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_fast_break_goals_against = _parse_goal_keeper_fast_break_goals_against(
            d.pop("goalKeeperFastBreakGoalsAgainst", UNSET)
        )

        goal_keeper_fast_break_save_accuracy = d.pop("goalKeeperFastBreakSaveAccuracy", UNSET)

        def _parse_goal_keeper_fast_break_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_fast_break_shots_against = _parse_goal_keeper_fast_break_shots_against(
            d.pop("goalKeeperFastBreakShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_fast_break_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_fast_break_shots_saved = _parse_goal_keeper_fast_break_shots_saved(
            d.pop("goalKeeperFastBreakShotsSaved", UNSET)
        )

        def _parse_goal_keeper_field_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_field_goals_against = _parse_goal_keeper_field_goals_against(
            d.pop("goalKeeperFieldGoalsAgainst", UNSET)
        )

        goal_keeper_field_save_accuracy = d.pop("goalKeeperFieldSaveAccuracy", UNSET)

        def _parse_goal_keeper_field_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_field_shots_against = _parse_goal_keeper_field_shots_against(
            d.pop("goalKeeperFieldShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_field_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_field_shots_saved = _parse_goal_keeper_field_shots_saved(d.pop("goalKeeperFieldShotsSaved", UNSET))

        def _parse_goal_keeper_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_goals_against = _parse_goal_keeper_goals_against(d.pop("goalKeeperGoalsAgainst", UNSET))

        def _parse_goal_keeper_nine_metre_centre_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_centre_goals_against = _parse_goal_keeper_nine_metre_centre_goals_against(
            d.pop("goalKeeperNineMetreCentreGoalsAgainst", UNSET)
        )

        goal_keeper_nine_metre_centre_save_accuracy = d.pop("goalKeeperNineMetreCentreSaveAccuracy", UNSET)

        def _parse_goal_keeper_nine_metre_centre_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_centre_shots_against = _parse_goal_keeper_nine_metre_centre_shots_against(
            d.pop("goalKeeperNineMetreCentreShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_nine_metre_centre_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_centre_shots_saved = _parse_goal_keeper_nine_metre_centre_shots_saved(
            d.pop("goalKeeperNineMetreCentreShotsSaved", UNSET)
        )

        def _parse_goal_keeper_nine_metre_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_goals_against = _parse_goal_keeper_nine_metre_goals_against(
            d.pop("goalKeeperNineMetreGoalsAgainst", UNSET)
        )

        def _parse_goal_keeper_nine_metre_left_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_left_goals_against = _parse_goal_keeper_nine_metre_left_goals_against(
            d.pop("goalKeeperNineMetreLeftGoalsAgainst", UNSET)
        )

        goal_keeper_nine_metre_left_save_accuracy = d.pop("goalKeeperNineMetreLeftSaveAccuracy", UNSET)

        def _parse_goal_keeper_nine_metre_left_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_left_shots_against = _parse_goal_keeper_nine_metre_left_shots_against(
            d.pop("goalKeeperNineMetreLeftShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_nine_metre_left_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_left_shots_saved = _parse_goal_keeper_nine_metre_left_shots_saved(
            d.pop("goalKeeperNineMetreLeftShotsSaved", UNSET)
        )

        def _parse_goal_keeper_nine_metre_right_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_right_goals_against = _parse_goal_keeper_nine_metre_right_goals_against(
            d.pop("goalKeeperNineMetreRightGoalsAgainst", UNSET)
        )

        goal_keeper_nine_metre_right_save_accuracy = d.pop("goalKeeperNineMetreRightSaveAccuracy", UNSET)

        def _parse_goal_keeper_nine_metre_right_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_right_shots_against = _parse_goal_keeper_nine_metre_right_shots_against(
            d.pop("goalKeeperNineMetreRightShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_nine_metre_right_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_right_shots_saved = _parse_goal_keeper_nine_metre_right_shots_saved(
            d.pop("goalKeeperNineMetreRightShotsSaved", UNSET)
        )

        goal_keeper_nine_metre_save_accuracy = d.pop("goalKeeperNineMetreSaveAccuracy", UNSET)

        def _parse_goal_keeper_nine_metre_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_shots_against = _parse_goal_keeper_nine_metre_shots_against(
            d.pop("goalKeeperNineMetreShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_nine_metre_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_shots_saved = _parse_goal_keeper_nine_metre_shots_saved(
            d.pop("goalKeeperNineMetreShotsSaved", UNSET)
        )

        def _parse_goal_keeper_pivot_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_pivot_goals_against = _parse_goal_keeper_pivot_goals_against(
            d.pop("goalKeeperPivotGoalsAgainst", UNSET)
        )

        goal_keeper_pivot_save_accuracy = d.pop("goalKeeperPivotSaveAccuracy", UNSET)

        def _parse_goal_keeper_pivot_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_pivot_shots_against = _parse_goal_keeper_pivot_shots_against(
            d.pop("goalKeeperPivotShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_pivot_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_pivot_shots_saved = _parse_goal_keeper_pivot_shots_saved(d.pop("goalKeeperPivotShotsSaved", UNSET))

        goal_keeper_save_accuracy = d.pop("goalKeeperSaveAccuracy", UNSET)

        def _parse_goal_keeper_seconds_played(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seconds_played = _parse_goal_keeper_seconds_played(d.pop("goalKeeperSecondsPlayed", UNSET))

        def _parse_goal_keeper_seven_metre_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seven_metre_goals_against = _parse_goal_keeper_seven_metre_goals_against(
            d.pop("goalKeeperSevenMetreGoalsAgainst", UNSET)
        )

        goal_keeper_seven_metre_save_accuracy = d.pop("goalKeeperSevenMetreSaveAccuracy", UNSET)

        def _parse_goal_keeper_seven_metre_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seven_metre_shots_against = _parse_goal_keeper_seven_metre_shots_against(
            d.pop("goalKeeperSevenMetreShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_seven_metre_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seven_metre_shots_saved = _parse_goal_keeper_seven_metre_shots_saved(
            d.pop("goalKeeperSevenMetreShotsSaved", UNSET)
        )

        def _parse_goal_keeper_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_shots_against = _parse_goal_keeper_shots_against(d.pop("goalKeeperShotsAgainst", UNSET))

        def _parse_goal_keeper_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_shots_saved = _parse_goal_keeper_shots_saved(d.pop("goalKeeperShotsSaved", UNSET))

        def _parse_goal_keeper_six_metre_centre_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_centre_goals_against = _parse_goal_keeper_six_metre_centre_goals_against(
            d.pop("goalKeeperSixMetreCentreGoalsAgainst", UNSET)
        )

        goal_keeper_six_metre_centre_save_accuracy = d.pop("goalKeeperSixMetreCentreSaveAccuracy", UNSET)

        def _parse_goal_keeper_six_metre_centre_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_centre_shots_against = _parse_goal_keeper_six_metre_centre_shots_against(
            d.pop("goalKeeperSixMetreCentreShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_six_metre_centre_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_centre_shots_saved = _parse_goal_keeper_six_metre_centre_shots_saved(
            d.pop("goalKeeperSixMetreCentreShotsSaved", UNSET)
        )

        def _parse_goal_keeper_six_metre_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_goals_against = _parse_goal_keeper_six_metre_goals_against(
            d.pop("goalKeeperSixMetreGoalsAgainst", UNSET)
        )

        def _parse_goal_keeper_six_metre_left_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_left_goals_against = _parse_goal_keeper_six_metre_left_goals_against(
            d.pop("goalKeeperSixMetreLeftGoalsAgainst", UNSET)
        )

        goal_keeper_six_metre_left_save_accuracy = d.pop("goalKeeperSixMetreLeftSaveAccuracy", UNSET)

        def _parse_goal_keeper_six_metre_left_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_left_shots_against = _parse_goal_keeper_six_metre_left_shots_against(
            d.pop("goalKeeperSixMetreLeftShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_six_metre_left_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_left_shots_saved = _parse_goal_keeper_six_metre_left_shots_saved(
            d.pop("goalKeeperSixMetreLeftShotsSaved", UNSET)
        )

        def _parse_goal_keeper_six_metre_right_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_right_goals_against = _parse_goal_keeper_six_metre_right_goals_against(
            d.pop("goalKeeperSixMetreRightGoalsAgainst", UNSET)
        )

        goal_keeper_six_metre_right_save_accuracy = d.pop("goalKeeperSixMetreRightSaveAccuracy", UNSET)

        def _parse_goal_keeper_six_metre_right_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_right_shots_against = _parse_goal_keeper_six_metre_right_shots_against(
            d.pop("goalKeeperSixMetreRightShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_six_metre_right_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_right_shots_saved = _parse_goal_keeper_six_metre_right_shots_saved(
            d.pop("goalKeeperSixMetreRightShotsSaved", UNSET)
        )

        goal_keeper_six_metre_save_accuracy = d.pop("goalKeeperSixMetreSaveAccuracy", UNSET)

        def _parse_goal_keeper_six_metre_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_shots_against = _parse_goal_keeper_six_metre_shots_against(
            d.pop("goalKeeperSixMetreShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_six_metre_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_shots_saved = _parse_goal_keeper_six_metre_shots_saved(
            d.pop("goalKeeperSixMetreShotsSaved", UNSET)
        )

        def _parse_goal_keeper_wing_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_goals_against = _parse_goal_keeper_wing_goals_against(
            d.pop("goalKeeperWingGoalsAgainst", UNSET)
        )

        def _parse_goal_keeper_wing_left_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_left_goals_against = _parse_goal_keeper_wing_left_goals_against(
            d.pop("goalKeeperWingLeftGoalsAgainst", UNSET)
        )

        goal_keeper_wing_left_save_accuracy = d.pop("goalKeeperWingLeftSaveAccuracy", UNSET)

        def _parse_goal_keeper_wing_left_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_left_shots_against = _parse_goal_keeper_wing_left_shots_against(
            d.pop("goalKeeperWingLeftShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_wing_left_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_left_shots_saved = _parse_goal_keeper_wing_left_shots_saved(
            d.pop("goalKeeperWingLeftShotsSaved", UNSET)
        )

        def _parse_goal_keeper_wing_right_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_right_goals_against = _parse_goal_keeper_wing_right_goals_against(
            d.pop("goalKeeperWingRightGoalsAgainst", UNSET)
        )

        goal_keeper_wing_right_save_accuracy = d.pop("goalKeeperWingRightSaveAccuracy", UNSET)

        def _parse_goal_keeper_wing_right_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_right_shots_against = _parse_goal_keeper_wing_right_shots_against(
            d.pop("goalKeeperWingRightShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_wing_right_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_right_shots_saved = _parse_goal_keeper_wing_right_shots_saved(
            d.pop("goalKeeperWingRightShotsSaved", UNSET)
        )

        goal_keeper_wing_save_accuracy = d.pop("goalKeeperWingSaveAccuracy", UNSET)

        def _parse_goal_keeper_wing_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_shots_against = _parse_goal_keeper_wing_shots_against(
            d.pop("goalKeeperWingShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_wing_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_shots_saved = _parse_goal_keeper_wing_shots_saved(d.pop("goalKeeperWingShotsSaved", UNSET))

        def _parse_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goals_scored = _parse_goals_scored(d.pop("goalsScored", UNSET))

        def _parse_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        missed_shots = _parse_missed_shots(d.pop("missedShots", UNSET))

        def _parse_nine_metre_centre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_goals_scored = _parse_nine_metre_centre_goals_scored(
            d.pop("nineMetreCentreGoalsScored", UNSET)
        )

        def _parse_nine_metre_centre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_missed_shots = _parse_nine_metre_centre_missed_shots(
            d.pop("nineMetreCentreMissedShots", UNSET)
        )

        def _parse_nine_metre_centre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_post_hits = _parse_nine_metre_centre_post_hits(d.pop("nineMetreCentrePostHits", UNSET))

        nine_metre_centre_shooting_accuracy = d.pop("nineMetreCentreShootingAccuracy", UNSET)

        def _parse_nine_metre_centre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_shots = _parse_nine_metre_centre_shots(d.pop("nineMetreCentreShots", UNSET))

        def _parse_nine_metre_centre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_shots_blocked = _parse_nine_metre_centre_shots_blocked(
            d.pop("nineMetreCentreShotsBlocked", UNSET)
        )

        def _parse_nine_metre_centre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_shots_on_goal = _parse_nine_metre_centre_shots_on_goal(
            d.pop("nineMetreCentreShotsOnGoal", UNSET)
        )

        def _parse_nine_metre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_goals_scored = _parse_nine_metre_goals_scored(d.pop("nineMetreGoalsScored", UNSET))

        def _parse_nine_metre_left_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_goals_scored = _parse_nine_metre_left_goals_scored(d.pop("nineMetreLeftGoalsScored", UNSET))

        def _parse_nine_metre_left_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_missed_shots = _parse_nine_metre_left_missed_shots(d.pop("nineMetreLeftMissedShots", UNSET))

        def _parse_nine_metre_left_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_post_hits = _parse_nine_metre_left_post_hits(d.pop("nineMetreLeftPostHits", UNSET))

        nine_metre_left_shooting_accuracy = d.pop("nineMetreLeftShootingAccuracy", UNSET)

        def _parse_nine_metre_left_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_shots = _parse_nine_metre_left_shots(d.pop("nineMetreLeftShots", UNSET))

        def _parse_nine_metre_left_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_shots_blocked = _parse_nine_metre_left_shots_blocked(d.pop("nineMetreLeftShotsBlocked", UNSET))

        def _parse_nine_metre_left_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_shots_on_goal = _parse_nine_metre_left_shots_on_goal(d.pop("nineMetreLeftShotsOnGoal", UNSET))

        def _parse_nine_metre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_missed_shots = _parse_nine_metre_missed_shots(d.pop("nineMetreMissedShots", UNSET))

        def _parse_nine_metre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_post_hits = _parse_nine_metre_post_hits(d.pop("nineMetrePostHits", UNSET))

        def _parse_nine_metre_right_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_goals_scored = _parse_nine_metre_right_goals_scored(d.pop("nineMetreRightGoalsScored", UNSET))

        def _parse_nine_metre_right_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_missed_shots = _parse_nine_metre_right_missed_shots(d.pop("nineMetreRightMissedShots", UNSET))

        def _parse_nine_metre_right_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_post_hits = _parse_nine_metre_right_post_hits(d.pop("nineMetreRightPostHits", UNSET))

        nine_metre_right_shooting_accuracy = d.pop("nineMetreRightShootingAccuracy", UNSET)

        def _parse_nine_metre_right_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_shots = _parse_nine_metre_right_shots(d.pop("nineMetreRightShots", UNSET))

        def _parse_nine_metre_right_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_shots_blocked = _parse_nine_metre_right_shots_blocked(
            d.pop("nineMetreRightShotsBlocked", UNSET)
        )

        def _parse_nine_metre_right_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_shots_on_goal = _parse_nine_metre_right_shots_on_goal(
            d.pop("nineMetreRightShotsOnGoal", UNSET)
        )

        nine_metre_shooting_accuracy = d.pop("nineMetreShootingAccuracy", UNSET)

        def _parse_nine_metre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_shots = _parse_nine_metre_shots(d.pop("nineMetreShots", UNSET))

        def _parse_nine_metre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_shots_blocked = _parse_nine_metre_shots_blocked(d.pop("nineMetreShotsBlocked", UNSET))

        def _parse_nine_metre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_shots_on_goal = _parse_nine_metre_shots_on_goal(d.pop("nineMetreShotsOnGoal", UNSET))

        def _parse_passive_play(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        passive_play = _parse_passive_play(d.pop("passivePlay", UNSET))

        def _parse_pivot_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_goals_scored = _parse_pivot_goals_scored(d.pop("pivotGoalsScored", UNSET))

        def _parse_pivot_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_missed_shots = _parse_pivot_missed_shots(d.pop("pivotMissedShots", UNSET))

        def _parse_pivot_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_post_hits = _parse_pivot_post_hits(d.pop("pivotPostHits", UNSET))

        pivot_shooting_accuracy = d.pop("pivotShootingAccuracy", UNSET)

        def _parse_pivot_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_shots = _parse_pivot_shots(d.pop("pivotShots", UNSET))

        def _parse_pivot_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_shots_blocked = _parse_pivot_shots_blocked(d.pop("pivotShotsBlocked", UNSET))

        def _parse_pivot_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_shots_on_goal = _parse_pivot_shots_on_goal(d.pop("pivotShotsOnGoal", UNSET))

        def _parse_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        post_hits = _parse_post_hits(d.pop("postHits", UNSET))

        def _parse_red_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        red_cards = _parse_red_cards(d.pop("redCards", UNSET))

        def _parse_seven_metre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_goals_scored = _parse_seven_metre_goals_scored(d.pop("sevenMetreGoalsScored", UNSET))

        def _parse_seven_metre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_missed_shots = _parse_seven_metre_missed_shots(d.pop("sevenMetreMissedShots", UNSET))

        def _parse_seven_metre_penalties_awarded(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_penalties_awarded = _parse_seven_metre_penalties_awarded(d.pop("sevenMetrePenaltiesAwarded", UNSET))

        def _parse_seven_metre_penalties_caused(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_penalties_caused = _parse_seven_metre_penalties_caused(d.pop("sevenMetrePenaltiesCaused", UNSET))

        def _parse_seven_metre_penalty_fouls(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_penalty_fouls = _parse_seven_metre_penalty_fouls(d.pop("sevenMetrePenaltyFouls", UNSET))

        def _parse_seven_metre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_post_hits = _parse_seven_metre_post_hits(d.pop("sevenMetrePostHits", UNSET))

        seven_metre_shooting_accuracy = d.pop("sevenMetreShootingAccuracy", UNSET)

        def _parse_seven_metre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_shots = _parse_seven_metre_shots(d.pop("sevenMetreShots", UNSET))

        def _parse_seven_metre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_shots_blocked = _parse_seven_metre_shots_blocked(d.pop("sevenMetreShotsBlocked", UNSET))

        def _parse_seven_metre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_shots_on_goal = _parse_seven_metre_shots_on_goal(d.pop("sevenMetreShotsOnGoal", UNSET))

        shooting_accuracy = d.pop("shootingAccuracy", UNSET)

        def _parse_shoot_out_attempts(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shoot_out_attempts = _parse_shoot_out_attempts(d.pop("shootOutAttempts", UNSET))

        def _parse_shoot_outs(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs = _parse_shoot_outs(d.pop("shootOuts", UNSET))

        def _parse_shoot_outs_made(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs_made = _parse_shoot_outs_made(d.pop("shootOutsMade", UNSET))

        def _parse_shoot_outs_missed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs_missed = _parse_shoot_outs_missed(d.pop("shootOutsMissed", UNSET))

        def _parse_shoot_outs_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs_saved = _parse_shoot_outs_saved(d.pop("shootOutsSaved", UNSET))

        def _parse_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots = _parse_shots(d.pop("shots", UNSET))

        def _parse_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots_blocked = _parse_shots_blocked(d.pop("shotsBlocked", UNSET))

        def _parse_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots_on_goal = _parse_shots_on_goal(d.pop("shotsOnGoal", UNSET))

        def _parse_shots_off_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots_off_goal = _parse_shots_off_goal(d.pop("shotsOffGoal", UNSET))

        def _parse_shots_saved_by_goal_keeper(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots_saved_by_goal_keeper = _parse_shots_saved_by_goal_keeper(d.pop("shotsSavedByGoalKeeper", UNSET))

        def _parse_six_metre_centre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_goals_scored = _parse_six_metre_centre_goals_scored(d.pop("sixMetreCentreGoalsScored", UNSET))

        def _parse_six_metre_centre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_missed_shots = _parse_six_metre_centre_missed_shots(d.pop("sixMetreCentreMissedShots", UNSET))

        def _parse_six_metre_centre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_post_hits = _parse_six_metre_centre_post_hits(d.pop("sixMetreCentrePostHits", UNSET))

        six_metre_centre_shooting_accuracy = d.pop("sixMetreCentreShootingAccuracy", UNSET)

        def _parse_six_metre_centre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_shots = _parse_six_metre_centre_shots(d.pop("sixMetreCentreShots", UNSET))

        def _parse_six_metre_centre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_shots_blocked = _parse_six_metre_centre_shots_blocked(
            d.pop("sixMetreCentreShotsBlocked", UNSET)
        )

        def _parse_six_metre_centre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_shots_on_goal = _parse_six_metre_centre_shots_on_goal(
            d.pop("sixMetreCentreShotsOnGoal", UNSET)
        )

        def _parse_six_metre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_goals_scored = _parse_six_metre_goals_scored(d.pop("sixMetreGoalsScored", UNSET))

        def _parse_six_metre_left_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_goals_scored = _parse_six_metre_left_goals_scored(d.pop("sixMetreLeftGoalsScored", UNSET))

        def _parse_six_metre_left_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_missed_shots = _parse_six_metre_left_missed_shots(d.pop("sixMetreLeftMissedShots", UNSET))

        def _parse_six_metre_left_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_post_hits = _parse_six_metre_left_post_hits(d.pop("sixMetreLeftPostHits", UNSET))

        six_metre_left_shooting_accuracy = d.pop("sixMetreLeftShootingAccuracy", UNSET)

        def _parse_six_metre_left_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_shots = _parse_six_metre_left_shots(d.pop("sixMetreLeftShots", UNSET))

        def _parse_six_metre_left_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_shots_blocked = _parse_six_metre_left_shots_blocked(d.pop("sixMetreLeftShotsBlocked", UNSET))

        def _parse_six_metre_left_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_shots_on_goal = _parse_six_metre_left_shots_on_goal(d.pop("sixMetreLeftShotsOnGoal", UNSET))

        def _parse_six_metre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_missed_shots = _parse_six_metre_missed_shots(d.pop("sixMetreMissedShots", UNSET))

        def _parse_six_metre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_post_hits = _parse_six_metre_post_hits(d.pop("sixMetrePostHits", UNSET))

        def _parse_six_metre_right_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_goals_scored = _parse_six_metre_right_goals_scored(d.pop("sixMetreRightGoalsScored", UNSET))

        def _parse_six_metre_right_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_missed_shots = _parse_six_metre_right_missed_shots(d.pop("sixMetreRightMissedShots", UNSET))

        def _parse_six_metre_right_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_post_hits = _parse_six_metre_right_post_hits(d.pop("sixMetreRightPostHits", UNSET))

        six_metre_right_shooting_accuracy = d.pop("sixMetreRightShootingAccuracy", UNSET)

        def _parse_six_metre_right_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_shots = _parse_six_metre_right_shots(d.pop("sixMetreRightShots", UNSET))

        def _parse_six_metre_right_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_shots_blocked = _parse_six_metre_right_shots_blocked(d.pop("sixMetreRightShotsBlocked", UNSET))

        def _parse_six_metre_right_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_shots_on_goal = _parse_six_metre_right_shots_on_goal(d.pop("sixMetreRightShotsOnGoal", UNSET))

        six_metre_shooting_accuracy = d.pop("sixMetreShootingAccuracy", UNSET)

        def _parse_six_metre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_shots = _parse_six_metre_shots(d.pop("sixMetreShots", UNSET))

        def _parse_six_metre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_shots_blocked = _parse_six_metre_shots_blocked(d.pop("sixMetreShotsBlocked", UNSET))

        def _parse_six_metre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_shots_on_goal = _parse_six_metre_shots_on_goal(d.pop("sixMetreShotsOnGoal", UNSET))

        def _parse_steals(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        steals = _parse_steals(d.pop("steals", UNSET))

        def _parse_substitutions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        substitutions = _parse_substitutions(d.pop("substitutions", UNSET))

        def _parse_suspensions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        suspensions = _parse_suspensions(d.pop("suspensions", UNSET))

        def _parse_technical_ball_faults(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        technical_ball_faults = _parse_technical_ball_faults(d.pop("technicalBallFaults", UNSET))

        def _parse_technical_faults(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        technical_faults = _parse_technical_faults(d.pop("technicalFaults", UNSET))

        def _parse_technical_rule_faults(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        technical_rule_faults = _parse_technical_rule_faults(d.pop("technicalRuleFaults", UNSET))

        def _parse_time_played(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        time_played = _parse_time_played(d.pop("timePlayed", UNSET))

        def _parse_turnovers(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        turnovers = _parse_turnovers(d.pop("turnovers", UNSET))

        def _parse_two_minute_suspensions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        two_minute_suspensions = _parse_two_minute_suspensions(d.pop("twoMinuteSuspensions", UNSET))

        def _parse_wing_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_goals_scored = _parse_wing_goals_scored(d.pop("wingGoalsScored", UNSET))

        def _parse_wing_left_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_goals_scored = _parse_wing_left_goals_scored(d.pop("wingLeftGoalsScored", UNSET))

        def _parse_wing_left_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_missed_shots = _parse_wing_left_missed_shots(d.pop("wingLeftMissedShots", UNSET))

        def _parse_wing_left_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_post_hits = _parse_wing_left_post_hits(d.pop("wingLeftPostHits", UNSET))

        wing_left_shooting_accuracy = d.pop("wingLeftShootingAccuracy", UNSET)

        def _parse_wing_left_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_shots = _parse_wing_left_shots(d.pop("wingLeftShots", UNSET))

        def _parse_wing_left_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_shots_blocked = _parse_wing_left_shots_blocked(d.pop("wingLeftShotsBlocked", UNSET))

        def _parse_wing_left_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_shots_on_goal = _parse_wing_left_shots_on_goal(d.pop("wingLeftShotsOnGoal", UNSET))

        def _parse_wing_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_missed_shots = _parse_wing_missed_shots(d.pop("wingMissedShots", UNSET))

        def _parse_wing_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_post_hits = _parse_wing_post_hits(d.pop("wingPostHits", UNSET))

        def _parse_wing_right_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_goals_scored = _parse_wing_right_goals_scored(d.pop("wingRightGoalsScored", UNSET))

        def _parse_wing_right_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_missed_shots = _parse_wing_right_missed_shots(d.pop("wingRightMissedShots", UNSET))

        def _parse_wing_right_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_post_hits = _parse_wing_right_post_hits(d.pop("wingRightPostHits", UNSET))

        wing_right_shooting_accuracy = d.pop("wingRightShootingAccuracy", UNSET)

        def _parse_wing_right_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_shots = _parse_wing_right_shots(d.pop("wingRightShots", UNSET))

        def _parse_wing_right_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_shots_blocked = _parse_wing_right_shots_blocked(d.pop("wingRightShotsBlocked", UNSET))

        def _parse_wing_right_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_shots_on_goal = _parse_wing_right_shots_on_goal(d.pop("wingRightShotsOnGoal", UNSET))

        wing_shooting_accuracy = d.pop("wingShootingAccuracy", UNSET)

        def _parse_wing_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_shots = _parse_wing_shots(d.pop("wingShots", UNSET))

        def _parse_wing_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_shots_blocked = _parse_wing_shots_blocked(d.pop("wingShotsBlocked", UNSET))

        def _parse_wing_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_shots_on_goal = _parse_wing_shots_on_goal(d.pop("wingShotsOnGoal", UNSET))

        def _parse_yellow_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        yellow_cards = _parse_yellow_cards(d.pop("yellowCards", UNSET))

        game_log_entity_model_statistics = cls(
            assists=assists,
            back_court_goals_scored=back_court_goals_scored,
            back_court_missed_shots=back_court_missed_shots,
            back_court_post_hits=back_court_post_hits,
            back_court_shooting_accuracy=back_court_shooting_accuracy,
            back_court_shots=back_court_shots,
            back_court_shots_blocked=back_court_shots_blocked,
            back_court_shots_on_goal=back_court_shots_on_goal,
            blocks=blocks,
            blue_cards=blue_cards,
            break_through_goals_scored=break_through_goals_scored,
            break_through_missed_shots=break_through_missed_shots,
            break_through_post_hits=break_through_post_hits,
            break_through_shooting_accuracy=break_through_shooting_accuracy,
            break_through_shots=break_through_shots,
            break_through_shots_blocked=break_through_shots_blocked,
            break_through_shots_on_goal=break_through_shots_on_goal,
            cards=cards,
            empty_net_goals_scored=empty_net_goals_scored,
            fast_break_goals_scored=fast_break_goals_scored,
            fast_break_missed_shots=fast_break_missed_shots,
            fast_break_post_hits=fast_break_post_hits,
            fast_break_shooting_accuracy=fast_break_shooting_accuracy,
            fast_break_shots=fast_break_shots,
            fast_break_shots_blocked=fast_break_shots_blocked,
            fast_break_shots_on_goal=fast_break_shots_on_goal,
            field_goals_scored=field_goals_scored,
            field_missed_shots=field_missed_shots,
            field_post_hits=field_post_hits,
            field_shooting_accuracy=field_shooting_accuracy,
            field_shots=field_shots,
            field_shots_blocked=field_shots_blocked,
            field_shots_on_goal=field_shots_on_goal,
            fouls=fouls,
            fouls_drawn=fouls_drawn,
            four_minute_suspensions=four_minute_suspensions,
            goal_keeper_back_court_goals_against=goal_keeper_back_court_goals_against,
            goal_keeper_back_court_save_accuracy=goal_keeper_back_court_save_accuracy,
            goal_keeper_back_court_shots_against=goal_keeper_back_court_shots_against,
            goal_keeper_back_court_shots_saved=goal_keeper_back_court_shots_saved,
            goal_keeper_break_through_goals_against=goal_keeper_break_through_goals_against,
            goal_keeper_break_through_save_accuracy=goal_keeper_break_through_save_accuracy,
            goal_keeper_break_through_shots_against=goal_keeper_break_through_shots_against,
            goal_keeper_break_through_shots_saved=goal_keeper_break_through_shots_saved,
            goal_keeper_fast_break_goals_against=goal_keeper_fast_break_goals_against,
            goal_keeper_fast_break_save_accuracy=goal_keeper_fast_break_save_accuracy,
            goal_keeper_fast_break_shots_against=goal_keeper_fast_break_shots_against,
            goal_keeper_fast_break_shots_saved=goal_keeper_fast_break_shots_saved,
            goal_keeper_field_goals_against=goal_keeper_field_goals_against,
            goal_keeper_field_save_accuracy=goal_keeper_field_save_accuracy,
            goal_keeper_field_shots_against=goal_keeper_field_shots_against,
            goal_keeper_field_shots_saved=goal_keeper_field_shots_saved,
            goal_keeper_goals_against=goal_keeper_goals_against,
            goal_keeper_nine_metre_centre_goals_against=goal_keeper_nine_metre_centre_goals_against,
            goal_keeper_nine_metre_centre_save_accuracy=goal_keeper_nine_metre_centre_save_accuracy,
            goal_keeper_nine_metre_centre_shots_against=goal_keeper_nine_metre_centre_shots_against,
            goal_keeper_nine_metre_centre_shots_saved=goal_keeper_nine_metre_centre_shots_saved,
            goal_keeper_nine_metre_goals_against=goal_keeper_nine_metre_goals_against,
            goal_keeper_nine_metre_left_goals_against=goal_keeper_nine_metre_left_goals_against,
            goal_keeper_nine_metre_left_save_accuracy=goal_keeper_nine_metre_left_save_accuracy,
            goal_keeper_nine_metre_left_shots_against=goal_keeper_nine_metre_left_shots_against,
            goal_keeper_nine_metre_left_shots_saved=goal_keeper_nine_metre_left_shots_saved,
            goal_keeper_nine_metre_right_goals_against=goal_keeper_nine_metre_right_goals_against,
            goal_keeper_nine_metre_right_save_accuracy=goal_keeper_nine_metre_right_save_accuracy,
            goal_keeper_nine_metre_right_shots_against=goal_keeper_nine_metre_right_shots_against,
            goal_keeper_nine_metre_right_shots_saved=goal_keeper_nine_metre_right_shots_saved,
            goal_keeper_nine_metre_save_accuracy=goal_keeper_nine_metre_save_accuracy,
            goal_keeper_nine_metre_shots_against=goal_keeper_nine_metre_shots_against,
            goal_keeper_nine_metre_shots_saved=goal_keeper_nine_metre_shots_saved,
            goal_keeper_pivot_goals_against=goal_keeper_pivot_goals_against,
            goal_keeper_pivot_save_accuracy=goal_keeper_pivot_save_accuracy,
            goal_keeper_pivot_shots_against=goal_keeper_pivot_shots_against,
            goal_keeper_pivot_shots_saved=goal_keeper_pivot_shots_saved,
            goal_keeper_save_accuracy=goal_keeper_save_accuracy,
            goal_keeper_seconds_played=goal_keeper_seconds_played,
            goal_keeper_seven_metre_goals_against=goal_keeper_seven_metre_goals_against,
            goal_keeper_seven_metre_save_accuracy=goal_keeper_seven_metre_save_accuracy,
            goal_keeper_seven_metre_shots_against=goal_keeper_seven_metre_shots_against,
            goal_keeper_seven_metre_shots_saved=goal_keeper_seven_metre_shots_saved,
            goal_keeper_shots_against=goal_keeper_shots_against,
            goal_keeper_shots_saved=goal_keeper_shots_saved,
            goal_keeper_six_metre_centre_goals_against=goal_keeper_six_metre_centre_goals_against,
            goal_keeper_six_metre_centre_save_accuracy=goal_keeper_six_metre_centre_save_accuracy,
            goal_keeper_six_metre_centre_shots_against=goal_keeper_six_metre_centre_shots_against,
            goal_keeper_six_metre_centre_shots_saved=goal_keeper_six_metre_centre_shots_saved,
            goal_keeper_six_metre_goals_against=goal_keeper_six_metre_goals_against,
            goal_keeper_six_metre_left_goals_against=goal_keeper_six_metre_left_goals_against,
            goal_keeper_six_metre_left_save_accuracy=goal_keeper_six_metre_left_save_accuracy,
            goal_keeper_six_metre_left_shots_against=goal_keeper_six_metre_left_shots_against,
            goal_keeper_six_metre_left_shots_saved=goal_keeper_six_metre_left_shots_saved,
            goal_keeper_six_metre_right_goals_against=goal_keeper_six_metre_right_goals_against,
            goal_keeper_six_metre_right_save_accuracy=goal_keeper_six_metre_right_save_accuracy,
            goal_keeper_six_metre_right_shots_against=goal_keeper_six_metre_right_shots_against,
            goal_keeper_six_metre_right_shots_saved=goal_keeper_six_metre_right_shots_saved,
            goal_keeper_six_metre_save_accuracy=goal_keeper_six_metre_save_accuracy,
            goal_keeper_six_metre_shots_against=goal_keeper_six_metre_shots_against,
            goal_keeper_six_metre_shots_saved=goal_keeper_six_metre_shots_saved,
            goal_keeper_wing_goals_against=goal_keeper_wing_goals_against,
            goal_keeper_wing_left_goals_against=goal_keeper_wing_left_goals_against,
            goal_keeper_wing_left_save_accuracy=goal_keeper_wing_left_save_accuracy,
            goal_keeper_wing_left_shots_against=goal_keeper_wing_left_shots_against,
            goal_keeper_wing_left_shots_saved=goal_keeper_wing_left_shots_saved,
            goal_keeper_wing_right_goals_against=goal_keeper_wing_right_goals_against,
            goal_keeper_wing_right_save_accuracy=goal_keeper_wing_right_save_accuracy,
            goal_keeper_wing_right_shots_against=goal_keeper_wing_right_shots_against,
            goal_keeper_wing_right_shots_saved=goal_keeper_wing_right_shots_saved,
            goal_keeper_wing_save_accuracy=goal_keeper_wing_save_accuracy,
            goal_keeper_wing_shots_against=goal_keeper_wing_shots_against,
            goal_keeper_wing_shots_saved=goal_keeper_wing_shots_saved,
            goals_scored=goals_scored,
            missed_shots=missed_shots,
            nine_metre_centre_goals_scored=nine_metre_centre_goals_scored,
            nine_metre_centre_missed_shots=nine_metre_centre_missed_shots,
            nine_metre_centre_post_hits=nine_metre_centre_post_hits,
            nine_metre_centre_shooting_accuracy=nine_metre_centre_shooting_accuracy,
            nine_metre_centre_shots=nine_metre_centre_shots,
            nine_metre_centre_shots_blocked=nine_metre_centre_shots_blocked,
            nine_metre_centre_shots_on_goal=nine_metre_centre_shots_on_goal,
            nine_metre_goals_scored=nine_metre_goals_scored,
            nine_metre_left_goals_scored=nine_metre_left_goals_scored,
            nine_metre_left_missed_shots=nine_metre_left_missed_shots,
            nine_metre_left_post_hits=nine_metre_left_post_hits,
            nine_metre_left_shooting_accuracy=nine_metre_left_shooting_accuracy,
            nine_metre_left_shots=nine_metre_left_shots,
            nine_metre_left_shots_blocked=nine_metre_left_shots_blocked,
            nine_metre_left_shots_on_goal=nine_metre_left_shots_on_goal,
            nine_metre_missed_shots=nine_metre_missed_shots,
            nine_metre_post_hits=nine_metre_post_hits,
            nine_metre_right_goals_scored=nine_metre_right_goals_scored,
            nine_metre_right_missed_shots=nine_metre_right_missed_shots,
            nine_metre_right_post_hits=nine_metre_right_post_hits,
            nine_metre_right_shooting_accuracy=nine_metre_right_shooting_accuracy,
            nine_metre_right_shots=nine_metre_right_shots,
            nine_metre_right_shots_blocked=nine_metre_right_shots_blocked,
            nine_metre_right_shots_on_goal=nine_metre_right_shots_on_goal,
            nine_metre_shooting_accuracy=nine_metre_shooting_accuracy,
            nine_metre_shots=nine_metre_shots,
            nine_metre_shots_blocked=nine_metre_shots_blocked,
            nine_metre_shots_on_goal=nine_metre_shots_on_goal,
            passive_play=passive_play,
            pivot_goals_scored=pivot_goals_scored,
            pivot_missed_shots=pivot_missed_shots,
            pivot_post_hits=pivot_post_hits,
            pivot_shooting_accuracy=pivot_shooting_accuracy,
            pivot_shots=pivot_shots,
            pivot_shots_blocked=pivot_shots_blocked,
            pivot_shots_on_goal=pivot_shots_on_goal,
            post_hits=post_hits,
            red_cards=red_cards,
            seven_metre_goals_scored=seven_metre_goals_scored,
            seven_metre_missed_shots=seven_metre_missed_shots,
            seven_metre_penalties_awarded=seven_metre_penalties_awarded,
            seven_metre_penalties_caused=seven_metre_penalties_caused,
            seven_metre_penalty_fouls=seven_metre_penalty_fouls,
            seven_metre_post_hits=seven_metre_post_hits,
            seven_metre_shooting_accuracy=seven_metre_shooting_accuracy,
            seven_metre_shots=seven_metre_shots,
            seven_metre_shots_blocked=seven_metre_shots_blocked,
            seven_metre_shots_on_goal=seven_metre_shots_on_goal,
            shooting_accuracy=shooting_accuracy,
            shoot_out_attempts=shoot_out_attempts,
            shoot_outs=shoot_outs,
            shoot_outs_made=shoot_outs_made,
            shoot_outs_missed=shoot_outs_missed,
            shoot_outs_saved=shoot_outs_saved,
            shots=shots,
            shots_blocked=shots_blocked,
            shots_on_goal=shots_on_goal,
            shots_off_goal=shots_off_goal,
            shots_saved_by_goal_keeper=shots_saved_by_goal_keeper,
            six_metre_centre_goals_scored=six_metre_centre_goals_scored,
            six_metre_centre_missed_shots=six_metre_centre_missed_shots,
            six_metre_centre_post_hits=six_metre_centre_post_hits,
            six_metre_centre_shooting_accuracy=six_metre_centre_shooting_accuracy,
            six_metre_centre_shots=six_metre_centre_shots,
            six_metre_centre_shots_blocked=six_metre_centre_shots_blocked,
            six_metre_centre_shots_on_goal=six_metre_centre_shots_on_goal,
            six_metre_goals_scored=six_metre_goals_scored,
            six_metre_left_goals_scored=six_metre_left_goals_scored,
            six_metre_left_missed_shots=six_metre_left_missed_shots,
            six_metre_left_post_hits=six_metre_left_post_hits,
            six_metre_left_shooting_accuracy=six_metre_left_shooting_accuracy,
            six_metre_left_shots=six_metre_left_shots,
            six_metre_left_shots_blocked=six_metre_left_shots_blocked,
            six_metre_left_shots_on_goal=six_metre_left_shots_on_goal,
            six_metre_missed_shots=six_metre_missed_shots,
            six_metre_post_hits=six_metre_post_hits,
            six_metre_right_goals_scored=six_metre_right_goals_scored,
            six_metre_right_missed_shots=six_metre_right_missed_shots,
            six_metre_right_post_hits=six_metre_right_post_hits,
            six_metre_right_shooting_accuracy=six_metre_right_shooting_accuracy,
            six_metre_right_shots=six_metre_right_shots,
            six_metre_right_shots_blocked=six_metre_right_shots_blocked,
            six_metre_right_shots_on_goal=six_metre_right_shots_on_goal,
            six_metre_shooting_accuracy=six_metre_shooting_accuracy,
            six_metre_shots=six_metre_shots,
            six_metre_shots_blocked=six_metre_shots_blocked,
            six_metre_shots_on_goal=six_metre_shots_on_goal,
            steals=steals,
            substitutions=substitutions,
            suspensions=suspensions,
            technical_ball_faults=technical_ball_faults,
            technical_faults=technical_faults,
            technical_rule_faults=technical_rule_faults,
            time_played=time_played,
            turnovers=turnovers,
            two_minute_suspensions=two_minute_suspensions,
            wing_goals_scored=wing_goals_scored,
            wing_left_goals_scored=wing_left_goals_scored,
            wing_left_missed_shots=wing_left_missed_shots,
            wing_left_post_hits=wing_left_post_hits,
            wing_left_shooting_accuracy=wing_left_shooting_accuracy,
            wing_left_shots=wing_left_shots,
            wing_left_shots_blocked=wing_left_shots_blocked,
            wing_left_shots_on_goal=wing_left_shots_on_goal,
            wing_missed_shots=wing_missed_shots,
            wing_post_hits=wing_post_hits,
            wing_right_goals_scored=wing_right_goals_scored,
            wing_right_missed_shots=wing_right_missed_shots,
            wing_right_post_hits=wing_right_post_hits,
            wing_right_shooting_accuracy=wing_right_shooting_accuracy,
            wing_right_shots=wing_right_shots,
            wing_right_shots_blocked=wing_right_shots_blocked,
            wing_right_shots_on_goal=wing_right_shots_on_goal,
            wing_shooting_accuracy=wing_shooting_accuracy,
            wing_shots=wing_shots,
            wing_shots_blocked=wing_shots_blocked,
            wing_shots_on_goal=wing_shots_on_goal,
            yellow_cards=yellow_cards,
        )

        return game_log_entity_model_statistics
