from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.match_profile_configuration_match_roles_item import MatchProfileConfigurationMatchRolesItem
from ..models.match_profile_configuration_type_of_cards_item import MatchProfileConfigurationTypeOfCardsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchProfileConfiguration")


@_attrs_define
class MatchProfileConfiguration:
    """Match Profile Configuration

    Attributes:
        number_of_periods (Union[Unset, float]): The number of regular periods to play.
        period_length (Union[Unset, float]): The length (in minutes) of a regular period.
        overtime_allowed (Union[Unset, bool]): Is overtime allowed?
        overtime_length (Union[Unset, float]): The length (in minutes) of an overtime period.
        maximum_roster_size (Union[Unset, float]): The maximum number of persons allowed on a roster.
        period_break_duration (Union[Unset, float]): The length (in minutes) of a break between periods.
        half_time_duration (Union[Unset, float]): The length (in minutes) of a half time break.
        maximum_players_on_court (Union[Unset, float]): The maximum number of players on the Court per team.
        maximum_goalkeeper_substitutions (Union[Unset, float]): The maximum number of Goalkeeper substitutions allowed
            per team for a match.
        type_of_cards (Union[Unset, list[MatchProfileConfigurationTypeOfCardsItem]]): The type of cards allowed in this
            match.
        red_card_seconds (Union[Unset, float]): The length (in seconds) a player leaves the field for when issued a red
            card.
        yellow_card_seconds (Union[Unset, float]): The length (in seconds) a player leaves the field for when issued a
            yellow card.
        blue_card_seconds (Union[Unset, float]): The length (in seconds) a player leaves the field for when issued a
            blue card.
        match_roles (Union[Unset, list[MatchProfileConfigurationMatchRolesItem]]): The official roles that are
            assignable for this match.
        bib_numbers_required (Union[Unset, bool]): Are bib numbers required for the match?.
        switch_playing_direction (Union[None, Unset, list[float]]): Switch direction of play after period/s. Example:
            [2].
        shootout_if_tie (Union[Unset, bool]): Is there a shootout if the game ends with a tied score?.
        shots_until_sudden_death (Union[Unset, float]): The number of shots each team takes in the shootout before it
            moves sudden death phase.
        timeouts_allowed (Union[Unset, float]): The number of timeouts a team can use in a match.
        video_review_allowed (Union[Unset, bool]): Is video review allowed?.
        reset_timeouts_after_periods (Union[None, Unset, list[float]]): Reset Timeouts to 0 after period/s. Example: [1,
            2, 3].
    """

    number_of_periods: Union[Unset, float] = UNSET
    period_length: Union[Unset, float] = UNSET
    overtime_allowed: Union[Unset, bool] = UNSET
    overtime_length: Union[Unset, float] = UNSET
    maximum_roster_size: Union[Unset, float] = UNSET
    period_break_duration: Union[Unset, float] = UNSET
    half_time_duration: Union[Unset, float] = UNSET
    maximum_players_on_court: Union[Unset, float] = UNSET
    maximum_goalkeeper_substitutions: Union[Unset, float] = UNSET
    type_of_cards: Union[Unset, list[MatchProfileConfigurationTypeOfCardsItem]] = UNSET
    red_card_seconds: Union[Unset, float] = UNSET
    yellow_card_seconds: Union[Unset, float] = UNSET
    blue_card_seconds: Union[Unset, float] = UNSET
    match_roles: Union[Unset, list[MatchProfileConfigurationMatchRolesItem]] = UNSET
    bib_numbers_required: Union[Unset, bool] = UNSET
    switch_playing_direction: Union[None, Unset, list[float]] = UNSET
    shootout_if_tie: Union[Unset, bool] = UNSET
    shots_until_sudden_death: Union[Unset, float] = UNSET
    timeouts_allowed: Union[Unset, float] = UNSET
    video_review_allowed: Union[Unset, bool] = UNSET
    reset_timeouts_after_periods: Union[None, Unset, list[float]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        number_of_periods = self.number_of_periods

        period_length = self.period_length

        overtime_allowed = self.overtime_allowed

        overtime_length = self.overtime_length

        maximum_roster_size = self.maximum_roster_size

        period_break_duration = self.period_break_duration

        half_time_duration = self.half_time_duration

        maximum_players_on_court = self.maximum_players_on_court

        maximum_goalkeeper_substitutions = self.maximum_goalkeeper_substitutions

        type_of_cards: Union[Unset, list[str]] = UNSET
        if not isinstance(self.type_of_cards, Unset):
            type_of_cards = []
            for type_of_cards_item_data in self.type_of_cards:
                type_of_cards_item = type_of_cards_item_data.value
                type_of_cards.append(type_of_cards_item)

        red_card_seconds = self.red_card_seconds

        yellow_card_seconds = self.yellow_card_seconds

        blue_card_seconds = self.blue_card_seconds

        match_roles: Union[Unset, list[str]] = UNSET
        if not isinstance(self.match_roles, Unset):
            match_roles = []
            for match_roles_item_data in self.match_roles:
                match_roles_item = match_roles_item_data.value
                match_roles.append(match_roles_item)

        bib_numbers_required = self.bib_numbers_required

        switch_playing_direction: Union[None, Unset, list[float]]
        if isinstance(self.switch_playing_direction, Unset):
            switch_playing_direction = UNSET
        elif isinstance(self.switch_playing_direction, list):
            switch_playing_direction = self.switch_playing_direction

        else:
            switch_playing_direction = self.switch_playing_direction

        shootout_if_tie = self.shootout_if_tie

        shots_until_sudden_death = self.shots_until_sudden_death

        timeouts_allowed = self.timeouts_allowed

        video_review_allowed = self.video_review_allowed

        reset_timeouts_after_periods: Union[None, Unset, list[float]]
        if isinstance(self.reset_timeouts_after_periods, Unset):
            reset_timeouts_after_periods = UNSET
        elif isinstance(self.reset_timeouts_after_periods, list):
            reset_timeouts_after_periods = self.reset_timeouts_after_periods

        else:
            reset_timeouts_after_periods = self.reset_timeouts_after_periods

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if number_of_periods is not UNSET:
            field_dict["numberOfPeriods"] = number_of_periods
        if period_length is not UNSET:
            field_dict["periodLength"] = period_length
        if overtime_allowed is not UNSET:
            field_dict["overtimeAllowed"] = overtime_allowed
        if overtime_length is not UNSET:
            field_dict["overtimeLength"] = overtime_length
        if maximum_roster_size is not UNSET:
            field_dict["maximumRosterSize"] = maximum_roster_size
        if period_break_duration is not UNSET:
            field_dict["periodBreakDuration"] = period_break_duration
        if half_time_duration is not UNSET:
            field_dict["halfTimeDuration"] = half_time_duration
        if maximum_players_on_court is not UNSET:
            field_dict["maximumPlayersOnCourt"] = maximum_players_on_court
        if maximum_goalkeeper_substitutions is not UNSET:
            field_dict["maximumGoalkeeperSubstitutions"] = maximum_goalkeeper_substitutions
        if type_of_cards is not UNSET:
            field_dict["typeOfCards"] = type_of_cards
        if red_card_seconds is not UNSET:
            field_dict["redCardSeconds"] = red_card_seconds
        if yellow_card_seconds is not UNSET:
            field_dict["yellowCardSeconds"] = yellow_card_seconds
        if blue_card_seconds is not UNSET:
            field_dict["blueCardSeconds"] = blue_card_seconds
        if match_roles is not UNSET:
            field_dict["matchRoles"] = match_roles
        if bib_numbers_required is not UNSET:
            field_dict["bibNumbersRequired"] = bib_numbers_required
        if switch_playing_direction is not UNSET:
            field_dict["switchPlayingDirection"] = switch_playing_direction
        if shootout_if_tie is not UNSET:
            field_dict["shootoutIfTie"] = shootout_if_tie
        if shots_until_sudden_death is not UNSET:
            field_dict["shotsUntilSuddenDeath"] = shots_until_sudden_death
        if timeouts_allowed is not UNSET:
            field_dict["timeoutsAllowed"] = timeouts_allowed
        if video_review_allowed is not UNSET:
            field_dict["videoReviewAllowed"] = video_review_allowed
        if reset_timeouts_after_periods is not UNSET:
            field_dict["resetTimeoutsAfterPeriods"] = reset_timeouts_after_periods

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        number_of_periods = d.pop("numberOfPeriods", UNSET)

        period_length = d.pop("periodLength", UNSET)

        overtime_allowed = d.pop("overtimeAllowed", UNSET)

        overtime_length = d.pop("overtimeLength", UNSET)

        maximum_roster_size = d.pop("maximumRosterSize", UNSET)

        period_break_duration = d.pop("periodBreakDuration", UNSET)

        half_time_duration = d.pop("halfTimeDuration", UNSET)

        maximum_players_on_court = d.pop("maximumPlayersOnCourt", UNSET)

        maximum_goalkeeper_substitutions = d.pop("maximumGoalkeeperSubstitutions", UNSET)

        type_of_cards = []
        _type_of_cards = d.pop("typeOfCards", UNSET)
        for type_of_cards_item_data in _type_of_cards or []:
            type_of_cards_item = MatchProfileConfigurationTypeOfCardsItem(type_of_cards_item_data)

            type_of_cards.append(type_of_cards_item)

        red_card_seconds = d.pop("redCardSeconds", UNSET)

        yellow_card_seconds = d.pop("yellowCardSeconds", UNSET)

        blue_card_seconds = d.pop("blueCardSeconds", UNSET)

        match_roles = []
        _match_roles = d.pop("matchRoles", UNSET)
        for match_roles_item_data in _match_roles or []:
            match_roles_item = MatchProfileConfigurationMatchRolesItem(match_roles_item_data)

            match_roles.append(match_roles_item)

        bib_numbers_required = d.pop("bibNumbersRequired", UNSET)

        def _parse_switch_playing_direction(data: object) -> Union[None, Unset, list[float]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                switch_playing_direction_type_0 = cast(list[float], data)

                return switch_playing_direction_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[float]], data)

        switch_playing_direction = _parse_switch_playing_direction(d.pop("switchPlayingDirection", UNSET))

        shootout_if_tie = d.pop("shootoutIfTie", UNSET)

        shots_until_sudden_death = d.pop("shotsUntilSuddenDeath", UNSET)

        timeouts_allowed = d.pop("timeoutsAllowed", UNSET)

        video_review_allowed = d.pop("videoReviewAllowed", UNSET)

        def _parse_reset_timeouts_after_periods(data: object) -> Union[None, Unset, list[float]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reset_timeouts_after_periods_type_0 = cast(list[float], data)

                return reset_timeouts_after_periods_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[float]], data)

        reset_timeouts_after_periods = _parse_reset_timeouts_after_periods(d.pop("resetTimeoutsAfterPeriods", UNSET))

        match_profile_configuration = cls(
            number_of_periods=number_of_periods,
            period_length=period_length,
            overtime_allowed=overtime_allowed,
            overtime_length=overtime_length,
            maximum_roster_size=maximum_roster_size,
            period_break_duration=period_break_duration,
            half_time_duration=half_time_duration,
            maximum_players_on_court=maximum_players_on_court,
            maximum_goalkeeper_substitutions=maximum_goalkeeper_substitutions,
            type_of_cards=type_of_cards,
            red_card_seconds=red_card_seconds,
            yellow_card_seconds=yellow_card_seconds,
            blue_card_seconds=blue_card_seconds,
            match_roles=match_roles,
            bib_numbers_required=bib_numbers_required,
            switch_playing_direction=switch_playing_direction,
            shootout_if_tie=shootout_if_tie,
            shots_until_sudden_death=shots_until_sudden_death,
            timeouts_allowed=timeouts_allowed,
            video_review_allowed=video_review_allowed,
            reset_timeouts_after_periods=reset_timeouts_after_periods,
        )

        return match_profile_configuration
