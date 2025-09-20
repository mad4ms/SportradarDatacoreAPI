from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonPersonStatisticsModelStatistics")


@_attrs_define
class SeasonPersonStatisticsModelStatistics:
    """
    Attributes:
        airtime_max (Union[None, Unset, float, str]): Time in minutes (in ISO8601 Duration format) a player was in the
            air (due to jumping)
        assists (Union[None, Unset, int]): Total number of assists
        assists_per_match (Union[None, Unset, float]): Average number of assists per match
        back_court_goals_scored (Union[None, Unset, int]): Total number of goals scored from a back court position
        back_court_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from a back court
            position per match
        back_court_missed_shots (Union[None, Unset, int]): Total number of missed shots from a back court position
        back_court_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from a back court
            position per match
        back_court_post_hits (Union[None, Unset, int]): Total number of post hits from a back court position
        back_court_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from a back court
            position per match
        back_court_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the back court position
        back_court_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the back
            court position per match
        back_court_shots (Union[None, Unset, int]): Total number of back court shots attempted
        back_court_shots_per_match (Union[None, Unset, float]): Average number of back court shots attempted per match
        back_court_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from a back court position
        back_court_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from a back
            court position per match
        back_court_shots_on_goal (Union[None, Unset, int]): Total number of back court shots on goal
        back_court_shots_on_goal_per_match (Union[None, Unset, float]): Average number of back court shots on goal per
            match
        blocks (Union[None, Unset, int]): Total number of blocks
        blocks_per_match (Union[None, Unset, float]): Average number of blocks per match
        blue_cards (Union[None, Unset, int]): Total number of blue cards
        blue_cards_per_match (Union[None, Unset, float]): Average number of blue cards per match
        break_through_goals_scored (Union[None, Unset, int]): Total number of goals scored from a break through attack
        break_through_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from a break
            through attack per match
        break_through_missed_shots (Union[None, Unset, int]): Total number of missed shots from a break through attack
        break_through_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from a break
            through attack per match
        break_through_post_hits (Union[None, Unset, int]): Total number of post hits from a break through attack
        break_through_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from a break through
            attack per match
        break_through_shooting_accuracy (Union[Unset, float]): Shot rate shots on goal from a break through attack
        break_through_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate shots on goal from a break
            through attack per match
        break_through_shots (Union[None, Unset, int]): Total number of break through shots attempted
        break_through_shots_per_match (Union[None, Unset, float]): Average number of break through shots attempted per
            match
        break_through_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from a break through attack
        break_through_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from a break
            through attack per match
        break_through_shots_on_goal (Union[None, Unset, int]): Total number of break through shots on goal
        break_through_shots_on_goal_per_match (Union[None, Unset, float]): Average number of break through shots on goal
            per match
        cards (Union[None, Unset, int]): Total number of cards
        cards_per_match (Union[None, Unset, float]): Average number of cards per match
        distance_speed_category_1 (Union[None, Unset, int]): Distance distribution [m] of the player in the very low
            speed zone (<4 km/h)
        distance_speed_category_2 (Union[None, Unset, int]): Distance distribution [m] of the player in the low speed
            zone (4-10 km/h)
        distance_speed_category_3 (Union[None, Unset, int]): Distance distribution [m] of the player in the medium speed
            zone (10-16 km/h)
        distance_speed_category_4 (Union[None, Unset, int]): Distance distribution [m] of the player in the high speed
            zone (16-22 km/h)
        distance_speed_category_5 (Union[None, Unset, int]): Distance distribution [m] of the player in the very high
            speed zone (>22 km/h)
        distance_total (Union[None, Unset, float]): Total distance [m] covered by the player
        draws (Union[None, Unset, int]): The number of draws
        empty_net_goals_scored (Union[None, Unset, int]): Total number of goals scored in an empty net
        fast_break_goals_scored (Union[None, Unset, int]): Total number of goals scored from a fast break attack
        fast_break_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from a fast break
            attack per match
        fast_break_missed_shots (Union[None, Unset, int]): Total number of missed shots from a fast break attack
        fast_break_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from a fast break
            attack per match
        fast_break_post_hits (Union[None, Unset, int]): Total number of post hits from a fast break attack
        fast_break_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from a fast break attack
            per match
        fast_break_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from a fast break attack
        fast_break_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from a fast break
            attack per match
        fast_break_shots (Union[None, Unset, int]): Total number of fast break shots attempted
        fast_break_shots_per_match (Union[None, Unset, float]): Average number of fast break shots attempted per match
        fast_break_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from a fast break attack
        fast_break_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from a fast
            break attack per match
        fast_break_shots_on_goal (Union[None, Unset, int]): Total number of fast break shots on goal
        fast_break_shots_on_goal_per_match (Union[None, Unset, float]): Average number of fast break shots on goal per
            match
        field_goals_scored (Union[None, Unset, int]): Total number of goals scored from the field
        field_goals_scored_per_match (Union[None, Unset, float]): Average number of field goals scored per match
        field_missed_shots (Union[None, Unset, int]): Total number of missed shots from the field
        field_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the field per
            match
        field_post_hits (Union[None, Unset, int]): Total number of post hits from the field
        field_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the field per match
        field_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the field
        field_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the field per
            match
        field_shots (Union[None, Unset, int]): Total number of field shots attempted
        field_shots_per_match (Union[None, Unset, float]): Average number of field shots attempted per match
        field_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the field
        field_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the field per
            match
        field_shots_on_goal (Union[None, Unset, int]): Total number of field shots on goal
        field_shots_on_goal_per_match (Union[None, Unset, float]): Average number of field shots on goal per match
        fouls (Union[None, Unset, int]): Total number of fouls committed
        fouls_per_match (Union[None, Unset, float]): Average number of fouls committed per match
        fouls_drawn (Union[None, Unset, int]): Total number of fouls drawn
        fouls_drawn_per_match (Union[None, Unset, float]): Average number of fouls drawn per match
        four_minute_suspensions (Union[None, Unset, int]): Total number of four minute suspensions
        four_minute_suspensions_per_match (Union[None, Unset, float]): Average number of four minute suspensions per
            match
        games (Union[None, Unset, int]): The number of matches that they have participated in
        games_started (Union[None, Unset, int]): The number of matches that they were a starter
        goal_keeper_back_court_goals_against (Union[None, Unset, int]): Total number of back court goals conceded by the
            goalkeeper
        goal_keeper_back_court_goals_against_per_match (Union[None, Unset, float]): Average number of back court goals
            conceded by the goalkeeper per match
        goal_keeper_back_court_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the back
            court position
        goal_keeper_back_court_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the back court position per match
        goal_keeper_back_court_shots_against (Union[None, Unset, int]): Total number of back court shots on goal against
            the goalkeeper
        goal_keeper_back_court_shots_against_per_match (Union[None, Unset, float]): Average number of back court shots
            on goal against the goalkeeper per match
        goal_keeper_back_court_shots_saved (Union[None, Unset, int]): Total number of back court shots saved by the
            goalkeeper
        goal_keeper_back_court_shots_saved_per_match (Union[None, Unset, float]): Average number of back court shots
            saved by the goalkeeper per match
        goal_keeper_break_through_goals_against (Union[None, Unset, int]): Total number of break through goals conceded
            by the goalkeeper
        goal_keeper_break_through_goals_against_per_match (Union[None, Unset, float]): Average number of break through
            goals conceded by the goalkeeper per match
        goal_keeper_break_through_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from a
            break through attack
        goal_keeper_break_through_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from a break through attack per match
        goal_keeper_break_through_shots_against (Union[None, Unset, int]): Total number of break through shots on goal
            against the goalkeeper
        goal_keeper_break_through_shots_against_per_match (Union[None, Unset, float]): Average number of break through
            shots on goal against the goalkeeper per match
        goal_keeper_break_through_shots_saved (Union[None, Unset, int]): Total number of break through shots saved by
            the goalkeeper
        goal_keeper_break_through_shots_saved_per_match (Union[None, Unset, float]): Average number of break through
            shots saved by the goalkeeper per match
        goal_keeper_fast_break_goals_against (Union[None, Unset, int]): Total number of fast break goals conceded by the
            goalkeeper
        goal_keeper_fast_break_goals_against_per_match (Union[None, Unset, float]): Average number of fast break goals
            conceded by the goalkeeper per match
        goal_keeper_fast_break_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from a fast
            break attack
        goal_keeper_fast_break_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from a fast break attack per match
        goal_keeper_fast_break_shots_against (Union[None, Unset, int]): Total number of fast break shots on goal against
            the goalkeeper
        goal_keeper_fast_break_shots_against_per_match (Union[None, Unset, float]): Average number of fast break shots
            on goal against the goalkeeper per match
        goal_keeper_fast_break_shots_saved (Union[None, Unset, int]): Total number of fast break shots saved by the
            goalkeeper
        goal_keeper_fast_break_shots_saved_per_match (Union[None, Unset, float]): Average number of fast break shots
            saved by the goalkeeper per match
        goal_keeper_field_goals_against (Union[None, Unset, int]): Total number of field goals conceded by the
            goalkeeper
        goal_keeper_field_goals_against_per_match (Union[None, Unset, float]): Average number of field goals conceded by
            the goalkeeper per match
        goal_keeper_field_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper when shooting from
            the field
        goal_keeper_field_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the goalkeeper
            when shooting from the field
        goal_keeper_field_shots_against (Union[None, Unset, int]): Total number of field shots on goal against the
            goalkeeper
        goal_keeper_field_shots_against_per_match (Union[None, Unset, float]): Average number of field shots on goal
            against the goalkeeper per match
        goal_keeper_field_shots_saved (Union[None, Unset, int]): Total number of field shots saved by the goalkeeper
        goal_keeper_field_shots_saved_per_match (Union[None, Unset, float]): Average number of field shots saved by the
            goalkeeper per match
        goal_keeper_goals_against (Union[None, Unset, int]): Total number of goals conceded by the goalkeeper
        goal_keeper_goals_against_per_match (Union[None, Unset, float]): Average number of goals conceded by the
            goalkeeper per match
        goal_keeper_nine_metre_centre_goals_against (Union[None, Unset, int]): Total number of nine metre centre goals
            conceded by the goalkeeper
        goal_keeper_nine_metre_centre_goals_against_per_match (Union[None, Unset, float]): Average number of nine metre
            centre goals conceded by the goalkeeper per match
        goal_keeper_nine_metre_centre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from
            the nine metre centre position
        goal_keeper_nine_metre_centre_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the nine metre centre position per match
        goal_keeper_nine_metre_centre_shots_against (Union[None, Unset, int]): Total number of nine metre centre shots
            on goal against the goalkeeper
        goal_keeper_nine_metre_centre_shots_against_per_match (Union[None, Unset, float]): Average number of nine metre
            centre shots on goal against the goalkeeper per match
        goal_keeper_nine_metre_centre_shots_saved (Union[None, Unset, int]): Total number of nine metre centre shots
            saved by the goalkeeper
        goal_keeper_nine_metre_centre_shots_saved_per_match (Union[None, Unset, float]): Average number of nine metre
            centre shots saved by the goalkeeper per match
        goal_keeper_nine_metre_goals_against (Union[None, Unset, int]): Total number of nine metre goals conceded by the
            goalkeeper
        goal_keeper_nine_metre_goals_against_per_match (Union[None, Unset, float]): Average number of nine metre goals
            conceded by the goalkeeper per match
        goal_keeper_nine_metre_left_goals_against (Union[None, Unset, int]): Total number of nine metre left goals
            conceded by the goalkeeper
        goal_keeper_nine_metre_left_goals_against_per_match (Union[None, Unset, float]): Average number of nine metre
            left goals conceded by the goalkeeper per match
        goal_keeper_nine_metre_left_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            nine metre left position
        goal_keeper_nine_metre_left_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the nine metre left position per match
        goal_keeper_nine_metre_left_shots_against (Union[None, Unset, int]): Total number of nine metre left shots on
            goal against the goalkeeper
        goal_keeper_nine_metre_left_shots_against_per_match (Union[None, Unset, float]): Average number of nine metre
            left shots on goal against the goalkeeper per match
        goal_keeper_nine_metre_left_shots_saved (Union[None, Unset, int]): Total number of nine metre left shots saved
            by the goalkeeper
        goal_keeper_nine_metre_left_shots_saved_per_match (Union[None, Unset, float]): Average number of nine metre left
            shots saved by the goalkeeper per match
        goal_keeper_nine_metre_right_goals_against (Union[None, Unset, int]): Total number of nine metre right goals
            conceded by the goalkeeper
        goal_keeper_nine_metre_right_goals_against_per_match (Union[None, Unset, float]): Average number of nine metre
            right goals conceded by the goalkeeper per match
        goal_keeper_nine_metre_right_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            nine metre right position
        goal_keeper_nine_metre_right_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the nine metre right position per match
        goal_keeper_nine_metre_right_shots_against (Union[None, Unset, int]): Total number of nine metre right shots on
            goal against the goalkeeper
        goal_keeper_nine_metre_right_shots_against_per_match (Union[None, Unset, float]): Average number of nine metre
            right shots on goal against the goalkeeper per match
        goal_keeper_nine_metre_right_shots_saved (Union[None, Unset, int]): Total number of nine metre right shots saved
            by the goalkeeper
        goal_keeper_nine_metre_right_shots_saved_per_match (Union[None, Unset, float]): Average number of nine metre
            right shots saved by the goalkeeper per match
        goal_keeper_nine_metre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the nine
            metre position
        goal_keeper_nine_metre_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the nine metre position per match
        goal_keeper_nine_metre_shots_against (Union[None, Unset, int]): Total number of nine metre shots on goal against
            the goalkeeper
        goal_keeper_nine_metre_shots_against_per_match (Union[None, Unset, float]): Average number of nine metre shots
            on goal against the goalkeeper per match
        goal_keeper_nine_metre_shots_saved (Union[None, Unset, int]): Total number of nine metre shots saved by the
            goalkeeper
        goal_keeper_nine_metre_shots_saved_per_match (Union[None, Unset, float]): Average number of nine metre shots
            saved by the goalkeeper per match
        goal_keeper_pivot_goals_against (Union[None, Unset, int]): Total number of pivot goals conceded by the
            goalkeeper
        goal_keeper_pivot_goals_against_per_match (Union[None, Unset, float]): Average number of pivot goals conceded by
            the goalkeeper per match
        goal_keeper_pivot_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the pivot
            position
        goal_keeper_pivot_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the goalkeeper
            from the pivot position per match
        goal_keeper_pivot_shots_against (Union[None, Unset, int]): Total number of pivot shots on goal against the
            goalkeeper
        goal_keeper_pivot_shots_against_per_match (Union[None, Unset, float]): Average number of pivot shots on goal
            against the goalkeeper per match
        goal_keeper_pivot_shots_saved (Union[None, Unset, int]): Total number of pivot shots saved by the goalkeeper
        goal_keeper_pivot_shots_saved_per_match (Union[None, Unset, float]): Average number of pivot shots saved by the
            goalkeeper per match
        goal_keeper_save_accuracy (Union[Unset, float]): Rate of all balls saved by the goalkeeper
        goal_keeper_save_accuracy_per_match (Union[None, Unset, float]): Rate of all balls saved by the goalkeeper per
            match
        goal_keeper_seconds_played (Union[None, Unset, int]): Total number of seconds played by the goalkeeper
        goal_keeper_seconds_played_per_match (Union[None, Unset, float]): Average number of seconds played by the
            goalkeeper per match
        goal_keeper_seven_metre_goals_against (Union[None, Unset, int]): Total number of seven metre penalty goals
            conceded by the goalkeeper
        goal_keeper_seven_metre_goals_against_per_match (Union[None, Unset, float]): Average number of seven metre
            penalty goals conceded by the goalkeeper per match
        goal_keeper_seven_metre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            seven metre position
        goal_keeper_seven_metre_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the seven metre position per match
        goal_keeper_seven_metre_shots_against (Union[None, Unset, int]): Total number of seven metre penalty shots on
            goal against the goalkeeper
        goal_keeper_seven_metre_shots_against_per_match (Union[None, Unset, float]): Average number of seven metre
            penalty shots on goal against the goalkeeper per match
        goal_keeper_seven_metre_shots_saved (Union[None, Unset, int]): Total number of seven metre penalty shots saved
            by the goalkeeper
        goal_keeper_seven_metre_shots_saved_per_match (Union[None, Unset, float]): Average number of seven metre penalty
            shots saved by the goalkeeper per match
        goal_keeper_shots_against (Union[None, Unset, int]): Total number of shots against the goalkeeper
        goal_keeper_shots_against_per_match (Union[None, Unset, float]): Average number of shots against the goalkeeper
            per match
        goal_keeper_shots_per_goals_against (Union[None, Unset, float]): Ratio of shots against to goals against for a
            goalkeeper
        goal_keeper_shots_saved (Union[None, Unset, int]): Total number of shots saved by the goalkeeper
        goal_keeper_shots_saved_per_match (Union[None, Unset, float]): Average number of shots saved by the goalkeeper
            per match
        goal_keeper_six_metre_centre_goals_against (Union[None, Unset, int]): Total number of six metre centre goals
            conceded by the goalkeeper
        goal_keeper_six_metre_centre_goals_against_per_match (Union[None, Unset, float]): Average number of six metre
            centre goals conceded by the goalkeeper per match
        goal_keeper_six_metre_centre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            six metre centre position
        goal_keeper_six_metre_centre_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the six metre centre position per match
        goal_keeper_six_metre_centre_shots_against (Union[None, Unset, int]): Total number of six metre centre shots on
            goal against the goalkeeper
        goal_keeper_six_metre_centre_shots_against_per_match (Union[None, Unset, float]): Average number of six metre
            centre shots on goal against the goalkeeper per match
        goal_keeper_six_metre_centre_shots_saved (Union[None, Unset, int]): Total number of six metre centre shots saved
            by the goalkeeper
        goal_keeper_six_metre_centre_shots_saved_per_match (Union[None, Unset, float]): Average number of six metre
            centre shots saved by the goalkeeper per match
        goal_keeper_six_metre_goals_against (Union[None, Unset, int]): Total number of six metre goals conceded by the
            goalkeeper
        goal_keeper_six_metre_goals_against_per_match (Union[None, Unset, float]): Average number of six metre goals
            conceded by the goalkeeper per match
        goal_keeper_six_metre_left_goals_against (Union[None, Unset, int]): Total number of six metre left goals
            conceded by the goalkeeper
        goal_keeper_six_metre_left_goals_against_per_match (Union[None, Unset, float]): Average number of six metre left
            goals conceded by the goalkeeper per match
        goal_keeper_six_metre_left_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            six metre left position
        goal_keeper_six_metre_left_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the six metre left position per match
        goal_keeper_six_metre_left_shots_against (Union[None, Unset, int]): Total number of six metre left shots on goal
            against the goalkeeper
        goal_keeper_six_metre_left_shots_against_per_match (Union[None, Unset, float]): Average number of six metre left
            shots on goal against the goalkeeper per match
        goal_keeper_six_metre_left_shots_saved (Union[None, Unset, int]): Total number of six metre left shots saved by
            the goalkeeper
        goal_keeper_six_metre_left_shots_saved_per_match (Union[None, Unset, float]): Average number of six metre left
            shots saved by the goalkeeper per match
        goal_keeper_six_metre_right_goals_against (Union[None, Unset, int]): Total number of six metre right goals
            conceded by the goalkeeper
        goal_keeper_six_metre_right_goals_against_per_match (Union[None, Unset, float]): Average number of six metre
            right goals conceded by the goalkeeper per match
        goal_keeper_six_metre_right_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the
            six metre right position
        goal_keeper_six_metre_right_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the six metre right position per match
        goal_keeper_six_metre_right_shots_against (Union[None, Unset, int]): Total number of six metre right shots on
            goal against the goalkeeper
        goal_keeper_six_metre_right_shots_against_per_match (Union[None, Unset, float]): Average number of six metre
            right shots on goal against the goalkeeper per match
        goal_keeper_six_metre_right_shots_saved (Union[None, Unset, int]): Total number of six metre right shots saved
            by the goalkeeper
        goal_keeper_six_metre_right_shots_saved_per_match (Union[None, Unset, float]): Average number of six metre right
            shots saved by the goalkeeper per match
        goal_keeper_six_metre_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the six
            metre position
        goal_keeper_six_metre_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the goalkeeper
            from the six metre position per match
        goal_keeper_six_metre_shots_against (Union[None, Unset, int]): Total number of six metre shots on goal against
            the goalkeeper
        goal_keeper_six_metre_shots_against_per_match (Union[None, Unset, float]): Average number of six metre shots on
            goal against the goalkeeper per match
        goal_keeper_six_metre_shots_saved (Union[None, Unset, int]): Total number of six metre shots saved by the
            goalkeeper
        goal_keeper_six_metre_shots_saved_per_match (Union[None, Unset, float]): Average number of six metre shots saved
            by the goalkeeper per match
        goal_keeper_wing_goals_against (Union[None, Unset, int]): Total number of wing goals conceded by the goalkeeper
        goal_keeper_wing_goals_against_per_match (Union[None, Unset, float]): Average number of wing goals conceded by
            the goalkeeper per match
        goal_keeper_wing_left_goals_against (Union[None, Unset, int]): Total number of left wing goals conceded by the
            goalkeeper
        goal_keeper_wing_left_goals_against_per_match (Union[None, Unset, float]): Average number of left wing goals
            conceded by the goalkeeper per match
        goal_keeper_wing_left_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the wing
            left position
        goal_keeper_wing_left_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the goalkeeper
            from the wing left position per match
        goal_keeper_wing_left_shots_against (Union[None, Unset, int]): Total number of left wing shots on goal against
            the goalkeeper
        goal_keeper_wing_left_shots_against_per_match (Union[None, Unset, float]): Average number of left wing shots on
            goal against the goalkeeper per match
        goal_keeper_wing_left_shots_saved (Union[None, Unset, int]): Total number of left wing shots saved by the
            goalkeeper
        goal_keeper_wing_left_shots_saved_per_match (Union[None, Unset, float]): Average number of left wing shots saved
            by the goalkeeper per match
        goal_keeper_wing_right_goals_against (Union[None, Unset, int]): Total number of right wing goals conceded by the
            goalkeeper
        goal_keeper_wing_right_goals_against_per_match (Union[None, Unset, float]): Average number of right wing goals
            conceded by the goalkeeper per match
        goal_keeper_wing_right_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the wing
            right position
        goal_keeper_wing_right_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the
            goalkeeper from the wing right position per match
        goal_keeper_wing_right_shots_against (Union[None, Unset, int]): Total number of right wing shots on goal against
            the goalkeeper
        goal_keeper_wing_right_shots_against_per_match (Union[None, Unset, float]): Average number of right wing shots
            on goal against the goalkeeper per match
        goal_keeper_wing_right_shots_saved (Union[None, Unset, int]): Total number of right wing shots saved by the
            goalkeeper
        goal_keeper_wing_right_shots_saved_per_match (Union[None, Unset, float]): Average number of right wing shots
            saved by the goalkeeper per match
        goal_keeper_wing_save_accuracy (Union[Unset, float]): Rate of balls saved by the goalkeeper from the wing
            position
        goal_keeper_wing_save_accuracy_per_match (Union[None, Unset, float]): Rate of balls saved by the goalkeeper from
            the wing position per match
        goal_keeper_wing_shots_against (Union[None, Unset, int]): Total number of wing shots on goal against the
            goalkeeper
        goal_keeper_wing_shots_against_per_match (Union[None, Unset, float]): Average number of wing shots on goal
            against the goalkeeper per match
        goal_keeper_wing_shots_saved (Union[None, Unset, int]): Total number of wing shots saved by the goalkeeper
        goal_keeper_wing_shots_saved_per_match (Union[None, Unset, float]): Average number of wing shots saved by the
            goalkeeper per match
        goals_scored (Union[None, Unset, int]): Total number of goals scored
        goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored per match
        handball_performance_index (Union[None, Unset, float]): Handball Performance Index
        losses (Union[None, Unset, int]): The number of losses
        matches_played (Union[None, Unset, int]): The number of matches that they have participated in
        minutes (Union[None, Unset, float, str]): Time in play (in ISO8601 Duration format); only available for
            goalkeepers
        minutes_per_match (Union[None, Unset, float, str]): Average time in play (in ISO8601 Duration format) per game;
            only for goalkeepers
        missed_shots (Union[None, Unset, int]): Total number of missed shots
        missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots per match
        nine_metre_centre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre
            centre position
        nine_metre_centre_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the
            nine metre centre position per match
        nine_metre_centre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre
            centre position
        nine_metre_centre_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the
            nine metre centre position per match
        nine_metre_centre_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre centre
            position
        nine_metre_centre_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the nine
            metre centre position per match
        nine_metre_centre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre centre
            position
        nine_metre_centre_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the
            nine metre centre position per match
        nine_metre_centre_shots (Union[None, Unset, int]): Total number of nine metre centre shots
        nine_metre_centre_shots_per_match (Union[None, Unset, float]): Average number of nine metre centre shots per
            match
        nine_metre_centre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre
            centre position
        nine_metre_centre_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the
            nine metre centre position per match
        nine_metre_centre_shots_on_goal (Union[None, Unset, int]): Total number of nine metre centre shots on goal
        nine_metre_centre_shots_on_goal_per_match (Union[None, Unset, float]): Average number of nine metre centre shots
            on goal per match
        nine_metre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre position
        nine_metre_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the nine
            metre position per match
        nine_metre_left_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre left
            position
        nine_metre_left_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the nine
            metre left position per match
        nine_metre_left_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre left
            position
        nine_metre_left_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the nine
            metre left position per match
        nine_metre_left_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre left position
        nine_metre_left_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the nine metre
            left position per match
        nine_metre_left_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre left
            position
        nine_metre_left_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the
            nine metre left position per match
        nine_metre_left_shots (Union[None, Unset, int]): Total number of nine metre left shots attempted
        nine_metre_left_shots_per_match (Union[None, Unset, float]): Average number of nine metre left shots attempted
            per match
        nine_metre_left_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre left
            position
        nine_metre_left_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the
            nine metre left position per match
        nine_metre_left_shots_on_goal (Union[None, Unset, int]): Total number of nine metre left shots on goal
        nine_metre_left_shots_on_goal_per_match (Union[None, Unset, float]): Average number of nine metre left shots on
            goal per match
        nine_metre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre position
        nine_metre_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the nine
            metre position per match
        nine_metre_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre position
        nine_metre_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the nine metre
            position per match
        nine_metre_right_goals_scored (Union[None, Unset, int]): Total number of goals scored from the nine metre right
            position
        nine_metre_right_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the
            nine metre right position per match
        nine_metre_right_missed_shots (Union[None, Unset, int]): Total number of missed shots from the nine metre right
            position
        nine_metre_right_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the
            nine metre right position per match
        nine_metre_right_post_hits (Union[None, Unset, int]): Total number of post hits from the nine metre right
            position
        nine_metre_right_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the nine
            metre right position per match
        nine_metre_right_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre right
            position
        nine_metre_right_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the
            nine metre right position per match
        nine_metre_right_shots (Union[None, Unset, int]): Total number of nine metre right shots attempted
        nine_metre_right_shots_per_match (Union[None, Unset, float]): Average number of nine metre right shots attempted
            per match
        nine_metre_right_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre
            right position
        nine_metre_right_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the
            nine metre right position per match
        nine_metre_right_shots_on_goal (Union[None, Unset, int]): Total number of nine metre right shots on goal
        nine_metre_right_shots_on_goal_per_match (Union[None, Unset, float]): Average number of nine metre right shots
            on goal per match
        nine_metre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the nine metre position
        nine_metre_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the nine
            metre position per match
        nine_metre_shots (Union[None, Unset, int]): Total number of nine metre shots attempted
        nine_metre_shots_per_match (Union[None, Unset, float]): Average number of nine metre shots attempted per match
        nine_metre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the nine metre position
        nine_metre_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the nine
            metre position per match
        nine_metre_shots_on_goal (Union[None, Unset, int]): Total number of nine metre shots on goal
        nine_metre_shots_on_goal_per_match (Union[None, Unset, float]): Average number of nine metre shots on goal per
            match
        passive_play (Union[None, Unset, int]): Total number of passive play
        pivot_goals_scored (Union[None, Unset, int]): Total number of goals scored from the pivot position
        pivot_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the pivot position
            per match
        pivot_missed_shots (Union[None, Unset, int]): Total number of missed shots from the pivot position
        pivot_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the pivot position
            per match
        pivot_post_hits (Union[None, Unset, int]): Total number of post hits from the pivot position
        pivot_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the pivot position per
            match
        pivot_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the pivot position
        pivot_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the pivot
            position per match
        pivot_shots (Union[None, Unset, int]): Total number of pivot shots attempted
        pivot_shots_per_match (Union[None, Unset, float]): Average number of pivot shots attempted per match
        pivot_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the pivot position
        pivot_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the pivot
            position per match
        pivot_shots_on_goal (Union[None, Unset, int]): Total number of pivot shots on goal
        pivot_shots_on_goal_per_match (Union[None, Unset, float]): Average number of pivot shots on goal per match
        post_hits (Union[None, Unset, int]): Total number of post hits
        post_hits_per_match (Union[None, Unset, float]): Average number of post hits per match
        red_cards (Union[None, Unset, int]): Total number of red cards
        red_cards_per_match (Union[None, Unset, float]): Average number of red cards per match
        seven_metre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the seven metre penalties
        seven_metre_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the seven
            metre penalties per match
        seven_metre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the seven metre penalties
        seven_metre_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the seven
            metre penalties per match
        seven_metre_penalties_awarded (Union[None, Unset, int]): Total number of seven metre penalties awarded
        seven_metre_penalties_awarded_per_match (Union[None, Unset, float]): Average number of seven metre penalties
            awarded per match
        seven_metre_penalties_caused (Union[None, Unset, int]): Total number of seven metre penalties caused
        seven_metre_penalties_caused_per_match (Union[None, Unset, float]): Average number of seven metre penalties
            caused per match
        seven_metre_penalty_fouls (Union[None, Unset, int]): Total number of seven metre penalty fouls
        seven_metre_penalty_fouls_per_match (Union[None, Unset, float]): Average number of seven metre penalty fouls per
            match
        seven_metre_post_hits (Union[None, Unset, int]): Total number of post hits from the seven metre penalties
        seven_metre_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the seven metre
            penalties per match
        seven_metre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from seven metre penalties
        seven_metre_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from seven metre
            penalties per match
        seven_metre_shots (Union[None, Unset, int]): Total number of seven metre penalty shots attempted
        seven_metre_shots_per_match (Union[None, Unset, float]): Average number of seven metre penalty shots attempted
            per match
        seven_metre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the seven metre
            penalties
        seven_metre_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the seven
            metre penalties per match
        seven_metre_shots_on_goal (Union[None, Unset, int]): Total number of seven metre penalty shots on goal
        seven_metre_shots_on_goal_per_match (Union[None, Unset, float]): Average number of seven metre penalty shots on
            goal per match
        shooting_accuracy (Union[Unset, float]): Shot rate for all shots on goal
        shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate for all shots on goal per match
        shoot_outs (Union[None, Unset, int]): Total number of shoot outs
        shoot_outs_per_match (Union[None, Unset, float]): Average number of shoot outs per match
        shoot_outs_made (Union[None, Unset, int]): Total number of goals scored from shoot out shots
        shoot_outs_made_per_match (Union[None, Unset, float]): Average number of shoot outs made per match
        shoot_outs_missed (Union[None, Unset, int]): Total number of shoot out shots missed
        shoot_outs_missed_per_match (Union[None, Unset, float]): Average number of shoot outs missed per match
        shoot_outs_saved (Union[None, Unset, int]): Total number of shoot out shots saved
        shoot_outs_saved_per_match (Union[None, Unset, float]): Average number of shoot outs saved per match
        shots (Union[None, Unset, int]): Total number of shots. This is made up of all shots, including shot that are
            blocked, saved, lead to a goal, missed, hit the bar or post.
        shots_per_match (Union[None, Unset, float]): Average number of shots per match
        shots_blocked (Union[None, Unset, int]): Total number of shots blocked
        shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked per match
        shots_on_goal (Union[None, Unset, int]): Total number of shots on target. This is made up of shots that lead to
            goals or a save from the Goalie.
        shots_on_goal_per_match (Union[None, Unset, float]): Average number of shots on goal per match
        shots_saved_by_goal_keeper (Union[None, Unset, int]): The number of shots taken by a player that were saved by
            the opposition goalkeeper
        shots_saved_by_goal_keeper_per_match (Union[None, Unset, float]): Average number of shots taken by a player that
            were saved by the opposition goalkeeper per match
        six_metre_centre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre centre
            position
        six_metre_centre_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the six
            metre centre position per match
        six_metre_centre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre centre
            position
        six_metre_centre_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the six
            metre centre position per match
        six_metre_centre_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre centre
            position
        six_metre_centre_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the six metre
            centre position per match
        six_metre_centre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre centre
            position
        six_metre_centre_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the
            six metre centre position per match
        six_metre_centre_shots (Union[None, Unset, int]): Total number of six metre centre shots
        six_metre_centre_shots_per_match (Union[None, Unset, float]): Average number of six metre centre shots per match
        six_metre_centre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre
            centre position
        six_metre_centre_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the
            six metre centre position per match
        six_metre_centre_shots_on_goal (Union[None, Unset, int]): Total number of six metre centre shots on goal
        six_metre_centre_shots_on_goal_per_match (Union[None, Unset, float]): Average number of six metre centre shots
            on goal per match
        six_metre_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre position
        six_metre_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the six metre
            position per match
        six_metre_left_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre left
            position
        six_metre_left_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the six
            metre left position per match
        six_metre_left_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre left
            position
        six_metre_left_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the six
            metre left position per match
        six_metre_left_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre left position
        six_metre_left_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the six metre
            left position per match
        six_metre_left_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre left
            position
        six_metre_left_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the six
            metre left position per match
        six_metre_left_shots (Union[None, Unset, int]): Total number of six metre left shots attempted
        six_metre_left_shots_per_match (Union[None, Unset, float]): Average number of six metre left shots attempted per
            match
        six_metre_left_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre left
            position
        six_metre_left_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the six
            metre left position per match
        six_metre_left_shots_on_goal (Union[None, Unset, int]): Total number of six metre left shots on goal
        six_metre_left_shots_on_goal_per_match (Union[None, Unset, float]): Average number of six metre left shots on
            goal per match
        six_metre_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre position
        six_metre_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the six metre
            position per match
        six_metre_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre position
        six_metre_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the six metre
            position per match
        six_metre_right_goals_scored (Union[None, Unset, int]): Total number of goals scored from the six metre right
            position
        six_metre_right_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the six
            metre right position per match
        six_metre_right_missed_shots (Union[None, Unset, int]): Total number of missed shots from the six metre right
            position
        six_metre_right_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the six
            metre right position per match
        six_metre_right_post_hits (Union[None, Unset, int]): Total number of post hits from the six metre right position
        six_metre_right_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the six metre
            right position per match
        six_metre_right_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre right
            position
        six_metre_right_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the six
            metre right position per match
        six_metre_right_shots (Union[None, Unset, int]): Total number of six metre right shots attempted
        six_metre_right_shots_per_match (Union[None, Unset, float]): Average number of six metre right shots attempted
            per match
        six_metre_right_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre right
            position
        six_metre_right_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the
            six metre right position per match
        six_metre_right_shots_on_goal (Union[None, Unset, int]): Total number of six metre right shots on goal
        six_metre_right_shots_on_goal_per_match (Union[None, Unset, float]): Average number of six metre right shots on
            goal per match
        six_metre_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the six metre position
        six_metre_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the six metre
            position per match
        six_metre_shots (Union[None, Unset, int]): Total number of six metre shots attempted
        six_metre_shots_per_match (Union[None, Unset, float]): Average number of six metre shots attempted per match
        six_metre_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the six metre position
        six_metre_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the six
            metre position per match
        six_metre_shots_on_goal (Union[None, Unset, int]): Total number of six metre shots on goal
        six_metre_shots_on_goal_per_match (Union[None, Unset, float]): Average number of six metre shots on goal per
            match
        speed_distance_per_time (Union[None, Unset, float]): Distance covered by the player on specific speed per minute
        speed_max (Union[None, Unset, float]): Maximum speed [m/s] of the player during the session
        steals (Union[None, Unset, int]): Total number of stolen balls by the player
        steals_per_match (Union[None, Unset, float]): Average number of stolen balls by the player per match
        substitutions (Union[None, Unset, int]): Total number of substitutions
        substitutions_per_match (Union[None, Unset, float]): Average number of substitutions per match
        suspensions (Union[None, Unset, int]): Total number of suspensions
        suspensions_per_match (Union[None, Unset, float]): Average number of suspensions per match
        technical_ball_faults (Union[None, Unset, int]): Total number of technical ball errors
        technical_ball_faults_per_match (Union[None, Unset, float]): Average number of technical ball errors per match
        technical_faults (Union[None, Unset, int]): Total number of technical errors
        technical_faults_per_match (Union[None, Unset, float]): Average number of technical errors per match
        technical_rule_faults (Union[None, Unset, int]): Total number of technical rule errors
        technical_rule_faults_per_match (Union[None, Unset, float]): Average number of technical rule errors per match
        time_on_playing_field (Union[None, Unset, float, str]): Time in minutes (in ISO8601 Duration format) that each
            player spent on the playing field during the game
        time_ball_possession (Union[None, Unset, float, str]): Accumulated time in minutes (in ISO8601 Duration format)
            in which the player had the possession of the ball
        time_played (Union[None, Unset, int]): Total number of minutes the played
        time_played_per_match (Union[None, Unset, float]): Average number of minutes the played per match
        turnovers (Union[None, Unset, int]): Total number of turnovers
        turnovers_per_match (Union[None, Unset, float]): Average number of turnovers per match
        two_minute_suspensions (Union[None, Unset, int]): Total number of two minute suspensions
        two_minute_suspensions_per_match (Union[None, Unset, float]): Average number of two minute suspensions per match
        wing_goals_scored (Union[None, Unset, int]): Total number of goals scored from the wing position
        wing_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the wing position
            per match
        wing_left_goals_scored (Union[None, Unset, int]): Total number of goals scored from the left wing position
        wing_left_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the left wing
            position per match
        wing_left_missed_shots (Union[None, Unset, int]): Total number of missed shots from the left wing position
        wing_left_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the left wing
            position per match
        wing_left_post_hits (Union[None, Unset, int]): Total number of post hits from the left wing position
        wing_left_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the left wing
            position per match
        wing_left_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the left wing position
        wing_left_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the left wing
            position per match
        wing_left_shots (Union[None, Unset, int]): Total number of wing left shots attempted
        wing_left_shots_per_match (Union[None, Unset, float]): Average number of wing left shots attempted per match
        wing_left_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the left wing position
        wing_left_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the left
            wing position per match
        wing_left_shots_on_goal (Union[None, Unset, int]): Total number of left wing shots on goal
        wing_left_shots_on_goal_per_match (Union[None, Unset, float]): Average number of left wing shots on goal per
            match
        wing_missed_shots (Union[None, Unset, int]): Total number of missed shots from the wing position
        wing_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the wing position
            per match
        wing_post_hits (Union[None, Unset, int]): Total number of post hits from the wing position
        wing_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the wing position per
            match
        wing_right_goals_scored (Union[None, Unset, int]): Total number of goals scored from the right wing position
        wing_right_goals_scored_per_match (Union[None, Unset, float]): Average number of goals scored from the right
            wing position per match
        wing_right_missed_shots (Union[None, Unset, int]): Total number of missed shots from the right wing position
        wing_right_missed_shots_per_match (Union[None, Unset, float]): Average number of missed shots from the right
            wing position per match
        wing_right_post_hits (Union[None, Unset, int]): Total number of post hits from the right wing position
        wing_right_post_hits_per_match (Union[None, Unset, float]): Average number of post hits from the right wing
            position per match
        wing_right_shooting_accuracy (Union[Unset, float]): Shot rate of shots on goal from the right wing position
        wing_right_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of shots on goal from the right
            wing position per match
        wing_right_shots (Union[None, Unset, int]): Total number of wing right shots attempted
        wing_right_shots_per_match (Union[None, Unset, float]): Average number of wing right shots attempted per match
        wing_right_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the right wing position
        wing_right_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the right
            wing position per match
        wing_right_shots_on_goal (Union[None, Unset, int]): Total number of right wing shots on goal
        wing_right_shots_on_goal_per_match (Union[None, Unset, float]): Average number of right wing shots on goal per
            match
        wing_shooting_accuracy (Union[Unset, float]): Shot rate of all shots on goal from the wing position
        wing_shooting_accuracy_per_match (Union[None, Unset, float]): Shot rate of all shots on goal from the wing
            position per match
        wing_shots (Union[None, Unset, int]): Total number of wing shots attempted
        wing_shots_per_match (Union[None, Unset, float]): Average number of wing shots attempted per match
        wing_shots_blocked (Union[None, Unset, int]): Total number of shots blocked from the wing position
        wing_shots_blocked_per_match (Union[None, Unset, float]): Average number of shots blocked from the wing position
            per match
        wing_shots_on_goal (Union[None, Unset, int]): Total number of wing shots on goal
        wing_shots_on_goal_per_match (Union[None, Unset, float]): Average number of wing shots on goal per match
        wins (Union[None, Unset, int]): The number of wins
        yellow_cards (Union[None, Unset, int]): Total number of yellow cards
        yellow_cards_per_match (Union[None, Unset, float]): Average number of yellow cards per match
    """

    airtime_max: Union[None, Unset, float, str] = UNSET
    assists: Union[None, Unset, int] = UNSET
    assists_per_match: Union[None, Unset, float] = UNSET
    back_court_goals_scored: Union[None, Unset, int] = UNSET
    back_court_goals_scored_per_match: Union[None, Unset, float] = UNSET
    back_court_missed_shots: Union[None, Unset, int] = UNSET
    back_court_missed_shots_per_match: Union[None, Unset, float] = UNSET
    back_court_post_hits: Union[None, Unset, int] = UNSET
    back_court_post_hits_per_match: Union[None, Unset, float] = UNSET
    back_court_shooting_accuracy: Union[Unset, float] = UNSET
    back_court_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    back_court_shots: Union[None, Unset, int] = UNSET
    back_court_shots_per_match: Union[None, Unset, float] = UNSET
    back_court_shots_blocked: Union[None, Unset, int] = UNSET
    back_court_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    back_court_shots_on_goal: Union[None, Unset, int] = UNSET
    back_court_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    blocks: Union[None, Unset, int] = UNSET
    blocks_per_match: Union[None, Unset, float] = UNSET
    blue_cards: Union[None, Unset, int] = UNSET
    blue_cards_per_match: Union[None, Unset, float] = UNSET
    break_through_goals_scored: Union[None, Unset, int] = UNSET
    break_through_goals_scored_per_match: Union[None, Unset, float] = UNSET
    break_through_missed_shots: Union[None, Unset, int] = UNSET
    break_through_missed_shots_per_match: Union[None, Unset, float] = UNSET
    break_through_post_hits: Union[None, Unset, int] = UNSET
    break_through_post_hits_per_match: Union[None, Unset, float] = UNSET
    break_through_shooting_accuracy: Union[Unset, float] = UNSET
    break_through_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    break_through_shots: Union[None, Unset, int] = UNSET
    break_through_shots_per_match: Union[None, Unset, float] = UNSET
    break_through_shots_blocked: Union[None, Unset, int] = UNSET
    break_through_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    break_through_shots_on_goal: Union[None, Unset, int] = UNSET
    break_through_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    cards: Union[None, Unset, int] = UNSET
    cards_per_match: Union[None, Unset, float] = UNSET
    distance_speed_category_1: Union[None, Unset, int] = UNSET
    distance_speed_category_2: Union[None, Unset, int] = UNSET
    distance_speed_category_3: Union[None, Unset, int] = UNSET
    distance_speed_category_4: Union[None, Unset, int] = UNSET
    distance_speed_category_5: Union[None, Unset, int] = UNSET
    distance_total: Union[None, Unset, float] = UNSET
    draws: Union[None, Unset, int] = UNSET
    empty_net_goals_scored: Union[None, Unset, int] = UNSET
    fast_break_goals_scored: Union[None, Unset, int] = UNSET
    fast_break_goals_scored_per_match: Union[None, Unset, float] = UNSET
    fast_break_missed_shots: Union[None, Unset, int] = UNSET
    fast_break_missed_shots_per_match: Union[None, Unset, float] = UNSET
    fast_break_post_hits: Union[None, Unset, int] = UNSET
    fast_break_post_hits_per_match: Union[None, Unset, float] = UNSET
    fast_break_shooting_accuracy: Union[Unset, float] = UNSET
    fast_break_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    fast_break_shots: Union[None, Unset, int] = UNSET
    fast_break_shots_per_match: Union[None, Unset, float] = UNSET
    fast_break_shots_blocked: Union[None, Unset, int] = UNSET
    fast_break_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    fast_break_shots_on_goal: Union[None, Unset, int] = UNSET
    fast_break_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    field_goals_scored: Union[None, Unset, int] = UNSET
    field_goals_scored_per_match: Union[None, Unset, float] = UNSET
    field_missed_shots: Union[None, Unset, int] = UNSET
    field_missed_shots_per_match: Union[None, Unset, float] = UNSET
    field_post_hits: Union[None, Unset, int] = UNSET
    field_post_hits_per_match: Union[None, Unset, float] = UNSET
    field_shooting_accuracy: Union[Unset, float] = UNSET
    field_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    field_shots: Union[None, Unset, int] = UNSET
    field_shots_per_match: Union[None, Unset, float] = UNSET
    field_shots_blocked: Union[None, Unset, int] = UNSET
    field_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    field_shots_on_goal: Union[None, Unset, int] = UNSET
    field_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    fouls: Union[None, Unset, int] = UNSET
    fouls_per_match: Union[None, Unset, float] = UNSET
    fouls_drawn: Union[None, Unset, int] = UNSET
    fouls_drawn_per_match: Union[None, Unset, float] = UNSET
    four_minute_suspensions: Union[None, Unset, int] = UNSET
    four_minute_suspensions_per_match: Union[None, Unset, float] = UNSET
    games: Union[None, Unset, int] = UNSET
    games_started: Union[None, Unset, int] = UNSET
    goal_keeper_back_court_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_back_court_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_back_court_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_back_court_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_back_court_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_back_court_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_back_court_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_back_court_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_break_through_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_break_through_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_break_through_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_break_through_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_break_through_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_break_through_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_break_through_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_break_through_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_fast_break_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_fast_break_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_fast_break_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_fast_break_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_fast_break_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_fast_break_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_fast_break_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_fast_break_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_field_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_field_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_field_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_field_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_field_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_field_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_field_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_field_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_nine_metre_centre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_centre_goals_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_centre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_centre_save_accuracy_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_centre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_centre_shots_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_centre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_centre_shots_saved_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_nine_metre_left_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_left_goals_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_left_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_left_save_accuracy_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_left_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_left_shots_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_left_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_left_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_nine_metre_right_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_right_goals_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_right_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_right_save_accuracy_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_right_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_right_shots_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_right_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_right_shots_saved_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_nine_metre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_nine_metre_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_nine_metre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_nine_metre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_nine_metre_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_pivot_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_pivot_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_pivot_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_pivot_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_pivot_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_pivot_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_pivot_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_pivot_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_seconds_played: Union[None, Unset, int] = UNSET
    goal_keeper_seconds_played_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_seven_metre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_seven_metre_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_seven_metre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_seven_metre_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_seven_metre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_seven_metre_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_seven_metre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_seven_metre_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_shots_per_goals_against: Union[None, Unset, float] = UNSET
    goal_keeper_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_six_metre_centre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_centre_goals_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_centre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_centre_save_accuracy_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_centre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_centre_shots_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_centre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_centre_shots_saved_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_six_metre_left_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_left_goals_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_left_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_left_save_accuracy_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_left_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_left_shots_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_left_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_left_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_six_metre_right_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_right_goals_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_right_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_right_save_accuracy_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_right_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_right_shots_against_per_match: Union[None, Unset, float] = (
        UNSET
    )
    goal_keeper_six_metre_right_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_right_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_six_metre_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_six_metre_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_six_metre_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_six_metre_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_six_metre_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_left_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_left_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_left_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_wing_left_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_left_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_left_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_left_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_wing_left_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_right_goals_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_right_goals_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_right_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_wing_right_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_right_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_right_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_right_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_wing_right_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_save_accuracy: Union[Unset, float] = UNSET
    goal_keeper_wing_save_accuracy_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_shots_against: Union[None, Unset, int] = UNSET
    goal_keeper_wing_shots_against_per_match: Union[None, Unset, float] = UNSET
    goal_keeper_wing_shots_saved: Union[None, Unset, int] = UNSET
    goal_keeper_wing_shots_saved_per_match: Union[None, Unset, float] = UNSET
    goals_scored: Union[None, Unset, int] = UNSET
    goals_scored_per_match: Union[None, Unset, float] = UNSET
    handball_performance_index: Union[None, Unset, float] = UNSET
    losses: Union[None, Unset, int] = UNSET
    matches_played: Union[None, Unset, int] = UNSET
    minutes: Union[None, Unset, float, str] = UNSET
    minutes_per_match: Union[None, Unset, float, str] = UNSET
    missed_shots: Union[None, Unset, int] = UNSET
    missed_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_centre_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_centre_goals_scored_per_match: Union[None, Unset, float] = UNSET
    nine_metre_centre_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_centre_missed_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_centre_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_centre_post_hits_per_match: Union[None, Unset, float] = UNSET
    nine_metre_centre_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_centre_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    nine_metre_centre_shots: Union[None, Unset, int] = UNSET
    nine_metre_centre_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_centre_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_centre_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    nine_metre_centre_shots_on_goal: Union[None, Unset, int] = UNSET
    nine_metre_centre_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    nine_metre_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_goals_scored_per_match: Union[None, Unset, float] = UNSET
    nine_metre_left_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_left_goals_scored_per_match: Union[None, Unset, float] = UNSET
    nine_metre_left_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_left_missed_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_left_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_left_post_hits_per_match: Union[None, Unset, float] = UNSET
    nine_metre_left_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_left_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    nine_metre_left_shots: Union[None, Unset, int] = UNSET
    nine_metre_left_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_left_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_left_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    nine_metre_left_shots_on_goal: Union[None, Unset, int] = UNSET
    nine_metre_left_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    nine_metre_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_missed_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_post_hits_per_match: Union[None, Unset, float] = UNSET
    nine_metre_right_goals_scored: Union[None, Unset, int] = UNSET
    nine_metre_right_goals_scored_per_match: Union[None, Unset, float] = UNSET
    nine_metre_right_missed_shots: Union[None, Unset, int] = UNSET
    nine_metre_right_missed_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_right_post_hits: Union[None, Unset, int] = UNSET
    nine_metre_right_post_hits_per_match: Union[None, Unset, float] = UNSET
    nine_metre_right_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_right_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    nine_metre_right_shots: Union[None, Unset, int] = UNSET
    nine_metre_right_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_right_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_right_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    nine_metre_right_shots_on_goal: Union[None, Unset, int] = UNSET
    nine_metre_right_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    nine_metre_shooting_accuracy: Union[Unset, float] = UNSET
    nine_metre_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    nine_metre_shots: Union[None, Unset, int] = UNSET
    nine_metre_shots_per_match: Union[None, Unset, float] = UNSET
    nine_metre_shots_blocked: Union[None, Unset, int] = UNSET
    nine_metre_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    nine_metre_shots_on_goal: Union[None, Unset, int] = UNSET
    nine_metre_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    passive_play: Union[None, Unset, int] = UNSET
    pivot_goals_scored: Union[None, Unset, int] = UNSET
    pivot_goals_scored_per_match: Union[None, Unset, float] = UNSET
    pivot_missed_shots: Union[None, Unset, int] = UNSET
    pivot_missed_shots_per_match: Union[None, Unset, float] = UNSET
    pivot_post_hits: Union[None, Unset, int] = UNSET
    pivot_post_hits_per_match: Union[None, Unset, float] = UNSET
    pivot_shooting_accuracy: Union[Unset, float] = UNSET
    pivot_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    pivot_shots: Union[None, Unset, int] = UNSET
    pivot_shots_per_match: Union[None, Unset, float] = UNSET
    pivot_shots_blocked: Union[None, Unset, int] = UNSET
    pivot_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    pivot_shots_on_goal: Union[None, Unset, int] = UNSET
    pivot_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    post_hits: Union[None, Unset, int] = UNSET
    post_hits_per_match: Union[None, Unset, float] = UNSET
    red_cards: Union[None, Unset, int] = UNSET
    red_cards_per_match: Union[None, Unset, float] = UNSET
    seven_metre_goals_scored: Union[None, Unset, int] = UNSET
    seven_metre_goals_scored_per_match: Union[None, Unset, float] = UNSET
    seven_metre_missed_shots: Union[None, Unset, int] = UNSET
    seven_metre_missed_shots_per_match: Union[None, Unset, float] = UNSET
    seven_metre_penalties_awarded: Union[None, Unset, int] = UNSET
    seven_metre_penalties_awarded_per_match: Union[None, Unset, float] = UNSET
    seven_metre_penalties_caused: Union[None, Unset, int] = UNSET
    seven_metre_penalties_caused_per_match: Union[None, Unset, float] = UNSET
    seven_metre_penalty_fouls: Union[None, Unset, int] = UNSET
    seven_metre_penalty_fouls_per_match: Union[None, Unset, float] = UNSET
    seven_metre_post_hits: Union[None, Unset, int] = UNSET
    seven_metre_post_hits_per_match: Union[None, Unset, float] = UNSET
    seven_metre_shooting_accuracy: Union[Unset, float] = UNSET
    seven_metre_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    seven_metre_shots: Union[None, Unset, int] = UNSET
    seven_metre_shots_per_match: Union[None, Unset, float] = UNSET
    seven_metre_shots_blocked: Union[None, Unset, int] = UNSET
    seven_metre_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    seven_metre_shots_on_goal: Union[None, Unset, int] = UNSET
    seven_metre_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    shooting_accuracy: Union[Unset, float] = UNSET
    shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    shoot_outs: Union[None, Unset, int] = UNSET
    shoot_outs_per_match: Union[None, Unset, float] = UNSET
    shoot_outs_made: Union[None, Unset, int] = UNSET
    shoot_outs_made_per_match: Union[None, Unset, float] = UNSET
    shoot_outs_missed: Union[None, Unset, int] = UNSET
    shoot_outs_missed_per_match: Union[None, Unset, float] = UNSET
    shoot_outs_saved: Union[None, Unset, int] = UNSET
    shoot_outs_saved_per_match: Union[None, Unset, float] = UNSET
    shots: Union[None, Unset, int] = UNSET
    shots_per_match: Union[None, Unset, float] = UNSET
    shots_blocked: Union[None, Unset, int] = UNSET
    shots_blocked_per_match: Union[None, Unset, float] = UNSET
    shots_on_goal: Union[None, Unset, int] = UNSET
    shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    shots_saved_by_goal_keeper: Union[None, Unset, int] = UNSET
    shots_saved_by_goal_keeper_per_match: Union[None, Unset, float] = UNSET
    six_metre_centre_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_centre_goals_scored_per_match: Union[None, Unset, float] = UNSET
    six_metre_centre_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_centre_missed_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_centre_post_hits: Union[None, Unset, int] = UNSET
    six_metre_centre_post_hits_per_match: Union[None, Unset, float] = UNSET
    six_metre_centre_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_centre_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    six_metre_centre_shots: Union[None, Unset, int] = UNSET
    six_metre_centre_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_centre_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_centre_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    six_metre_centre_shots_on_goal: Union[None, Unset, int] = UNSET
    six_metre_centre_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    six_metre_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_goals_scored_per_match: Union[None, Unset, float] = UNSET
    six_metre_left_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_left_goals_scored_per_match: Union[None, Unset, float] = UNSET
    six_metre_left_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_left_missed_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_left_post_hits: Union[None, Unset, int] = UNSET
    six_metre_left_post_hits_per_match: Union[None, Unset, float] = UNSET
    six_metre_left_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_left_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    six_metre_left_shots: Union[None, Unset, int] = UNSET
    six_metre_left_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_left_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_left_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    six_metre_left_shots_on_goal: Union[None, Unset, int] = UNSET
    six_metre_left_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    six_metre_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_missed_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_post_hits: Union[None, Unset, int] = UNSET
    six_metre_post_hits_per_match: Union[None, Unset, float] = UNSET
    six_metre_right_goals_scored: Union[None, Unset, int] = UNSET
    six_metre_right_goals_scored_per_match: Union[None, Unset, float] = UNSET
    six_metre_right_missed_shots: Union[None, Unset, int] = UNSET
    six_metre_right_missed_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_right_post_hits: Union[None, Unset, int] = UNSET
    six_metre_right_post_hits_per_match: Union[None, Unset, float] = UNSET
    six_metre_right_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_right_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    six_metre_right_shots: Union[None, Unset, int] = UNSET
    six_metre_right_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_right_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_right_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    six_metre_right_shots_on_goal: Union[None, Unset, int] = UNSET
    six_metre_right_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    six_metre_shooting_accuracy: Union[Unset, float] = UNSET
    six_metre_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    six_metre_shots: Union[None, Unset, int] = UNSET
    six_metre_shots_per_match: Union[None, Unset, float] = UNSET
    six_metre_shots_blocked: Union[None, Unset, int] = UNSET
    six_metre_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    six_metre_shots_on_goal: Union[None, Unset, int] = UNSET
    six_metre_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    speed_distance_per_time: Union[None, Unset, float] = UNSET
    speed_max: Union[None, Unset, float] = UNSET
    steals: Union[None, Unset, int] = UNSET
    steals_per_match: Union[None, Unset, float] = UNSET
    substitutions: Union[None, Unset, int] = UNSET
    substitutions_per_match: Union[None, Unset, float] = UNSET
    suspensions: Union[None, Unset, int] = UNSET
    suspensions_per_match: Union[None, Unset, float] = UNSET
    technical_ball_faults: Union[None, Unset, int] = UNSET
    technical_ball_faults_per_match: Union[None, Unset, float] = UNSET
    technical_faults: Union[None, Unset, int] = UNSET
    technical_faults_per_match: Union[None, Unset, float] = UNSET
    technical_rule_faults: Union[None, Unset, int] = UNSET
    technical_rule_faults_per_match: Union[None, Unset, float] = UNSET
    time_on_playing_field: Union[None, Unset, float, str] = UNSET
    time_ball_possession: Union[None, Unset, float, str] = UNSET
    time_played: Union[None, Unset, int] = UNSET
    time_played_per_match: Union[None, Unset, float] = UNSET
    turnovers: Union[None, Unset, int] = UNSET
    turnovers_per_match: Union[None, Unset, float] = UNSET
    two_minute_suspensions: Union[None, Unset, int] = UNSET
    two_minute_suspensions_per_match: Union[None, Unset, float] = UNSET
    wing_goals_scored: Union[None, Unset, int] = UNSET
    wing_goals_scored_per_match: Union[None, Unset, float] = UNSET
    wing_left_goals_scored: Union[None, Unset, int] = UNSET
    wing_left_goals_scored_per_match: Union[None, Unset, float] = UNSET
    wing_left_missed_shots: Union[None, Unset, int] = UNSET
    wing_left_missed_shots_per_match: Union[None, Unset, float] = UNSET
    wing_left_post_hits: Union[None, Unset, int] = UNSET
    wing_left_post_hits_per_match: Union[None, Unset, float] = UNSET
    wing_left_shooting_accuracy: Union[Unset, float] = UNSET
    wing_left_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    wing_left_shots: Union[None, Unset, int] = UNSET
    wing_left_shots_per_match: Union[None, Unset, float] = UNSET
    wing_left_shots_blocked: Union[None, Unset, int] = UNSET
    wing_left_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    wing_left_shots_on_goal: Union[None, Unset, int] = UNSET
    wing_left_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    wing_missed_shots: Union[None, Unset, int] = UNSET
    wing_missed_shots_per_match: Union[None, Unset, float] = UNSET
    wing_post_hits: Union[None, Unset, int] = UNSET
    wing_post_hits_per_match: Union[None, Unset, float] = UNSET
    wing_right_goals_scored: Union[None, Unset, int] = UNSET
    wing_right_goals_scored_per_match: Union[None, Unset, float] = UNSET
    wing_right_missed_shots: Union[None, Unset, int] = UNSET
    wing_right_missed_shots_per_match: Union[None, Unset, float] = UNSET
    wing_right_post_hits: Union[None, Unset, int] = UNSET
    wing_right_post_hits_per_match: Union[None, Unset, float] = UNSET
    wing_right_shooting_accuracy: Union[Unset, float] = UNSET
    wing_right_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    wing_right_shots: Union[None, Unset, int] = UNSET
    wing_right_shots_per_match: Union[None, Unset, float] = UNSET
    wing_right_shots_blocked: Union[None, Unset, int] = UNSET
    wing_right_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    wing_right_shots_on_goal: Union[None, Unset, int] = UNSET
    wing_right_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    wing_shooting_accuracy: Union[Unset, float] = UNSET
    wing_shooting_accuracy_per_match: Union[None, Unset, float] = UNSET
    wing_shots: Union[None, Unset, int] = UNSET
    wing_shots_per_match: Union[None, Unset, float] = UNSET
    wing_shots_blocked: Union[None, Unset, int] = UNSET
    wing_shots_blocked_per_match: Union[None, Unset, float] = UNSET
    wing_shots_on_goal: Union[None, Unset, int] = UNSET
    wing_shots_on_goal_per_match: Union[None, Unset, float] = UNSET
    wins: Union[None, Unset, int] = UNSET
    yellow_cards: Union[None, Unset, int] = UNSET
    yellow_cards_per_match: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        airtime_max: Union[None, Unset, float, str]
        if isinstance(self.airtime_max, Unset):
            airtime_max = UNSET
        else:
            airtime_max = self.airtime_max

        assists: Union[None, Unset, int]
        if isinstance(self.assists, Unset):
            assists = UNSET
        else:
            assists = self.assists

        assists_per_match: Union[None, Unset, float]
        if isinstance(self.assists_per_match, Unset):
            assists_per_match = UNSET
        else:
            assists_per_match = self.assists_per_match

        back_court_goals_scored: Union[None, Unset, int]
        if isinstance(self.back_court_goals_scored, Unset):
            back_court_goals_scored = UNSET
        else:
            back_court_goals_scored = self.back_court_goals_scored

        back_court_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.back_court_goals_scored_per_match, Unset):
            back_court_goals_scored_per_match = UNSET
        else:
            back_court_goals_scored_per_match = self.back_court_goals_scored_per_match

        back_court_missed_shots: Union[None, Unset, int]
        if isinstance(self.back_court_missed_shots, Unset):
            back_court_missed_shots = UNSET
        else:
            back_court_missed_shots = self.back_court_missed_shots

        back_court_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.back_court_missed_shots_per_match, Unset):
            back_court_missed_shots_per_match = UNSET
        else:
            back_court_missed_shots_per_match = self.back_court_missed_shots_per_match

        back_court_post_hits: Union[None, Unset, int]
        if isinstance(self.back_court_post_hits, Unset):
            back_court_post_hits = UNSET
        else:
            back_court_post_hits = self.back_court_post_hits

        back_court_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.back_court_post_hits_per_match, Unset):
            back_court_post_hits_per_match = UNSET
        else:
            back_court_post_hits_per_match = self.back_court_post_hits_per_match

        back_court_shooting_accuracy = self.back_court_shooting_accuracy

        back_court_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.back_court_shooting_accuracy_per_match, Unset):
            back_court_shooting_accuracy_per_match = UNSET
        else:
            back_court_shooting_accuracy_per_match = (
                self.back_court_shooting_accuracy_per_match
            )

        back_court_shots: Union[None, Unset, int]
        if isinstance(self.back_court_shots, Unset):
            back_court_shots = UNSET
        else:
            back_court_shots = self.back_court_shots

        back_court_shots_per_match: Union[None, Unset, float]
        if isinstance(self.back_court_shots_per_match, Unset):
            back_court_shots_per_match = UNSET
        else:
            back_court_shots_per_match = self.back_court_shots_per_match

        back_court_shots_blocked: Union[None, Unset, int]
        if isinstance(self.back_court_shots_blocked, Unset):
            back_court_shots_blocked = UNSET
        else:
            back_court_shots_blocked = self.back_court_shots_blocked

        back_court_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.back_court_shots_blocked_per_match, Unset):
            back_court_shots_blocked_per_match = UNSET
        else:
            back_court_shots_blocked_per_match = self.back_court_shots_blocked_per_match

        back_court_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.back_court_shots_on_goal, Unset):
            back_court_shots_on_goal = UNSET
        else:
            back_court_shots_on_goal = self.back_court_shots_on_goal

        back_court_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.back_court_shots_on_goal_per_match, Unset):
            back_court_shots_on_goal_per_match = UNSET
        else:
            back_court_shots_on_goal_per_match = self.back_court_shots_on_goal_per_match

        blocks: Union[None, Unset, int]
        if isinstance(self.blocks, Unset):
            blocks = UNSET
        else:
            blocks = self.blocks

        blocks_per_match: Union[None, Unset, float]
        if isinstance(self.blocks_per_match, Unset):
            blocks_per_match = UNSET
        else:
            blocks_per_match = self.blocks_per_match

        blue_cards: Union[None, Unset, int]
        if isinstance(self.blue_cards, Unset):
            blue_cards = UNSET
        else:
            blue_cards = self.blue_cards

        blue_cards_per_match: Union[None, Unset, float]
        if isinstance(self.blue_cards_per_match, Unset):
            blue_cards_per_match = UNSET
        else:
            blue_cards_per_match = self.blue_cards_per_match

        break_through_goals_scored: Union[None, Unset, int]
        if isinstance(self.break_through_goals_scored, Unset):
            break_through_goals_scored = UNSET
        else:
            break_through_goals_scored = self.break_through_goals_scored

        break_through_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.break_through_goals_scored_per_match, Unset):
            break_through_goals_scored_per_match = UNSET
        else:
            break_through_goals_scored_per_match = (
                self.break_through_goals_scored_per_match
            )

        break_through_missed_shots: Union[None, Unset, int]
        if isinstance(self.break_through_missed_shots, Unset):
            break_through_missed_shots = UNSET
        else:
            break_through_missed_shots = self.break_through_missed_shots

        break_through_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.break_through_missed_shots_per_match, Unset):
            break_through_missed_shots_per_match = UNSET
        else:
            break_through_missed_shots_per_match = (
                self.break_through_missed_shots_per_match
            )

        break_through_post_hits: Union[None, Unset, int]
        if isinstance(self.break_through_post_hits, Unset):
            break_through_post_hits = UNSET
        else:
            break_through_post_hits = self.break_through_post_hits

        break_through_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.break_through_post_hits_per_match, Unset):
            break_through_post_hits_per_match = UNSET
        else:
            break_through_post_hits_per_match = self.break_through_post_hits_per_match

        break_through_shooting_accuracy = self.break_through_shooting_accuracy

        break_through_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.break_through_shooting_accuracy_per_match, Unset):
            break_through_shooting_accuracy_per_match = UNSET
        else:
            break_through_shooting_accuracy_per_match = (
                self.break_through_shooting_accuracy_per_match
            )

        break_through_shots: Union[None, Unset, int]
        if isinstance(self.break_through_shots, Unset):
            break_through_shots = UNSET
        else:
            break_through_shots = self.break_through_shots

        break_through_shots_per_match: Union[None, Unset, float]
        if isinstance(self.break_through_shots_per_match, Unset):
            break_through_shots_per_match = UNSET
        else:
            break_through_shots_per_match = self.break_through_shots_per_match

        break_through_shots_blocked: Union[None, Unset, int]
        if isinstance(self.break_through_shots_blocked, Unset):
            break_through_shots_blocked = UNSET
        else:
            break_through_shots_blocked = self.break_through_shots_blocked

        break_through_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.break_through_shots_blocked_per_match, Unset):
            break_through_shots_blocked_per_match = UNSET
        else:
            break_through_shots_blocked_per_match = (
                self.break_through_shots_blocked_per_match
            )

        break_through_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.break_through_shots_on_goal, Unset):
            break_through_shots_on_goal = UNSET
        else:
            break_through_shots_on_goal = self.break_through_shots_on_goal

        break_through_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.break_through_shots_on_goal_per_match, Unset):
            break_through_shots_on_goal_per_match = UNSET
        else:
            break_through_shots_on_goal_per_match = (
                self.break_through_shots_on_goal_per_match
            )

        cards: Union[None, Unset, int]
        if isinstance(self.cards, Unset):
            cards = UNSET
        else:
            cards = self.cards

        cards_per_match: Union[None, Unset, float]
        if isinstance(self.cards_per_match, Unset):
            cards_per_match = UNSET
        else:
            cards_per_match = self.cards_per_match

        distance_speed_category_1: Union[None, Unset, int]
        if isinstance(self.distance_speed_category_1, Unset):
            distance_speed_category_1 = UNSET
        else:
            distance_speed_category_1 = self.distance_speed_category_1

        distance_speed_category_2: Union[None, Unset, int]
        if isinstance(self.distance_speed_category_2, Unset):
            distance_speed_category_2 = UNSET
        else:
            distance_speed_category_2 = self.distance_speed_category_2

        distance_speed_category_3: Union[None, Unset, int]
        if isinstance(self.distance_speed_category_3, Unset):
            distance_speed_category_3 = UNSET
        else:
            distance_speed_category_3 = self.distance_speed_category_3

        distance_speed_category_4: Union[None, Unset, int]
        if isinstance(self.distance_speed_category_4, Unset):
            distance_speed_category_4 = UNSET
        else:
            distance_speed_category_4 = self.distance_speed_category_4

        distance_speed_category_5: Union[None, Unset, int]
        if isinstance(self.distance_speed_category_5, Unset):
            distance_speed_category_5 = UNSET
        else:
            distance_speed_category_5 = self.distance_speed_category_5

        distance_total: Union[None, Unset, float]
        if isinstance(self.distance_total, Unset):
            distance_total = UNSET
        else:
            distance_total = self.distance_total

        draws: Union[None, Unset, int]
        if isinstance(self.draws, Unset):
            draws = UNSET
        else:
            draws = self.draws

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

        fast_break_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.fast_break_goals_scored_per_match, Unset):
            fast_break_goals_scored_per_match = UNSET
        else:
            fast_break_goals_scored_per_match = self.fast_break_goals_scored_per_match

        fast_break_missed_shots: Union[None, Unset, int]
        if isinstance(self.fast_break_missed_shots, Unset):
            fast_break_missed_shots = UNSET
        else:
            fast_break_missed_shots = self.fast_break_missed_shots

        fast_break_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.fast_break_missed_shots_per_match, Unset):
            fast_break_missed_shots_per_match = UNSET
        else:
            fast_break_missed_shots_per_match = self.fast_break_missed_shots_per_match

        fast_break_post_hits: Union[None, Unset, int]
        if isinstance(self.fast_break_post_hits, Unset):
            fast_break_post_hits = UNSET
        else:
            fast_break_post_hits = self.fast_break_post_hits

        fast_break_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.fast_break_post_hits_per_match, Unset):
            fast_break_post_hits_per_match = UNSET
        else:
            fast_break_post_hits_per_match = self.fast_break_post_hits_per_match

        fast_break_shooting_accuracy = self.fast_break_shooting_accuracy

        fast_break_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.fast_break_shooting_accuracy_per_match, Unset):
            fast_break_shooting_accuracy_per_match = UNSET
        else:
            fast_break_shooting_accuracy_per_match = (
                self.fast_break_shooting_accuracy_per_match
            )

        fast_break_shots: Union[None, Unset, int]
        if isinstance(self.fast_break_shots, Unset):
            fast_break_shots = UNSET
        else:
            fast_break_shots = self.fast_break_shots

        fast_break_shots_per_match: Union[None, Unset, float]
        if isinstance(self.fast_break_shots_per_match, Unset):
            fast_break_shots_per_match = UNSET
        else:
            fast_break_shots_per_match = self.fast_break_shots_per_match

        fast_break_shots_blocked: Union[None, Unset, int]
        if isinstance(self.fast_break_shots_blocked, Unset):
            fast_break_shots_blocked = UNSET
        else:
            fast_break_shots_blocked = self.fast_break_shots_blocked

        fast_break_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.fast_break_shots_blocked_per_match, Unset):
            fast_break_shots_blocked_per_match = UNSET
        else:
            fast_break_shots_blocked_per_match = self.fast_break_shots_blocked_per_match

        fast_break_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.fast_break_shots_on_goal, Unset):
            fast_break_shots_on_goal = UNSET
        else:
            fast_break_shots_on_goal = self.fast_break_shots_on_goal

        fast_break_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.fast_break_shots_on_goal_per_match, Unset):
            fast_break_shots_on_goal_per_match = UNSET
        else:
            fast_break_shots_on_goal_per_match = self.fast_break_shots_on_goal_per_match

        field_goals_scored: Union[None, Unset, int]
        if isinstance(self.field_goals_scored, Unset):
            field_goals_scored = UNSET
        else:
            field_goals_scored = self.field_goals_scored

        field_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.field_goals_scored_per_match, Unset):
            field_goals_scored_per_match = UNSET
        else:
            field_goals_scored_per_match = self.field_goals_scored_per_match

        field_missed_shots: Union[None, Unset, int]
        if isinstance(self.field_missed_shots, Unset):
            field_missed_shots = UNSET
        else:
            field_missed_shots = self.field_missed_shots

        field_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.field_missed_shots_per_match, Unset):
            field_missed_shots_per_match = UNSET
        else:
            field_missed_shots_per_match = self.field_missed_shots_per_match

        field_post_hits: Union[None, Unset, int]
        if isinstance(self.field_post_hits, Unset):
            field_post_hits = UNSET
        else:
            field_post_hits = self.field_post_hits

        field_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.field_post_hits_per_match, Unset):
            field_post_hits_per_match = UNSET
        else:
            field_post_hits_per_match = self.field_post_hits_per_match

        field_shooting_accuracy = self.field_shooting_accuracy

        field_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.field_shooting_accuracy_per_match, Unset):
            field_shooting_accuracy_per_match = UNSET
        else:
            field_shooting_accuracy_per_match = self.field_shooting_accuracy_per_match

        field_shots: Union[None, Unset, int]
        if isinstance(self.field_shots, Unset):
            field_shots = UNSET
        else:
            field_shots = self.field_shots

        field_shots_per_match: Union[None, Unset, float]
        if isinstance(self.field_shots_per_match, Unset):
            field_shots_per_match = UNSET
        else:
            field_shots_per_match = self.field_shots_per_match

        field_shots_blocked: Union[None, Unset, int]
        if isinstance(self.field_shots_blocked, Unset):
            field_shots_blocked = UNSET
        else:
            field_shots_blocked = self.field_shots_blocked

        field_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.field_shots_blocked_per_match, Unset):
            field_shots_blocked_per_match = UNSET
        else:
            field_shots_blocked_per_match = self.field_shots_blocked_per_match

        field_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.field_shots_on_goal, Unset):
            field_shots_on_goal = UNSET
        else:
            field_shots_on_goal = self.field_shots_on_goal

        field_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.field_shots_on_goal_per_match, Unset):
            field_shots_on_goal_per_match = UNSET
        else:
            field_shots_on_goal_per_match = self.field_shots_on_goal_per_match

        fouls: Union[None, Unset, int]
        if isinstance(self.fouls, Unset):
            fouls = UNSET
        else:
            fouls = self.fouls

        fouls_per_match: Union[None, Unset, float]
        if isinstance(self.fouls_per_match, Unset):
            fouls_per_match = UNSET
        else:
            fouls_per_match = self.fouls_per_match

        fouls_drawn: Union[None, Unset, int]
        if isinstance(self.fouls_drawn, Unset):
            fouls_drawn = UNSET
        else:
            fouls_drawn = self.fouls_drawn

        fouls_drawn_per_match: Union[None, Unset, float]
        if isinstance(self.fouls_drawn_per_match, Unset):
            fouls_drawn_per_match = UNSET
        else:
            fouls_drawn_per_match = self.fouls_drawn_per_match

        four_minute_suspensions: Union[None, Unset, int]
        if isinstance(self.four_minute_suspensions, Unset):
            four_minute_suspensions = UNSET
        else:
            four_minute_suspensions = self.four_minute_suspensions

        four_minute_suspensions_per_match: Union[None, Unset, float]
        if isinstance(self.four_minute_suspensions_per_match, Unset):
            four_minute_suspensions_per_match = UNSET
        else:
            four_minute_suspensions_per_match = self.four_minute_suspensions_per_match

        games: Union[None, Unset, int]
        if isinstance(self.games, Unset):
            games = UNSET
        else:
            games = self.games

        games_started: Union[None, Unset, int]
        if isinstance(self.games_started, Unset):
            games_started = UNSET
        else:
            games_started = self.games_started

        goal_keeper_back_court_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_back_court_goals_against, Unset):
            goal_keeper_back_court_goals_against = UNSET
        else:
            goal_keeper_back_court_goals_against = (
                self.goal_keeper_back_court_goals_against
            )

        goal_keeper_back_court_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_back_court_goals_against_per_match, Unset):
            goal_keeper_back_court_goals_against_per_match = UNSET
        else:
            goal_keeper_back_court_goals_against_per_match = (
                self.goal_keeper_back_court_goals_against_per_match
            )

        goal_keeper_back_court_save_accuracy = self.goal_keeper_back_court_save_accuracy

        goal_keeper_back_court_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_back_court_save_accuracy_per_match, Unset):
            goal_keeper_back_court_save_accuracy_per_match = UNSET
        else:
            goal_keeper_back_court_save_accuracy_per_match = (
                self.goal_keeper_back_court_save_accuracy_per_match
            )

        goal_keeper_back_court_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_back_court_shots_against, Unset):
            goal_keeper_back_court_shots_against = UNSET
        else:
            goal_keeper_back_court_shots_against = (
                self.goal_keeper_back_court_shots_against
            )

        goal_keeper_back_court_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_back_court_shots_against_per_match, Unset):
            goal_keeper_back_court_shots_against_per_match = UNSET
        else:
            goal_keeper_back_court_shots_against_per_match = (
                self.goal_keeper_back_court_shots_against_per_match
            )

        goal_keeper_back_court_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_back_court_shots_saved, Unset):
            goal_keeper_back_court_shots_saved = UNSET
        else:
            goal_keeper_back_court_shots_saved = self.goal_keeper_back_court_shots_saved

        goal_keeper_back_court_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_back_court_shots_saved_per_match, Unset):
            goal_keeper_back_court_shots_saved_per_match = UNSET
        else:
            goal_keeper_back_court_shots_saved_per_match = (
                self.goal_keeper_back_court_shots_saved_per_match
            )

        goal_keeper_break_through_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_break_through_goals_against, Unset):
            goal_keeper_break_through_goals_against = UNSET
        else:
            goal_keeper_break_through_goals_against = (
                self.goal_keeper_break_through_goals_against
            )

        goal_keeper_break_through_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_break_through_goals_against_per_match, Unset):
            goal_keeper_break_through_goals_against_per_match = UNSET
        else:
            goal_keeper_break_through_goals_against_per_match = (
                self.goal_keeper_break_through_goals_against_per_match
            )

        goal_keeper_break_through_save_accuracy = (
            self.goal_keeper_break_through_save_accuracy
        )

        goal_keeper_break_through_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_break_through_save_accuracy_per_match, Unset):
            goal_keeper_break_through_save_accuracy_per_match = UNSET
        else:
            goal_keeper_break_through_save_accuracy_per_match = (
                self.goal_keeper_break_through_save_accuracy_per_match
            )

        goal_keeper_break_through_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_break_through_shots_against, Unset):
            goal_keeper_break_through_shots_against = UNSET
        else:
            goal_keeper_break_through_shots_against = (
                self.goal_keeper_break_through_shots_against
            )

        goal_keeper_break_through_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_break_through_shots_against_per_match, Unset):
            goal_keeper_break_through_shots_against_per_match = UNSET
        else:
            goal_keeper_break_through_shots_against_per_match = (
                self.goal_keeper_break_through_shots_against_per_match
            )

        goal_keeper_break_through_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_break_through_shots_saved, Unset):
            goal_keeper_break_through_shots_saved = UNSET
        else:
            goal_keeper_break_through_shots_saved = (
                self.goal_keeper_break_through_shots_saved
            )

        goal_keeper_break_through_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_break_through_shots_saved_per_match, Unset):
            goal_keeper_break_through_shots_saved_per_match = UNSET
        else:
            goal_keeper_break_through_shots_saved_per_match = (
                self.goal_keeper_break_through_shots_saved_per_match
            )

        goal_keeper_fast_break_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_fast_break_goals_against, Unset):
            goal_keeper_fast_break_goals_against = UNSET
        else:
            goal_keeper_fast_break_goals_against = (
                self.goal_keeper_fast_break_goals_against
            )

        goal_keeper_fast_break_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_fast_break_goals_against_per_match, Unset):
            goal_keeper_fast_break_goals_against_per_match = UNSET
        else:
            goal_keeper_fast_break_goals_against_per_match = (
                self.goal_keeper_fast_break_goals_against_per_match
            )

        goal_keeper_fast_break_save_accuracy = self.goal_keeper_fast_break_save_accuracy

        goal_keeper_fast_break_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_fast_break_save_accuracy_per_match, Unset):
            goal_keeper_fast_break_save_accuracy_per_match = UNSET
        else:
            goal_keeper_fast_break_save_accuracy_per_match = (
                self.goal_keeper_fast_break_save_accuracy_per_match
            )

        goal_keeper_fast_break_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_fast_break_shots_against, Unset):
            goal_keeper_fast_break_shots_against = UNSET
        else:
            goal_keeper_fast_break_shots_against = (
                self.goal_keeper_fast_break_shots_against
            )

        goal_keeper_fast_break_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_fast_break_shots_against_per_match, Unset):
            goal_keeper_fast_break_shots_against_per_match = UNSET
        else:
            goal_keeper_fast_break_shots_against_per_match = (
                self.goal_keeper_fast_break_shots_against_per_match
            )

        goal_keeper_fast_break_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_fast_break_shots_saved, Unset):
            goal_keeper_fast_break_shots_saved = UNSET
        else:
            goal_keeper_fast_break_shots_saved = self.goal_keeper_fast_break_shots_saved

        goal_keeper_fast_break_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_fast_break_shots_saved_per_match, Unset):
            goal_keeper_fast_break_shots_saved_per_match = UNSET
        else:
            goal_keeper_fast_break_shots_saved_per_match = (
                self.goal_keeper_fast_break_shots_saved_per_match
            )

        goal_keeper_field_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_field_goals_against, Unset):
            goal_keeper_field_goals_against = UNSET
        else:
            goal_keeper_field_goals_against = self.goal_keeper_field_goals_against

        goal_keeper_field_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_field_goals_against_per_match, Unset):
            goal_keeper_field_goals_against_per_match = UNSET
        else:
            goal_keeper_field_goals_against_per_match = (
                self.goal_keeper_field_goals_against_per_match
            )

        goal_keeper_field_save_accuracy = self.goal_keeper_field_save_accuracy

        goal_keeper_field_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_field_save_accuracy_per_match, Unset):
            goal_keeper_field_save_accuracy_per_match = UNSET
        else:
            goal_keeper_field_save_accuracy_per_match = (
                self.goal_keeper_field_save_accuracy_per_match
            )

        goal_keeper_field_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_field_shots_against, Unset):
            goal_keeper_field_shots_against = UNSET
        else:
            goal_keeper_field_shots_against = self.goal_keeper_field_shots_against

        goal_keeper_field_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_field_shots_against_per_match, Unset):
            goal_keeper_field_shots_against_per_match = UNSET
        else:
            goal_keeper_field_shots_against_per_match = (
                self.goal_keeper_field_shots_against_per_match
            )

        goal_keeper_field_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_field_shots_saved, Unset):
            goal_keeper_field_shots_saved = UNSET
        else:
            goal_keeper_field_shots_saved = self.goal_keeper_field_shots_saved

        goal_keeper_field_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_field_shots_saved_per_match, Unset):
            goal_keeper_field_shots_saved_per_match = UNSET
        else:
            goal_keeper_field_shots_saved_per_match = (
                self.goal_keeper_field_shots_saved_per_match
            )

        goal_keeper_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_goals_against, Unset):
            goal_keeper_goals_against = UNSET
        else:
            goal_keeper_goals_against = self.goal_keeper_goals_against

        goal_keeper_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_goals_against_per_match, Unset):
            goal_keeper_goals_against_per_match = UNSET
        else:
            goal_keeper_goals_against_per_match = (
                self.goal_keeper_goals_against_per_match
            )

        goal_keeper_nine_metre_centre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_centre_goals_against, Unset):
            goal_keeper_nine_metre_centre_goals_against = UNSET
        else:
            goal_keeper_nine_metre_centre_goals_against = (
                self.goal_keeper_nine_metre_centre_goals_against
            )

        goal_keeper_nine_metre_centre_goals_against_per_match: Union[None, Unset, float]
        if isinstance(
            self.goal_keeper_nine_metre_centre_goals_against_per_match, Unset
        ):
            goal_keeper_nine_metre_centre_goals_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_centre_goals_against_per_match = (
                self.goal_keeper_nine_metre_centre_goals_against_per_match
            )

        goal_keeper_nine_metre_centre_save_accuracy = (
            self.goal_keeper_nine_metre_centre_save_accuracy
        )

        goal_keeper_nine_metre_centre_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(
            self.goal_keeper_nine_metre_centre_save_accuracy_per_match, Unset
        ):
            goal_keeper_nine_metre_centre_save_accuracy_per_match = UNSET
        else:
            goal_keeper_nine_metre_centre_save_accuracy_per_match = (
                self.goal_keeper_nine_metre_centre_save_accuracy_per_match
            )

        goal_keeper_nine_metre_centre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_centre_shots_against, Unset):
            goal_keeper_nine_metre_centre_shots_against = UNSET
        else:
            goal_keeper_nine_metre_centre_shots_against = (
                self.goal_keeper_nine_metre_centre_shots_against
            )

        goal_keeper_nine_metre_centre_shots_against_per_match: Union[None, Unset, float]
        if isinstance(
            self.goal_keeper_nine_metre_centre_shots_against_per_match, Unset
        ):
            goal_keeper_nine_metre_centre_shots_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_centre_shots_against_per_match = (
                self.goal_keeper_nine_metre_centre_shots_against_per_match
            )

        goal_keeper_nine_metre_centre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_centre_shots_saved, Unset):
            goal_keeper_nine_metre_centre_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_centre_shots_saved = (
                self.goal_keeper_nine_metre_centre_shots_saved
            )

        goal_keeper_nine_metre_centre_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_centre_shots_saved_per_match, Unset):
            goal_keeper_nine_metre_centre_shots_saved_per_match = UNSET
        else:
            goal_keeper_nine_metre_centre_shots_saved_per_match = (
                self.goal_keeper_nine_metre_centre_shots_saved_per_match
            )

        goal_keeper_nine_metre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_goals_against, Unset):
            goal_keeper_nine_metre_goals_against = UNSET
        else:
            goal_keeper_nine_metre_goals_against = (
                self.goal_keeper_nine_metre_goals_against
            )

        goal_keeper_nine_metre_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_goals_against_per_match, Unset):
            goal_keeper_nine_metre_goals_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_goals_against_per_match = (
                self.goal_keeper_nine_metre_goals_against_per_match
            )

        goal_keeper_nine_metre_left_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_left_goals_against, Unset):
            goal_keeper_nine_metre_left_goals_against = UNSET
        else:
            goal_keeper_nine_metre_left_goals_against = (
                self.goal_keeper_nine_metre_left_goals_against
            )

        goal_keeper_nine_metre_left_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_left_goals_against_per_match, Unset):
            goal_keeper_nine_metre_left_goals_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_left_goals_against_per_match = (
                self.goal_keeper_nine_metre_left_goals_against_per_match
            )

        goal_keeper_nine_metre_left_save_accuracy = (
            self.goal_keeper_nine_metre_left_save_accuracy
        )

        goal_keeper_nine_metre_left_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_left_save_accuracy_per_match, Unset):
            goal_keeper_nine_metre_left_save_accuracy_per_match = UNSET
        else:
            goal_keeper_nine_metre_left_save_accuracy_per_match = (
                self.goal_keeper_nine_metre_left_save_accuracy_per_match
            )

        goal_keeper_nine_metre_left_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_left_shots_against, Unset):
            goal_keeper_nine_metre_left_shots_against = UNSET
        else:
            goal_keeper_nine_metre_left_shots_against = (
                self.goal_keeper_nine_metre_left_shots_against
            )

        goal_keeper_nine_metre_left_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_left_shots_against_per_match, Unset):
            goal_keeper_nine_metre_left_shots_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_left_shots_against_per_match = (
                self.goal_keeper_nine_metre_left_shots_against_per_match
            )

        goal_keeper_nine_metre_left_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_left_shots_saved, Unset):
            goal_keeper_nine_metre_left_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_left_shots_saved = (
                self.goal_keeper_nine_metre_left_shots_saved
            )

        goal_keeper_nine_metre_left_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_left_shots_saved_per_match, Unset):
            goal_keeper_nine_metre_left_shots_saved_per_match = UNSET
        else:
            goal_keeper_nine_metre_left_shots_saved_per_match = (
                self.goal_keeper_nine_metre_left_shots_saved_per_match
            )

        goal_keeper_nine_metre_right_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_right_goals_against, Unset):
            goal_keeper_nine_metre_right_goals_against = UNSET
        else:
            goal_keeper_nine_metre_right_goals_against = (
                self.goal_keeper_nine_metre_right_goals_against
            )

        goal_keeper_nine_metre_right_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_right_goals_against_per_match, Unset):
            goal_keeper_nine_metre_right_goals_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_right_goals_against_per_match = (
                self.goal_keeper_nine_metre_right_goals_against_per_match
            )

        goal_keeper_nine_metre_right_save_accuracy = (
            self.goal_keeper_nine_metre_right_save_accuracy
        )

        goal_keeper_nine_metre_right_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_right_save_accuracy_per_match, Unset):
            goal_keeper_nine_metre_right_save_accuracy_per_match = UNSET
        else:
            goal_keeper_nine_metre_right_save_accuracy_per_match = (
                self.goal_keeper_nine_metre_right_save_accuracy_per_match
            )

        goal_keeper_nine_metre_right_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_right_shots_against, Unset):
            goal_keeper_nine_metre_right_shots_against = UNSET
        else:
            goal_keeper_nine_metre_right_shots_against = (
                self.goal_keeper_nine_metre_right_shots_against
            )

        goal_keeper_nine_metre_right_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_right_shots_against_per_match, Unset):
            goal_keeper_nine_metre_right_shots_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_right_shots_against_per_match = (
                self.goal_keeper_nine_metre_right_shots_against_per_match
            )

        goal_keeper_nine_metre_right_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_right_shots_saved, Unset):
            goal_keeper_nine_metre_right_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_right_shots_saved = (
                self.goal_keeper_nine_metre_right_shots_saved
            )

        goal_keeper_nine_metre_right_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_right_shots_saved_per_match, Unset):
            goal_keeper_nine_metre_right_shots_saved_per_match = UNSET
        else:
            goal_keeper_nine_metre_right_shots_saved_per_match = (
                self.goal_keeper_nine_metre_right_shots_saved_per_match
            )

        goal_keeper_nine_metre_save_accuracy = self.goal_keeper_nine_metre_save_accuracy

        goal_keeper_nine_metre_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_save_accuracy_per_match, Unset):
            goal_keeper_nine_metre_save_accuracy_per_match = UNSET
        else:
            goal_keeper_nine_metre_save_accuracy_per_match = (
                self.goal_keeper_nine_metre_save_accuracy_per_match
            )

        goal_keeper_nine_metre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_shots_against, Unset):
            goal_keeper_nine_metre_shots_against = UNSET
        else:
            goal_keeper_nine_metre_shots_against = (
                self.goal_keeper_nine_metre_shots_against
            )

        goal_keeper_nine_metre_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_shots_against_per_match, Unset):
            goal_keeper_nine_metre_shots_against_per_match = UNSET
        else:
            goal_keeper_nine_metre_shots_against_per_match = (
                self.goal_keeper_nine_metre_shots_against_per_match
            )

        goal_keeper_nine_metre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_nine_metre_shots_saved, Unset):
            goal_keeper_nine_metre_shots_saved = UNSET
        else:
            goal_keeper_nine_metre_shots_saved = self.goal_keeper_nine_metre_shots_saved

        goal_keeper_nine_metre_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_nine_metre_shots_saved_per_match, Unset):
            goal_keeper_nine_metre_shots_saved_per_match = UNSET
        else:
            goal_keeper_nine_metre_shots_saved_per_match = (
                self.goal_keeper_nine_metre_shots_saved_per_match
            )

        goal_keeper_pivot_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_pivot_goals_against, Unset):
            goal_keeper_pivot_goals_against = UNSET
        else:
            goal_keeper_pivot_goals_against = self.goal_keeper_pivot_goals_against

        goal_keeper_pivot_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_pivot_goals_against_per_match, Unset):
            goal_keeper_pivot_goals_against_per_match = UNSET
        else:
            goal_keeper_pivot_goals_against_per_match = (
                self.goal_keeper_pivot_goals_against_per_match
            )

        goal_keeper_pivot_save_accuracy = self.goal_keeper_pivot_save_accuracy

        goal_keeper_pivot_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_pivot_save_accuracy_per_match, Unset):
            goal_keeper_pivot_save_accuracy_per_match = UNSET
        else:
            goal_keeper_pivot_save_accuracy_per_match = (
                self.goal_keeper_pivot_save_accuracy_per_match
            )

        goal_keeper_pivot_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_pivot_shots_against, Unset):
            goal_keeper_pivot_shots_against = UNSET
        else:
            goal_keeper_pivot_shots_against = self.goal_keeper_pivot_shots_against

        goal_keeper_pivot_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_pivot_shots_against_per_match, Unset):
            goal_keeper_pivot_shots_against_per_match = UNSET
        else:
            goal_keeper_pivot_shots_against_per_match = (
                self.goal_keeper_pivot_shots_against_per_match
            )

        goal_keeper_pivot_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_pivot_shots_saved, Unset):
            goal_keeper_pivot_shots_saved = UNSET
        else:
            goal_keeper_pivot_shots_saved = self.goal_keeper_pivot_shots_saved

        goal_keeper_pivot_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_pivot_shots_saved_per_match, Unset):
            goal_keeper_pivot_shots_saved_per_match = UNSET
        else:
            goal_keeper_pivot_shots_saved_per_match = (
                self.goal_keeper_pivot_shots_saved_per_match
            )

        goal_keeper_save_accuracy = self.goal_keeper_save_accuracy

        goal_keeper_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_save_accuracy_per_match, Unset):
            goal_keeper_save_accuracy_per_match = UNSET
        else:
            goal_keeper_save_accuracy_per_match = (
                self.goal_keeper_save_accuracy_per_match
            )

        goal_keeper_seconds_played: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seconds_played, Unset):
            goal_keeper_seconds_played = UNSET
        else:
            goal_keeper_seconds_played = self.goal_keeper_seconds_played

        goal_keeper_seconds_played_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_seconds_played_per_match, Unset):
            goal_keeper_seconds_played_per_match = UNSET
        else:
            goal_keeper_seconds_played_per_match = (
                self.goal_keeper_seconds_played_per_match
            )

        goal_keeper_seven_metre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seven_metre_goals_against, Unset):
            goal_keeper_seven_metre_goals_against = UNSET
        else:
            goal_keeper_seven_metre_goals_against = (
                self.goal_keeper_seven_metre_goals_against
            )

        goal_keeper_seven_metre_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_seven_metre_goals_against_per_match, Unset):
            goal_keeper_seven_metre_goals_against_per_match = UNSET
        else:
            goal_keeper_seven_metre_goals_against_per_match = (
                self.goal_keeper_seven_metre_goals_against_per_match
            )

        goal_keeper_seven_metre_save_accuracy = (
            self.goal_keeper_seven_metre_save_accuracy
        )

        goal_keeper_seven_metre_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_seven_metre_save_accuracy_per_match, Unset):
            goal_keeper_seven_metre_save_accuracy_per_match = UNSET
        else:
            goal_keeper_seven_metre_save_accuracy_per_match = (
                self.goal_keeper_seven_metre_save_accuracy_per_match
            )

        goal_keeper_seven_metre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seven_metre_shots_against, Unset):
            goal_keeper_seven_metre_shots_against = UNSET
        else:
            goal_keeper_seven_metre_shots_against = (
                self.goal_keeper_seven_metre_shots_against
            )

        goal_keeper_seven_metre_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_seven_metre_shots_against_per_match, Unset):
            goal_keeper_seven_metre_shots_against_per_match = UNSET
        else:
            goal_keeper_seven_metre_shots_against_per_match = (
                self.goal_keeper_seven_metre_shots_against_per_match
            )

        goal_keeper_seven_metre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_seven_metre_shots_saved, Unset):
            goal_keeper_seven_metre_shots_saved = UNSET
        else:
            goal_keeper_seven_metre_shots_saved = (
                self.goal_keeper_seven_metre_shots_saved
            )

        goal_keeper_seven_metre_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_seven_metre_shots_saved_per_match, Unset):
            goal_keeper_seven_metre_shots_saved_per_match = UNSET
        else:
            goal_keeper_seven_metre_shots_saved_per_match = (
                self.goal_keeper_seven_metre_shots_saved_per_match
            )

        goal_keeper_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_shots_against, Unset):
            goal_keeper_shots_against = UNSET
        else:
            goal_keeper_shots_against = self.goal_keeper_shots_against

        goal_keeper_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_shots_against_per_match, Unset):
            goal_keeper_shots_against_per_match = UNSET
        else:
            goal_keeper_shots_against_per_match = (
                self.goal_keeper_shots_against_per_match
            )

        goal_keeper_shots_per_goals_against: Union[None, Unset, float]
        if isinstance(self.goal_keeper_shots_per_goals_against, Unset):
            goal_keeper_shots_per_goals_against = UNSET
        else:
            goal_keeper_shots_per_goals_against = (
                self.goal_keeper_shots_per_goals_against
            )

        goal_keeper_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_shots_saved, Unset):
            goal_keeper_shots_saved = UNSET
        else:
            goal_keeper_shots_saved = self.goal_keeper_shots_saved

        goal_keeper_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_shots_saved_per_match, Unset):
            goal_keeper_shots_saved_per_match = UNSET
        else:
            goal_keeper_shots_saved_per_match = self.goal_keeper_shots_saved_per_match

        goal_keeper_six_metre_centre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_centre_goals_against, Unset):
            goal_keeper_six_metre_centre_goals_against = UNSET
        else:
            goal_keeper_six_metre_centre_goals_against = (
                self.goal_keeper_six_metre_centre_goals_against
            )

        goal_keeper_six_metre_centre_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_centre_goals_against_per_match, Unset):
            goal_keeper_six_metre_centre_goals_against_per_match = UNSET
        else:
            goal_keeper_six_metre_centre_goals_against_per_match = (
                self.goal_keeper_six_metre_centre_goals_against_per_match
            )

        goal_keeper_six_metre_centre_save_accuracy = (
            self.goal_keeper_six_metre_centre_save_accuracy
        )

        goal_keeper_six_metre_centre_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_centre_save_accuracy_per_match, Unset):
            goal_keeper_six_metre_centre_save_accuracy_per_match = UNSET
        else:
            goal_keeper_six_metre_centre_save_accuracy_per_match = (
                self.goal_keeper_six_metre_centre_save_accuracy_per_match
            )

        goal_keeper_six_metre_centre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_centre_shots_against, Unset):
            goal_keeper_six_metre_centre_shots_against = UNSET
        else:
            goal_keeper_six_metre_centre_shots_against = (
                self.goal_keeper_six_metre_centre_shots_against
            )

        goal_keeper_six_metre_centre_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_centre_shots_against_per_match, Unset):
            goal_keeper_six_metre_centre_shots_against_per_match = UNSET
        else:
            goal_keeper_six_metre_centre_shots_against_per_match = (
                self.goal_keeper_six_metre_centre_shots_against_per_match
            )

        goal_keeper_six_metre_centre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_centre_shots_saved, Unset):
            goal_keeper_six_metre_centre_shots_saved = UNSET
        else:
            goal_keeper_six_metre_centre_shots_saved = (
                self.goal_keeper_six_metre_centre_shots_saved
            )

        goal_keeper_six_metre_centre_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_centre_shots_saved_per_match, Unset):
            goal_keeper_six_metre_centre_shots_saved_per_match = UNSET
        else:
            goal_keeper_six_metre_centre_shots_saved_per_match = (
                self.goal_keeper_six_metre_centre_shots_saved_per_match
            )

        goal_keeper_six_metre_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_goals_against, Unset):
            goal_keeper_six_metre_goals_against = UNSET
        else:
            goal_keeper_six_metre_goals_against = (
                self.goal_keeper_six_metre_goals_against
            )

        goal_keeper_six_metre_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_goals_against_per_match, Unset):
            goal_keeper_six_metre_goals_against_per_match = UNSET
        else:
            goal_keeper_six_metre_goals_against_per_match = (
                self.goal_keeper_six_metre_goals_against_per_match
            )

        goal_keeper_six_metre_left_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_left_goals_against, Unset):
            goal_keeper_six_metre_left_goals_against = UNSET
        else:
            goal_keeper_six_metre_left_goals_against = (
                self.goal_keeper_six_metre_left_goals_against
            )

        goal_keeper_six_metre_left_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_left_goals_against_per_match, Unset):
            goal_keeper_six_metre_left_goals_against_per_match = UNSET
        else:
            goal_keeper_six_metre_left_goals_against_per_match = (
                self.goal_keeper_six_metre_left_goals_against_per_match
            )

        goal_keeper_six_metre_left_save_accuracy = (
            self.goal_keeper_six_metre_left_save_accuracy
        )

        goal_keeper_six_metre_left_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_left_save_accuracy_per_match, Unset):
            goal_keeper_six_metre_left_save_accuracy_per_match = UNSET
        else:
            goal_keeper_six_metre_left_save_accuracy_per_match = (
                self.goal_keeper_six_metre_left_save_accuracy_per_match
            )

        goal_keeper_six_metre_left_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_left_shots_against, Unset):
            goal_keeper_six_metre_left_shots_against = UNSET
        else:
            goal_keeper_six_metre_left_shots_against = (
                self.goal_keeper_six_metre_left_shots_against
            )

        goal_keeper_six_metre_left_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_left_shots_against_per_match, Unset):
            goal_keeper_six_metre_left_shots_against_per_match = UNSET
        else:
            goal_keeper_six_metre_left_shots_against_per_match = (
                self.goal_keeper_six_metre_left_shots_against_per_match
            )

        goal_keeper_six_metre_left_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_left_shots_saved, Unset):
            goal_keeper_six_metre_left_shots_saved = UNSET
        else:
            goal_keeper_six_metre_left_shots_saved = (
                self.goal_keeper_six_metre_left_shots_saved
            )

        goal_keeper_six_metre_left_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_left_shots_saved_per_match, Unset):
            goal_keeper_six_metre_left_shots_saved_per_match = UNSET
        else:
            goal_keeper_six_metre_left_shots_saved_per_match = (
                self.goal_keeper_six_metre_left_shots_saved_per_match
            )

        goal_keeper_six_metre_right_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_right_goals_against, Unset):
            goal_keeper_six_metre_right_goals_against = UNSET
        else:
            goal_keeper_six_metre_right_goals_against = (
                self.goal_keeper_six_metre_right_goals_against
            )

        goal_keeper_six_metre_right_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_right_goals_against_per_match, Unset):
            goal_keeper_six_metre_right_goals_against_per_match = UNSET
        else:
            goal_keeper_six_metre_right_goals_against_per_match = (
                self.goal_keeper_six_metre_right_goals_against_per_match
            )

        goal_keeper_six_metre_right_save_accuracy = (
            self.goal_keeper_six_metre_right_save_accuracy
        )

        goal_keeper_six_metre_right_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_right_save_accuracy_per_match, Unset):
            goal_keeper_six_metre_right_save_accuracy_per_match = UNSET
        else:
            goal_keeper_six_metre_right_save_accuracy_per_match = (
                self.goal_keeper_six_metre_right_save_accuracy_per_match
            )

        goal_keeper_six_metre_right_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_right_shots_against, Unset):
            goal_keeper_six_metre_right_shots_against = UNSET
        else:
            goal_keeper_six_metre_right_shots_against = (
                self.goal_keeper_six_metre_right_shots_against
            )

        goal_keeper_six_metre_right_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_right_shots_against_per_match, Unset):
            goal_keeper_six_metre_right_shots_against_per_match = UNSET
        else:
            goal_keeper_six_metre_right_shots_against_per_match = (
                self.goal_keeper_six_metre_right_shots_against_per_match
            )

        goal_keeper_six_metre_right_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_right_shots_saved, Unset):
            goal_keeper_six_metre_right_shots_saved = UNSET
        else:
            goal_keeper_six_metre_right_shots_saved = (
                self.goal_keeper_six_metre_right_shots_saved
            )

        goal_keeper_six_metre_right_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_right_shots_saved_per_match, Unset):
            goal_keeper_six_metre_right_shots_saved_per_match = UNSET
        else:
            goal_keeper_six_metre_right_shots_saved_per_match = (
                self.goal_keeper_six_metre_right_shots_saved_per_match
            )

        goal_keeper_six_metre_save_accuracy = self.goal_keeper_six_metre_save_accuracy

        goal_keeper_six_metre_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_save_accuracy_per_match, Unset):
            goal_keeper_six_metre_save_accuracy_per_match = UNSET
        else:
            goal_keeper_six_metre_save_accuracy_per_match = (
                self.goal_keeper_six_metre_save_accuracy_per_match
            )

        goal_keeper_six_metre_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_shots_against, Unset):
            goal_keeper_six_metre_shots_against = UNSET
        else:
            goal_keeper_six_metre_shots_against = (
                self.goal_keeper_six_metre_shots_against
            )

        goal_keeper_six_metre_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_shots_against_per_match, Unset):
            goal_keeper_six_metre_shots_against_per_match = UNSET
        else:
            goal_keeper_six_metre_shots_against_per_match = (
                self.goal_keeper_six_metre_shots_against_per_match
            )

        goal_keeper_six_metre_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_six_metre_shots_saved, Unset):
            goal_keeper_six_metre_shots_saved = UNSET
        else:
            goal_keeper_six_metre_shots_saved = self.goal_keeper_six_metre_shots_saved

        goal_keeper_six_metre_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_six_metre_shots_saved_per_match, Unset):
            goal_keeper_six_metre_shots_saved_per_match = UNSET
        else:
            goal_keeper_six_metre_shots_saved_per_match = (
                self.goal_keeper_six_metre_shots_saved_per_match
            )

        goal_keeper_wing_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_goals_against, Unset):
            goal_keeper_wing_goals_against = UNSET
        else:
            goal_keeper_wing_goals_against = self.goal_keeper_wing_goals_against

        goal_keeper_wing_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_goals_against_per_match, Unset):
            goal_keeper_wing_goals_against_per_match = UNSET
        else:
            goal_keeper_wing_goals_against_per_match = (
                self.goal_keeper_wing_goals_against_per_match
            )

        goal_keeper_wing_left_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_left_goals_against, Unset):
            goal_keeper_wing_left_goals_against = UNSET
        else:
            goal_keeper_wing_left_goals_against = (
                self.goal_keeper_wing_left_goals_against
            )

        goal_keeper_wing_left_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_left_goals_against_per_match, Unset):
            goal_keeper_wing_left_goals_against_per_match = UNSET
        else:
            goal_keeper_wing_left_goals_against_per_match = (
                self.goal_keeper_wing_left_goals_against_per_match
            )

        goal_keeper_wing_left_save_accuracy = self.goal_keeper_wing_left_save_accuracy

        goal_keeper_wing_left_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_left_save_accuracy_per_match, Unset):
            goal_keeper_wing_left_save_accuracy_per_match = UNSET
        else:
            goal_keeper_wing_left_save_accuracy_per_match = (
                self.goal_keeper_wing_left_save_accuracy_per_match
            )

        goal_keeper_wing_left_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_left_shots_against, Unset):
            goal_keeper_wing_left_shots_against = UNSET
        else:
            goal_keeper_wing_left_shots_against = (
                self.goal_keeper_wing_left_shots_against
            )

        goal_keeper_wing_left_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_left_shots_against_per_match, Unset):
            goal_keeper_wing_left_shots_against_per_match = UNSET
        else:
            goal_keeper_wing_left_shots_against_per_match = (
                self.goal_keeper_wing_left_shots_against_per_match
            )

        goal_keeper_wing_left_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_left_shots_saved, Unset):
            goal_keeper_wing_left_shots_saved = UNSET
        else:
            goal_keeper_wing_left_shots_saved = self.goal_keeper_wing_left_shots_saved

        goal_keeper_wing_left_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_left_shots_saved_per_match, Unset):
            goal_keeper_wing_left_shots_saved_per_match = UNSET
        else:
            goal_keeper_wing_left_shots_saved_per_match = (
                self.goal_keeper_wing_left_shots_saved_per_match
            )

        goal_keeper_wing_right_goals_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_right_goals_against, Unset):
            goal_keeper_wing_right_goals_against = UNSET
        else:
            goal_keeper_wing_right_goals_against = (
                self.goal_keeper_wing_right_goals_against
            )

        goal_keeper_wing_right_goals_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_right_goals_against_per_match, Unset):
            goal_keeper_wing_right_goals_against_per_match = UNSET
        else:
            goal_keeper_wing_right_goals_against_per_match = (
                self.goal_keeper_wing_right_goals_against_per_match
            )

        goal_keeper_wing_right_save_accuracy = self.goal_keeper_wing_right_save_accuracy

        goal_keeper_wing_right_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_right_save_accuracy_per_match, Unset):
            goal_keeper_wing_right_save_accuracy_per_match = UNSET
        else:
            goal_keeper_wing_right_save_accuracy_per_match = (
                self.goal_keeper_wing_right_save_accuracy_per_match
            )

        goal_keeper_wing_right_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_right_shots_against, Unset):
            goal_keeper_wing_right_shots_against = UNSET
        else:
            goal_keeper_wing_right_shots_against = (
                self.goal_keeper_wing_right_shots_against
            )

        goal_keeper_wing_right_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_right_shots_against_per_match, Unset):
            goal_keeper_wing_right_shots_against_per_match = UNSET
        else:
            goal_keeper_wing_right_shots_against_per_match = (
                self.goal_keeper_wing_right_shots_against_per_match
            )

        goal_keeper_wing_right_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_right_shots_saved, Unset):
            goal_keeper_wing_right_shots_saved = UNSET
        else:
            goal_keeper_wing_right_shots_saved = self.goal_keeper_wing_right_shots_saved

        goal_keeper_wing_right_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_right_shots_saved_per_match, Unset):
            goal_keeper_wing_right_shots_saved_per_match = UNSET
        else:
            goal_keeper_wing_right_shots_saved_per_match = (
                self.goal_keeper_wing_right_shots_saved_per_match
            )

        goal_keeper_wing_save_accuracy = self.goal_keeper_wing_save_accuracy

        goal_keeper_wing_save_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_save_accuracy_per_match, Unset):
            goal_keeper_wing_save_accuracy_per_match = UNSET
        else:
            goal_keeper_wing_save_accuracy_per_match = (
                self.goal_keeper_wing_save_accuracy_per_match
            )

        goal_keeper_wing_shots_against: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_shots_against, Unset):
            goal_keeper_wing_shots_against = UNSET
        else:
            goal_keeper_wing_shots_against = self.goal_keeper_wing_shots_against

        goal_keeper_wing_shots_against_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_shots_against_per_match, Unset):
            goal_keeper_wing_shots_against_per_match = UNSET
        else:
            goal_keeper_wing_shots_against_per_match = (
                self.goal_keeper_wing_shots_against_per_match
            )

        goal_keeper_wing_shots_saved: Union[None, Unset, int]
        if isinstance(self.goal_keeper_wing_shots_saved, Unset):
            goal_keeper_wing_shots_saved = UNSET
        else:
            goal_keeper_wing_shots_saved = self.goal_keeper_wing_shots_saved

        goal_keeper_wing_shots_saved_per_match: Union[None, Unset, float]
        if isinstance(self.goal_keeper_wing_shots_saved_per_match, Unset):
            goal_keeper_wing_shots_saved_per_match = UNSET
        else:
            goal_keeper_wing_shots_saved_per_match = (
                self.goal_keeper_wing_shots_saved_per_match
            )

        goals_scored: Union[None, Unset, int]
        if isinstance(self.goals_scored, Unset):
            goals_scored = UNSET
        else:
            goals_scored = self.goals_scored

        goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.goals_scored_per_match, Unset):
            goals_scored_per_match = UNSET
        else:
            goals_scored_per_match = self.goals_scored_per_match

        handball_performance_index: Union[None, Unset, float]
        if isinstance(self.handball_performance_index, Unset):
            handball_performance_index = UNSET
        else:
            handball_performance_index = self.handball_performance_index

        losses: Union[None, Unset, int]
        if isinstance(self.losses, Unset):
            losses = UNSET
        else:
            losses = self.losses

        matches_played: Union[None, Unset, int]
        if isinstance(self.matches_played, Unset):
            matches_played = UNSET
        else:
            matches_played = self.matches_played

        minutes: Union[None, Unset, float, str]
        if isinstance(self.minutes, Unset):
            minutes = UNSET
        else:
            minutes = self.minutes

        minutes_per_match: Union[None, Unset, float, str]
        if isinstance(self.minutes_per_match, Unset):
            minutes_per_match = UNSET
        else:
            minutes_per_match = self.minutes_per_match

        missed_shots: Union[None, Unset, int]
        if isinstance(self.missed_shots, Unset):
            missed_shots = UNSET
        else:
            missed_shots = self.missed_shots

        missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.missed_shots_per_match, Unset):
            missed_shots_per_match = UNSET
        else:
            missed_shots_per_match = self.missed_shots_per_match

        nine_metre_centre_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_goals_scored, Unset):
            nine_metre_centre_goals_scored = UNSET
        else:
            nine_metre_centre_goals_scored = self.nine_metre_centre_goals_scored

        nine_metre_centre_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_centre_goals_scored_per_match, Unset):
            nine_metre_centre_goals_scored_per_match = UNSET
        else:
            nine_metre_centre_goals_scored_per_match = (
                self.nine_metre_centre_goals_scored_per_match
            )

        nine_metre_centre_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_missed_shots, Unset):
            nine_metre_centre_missed_shots = UNSET
        else:
            nine_metre_centre_missed_shots = self.nine_metre_centre_missed_shots

        nine_metre_centre_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_centre_missed_shots_per_match, Unset):
            nine_metre_centre_missed_shots_per_match = UNSET
        else:
            nine_metre_centre_missed_shots_per_match = (
                self.nine_metre_centre_missed_shots_per_match
            )

        nine_metre_centre_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_post_hits, Unset):
            nine_metre_centre_post_hits = UNSET
        else:
            nine_metre_centre_post_hits = self.nine_metre_centre_post_hits

        nine_metre_centre_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_centre_post_hits_per_match, Unset):
            nine_metre_centre_post_hits_per_match = UNSET
        else:
            nine_metre_centre_post_hits_per_match = (
                self.nine_metre_centre_post_hits_per_match
            )

        nine_metre_centre_shooting_accuracy = self.nine_metre_centre_shooting_accuracy

        nine_metre_centre_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_centre_shooting_accuracy_per_match, Unset):
            nine_metre_centre_shooting_accuracy_per_match = UNSET
        else:
            nine_metre_centre_shooting_accuracy_per_match = (
                self.nine_metre_centre_shooting_accuracy_per_match
            )

        nine_metre_centre_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_shots, Unset):
            nine_metre_centre_shots = UNSET
        else:
            nine_metre_centre_shots = self.nine_metre_centre_shots

        nine_metre_centre_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_centre_shots_per_match, Unset):
            nine_metre_centre_shots_per_match = UNSET
        else:
            nine_metre_centre_shots_per_match = self.nine_metre_centre_shots_per_match

        nine_metre_centre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_shots_blocked, Unset):
            nine_metre_centre_shots_blocked = UNSET
        else:
            nine_metre_centre_shots_blocked = self.nine_metre_centre_shots_blocked

        nine_metre_centre_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_centre_shots_blocked_per_match, Unset):
            nine_metre_centre_shots_blocked_per_match = UNSET
        else:
            nine_metre_centre_shots_blocked_per_match = (
                self.nine_metre_centre_shots_blocked_per_match
            )

        nine_metre_centre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_centre_shots_on_goal, Unset):
            nine_metre_centre_shots_on_goal = UNSET
        else:
            nine_metre_centre_shots_on_goal = self.nine_metre_centre_shots_on_goal

        nine_metre_centre_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_centre_shots_on_goal_per_match, Unset):
            nine_metre_centre_shots_on_goal_per_match = UNSET
        else:
            nine_metre_centre_shots_on_goal_per_match = (
                self.nine_metre_centre_shots_on_goal_per_match
            )

        nine_metre_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_goals_scored, Unset):
            nine_metre_goals_scored = UNSET
        else:
            nine_metre_goals_scored = self.nine_metre_goals_scored

        nine_metre_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_goals_scored_per_match, Unset):
            nine_metre_goals_scored_per_match = UNSET
        else:
            nine_metre_goals_scored_per_match = self.nine_metre_goals_scored_per_match

        nine_metre_left_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_goals_scored, Unset):
            nine_metre_left_goals_scored = UNSET
        else:
            nine_metre_left_goals_scored = self.nine_metre_left_goals_scored

        nine_metre_left_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_left_goals_scored_per_match, Unset):
            nine_metre_left_goals_scored_per_match = UNSET
        else:
            nine_metre_left_goals_scored_per_match = (
                self.nine_metre_left_goals_scored_per_match
            )

        nine_metre_left_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_missed_shots, Unset):
            nine_metre_left_missed_shots = UNSET
        else:
            nine_metre_left_missed_shots = self.nine_metre_left_missed_shots

        nine_metre_left_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_left_missed_shots_per_match, Unset):
            nine_metre_left_missed_shots_per_match = UNSET
        else:
            nine_metre_left_missed_shots_per_match = (
                self.nine_metre_left_missed_shots_per_match
            )

        nine_metre_left_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_post_hits, Unset):
            nine_metre_left_post_hits = UNSET
        else:
            nine_metre_left_post_hits = self.nine_metre_left_post_hits

        nine_metre_left_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_left_post_hits_per_match, Unset):
            nine_metre_left_post_hits_per_match = UNSET
        else:
            nine_metre_left_post_hits_per_match = (
                self.nine_metre_left_post_hits_per_match
            )

        nine_metre_left_shooting_accuracy = self.nine_metre_left_shooting_accuracy

        nine_metre_left_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_left_shooting_accuracy_per_match, Unset):
            nine_metre_left_shooting_accuracy_per_match = UNSET
        else:
            nine_metre_left_shooting_accuracy_per_match = (
                self.nine_metre_left_shooting_accuracy_per_match
            )

        nine_metre_left_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_shots, Unset):
            nine_metre_left_shots = UNSET
        else:
            nine_metre_left_shots = self.nine_metre_left_shots

        nine_metre_left_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_left_shots_per_match, Unset):
            nine_metre_left_shots_per_match = UNSET
        else:
            nine_metre_left_shots_per_match = self.nine_metre_left_shots_per_match

        nine_metre_left_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_shots_blocked, Unset):
            nine_metre_left_shots_blocked = UNSET
        else:
            nine_metre_left_shots_blocked = self.nine_metre_left_shots_blocked

        nine_metre_left_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_left_shots_blocked_per_match, Unset):
            nine_metre_left_shots_blocked_per_match = UNSET
        else:
            nine_metre_left_shots_blocked_per_match = (
                self.nine_metre_left_shots_blocked_per_match
            )

        nine_metre_left_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_left_shots_on_goal, Unset):
            nine_metre_left_shots_on_goal = UNSET
        else:
            nine_metre_left_shots_on_goal = self.nine_metre_left_shots_on_goal

        nine_metre_left_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_left_shots_on_goal_per_match, Unset):
            nine_metre_left_shots_on_goal_per_match = UNSET
        else:
            nine_metre_left_shots_on_goal_per_match = (
                self.nine_metre_left_shots_on_goal_per_match
            )

        nine_metre_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_missed_shots, Unset):
            nine_metre_missed_shots = UNSET
        else:
            nine_metre_missed_shots = self.nine_metre_missed_shots

        nine_metre_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_missed_shots_per_match, Unset):
            nine_metre_missed_shots_per_match = UNSET
        else:
            nine_metre_missed_shots_per_match = self.nine_metre_missed_shots_per_match

        nine_metre_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_post_hits, Unset):
            nine_metre_post_hits = UNSET
        else:
            nine_metre_post_hits = self.nine_metre_post_hits

        nine_metre_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_post_hits_per_match, Unset):
            nine_metre_post_hits_per_match = UNSET
        else:
            nine_metre_post_hits_per_match = self.nine_metre_post_hits_per_match

        nine_metre_right_goals_scored: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_goals_scored, Unset):
            nine_metre_right_goals_scored = UNSET
        else:
            nine_metre_right_goals_scored = self.nine_metre_right_goals_scored

        nine_metre_right_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_right_goals_scored_per_match, Unset):
            nine_metre_right_goals_scored_per_match = UNSET
        else:
            nine_metre_right_goals_scored_per_match = (
                self.nine_metre_right_goals_scored_per_match
            )

        nine_metre_right_missed_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_missed_shots, Unset):
            nine_metre_right_missed_shots = UNSET
        else:
            nine_metre_right_missed_shots = self.nine_metre_right_missed_shots

        nine_metre_right_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_right_missed_shots_per_match, Unset):
            nine_metre_right_missed_shots_per_match = UNSET
        else:
            nine_metre_right_missed_shots_per_match = (
                self.nine_metre_right_missed_shots_per_match
            )

        nine_metre_right_post_hits: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_post_hits, Unset):
            nine_metre_right_post_hits = UNSET
        else:
            nine_metre_right_post_hits = self.nine_metre_right_post_hits

        nine_metre_right_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_right_post_hits_per_match, Unset):
            nine_metre_right_post_hits_per_match = UNSET
        else:
            nine_metre_right_post_hits_per_match = (
                self.nine_metre_right_post_hits_per_match
            )

        nine_metre_right_shooting_accuracy = self.nine_metre_right_shooting_accuracy

        nine_metre_right_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_right_shooting_accuracy_per_match, Unset):
            nine_metre_right_shooting_accuracy_per_match = UNSET
        else:
            nine_metre_right_shooting_accuracy_per_match = (
                self.nine_metre_right_shooting_accuracy_per_match
            )

        nine_metre_right_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_shots, Unset):
            nine_metre_right_shots = UNSET
        else:
            nine_metre_right_shots = self.nine_metre_right_shots

        nine_metre_right_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_right_shots_per_match, Unset):
            nine_metre_right_shots_per_match = UNSET
        else:
            nine_metre_right_shots_per_match = self.nine_metre_right_shots_per_match

        nine_metre_right_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_shots_blocked, Unset):
            nine_metre_right_shots_blocked = UNSET
        else:
            nine_metre_right_shots_blocked = self.nine_metre_right_shots_blocked

        nine_metre_right_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_right_shots_blocked_per_match, Unset):
            nine_metre_right_shots_blocked_per_match = UNSET
        else:
            nine_metre_right_shots_blocked_per_match = (
                self.nine_metre_right_shots_blocked_per_match
            )

        nine_metre_right_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_right_shots_on_goal, Unset):
            nine_metre_right_shots_on_goal = UNSET
        else:
            nine_metre_right_shots_on_goal = self.nine_metre_right_shots_on_goal

        nine_metre_right_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_right_shots_on_goal_per_match, Unset):
            nine_metre_right_shots_on_goal_per_match = UNSET
        else:
            nine_metre_right_shots_on_goal_per_match = (
                self.nine_metre_right_shots_on_goal_per_match
            )

        nine_metre_shooting_accuracy = self.nine_metre_shooting_accuracy

        nine_metre_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_shooting_accuracy_per_match, Unset):
            nine_metre_shooting_accuracy_per_match = UNSET
        else:
            nine_metre_shooting_accuracy_per_match = (
                self.nine_metre_shooting_accuracy_per_match
            )

        nine_metre_shots: Union[None, Unset, int]
        if isinstance(self.nine_metre_shots, Unset):
            nine_metre_shots = UNSET
        else:
            nine_metre_shots = self.nine_metre_shots

        nine_metre_shots_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_shots_per_match, Unset):
            nine_metre_shots_per_match = UNSET
        else:
            nine_metre_shots_per_match = self.nine_metre_shots_per_match

        nine_metre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.nine_metre_shots_blocked, Unset):
            nine_metre_shots_blocked = UNSET
        else:
            nine_metre_shots_blocked = self.nine_metre_shots_blocked

        nine_metre_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_shots_blocked_per_match, Unset):
            nine_metre_shots_blocked_per_match = UNSET
        else:
            nine_metre_shots_blocked_per_match = self.nine_metre_shots_blocked_per_match

        nine_metre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.nine_metre_shots_on_goal, Unset):
            nine_metre_shots_on_goal = UNSET
        else:
            nine_metre_shots_on_goal = self.nine_metre_shots_on_goal

        nine_metre_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.nine_metre_shots_on_goal_per_match, Unset):
            nine_metre_shots_on_goal_per_match = UNSET
        else:
            nine_metre_shots_on_goal_per_match = self.nine_metre_shots_on_goal_per_match

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

        pivot_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.pivot_goals_scored_per_match, Unset):
            pivot_goals_scored_per_match = UNSET
        else:
            pivot_goals_scored_per_match = self.pivot_goals_scored_per_match

        pivot_missed_shots: Union[None, Unset, int]
        if isinstance(self.pivot_missed_shots, Unset):
            pivot_missed_shots = UNSET
        else:
            pivot_missed_shots = self.pivot_missed_shots

        pivot_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.pivot_missed_shots_per_match, Unset):
            pivot_missed_shots_per_match = UNSET
        else:
            pivot_missed_shots_per_match = self.pivot_missed_shots_per_match

        pivot_post_hits: Union[None, Unset, int]
        if isinstance(self.pivot_post_hits, Unset):
            pivot_post_hits = UNSET
        else:
            pivot_post_hits = self.pivot_post_hits

        pivot_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.pivot_post_hits_per_match, Unset):
            pivot_post_hits_per_match = UNSET
        else:
            pivot_post_hits_per_match = self.pivot_post_hits_per_match

        pivot_shooting_accuracy = self.pivot_shooting_accuracy

        pivot_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.pivot_shooting_accuracy_per_match, Unset):
            pivot_shooting_accuracy_per_match = UNSET
        else:
            pivot_shooting_accuracy_per_match = self.pivot_shooting_accuracy_per_match

        pivot_shots: Union[None, Unset, int]
        if isinstance(self.pivot_shots, Unset):
            pivot_shots = UNSET
        else:
            pivot_shots = self.pivot_shots

        pivot_shots_per_match: Union[None, Unset, float]
        if isinstance(self.pivot_shots_per_match, Unset):
            pivot_shots_per_match = UNSET
        else:
            pivot_shots_per_match = self.pivot_shots_per_match

        pivot_shots_blocked: Union[None, Unset, int]
        if isinstance(self.pivot_shots_blocked, Unset):
            pivot_shots_blocked = UNSET
        else:
            pivot_shots_blocked = self.pivot_shots_blocked

        pivot_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.pivot_shots_blocked_per_match, Unset):
            pivot_shots_blocked_per_match = UNSET
        else:
            pivot_shots_blocked_per_match = self.pivot_shots_blocked_per_match

        pivot_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.pivot_shots_on_goal, Unset):
            pivot_shots_on_goal = UNSET
        else:
            pivot_shots_on_goal = self.pivot_shots_on_goal

        pivot_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.pivot_shots_on_goal_per_match, Unset):
            pivot_shots_on_goal_per_match = UNSET
        else:
            pivot_shots_on_goal_per_match = self.pivot_shots_on_goal_per_match

        post_hits: Union[None, Unset, int]
        if isinstance(self.post_hits, Unset):
            post_hits = UNSET
        else:
            post_hits = self.post_hits

        post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.post_hits_per_match, Unset):
            post_hits_per_match = UNSET
        else:
            post_hits_per_match = self.post_hits_per_match

        red_cards: Union[None, Unset, int]
        if isinstance(self.red_cards, Unset):
            red_cards = UNSET
        else:
            red_cards = self.red_cards

        red_cards_per_match: Union[None, Unset, float]
        if isinstance(self.red_cards_per_match, Unset):
            red_cards_per_match = UNSET
        else:
            red_cards_per_match = self.red_cards_per_match

        seven_metre_goals_scored: Union[None, Unset, int]
        if isinstance(self.seven_metre_goals_scored, Unset):
            seven_metre_goals_scored = UNSET
        else:
            seven_metre_goals_scored = self.seven_metre_goals_scored

        seven_metre_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_goals_scored_per_match, Unset):
            seven_metre_goals_scored_per_match = UNSET
        else:
            seven_metre_goals_scored_per_match = self.seven_metre_goals_scored_per_match

        seven_metre_missed_shots: Union[None, Unset, int]
        if isinstance(self.seven_metre_missed_shots, Unset):
            seven_metre_missed_shots = UNSET
        else:
            seven_metre_missed_shots = self.seven_metre_missed_shots

        seven_metre_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_missed_shots_per_match, Unset):
            seven_metre_missed_shots_per_match = UNSET
        else:
            seven_metre_missed_shots_per_match = self.seven_metre_missed_shots_per_match

        seven_metre_penalties_awarded: Union[None, Unset, int]
        if isinstance(self.seven_metre_penalties_awarded, Unset):
            seven_metre_penalties_awarded = UNSET
        else:
            seven_metre_penalties_awarded = self.seven_metre_penalties_awarded

        seven_metre_penalties_awarded_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_penalties_awarded_per_match, Unset):
            seven_metre_penalties_awarded_per_match = UNSET
        else:
            seven_metre_penalties_awarded_per_match = (
                self.seven_metre_penalties_awarded_per_match
            )

        seven_metre_penalties_caused: Union[None, Unset, int]
        if isinstance(self.seven_metre_penalties_caused, Unset):
            seven_metre_penalties_caused = UNSET
        else:
            seven_metre_penalties_caused = self.seven_metre_penalties_caused

        seven_metre_penalties_caused_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_penalties_caused_per_match, Unset):
            seven_metre_penalties_caused_per_match = UNSET
        else:
            seven_metre_penalties_caused_per_match = (
                self.seven_metre_penalties_caused_per_match
            )

        seven_metre_penalty_fouls: Union[None, Unset, int]
        if isinstance(self.seven_metre_penalty_fouls, Unset):
            seven_metre_penalty_fouls = UNSET
        else:
            seven_metre_penalty_fouls = self.seven_metre_penalty_fouls

        seven_metre_penalty_fouls_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_penalty_fouls_per_match, Unset):
            seven_metre_penalty_fouls_per_match = UNSET
        else:
            seven_metre_penalty_fouls_per_match = (
                self.seven_metre_penalty_fouls_per_match
            )

        seven_metre_post_hits: Union[None, Unset, int]
        if isinstance(self.seven_metre_post_hits, Unset):
            seven_metre_post_hits = UNSET
        else:
            seven_metre_post_hits = self.seven_metre_post_hits

        seven_metre_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_post_hits_per_match, Unset):
            seven_metre_post_hits_per_match = UNSET
        else:
            seven_metre_post_hits_per_match = self.seven_metre_post_hits_per_match

        seven_metre_shooting_accuracy = self.seven_metre_shooting_accuracy

        seven_metre_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_shooting_accuracy_per_match, Unset):
            seven_metre_shooting_accuracy_per_match = UNSET
        else:
            seven_metre_shooting_accuracy_per_match = (
                self.seven_metre_shooting_accuracy_per_match
            )

        seven_metre_shots: Union[None, Unset, int]
        if isinstance(self.seven_metre_shots, Unset):
            seven_metre_shots = UNSET
        else:
            seven_metre_shots = self.seven_metre_shots

        seven_metre_shots_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_shots_per_match, Unset):
            seven_metre_shots_per_match = UNSET
        else:
            seven_metre_shots_per_match = self.seven_metre_shots_per_match

        seven_metre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.seven_metre_shots_blocked, Unset):
            seven_metre_shots_blocked = UNSET
        else:
            seven_metre_shots_blocked = self.seven_metre_shots_blocked

        seven_metre_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_shots_blocked_per_match, Unset):
            seven_metre_shots_blocked_per_match = UNSET
        else:
            seven_metre_shots_blocked_per_match = (
                self.seven_metre_shots_blocked_per_match
            )

        seven_metre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.seven_metre_shots_on_goal, Unset):
            seven_metre_shots_on_goal = UNSET
        else:
            seven_metre_shots_on_goal = self.seven_metre_shots_on_goal

        seven_metre_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.seven_metre_shots_on_goal_per_match, Unset):
            seven_metre_shots_on_goal_per_match = UNSET
        else:
            seven_metre_shots_on_goal_per_match = (
                self.seven_metre_shots_on_goal_per_match
            )

        shooting_accuracy = self.shooting_accuracy

        shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.shooting_accuracy_per_match, Unset):
            shooting_accuracy_per_match = UNSET
        else:
            shooting_accuracy_per_match = self.shooting_accuracy_per_match

        shoot_outs: Union[None, Unset, int]
        if isinstance(self.shoot_outs, Unset):
            shoot_outs = UNSET
        else:
            shoot_outs = self.shoot_outs

        shoot_outs_per_match: Union[None, Unset, float]
        if isinstance(self.shoot_outs_per_match, Unset):
            shoot_outs_per_match = UNSET
        else:
            shoot_outs_per_match = self.shoot_outs_per_match

        shoot_outs_made: Union[None, Unset, int]
        if isinstance(self.shoot_outs_made, Unset):
            shoot_outs_made = UNSET
        else:
            shoot_outs_made = self.shoot_outs_made

        shoot_outs_made_per_match: Union[None, Unset, float]
        if isinstance(self.shoot_outs_made_per_match, Unset):
            shoot_outs_made_per_match = UNSET
        else:
            shoot_outs_made_per_match = self.shoot_outs_made_per_match

        shoot_outs_missed: Union[None, Unset, int]
        if isinstance(self.shoot_outs_missed, Unset):
            shoot_outs_missed = UNSET
        else:
            shoot_outs_missed = self.shoot_outs_missed

        shoot_outs_missed_per_match: Union[None, Unset, float]
        if isinstance(self.shoot_outs_missed_per_match, Unset):
            shoot_outs_missed_per_match = UNSET
        else:
            shoot_outs_missed_per_match = self.shoot_outs_missed_per_match

        shoot_outs_saved: Union[None, Unset, int]
        if isinstance(self.shoot_outs_saved, Unset):
            shoot_outs_saved = UNSET
        else:
            shoot_outs_saved = self.shoot_outs_saved

        shoot_outs_saved_per_match: Union[None, Unset, float]
        if isinstance(self.shoot_outs_saved_per_match, Unset):
            shoot_outs_saved_per_match = UNSET
        else:
            shoot_outs_saved_per_match = self.shoot_outs_saved_per_match

        shots: Union[None, Unset, int]
        if isinstance(self.shots, Unset):
            shots = UNSET
        else:
            shots = self.shots

        shots_per_match: Union[None, Unset, float]
        if isinstance(self.shots_per_match, Unset):
            shots_per_match = UNSET
        else:
            shots_per_match = self.shots_per_match

        shots_blocked: Union[None, Unset, int]
        if isinstance(self.shots_blocked, Unset):
            shots_blocked = UNSET
        else:
            shots_blocked = self.shots_blocked

        shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.shots_blocked_per_match, Unset):
            shots_blocked_per_match = UNSET
        else:
            shots_blocked_per_match = self.shots_blocked_per_match

        shots_on_goal: Union[None, Unset, int]
        if isinstance(self.shots_on_goal, Unset):
            shots_on_goal = UNSET
        else:
            shots_on_goal = self.shots_on_goal

        shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.shots_on_goal_per_match, Unset):
            shots_on_goal_per_match = UNSET
        else:
            shots_on_goal_per_match = self.shots_on_goal_per_match

        shots_saved_by_goal_keeper: Union[None, Unset, int]
        if isinstance(self.shots_saved_by_goal_keeper, Unset):
            shots_saved_by_goal_keeper = UNSET
        else:
            shots_saved_by_goal_keeper = self.shots_saved_by_goal_keeper

        shots_saved_by_goal_keeper_per_match: Union[None, Unset, float]
        if isinstance(self.shots_saved_by_goal_keeper_per_match, Unset):
            shots_saved_by_goal_keeper_per_match = UNSET
        else:
            shots_saved_by_goal_keeper_per_match = (
                self.shots_saved_by_goal_keeper_per_match
            )

        six_metre_centre_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_goals_scored, Unset):
            six_metre_centre_goals_scored = UNSET
        else:
            six_metre_centre_goals_scored = self.six_metre_centre_goals_scored

        six_metre_centre_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_centre_goals_scored_per_match, Unset):
            six_metre_centre_goals_scored_per_match = UNSET
        else:
            six_metre_centre_goals_scored_per_match = (
                self.six_metre_centre_goals_scored_per_match
            )

        six_metre_centre_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_missed_shots, Unset):
            six_metre_centre_missed_shots = UNSET
        else:
            six_metre_centre_missed_shots = self.six_metre_centre_missed_shots

        six_metre_centre_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_centre_missed_shots_per_match, Unset):
            six_metre_centre_missed_shots_per_match = UNSET
        else:
            six_metre_centre_missed_shots_per_match = (
                self.six_metre_centre_missed_shots_per_match
            )

        six_metre_centre_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_post_hits, Unset):
            six_metre_centre_post_hits = UNSET
        else:
            six_metre_centre_post_hits = self.six_metre_centre_post_hits

        six_metre_centre_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_centre_post_hits_per_match, Unset):
            six_metre_centre_post_hits_per_match = UNSET
        else:
            six_metre_centre_post_hits_per_match = (
                self.six_metre_centre_post_hits_per_match
            )

        six_metre_centre_shooting_accuracy = self.six_metre_centre_shooting_accuracy

        six_metre_centre_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_centre_shooting_accuracy_per_match, Unset):
            six_metre_centre_shooting_accuracy_per_match = UNSET
        else:
            six_metre_centre_shooting_accuracy_per_match = (
                self.six_metre_centre_shooting_accuracy_per_match
            )

        six_metre_centre_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_shots, Unset):
            six_metre_centre_shots = UNSET
        else:
            six_metre_centre_shots = self.six_metre_centre_shots

        six_metre_centre_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_centre_shots_per_match, Unset):
            six_metre_centre_shots_per_match = UNSET
        else:
            six_metre_centre_shots_per_match = self.six_metre_centre_shots_per_match

        six_metre_centre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_shots_blocked, Unset):
            six_metre_centre_shots_blocked = UNSET
        else:
            six_metre_centre_shots_blocked = self.six_metre_centre_shots_blocked

        six_metre_centre_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_centre_shots_blocked_per_match, Unset):
            six_metre_centre_shots_blocked_per_match = UNSET
        else:
            six_metre_centre_shots_blocked_per_match = (
                self.six_metre_centre_shots_blocked_per_match
            )

        six_metre_centre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_centre_shots_on_goal, Unset):
            six_metre_centre_shots_on_goal = UNSET
        else:
            six_metre_centre_shots_on_goal = self.six_metre_centre_shots_on_goal

        six_metre_centre_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_centre_shots_on_goal_per_match, Unset):
            six_metre_centre_shots_on_goal_per_match = UNSET
        else:
            six_metre_centre_shots_on_goal_per_match = (
                self.six_metre_centre_shots_on_goal_per_match
            )

        six_metre_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_goals_scored, Unset):
            six_metre_goals_scored = UNSET
        else:
            six_metre_goals_scored = self.six_metre_goals_scored

        six_metre_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_goals_scored_per_match, Unset):
            six_metre_goals_scored_per_match = UNSET
        else:
            six_metre_goals_scored_per_match = self.six_metre_goals_scored_per_match

        six_metre_left_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_left_goals_scored, Unset):
            six_metre_left_goals_scored = UNSET
        else:
            six_metre_left_goals_scored = self.six_metre_left_goals_scored

        six_metre_left_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_left_goals_scored_per_match, Unset):
            six_metre_left_goals_scored_per_match = UNSET
        else:
            six_metre_left_goals_scored_per_match = (
                self.six_metre_left_goals_scored_per_match
            )

        six_metre_left_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_left_missed_shots, Unset):
            six_metre_left_missed_shots = UNSET
        else:
            six_metre_left_missed_shots = self.six_metre_left_missed_shots

        six_metre_left_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_left_missed_shots_per_match, Unset):
            six_metre_left_missed_shots_per_match = UNSET
        else:
            six_metre_left_missed_shots_per_match = (
                self.six_metre_left_missed_shots_per_match
            )

        six_metre_left_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_left_post_hits, Unset):
            six_metre_left_post_hits = UNSET
        else:
            six_metre_left_post_hits = self.six_metre_left_post_hits

        six_metre_left_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_left_post_hits_per_match, Unset):
            six_metre_left_post_hits_per_match = UNSET
        else:
            six_metre_left_post_hits_per_match = self.six_metre_left_post_hits_per_match

        six_metre_left_shooting_accuracy = self.six_metre_left_shooting_accuracy

        six_metre_left_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_left_shooting_accuracy_per_match, Unset):
            six_metre_left_shooting_accuracy_per_match = UNSET
        else:
            six_metre_left_shooting_accuracy_per_match = (
                self.six_metre_left_shooting_accuracy_per_match
            )

        six_metre_left_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_left_shots, Unset):
            six_metre_left_shots = UNSET
        else:
            six_metre_left_shots = self.six_metre_left_shots

        six_metre_left_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_left_shots_per_match, Unset):
            six_metre_left_shots_per_match = UNSET
        else:
            six_metre_left_shots_per_match = self.six_metre_left_shots_per_match

        six_metre_left_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_left_shots_blocked, Unset):
            six_metre_left_shots_blocked = UNSET
        else:
            six_metre_left_shots_blocked = self.six_metre_left_shots_blocked

        six_metre_left_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_left_shots_blocked_per_match, Unset):
            six_metre_left_shots_blocked_per_match = UNSET
        else:
            six_metre_left_shots_blocked_per_match = (
                self.six_metre_left_shots_blocked_per_match
            )

        six_metre_left_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_left_shots_on_goal, Unset):
            six_metre_left_shots_on_goal = UNSET
        else:
            six_metre_left_shots_on_goal = self.six_metre_left_shots_on_goal

        six_metre_left_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_left_shots_on_goal_per_match, Unset):
            six_metre_left_shots_on_goal_per_match = UNSET
        else:
            six_metre_left_shots_on_goal_per_match = (
                self.six_metre_left_shots_on_goal_per_match
            )

        six_metre_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_missed_shots, Unset):
            six_metre_missed_shots = UNSET
        else:
            six_metre_missed_shots = self.six_metre_missed_shots

        six_metre_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_missed_shots_per_match, Unset):
            six_metre_missed_shots_per_match = UNSET
        else:
            six_metre_missed_shots_per_match = self.six_metre_missed_shots_per_match

        six_metre_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_post_hits, Unset):
            six_metre_post_hits = UNSET
        else:
            six_metre_post_hits = self.six_metre_post_hits

        six_metre_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_post_hits_per_match, Unset):
            six_metre_post_hits_per_match = UNSET
        else:
            six_metre_post_hits_per_match = self.six_metre_post_hits_per_match

        six_metre_right_goals_scored: Union[None, Unset, int]
        if isinstance(self.six_metre_right_goals_scored, Unset):
            six_metre_right_goals_scored = UNSET
        else:
            six_metre_right_goals_scored = self.six_metre_right_goals_scored

        six_metre_right_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_right_goals_scored_per_match, Unset):
            six_metre_right_goals_scored_per_match = UNSET
        else:
            six_metre_right_goals_scored_per_match = (
                self.six_metre_right_goals_scored_per_match
            )

        six_metre_right_missed_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_right_missed_shots, Unset):
            six_metre_right_missed_shots = UNSET
        else:
            six_metre_right_missed_shots = self.six_metre_right_missed_shots

        six_metre_right_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_right_missed_shots_per_match, Unset):
            six_metre_right_missed_shots_per_match = UNSET
        else:
            six_metre_right_missed_shots_per_match = (
                self.six_metre_right_missed_shots_per_match
            )

        six_metre_right_post_hits: Union[None, Unset, int]
        if isinstance(self.six_metre_right_post_hits, Unset):
            six_metre_right_post_hits = UNSET
        else:
            six_metre_right_post_hits = self.six_metre_right_post_hits

        six_metre_right_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_right_post_hits_per_match, Unset):
            six_metre_right_post_hits_per_match = UNSET
        else:
            six_metre_right_post_hits_per_match = (
                self.six_metre_right_post_hits_per_match
            )

        six_metre_right_shooting_accuracy = self.six_metre_right_shooting_accuracy

        six_metre_right_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_right_shooting_accuracy_per_match, Unset):
            six_metre_right_shooting_accuracy_per_match = UNSET
        else:
            six_metre_right_shooting_accuracy_per_match = (
                self.six_metre_right_shooting_accuracy_per_match
            )

        six_metre_right_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_right_shots, Unset):
            six_metre_right_shots = UNSET
        else:
            six_metre_right_shots = self.six_metre_right_shots

        six_metre_right_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_right_shots_per_match, Unset):
            six_metre_right_shots_per_match = UNSET
        else:
            six_metre_right_shots_per_match = self.six_metre_right_shots_per_match

        six_metre_right_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_right_shots_blocked, Unset):
            six_metre_right_shots_blocked = UNSET
        else:
            six_metre_right_shots_blocked = self.six_metre_right_shots_blocked

        six_metre_right_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_right_shots_blocked_per_match, Unset):
            six_metre_right_shots_blocked_per_match = UNSET
        else:
            six_metre_right_shots_blocked_per_match = (
                self.six_metre_right_shots_blocked_per_match
            )

        six_metre_right_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_right_shots_on_goal, Unset):
            six_metre_right_shots_on_goal = UNSET
        else:
            six_metre_right_shots_on_goal = self.six_metre_right_shots_on_goal

        six_metre_right_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_right_shots_on_goal_per_match, Unset):
            six_metre_right_shots_on_goal_per_match = UNSET
        else:
            six_metre_right_shots_on_goal_per_match = (
                self.six_metre_right_shots_on_goal_per_match
            )

        six_metre_shooting_accuracy = self.six_metre_shooting_accuracy

        six_metre_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_shooting_accuracy_per_match, Unset):
            six_metre_shooting_accuracy_per_match = UNSET
        else:
            six_metre_shooting_accuracy_per_match = (
                self.six_metre_shooting_accuracy_per_match
            )

        six_metre_shots: Union[None, Unset, int]
        if isinstance(self.six_metre_shots, Unset):
            six_metre_shots = UNSET
        else:
            six_metre_shots = self.six_metre_shots

        six_metre_shots_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_shots_per_match, Unset):
            six_metre_shots_per_match = UNSET
        else:
            six_metre_shots_per_match = self.six_metre_shots_per_match

        six_metre_shots_blocked: Union[None, Unset, int]
        if isinstance(self.six_metre_shots_blocked, Unset):
            six_metre_shots_blocked = UNSET
        else:
            six_metre_shots_blocked = self.six_metre_shots_blocked

        six_metre_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_shots_blocked_per_match, Unset):
            six_metre_shots_blocked_per_match = UNSET
        else:
            six_metre_shots_blocked_per_match = self.six_metre_shots_blocked_per_match

        six_metre_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.six_metre_shots_on_goal, Unset):
            six_metre_shots_on_goal = UNSET
        else:
            six_metre_shots_on_goal = self.six_metre_shots_on_goal

        six_metre_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.six_metre_shots_on_goal_per_match, Unset):
            six_metre_shots_on_goal_per_match = UNSET
        else:
            six_metre_shots_on_goal_per_match = self.six_metre_shots_on_goal_per_match

        speed_distance_per_time: Union[None, Unset, float]
        if isinstance(self.speed_distance_per_time, Unset):
            speed_distance_per_time = UNSET
        else:
            speed_distance_per_time = self.speed_distance_per_time

        speed_max: Union[None, Unset, float]
        if isinstance(self.speed_max, Unset):
            speed_max = UNSET
        else:
            speed_max = self.speed_max

        steals: Union[None, Unset, int]
        if isinstance(self.steals, Unset):
            steals = UNSET
        else:
            steals = self.steals

        steals_per_match: Union[None, Unset, float]
        if isinstance(self.steals_per_match, Unset):
            steals_per_match = UNSET
        else:
            steals_per_match = self.steals_per_match

        substitutions: Union[None, Unset, int]
        if isinstance(self.substitutions, Unset):
            substitutions = UNSET
        else:
            substitutions = self.substitutions

        substitutions_per_match: Union[None, Unset, float]
        if isinstance(self.substitutions_per_match, Unset):
            substitutions_per_match = UNSET
        else:
            substitutions_per_match = self.substitutions_per_match

        suspensions: Union[None, Unset, int]
        if isinstance(self.suspensions, Unset):
            suspensions = UNSET
        else:
            suspensions = self.suspensions

        suspensions_per_match: Union[None, Unset, float]
        if isinstance(self.suspensions_per_match, Unset):
            suspensions_per_match = UNSET
        else:
            suspensions_per_match = self.suspensions_per_match

        technical_ball_faults: Union[None, Unset, int]
        if isinstance(self.technical_ball_faults, Unset):
            technical_ball_faults = UNSET
        else:
            technical_ball_faults = self.technical_ball_faults

        technical_ball_faults_per_match: Union[None, Unset, float]
        if isinstance(self.technical_ball_faults_per_match, Unset):
            technical_ball_faults_per_match = UNSET
        else:
            technical_ball_faults_per_match = self.technical_ball_faults_per_match

        technical_faults: Union[None, Unset, int]
        if isinstance(self.technical_faults, Unset):
            technical_faults = UNSET
        else:
            technical_faults = self.technical_faults

        technical_faults_per_match: Union[None, Unset, float]
        if isinstance(self.technical_faults_per_match, Unset):
            technical_faults_per_match = UNSET
        else:
            technical_faults_per_match = self.technical_faults_per_match

        technical_rule_faults: Union[None, Unset, int]
        if isinstance(self.technical_rule_faults, Unset):
            technical_rule_faults = UNSET
        else:
            technical_rule_faults = self.technical_rule_faults

        technical_rule_faults_per_match: Union[None, Unset, float]
        if isinstance(self.technical_rule_faults_per_match, Unset):
            technical_rule_faults_per_match = UNSET
        else:
            technical_rule_faults_per_match = self.technical_rule_faults_per_match

        time_on_playing_field: Union[None, Unset, float, str]
        if isinstance(self.time_on_playing_field, Unset):
            time_on_playing_field = UNSET
        else:
            time_on_playing_field = self.time_on_playing_field

        time_ball_possession: Union[None, Unset, float, str]
        if isinstance(self.time_ball_possession, Unset):
            time_ball_possession = UNSET
        else:
            time_ball_possession = self.time_ball_possession

        time_played: Union[None, Unset, int]
        if isinstance(self.time_played, Unset):
            time_played = UNSET
        else:
            time_played = self.time_played

        time_played_per_match: Union[None, Unset, float]
        if isinstance(self.time_played_per_match, Unset):
            time_played_per_match = UNSET
        else:
            time_played_per_match = self.time_played_per_match

        turnovers: Union[None, Unset, int]
        if isinstance(self.turnovers, Unset):
            turnovers = UNSET
        else:
            turnovers = self.turnovers

        turnovers_per_match: Union[None, Unset, float]
        if isinstance(self.turnovers_per_match, Unset):
            turnovers_per_match = UNSET
        else:
            turnovers_per_match = self.turnovers_per_match

        two_minute_suspensions: Union[None, Unset, int]
        if isinstance(self.two_minute_suspensions, Unset):
            two_minute_suspensions = UNSET
        else:
            two_minute_suspensions = self.two_minute_suspensions

        two_minute_suspensions_per_match: Union[None, Unset, float]
        if isinstance(self.two_minute_suspensions_per_match, Unset):
            two_minute_suspensions_per_match = UNSET
        else:
            two_minute_suspensions_per_match = self.two_minute_suspensions_per_match

        wing_goals_scored: Union[None, Unset, int]
        if isinstance(self.wing_goals_scored, Unset):
            wing_goals_scored = UNSET
        else:
            wing_goals_scored = self.wing_goals_scored

        wing_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.wing_goals_scored_per_match, Unset):
            wing_goals_scored_per_match = UNSET
        else:
            wing_goals_scored_per_match = self.wing_goals_scored_per_match

        wing_left_goals_scored: Union[None, Unset, int]
        if isinstance(self.wing_left_goals_scored, Unset):
            wing_left_goals_scored = UNSET
        else:
            wing_left_goals_scored = self.wing_left_goals_scored

        wing_left_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.wing_left_goals_scored_per_match, Unset):
            wing_left_goals_scored_per_match = UNSET
        else:
            wing_left_goals_scored_per_match = self.wing_left_goals_scored_per_match

        wing_left_missed_shots: Union[None, Unset, int]
        if isinstance(self.wing_left_missed_shots, Unset):
            wing_left_missed_shots = UNSET
        else:
            wing_left_missed_shots = self.wing_left_missed_shots

        wing_left_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.wing_left_missed_shots_per_match, Unset):
            wing_left_missed_shots_per_match = UNSET
        else:
            wing_left_missed_shots_per_match = self.wing_left_missed_shots_per_match

        wing_left_post_hits: Union[None, Unset, int]
        if isinstance(self.wing_left_post_hits, Unset):
            wing_left_post_hits = UNSET
        else:
            wing_left_post_hits = self.wing_left_post_hits

        wing_left_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.wing_left_post_hits_per_match, Unset):
            wing_left_post_hits_per_match = UNSET
        else:
            wing_left_post_hits_per_match = self.wing_left_post_hits_per_match

        wing_left_shooting_accuracy = self.wing_left_shooting_accuracy

        wing_left_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.wing_left_shooting_accuracy_per_match, Unset):
            wing_left_shooting_accuracy_per_match = UNSET
        else:
            wing_left_shooting_accuracy_per_match = (
                self.wing_left_shooting_accuracy_per_match
            )

        wing_left_shots: Union[None, Unset, int]
        if isinstance(self.wing_left_shots, Unset):
            wing_left_shots = UNSET
        else:
            wing_left_shots = self.wing_left_shots

        wing_left_shots_per_match: Union[None, Unset, float]
        if isinstance(self.wing_left_shots_per_match, Unset):
            wing_left_shots_per_match = UNSET
        else:
            wing_left_shots_per_match = self.wing_left_shots_per_match

        wing_left_shots_blocked: Union[None, Unset, int]
        if isinstance(self.wing_left_shots_blocked, Unset):
            wing_left_shots_blocked = UNSET
        else:
            wing_left_shots_blocked = self.wing_left_shots_blocked

        wing_left_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.wing_left_shots_blocked_per_match, Unset):
            wing_left_shots_blocked_per_match = UNSET
        else:
            wing_left_shots_blocked_per_match = self.wing_left_shots_blocked_per_match

        wing_left_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.wing_left_shots_on_goal, Unset):
            wing_left_shots_on_goal = UNSET
        else:
            wing_left_shots_on_goal = self.wing_left_shots_on_goal

        wing_left_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.wing_left_shots_on_goal_per_match, Unset):
            wing_left_shots_on_goal_per_match = UNSET
        else:
            wing_left_shots_on_goal_per_match = self.wing_left_shots_on_goal_per_match

        wing_missed_shots: Union[None, Unset, int]
        if isinstance(self.wing_missed_shots, Unset):
            wing_missed_shots = UNSET
        else:
            wing_missed_shots = self.wing_missed_shots

        wing_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.wing_missed_shots_per_match, Unset):
            wing_missed_shots_per_match = UNSET
        else:
            wing_missed_shots_per_match = self.wing_missed_shots_per_match

        wing_post_hits: Union[None, Unset, int]
        if isinstance(self.wing_post_hits, Unset):
            wing_post_hits = UNSET
        else:
            wing_post_hits = self.wing_post_hits

        wing_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.wing_post_hits_per_match, Unset):
            wing_post_hits_per_match = UNSET
        else:
            wing_post_hits_per_match = self.wing_post_hits_per_match

        wing_right_goals_scored: Union[None, Unset, int]
        if isinstance(self.wing_right_goals_scored, Unset):
            wing_right_goals_scored = UNSET
        else:
            wing_right_goals_scored = self.wing_right_goals_scored

        wing_right_goals_scored_per_match: Union[None, Unset, float]
        if isinstance(self.wing_right_goals_scored_per_match, Unset):
            wing_right_goals_scored_per_match = UNSET
        else:
            wing_right_goals_scored_per_match = self.wing_right_goals_scored_per_match

        wing_right_missed_shots: Union[None, Unset, int]
        if isinstance(self.wing_right_missed_shots, Unset):
            wing_right_missed_shots = UNSET
        else:
            wing_right_missed_shots = self.wing_right_missed_shots

        wing_right_missed_shots_per_match: Union[None, Unset, float]
        if isinstance(self.wing_right_missed_shots_per_match, Unset):
            wing_right_missed_shots_per_match = UNSET
        else:
            wing_right_missed_shots_per_match = self.wing_right_missed_shots_per_match

        wing_right_post_hits: Union[None, Unset, int]
        if isinstance(self.wing_right_post_hits, Unset):
            wing_right_post_hits = UNSET
        else:
            wing_right_post_hits = self.wing_right_post_hits

        wing_right_post_hits_per_match: Union[None, Unset, float]
        if isinstance(self.wing_right_post_hits_per_match, Unset):
            wing_right_post_hits_per_match = UNSET
        else:
            wing_right_post_hits_per_match = self.wing_right_post_hits_per_match

        wing_right_shooting_accuracy = self.wing_right_shooting_accuracy

        wing_right_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.wing_right_shooting_accuracy_per_match, Unset):
            wing_right_shooting_accuracy_per_match = UNSET
        else:
            wing_right_shooting_accuracy_per_match = (
                self.wing_right_shooting_accuracy_per_match
            )

        wing_right_shots: Union[None, Unset, int]
        if isinstance(self.wing_right_shots, Unset):
            wing_right_shots = UNSET
        else:
            wing_right_shots = self.wing_right_shots

        wing_right_shots_per_match: Union[None, Unset, float]
        if isinstance(self.wing_right_shots_per_match, Unset):
            wing_right_shots_per_match = UNSET
        else:
            wing_right_shots_per_match = self.wing_right_shots_per_match

        wing_right_shots_blocked: Union[None, Unset, int]
        if isinstance(self.wing_right_shots_blocked, Unset):
            wing_right_shots_blocked = UNSET
        else:
            wing_right_shots_blocked = self.wing_right_shots_blocked

        wing_right_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.wing_right_shots_blocked_per_match, Unset):
            wing_right_shots_blocked_per_match = UNSET
        else:
            wing_right_shots_blocked_per_match = self.wing_right_shots_blocked_per_match

        wing_right_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.wing_right_shots_on_goal, Unset):
            wing_right_shots_on_goal = UNSET
        else:
            wing_right_shots_on_goal = self.wing_right_shots_on_goal

        wing_right_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.wing_right_shots_on_goal_per_match, Unset):
            wing_right_shots_on_goal_per_match = UNSET
        else:
            wing_right_shots_on_goal_per_match = self.wing_right_shots_on_goal_per_match

        wing_shooting_accuracy = self.wing_shooting_accuracy

        wing_shooting_accuracy_per_match: Union[None, Unset, float]
        if isinstance(self.wing_shooting_accuracy_per_match, Unset):
            wing_shooting_accuracy_per_match = UNSET
        else:
            wing_shooting_accuracy_per_match = self.wing_shooting_accuracy_per_match

        wing_shots: Union[None, Unset, int]
        if isinstance(self.wing_shots, Unset):
            wing_shots = UNSET
        else:
            wing_shots = self.wing_shots

        wing_shots_per_match: Union[None, Unset, float]
        if isinstance(self.wing_shots_per_match, Unset):
            wing_shots_per_match = UNSET
        else:
            wing_shots_per_match = self.wing_shots_per_match

        wing_shots_blocked: Union[None, Unset, int]
        if isinstance(self.wing_shots_blocked, Unset):
            wing_shots_blocked = UNSET
        else:
            wing_shots_blocked = self.wing_shots_blocked

        wing_shots_blocked_per_match: Union[None, Unset, float]
        if isinstance(self.wing_shots_blocked_per_match, Unset):
            wing_shots_blocked_per_match = UNSET
        else:
            wing_shots_blocked_per_match = self.wing_shots_blocked_per_match

        wing_shots_on_goal: Union[None, Unset, int]
        if isinstance(self.wing_shots_on_goal, Unset):
            wing_shots_on_goal = UNSET
        else:
            wing_shots_on_goal = self.wing_shots_on_goal

        wing_shots_on_goal_per_match: Union[None, Unset, float]
        if isinstance(self.wing_shots_on_goal_per_match, Unset):
            wing_shots_on_goal_per_match = UNSET
        else:
            wing_shots_on_goal_per_match = self.wing_shots_on_goal_per_match

        wins: Union[None, Unset, int]
        if isinstance(self.wins, Unset):
            wins = UNSET
        else:
            wins = self.wins

        yellow_cards: Union[None, Unset, int]
        if isinstance(self.yellow_cards, Unset):
            yellow_cards = UNSET
        else:
            yellow_cards = self.yellow_cards

        yellow_cards_per_match: Union[None, Unset, float]
        if isinstance(self.yellow_cards_per_match, Unset):
            yellow_cards_per_match = UNSET
        else:
            yellow_cards_per_match = self.yellow_cards_per_match

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if airtime_max is not UNSET:
            field_dict["airtimeMax"] = airtime_max
        if assists is not UNSET:
            field_dict["assists"] = assists
        if assists_per_match is not UNSET:
            field_dict["assistsPerMatch"] = assists_per_match
        if back_court_goals_scored is not UNSET:
            field_dict["backCourtGoalsScored"] = back_court_goals_scored
        if back_court_goals_scored_per_match is not UNSET:
            field_dict["backCourtGoalsScoredPerMatch"] = (
                back_court_goals_scored_per_match
            )
        if back_court_missed_shots is not UNSET:
            field_dict["backCourtMissedShots"] = back_court_missed_shots
        if back_court_missed_shots_per_match is not UNSET:
            field_dict["backCourtMissedShotsPerMatch"] = (
                back_court_missed_shots_per_match
            )
        if back_court_post_hits is not UNSET:
            field_dict["backCourtPostHits"] = back_court_post_hits
        if back_court_post_hits_per_match is not UNSET:
            field_dict["backCourtPostHitsPerMatch"] = back_court_post_hits_per_match
        if back_court_shooting_accuracy is not UNSET:
            field_dict["backCourtShootingAccuracy"] = back_court_shooting_accuracy
        if back_court_shooting_accuracy_per_match is not UNSET:
            field_dict["backCourtShootingAccuracyPerMatch"] = (
                back_court_shooting_accuracy_per_match
            )
        if back_court_shots is not UNSET:
            field_dict["backCourtShots"] = back_court_shots
        if back_court_shots_per_match is not UNSET:
            field_dict["backCourtShotsPerMatch"] = back_court_shots_per_match
        if back_court_shots_blocked is not UNSET:
            field_dict["backCourtShotsBlocked"] = back_court_shots_blocked
        if back_court_shots_blocked_per_match is not UNSET:
            field_dict["backCourtShotsBlockedPerMatch"] = (
                back_court_shots_blocked_per_match
            )
        if back_court_shots_on_goal is not UNSET:
            field_dict["backCourtShotsOnGoal"] = back_court_shots_on_goal
        if back_court_shots_on_goal_per_match is not UNSET:
            field_dict["backCourtShotsOnGoalPerMatch"] = (
                back_court_shots_on_goal_per_match
            )
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if blocks_per_match is not UNSET:
            field_dict["blocksPerMatch"] = blocks_per_match
        if blue_cards is not UNSET:
            field_dict["blueCards"] = blue_cards
        if blue_cards_per_match is not UNSET:
            field_dict["blueCardsPerMatch"] = blue_cards_per_match
        if break_through_goals_scored is not UNSET:
            field_dict["breakThroughGoalsScored"] = break_through_goals_scored
        if break_through_goals_scored_per_match is not UNSET:
            field_dict["breakThroughGoalsScoredPerMatch"] = (
                break_through_goals_scored_per_match
            )
        if break_through_missed_shots is not UNSET:
            field_dict["breakThroughMissedShots"] = break_through_missed_shots
        if break_through_missed_shots_per_match is not UNSET:
            field_dict["breakThroughMissedShotsPerMatch"] = (
                break_through_missed_shots_per_match
            )
        if break_through_post_hits is not UNSET:
            field_dict["breakThroughPostHits"] = break_through_post_hits
        if break_through_post_hits_per_match is not UNSET:
            field_dict["breakThroughPostHitsPerMatch"] = (
                break_through_post_hits_per_match
            )
        if break_through_shooting_accuracy is not UNSET:
            field_dict["breakThroughShootingAccuracy"] = break_through_shooting_accuracy
        if break_through_shooting_accuracy_per_match is not UNSET:
            field_dict["breakThroughShootingAccuracyPerMatch"] = (
                break_through_shooting_accuracy_per_match
            )
        if break_through_shots is not UNSET:
            field_dict["breakThroughShots"] = break_through_shots
        if break_through_shots_per_match is not UNSET:
            field_dict["breakThroughShotsPerMatch"] = break_through_shots_per_match
        if break_through_shots_blocked is not UNSET:
            field_dict["breakThroughShotsBlocked"] = break_through_shots_blocked
        if break_through_shots_blocked_per_match is not UNSET:
            field_dict["breakThroughShotsBlockedPerMatch"] = (
                break_through_shots_blocked_per_match
            )
        if break_through_shots_on_goal is not UNSET:
            field_dict["breakThroughShotsOnGoal"] = break_through_shots_on_goal
        if break_through_shots_on_goal_per_match is not UNSET:
            field_dict["breakThroughShotsOnGoalPerMatch"] = (
                break_through_shots_on_goal_per_match
            )
        if cards is not UNSET:
            field_dict["cards"] = cards
        if cards_per_match is not UNSET:
            field_dict["cardsPerMatch"] = cards_per_match
        if distance_speed_category_1 is not UNSET:
            field_dict["distanceSpeedCategory1"] = distance_speed_category_1
        if distance_speed_category_2 is not UNSET:
            field_dict["distanceSpeedCategory2"] = distance_speed_category_2
        if distance_speed_category_3 is not UNSET:
            field_dict["distanceSpeedCategory3"] = distance_speed_category_3
        if distance_speed_category_4 is not UNSET:
            field_dict["distanceSpeedCategory4"] = distance_speed_category_4
        if distance_speed_category_5 is not UNSET:
            field_dict["distanceSpeedCategory5"] = distance_speed_category_5
        if distance_total is not UNSET:
            field_dict["distanceTotal"] = distance_total
        if draws is not UNSET:
            field_dict["draws"] = draws
        if empty_net_goals_scored is not UNSET:
            field_dict["emptyNetGoalsScored"] = empty_net_goals_scored
        if fast_break_goals_scored is not UNSET:
            field_dict["fastBreakGoalsScored"] = fast_break_goals_scored
        if fast_break_goals_scored_per_match is not UNSET:
            field_dict["fastBreakGoalsScoredPerMatch"] = (
                fast_break_goals_scored_per_match
            )
        if fast_break_missed_shots is not UNSET:
            field_dict["fastBreakMissedShots"] = fast_break_missed_shots
        if fast_break_missed_shots_per_match is not UNSET:
            field_dict["fastBreakMissedShotsPerMatch"] = (
                fast_break_missed_shots_per_match
            )
        if fast_break_post_hits is not UNSET:
            field_dict["fastBreakPostHits"] = fast_break_post_hits
        if fast_break_post_hits_per_match is not UNSET:
            field_dict["fastBreakPostHitsPerMatch"] = fast_break_post_hits_per_match
        if fast_break_shooting_accuracy is not UNSET:
            field_dict["fastBreakShootingAccuracy"] = fast_break_shooting_accuracy
        if fast_break_shooting_accuracy_per_match is not UNSET:
            field_dict["fastBreakShootingAccuracyPerMatch"] = (
                fast_break_shooting_accuracy_per_match
            )
        if fast_break_shots is not UNSET:
            field_dict["fastBreakShots"] = fast_break_shots
        if fast_break_shots_per_match is not UNSET:
            field_dict["fastBreakShotsPerMatch"] = fast_break_shots_per_match
        if fast_break_shots_blocked is not UNSET:
            field_dict["fastBreakShotsBlocked"] = fast_break_shots_blocked
        if fast_break_shots_blocked_per_match is not UNSET:
            field_dict["fastBreakShotsBlockedPerMatch"] = (
                fast_break_shots_blocked_per_match
            )
        if fast_break_shots_on_goal is not UNSET:
            field_dict["fastBreakShotsOnGoal"] = fast_break_shots_on_goal
        if fast_break_shots_on_goal_per_match is not UNSET:
            field_dict["fastBreakShotsOnGoalPerMatch"] = (
                fast_break_shots_on_goal_per_match
            )
        if field_goals_scored is not UNSET:
            field_dict["fieldGoalsScored"] = field_goals_scored
        if field_goals_scored_per_match is not UNSET:
            field_dict["fieldGoalsScoredPerMatch"] = field_goals_scored_per_match
        if field_missed_shots is not UNSET:
            field_dict["fieldMissedShots"] = field_missed_shots
        if field_missed_shots_per_match is not UNSET:
            field_dict["fieldMissedShotsPerMatch"] = field_missed_shots_per_match
        if field_post_hits is not UNSET:
            field_dict["fieldPostHits"] = field_post_hits
        if field_post_hits_per_match is not UNSET:
            field_dict["fieldPostHitsPerMatch"] = field_post_hits_per_match
        if field_shooting_accuracy is not UNSET:
            field_dict["fieldShootingAccuracy"] = field_shooting_accuracy
        if field_shooting_accuracy_per_match is not UNSET:
            field_dict["fieldShootingAccuracyPerMatch"] = (
                field_shooting_accuracy_per_match
            )
        if field_shots is not UNSET:
            field_dict["fieldShots"] = field_shots
        if field_shots_per_match is not UNSET:
            field_dict["fieldShotsPerMatch"] = field_shots_per_match
        if field_shots_blocked is not UNSET:
            field_dict["fieldShotsBlocked"] = field_shots_blocked
        if field_shots_blocked_per_match is not UNSET:
            field_dict["fieldShotsBlockedPerMatch"] = field_shots_blocked_per_match
        if field_shots_on_goal is not UNSET:
            field_dict["fieldShotsOnGoal"] = field_shots_on_goal
        if field_shots_on_goal_per_match is not UNSET:
            field_dict["fieldShotsOnGoalPerMatch"] = field_shots_on_goal_per_match
        if fouls is not UNSET:
            field_dict["fouls"] = fouls
        if fouls_per_match is not UNSET:
            field_dict["foulsPerMatch"] = fouls_per_match
        if fouls_drawn is not UNSET:
            field_dict["foulsDrawn"] = fouls_drawn
        if fouls_drawn_per_match is not UNSET:
            field_dict["foulsDrawnPerMatch"] = fouls_drawn_per_match
        if four_minute_suspensions is not UNSET:
            field_dict["fourMinuteSuspensions"] = four_minute_suspensions
        if four_minute_suspensions_per_match is not UNSET:
            field_dict["fourMinuteSuspensionsPerMatch"] = (
                four_minute_suspensions_per_match
            )
        if games is not UNSET:
            field_dict["games"] = games
        if games_started is not UNSET:
            field_dict["gamesStarted"] = games_started
        if goal_keeper_back_court_goals_against is not UNSET:
            field_dict["goalKeeperBackCourtGoalsAgainst"] = (
                goal_keeper_back_court_goals_against
            )
        if goal_keeper_back_court_goals_against_per_match is not UNSET:
            field_dict["goalKeeperBackCourtGoalsAgainstPerMatch"] = (
                goal_keeper_back_court_goals_against_per_match
            )
        if goal_keeper_back_court_save_accuracy is not UNSET:
            field_dict["goalKeeperBackCourtSaveAccuracy"] = (
                goal_keeper_back_court_save_accuracy
            )
        if goal_keeper_back_court_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperBackCourtSaveAccuracyPerMatch"] = (
                goal_keeper_back_court_save_accuracy_per_match
            )
        if goal_keeper_back_court_shots_against is not UNSET:
            field_dict["goalKeeperBackCourtShotsAgainst"] = (
                goal_keeper_back_court_shots_against
            )
        if goal_keeper_back_court_shots_against_per_match is not UNSET:
            field_dict["goalKeeperBackCourtShotsAgainstPerMatch"] = (
                goal_keeper_back_court_shots_against_per_match
            )
        if goal_keeper_back_court_shots_saved is not UNSET:
            field_dict["goalKeeperBackCourtShotsSaved"] = (
                goal_keeper_back_court_shots_saved
            )
        if goal_keeper_back_court_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperBackCourtShotsSavedPerMatch"] = (
                goal_keeper_back_court_shots_saved_per_match
            )
        if goal_keeper_break_through_goals_against is not UNSET:
            field_dict["goalKeeperBreakThroughGoalsAgainst"] = (
                goal_keeper_break_through_goals_against
            )
        if goal_keeper_break_through_goals_against_per_match is not UNSET:
            field_dict["goalKeeperBreakThroughGoalsAgainstPerMatch"] = (
                goal_keeper_break_through_goals_against_per_match
            )
        if goal_keeper_break_through_save_accuracy is not UNSET:
            field_dict["goalKeeperBreakThroughSaveAccuracy"] = (
                goal_keeper_break_through_save_accuracy
            )
        if goal_keeper_break_through_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperBreakThroughSaveAccuracyPerMatch"] = (
                goal_keeper_break_through_save_accuracy_per_match
            )
        if goal_keeper_break_through_shots_against is not UNSET:
            field_dict["goalKeeperBreakThroughShotsAgainst"] = (
                goal_keeper_break_through_shots_against
            )
        if goal_keeper_break_through_shots_against_per_match is not UNSET:
            field_dict["goalKeeperBreakThroughShotsAgainstPerMatch"] = (
                goal_keeper_break_through_shots_against_per_match
            )
        if goal_keeper_break_through_shots_saved is not UNSET:
            field_dict["goalKeeperBreakThroughShotsSaved"] = (
                goal_keeper_break_through_shots_saved
            )
        if goal_keeper_break_through_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperBreakThroughShotsSavedPerMatch"] = (
                goal_keeper_break_through_shots_saved_per_match
            )
        if goal_keeper_fast_break_goals_against is not UNSET:
            field_dict["goalKeeperFastBreakGoalsAgainst"] = (
                goal_keeper_fast_break_goals_against
            )
        if goal_keeper_fast_break_goals_against_per_match is not UNSET:
            field_dict["goalKeeperFastBreakGoalsAgainstPerMatch"] = (
                goal_keeper_fast_break_goals_against_per_match
            )
        if goal_keeper_fast_break_save_accuracy is not UNSET:
            field_dict["goalKeeperFastBreakSaveAccuracy"] = (
                goal_keeper_fast_break_save_accuracy
            )
        if goal_keeper_fast_break_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperFastBreakSaveAccuracyPerMatch"] = (
                goal_keeper_fast_break_save_accuracy_per_match
            )
        if goal_keeper_fast_break_shots_against is not UNSET:
            field_dict["goalKeeperFastBreakShotsAgainst"] = (
                goal_keeper_fast_break_shots_against
            )
        if goal_keeper_fast_break_shots_against_per_match is not UNSET:
            field_dict["goalKeeperFastBreakShotsAgainstPerMatch"] = (
                goal_keeper_fast_break_shots_against_per_match
            )
        if goal_keeper_fast_break_shots_saved is not UNSET:
            field_dict["goalKeeperFastBreakShotsSaved"] = (
                goal_keeper_fast_break_shots_saved
            )
        if goal_keeper_fast_break_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperFastBreakShotsSavedPerMatch"] = (
                goal_keeper_fast_break_shots_saved_per_match
            )
        if goal_keeper_field_goals_against is not UNSET:
            field_dict["goalKeeperFieldGoalsAgainst"] = goal_keeper_field_goals_against
        if goal_keeper_field_goals_against_per_match is not UNSET:
            field_dict["goalKeeperFieldGoalsAgainstPerMatch"] = (
                goal_keeper_field_goals_against_per_match
            )
        if goal_keeper_field_save_accuracy is not UNSET:
            field_dict["goalKeeperFieldSaveAccuracy"] = goal_keeper_field_save_accuracy
        if goal_keeper_field_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperFieldSaveAccuracyPerMatch"] = (
                goal_keeper_field_save_accuracy_per_match
            )
        if goal_keeper_field_shots_against is not UNSET:
            field_dict["goalKeeperFieldShotsAgainst"] = goal_keeper_field_shots_against
        if goal_keeper_field_shots_against_per_match is not UNSET:
            field_dict["goalKeeperFieldShotsAgainstPerMatch"] = (
                goal_keeper_field_shots_against_per_match
            )
        if goal_keeper_field_shots_saved is not UNSET:
            field_dict["goalKeeperFieldShotsSaved"] = goal_keeper_field_shots_saved
        if goal_keeper_field_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperFieldShotsSavedPerMatch"] = (
                goal_keeper_field_shots_saved_per_match
            )
        if goal_keeper_goals_against is not UNSET:
            field_dict["goalKeeperGoalsAgainst"] = goal_keeper_goals_against
        if goal_keeper_goals_against_per_match is not UNSET:
            field_dict["goalKeeperGoalsAgainstPerMatch"] = (
                goal_keeper_goals_against_per_match
            )
        if goal_keeper_nine_metre_centre_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreCentreGoalsAgainst"] = (
                goal_keeper_nine_metre_centre_goals_against
            )
        if goal_keeper_nine_metre_centre_goals_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreCentreGoalsAgainstPerMatch"] = (
                goal_keeper_nine_metre_centre_goals_against_per_match
            )
        if goal_keeper_nine_metre_centre_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreCentreSaveAccuracy"] = (
                goal_keeper_nine_metre_centre_save_accuracy
            )
        if goal_keeper_nine_metre_centre_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperNineMetreCentreSaveAccuracyPerMatch"] = (
                goal_keeper_nine_metre_centre_save_accuracy_per_match
            )
        if goal_keeper_nine_metre_centre_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreCentreShotsAgainst"] = (
                goal_keeper_nine_metre_centre_shots_against
            )
        if goal_keeper_nine_metre_centre_shots_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreCentreShotsAgainstPerMatch"] = (
                goal_keeper_nine_metre_centre_shots_against_per_match
            )
        if goal_keeper_nine_metre_centre_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreCentreShotsSaved"] = (
                goal_keeper_nine_metre_centre_shots_saved
            )
        if goal_keeper_nine_metre_centre_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperNineMetreCentreShotsSavedPerMatch"] = (
                goal_keeper_nine_metre_centre_shots_saved_per_match
            )
        if goal_keeper_nine_metre_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreGoalsAgainst"] = (
                goal_keeper_nine_metre_goals_against
            )
        if goal_keeper_nine_metre_goals_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreGoalsAgainstPerMatch"] = (
                goal_keeper_nine_metre_goals_against_per_match
            )
        if goal_keeper_nine_metre_left_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreLeftGoalsAgainst"] = (
                goal_keeper_nine_metre_left_goals_against
            )
        if goal_keeper_nine_metre_left_goals_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreLeftGoalsAgainstPerMatch"] = (
                goal_keeper_nine_metre_left_goals_against_per_match
            )
        if goal_keeper_nine_metre_left_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreLeftSaveAccuracy"] = (
                goal_keeper_nine_metre_left_save_accuracy
            )
        if goal_keeper_nine_metre_left_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperNineMetreLeftSaveAccuracyPerMatch"] = (
                goal_keeper_nine_metre_left_save_accuracy_per_match
            )
        if goal_keeper_nine_metre_left_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreLeftShotsAgainst"] = (
                goal_keeper_nine_metre_left_shots_against
            )
        if goal_keeper_nine_metre_left_shots_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreLeftShotsAgainstPerMatch"] = (
                goal_keeper_nine_metre_left_shots_against_per_match
            )
        if goal_keeper_nine_metre_left_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreLeftShotsSaved"] = (
                goal_keeper_nine_metre_left_shots_saved
            )
        if goal_keeper_nine_metre_left_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperNineMetreLeftShotsSavedPerMatch"] = (
                goal_keeper_nine_metre_left_shots_saved_per_match
            )
        if goal_keeper_nine_metre_right_goals_against is not UNSET:
            field_dict["goalKeeperNineMetreRightGoalsAgainst"] = (
                goal_keeper_nine_metre_right_goals_against
            )
        if goal_keeper_nine_metre_right_goals_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreRightGoalsAgainstPerMatch"] = (
                goal_keeper_nine_metre_right_goals_against_per_match
            )
        if goal_keeper_nine_metre_right_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreRightSaveAccuracy"] = (
                goal_keeper_nine_metre_right_save_accuracy
            )
        if goal_keeper_nine_metre_right_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperNineMetreRightSaveAccuracyPerMatch"] = (
                goal_keeper_nine_metre_right_save_accuracy_per_match
            )
        if goal_keeper_nine_metre_right_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreRightShotsAgainst"] = (
                goal_keeper_nine_metre_right_shots_against
            )
        if goal_keeper_nine_metre_right_shots_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreRightShotsAgainstPerMatch"] = (
                goal_keeper_nine_metre_right_shots_against_per_match
            )
        if goal_keeper_nine_metre_right_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreRightShotsSaved"] = (
                goal_keeper_nine_metre_right_shots_saved
            )
        if goal_keeper_nine_metre_right_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperNineMetreRightShotsSavedPerMatch"] = (
                goal_keeper_nine_metre_right_shots_saved_per_match
            )
        if goal_keeper_nine_metre_save_accuracy is not UNSET:
            field_dict["goalKeeperNineMetreSaveAccuracy"] = (
                goal_keeper_nine_metre_save_accuracy
            )
        if goal_keeper_nine_metre_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperNineMetreSaveAccuracyPerMatch"] = (
                goal_keeper_nine_metre_save_accuracy_per_match
            )
        if goal_keeper_nine_metre_shots_against is not UNSET:
            field_dict["goalKeeperNineMetreShotsAgainst"] = (
                goal_keeper_nine_metre_shots_against
            )
        if goal_keeper_nine_metre_shots_against_per_match is not UNSET:
            field_dict["goalKeeperNineMetreShotsAgainstPerMatch"] = (
                goal_keeper_nine_metre_shots_against_per_match
            )
        if goal_keeper_nine_metre_shots_saved is not UNSET:
            field_dict["goalKeeperNineMetreShotsSaved"] = (
                goal_keeper_nine_metre_shots_saved
            )
        if goal_keeper_nine_metre_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperNineMetreShotsSavedPerMatch"] = (
                goal_keeper_nine_metre_shots_saved_per_match
            )
        if goal_keeper_pivot_goals_against is not UNSET:
            field_dict["goalKeeperPivotGoalsAgainst"] = goal_keeper_pivot_goals_against
        if goal_keeper_pivot_goals_against_per_match is not UNSET:
            field_dict["goalKeeperPivotGoalsAgainstPerMatch"] = (
                goal_keeper_pivot_goals_against_per_match
            )
        if goal_keeper_pivot_save_accuracy is not UNSET:
            field_dict["goalKeeperPivotSaveAccuracy"] = goal_keeper_pivot_save_accuracy
        if goal_keeper_pivot_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperPivotSaveAccuracyPerMatch"] = (
                goal_keeper_pivot_save_accuracy_per_match
            )
        if goal_keeper_pivot_shots_against is not UNSET:
            field_dict["goalKeeperPivotShotsAgainst"] = goal_keeper_pivot_shots_against
        if goal_keeper_pivot_shots_against_per_match is not UNSET:
            field_dict["goalKeeperPivotShotsAgainstPerMatch"] = (
                goal_keeper_pivot_shots_against_per_match
            )
        if goal_keeper_pivot_shots_saved is not UNSET:
            field_dict["goalKeeperPivotShotsSaved"] = goal_keeper_pivot_shots_saved
        if goal_keeper_pivot_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperPivotShotsSavedPerMatch"] = (
                goal_keeper_pivot_shots_saved_per_match
            )
        if goal_keeper_save_accuracy is not UNSET:
            field_dict["goalKeeperSaveAccuracy"] = goal_keeper_save_accuracy
        if goal_keeper_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperSaveAccuracyPerMatch"] = (
                goal_keeper_save_accuracy_per_match
            )
        if goal_keeper_seconds_played is not UNSET:
            field_dict["goalKeeperSecondsPlayed"] = goal_keeper_seconds_played
        if goal_keeper_seconds_played_per_match is not UNSET:
            field_dict["goalKeeperSecondsPlayedPerMatch"] = (
                goal_keeper_seconds_played_per_match
            )
        if goal_keeper_seven_metre_goals_against is not UNSET:
            field_dict["goalKeeperSevenMetreGoalsAgainst"] = (
                goal_keeper_seven_metre_goals_against
            )
        if goal_keeper_seven_metre_goals_against_per_match is not UNSET:
            field_dict["goalKeeperSevenMetreGoalsAgainstPerMatch"] = (
                goal_keeper_seven_metre_goals_against_per_match
            )
        if goal_keeper_seven_metre_save_accuracy is not UNSET:
            field_dict["goalKeeperSevenMetreSaveAccuracy"] = (
                goal_keeper_seven_metre_save_accuracy
            )
        if goal_keeper_seven_metre_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperSevenMetreSaveAccuracyPerMatch"] = (
                goal_keeper_seven_metre_save_accuracy_per_match
            )
        if goal_keeper_seven_metre_shots_against is not UNSET:
            field_dict["goalKeeperSevenMetreShotsAgainst"] = (
                goal_keeper_seven_metre_shots_against
            )
        if goal_keeper_seven_metre_shots_against_per_match is not UNSET:
            field_dict["goalKeeperSevenMetreShotsAgainstPerMatch"] = (
                goal_keeper_seven_metre_shots_against_per_match
            )
        if goal_keeper_seven_metre_shots_saved is not UNSET:
            field_dict["goalKeeperSevenMetreShotsSaved"] = (
                goal_keeper_seven_metre_shots_saved
            )
        if goal_keeper_seven_metre_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperSevenMetreShotsSavedPerMatch"] = (
                goal_keeper_seven_metre_shots_saved_per_match
            )
        if goal_keeper_shots_against is not UNSET:
            field_dict["goalKeeperShotsAgainst"] = goal_keeper_shots_against
        if goal_keeper_shots_against_per_match is not UNSET:
            field_dict["goalKeeperShotsAgainstPerMatch"] = (
                goal_keeper_shots_against_per_match
            )
        if goal_keeper_shots_per_goals_against is not UNSET:
            field_dict["goalKeeperShotsPerGoalsAgainst"] = (
                goal_keeper_shots_per_goals_against
            )
        if goal_keeper_shots_saved is not UNSET:
            field_dict["goalKeeperShotsSaved"] = goal_keeper_shots_saved
        if goal_keeper_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperShotsSavedPerMatch"] = (
                goal_keeper_shots_saved_per_match
            )
        if goal_keeper_six_metre_centre_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreCentreGoalsAgainst"] = (
                goal_keeper_six_metre_centre_goals_against
            )
        if goal_keeper_six_metre_centre_goals_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreCentreGoalsAgainstPerMatch"] = (
                goal_keeper_six_metre_centre_goals_against_per_match
            )
        if goal_keeper_six_metre_centre_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreCentreSaveAccuracy"] = (
                goal_keeper_six_metre_centre_save_accuracy
            )
        if goal_keeper_six_metre_centre_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperSixMetreCentreSaveAccuracyPerMatch"] = (
                goal_keeper_six_metre_centre_save_accuracy_per_match
            )
        if goal_keeper_six_metre_centre_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreCentreShotsAgainst"] = (
                goal_keeper_six_metre_centre_shots_against
            )
        if goal_keeper_six_metre_centre_shots_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreCentreShotsAgainstPerMatch"] = (
                goal_keeper_six_metre_centre_shots_against_per_match
            )
        if goal_keeper_six_metre_centre_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreCentreShotsSaved"] = (
                goal_keeper_six_metre_centre_shots_saved
            )
        if goal_keeper_six_metre_centre_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperSixMetreCentreShotsSavedPerMatch"] = (
                goal_keeper_six_metre_centre_shots_saved_per_match
            )
        if goal_keeper_six_metre_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreGoalsAgainst"] = (
                goal_keeper_six_metre_goals_against
            )
        if goal_keeper_six_metre_goals_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreGoalsAgainstPerMatch"] = (
                goal_keeper_six_metre_goals_against_per_match
            )
        if goal_keeper_six_metre_left_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreLeftGoalsAgainst"] = (
                goal_keeper_six_metre_left_goals_against
            )
        if goal_keeper_six_metre_left_goals_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreLeftGoalsAgainstPerMatch"] = (
                goal_keeper_six_metre_left_goals_against_per_match
            )
        if goal_keeper_six_metre_left_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreLeftSaveAccuracy"] = (
                goal_keeper_six_metre_left_save_accuracy
            )
        if goal_keeper_six_metre_left_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperSixMetreLeftSaveAccuracyPerMatch"] = (
                goal_keeper_six_metre_left_save_accuracy_per_match
            )
        if goal_keeper_six_metre_left_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreLeftShotsAgainst"] = (
                goal_keeper_six_metre_left_shots_against
            )
        if goal_keeper_six_metre_left_shots_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreLeftShotsAgainstPerMatch"] = (
                goal_keeper_six_metre_left_shots_against_per_match
            )
        if goal_keeper_six_metre_left_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreLeftShotsSaved"] = (
                goal_keeper_six_metre_left_shots_saved
            )
        if goal_keeper_six_metre_left_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperSixMetreLeftShotsSavedPerMatch"] = (
                goal_keeper_six_metre_left_shots_saved_per_match
            )
        if goal_keeper_six_metre_right_goals_against is not UNSET:
            field_dict["goalKeeperSixMetreRightGoalsAgainst"] = (
                goal_keeper_six_metre_right_goals_against
            )
        if goal_keeper_six_metre_right_goals_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreRightGoalsAgainstPerMatch"] = (
                goal_keeper_six_metre_right_goals_against_per_match
            )
        if goal_keeper_six_metre_right_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreRightSaveAccuracy"] = (
                goal_keeper_six_metre_right_save_accuracy
            )
        if goal_keeper_six_metre_right_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperSixMetreRightSaveAccuracyPerMatch"] = (
                goal_keeper_six_metre_right_save_accuracy_per_match
            )
        if goal_keeper_six_metre_right_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreRightShotsAgainst"] = (
                goal_keeper_six_metre_right_shots_against
            )
        if goal_keeper_six_metre_right_shots_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreRightShotsAgainstPerMatch"] = (
                goal_keeper_six_metre_right_shots_against_per_match
            )
        if goal_keeper_six_metre_right_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreRightShotsSaved"] = (
                goal_keeper_six_metre_right_shots_saved
            )
        if goal_keeper_six_metre_right_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperSixMetreRightShotsSavedPerMatch"] = (
                goal_keeper_six_metre_right_shots_saved_per_match
            )
        if goal_keeper_six_metre_save_accuracy is not UNSET:
            field_dict["goalKeeperSixMetreSaveAccuracy"] = (
                goal_keeper_six_metre_save_accuracy
            )
        if goal_keeper_six_metre_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperSixMetreSaveAccuracyPerMatch"] = (
                goal_keeper_six_metre_save_accuracy_per_match
            )
        if goal_keeper_six_metre_shots_against is not UNSET:
            field_dict["goalKeeperSixMetreShotsAgainst"] = (
                goal_keeper_six_metre_shots_against
            )
        if goal_keeper_six_metre_shots_against_per_match is not UNSET:
            field_dict["goalKeeperSixMetreShotsAgainstPerMatch"] = (
                goal_keeper_six_metre_shots_against_per_match
            )
        if goal_keeper_six_metre_shots_saved is not UNSET:
            field_dict["goalKeeperSixMetreShotsSaved"] = (
                goal_keeper_six_metre_shots_saved
            )
        if goal_keeper_six_metre_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperSixMetreShotsSavedPerMatch"] = (
                goal_keeper_six_metre_shots_saved_per_match
            )
        if goal_keeper_wing_goals_against is not UNSET:
            field_dict["goalKeeperWingGoalsAgainst"] = goal_keeper_wing_goals_against
        if goal_keeper_wing_goals_against_per_match is not UNSET:
            field_dict["goalKeeperWingGoalsAgainstPerMatch"] = (
                goal_keeper_wing_goals_against_per_match
            )
        if goal_keeper_wing_left_goals_against is not UNSET:
            field_dict["goalKeeperWingLeftGoalsAgainst"] = (
                goal_keeper_wing_left_goals_against
            )
        if goal_keeper_wing_left_goals_against_per_match is not UNSET:
            field_dict["goalKeeperWingLeftGoalsAgainstPerMatch"] = (
                goal_keeper_wing_left_goals_against_per_match
            )
        if goal_keeper_wing_left_save_accuracy is not UNSET:
            field_dict["goalKeeperWingLeftSaveAccuracy"] = (
                goal_keeper_wing_left_save_accuracy
            )
        if goal_keeper_wing_left_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperWingLeftSaveAccuracyPerMatch"] = (
                goal_keeper_wing_left_save_accuracy_per_match
            )
        if goal_keeper_wing_left_shots_against is not UNSET:
            field_dict["goalKeeperWingLeftShotsAgainst"] = (
                goal_keeper_wing_left_shots_against
            )
        if goal_keeper_wing_left_shots_against_per_match is not UNSET:
            field_dict["goalKeeperWingLeftShotsAgainstPerMatch"] = (
                goal_keeper_wing_left_shots_against_per_match
            )
        if goal_keeper_wing_left_shots_saved is not UNSET:
            field_dict["goalKeeperWingLeftShotsSaved"] = (
                goal_keeper_wing_left_shots_saved
            )
        if goal_keeper_wing_left_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperWingLeftShotsSavedPerMatch"] = (
                goal_keeper_wing_left_shots_saved_per_match
            )
        if goal_keeper_wing_right_goals_against is not UNSET:
            field_dict["goalKeeperWingRightGoalsAgainst"] = (
                goal_keeper_wing_right_goals_against
            )
        if goal_keeper_wing_right_goals_against_per_match is not UNSET:
            field_dict["goalKeeperWingRightGoalsAgainstPerMatch"] = (
                goal_keeper_wing_right_goals_against_per_match
            )
        if goal_keeper_wing_right_save_accuracy is not UNSET:
            field_dict["goalKeeperWingRightSaveAccuracy"] = (
                goal_keeper_wing_right_save_accuracy
            )
        if goal_keeper_wing_right_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperWingRightSaveAccuracyPerMatch"] = (
                goal_keeper_wing_right_save_accuracy_per_match
            )
        if goal_keeper_wing_right_shots_against is not UNSET:
            field_dict["goalKeeperWingRightShotsAgainst"] = (
                goal_keeper_wing_right_shots_against
            )
        if goal_keeper_wing_right_shots_against_per_match is not UNSET:
            field_dict["goalKeeperWingRightShotsAgainstPerMatch"] = (
                goal_keeper_wing_right_shots_against_per_match
            )
        if goal_keeper_wing_right_shots_saved is not UNSET:
            field_dict["goalKeeperWingRightShotsSaved"] = (
                goal_keeper_wing_right_shots_saved
            )
        if goal_keeper_wing_right_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperWingRightShotsSavedPerMatch"] = (
                goal_keeper_wing_right_shots_saved_per_match
            )
        if goal_keeper_wing_save_accuracy is not UNSET:
            field_dict["goalKeeperWingSaveAccuracy"] = goal_keeper_wing_save_accuracy
        if goal_keeper_wing_save_accuracy_per_match is not UNSET:
            field_dict["goalKeeperWingSaveAccuracyPerMatch"] = (
                goal_keeper_wing_save_accuracy_per_match
            )
        if goal_keeper_wing_shots_against is not UNSET:
            field_dict["goalKeeperWingShotsAgainst"] = goal_keeper_wing_shots_against
        if goal_keeper_wing_shots_against_per_match is not UNSET:
            field_dict["goalKeeperWingShotsAgainstPerMatch"] = (
                goal_keeper_wing_shots_against_per_match
            )
        if goal_keeper_wing_shots_saved is not UNSET:
            field_dict["goalKeeperWingShotsSaved"] = goal_keeper_wing_shots_saved
        if goal_keeper_wing_shots_saved_per_match is not UNSET:
            field_dict["goalKeeperWingShotsSavedPerMatch"] = (
                goal_keeper_wing_shots_saved_per_match
            )
        if goals_scored is not UNSET:
            field_dict["goalsScored"] = goals_scored
        if goals_scored_per_match is not UNSET:
            field_dict["goalsScoredPerMatch"] = goals_scored_per_match
        if handball_performance_index is not UNSET:
            field_dict["handballPerformanceIndex"] = handball_performance_index
        if losses is not UNSET:
            field_dict["losses"] = losses
        if matches_played is not UNSET:
            field_dict["matchesPlayed"] = matches_played
        if minutes is not UNSET:
            field_dict["minutes"] = minutes
        if minutes_per_match is not UNSET:
            field_dict["minutesPerMatch"] = minutes_per_match
        if missed_shots is not UNSET:
            field_dict["missedShots"] = missed_shots
        if missed_shots_per_match is not UNSET:
            field_dict["missedShotsPerMatch"] = missed_shots_per_match
        if nine_metre_centre_goals_scored is not UNSET:
            field_dict["nineMetreCentreGoalsScored"] = nine_metre_centre_goals_scored
        if nine_metre_centre_goals_scored_per_match is not UNSET:
            field_dict["nineMetreCentreGoalsScoredPerMatch"] = (
                nine_metre_centre_goals_scored_per_match
            )
        if nine_metre_centre_missed_shots is not UNSET:
            field_dict["nineMetreCentreMissedShots"] = nine_metre_centre_missed_shots
        if nine_metre_centre_missed_shots_per_match is not UNSET:
            field_dict["nineMetreCentreMissedShotsPerMatch"] = (
                nine_metre_centre_missed_shots_per_match
            )
        if nine_metre_centre_post_hits is not UNSET:
            field_dict["nineMetreCentrePostHits"] = nine_metre_centre_post_hits
        if nine_metre_centre_post_hits_per_match is not UNSET:
            field_dict["nineMetreCentrePostHitsPerMatch"] = (
                nine_metre_centre_post_hits_per_match
            )
        if nine_metre_centre_shooting_accuracy is not UNSET:
            field_dict["nineMetreCentreShootingAccuracy"] = (
                nine_metre_centre_shooting_accuracy
            )
        if nine_metre_centre_shooting_accuracy_per_match is not UNSET:
            field_dict["nineMetreCentreShootingAccuracyPerMatch"] = (
                nine_metre_centre_shooting_accuracy_per_match
            )
        if nine_metre_centre_shots is not UNSET:
            field_dict["nineMetreCentreShots"] = nine_metre_centre_shots
        if nine_metre_centre_shots_per_match is not UNSET:
            field_dict["nineMetreCentreShotsPerMatch"] = (
                nine_metre_centre_shots_per_match
            )
        if nine_metre_centre_shots_blocked is not UNSET:
            field_dict["nineMetreCentreShotsBlocked"] = nine_metre_centre_shots_blocked
        if nine_metre_centre_shots_blocked_per_match is not UNSET:
            field_dict["nineMetreCentreShotsBlockedPerMatch"] = (
                nine_metre_centre_shots_blocked_per_match
            )
        if nine_metre_centre_shots_on_goal is not UNSET:
            field_dict["nineMetreCentreShotsOnGoal"] = nine_metre_centre_shots_on_goal
        if nine_metre_centre_shots_on_goal_per_match is not UNSET:
            field_dict["nineMetreCentreShotsOnGoalPerMatch"] = (
                nine_metre_centre_shots_on_goal_per_match
            )
        if nine_metre_goals_scored is not UNSET:
            field_dict["nineMetreGoalsScored"] = nine_metre_goals_scored
        if nine_metre_goals_scored_per_match is not UNSET:
            field_dict["nineMetreGoalsScoredPerMatch"] = (
                nine_metre_goals_scored_per_match
            )
        if nine_metre_left_goals_scored is not UNSET:
            field_dict["nineMetreLeftGoalsScored"] = nine_metre_left_goals_scored
        if nine_metre_left_goals_scored_per_match is not UNSET:
            field_dict["nineMetreLeftGoalsScoredPerMatch"] = (
                nine_metre_left_goals_scored_per_match
            )
        if nine_metre_left_missed_shots is not UNSET:
            field_dict["nineMetreLeftMissedShots"] = nine_metre_left_missed_shots
        if nine_metre_left_missed_shots_per_match is not UNSET:
            field_dict["nineMetreLeftMissedShotsPerMatch"] = (
                nine_metre_left_missed_shots_per_match
            )
        if nine_metre_left_post_hits is not UNSET:
            field_dict["nineMetreLeftPostHits"] = nine_metre_left_post_hits
        if nine_metre_left_post_hits_per_match is not UNSET:
            field_dict["nineMetreLeftPostHitsPerMatch"] = (
                nine_metre_left_post_hits_per_match
            )
        if nine_metre_left_shooting_accuracy is not UNSET:
            field_dict["nineMetreLeftShootingAccuracy"] = (
                nine_metre_left_shooting_accuracy
            )
        if nine_metre_left_shooting_accuracy_per_match is not UNSET:
            field_dict["nineMetreLeftShootingAccuracyPerMatch"] = (
                nine_metre_left_shooting_accuracy_per_match
            )
        if nine_metre_left_shots is not UNSET:
            field_dict["nineMetreLeftShots"] = nine_metre_left_shots
        if nine_metre_left_shots_per_match is not UNSET:
            field_dict["nineMetreLeftShotsPerMatch"] = nine_metre_left_shots_per_match
        if nine_metre_left_shots_blocked is not UNSET:
            field_dict["nineMetreLeftShotsBlocked"] = nine_metre_left_shots_blocked
        if nine_metre_left_shots_blocked_per_match is not UNSET:
            field_dict["nineMetreLeftShotsBlockedPerMatch"] = (
                nine_metre_left_shots_blocked_per_match
            )
        if nine_metre_left_shots_on_goal is not UNSET:
            field_dict["nineMetreLeftShotsOnGoal"] = nine_metre_left_shots_on_goal
        if nine_metre_left_shots_on_goal_per_match is not UNSET:
            field_dict["nineMetreLeftShotsOnGoalPerMatch"] = (
                nine_metre_left_shots_on_goal_per_match
            )
        if nine_metre_missed_shots is not UNSET:
            field_dict["nineMetreMissedShots"] = nine_metre_missed_shots
        if nine_metre_missed_shots_per_match is not UNSET:
            field_dict["nineMetreMissedShotsPerMatch"] = (
                nine_metre_missed_shots_per_match
            )
        if nine_metre_post_hits is not UNSET:
            field_dict["nineMetrePostHits"] = nine_metre_post_hits
        if nine_metre_post_hits_per_match is not UNSET:
            field_dict["nineMetrePostHitsPerMatch"] = nine_metre_post_hits_per_match
        if nine_metre_right_goals_scored is not UNSET:
            field_dict["nineMetreRightGoalsScored"] = nine_metre_right_goals_scored
        if nine_metre_right_goals_scored_per_match is not UNSET:
            field_dict["nineMetreRightGoalsScoredPerMatch"] = (
                nine_metre_right_goals_scored_per_match
            )
        if nine_metre_right_missed_shots is not UNSET:
            field_dict["nineMetreRightMissedShots"] = nine_metre_right_missed_shots
        if nine_metre_right_missed_shots_per_match is not UNSET:
            field_dict["nineMetreRightMissedShotsPerMatch"] = (
                nine_metre_right_missed_shots_per_match
            )
        if nine_metre_right_post_hits is not UNSET:
            field_dict["nineMetreRightPostHits"] = nine_metre_right_post_hits
        if nine_metre_right_post_hits_per_match is not UNSET:
            field_dict["nineMetreRightPostHitsPerMatch"] = (
                nine_metre_right_post_hits_per_match
            )
        if nine_metre_right_shooting_accuracy is not UNSET:
            field_dict["nineMetreRightShootingAccuracy"] = (
                nine_metre_right_shooting_accuracy
            )
        if nine_metre_right_shooting_accuracy_per_match is not UNSET:
            field_dict["nineMetreRightShootingAccuracyPerMatch"] = (
                nine_metre_right_shooting_accuracy_per_match
            )
        if nine_metre_right_shots is not UNSET:
            field_dict["nineMetreRightShots"] = nine_metre_right_shots
        if nine_metre_right_shots_per_match is not UNSET:
            field_dict["nineMetreRightShotsPerMatch"] = nine_metre_right_shots_per_match
        if nine_metre_right_shots_blocked is not UNSET:
            field_dict["nineMetreRightShotsBlocked"] = nine_metre_right_shots_blocked
        if nine_metre_right_shots_blocked_per_match is not UNSET:
            field_dict["nineMetreRightShotsBlockedPerMatch"] = (
                nine_metre_right_shots_blocked_per_match
            )
        if nine_metre_right_shots_on_goal is not UNSET:
            field_dict["nineMetreRightShotsOnGoal"] = nine_metre_right_shots_on_goal
        if nine_metre_right_shots_on_goal_per_match is not UNSET:
            field_dict["nineMetreRightShotsOnGoalPerMatch"] = (
                nine_metre_right_shots_on_goal_per_match
            )
        if nine_metre_shooting_accuracy is not UNSET:
            field_dict["nineMetreShootingAccuracy"] = nine_metre_shooting_accuracy
        if nine_metre_shooting_accuracy_per_match is not UNSET:
            field_dict["nineMetreShootingAccuracyPerMatch"] = (
                nine_metre_shooting_accuracy_per_match
            )
        if nine_metre_shots is not UNSET:
            field_dict["nineMetreShots"] = nine_metre_shots
        if nine_metre_shots_per_match is not UNSET:
            field_dict["nineMetreShotsPerMatch"] = nine_metre_shots_per_match
        if nine_metre_shots_blocked is not UNSET:
            field_dict["nineMetreShotsBlocked"] = nine_metre_shots_blocked
        if nine_metre_shots_blocked_per_match is not UNSET:
            field_dict["nineMetreShotsBlockedPerMatch"] = (
                nine_metre_shots_blocked_per_match
            )
        if nine_metre_shots_on_goal is not UNSET:
            field_dict["nineMetreShotsOnGoal"] = nine_metre_shots_on_goal
        if nine_metre_shots_on_goal_per_match is not UNSET:
            field_dict["nineMetreShotsOnGoalPerMatch"] = (
                nine_metre_shots_on_goal_per_match
            )
        if passive_play is not UNSET:
            field_dict["passivePlay"] = passive_play
        if pivot_goals_scored is not UNSET:
            field_dict["pivotGoalsScored"] = pivot_goals_scored
        if pivot_goals_scored_per_match is not UNSET:
            field_dict["pivotGoalsScoredPerMatch"] = pivot_goals_scored_per_match
        if pivot_missed_shots is not UNSET:
            field_dict["pivotMissedShots"] = pivot_missed_shots
        if pivot_missed_shots_per_match is not UNSET:
            field_dict["pivotMissedShotsPerMatch"] = pivot_missed_shots_per_match
        if pivot_post_hits is not UNSET:
            field_dict["pivotPostHits"] = pivot_post_hits
        if pivot_post_hits_per_match is not UNSET:
            field_dict["pivotPostHitsPerMatch"] = pivot_post_hits_per_match
        if pivot_shooting_accuracy is not UNSET:
            field_dict["pivotShootingAccuracy"] = pivot_shooting_accuracy
        if pivot_shooting_accuracy_per_match is not UNSET:
            field_dict["pivotShootingAccuracyPerMatch"] = (
                pivot_shooting_accuracy_per_match
            )
        if pivot_shots is not UNSET:
            field_dict["pivotShots"] = pivot_shots
        if pivot_shots_per_match is not UNSET:
            field_dict["pivotShotsPerMatch"] = pivot_shots_per_match
        if pivot_shots_blocked is not UNSET:
            field_dict["pivotShotsBlocked"] = pivot_shots_blocked
        if pivot_shots_blocked_per_match is not UNSET:
            field_dict["pivotShotsBlockedPerMatch"] = pivot_shots_blocked_per_match
        if pivot_shots_on_goal is not UNSET:
            field_dict["pivotShotsOnGoal"] = pivot_shots_on_goal
        if pivot_shots_on_goal_per_match is not UNSET:
            field_dict["pivotShotsOnGoalPerMatch"] = pivot_shots_on_goal_per_match
        if post_hits is not UNSET:
            field_dict["postHits"] = post_hits
        if post_hits_per_match is not UNSET:
            field_dict["postHitsPerMatch"] = post_hits_per_match
        if red_cards is not UNSET:
            field_dict["redCards"] = red_cards
        if red_cards_per_match is not UNSET:
            field_dict["redCardsPerMatch"] = red_cards_per_match
        if seven_metre_goals_scored is not UNSET:
            field_dict["sevenMetreGoalsScored"] = seven_metre_goals_scored
        if seven_metre_goals_scored_per_match is not UNSET:
            field_dict["sevenMetreGoalsScoredPerMatch"] = (
                seven_metre_goals_scored_per_match
            )
        if seven_metre_missed_shots is not UNSET:
            field_dict["sevenMetreMissedShots"] = seven_metre_missed_shots
        if seven_metre_missed_shots_per_match is not UNSET:
            field_dict["sevenMetreMissedShotsPerMatch"] = (
                seven_metre_missed_shots_per_match
            )
        if seven_metre_penalties_awarded is not UNSET:
            field_dict["sevenMetrePenaltiesAwarded"] = seven_metre_penalties_awarded
        if seven_metre_penalties_awarded_per_match is not UNSET:
            field_dict["sevenMetrePenaltiesAwardedPerMatch"] = (
                seven_metre_penalties_awarded_per_match
            )
        if seven_metre_penalties_caused is not UNSET:
            field_dict["sevenMetrePenaltiesCaused"] = seven_metre_penalties_caused
        if seven_metre_penalties_caused_per_match is not UNSET:
            field_dict["sevenMetrePenaltiesCausedPerMatch"] = (
                seven_metre_penalties_caused_per_match
            )
        if seven_metre_penalty_fouls is not UNSET:
            field_dict["sevenMetrePenaltyFouls"] = seven_metre_penalty_fouls
        if seven_metre_penalty_fouls_per_match is not UNSET:
            field_dict["sevenMetrePenaltyFoulsPerMatch"] = (
                seven_metre_penalty_fouls_per_match
            )
        if seven_metre_post_hits is not UNSET:
            field_dict["sevenMetrePostHits"] = seven_metre_post_hits
        if seven_metre_post_hits_per_match is not UNSET:
            field_dict["sevenMetrePostHitsPerMatch"] = seven_metre_post_hits_per_match
        if seven_metre_shooting_accuracy is not UNSET:
            field_dict["sevenMetreShootingAccuracy"] = seven_metre_shooting_accuracy
        if seven_metre_shooting_accuracy_per_match is not UNSET:
            field_dict["sevenMetreShootingAccuracyPerMatch"] = (
                seven_metre_shooting_accuracy_per_match
            )
        if seven_metre_shots is not UNSET:
            field_dict["sevenMetreShots"] = seven_metre_shots
        if seven_metre_shots_per_match is not UNSET:
            field_dict["sevenMetreShotsPerMatch"] = seven_metre_shots_per_match
        if seven_metre_shots_blocked is not UNSET:
            field_dict["sevenMetreShotsBlocked"] = seven_metre_shots_blocked
        if seven_metre_shots_blocked_per_match is not UNSET:
            field_dict["sevenMetreShotsBlockedPerMatch"] = (
                seven_metre_shots_blocked_per_match
            )
        if seven_metre_shots_on_goal is not UNSET:
            field_dict["sevenMetreShotsOnGoal"] = seven_metre_shots_on_goal
        if seven_metre_shots_on_goal_per_match is not UNSET:
            field_dict["sevenMetreShotsOnGoalPerMatch"] = (
                seven_metre_shots_on_goal_per_match
            )
        if shooting_accuracy is not UNSET:
            field_dict["shootingAccuracy"] = shooting_accuracy
        if shooting_accuracy_per_match is not UNSET:
            field_dict["shootingAccuracyPerMatch"] = shooting_accuracy_per_match
        if shoot_outs is not UNSET:
            field_dict["shootOuts"] = shoot_outs
        if shoot_outs_per_match is not UNSET:
            field_dict["shootOutsPerMatch"] = shoot_outs_per_match
        if shoot_outs_made is not UNSET:
            field_dict["shootOutsMade"] = shoot_outs_made
        if shoot_outs_made_per_match is not UNSET:
            field_dict["shootOutsMadePerMatch"] = shoot_outs_made_per_match
        if shoot_outs_missed is not UNSET:
            field_dict["shootOutsMissed"] = shoot_outs_missed
        if shoot_outs_missed_per_match is not UNSET:
            field_dict["shootOutsMissedPerMatch"] = shoot_outs_missed_per_match
        if shoot_outs_saved is not UNSET:
            field_dict["shootOutsSaved"] = shoot_outs_saved
        if shoot_outs_saved_per_match is not UNSET:
            field_dict["shootOutsSavedPerMatch"] = shoot_outs_saved_per_match
        if shots is not UNSET:
            field_dict["shots"] = shots
        if shots_per_match is not UNSET:
            field_dict["shotsPerMatch"] = shots_per_match
        if shots_blocked is not UNSET:
            field_dict["shotsBlocked"] = shots_blocked
        if shots_blocked_per_match is not UNSET:
            field_dict["shotsBlockedPerMatch"] = shots_blocked_per_match
        if shots_on_goal is not UNSET:
            field_dict["shotsOnGoal"] = shots_on_goal
        if shots_on_goal_per_match is not UNSET:
            field_dict["shotsOnGoalPerMatch"] = shots_on_goal_per_match
        if shots_saved_by_goal_keeper is not UNSET:
            field_dict["shotsSavedByGoalKeeper"] = shots_saved_by_goal_keeper
        if shots_saved_by_goal_keeper_per_match is not UNSET:
            field_dict["shotsSavedByGoalKeeperPerMatch"] = (
                shots_saved_by_goal_keeper_per_match
            )
        if six_metre_centre_goals_scored is not UNSET:
            field_dict["sixMetreCentreGoalsScored"] = six_metre_centre_goals_scored
        if six_metre_centre_goals_scored_per_match is not UNSET:
            field_dict["sixMetreCentreGoalsScoredPerMatch"] = (
                six_metre_centre_goals_scored_per_match
            )
        if six_metre_centre_missed_shots is not UNSET:
            field_dict["sixMetreCentreMissedShots"] = six_metre_centre_missed_shots
        if six_metre_centre_missed_shots_per_match is not UNSET:
            field_dict["sixMetreCentreMissedShotsPerMatch"] = (
                six_metre_centre_missed_shots_per_match
            )
        if six_metre_centre_post_hits is not UNSET:
            field_dict["sixMetreCentrePostHits"] = six_metre_centre_post_hits
        if six_metre_centre_post_hits_per_match is not UNSET:
            field_dict["sixMetreCentrePostHitsPerMatch"] = (
                six_metre_centre_post_hits_per_match
            )
        if six_metre_centre_shooting_accuracy is not UNSET:
            field_dict["sixMetreCentreShootingAccuracy"] = (
                six_metre_centre_shooting_accuracy
            )
        if six_metre_centre_shooting_accuracy_per_match is not UNSET:
            field_dict["sixMetreCentreShootingAccuracyPerMatch"] = (
                six_metre_centre_shooting_accuracy_per_match
            )
        if six_metre_centre_shots is not UNSET:
            field_dict["sixMetreCentreShots"] = six_metre_centre_shots
        if six_metre_centre_shots_per_match is not UNSET:
            field_dict["sixMetreCentreShotsPerMatch"] = six_metre_centre_shots_per_match
        if six_metre_centre_shots_blocked is not UNSET:
            field_dict["sixMetreCentreShotsBlocked"] = six_metre_centre_shots_blocked
        if six_metre_centre_shots_blocked_per_match is not UNSET:
            field_dict["sixMetreCentreShotsBlockedPerMatch"] = (
                six_metre_centre_shots_blocked_per_match
            )
        if six_metre_centre_shots_on_goal is not UNSET:
            field_dict["sixMetreCentreShotsOnGoal"] = six_metre_centre_shots_on_goal
        if six_metre_centre_shots_on_goal_per_match is not UNSET:
            field_dict["sixMetreCentreShotsOnGoalPerMatch"] = (
                six_metre_centre_shots_on_goal_per_match
            )
        if six_metre_goals_scored is not UNSET:
            field_dict["sixMetreGoalsScored"] = six_metre_goals_scored
        if six_metre_goals_scored_per_match is not UNSET:
            field_dict["sixMetreGoalsScoredPerMatch"] = six_metre_goals_scored_per_match
        if six_metre_left_goals_scored is not UNSET:
            field_dict["sixMetreLeftGoalsScored"] = six_metre_left_goals_scored
        if six_metre_left_goals_scored_per_match is not UNSET:
            field_dict["sixMetreLeftGoalsScoredPerMatch"] = (
                six_metre_left_goals_scored_per_match
            )
        if six_metre_left_missed_shots is not UNSET:
            field_dict["sixMetreLeftMissedShots"] = six_metre_left_missed_shots
        if six_metre_left_missed_shots_per_match is not UNSET:
            field_dict["sixMetreLeftMissedShotsPerMatch"] = (
                six_metre_left_missed_shots_per_match
            )
        if six_metre_left_post_hits is not UNSET:
            field_dict["sixMetreLeftPostHits"] = six_metre_left_post_hits
        if six_metre_left_post_hits_per_match is not UNSET:
            field_dict["sixMetreLeftPostHitsPerMatch"] = (
                six_metre_left_post_hits_per_match
            )
        if six_metre_left_shooting_accuracy is not UNSET:
            field_dict["sixMetreLeftShootingAccuracy"] = (
                six_metre_left_shooting_accuracy
            )
        if six_metre_left_shooting_accuracy_per_match is not UNSET:
            field_dict["sixMetreLeftShootingAccuracyPerMatch"] = (
                six_metre_left_shooting_accuracy_per_match
            )
        if six_metre_left_shots is not UNSET:
            field_dict["sixMetreLeftShots"] = six_metre_left_shots
        if six_metre_left_shots_per_match is not UNSET:
            field_dict["sixMetreLeftShotsPerMatch"] = six_metre_left_shots_per_match
        if six_metre_left_shots_blocked is not UNSET:
            field_dict["sixMetreLeftShotsBlocked"] = six_metre_left_shots_blocked
        if six_metre_left_shots_blocked_per_match is not UNSET:
            field_dict["sixMetreLeftShotsBlockedPerMatch"] = (
                six_metre_left_shots_blocked_per_match
            )
        if six_metre_left_shots_on_goal is not UNSET:
            field_dict["sixMetreLeftShotsOnGoal"] = six_metre_left_shots_on_goal
        if six_metre_left_shots_on_goal_per_match is not UNSET:
            field_dict["sixMetreLeftShotsOnGoalPerMatch"] = (
                six_metre_left_shots_on_goal_per_match
            )
        if six_metre_missed_shots is not UNSET:
            field_dict["sixMetreMissedShots"] = six_metre_missed_shots
        if six_metre_missed_shots_per_match is not UNSET:
            field_dict["sixMetreMissedShotsPerMatch"] = six_metre_missed_shots_per_match
        if six_metre_post_hits is not UNSET:
            field_dict["sixMetrePostHits"] = six_metre_post_hits
        if six_metre_post_hits_per_match is not UNSET:
            field_dict["sixMetrePostHitsPerMatch"] = six_metre_post_hits_per_match
        if six_metre_right_goals_scored is not UNSET:
            field_dict["sixMetreRightGoalsScored"] = six_metre_right_goals_scored
        if six_metre_right_goals_scored_per_match is not UNSET:
            field_dict["sixMetreRightGoalsScoredPerMatch"] = (
                six_metre_right_goals_scored_per_match
            )
        if six_metre_right_missed_shots is not UNSET:
            field_dict["sixMetreRightMissedShots"] = six_metre_right_missed_shots
        if six_metre_right_missed_shots_per_match is not UNSET:
            field_dict["sixMetreRightMissedShotsPerMatch"] = (
                six_metre_right_missed_shots_per_match
            )
        if six_metre_right_post_hits is not UNSET:
            field_dict["sixMetreRightPostHits"] = six_metre_right_post_hits
        if six_metre_right_post_hits_per_match is not UNSET:
            field_dict["sixMetreRightPostHitsPerMatch"] = (
                six_metre_right_post_hits_per_match
            )
        if six_metre_right_shooting_accuracy is not UNSET:
            field_dict["sixMetreRightShootingAccuracy"] = (
                six_metre_right_shooting_accuracy
            )
        if six_metre_right_shooting_accuracy_per_match is not UNSET:
            field_dict["sixMetreRightShootingAccuracyPerMatch"] = (
                six_metre_right_shooting_accuracy_per_match
            )
        if six_metre_right_shots is not UNSET:
            field_dict["sixMetreRightShots"] = six_metre_right_shots
        if six_metre_right_shots_per_match is not UNSET:
            field_dict["sixMetreRightShotsPerMatch"] = six_metre_right_shots_per_match
        if six_metre_right_shots_blocked is not UNSET:
            field_dict["sixMetreRightShotsBlocked"] = six_metre_right_shots_blocked
        if six_metre_right_shots_blocked_per_match is not UNSET:
            field_dict["sixMetreRightShotsBlockedPerMatch"] = (
                six_metre_right_shots_blocked_per_match
            )
        if six_metre_right_shots_on_goal is not UNSET:
            field_dict["sixMetreRightShotsOnGoal"] = six_metre_right_shots_on_goal
        if six_metre_right_shots_on_goal_per_match is not UNSET:
            field_dict["sixMetreRightShotsOnGoalPerMatch"] = (
                six_metre_right_shots_on_goal_per_match
            )
        if six_metre_shooting_accuracy is not UNSET:
            field_dict["sixMetreShootingAccuracy"] = six_metre_shooting_accuracy
        if six_metre_shooting_accuracy_per_match is not UNSET:
            field_dict["sixMetreShootingAccuracyPerMatch"] = (
                six_metre_shooting_accuracy_per_match
            )
        if six_metre_shots is not UNSET:
            field_dict["sixMetreShots"] = six_metre_shots
        if six_metre_shots_per_match is not UNSET:
            field_dict["sixMetreShotsPerMatch"] = six_metre_shots_per_match
        if six_metre_shots_blocked is not UNSET:
            field_dict["sixMetreShotsBlocked"] = six_metre_shots_blocked
        if six_metre_shots_blocked_per_match is not UNSET:
            field_dict["sixMetreShotsBlockedPerMatch"] = (
                six_metre_shots_blocked_per_match
            )
        if six_metre_shots_on_goal is not UNSET:
            field_dict["sixMetreShotsOnGoal"] = six_metre_shots_on_goal
        if six_metre_shots_on_goal_per_match is not UNSET:
            field_dict["sixMetreShotsOnGoalPerMatch"] = (
                six_metre_shots_on_goal_per_match
            )
        if speed_distance_per_time is not UNSET:
            field_dict["speedDistancePerTime"] = speed_distance_per_time
        if speed_max is not UNSET:
            field_dict["speedMax"] = speed_max
        if steals is not UNSET:
            field_dict["steals"] = steals
        if steals_per_match is not UNSET:
            field_dict["stealsPerMatch"] = steals_per_match
        if substitutions is not UNSET:
            field_dict["substitutions"] = substitutions
        if substitutions_per_match is not UNSET:
            field_dict["substitutionsPerMatch"] = substitutions_per_match
        if suspensions is not UNSET:
            field_dict["suspensions"] = suspensions
        if suspensions_per_match is not UNSET:
            field_dict["suspensionsPerMatch"] = suspensions_per_match
        if technical_ball_faults is not UNSET:
            field_dict["technicalBallFaults"] = technical_ball_faults
        if technical_ball_faults_per_match is not UNSET:
            field_dict["technicalBallFaultsPerMatch"] = technical_ball_faults_per_match
        if technical_faults is not UNSET:
            field_dict["technicalFaults"] = technical_faults
        if technical_faults_per_match is not UNSET:
            field_dict["technicalFaultsPerMatch"] = technical_faults_per_match
        if technical_rule_faults is not UNSET:
            field_dict["technicalRuleFaults"] = technical_rule_faults
        if technical_rule_faults_per_match is not UNSET:
            field_dict["technicalRuleFaultsPerMatch"] = technical_rule_faults_per_match
        if time_on_playing_field is not UNSET:
            field_dict["timeOnPlayingField"] = time_on_playing_field
        if time_ball_possession is not UNSET:
            field_dict["timeBallPossession"] = time_ball_possession
        if time_played is not UNSET:
            field_dict["timePlayed"] = time_played
        if time_played_per_match is not UNSET:
            field_dict["timePlayedPerMatch"] = time_played_per_match
        if turnovers is not UNSET:
            field_dict["turnovers"] = turnovers
        if turnovers_per_match is not UNSET:
            field_dict["turnoversPerMatch"] = turnovers_per_match
        if two_minute_suspensions is not UNSET:
            field_dict["twoMinuteSuspensions"] = two_minute_suspensions
        if two_minute_suspensions_per_match is not UNSET:
            field_dict["twoMinuteSuspensionsPerMatch"] = (
                two_minute_suspensions_per_match
            )
        if wing_goals_scored is not UNSET:
            field_dict["wingGoalsScored"] = wing_goals_scored
        if wing_goals_scored_per_match is not UNSET:
            field_dict["wingGoalsScoredPerMatch"] = wing_goals_scored_per_match
        if wing_left_goals_scored is not UNSET:
            field_dict["wingLeftGoalsScored"] = wing_left_goals_scored
        if wing_left_goals_scored_per_match is not UNSET:
            field_dict["wingLeftGoalsScoredPerMatch"] = wing_left_goals_scored_per_match
        if wing_left_missed_shots is not UNSET:
            field_dict["wingLeftMissedShots"] = wing_left_missed_shots
        if wing_left_missed_shots_per_match is not UNSET:
            field_dict["wingLeftMissedShotsPerMatch"] = wing_left_missed_shots_per_match
        if wing_left_post_hits is not UNSET:
            field_dict["wingLeftPostHits"] = wing_left_post_hits
        if wing_left_post_hits_per_match is not UNSET:
            field_dict["wingLeftPostHitsPerMatch"] = wing_left_post_hits_per_match
        if wing_left_shooting_accuracy is not UNSET:
            field_dict["wingLeftShootingAccuracy"] = wing_left_shooting_accuracy
        if wing_left_shooting_accuracy_per_match is not UNSET:
            field_dict["wingLeftShootingAccuracyPerMatch"] = (
                wing_left_shooting_accuracy_per_match
            )
        if wing_left_shots is not UNSET:
            field_dict["wingLeftShots"] = wing_left_shots
        if wing_left_shots_per_match is not UNSET:
            field_dict["wingLeftShotsPerMatch"] = wing_left_shots_per_match
        if wing_left_shots_blocked is not UNSET:
            field_dict["wingLeftShotsBlocked"] = wing_left_shots_blocked
        if wing_left_shots_blocked_per_match is not UNSET:
            field_dict["wingLeftShotsBlockedPerMatch"] = (
                wing_left_shots_blocked_per_match
            )
        if wing_left_shots_on_goal is not UNSET:
            field_dict["wingLeftShotsOnGoal"] = wing_left_shots_on_goal
        if wing_left_shots_on_goal_per_match is not UNSET:
            field_dict["wingLeftShotsOnGoalPerMatch"] = (
                wing_left_shots_on_goal_per_match
            )
        if wing_missed_shots is not UNSET:
            field_dict["wingMissedShots"] = wing_missed_shots
        if wing_missed_shots_per_match is not UNSET:
            field_dict["wingMissedShotsPerMatch"] = wing_missed_shots_per_match
        if wing_post_hits is not UNSET:
            field_dict["wingPostHits"] = wing_post_hits
        if wing_post_hits_per_match is not UNSET:
            field_dict["wingPostHitsPerMatch"] = wing_post_hits_per_match
        if wing_right_goals_scored is not UNSET:
            field_dict["wingRightGoalsScored"] = wing_right_goals_scored
        if wing_right_goals_scored_per_match is not UNSET:
            field_dict["wingRightGoalsScoredPerMatch"] = (
                wing_right_goals_scored_per_match
            )
        if wing_right_missed_shots is not UNSET:
            field_dict["wingRightMissedShots"] = wing_right_missed_shots
        if wing_right_missed_shots_per_match is not UNSET:
            field_dict["wingRightMissedShotsPerMatch"] = (
                wing_right_missed_shots_per_match
            )
        if wing_right_post_hits is not UNSET:
            field_dict["wingRightPostHits"] = wing_right_post_hits
        if wing_right_post_hits_per_match is not UNSET:
            field_dict["wingRightPostHitsPerMatch"] = wing_right_post_hits_per_match
        if wing_right_shooting_accuracy is not UNSET:
            field_dict["wingRightShootingAccuracy"] = wing_right_shooting_accuracy
        if wing_right_shooting_accuracy_per_match is not UNSET:
            field_dict["wingRightShootingAccuracyPerMatch"] = (
                wing_right_shooting_accuracy_per_match
            )
        if wing_right_shots is not UNSET:
            field_dict["wingRightShots"] = wing_right_shots
        if wing_right_shots_per_match is not UNSET:
            field_dict["wingRightShotsPerMatch"] = wing_right_shots_per_match
        if wing_right_shots_blocked is not UNSET:
            field_dict["wingRightShotsBlocked"] = wing_right_shots_blocked
        if wing_right_shots_blocked_per_match is not UNSET:
            field_dict["wingRightShotsBlockedPerMatch"] = (
                wing_right_shots_blocked_per_match
            )
        if wing_right_shots_on_goal is not UNSET:
            field_dict["wingRightShotsOnGoal"] = wing_right_shots_on_goal
        if wing_right_shots_on_goal_per_match is not UNSET:
            field_dict["wingRightShotsOnGoalPerMatch"] = (
                wing_right_shots_on_goal_per_match
            )
        if wing_shooting_accuracy is not UNSET:
            field_dict["wingShootingAccuracy"] = wing_shooting_accuracy
        if wing_shooting_accuracy_per_match is not UNSET:
            field_dict["wingShootingAccuracyPerMatch"] = (
                wing_shooting_accuracy_per_match
            )
        if wing_shots is not UNSET:
            field_dict["wingShots"] = wing_shots
        if wing_shots_per_match is not UNSET:
            field_dict["wingShotsPerMatch"] = wing_shots_per_match
        if wing_shots_blocked is not UNSET:
            field_dict["wingShotsBlocked"] = wing_shots_blocked
        if wing_shots_blocked_per_match is not UNSET:
            field_dict["wingShotsBlockedPerMatch"] = wing_shots_blocked_per_match
        if wing_shots_on_goal is not UNSET:
            field_dict["wingShotsOnGoal"] = wing_shots_on_goal
        if wing_shots_on_goal_per_match is not UNSET:
            field_dict["wingShotsOnGoalPerMatch"] = wing_shots_on_goal_per_match
        if wins is not UNSET:
            field_dict["wins"] = wins
        if yellow_cards is not UNSET:
            field_dict["yellowCards"] = yellow_cards
        if yellow_cards_per_match is not UNSET:
            field_dict["yellowCardsPerMatch"] = yellow_cards_per_match

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_airtime_max(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        airtime_max = _parse_airtime_max(d.pop("airtimeMax", UNSET))

        def _parse_assists(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        assists = _parse_assists(d.pop("assists", UNSET))

        def _parse_assists_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        assists_per_match = _parse_assists_per_match(d.pop("assistsPerMatch", UNSET))

        def _parse_back_court_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_goals_scored = _parse_back_court_goals_scored(
            d.pop("backCourtGoalsScored", UNSET)
        )

        def _parse_back_court_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        back_court_goals_scored_per_match = _parse_back_court_goals_scored_per_match(
            d.pop("backCourtGoalsScoredPerMatch", UNSET)
        )

        def _parse_back_court_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_missed_shots = _parse_back_court_missed_shots(
            d.pop("backCourtMissedShots", UNSET)
        )

        def _parse_back_court_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        back_court_missed_shots_per_match = _parse_back_court_missed_shots_per_match(
            d.pop("backCourtMissedShotsPerMatch", UNSET)
        )

        def _parse_back_court_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_post_hits = _parse_back_court_post_hits(
            d.pop("backCourtPostHits", UNSET)
        )

        def _parse_back_court_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        back_court_post_hits_per_match = _parse_back_court_post_hits_per_match(
            d.pop("backCourtPostHitsPerMatch", UNSET)
        )

        back_court_shooting_accuracy = d.pop("backCourtShootingAccuracy", UNSET)

        def _parse_back_court_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        back_court_shooting_accuracy_per_match = (
            _parse_back_court_shooting_accuracy_per_match(
                d.pop("backCourtShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_back_court_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_shots = _parse_back_court_shots(d.pop("backCourtShots", UNSET))

        def _parse_back_court_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        back_court_shots_per_match = _parse_back_court_shots_per_match(
            d.pop("backCourtShotsPerMatch", UNSET)
        )

        def _parse_back_court_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_shots_blocked = _parse_back_court_shots_blocked(
            d.pop("backCourtShotsBlocked", UNSET)
        )

        def _parse_back_court_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        back_court_shots_blocked_per_match = _parse_back_court_shots_blocked_per_match(
            d.pop("backCourtShotsBlockedPerMatch", UNSET)
        )

        def _parse_back_court_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        back_court_shots_on_goal = _parse_back_court_shots_on_goal(
            d.pop("backCourtShotsOnGoal", UNSET)
        )

        def _parse_back_court_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        back_court_shots_on_goal_per_match = _parse_back_court_shots_on_goal_per_match(
            d.pop("backCourtShotsOnGoalPerMatch", UNSET)
        )

        def _parse_blocks(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        blocks = _parse_blocks(d.pop("blocks", UNSET))

        def _parse_blocks_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        blocks_per_match = _parse_blocks_per_match(d.pop("blocksPerMatch", UNSET))

        def _parse_blue_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        blue_cards = _parse_blue_cards(d.pop("blueCards", UNSET))

        def _parse_blue_cards_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        blue_cards_per_match = _parse_blue_cards_per_match(
            d.pop("blueCardsPerMatch", UNSET)
        )

        def _parse_break_through_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_goals_scored = _parse_break_through_goals_scored(
            d.pop("breakThroughGoalsScored", UNSET)
        )

        def _parse_break_through_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        break_through_goals_scored_per_match = (
            _parse_break_through_goals_scored_per_match(
                d.pop("breakThroughGoalsScoredPerMatch", UNSET)
            )
        )

        def _parse_break_through_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_missed_shots = _parse_break_through_missed_shots(
            d.pop("breakThroughMissedShots", UNSET)
        )

        def _parse_break_through_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        break_through_missed_shots_per_match = (
            _parse_break_through_missed_shots_per_match(
                d.pop("breakThroughMissedShotsPerMatch", UNSET)
            )
        )

        def _parse_break_through_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_post_hits = _parse_break_through_post_hits(
            d.pop("breakThroughPostHits", UNSET)
        )

        def _parse_break_through_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        break_through_post_hits_per_match = _parse_break_through_post_hits_per_match(
            d.pop("breakThroughPostHitsPerMatch", UNSET)
        )

        break_through_shooting_accuracy = d.pop("breakThroughShootingAccuracy", UNSET)

        def _parse_break_through_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        break_through_shooting_accuracy_per_match = (
            _parse_break_through_shooting_accuracy_per_match(
                d.pop("breakThroughShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_break_through_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_shots = _parse_break_through_shots(
            d.pop("breakThroughShots", UNSET)
        )

        def _parse_break_through_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        break_through_shots_per_match = _parse_break_through_shots_per_match(
            d.pop("breakThroughShotsPerMatch", UNSET)
        )

        def _parse_break_through_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_shots_blocked = _parse_break_through_shots_blocked(
            d.pop("breakThroughShotsBlocked", UNSET)
        )

        def _parse_break_through_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        break_through_shots_blocked_per_match = (
            _parse_break_through_shots_blocked_per_match(
                d.pop("breakThroughShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_break_through_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        break_through_shots_on_goal = _parse_break_through_shots_on_goal(
            d.pop("breakThroughShotsOnGoal", UNSET)
        )

        def _parse_break_through_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        break_through_shots_on_goal_per_match = (
            _parse_break_through_shots_on_goal_per_match(
                d.pop("breakThroughShotsOnGoalPerMatch", UNSET)
            )
        )

        def _parse_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cards = _parse_cards(d.pop("cards", UNSET))

        def _parse_cards_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cards_per_match = _parse_cards_per_match(d.pop("cardsPerMatch", UNSET))

        def _parse_distance_speed_category_1(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        distance_speed_category_1 = _parse_distance_speed_category_1(
            d.pop("distanceSpeedCategory1", UNSET)
        )

        def _parse_distance_speed_category_2(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        distance_speed_category_2 = _parse_distance_speed_category_2(
            d.pop("distanceSpeedCategory2", UNSET)
        )

        def _parse_distance_speed_category_3(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        distance_speed_category_3 = _parse_distance_speed_category_3(
            d.pop("distanceSpeedCategory3", UNSET)
        )

        def _parse_distance_speed_category_4(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        distance_speed_category_4 = _parse_distance_speed_category_4(
            d.pop("distanceSpeedCategory4", UNSET)
        )

        def _parse_distance_speed_category_5(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        distance_speed_category_5 = _parse_distance_speed_category_5(
            d.pop("distanceSpeedCategory5", UNSET)
        )

        def _parse_distance_total(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        distance_total = _parse_distance_total(d.pop("distanceTotal", UNSET))

        def _parse_draws(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        draws = _parse_draws(d.pop("draws", UNSET))

        def _parse_empty_net_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        empty_net_goals_scored = _parse_empty_net_goals_scored(
            d.pop("emptyNetGoalsScored", UNSET)
        )

        def _parse_fast_break_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_goals_scored = _parse_fast_break_goals_scored(
            d.pop("fastBreakGoalsScored", UNSET)
        )

        def _parse_fast_break_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fast_break_goals_scored_per_match = _parse_fast_break_goals_scored_per_match(
            d.pop("fastBreakGoalsScoredPerMatch", UNSET)
        )

        def _parse_fast_break_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_missed_shots = _parse_fast_break_missed_shots(
            d.pop("fastBreakMissedShots", UNSET)
        )

        def _parse_fast_break_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fast_break_missed_shots_per_match = _parse_fast_break_missed_shots_per_match(
            d.pop("fastBreakMissedShotsPerMatch", UNSET)
        )

        def _parse_fast_break_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_post_hits = _parse_fast_break_post_hits(
            d.pop("fastBreakPostHits", UNSET)
        )

        def _parse_fast_break_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fast_break_post_hits_per_match = _parse_fast_break_post_hits_per_match(
            d.pop("fastBreakPostHitsPerMatch", UNSET)
        )

        fast_break_shooting_accuracy = d.pop("fastBreakShootingAccuracy", UNSET)

        def _parse_fast_break_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fast_break_shooting_accuracy_per_match = (
            _parse_fast_break_shooting_accuracy_per_match(
                d.pop("fastBreakShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_fast_break_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_shots = _parse_fast_break_shots(d.pop("fastBreakShots", UNSET))

        def _parse_fast_break_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fast_break_shots_per_match = _parse_fast_break_shots_per_match(
            d.pop("fastBreakShotsPerMatch", UNSET)
        )

        def _parse_fast_break_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_shots_blocked = _parse_fast_break_shots_blocked(
            d.pop("fastBreakShotsBlocked", UNSET)
        )

        def _parse_fast_break_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fast_break_shots_blocked_per_match = _parse_fast_break_shots_blocked_per_match(
            d.pop("fastBreakShotsBlockedPerMatch", UNSET)
        )

        def _parse_fast_break_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fast_break_shots_on_goal = _parse_fast_break_shots_on_goal(
            d.pop("fastBreakShotsOnGoal", UNSET)
        )

        def _parse_fast_break_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fast_break_shots_on_goal_per_match = _parse_fast_break_shots_on_goal_per_match(
            d.pop("fastBreakShotsOnGoalPerMatch", UNSET)
        )

        def _parse_field_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_goals_scored = _parse_field_goals_scored(d.pop("fieldGoalsScored", UNSET))

        def _parse_field_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        field_goals_scored_per_match = _parse_field_goals_scored_per_match(
            d.pop("fieldGoalsScoredPerMatch", UNSET)
        )

        def _parse_field_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_missed_shots = _parse_field_missed_shots(d.pop("fieldMissedShots", UNSET))

        def _parse_field_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        field_missed_shots_per_match = _parse_field_missed_shots_per_match(
            d.pop("fieldMissedShotsPerMatch", UNSET)
        )

        def _parse_field_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_post_hits = _parse_field_post_hits(d.pop("fieldPostHits", UNSET))

        def _parse_field_post_hits_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        field_post_hits_per_match = _parse_field_post_hits_per_match(
            d.pop("fieldPostHitsPerMatch", UNSET)
        )

        field_shooting_accuracy = d.pop("fieldShootingAccuracy", UNSET)

        def _parse_field_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        field_shooting_accuracy_per_match = _parse_field_shooting_accuracy_per_match(
            d.pop("fieldShootingAccuracyPerMatch", UNSET)
        )

        def _parse_field_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_shots = _parse_field_shots(d.pop("fieldShots", UNSET))

        def _parse_field_shots_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        field_shots_per_match = _parse_field_shots_per_match(
            d.pop("fieldShotsPerMatch", UNSET)
        )

        def _parse_field_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_shots_blocked = _parse_field_shots_blocked(
            d.pop("fieldShotsBlocked", UNSET)
        )

        def _parse_field_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        field_shots_blocked_per_match = _parse_field_shots_blocked_per_match(
            d.pop("fieldShotsBlockedPerMatch", UNSET)
        )

        def _parse_field_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        field_shots_on_goal = _parse_field_shots_on_goal(
            d.pop("fieldShotsOnGoal", UNSET)
        )

        def _parse_field_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        field_shots_on_goal_per_match = _parse_field_shots_on_goal_per_match(
            d.pop("fieldShotsOnGoalPerMatch", UNSET)
        )

        def _parse_fouls(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fouls = _parse_fouls(d.pop("fouls", UNSET))

        def _parse_fouls_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fouls_per_match = _parse_fouls_per_match(d.pop("foulsPerMatch", UNSET))

        def _parse_fouls_drawn(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        fouls_drawn = _parse_fouls_drawn(d.pop("foulsDrawn", UNSET))

        def _parse_fouls_drawn_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fouls_drawn_per_match = _parse_fouls_drawn_per_match(
            d.pop("foulsDrawnPerMatch", UNSET)
        )

        def _parse_four_minute_suspensions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        four_minute_suspensions = _parse_four_minute_suspensions(
            d.pop("fourMinuteSuspensions", UNSET)
        )

        def _parse_four_minute_suspensions_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        four_minute_suspensions_per_match = _parse_four_minute_suspensions_per_match(
            d.pop("fourMinuteSuspensionsPerMatch", UNSET)
        )

        def _parse_games(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        games = _parse_games(d.pop("games", UNSET))

        def _parse_games_started(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        games_started = _parse_games_started(d.pop("gamesStarted", UNSET))

        def _parse_goal_keeper_back_court_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_back_court_goals_against = (
            _parse_goal_keeper_back_court_goals_against(
                d.pop("goalKeeperBackCourtGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_back_court_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_back_court_goals_against_per_match = (
            _parse_goal_keeper_back_court_goals_against_per_match(
                d.pop("goalKeeperBackCourtGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_back_court_save_accuracy = d.pop(
            "goalKeeperBackCourtSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_back_court_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_back_court_save_accuracy_per_match = (
            _parse_goal_keeper_back_court_save_accuracy_per_match(
                d.pop("goalKeeperBackCourtSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_back_court_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_back_court_shots_against = (
            _parse_goal_keeper_back_court_shots_against(
                d.pop("goalKeeperBackCourtShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_back_court_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_back_court_shots_against_per_match = (
            _parse_goal_keeper_back_court_shots_against_per_match(
                d.pop("goalKeeperBackCourtShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_back_court_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_back_court_shots_saved = _parse_goal_keeper_back_court_shots_saved(
            d.pop("goalKeeperBackCourtShotsSaved", UNSET)
        )

        def _parse_goal_keeper_back_court_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_back_court_shots_saved_per_match = (
            _parse_goal_keeper_back_court_shots_saved_per_match(
                d.pop("goalKeeperBackCourtShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_break_through_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_break_through_goals_against = (
            _parse_goal_keeper_break_through_goals_against(
                d.pop("goalKeeperBreakThroughGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_break_through_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_break_through_goals_against_per_match = (
            _parse_goal_keeper_break_through_goals_against_per_match(
                d.pop("goalKeeperBreakThroughGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_break_through_save_accuracy = d.pop(
            "goalKeeperBreakThroughSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_break_through_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_break_through_save_accuracy_per_match = (
            _parse_goal_keeper_break_through_save_accuracy_per_match(
                d.pop("goalKeeperBreakThroughSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_break_through_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_break_through_shots_against = (
            _parse_goal_keeper_break_through_shots_against(
                d.pop("goalKeeperBreakThroughShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_break_through_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_break_through_shots_against_per_match = (
            _parse_goal_keeper_break_through_shots_against_per_match(
                d.pop("goalKeeperBreakThroughShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_break_through_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_break_through_shots_saved = (
            _parse_goal_keeper_break_through_shots_saved(
                d.pop("goalKeeperBreakThroughShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_break_through_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_break_through_shots_saved_per_match = (
            _parse_goal_keeper_break_through_shots_saved_per_match(
                d.pop("goalKeeperBreakThroughShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_fast_break_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_fast_break_goals_against = (
            _parse_goal_keeper_fast_break_goals_against(
                d.pop("goalKeeperFastBreakGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_fast_break_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_fast_break_goals_against_per_match = (
            _parse_goal_keeper_fast_break_goals_against_per_match(
                d.pop("goalKeeperFastBreakGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_fast_break_save_accuracy = d.pop(
            "goalKeeperFastBreakSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_fast_break_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_fast_break_save_accuracy_per_match = (
            _parse_goal_keeper_fast_break_save_accuracy_per_match(
                d.pop("goalKeeperFastBreakSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_fast_break_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_fast_break_shots_against = (
            _parse_goal_keeper_fast_break_shots_against(
                d.pop("goalKeeperFastBreakShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_fast_break_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_fast_break_shots_against_per_match = (
            _parse_goal_keeper_fast_break_shots_against_per_match(
                d.pop("goalKeeperFastBreakShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_fast_break_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_fast_break_shots_saved = _parse_goal_keeper_fast_break_shots_saved(
            d.pop("goalKeeperFastBreakShotsSaved", UNSET)
        )

        def _parse_goal_keeper_fast_break_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_fast_break_shots_saved_per_match = (
            _parse_goal_keeper_fast_break_shots_saved_per_match(
                d.pop("goalKeeperFastBreakShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_field_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_field_goals_against = _parse_goal_keeper_field_goals_against(
            d.pop("goalKeeperFieldGoalsAgainst", UNSET)
        )

        def _parse_goal_keeper_field_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_field_goals_against_per_match = (
            _parse_goal_keeper_field_goals_against_per_match(
                d.pop("goalKeeperFieldGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_field_save_accuracy = d.pop("goalKeeperFieldSaveAccuracy", UNSET)

        def _parse_goal_keeper_field_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_field_save_accuracy_per_match = (
            _parse_goal_keeper_field_save_accuracy_per_match(
                d.pop("goalKeeperFieldSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_field_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_field_shots_against = _parse_goal_keeper_field_shots_against(
            d.pop("goalKeeperFieldShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_field_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_field_shots_against_per_match = (
            _parse_goal_keeper_field_shots_against_per_match(
                d.pop("goalKeeperFieldShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_field_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_field_shots_saved = _parse_goal_keeper_field_shots_saved(
            d.pop("goalKeeperFieldShotsSaved", UNSET)
        )

        def _parse_goal_keeper_field_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_field_shots_saved_per_match = (
            _parse_goal_keeper_field_shots_saved_per_match(
                d.pop("goalKeeperFieldShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_goals_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_goals_against = _parse_goal_keeper_goals_against(
            d.pop("goalKeeperGoalsAgainst", UNSET)
        )

        def _parse_goal_keeper_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_goals_against_per_match = (
            _parse_goal_keeper_goals_against_per_match(
                d.pop("goalKeeperGoalsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_centre_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_centre_goals_against = (
            _parse_goal_keeper_nine_metre_centre_goals_against(
                d.pop("goalKeeperNineMetreCentreGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_centre_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_centre_goals_against_per_match = (
            _parse_goal_keeper_nine_metre_centre_goals_against_per_match(
                d.pop("goalKeeperNineMetreCentreGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_nine_metre_centre_save_accuracy = d.pop(
            "goalKeeperNineMetreCentreSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_nine_metre_centre_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_centre_save_accuracy_per_match = (
            _parse_goal_keeper_nine_metre_centre_save_accuracy_per_match(
                d.pop("goalKeeperNineMetreCentreSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_centre_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_centre_shots_against = (
            _parse_goal_keeper_nine_metre_centre_shots_against(
                d.pop("goalKeeperNineMetreCentreShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_centre_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_centre_shots_against_per_match = (
            _parse_goal_keeper_nine_metre_centre_shots_against_per_match(
                d.pop("goalKeeperNineMetreCentreShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_centre_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_centre_shots_saved = (
            _parse_goal_keeper_nine_metre_centre_shots_saved(
                d.pop("goalKeeperNineMetreCentreShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_centre_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_centre_shots_saved_per_match = (
            _parse_goal_keeper_nine_metre_centre_shots_saved_per_match(
                d.pop("goalKeeperNineMetreCentreShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_goals_against = (
            _parse_goal_keeper_nine_metre_goals_against(
                d.pop("goalKeeperNineMetreGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_goals_against_per_match = (
            _parse_goal_keeper_nine_metre_goals_against_per_match(
                d.pop("goalKeeperNineMetreGoalsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_left_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_left_goals_against = (
            _parse_goal_keeper_nine_metre_left_goals_against(
                d.pop("goalKeeperNineMetreLeftGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_left_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_left_goals_against_per_match = (
            _parse_goal_keeper_nine_metre_left_goals_against_per_match(
                d.pop("goalKeeperNineMetreLeftGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_nine_metre_left_save_accuracy = d.pop(
            "goalKeeperNineMetreLeftSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_nine_metre_left_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_left_save_accuracy_per_match = (
            _parse_goal_keeper_nine_metre_left_save_accuracy_per_match(
                d.pop("goalKeeperNineMetreLeftSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_left_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_left_shots_against = (
            _parse_goal_keeper_nine_metre_left_shots_against(
                d.pop("goalKeeperNineMetreLeftShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_left_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_left_shots_against_per_match = (
            _parse_goal_keeper_nine_metre_left_shots_against_per_match(
                d.pop("goalKeeperNineMetreLeftShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_left_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_left_shots_saved = (
            _parse_goal_keeper_nine_metre_left_shots_saved(
                d.pop("goalKeeperNineMetreLeftShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_left_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_left_shots_saved_per_match = (
            _parse_goal_keeper_nine_metre_left_shots_saved_per_match(
                d.pop("goalKeeperNineMetreLeftShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_right_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_right_goals_against = (
            _parse_goal_keeper_nine_metre_right_goals_against(
                d.pop("goalKeeperNineMetreRightGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_right_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_right_goals_against_per_match = (
            _parse_goal_keeper_nine_metre_right_goals_against_per_match(
                d.pop("goalKeeperNineMetreRightGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_nine_metre_right_save_accuracy = d.pop(
            "goalKeeperNineMetreRightSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_nine_metre_right_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_right_save_accuracy_per_match = (
            _parse_goal_keeper_nine_metre_right_save_accuracy_per_match(
                d.pop("goalKeeperNineMetreRightSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_right_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_right_shots_against = (
            _parse_goal_keeper_nine_metre_right_shots_against(
                d.pop("goalKeeperNineMetreRightShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_right_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_right_shots_against_per_match = (
            _parse_goal_keeper_nine_metre_right_shots_against_per_match(
                d.pop("goalKeeperNineMetreRightShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_right_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_right_shots_saved = (
            _parse_goal_keeper_nine_metre_right_shots_saved(
                d.pop("goalKeeperNineMetreRightShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_right_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_right_shots_saved_per_match = (
            _parse_goal_keeper_nine_metre_right_shots_saved_per_match(
                d.pop("goalKeeperNineMetreRightShotsSavedPerMatch", UNSET)
            )
        )

        goal_keeper_nine_metre_save_accuracy = d.pop(
            "goalKeeperNineMetreSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_nine_metre_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_save_accuracy_per_match = (
            _parse_goal_keeper_nine_metre_save_accuracy_per_match(
                d.pop("goalKeeperNineMetreSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_shots_against = (
            _parse_goal_keeper_nine_metre_shots_against(
                d.pop("goalKeeperNineMetreShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_shots_against_per_match = (
            _parse_goal_keeper_nine_metre_shots_against_per_match(
                d.pop("goalKeeperNineMetreShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_nine_metre_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_nine_metre_shots_saved = _parse_goal_keeper_nine_metre_shots_saved(
            d.pop("goalKeeperNineMetreShotsSaved", UNSET)
        )

        def _parse_goal_keeper_nine_metre_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_nine_metre_shots_saved_per_match = (
            _parse_goal_keeper_nine_metre_shots_saved_per_match(
                d.pop("goalKeeperNineMetreShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_pivot_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_pivot_goals_against = _parse_goal_keeper_pivot_goals_against(
            d.pop("goalKeeperPivotGoalsAgainst", UNSET)
        )

        def _parse_goal_keeper_pivot_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_pivot_goals_against_per_match = (
            _parse_goal_keeper_pivot_goals_against_per_match(
                d.pop("goalKeeperPivotGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_pivot_save_accuracy = d.pop("goalKeeperPivotSaveAccuracy", UNSET)

        def _parse_goal_keeper_pivot_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_pivot_save_accuracy_per_match = (
            _parse_goal_keeper_pivot_save_accuracy_per_match(
                d.pop("goalKeeperPivotSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_pivot_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_pivot_shots_against = _parse_goal_keeper_pivot_shots_against(
            d.pop("goalKeeperPivotShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_pivot_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_pivot_shots_against_per_match = (
            _parse_goal_keeper_pivot_shots_against_per_match(
                d.pop("goalKeeperPivotShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_pivot_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_pivot_shots_saved = _parse_goal_keeper_pivot_shots_saved(
            d.pop("goalKeeperPivotShotsSaved", UNSET)
        )

        def _parse_goal_keeper_pivot_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_pivot_shots_saved_per_match = (
            _parse_goal_keeper_pivot_shots_saved_per_match(
                d.pop("goalKeeperPivotShotsSavedPerMatch", UNSET)
            )
        )

        goal_keeper_save_accuracy = d.pop("goalKeeperSaveAccuracy", UNSET)

        def _parse_goal_keeper_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_save_accuracy_per_match = (
            _parse_goal_keeper_save_accuracy_per_match(
                d.pop("goalKeeperSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_seconds_played(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seconds_played = _parse_goal_keeper_seconds_played(
            d.pop("goalKeeperSecondsPlayed", UNSET)
        )

        def _parse_goal_keeper_seconds_played_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_seconds_played_per_match = (
            _parse_goal_keeper_seconds_played_per_match(
                d.pop("goalKeeperSecondsPlayedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_seven_metre_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seven_metre_goals_against = (
            _parse_goal_keeper_seven_metre_goals_against(
                d.pop("goalKeeperSevenMetreGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_seven_metre_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_seven_metre_goals_against_per_match = (
            _parse_goal_keeper_seven_metre_goals_against_per_match(
                d.pop("goalKeeperSevenMetreGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_seven_metre_save_accuracy = d.pop(
            "goalKeeperSevenMetreSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_seven_metre_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_seven_metre_save_accuracy_per_match = (
            _parse_goal_keeper_seven_metre_save_accuracy_per_match(
                d.pop("goalKeeperSevenMetreSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_seven_metre_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seven_metre_shots_against = (
            _parse_goal_keeper_seven_metre_shots_against(
                d.pop("goalKeeperSevenMetreShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_seven_metre_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_seven_metre_shots_against_per_match = (
            _parse_goal_keeper_seven_metre_shots_against_per_match(
                d.pop("goalKeeperSevenMetreShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_seven_metre_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_seven_metre_shots_saved = (
            _parse_goal_keeper_seven_metre_shots_saved(
                d.pop("goalKeeperSevenMetreShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_seven_metre_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_seven_metre_shots_saved_per_match = (
            _parse_goal_keeper_seven_metre_shots_saved_per_match(
                d.pop("goalKeeperSevenMetreShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_shots_against(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_shots_against = _parse_goal_keeper_shots_against(
            d.pop("goalKeeperShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_shots_against_per_match = (
            _parse_goal_keeper_shots_against_per_match(
                d.pop("goalKeeperShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_shots_per_goals_against(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_shots_per_goals_against = (
            _parse_goal_keeper_shots_per_goals_against(
                d.pop("goalKeeperShotsPerGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_shots_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_shots_saved = _parse_goal_keeper_shots_saved(
            d.pop("goalKeeperShotsSaved", UNSET)
        )

        def _parse_goal_keeper_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_shots_saved_per_match = _parse_goal_keeper_shots_saved_per_match(
            d.pop("goalKeeperShotsSavedPerMatch", UNSET)
        )

        def _parse_goal_keeper_six_metre_centre_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_centre_goals_against = (
            _parse_goal_keeper_six_metre_centre_goals_against(
                d.pop("goalKeeperSixMetreCentreGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_centre_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_centre_goals_against_per_match = (
            _parse_goal_keeper_six_metre_centre_goals_against_per_match(
                d.pop("goalKeeperSixMetreCentreGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_six_metre_centre_save_accuracy = d.pop(
            "goalKeeperSixMetreCentreSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_six_metre_centre_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_centre_save_accuracy_per_match = (
            _parse_goal_keeper_six_metre_centre_save_accuracy_per_match(
                d.pop("goalKeeperSixMetreCentreSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_centre_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_centre_shots_against = (
            _parse_goal_keeper_six_metre_centre_shots_against(
                d.pop("goalKeeperSixMetreCentreShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_centre_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_centre_shots_against_per_match = (
            _parse_goal_keeper_six_metre_centre_shots_against_per_match(
                d.pop("goalKeeperSixMetreCentreShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_centre_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_centre_shots_saved = (
            _parse_goal_keeper_six_metre_centre_shots_saved(
                d.pop("goalKeeperSixMetreCentreShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_centre_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_centre_shots_saved_per_match = (
            _parse_goal_keeper_six_metre_centre_shots_saved_per_match(
                d.pop("goalKeeperSixMetreCentreShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_goals_against = (
            _parse_goal_keeper_six_metre_goals_against(
                d.pop("goalKeeperSixMetreGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_goals_against_per_match = (
            _parse_goal_keeper_six_metre_goals_against_per_match(
                d.pop("goalKeeperSixMetreGoalsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_left_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_left_goals_against = (
            _parse_goal_keeper_six_metre_left_goals_against(
                d.pop("goalKeeperSixMetreLeftGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_left_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_left_goals_against_per_match = (
            _parse_goal_keeper_six_metre_left_goals_against_per_match(
                d.pop("goalKeeperSixMetreLeftGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_six_metre_left_save_accuracy = d.pop(
            "goalKeeperSixMetreLeftSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_six_metre_left_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_left_save_accuracy_per_match = (
            _parse_goal_keeper_six_metre_left_save_accuracy_per_match(
                d.pop("goalKeeperSixMetreLeftSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_left_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_left_shots_against = (
            _parse_goal_keeper_six_metre_left_shots_against(
                d.pop("goalKeeperSixMetreLeftShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_left_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_left_shots_against_per_match = (
            _parse_goal_keeper_six_metre_left_shots_against_per_match(
                d.pop("goalKeeperSixMetreLeftShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_left_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_left_shots_saved = (
            _parse_goal_keeper_six_metre_left_shots_saved(
                d.pop("goalKeeperSixMetreLeftShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_left_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_left_shots_saved_per_match = (
            _parse_goal_keeper_six_metre_left_shots_saved_per_match(
                d.pop("goalKeeperSixMetreLeftShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_right_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_right_goals_against = (
            _parse_goal_keeper_six_metre_right_goals_against(
                d.pop("goalKeeperSixMetreRightGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_right_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_right_goals_against_per_match = (
            _parse_goal_keeper_six_metre_right_goals_against_per_match(
                d.pop("goalKeeperSixMetreRightGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_six_metre_right_save_accuracy = d.pop(
            "goalKeeperSixMetreRightSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_six_metre_right_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_right_save_accuracy_per_match = (
            _parse_goal_keeper_six_metre_right_save_accuracy_per_match(
                d.pop("goalKeeperSixMetreRightSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_right_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_right_shots_against = (
            _parse_goal_keeper_six_metre_right_shots_against(
                d.pop("goalKeeperSixMetreRightShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_right_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_right_shots_against_per_match = (
            _parse_goal_keeper_six_metre_right_shots_against_per_match(
                d.pop("goalKeeperSixMetreRightShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_right_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_right_shots_saved = (
            _parse_goal_keeper_six_metre_right_shots_saved(
                d.pop("goalKeeperSixMetreRightShotsSaved", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_right_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_right_shots_saved_per_match = (
            _parse_goal_keeper_six_metre_right_shots_saved_per_match(
                d.pop("goalKeeperSixMetreRightShotsSavedPerMatch", UNSET)
            )
        )

        goal_keeper_six_metre_save_accuracy = d.pop(
            "goalKeeperSixMetreSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_six_metre_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_save_accuracy_per_match = (
            _parse_goal_keeper_six_metre_save_accuracy_per_match(
                d.pop("goalKeeperSixMetreSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_shots_against = (
            _parse_goal_keeper_six_metre_shots_against(
                d.pop("goalKeeperSixMetreShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_shots_against_per_match = (
            _parse_goal_keeper_six_metre_shots_against_per_match(
                d.pop("goalKeeperSixMetreShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_six_metre_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_six_metre_shots_saved = _parse_goal_keeper_six_metre_shots_saved(
            d.pop("goalKeeperSixMetreShotsSaved", UNSET)
        )

        def _parse_goal_keeper_six_metre_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_six_metre_shots_saved_per_match = (
            _parse_goal_keeper_six_metre_shots_saved_per_match(
                d.pop("goalKeeperSixMetreShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_goals_against = _parse_goal_keeper_wing_goals_against(
            d.pop("goalKeeperWingGoalsAgainst", UNSET)
        )

        def _parse_goal_keeper_wing_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_goals_against_per_match = (
            _parse_goal_keeper_wing_goals_against_per_match(
                d.pop("goalKeeperWingGoalsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_left_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_left_goals_against = (
            _parse_goal_keeper_wing_left_goals_against(
                d.pop("goalKeeperWingLeftGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_wing_left_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_left_goals_against_per_match = (
            _parse_goal_keeper_wing_left_goals_against_per_match(
                d.pop("goalKeeperWingLeftGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_wing_left_save_accuracy = d.pop(
            "goalKeeperWingLeftSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_wing_left_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_left_save_accuracy_per_match = (
            _parse_goal_keeper_wing_left_save_accuracy_per_match(
                d.pop("goalKeeperWingLeftSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_left_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_left_shots_against = (
            _parse_goal_keeper_wing_left_shots_against(
                d.pop("goalKeeperWingLeftShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_wing_left_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_left_shots_against_per_match = (
            _parse_goal_keeper_wing_left_shots_against_per_match(
                d.pop("goalKeeperWingLeftShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_left_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_left_shots_saved = _parse_goal_keeper_wing_left_shots_saved(
            d.pop("goalKeeperWingLeftShotsSaved", UNSET)
        )

        def _parse_goal_keeper_wing_left_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_left_shots_saved_per_match = (
            _parse_goal_keeper_wing_left_shots_saved_per_match(
                d.pop("goalKeeperWingLeftShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_right_goals_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_right_goals_against = (
            _parse_goal_keeper_wing_right_goals_against(
                d.pop("goalKeeperWingRightGoalsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_wing_right_goals_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_right_goals_against_per_match = (
            _parse_goal_keeper_wing_right_goals_against_per_match(
                d.pop("goalKeeperWingRightGoalsAgainstPerMatch", UNSET)
            )
        )

        goal_keeper_wing_right_save_accuracy = d.pop(
            "goalKeeperWingRightSaveAccuracy", UNSET
        )

        def _parse_goal_keeper_wing_right_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_right_save_accuracy_per_match = (
            _parse_goal_keeper_wing_right_save_accuracy_per_match(
                d.pop("goalKeeperWingRightSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_right_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_right_shots_against = (
            _parse_goal_keeper_wing_right_shots_against(
                d.pop("goalKeeperWingRightShotsAgainst", UNSET)
            )
        )

        def _parse_goal_keeper_wing_right_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_right_shots_against_per_match = (
            _parse_goal_keeper_wing_right_shots_against_per_match(
                d.pop("goalKeeperWingRightShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_right_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_right_shots_saved = _parse_goal_keeper_wing_right_shots_saved(
            d.pop("goalKeeperWingRightShotsSaved", UNSET)
        )

        def _parse_goal_keeper_wing_right_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_right_shots_saved_per_match = (
            _parse_goal_keeper_wing_right_shots_saved_per_match(
                d.pop("goalKeeperWingRightShotsSavedPerMatch", UNSET)
            )
        )

        goal_keeper_wing_save_accuracy = d.pop("goalKeeperWingSaveAccuracy", UNSET)

        def _parse_goal_keeper_wing_save_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_save_accuracy_per_match = (
            _parse_goal_keeper_wing_save_accuracy_per_match(
                d.pop("goalKeeperWingSaveAccuracyPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_shots_against(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_shots_against = _parse_goal_keeper_wing_shots_against(
            d.pop("goalKeeperWingShotsAgainst", UNSET)
        )

        def _parse_goal_keeper_wing_shots_against_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_shots_against_per_match = (
            _parse_goal_keeper_wing_shots_against_per_match(
                d.pop("goalKeeperWingShotsAgainstPerMatch", UNSET)
            )
        )

        def _parse_goal_keeper_wing_shots_saved(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goal_keeper_wing_shots_saved = _parse_goal_keeper_wing_shots_saved(
            d.pop("goalKeeperWingShotsSaved", UNSET)
        )

        def _parse_goal_keeper_wing_shots_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goal_keeper_wing_shots_saved_per_match = (
            _parse_goal_keeper_wing_shots_saved_per_match(
                d.pop("goalKeeperWingShotsSavedPerMatch", UNSET)
            )
        )

        def _parse_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        goals_scored = _parse_goals_scored(d.pop("goalsScored", UNSET))

        def _parse_goals_scored_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        goals_scored_per_match = _parse_goals_scored_per_match(
            d.pop("goalsScoredPerMatch", UNSET)
        )

        def _parse_handball_performance_index(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        handball_performance_index = _parse_handball_performance_index(
            d.pop("handballPerformanceIndex", UNSET)
        )

        def _parse_losses(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        losses = _parse_losses(d.pop("losses", UNSET))

        def _parse_matches_played(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        matches_played = _parse_matches_played(d.pop("matchesPlayed", UNSET))

        def _parse_minutes(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        minutes = _parse_minutes(d.pop("minutes", UNSET))

        def _parse_minutes_per_match(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        minutes_per_match = _parse_minutes_per_match(d.pop("minutesPerMatch", UNSET))

        def _parse_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        missed_shots = _parse_missed_shots(d.pop("missedShots", UNSET))

        def _parse_missed_shots_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        missed_shots_per_match = _parse_missed_shots_per_match(
            d.pop("missedShotsPerMatch", UNSET)
        )

        def _parse_nine_metre_centre_goals_scored(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_goals_scored = _parse_nine_metre_centre_goals_scored(
            d.pop("nineMetreCentreGoalsScored", UNSET)
        )

        def _parse_nine_metre_centre_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_centre_goals_scored_per_match = (
            _parse_nine_metre_centre_goals_scored_per_match(
                d.pop("nineMetreCentreGoalsScoredPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_centre_missed_shots(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_missed_shots = _parse_nine_metre_centre_missed_shots(
            d.pop("nineMetreCentreMissedShots", UNSET)
        )

        def _parse_nine_metre_centre_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_centre_missed_shots_per_match = (
            _parse_nine_metre_centre_missed_shots_per_match(
                d.pop("nineMetreCentreMissedShotsPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_centre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_post_hits = _parse_nine_metre_centre_post_hits(
            d.pop("nineMetreCentrePostHits", UNSET)
        )

        def _parse_nine_metre_centre_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_centre_post_hits_per_match = (
            _parse_nine_metre_centre_post_hits_per_match(
                d.pop("nineMetreCentrePostHitsPerMatch", UNSET)
            )
        )

        nine_metre_centre_shooting_accuracy = d.pop(
            "nineMetreCentreShootingAccuracy", UNSET
        )

        def _parse_nine_metre_centre_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_centre_shooting_accuracy_per_match = (
            _parse_nine_metre_centre_shooting_accuracy_per_match(
                d.pop("nineMetreCentreShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_centre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_shots = _parse_nine_metre_centre_shots(
            d.pop("nineMetreCentreShots", UNSET)
        )

        def _parse_nine_metre_centre_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_centre_shots_per_match = _parse_nine_metre_centre_shots_per_match(
            d.pop("nineMetreCentreShotsPerMatch", UNSET)
        )

        def _parse_nine_metre_centre_shots_blocked(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_shots_blocked = _parse_nine_metre_centre_shots_blocked(
            d.pop("nineMetreCentreShotsBlocked", UNSET)
        )

        def _parse_nine_metre_centre_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_centre_shots_blocked_per_match = (
            _parse_nine_metre_centre_shots_blocked_per_match(
                d.pop("nineMetreCentreShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_centre_shots_on_goal(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_centre_shots_on_goal = _parse_nine_metre_centre_shots_on_goal(
            d.pop("nineMetreCentreShotsOnGoal", UNSET)
        )

        def _parse_nine_metre_centre_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_centre_shots_on_goal_per_match = (
            _parse_nine_metre_centre_shots_on_goal_per_match(
                d.pop("nineMetreCentreShotsOnGoalPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_goals_scored = _parse_nine_metre_goals_scored(
            d.pop("nineMetreGoalsScored", UNSET)
        )

        def _parse_nine_metre_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_goals_scored_per_match = _parse_nine_metre_goals_scored_per_match(
            d.pop("nineMetreGoalsScoredPerMatch", UNSET)
        )

        def _parse_nine_metre_left_goals_scored(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_goals_scored = _parse_nine_metre_left_goals_scored(
            d.pop("nineMetreLeftGoalsScored", UNSET)
        )

        def _parse_nine_metre_left_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_left_goals_scored_per_match = (
            _parse_nine_metre_left_goals_scored_per_match(
                d.pop("nineMetreLeftGoalsScoredPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_left_missed_shots(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_missed_shots = _parse_nine_metre_left_missed_shots(
            d.pop("nineMetreLeftMissedShots", UNSET)
        )

        def _parse_nine_metre_left_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_left_missed_shots_per_match = (
            _parse_nine_metre_left_missed_shots_per_match(
                d.pop("nineMetreLeftMissedShotsPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_left_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_post_hits = _parse_nine_metre_left_post_hits(
            d.pop("nineMetreLeftPostHits", UNSET)
        )

        def _parse_nine_metre_left_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_left_post_hits_per_match = (
            _parse_nine_metre_left_post_hits_per_match(
                d.pop("nineMetreLeftPostHitsPerMatch", UNSET)
            )
        )

        nine_metre_left_shooting_accuracy = d.pop(
            "nineMetreLeftShootingAccuracy", UNSET
        )

        def _parse_nine_metre_left_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_left_shooting_accuracy_per_match = (
            _parse_nine_metre_left_shooting_accuracy_per_match(
                d.pop("nineMetreLeftShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_left_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_shots = _parse_nine_metre_left_shots(
            d.pop("nineMetreLeftShots", UNSET)
        )

        def _parse_nine_metre_left_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_left_shots_per_match = _parse_nine_metre_left_shots_per_match(
            d.pop("nineMetreLeftShotsPerMatch", UNSET)
        )

        def _parse_nine_metre_left_shots_blocked(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_shots_blocked = _parse_nine_metre_left_shots_blocked(
            d.pop("nineMetreLeftShotsBlocked", UNSET)
        )

        def _parse_nine_metre_left_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_left_shots_blocked_per_match = (
            _parse_nine_metre_left_shots_blocked_per_match(
                d.pop("nineMetreLeftShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_left_shots_on_goal(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_left_shots_on_goal = _parse_nine_metre_left_shots_on_goal(
            d.pop("nineMetreLeftShotsOnGoal", UNSET)
        )

        def _parse_nine_metre_left_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_left_shots_on_goal_per_match = (
            _parse_nine_metre_left_shots_on_goal_per_match(
                d.pop("nineMetreLeftShotsOnGoalPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_missed_shots = _parse_nine_metre_missed_shots(
            d.pop("nineMetreMissedShots", UNSET)
        )

        def _parse_nine_metre_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_missed_shots_per_match = _parse_nine_metre_missed_shots_per_match(
            d.pop("nineMetreMissedShotsPerMatch", UNSET)
        )

        def _parse_nine_metre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_post_hits = _parse_nine_metre_post_hits(
            d.pop("nineMetrePostHits", UNSET)
        )

        def _parse_nine_metre_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_post_hits_per_match = _parse_nine_metre_post_hits_per_match(
            d.pop("nineMetrePostHitsPerMatch", UNSET)
        )

        def _parse_nine_metre_right_goals_scored(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_goals_scored = _parse_nine_metre_right_goals_scored(
            d.pop("nineMetreRightGoalsScored", UNSET)
        )

        def _parse_nine_metre_right_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_right_goals_scored_per_match = (
            _parse_nine_metre_right_goals_scored_per_match(
                d.pop("nineMetreRightGoalsScoredPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_right_missed_shots(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_missed_shots = _parse_nine_metre_right_missed_shots(
            d.pop("nineMetreRightMissedShots", UNSET)
        )

        def _parse_nine_metre_right_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_right_missed_shots_per_match = (
            _parse_nine_metre_right_missed_shots_per_match(
                d.pop("nineMetreRightMissedShotsPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_right_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_post_hits = _parse_nine_metre_right_post_hits(
            d.pop("nineMetreRightPostHits", UNSET)
        )

        def _parse_nine_metre_right_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_right_post_hits_per_match = (
            _parse_nine_metre_right_post_hits_per_match(
                d.pop("nineMetreRightPostHitsPerMatch", UNSET)
            )
        )

        nine_metre_right_shooting_accuracy = d.pop(
            "nineMetreRightShootingAccuracy", UNSET
        )

        def _parse_nine_metre_right_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_right_shooting_accuracy_per_match = (
            _parse_nine_metre_right_shooting_accuracy_per_match(
                d.pop("nineMetreRightShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_right_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_shots = _parse_nine_metre_right_shots(
            d.pop("nineMetreRightShots", UNSET)
        )

        def _parse_nine_metre_right_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_right_shots_per_match = _parse_nine_metre_right_shots_per_match(
            d.pop("nineMetreRightShotsPerMatch", UNSET)
        )

        def _parse_nine_metre_right_shots_blocked(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_shots_blocked = _parse_nine_metre_right_shots_blocked(
            d.pop("nineMetreRightShotsBlocked", UNSET)
        )

        def _parse_nine_metre_right_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_right_shots_blocked_per_match = (
            _parse_nine_metre_right_shots_blocked_per_match(
                d.pop("nineMetreRightShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_right_shots_on_goal(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_right_shots_on_goal = _parse_nine_metre_right_shots_on_goal(
            d.pop("nineMetreRightShotsOnGoal", UNSET)
        )

        def _parse_nine_metre_right_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_right_shots_on_goal_per_match = (
            _parse_nine_metre_right_shots_on_goal_per_match(
                d.pop("nineMetreRightShotsOnGoalPerMatch", UNSET)
            )
        )

        nine_metre_shooting_accuracy = d.pop("nineMetreShootingAccuracy", UNSET)

        def _parse_nine_metre_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_shooting_accuracy_per_match = (
            _parse_nine_metre_shooting_accuracy_per_match(
                d.pop("nineMetreShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_nine_metre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_shots = _parse_nine_metre_shots(d.pop("nineMetreShots", UNSET))

        def _parse_nine_metre_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_shots_per_match = _parse_nine_metre_shots_per_match(
            d.pop("nineMetreShotsPerMatch", UNSET)
        )

        def _parse_nine_metre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_shots_blocked = _parse_nine_metre_shots_blocked(
            d.pop("nineMetreShotsBlocked", UNSET)
        )

        def _parse_nine_metre_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_shots_blocked_per_match = _parse_nine_metre_shots_blocked_per_match(
            d.pop("nineMetreShotsBlockedPerMatch", UNSET)
        )

        def _parse_nine_metre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        nine_metre_shots_on_goal = _parse_nine_metre_shots_on_goal(
            d.pop("nineMetreShotsOnGoal", UNSET)
        )

        def _parse_nine_metre_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        nine_metre_shots_on_goal_per_match = _parse_nine_metre_shots_on_goal_per_match(
            d.pop("nineMetreShotsOnGoalPerMatch", UNSET)
        )

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

        def _parse_pivot_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pivot_goals_scored_per_match = _parse_pivot_goals_scored_per_match(
            d.pop("pivotGoalsScoredPerMatch", UNSET)
        )

        def _parse_pivot_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_missed_shots = _parse_pivot_missed_shots(d.pop("pivotMissedShots", UNSET))

        def _parse_pivot_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pivot_missed_shots_per_match = _parse_pivot_missed_shots_per_match(
            d.pop("pivotMissedShotsPerMatch", UNSET)
        )

        def _parse_pivot_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_post_hits = _parse_pivot_post_hits(d.pop("pivotPostHits", UNSET))

        def _parse_pivot_post_hits_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pivot_post_hits_per_match = _parse_pivot_post_hits_per_match(
            d.pop("pivotPostHitsPerMatch", UNSET)
        )

        pivot_shooting_accuracy = d.pop("pivotShootingAccuracy", UNSET)

        def _parse_pivot_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pivot_shooting_accuracy_per_match = _parse_pivot_shooting_accuracy_per_match(
            d.pop("pivotShootingAccuracyPerMatch", UNSET)
        )

        def _parse_pivot_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_shots = _parse_pivot_shots(d.pop("pivotShots", UNSET))

        def _parse_pivot_shots_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pivot_shots_per_match = _parse_pivot_shots_per_match(
            d.pop("pivotShotsPerMatch", UNSET)
        )

        def _parse_pivot_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_shots_blocked = _parse_pivot_shots_blocked(
            d.pop("pivotShotsBlocked", UNSET)
        )

        def _parse_pivot_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pivot_shots_blocked_per_match = _parse_pivot_shots_blocked_per_match(
            d.pop("pivotShotsBlockedPerMatch", UNSET)
        )

        def _parse_pivot_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        pivot_shots_on_goal = _parse_pivot_shots_on_goal(
            d.pop("pivotShotsOnGoal", UNSET)
        )

        def _parse_pivot_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        pivot_shots_on_goal_per_match = _parse_pivot_shots_on_goal_per_match(
            d.pop("pivotShotsOnGoalPerMatch", UNSET)
        )

        def _parse_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        post_hits = _parse_post_hits(d.pop("postHits", UNSET))

        def _parse_post_hits_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        post_hits_per_match = _parse_post_hits_per_match(
            d.pop("postHitsPerMatch", UNSET)
        )

        def _parse_red_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        red_cards = _parse_red_cards(d.pop("redCards", UNSET))

        def _parse_red_cards_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        red_cards_per_match = _parse_red_cards_per_match(
            d.pop("redCardsPerMatch", UNSET)
        )

        def _parse_seven_metre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_goals_scored = _parse_seven_metre_goals_scored(
            d.pop("sevenMetreGoalsScored", UNSET)
        )

        def _parse_seven_metre_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_goals_scored_per_match = _parse_seven_metre_goals_scored_per_match(
            d.pop("sevenMetreGoalsScoredPerMatch", UNSET)
        )

        def _parse_seven_metre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_missed_shots = _parse_seven_metre_missed_shots(
            d.pop("sevenMetreMissedShots", UNSET)
        )

        def _parse_seven_metre_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_missed_shots_per_match = _parse_seven_metre_missed_shots_per_match(
            d.pop("sevenMetreMissedShotsPerMatch", UNSET)
        )

        def _parse_seven_metre_penalties_awarded(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_penalties_awarded = _parse_seven_metre_penalties_awarded(
            d.pop("sevenMetrePenaltiesAwarded", UNSET)
        )

        def _parse_seven_metre_penalties_awarded_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_penalties_awarded_per_match = (
            _parse_seven_metre_penalties_awarded_per_match(
                d.pop("sevenMetrePenaltiesAwardedPerMatch", UNSET)
            )
        )

        def _parse_seven_metre_penalties_caused(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_penalties_caused = _parse_seven_metre_penalties_caused(
            d.pop("sevenMetrePenaltiesCaused", UNSET)
        )

        def _parse_seven_metre_penalties_caused_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_penalties_caused_per_match = (
            _parse_seven_metre_penalties_caused_per_match(
                d.pop("sevenMetrePenaltiesCausedPerMatch", UNSET)
            )
        )

        def _parse_seven_metre_penalty_fouls(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_penalty_fouls = _parse_seven_metre_penalty_fouls(
            d.pop("sevenMetrePenaltyFouls", UNSET)
        )

        def _parse_seven_metre_penalty_fouls_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_penalty_fouls_per_match = (
            _parse_seven_metre_penalty_fouls_per_match(
                d.pop("sevenMetrePenaltyFoulsPerMatch", UNSET)
            )
        )

        def _parse_seven_metre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_post_hits = _parse_seven_metre_post_hits(
            d.pop("sevenMetrePostHits", UNSET)
        )

        def _parse_seven_metre_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_post_hits_per_match = _parse_seven_metre_post_hits_per_match(
            d.pop("sevenMetrePostHitsPerMatch", UNSET)
        )

        seven_metre_shooting_accuracy = d.pop("sevenMetreShootingAccuracy", UNSET)

        def _parse_seven_metre_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_shooting_accuracy_per_match = (
            _parse_seven_metre_shooting_accuracy_per_match(
                d.pop("sevenMetreShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_seven_metre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_shots = _parse_seven_metre_shots(d.pop("sevenMetreShots", UNSET))

        def _parse_seven_metre_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_shots_per_match = _parse_seven_metre_shots_per_match(
            d.pop("sevenMetreShotsPerMatch", UNSET)
        )

        def _parse_seven_metre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_shots_blocked = _parse_seven_metre_shots_blocked(
            d.pop("sevenMetreShotsBlocked", UNSET)
        )

        def _parse_seven_metre_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_shots_blocked_per_match = (
            _parse_seven_metre_shots_blocked_per_match(
                d.pop("sevenMetreShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_seven_metre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seven_metre_shots_on_goal = _parse_seven_metre_shots_on_goal(
            d.pop("sevenMetreShotsOnGoal", UNSET)
        )

        def _parse_seven_metre_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        seven_metre_shots_on_goal_per_match = (
            _parse_seven_metre_shots_on_goal_per_match(
                d.pop("sevenMetreShotsOnGoalPerMatch", UNSET)
            )
        )

        shooting_accuracy = d.pop("shootingAccuracy", UNSET)

        def _parse_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shooting_accuracy_per_match = _parse_shooting_accuracy_per_match(
            d.pop("shootingAccuracyPerMatch", UNSET)
        )

        def _parse_shoot_outs(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs = _parse_shoot_outs(d.pop("shootOuts", UNSET))

        def _parse_shoot_outs_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_outs_per_match = _parse_shoot_outs_per_match(
            d.pop("shootOutsPerMatch", UNSET)
        )

        def _parse_shoot_outs_made(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs_made = _parse_shoot_outs_made(d.pop("shootOutsMade", UNSET))

        def _parse_shoot_outs_made_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_outs_made_per_match = _parse_shoot_outs_made_per_match(
            d.pop("shootOutsMadePerMatch", UNSET)
        )

        def _parse_shoot_outs_missed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs_missed = _parse_shoot_outs_missed(d.pop("shootOutsMissed", UNSET))

        def _parse_shoot_outs_missed_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_outs_missed_per_match = _parse_shoot_outs_missed_per_match(
            d.pop("shootOutsMissedPerMatch", UNSET)
        )

        def _parse_shoot_outs_saved(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shoot_outs_saved = _parse_shoot_outs_saved(d.pop("shootOutsSaved", UNSET))

        def _parse_shoot_outs_saved_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shoot_outs_saved_per_match = _parse_shoot_outs_saved_per_match(
            d.pop("shootOutsSavedPerMatch", UNSET)
        )

        def _parse_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots = _parse_shots(d.pop("shots", UNSET))

        def _parse_shots_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shots_per_match = _parse_shots_per_match(d.pop("shotsPerMatch", UNSET))

        def _parse_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots_blocked = _parse_shots_blocked(d.pop("shotsBlocked", UNSET))

        def _parse_shots_blocked_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shots_blocked_per_match = _parse_shots_blocked_per_match(
            d.pop("shotsBlockedPerMatch", UNSET)
        )

        def _parse_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots_on_goal = _parse_shots_on_goal(d.pop("shotsOnGoal", UNSET))

        def _parse_shots_on_goal_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shots_on_goal_per_match = _parse_shots_on_goal_per_match(
            d.pop("shotsOnGoalPerMatch", UNSET)
        )

        def _parse_shots_saved_by_goal_keeper(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        shots_saved_by_goal_keeper = _parse_shots_saved_by_goal_keeper(
            d.pop("shotsSavedByGoalKeeper", UNSET)
        )

        def _parse_shots_saved_by_goal_keeper_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        shots_saved_by_goal_keeper_per_match = (
            _parse_shots_saved_by_goal_keeper_per_match(
                d.pop("shotsSavedByGoalKeeperPerMatch", UNSET)
            )
        )

        def _parse_six_metre_centre_goals_scored(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_goals_scored = _parse_six_metre_centre_goals_scored(
            d.pop("sixMetreCentreGoalsScored", UNSET)
        )

        def _parse_six_metre_centre_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_centre_goals_scored_per_match = (
            _parse_six_metre_centre_goals_scored_per_match(
                d.pop("sixMetreCentreGoalsScoredPerMatch", UNSET)
            )
        )

        def _parse_six_metre_centre_missed_shots(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_missed_shots = _parse_six_metre_centre_missed_shots(
            d.pop("sixMetreCentreMissedShots", UNSET)
        )

        def _parse_six_metre_centre_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_centre_missed_shots_per_match = (
            _parse_six_metre_centre_missed_shots_per_match(
                d.pop("sixMetreCentreMissedShotsPerMatch", UNSET)
            )
        )

        def _parse_six_metre_centre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_post_hits = _parse_six_metre_centre_post_hits(
            d.pop("sixMetreCentrePostHits", UNSET)
        )

        def _parse_six_metre_centre_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_centre_post_hits_per_match = (
            _parse_six_metre_centre_post_hits_per_match(
                d.pop("sixMetreCentrePostHitsPerMatch", UNSET)
            )
        )

        six_metre_centre_shooting_accuracy = d.pop(
            "sixMetreCentreShootingAccuracy", UNSET
        )

        def _parse_six_metre_centre_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_centre_shooting_accuracy_per_match = (
            _parse_six_metre_centre_shooting_accuracy_per_match(
                d.pop("sixMetreCentreShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_six_metre_centre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_shots = _parse_six_metre_centre_shots(
            d.pop("sixMetreCentreShots", UNSET)
        )

        def _parse_six_metre_centre_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_centre_shots_per_match = _parse_six_metre_centre_shots_per_match(
            d.pop("sixMetreCentreShotsPerMatch", UNSET)
        )

        def _parse_six_metre_centre_shots_blocked(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_shots_blocked = _parse_six_metre_centre_shots_blocked(
            d.pop("sixMetreCentreShotsBlocked", UNSET)
        )

        def _parse_six_metre_centre_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_centre_shots_blocked_per_match = (
            _parse_six_metre_centre_shots_blocked_per_match(
                d.pop("sixMetreCentreShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_six_metre_centre_shots_on_goal(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_centre_shots_on_goal = _parse_six_metre_centre_shots_on_goal(
            d.pop("sixMetreCentreShotsOnGoal", UNSET)
        )

        def _parse_six_metre_centre_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_centre_shots_on_goal_per_match = (
            _parse_six_metre_centre_shots_on_goal_per_match(
                d.pop("sixMetreCentreShotsOnGoalPerMatch", UNSET)
            )
        )

        def _parse_six_metre_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_goals_scored = _parse_six_metre_goals_scored(
            d.pop("sixMetreGoalsScored", UNSET)
        )

        def _parse_six_metre_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_goals_scored_per_match = _parse_six_metre_goals_scored_per_match(
            d.pop("sixMetreGoalsScoredPerMatch", UNSET)
        )

        def _parse_six_metre_left_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_goals_scored = _parse_six_metre_left_goals_scored(
            d.pop("sixMetreLeftGoalsScored", UNSET)
        )

        def _parse_six_metre_left_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_left_goals_scored_per_match = (
            _parse_six_metre_left_goals_scored_per_match(
                d.pop("sixMetreLeftGoalsScoredPerMatch", UNSET)
            )
        )

        def _parse_six_metre_left_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_missed_shots = _parse_six_metre_left_missed_shots(
            d.pop("sixMetreLeftMissedShots", UNSET)
        )

        def _parse_six_metre_left_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_left_missed_shots_per_match = (
            _parse_six_metre_left_missed_shots_per_match(
                d.pop("sixMetreLeftMissedShotsPerMatch", UNSET)
            )
        )

        def _parse_six_metre_left_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_post_hits = _parse_six_metre_left_post_hits(
            d.pop("sixMetreLeftPostHits", UNSET)
        )

        def _parse_six_metre_left_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_left_post_hits_per_match = _parse_six_metre_left_post_hits_per_match(
            d.pop("sixMetreLeftPostHitsPerMatch", UNSET)
        )

        six_metre_left_shooting_accuracy = d.pop("sixMetreLeftShootingAccuracy", UNSET)

        def _parse_six_metre_left_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_left_shooting_accuracy_per_match = (
            _parse_six_metre_left_shooting_accuracy_per_match(
                d.pop("sixMetreLeftShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_six_metre_left_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_shots = _parse_six_metre_left_shots(
            d.pop("sixMetreLeftShots", UNSET)
        )

        def _parse_six_metre_left_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_left_shots_per_match = _parse_six_metre_left_shots_per_match(
            d.pop("sixMetreLeftShotsPerMatch", UNSET)
        )

        def _parse_six_metre_left_shots_blocked(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_shots_blocked = _parse_six_metre_left_shots_blocked(
            d.pop("sixMetreLeftShotsBlocked", UNSET)
        )

        def _parse_six_metre_left_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_left_shots_blocked_per_match = (
            _parse_six_metre_left_shots_blocked_per_match(
                d.pop("sixMetreLeftShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_six_metre_left_shots_on_goal(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_left_shots_on_goal = _parse_six_metre_left_shots_on_goal(
            d.pop("sixMetreLeftShotsOnGoal", UNSET)
        )

        def _parse_six_metre_left_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_left_shots_on_goal_per_match = (
            _parse_six_metre_left_shots_on_goal_per_match(
                d.pop("sixMetreLeftShotsOnGoalPerMatch", UNSET)
            )
        )

        def _parse_six_metre_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_missed_shots = _parse_six_metre_missed_shots(
            d.pop("sixMetreMissedShots", UNSET)
        )

        def _parse_six_metre_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_missed_shots_per_match = _parse_six_metre_missed_shots_per_match(
            d.pop("sixMetreMissedShotsPerMatch", UNSET)
        )

        def _parse_six_metre_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_post_hits = _parse_six_metre_post_hits(
            d.pop("sixMetrePostHits", UNSET)
        )

        def _parse_six_metre_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_post_hits_per_match = _parse_six_metre_post_hits_per_match(
            d.pop("sixMetrePostHitsPerMatch", UNSET)
        )

        def _parse_six_metre_right_goals_scored(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_goals_scored = _parse_six_metre_right_goals_scored(
            d.pop("sixMetreRightGoalsScored", UNSET)
        )

        def _parse_six_metre_right_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_right_goals_scored_per_match = (
            _parse_six_metre_right_goals_scored_per_match(
                d.pop("sixMetreRightGoalsScoredPerMatch", UNSET)
            )
        )

        def _parse_six_metre_right_missed_shots(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_missed_shots = _parse_six_metre_right_missed_shots(
            d.pop("sixMetreRightMissedShots", UNSET)
        )

        def _parse_six_metre_right_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_right_missed_shots_per_match = (
            _parse_six_metre_right_missed_shots_per_match(
                d.pop("sixMetreRightMissedShotsPerMatch", UNSET)
            )
        )

        def _parse_six_metre_right_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_post_hits = _parse_six_metre_right_post_hits(
            d.pop("sixMetreRightPostHits", UNSET)
        )

        def _parse_six_metre_right_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_right_post_hits_per_match = (
            _parse_six_metre_right_post_hits_per_match(
                d.pop("sixMetreRightPostHitsPerMatch", UNSET)
            )
        )

        six_metre_right_shooting_accuracy = d.pop(
            "sixMetreRightShootingAccuracy", UNSET
        )

        def _parse_six_metre_right_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_right_shooting_accuracy_per_match = (
            _parse_six_metre_right_shooting_accuracy_per_match(
                d.pop("sixMetreRightShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_six_metre_right_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_shots = _parse_six_metre_right_shots(
            d.pop("sixMetreRightShots", UNSET)
        )

        def _parse_six_metre_right_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_right_shots_per_match = _parse_six_metre_right_shots_per_match(
            d.pop("sixMetreRightShotsPerMatch", UNSET)
        )

        def _parse_six_metre_right_shots_blocked(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_shots_blocked = _parse_six_metre_right_shots_blocked(
            d.pop("sixMetreRightShotsBlocked", UNSET)
        )

        def _parse_six_metre_right_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_right_shots_blocked_per_match = (
            _parse_six_metre_right_shots_blocked_per_match(
                d.pop("sixMetreRightShotsBlockedPerMatch", UNSET)
            )
        )

        def _parse_six_metre_right_shots_on_goal(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_right_shots_on_goal = _parse_six_metre_right_shots_on_goal(
            d.pop("sixMetreRightShotsOnGoal", UNSET)
        )

        def _parse_six_metre_right_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_right_shots_on_goal_per_match = (
            _parse_six_metre_right_shots_on_goal_per_match(
                d.pop("sixMetreRightShotsOnGoalPerMatch", UNSET)
            )
        )

        six_metre_shooting_accuracy = d.pop("sixMetreShootingAccuracy", UNSET)

        def _parse_six_metre_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_shooting_accuracy_per_match = (
            _parse_six_metre_shooting_accuracy_per_match(
                d.pop("sixMetreShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_six_metre_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_shots = _parse_six_metre_shots(d.pop("sixMetreShots", UNSET))

        def _parse_six_metre_shots_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_shots_per_match = _parse_six_metre_shots_per_match(
            d.pop("sixMetreShotsPerMatch", UNSET)
        )

        def _parse_six_metre_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_shots_blocked = _parse_six_metre_shots_blocked(
            d.pop("sixMetreShotsBlocked", UNSET)
        )

        def _parse_six_metre_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_shots_blocked_per_match = _parse_six_metre_shots_blocked_per_match(
            d.pop("sixMetreShotsBlockedPerMatch", UNSET)
        )

        def _parse_six_metre_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        six_metre_shots_on_goal = _parse_six_metre_shots_on_goal(
            d.pop("sixMetreShotsOnGoal", UNSET)
        )

        def _parse_six_metre_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        six_metre_shots_on_goal_per_match = _parse_six_metre_shots_on_goal_per_match(
            d.pop("sixMetreShotsOnGoalPerMatch", UNSET)
        )

        def _parse_speed_distance_per_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        speed_distance_per_time = _parse_speed_distance_per_time(
            d.pop("speedDistancePerTime", UNSET)
        )

        def _parse_speed_max(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        speed_max = _parse_speed_max(d.pop("speedMax", UNSET))

        def _parse_steals(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        steals = _parse_steals(d.pop("steals", UNSET))

        def _parse_steals_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        steals_per_match = _parse_steals_per_match(d.pop("stealsPerMatch", UNSET))

        def _parse_substitutions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        substitutions = _parse_substitutions(d.pop("substitutions", UNSET))

        def _parse_substitutions_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        substitutions_per_match = _parse_substitutions_per_match(
            d.pop("substitutionsPerMatch", UNSET)
        )

        def _parse_suspensions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        suspensions = _parse_suspensions(d.pop("suspensions", UNSET))

        def _parse_suspensions_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        suspensions_per_match = _parse_suspensions_per_match(
            d.pop("suspensionsPerMatch", UNSET)
        )

        def _parse_technical_ball_faults(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        technical_ball_faults = _parse_technical_ball_faults(
            d.pop("technicalBallFaults", UNSET)
        )

        def _parse_technical_ball_faults_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        technical_ball_faults_per_match = _parse_technical_ball_faults_per_match(
            d.pop("technicalBallFaultsPerMatch", UNSET)
        )

        def _parse_technical_faults(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        technical_faults = _parse_technical_faults(d.pop("technicalFaults", UNSET))

        def _parse_technical_faults_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        technical_faults_per_match = _parse_technical_faults_per_match(
            d.pop("technicalFaultsPerMatch", UNSET)
        )

        def _parse_technical_rule_faults(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        technical_rule_faults = _parse_technical_rule_faults(
            d.pop("technicalRuleFaults", UNSET)
        )

        def _parse_technical_rule_faults_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        technical_rule_faults_per_match = _parse_technical_rule_faults_per_match(
            d.pop("technicalRuleFaultsPerMatch", UNSET)
        )

        def _parse_time_on_playing_field(
            data: object,
        ) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        time_on_playing_field = _parse_time_on_playing_field(
            d.pop("timeOnPlayingField", UNSET)
        )

        def _parse_time_ball_possession(data: object) -> Union[None, Unset, float, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float, str], data)

        time_ball_possession = _parse_time_ball_possession(
            d.pop("timeBallPossession", UNSET)
        )

        def _parse_time_played(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        time_played = _parse_time_played(d.pop("timePlayed", UNSET))

        def _parse_time_played_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        time_played_per_match = _parse_time_played_per_match(
            d.pop("timePlayedPerMatch", UNSET)
        )

        def _parse_turnovers(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        turnovers = _parse_turnovers(d.pop("turnovers", UNSET))

        def _parse_turnovers_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        turnovers_per_match = _parse_turnovers_per_match(
            d.pop("turnoversPerMatch", UNSET)
        )

        def _parse_two_minute_suspensions(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        two_minute_suspensions = _parse_two_minute_suspensions(
            d.pop("twoMinuteSuspensions", UNSET)
        )

        def _parse_two_minute_suspensions_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        two_minute_suspensions_per_match = _parse_two_minute_suspensions_per_match(
            d.pop("twoMinuteSuspensionsPerMatch", UNSET)
        )

        def _parse_wing_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_goals_scored = _parse_wing_goals_scored(d.pop("wingGoalsScored", UNSET))

        def _parse_wing_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_goals_scored_per_match = _parse_wing_goals_scored_per_match(
            d.pop("wingGoalsScoredPerMatch", UNSET)
        )

        def _parse_wing_left_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_goals_scored = _parse_wing_left_goals_scored(
            d.pop("wingLeftGoalsScored", UNSET)
        )

        def _parse_wing_left_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_left_goals_scored_per_match = _parse_wing_left_goals_scored_per_match(
            d.pop("wingLeftGoalsScoredPerMatch", UNSET)
        )

        def _parse_wing_left_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_missed_shots = _parse_wing_left_missed_shots(
            d.pop("wingLeftMissedShots", UNSET)
        )

        def _parse_wing_left_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_left_missed_shots_per_match = _parse_wing_left_missed_shots_per_match(
            d.pop("wingLeftMissedShotsPerMatch", UNSET)
        )

        def _parse_wing_left_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_post_hits = _parse_wing_left_post_hits(
            d.pop("wingLeftPostHits", UNSET)
        )

        def _parse_wing_left_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_left_post_hits_per_match = _parse_wing_left_post_hits_per_match(
            d.pop("wingLeftPostHitsPerMatch", UNSET)
        )

        wing_left_shooting_accuracy = d.pop("wingLeftShootingAccuracy", UNSET)

        def _parse_wing_left_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_left_shooting_accuracy_per_match = (
            _parse_wing_left_shooting_accuracy_per_match(
                d.pop("wingLeftShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_wing_left_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_shots = _parse_wing_left_shots(d.pop("wingLeftShots", UNSET))

        def _parse_wing_left_shots_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_left_shots_per_match = _parse_wing_left_shots_per_match(
            d.pop("wingLeftShotsPerMatch", UNSET)
        )

        def _parse_wing_left_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_shots_blocked = _parse_wing_left_shots_blocked(
            d.pop("wingLeftShotsBlocked", UNSET)
        )

        def _parse_wing_left_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_left_shots_blocked_per_match = _parse_wing_left_shots_blocked_per_match(
            d.pop("wingLeftShotsBlockedPerMatch", UNSET)
        )

        def _parse_wing_left_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_left_shots_on_goal = _parse_wing_left_shots_on_goal(
            d.pop("wingLeftShotsOnGoal", UNSET)
        )

        def _parse_wing_left_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_left_shots_on_goal_per_match = _parse_wing_left_shots_on_goal_per_match(
            d.pop("wingLeftShotsOnGoalPerMatch", UNSET)
        )

        def _parse_wing_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_missed_shots = _parse_wing_missed_shots(d.pop("wingMissedShots", UNSET))

        def _parse_wing_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_missed_shots_per_match = _parse_wing_missed_shots_per_match(
            d.pop("wingMissedShotsPerMatch", UNSET)
        )

        def _parse_wing_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_post_hits = _parse_wing_post_hits(d.pop("wingPostHits", UNSET))

        def _parse_wing_post_hits_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_post_hits_per_match = _parse_wing_post_hits_per_match(
            d.pop("wingPostHitsPerMatch", UNSET)
        )

        def _parse_wing_right_goals_scored(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_goals_scored = _parse_wing_right_goals_scored(
            d.pop("wingRightGoalsScored", UNSET)
        )

        def _parse_wing_right_goals_scored_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_right_goals_scored_per_match = _parse_wing_right_goals_scored_per_match(
            d.pop("wingRightGoalsScoredPerMatch", UNSET)
        )

        def _parse_wing_right_missed_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_missed_shots = _parse_wing_right_missed_shots(
            d.pop("wingRightMissedShots", UNSET)
        )

        def _parse_wing_right_missed_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_right_missed_shots_per_match = _parse_wing_right_missed_shots_per_match(
            d.pop("wingRightMissedShotsPerMatch", UNSET)
        )

        def _parse_wing_right_post_hits(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_post_hits = _parse_wing_right_post_hits(
            d.pop("wingRightPostHits", UNSET)
        )

        def _parse_wing_right_post_hits_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_right_post_hits_per_match = _parse_wing_right_post_hits_per_match(
            d.pop("wingRightPostHitsPerMatch", UNSET)
        )

        wing_right_shooting_accuracy = d.pop("wingRightShootingAccuracy", UNSET)

        def _parse_wing_right_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_right_shooting_accuracy_per_match = (
            _parse_wing_right_shooting_accuracy_per_match(
                d.pop("wingRightShootingAccuracyPerMatch", UNSET)
            )
        )

        def _parse_wing_right_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_shots = _parse_wing_right_shots(d.pop("wingRightShots", UNSET))

        def _parse_wing_right_shots_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_right_shots_per_match = _parse_wing_right_shots_per_match(
            d.pop("wingRightShotsPerMatch", UNSET)
        )

        def _parse_wing_right_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_shots_blocked = _parse_wing_right_shots_blocked(
            d.pop("wingRightShotsBlocked", UNSET)
        )

        def _parse_wing_right_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_right_shots_blocked_per_match = _parse_wing_right_shots_blocked_per_match(
            d.pop("wingRightShotsBlockedPerMatch", UNSET)
        )

        def _parse_wing_right_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_right_shots_on_goal = _parse_wing_right_shots_on_goal(
            d.pop("wingRightShotsOnGoal", UNSET)
        )

        def _parse_wing_right_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_right_shots_on_goal_per_match = _parse_wing_right_shots_on_goal_per_match(
            d.pop("wingRightShotsOnGoalPerMatch", UNSET)
        )

        wing_shooting_accuracy = d.pop("wingShootingAccuracy", UNSET)

        def _parse_wing_shooting_accuracy_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_shooting_accuracy_per_match = _parse_wing_shooting_accuracy_per_match(
            d.pop("wingShootingAccuracyPerMatch", UNSET)
        )

        def _parse_wing_shots(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_shots = _parse_wing_shots(d.pop("wingShots", UNSET))

        def _parse_wing_shots_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_shots_per_match = _parse_wing_shots_per_match(
            d.pop("wingShotsPerMatch", UNSET)
        )

        def _parse_wing_shots_blocked(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_shots_blocked = _parse_wing_shots_blocked(d.pop("wingShotsBlocked", UNSET))

        def _parse_wing_shots_blocked_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_shots_blocked_per_match = _parse_wing_shots_blocked_per_match(
            d.pop("wingShotsBlockedPerMatch", UNSET)
        )

        def _parse_wing_shots_on_goal(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wing_shots_on_goal = _parse_wing_shots_on_goal(d.pop("wingShotsOnGoal", UNSET))

        def _parse_wing_shots_on_goal_per_match(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        wing_shots_on_goal_per_match = _parse_wing_shots_on_goal_per_match(
            d.pop("wingShotsOnGoalPerMatch", UNSET)
        )

        def _parse_wins(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        wins = _parse_wins(d.pop("wins", UNSET))

        def _parse_yellow_cards(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        yellow_cards = _parse_yellow_cards(d.pop("yellowCards", UNSET))

        def _parse_yellow_cards_per_match(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        yellow_cards_per_match = _parse_yellow_cards_per_match(
            d.pop("yellowCardsPerMatch", UNSET)
        )

        season_person_statistics_model_statistics = cls(
            airtime_max=airtime_max,
            assists=assists,
            assists_per_match=assists_per_match,
            back_court_goals_scored=back_court_goals_scored,
            back_court_goals_scored_per_match=back_court_goals_scored_per_match,
            back_court_missed_shots=back_court_missed_shots,
            back_court_missed_shots_per_match=back_court_missed_shots_per_match,
            back_court_post_hits=back_court_post_hits,
            back_court_post_hits_per_match=back_court_post_hits_per_match,
            back_court_shooting_accuracy=back_court_shooting_accuracy,
            back_court_shooting_accuracy_per_match=back_court_shooting_accuracy_per_match,
            back_court_shots=back_court_shots,
            back_court_shots_per_match=back_court_shots_per_match,
            back_court_shots_blocked=back_court_shots_blocked,
            back_court_shots_blocked_per_match=back_court_shots_blocked_per_match,
            back_court_shots_on_goal=back_court_shots_on_goal,
            back_court_shots_on_goal_per_match=back_court_shots_on_goal_per_match,
            blocks=blocks,
            blocks_per_match=blocks_per_match,
            blue_cards=blue_cards,
            blue_cards_per_match=blue_cards_per_match,
            break_through_goals_scored=break_through_goals_scored,
            break_through_goals_scored_per_match=break_through_goals_scored_per_match,
            break_through_missed_shots=break_through_missed_shots,
            break_through_missed_shots_per_match=break_through_missed_shots_per_match,
            break_through_post_hits=break_through_post_hits,
            break_through_post_hits_per_match=break_through_post_hits_per_match,
            break_through_shooting_accuracy=break_through_shooting_accuracy,
            break_through_shooting_accuracy_per_match=break_through_shooting_accuracy_per_match,
            break_through_shots=break_through_shots,
            break_through_shots_per_match=break_through_shots_per_match,
            break_through_shots_blocked=break_through_shots_blocked,
            break_through_shots_blocked_per_match=break_through_shots_blocked_per_match,
            break_through_shots_on_goal=break_through_shots_on_goal,
            break_through_shots_on_goal_per_match=break_through_shots_on_goal_per_match,
            cards=cards,
            cards_per_match=cards_per_match,
            distance_speed_category_1=distance_speed_category_1,
            distance_speed_category_2=distance_speed_category_2,
            distance_speed_category_3=distance_speed_category_3,
            distance_speed_category_4=distance_speed_category_4,
            distance_speed_category_5=distance_speed_category_5,
            distance_total=distance_total,
            draws=draws,
            empty_net_goals_scored=empty_net_goals_scored,
            fast_break_goals_scored=fast_break_goals_scored,
            fast_break_goals_scored_per_match=fast_break_goals_scored_per_match,
            fast_break_missed_shots=fast_break_missed_shots,
            fast_break_missed_shots_per_match=fast_break_missed_shots_per_match,
            fast_break_post_hits=fast_break_post_hits,
            fast_break_post_hits_per_match=fast_break_post_hits_per_match,
            fast_break_shooting_accuracy=fast_break_shooting_accuracy,
            fast_break_shooting_accuracy_per_match=fast_break_shooting_accuracy_per_match,
            fast_break_shots=fast_break_shots,
            fast_break_shots_per_match=fast_break_shots_per_match,
            fast_break_shots_blocked=fast_break_shots_blocked,
            fast_break_shots_blocked_per_match=fast_break_shots_blocked_per_match,
            fast_break_shots_on_goal=fast_break_shots_on_goal,
            fast_break_shots_on_goal_per_match=fast_break_shots_on_goal_per_match,
            field_goals_scored=field_goals_scored,
            field_goals_scored_per_match=field_goals_scored_per_match,
            field_missed_shots=field_missed_shots,
            field_missed_shots_per_match=field_missed_shots_per_match,
            field_post_hits=field_post_hits,
            field_post_hits_per_match=field_post_hits_per_match,
            field_shooting_accuracy=field_shooting_accuracy,
            field_shooting_accuracy_per_match=field_shooting_accuracy_per_match,
            field_shots=field_shots,
            field_shots_per_match=field_shots_per_match,
            field_shots_blocked=field_shots_blocked,
            field_shots_blocked_per_match=field_shots_blocked_per_match,
            field_shots_on_goal=field_shots_on_goal,
            field_shots_on_goal_per_match=field_shots_on_goal_per_match,
            fouls=fouls,
            fouls_per_match=fouls_per_match,
            fouls_drawn=fouls_drawn,
            fouls_drawn_per_match=fouls_drawn_per_match,
            four_minute_suspensions=four_minute_suspensions,
            four_minute_suspensions_per_match=four_minute_suspensions_per_match,
            games=games,
            games_started=games_started,
            goal_keeper_back_court_goals_against=goal_keeper_back_court_goals_against,
            goal_keeper_back_court_goals_against_per_match=goal_keeper_back_court_goals_against_per_match,
            goal_keeper_back_court_save_accuracy=goal_keeper_back_court_save_accuracy,
            goal_keeper_back_court_save_accuracy_per_match=goal_keeper_back_court_save_accuracy_per_match,
            goal_keeper_back_court_shots_against=goal_keeper_back_court_shots_against,
            goal_keeper_back_court_shots_against_per_match=goal_keeper_back_court_shots_against_per_match,
            goal_keeper_back_court_shots_saved=goal_keeper_back_court_shots_saved,
            goal_keeper_back_court_shots_saved_per_match=goal_keeper_back_court_shots_saved_per_match,
            goal_keeper_break_through_goals_against=goal_keeper_break_through_goals_against,
            goal_keeper_break_through_goals_against_per_match=goal_keeper_break_through_goals_against_per_match,
            goal_keeper_break_through_save_accuracy=goal_keeper_break_through_save_accuracy,
            goal_keeper_break_through_save_accuracy_per_match=goal_keeper_break_through_save_accuracy_per_match,
            goal_keeper_break_through_shots_against=goal_keeper_break_through_shots_against,
            goal_keeper_break_through_shots_against_per_match=goal_keeper_break_through_shots_against_per_match,
            goal_keeper_break_through_shots_saved=goal_keeper_break_through_shots_saved,
            goal_keeper_break_through_shots_saved_per_match=goal_keeper_break_through_shots_saved_per_match,
            goal_keeper_fast_break_goals_against=goal_keeper_fast_break_goals_against,
            goal_keeper_fast_break_goals_against_per_match=goal_keeper_fast_break_goals_against_per_match,
            goal_keeper_fast_break_save_accuracy=goal_keeper_fast_break_save_accuracy,
            goal_keeper_fast_break_save_accuracy_per_match=goal_keeper_fast_break_save_accuracy_per_match,
            goal_keeper_fast_break_shots_against=goal_keeper_fast_break_shots_against,
            goal_keeper_fast_break_shots_against_per_match=goal_keeper_fast_break_shots_against_per_match,
            goal_keeper_fast_break_shots_saved=goal_keeper_fast_break_shots_saved,
            goal_keeper_fast_break_shots_saved_per_match=goal_keeper_fast_break_shots_saved_per_match,
            goal_keeper_field_goals_against=goal_keeper_field_goals_against,
            goal_keeper_field_goals_against_per_match=goal_keeper_field_goals_against_per_match,
            goal_keeper_field_save_accuracy=goal_keeper_field_save_accuracy,
            goal_keeper_field_save_accuracy_per_match=goal_keeper_field_save_accuracy_per_match,
            goal_keeper_field_shots_against=goal_keeper_field_shots_against,
            goal_keeper_field_shots_against_per_match=goal_keeper_field_shots_against_per_match,
            goal_keeper_field_shots_saved=goal_keeper_field_shots_saved,
            goal_keeper_field_shots_saved_per_match=goal_keeper_field_shots_saved_per_match,
            goal_keeper_goals_against=goal_keeper_goals_against,
            goal_keeper_goals_against_per_match=goal_keeper_goals_against_per_match,
            goal_keeper_nine_metre_centre_goals_against=goal_keeper_nine_metre_centre_goals_against,
            goal_keeper_nine_metre_centre_goals_against_per_match=goal_keeper_nine_metre_centre_goals_against_per_match,
            goal_keeper_nine_metre_centre_save_accuracy=goal_keeper_nine_metre_centre_save_accuracy,
            goal_keeper_nine_metre_centre_save_accuracy_per_match=goal_keeper_nine_metre_centre_save_accuracy_per_match,
            goal_keeper_nine_metre_centre_shots_against=goal_keeper_nine_metre_centre_shots_against,
            goal_keeper_nine_metre_centre_shots_against_per_match=goal_keeper_nine_metre_centre_shots_against_per_match,
            goal_keeper_nine_metre_centre_shots_saved=goal_keeper_nine_metre_centre_shots_saved,
            goal_keeper_nine_metre_centre_shots_saved_per_match=goal_keeper_nine_metre_centre_shots_saved_per_match,
            goal_keeper_nine_metre_goals_against=goal_keeper_nine_metre_goals_against,
            goal_keeper_nine_metre_goals_against_per_match=goal_keeper_nine_metre_goals_against_per_match,
            goal_keeper_nine_metre_left_goals_against=goal_keeper_nine_metre_left_goals_against,
            goal_keeper_nine_metre_left_goals_against_per_match=goal_keeper_nine_metre_left_goals_against_per_match,
            goal_keeper_nine_metre_left_save_accuracy=goal_keeper_nine_metre_left_save_accuracy,
            goal_keeper_nine_metre_left_save_accuracy_per_match=goal_keeper_nine_metre_left_save_accuracy_per_match,
            goal_keeper_nine_metre_left_shots_against=goal_keeper_nine_metre_left_shots_against,
            goal_keeper_nine_metre_left_shots_against_per_match=goal_keeper_nine_metre_left_shots_against_per_match,
            goal_keeper_nine_metre_left_shots_saved=goal_keeper_nine_metre_left_shots_saved,
            goal_keeper_nine_metre_left_shots_saved_per_match=goal_keeper_nine_metre_left_shots_saved_per_match,
            goal_keeper_nine_metre_right_goals_against=goal_keeper_nine_metre_right_goals_against,
            goal_keeper_nine_metre_right_goals_against_per_match=goal_keeper_nine_metre_right_goals_against_per_match,
            goal_keeper_nine_metre_right_save_accuracy=goal_keeper_nine_metre_right_save_accuracy,
            goal_keeper_nine_metre_right_save_accuracy_per_match=goal_keeper_nine_metre_right_save_accuracy_per_match,
            goal_keeper_nine_metre_right_shots_against=goal_keeper_nine_metre_right_shots_against,
            goal_keeper_nine_metre_right_shots_against_per_match=goal_keeper_nine_metre_right_shots_against_per_match,
            goal_keeper_nine_metre_right_shots_saved=goal_keeper_nine_metre_right_shots_saved,
            goal_keeper_nine_metre_right_shots_saved_per_match=goal_keeper_nine_metre_right_shots_saved_per_match,
            goal_keeper_nine_metre_save_accuracy=goal_keeper_nine_metre_save_accuracy,
            goal_keeper_nine_metre_save_accuracy_per_match=goal_keeper_nine_metre_save_accuracy_per_match,
            goal_keeper_nine_metre_shots_against=goal_keeper_nine_metre_shots_against,
            goal_keeper_nine_metre_shots_against_per_match=goal_keeper_nine_metre_shots_against_per_match,
            goal_keeper_nine_metre_shots_saved=goal_keeper_nine_metre_shots_saved,
            goal_keeper_nine_metre_shots_saved_per_match=goal_keeper_nine_metre_shots_saved_per_match,
            goal_keeper_pivot_goals_against=goal_keeper_pivot_goals_against,
            goal_keeper_pivot_goals_against_per_match=goal_keeper_pivot_goals_against_per_match,
            goal_keeper_pivot_save_accuracy=goal_keeper_pivot_save_accuracy,
            goal_keeper_pivot_save_accuracy_per_match=goal_keeper_pivot_save_accuracy_per_match,
            goal_keeper_pivot_shots_against=goal_keeper_pivot_shots_against,
            goal_keeper_pivot_shots_against_per_match=goal_keeper_pivot_shots_against_per_match,
            goal_keeper_pivot_shots_saved=goal_keeper_pivot_shots_saved,
            goal_keeper_pivot_shots_saved_per_match=goal_keeper_pivot_shots_saved_per_match,
            goal_keeper_save_accuracy=goal_keeper_save_accuracy,
            goal_keeper_save_accuracy_per_match=goal_keeper_save_accuracy_per_match,
            goal_keeper_seconds_played=goal_keeper_seconds_played,
            goal_keeper_seconds_played_per_match=goal_keeper_seconds_played_per_match,
            goal_keeper_seven_metre_goals_against=goal_keeper_seven_metre_goals_against,
            goal_keeper_seven_metre_goals_against_per_match=goal_keeper_seven_metre_goals_against_per_match,
            goal_keeper_seven_metre_save_accuracy=goal_keeper_seven_metre_save_accuracy,
            goal_keeper_seven_metre_save_accuracy_per_match=goal_keeper_seven_metre_save_accuracy_per_match,
            goal_keeper_seven_metre_shots_against=goal_keeper_seven_metre_shots_against,
            goal_keeper_seven_metre_shots_against_per_match=goal_keeper_seven_metre_shots_against_per_match,
            goal_keeper_seven_metre_shots_saved=goal_keeper_seven_metre_shots_saved,
            goal_keeper_seven_metre_shots_saved_per_match=goal_keeper_seven_metre_shots_saved_per_match,
            goal_keeper_shots_against=goal_keeper_shots_against,
            goal_keeper_shots_against_per_match=goal_keeper_shots_against_per_match,
            goal_keeper_shots_per_goals_against=goal_keeper_shots_per_goals_against,
            goal_keeper_shots_saved=goal_keeper_shots_saved,
            goal_keeper_shots_saved_per_match=goal_keeper_shots_saved_per_match,
            goal_keeper_six_metre_centre_goals_against=goal_keeper_six_metre_centre_goals_against,
            goal_keeper_six_metre_centre_goals_against_per_match=goal_keeper_six_metre_centre_goals_against_per_match,
            goal_keeper_six_metre_centre_save_accuracy=goal_keeper_six_metre_centre_save_accuracy,
            goal_keeper_six_metre_centre_save_accuracy_per_match=goal_keeper_six_metre_centre_save_accuracy_per_match,
            goal_keeper_six_metre_centre_shots_against=goal_keeper_six_metre_centre_shots_against,
            goal_keeper_six_metre_centre_shots_against_per_match=goal_keeper_six_metre_centre_shots_against_per_match,
            goal_keeper_six_metre_centre_shots_saved=goal_keeper_six_metre_centre_shots_saved,
            goal_keeper_six_metre_centre_shots_saved_per_match=goal_keeper_six_metre_centre_shots_saved_per_match,
            goal_keeper_six_metre_goals_against=goal_keeper_six_metre_goals_against,
            goal_keeper_six_metre_goals_against_per_match=goal_keeper_six_metre_goals_against_per_match,
            goal_keeper_six_metre_left_goals_against=goal_keeper_six_metre_left_goals_against,
            goal_keeper_six_metre_left_goals_against_per_match=goal_keeper_six_metre_left_goals_against_per_match,
            goal_keeper_six_metre_left_save_accuracy=goal_keeper_six_metre_left_save_accuracy,
            goal_keeper_six_metre_left_save_accuracy_per_match=goal_keeper_six_metre_left_save_accuracy_per_match,
            goal_keeper_six_metre_left_shots_against=goal_keeper_six_metre_left_shots_against,
            goal_keeper_six_metre_left_shots_against_per_match=goal_keeper_six_metre_left_shots_against_per_match,
            goal_keeper_six_metre_left_shots_saved=goal_keeper_six_metre_left_shots_saved,
            goal_keeper_six_metre_left_shots_saved_per_match=goal_keeper_six_metre_left_shots_saved_per_match,
            goal_keeper_six_metre_right_goals_against=goal_keeper_six_metre_right_goals_against,
            goal_keeper_six_metre_right_goals_against_per_match=goal_keeper_six_metre_right_goals_against_per_match,
            goal_keeper_six_metre_right_save_accuracy=goal_keeper_six_metre_right_save_accuracy,
            goal_keeper_six_metre_right_save_accuracy_per_match=goal_keeper_six_metre_right_save_accuracy_per_match,
            goal_keeper_six_metre_right_shots_against=goal_keeper_six_metre_right_shots_against,
            goal_keeper_six_metre_right_shots_against_per_match=goal_keeper_six_metre_right_shots_against_per_match,
            goal_keeper_six_metre_right_shots_saved=goal_keeper_six_metre_right_shots_saved,
            goal_keeper_six_metre_right_shots_saved_per_match=goal_keeper_six_metre_right_shots_saved_per_match,
            goal_keeper_six_metre_save_accuracy=goal_keeper_six_metre_save_accuracy,
            goal_keeper_six_metre_save_accuracy_per_match=goal_keeper_six_metre_save_accuracy_per_match,
            goal_keeper_six_metre_shots_against=goal_keeper_six_metre_shots_against,
            goal_keeper_six_metre_shots_against_per_match=goal_keeper_six_metre_shots_against_per_match,
            goal_keeper_six_metre_shots_saved=goal_keeper_six_metre_shots_saved,
            goal_keeper_six_metre_shots_saved_per_match=goal_keeper_six_metre_shots_saved_per_match,
            goal_keeper_wing_goals_against=goal_keeper_wing_goals_against,
            goal_keeper_wing_goals_against_per_match=goal_keeper_wing_goals_against_per_match,
            goal_keeper_wing_left_goals_against=goal_keeper_wing_left_goals_against,
            goal_keeper_wing_left_goals_against_per_match=goal_keeper_wing_left_goals_against_per_match,
            goal_keeper_wing_left_save_accuracy=goal_keeper_wing_left_save_accuracy,
            goal_keeper_wing_left_save_accuracy_per_match=goal_keeper_wing_left_save_accuracy_per_match,
            goal_keeper_wing_left_shots_against=goal_keeper_wing_left_shots_against,
            goal_keeper_wing_left_shots_against_per_match=goal_keeper_wing_left_shots_against_per_match,
            goal_keeper_wing_left_shots_saved=goal_keeper_wing_left_shots_saved,
            goal_keeper_wing_left_shots_saved_per_match=goal_keeper_wing_left_shots_saved_per_match,
            goal_keeper_wing_right_goals_against=goal_keeper_wing_right_goals_against,
            goal_keeper_wing_right_goals_against_per_match=goal_keeper_wing_right_goals_against_per_match,
            goal_keeper_wing_right_save_accuracy=goal_keeper_wing_right_save_accuracy,
            goal_keeper_wing_right_save_accuracy_per_match=goal_keeper_wing_right_save_accuracy_per_match,
            goal_keeper_wing_right_shots_against=goal_keeper_wing_right_shots_against,
            goal_keeper_wing_right_shots_against_per_match=goal_keeper_wing_right_shots_against_per_match,
            goal_keeper_wing_right_shots_saved=goal_keeper_wing_right_shots_saved,
            goal_keeper_wing_right_shots_saved_per_match=goal_keeper_wing_right_shots_saved_per_match,
            goal_keeper_wing_save_accuracy=goal_keeper_wing_save_accuracy,
            goal_keeper_wing_save_accuracy_per_match=goal_keeper_wing_save_accuracy_per_match,
            goal_keeper_wing_shots_against=goal_keeper_wing_shots_against,
            goal_keeper_wing_shots_against_per_match=goal_keeper_wing_shots_against_per_match,
            goal_keeper_wing_shots_saved=goal_keeper_wing_shots_saved,
            goal_keeper_wing_shots_saved_per_match=goal_keeper_wing_shots_saved_per_match,
            goals_scored=goals_scored,
            goals_scored_per_match=goals_scored_per_match,
            handball_performance_index=handball_performance_index,
            losses=losses,
            matches_played=matches_played,
            minutes=minutes,
            minutes_per_match=minutes_per_match,
            missed_shots=missed_shots,
            missed_shots_per_match=missed_shots_per_match,
            nine_metre_centre_goals_scored=nine_metre_centre_goals_scored,
            nine_metre_centre_goals_scored_per_match=nine_metre_centre_goals_scored_per_match,
            nine_metre_centre_missed_shots=nine_metre_centre_missed_shots,
            nine_metre_centre_missed_shots_per_match=nine_metre_centre_missed_shots_per_match,
            nine_metre_centre_post_hits=nine_metre_centre_post_hits,
            nine_metre_centre_post_hits_per_match=nine_metre_centre_post_hits_per_match,
            nine_metre_centre_shooting_accuracy=nine_metre_centre_shooting_accuracy,
            nine_metre_centre_shooting_accuracy_per_match=nine_metre_centre_shooting_accuracy_per_match,
            nine_metre_centre_shots=nine_metre_centre_shots,
            nine_metre_centre_shots_per_match=nine_metre_centre_shots_per_match,
            nine_metre_centre_shots_blocked=nine_metre_centre_shots_blocked,
            nine_metre_centre_shots_blocked_per_match=nine_metre_centre_shots_blocked_per_match,
            nine_metre_centre_shots_on_goal=nine_metre_centre_shots_on_goal,
            nine_metre_centre_shots_on_goal_per_match=nine_metre_centre_shots_on_goal_per_match,
            nine_metre_goals_scored=nine_metre_goals_scored,
            nine_metre_goals_scored_per_match=nine_metre_goals_scored_per_match,
            nine_metre_left_goals_scored=nine_metre_left_goals_scored,
            nine_metre_left_goals_scored_per_match=nine_metre_left_goals_scored_per_match,
            nine_metre_left_missed_shots=nine_metre_left_missed_shots,
            nine_metre_left_missed_shots_per_match=nine_metre_left_missed_shots_per_match,
            nine_metre_left_post_hits=nine_metre_left_post_hits,
            nine_metre_left_post_hits_per_match=nine_metre_left_post_hits_per_match,
            nine_metre_left_shooting_accuracy=nine_metre_left_shooting_accuracy,
            nine_metre_left_shooting_accuracy_per_match=nine_metre_left_shooting_accuracy_per_match,
            nine_metre_left_shots=nine_metre_left_shots,
            nine_metre_left_shots_per_match=nine_metre_left_shots_per_match,
            nine_metre_left_shots_blocked=nine_metre_left_shots_blocked,
            nine_metre_left_shots_blocked_per_match=nine_metre_left_shots_blocked_per_match,
            nine_metre_left_shots_on_goal=nine_metre_left_shots_on_goal,
            nine_metre_left_shots_on_goal_per_match=nine_metre_left_shots_on_goal_per_match,
            nine_metre_missed_shots=nine_metre_missed_shots,
            nine_metre_missed_shots_per_match=nine_metre_missed_shots_per_match,
            nine_metre_post_hits=nine_metre_post_hits,
            nine_metre_post_hits_per_match=nine_metre_post_hits_per_match,
            nine_metre_right_goals_scored=nine_metre_right_goals_scored,
            nine_metre_right_goals_scored_per_match=nine_metre_right_goals_scored_per_match,
            nine_metre_right_missed_shots=nine_metre_right_missed_shots,
            nine_metre_right_missed_shots_per_match=nine_metre_right_missed_shots_per_match,
            nine_metre_right_post_hits=nine_metre_right_post_hits,
            nine_metre_right_post_hits_per_match=nine_metre_right_post_hits_per_match,
            nine_metre_right_shooting_accuracy=nine_metre_right_shooting_accuracy,
            nine_metre_right_shooting_accuracy_per_match=nine_metre_right_shooting_accuracy_per_match,
            nine_metre_right_shots=nine_metre_right_shots,
            nine_metre_right_shots_per_match=nine_metre_right_shots_per_match,
            nine_metre_right_shots_blocked=nine_metre_right_shots_blocked,
            nine_metre_right_shots_blocked_per_match=nine_metre_right_shots_blocked_per_match,
            nine_metre_right_shots_on_goal=nine_metre_right_shots_on_goal,
            nine_metre_right_shots_on_goal_per_match=nine_metre_right_shots_on_goal_per_match,
            nine_metre_shooting_accuracy=nine_metre_shooting_accuracy,
            nine_metre_shooting_accuracy_per_match=nine_metre_shooting_accuracy_per_match,
            nine_metre_shots=nine_metre_shots,
            nine_metre_shots_per_match=nine_metre_shots_per_match,
            nine_metre_shots_blocked=nine_metre_shots_blocked,
            nine_metre_shots_blocked_per_match=nine_metre_shots_blocked_per_match,
            nine_metre_shots_on_goal=nine_metre_shots_on_goal,
            nine_metre_shots_on_goal_per_match=nine_metre_shots_on_goal_per_match,
            passive_play=passive_play,
            pivot_goals_scored=pivot_goals_scored,
            pivot_goals_scored_per_match=pivot_goals_scored_per_match,
            pivot_missed_shots=pivot_missed_shots,
            pivot_missed_shots_per_match=pivot_missed_shots_per_match,
            pivot_post_hits=pivot_post_hits,
            pivot_post_hits_per_match=pivot_post_hits_per_match,
            pivot_shooting_accuracy=pivot_shooting_accuracy,
            pivot_shooting_accuracy_per_match=pivot_shooting_accuracy_per_match,
            pivot_shots=pivot_shots,
            pivot_shots_per_match=pivot_shots_per_match,
            pivot_shots_blocked=pivot_shots_blocked,
            pivot_shots_blocked_per_match=pivot_shots_blocked_per_match,
            pivot_shots_on_goal=pivot_shots_on_goal,
            pivot_shots_on_goal_per_match=pivot_shots_on_goal_per_match,
            post_hits=post_hits,
            post_hits_per_match=post_hits_per_match,
            red_cards=red_cards,
            red_cards_per_match=red_cards_per_match,
            seven_metre_goals_scored=seven_metre_goals_scored,
            seven_metre_goals_scored_per_match=seven_metre_goals_scored_per_match,
            seven_metre_missed_shots=seven_metre_missed_shots,
            seven_metre_missed_shots_per_match=seven_metre_missed_shots_per_match,
            seven_metre_penalties_awarded=seven_metre_penalties_awarded,
            seven_metre_penalties_awarded_per_match=seven_metre_penalties_awarded_per_match,
            seven_metre_penalties_caused=seven_metre_penalties_caused,
            seven_metre_penalties_caused_per_match=seven_metre_penalties_caused_per_match,
            seven_metre_penalty_fouls=seven_metre_penalty_fouls,
            seven_metre_penalty_fouls_per_match=seven_metre_penalty_fouls_per_match,
            seven_metre_post_hits=seven_metre_post_hits,
            seven_metre_post_hits_per_match=seven_metre_post_hits_per_match,
            seven_metre_shooting_accuracy=seven_metre_shooting_accuracy,
            seven_metre_shooting_accuracy_per_match=seven_metre_shooting_accuracy_per_match,
            seven_metre_shots=seven_metre_shots,
            seven_metre_shots_per_match=seven_metre_shots_per_match,
            seven_metre_shots_blocked=seven_metre_shots_blocked,
            seven_metre_shots_blocked_per_match=seven_metre_shots_blocked_per_match,
            seven_metre_shots_on_goal=seven_metre_shots_on_goal,
            seven_metre_shots_on_goal_per_match=seven_metre_shots_on_goal_per_match,
            shooting_accuracy=shooting_accuracy,
            shooting_accuracy_per_match=shooting_accuracy_per_match,
            shoot_outs=shoot_outs,
            shoot_outs_per_match=shoot_outs_per_match,
            shoot_outs_made=shoot_outs_made,
            shoot_outs_made_per_match=shoot_outs_made_per_match,
            shoot_outs_missed=shoot_outs_missed,
            shoot_outs_missed_per_match=shoot_outs_missed_per_match,
            shoot_outs_saved=shoot_outs_saved,
            shoot_outs_saved_per_match=shoot_outs_saved_per_match,
            shots=shots,
            shots_per_match=shots_per_match,
            shots_blocked=shots_blocked,
            shots_blocked_per_match=shots_blocked_per_match,
            shots_on_goal=shots_on_goal,
            shots_on_goal_per_match=shots_on_goal_per_match,
            shots_saved_by_goal_keeper=shots_saved_by_goal_keeper,
            shots_saved_by_goal_keeper_per_match=shots_saved_by_goal_keeper_per_match,
            six_metre_centre_goals_scored=six_metre_centre_goals_scored,
            six_metre_centre_goals_scored_per_match=six_metre_centre_goals_scored_per_match,
            six_metre_centre_missed_shots=six_metre_centre_missed_shots,
            six_metre_centre_missed_shots_per_match=six_metre_centre_missed_shots_per_match,
            six_metre_centre_post_hits=six_metre_centre_post_hits,
            six_metre_centre_post_hits_per_match=six_metre_centre_post_hits_per_match,
            six_metre_centre_shooting_accuracy=six_metre_centre_shooting_accuracy,
            six_metre_centre_shooting_accuracy_per_match=six_metre_centre_shooting_accuracy_per_match,
            six_metre_centre_shots=six_metre_centre_shots,
            six_metre_centre_shots_per_match=six_metre_centre_shots_per_match,
            six_metre_centre_shots_blocked=six_metre_centre_shots_blocked,
            six_metre_centre_shots_blocked_per_match=six_metre_centre_shots_blocked_per_match,
            six_metre_centre_shots_on_goal=six_metre_centre_shots_on_goal,
            six_metre_centre_shots_on_goal_per_match=six_metre_centre_shots_on_goal_per_match,
            six_metre_goals_scored=six_metre_goals_scored,
            six_metre_goals_scored_per_match=six_metre_goals_scored_per_match,
            six_metre_left_goals_scored=six_metre_left_goals_scored,
            six_metre_left_goals_scored_per_match=six_metre_left_goals_scored_per_match,
            six_metre_left_missed_shots=six_metre_left_missed_shots,
            six_metre_left_missed_shots_per_match=six_metre_left_missed_shots_per_match,
            six_metre_left_post_hits=six_metre_left_post_hits,
            six_metre_left_post_hits_per_match=six_metre_left_post_hits_per_match,
            six_metre_left_shooting_accuracy=six_metre_left_shooting_accuracy,
            six_metre_left_shooting_accuracy_per_match=six_metre_left_shooting_accuracy_per_match,
            six_metre_left_shots=six_metre_left_shots,
            six_metre_left_shots_per_match=six_metre_left_shots_per_match,
            six_metre_left_shots_blocked=six_metre_left_shots_blocked,
            six_metre_left_shots_blocked_per_match=six_metre_left_shots_blocked_per_match,
            six_metre_left_shots_on_goal=six_metre_left_shots_on_goal,
            six_metre_left_shots_on_goal_per_match=six_metre_left_shots_on_goal_per_match,
            six_metre_missed_shots=six_metre_missed_shots,
            six_metre_missed_shots_per_match=six_metre_missed_shots_per_match,
            six_metre_post_hits=six_metre_post_hits,
            six_metre_post_hits_per_match=six_metre_post_hits_per_match,
            six_metre_right_goals_scored=six_metre_right_goals_scored,
            six_metre_right_goals_scored_per_match=six_metre_right_goals_scored_per_match,
            six_metre_right_missed_shots=six_metre_right_missed_shots,
            six_metre_right_missed_shots_per_match=six_metre_right_missed_shots_per_match,
            six_metre_right_post_hits=six_metre_right_post_hits,
            six_metre_right_post_hits_per_match=six_metre_right_post_hits_per_match,
            six_metre_right_shooting_accuracy=six_metre_right_shooting_accuracy,
            six_metre_right_shooting_accuracy_per_match=six_metre_right_shooting_accuracy_per_match,
            six_metre_right_shots=six_metre_right_shots,
            six_metre_right_shots_per_match=six_metre_right_shots_per_match,
            six_metre_right_shots_blocked=six_metre_right_shots_blocked,
            six_metre_right_shots_blocked_per_match=six_metre_right_shots_blocked_per_match,
            six_metre_right_shots_on_goal=six_metre_right_shots_on_goal,
            six_metre_right_shots_on_goal_per_match=six_metre_right_shots_on_goal_per_match,
            six_metre_shooting_accuracy=six_metre_shooting_accuracy,
            six_metre_shooting_accuracy_per_match=six_metre_shooting_accuracy_per_match,
            six_metre_shots=six_metre_shots,
            six_metre_shots_per_match=six_metre_shots_per_match,
            six_metre_shots_blocked=six_metre_shots_blocked,
            six_metre_shots_blocked_per_match=six_metre_shots_blocked_per_match,
            six_metre_shots_on_goal=six_metre_shots_on_goal,
            six_metre_shots_on_goal_per_match=six_metre_shots_on_goal_per_match,
            speed_distance_per_time=speed_distance_per_time,
            speed_max=speed_max,
            steals=steals,
            steals_per_match=steals_per_match,
            substitutions=substitutions,
            substitutions_per_match=substitutions_per_match,
            suspensions=suspensions,
            suspensions_per_match=suspensions_per_match,
            technical_ball_faults=technical_ball_faults,
            technical_ball_faults_per_match=technical_ball_faults_per_match,
            technical_faults=technical_faults,
            technical_faults_per_match=technical_faults_per_match,
            technical_rule_faults=technical_rule_faults,
            technical_rule_faults_per_match=technical_rule_faults_per_match,
            time_on_playing_field=time_on_playing_field,
            time_ball_possession=time_ball_possession,
            time_played=time_played,
            time_played_per_match=time_played_per_match,
            turnovers=turnovers,
            turnovers_per_match=turnovers_per_match,
            two_minute_suspensions=two_minute_suspensions,
            two_minute_suspensions_per_match=two_minute_suspensions_per_match,
            wing_goals_scored=wing_goals_scored,
            wing_goals_scored_per_match=wing_goals_scored_per_match,
            wing_left_goals_scored=wing_left_goals_scored,
            wing_left_goals_scored_per_match=wing_left_goals_scored_per_match,
            wing_left_missed_shots=wing_left_missed_shots,
            wing_left_missed_shots_per_match=wing_left_missed_shots_per_match,
            wing_left_post_hits=wing_left_post_hits,
            wing_left_post_hits_per_match=wing_left_post_hits_per_match,
            wing_left_shooting_accuracy=wing_left_shooting_accuracy,
            wing_left_shooting_accuracy_per_match=wing_left_shooting_accuracy_per_match,
            wing_left_shots=wing_left_shots,
            wing_left_shots_per_match=wing_left_shots_per_match,
            wing_left_shots_blocked=wing_left_shots_blocked,
            wing_left_shots_blocked_per_match=wing_left_shots_blocked_per_match,
            wing_left_shots_on_goal=wing_left_shots_on_goal,
            wing_left_shots_on_goal_per_match=wing_left_shots_on_goal_per_match,
            wing_missed_shots=wing_missed_shots,
            wing_missed_shots_per_match=wing_missed_shots_per_match,
            wing_post_hits=wing_post_hits,
            wing_post_hits_per_match=wing_post_hits_per_match,
            wing_right_goals_scored=wing_right_goals_scored,
            wing_right_goals_scored_per_match=wing_right_goals_scored_per_match,
            wing_right_missed_shots=wing_right_missed_shots,
            wing_right_missed_shots_per_match=wing_right_missed_shots_per_match,
            wing_right_post_hits=wing_right_post_hits,
            wing_right_post_hits_per_match=wing_right_post_hits_per_match,
            wing_right_shooting_accuracy=wing_right_shooting_accuracy,
            wing_right_shooting_accuracy_per_match=wing_right_shooting_accuracy_per_match,
            wing_right_shots=wing_right_shots,
            wing_right_shots_per_match=wing_right_shots_per_match,
            wing_right_shots_blocked=wing_right_shots_blocked,
            wing_right_shots_blocked_per_match=wing_right_shots_blocked_per_match,
            wing_right_shots_on_goal=wing_right_shots_on_goal,
            wing_right_shots_on_goal_per_match=wing_right_shots_on_goal_per_match,
            wing_shooting_accuracy=wing_shooting_accuracy,
            wing_shooting_accuracy_per_match=wing_shooting_accuracy_per_match,
            wing_shots=wing_shots,
            wing_shots_per_match=wing_shots_per_match,
            wing_shots_blocked=wing_shots_blocked,
            wing_shots_blocked_per_match=wing_shots_blocked_per_match,
            wing_shots_on_goal=wing_shots_on_goal,
            wing_shots_on_goal_per_match=wing_shots_on_goal_per_match,
            wins=wins,
            yellow_cards=yellow_cards,
            yellow_cards_per_match=yellow_cards_per_match,
        )

        return season_person_statistics_model_statistics
