from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.fixture_insert_match_post_body_match_competitor_result_status import (
    FixtureInsertMatchPostBodyMatchCompetitorResultStatus,
)
from ..models.fixture_insert_match_post_body_match_competitor_roster_status import (
    FixtureInsertMatchPostBodyMatchCompetitorRosterStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FixtureInsertMatchPostBodyMatchCompetitor")


@_attrs_define
class FixtureInsertMatchPostBodyMatchCompetitor:
    """
    Attributes:
        entity_id (str): The uuid of the entity
        conference_id (Union[Unset, str]): The uuid of the conference
        division_id (Union[Unset, str]): The uuid of the division
        include_in_conference_statistics (Union[Unset, bool]): Include the statistics for this competitors in the
            conference statistics?
        is_home (Union[Unset, bool]): Is competitor the home team ?
        include_in_representation (Union[Unset, bool]): Include participant in representation count
        draw (Union[Unset, bool]): Result for this competitor was a draw ?
        result_status (Union[Unset, FixtureInsertMatchPostBodyMatchCompetitorResultStatus]): Result status
        result_place (Union[None, Unset, float]): Result placing (1=Won, 2=Lost)
        result_secondary_score_place (Union[None, Unset, float]): Secondary Score Result placing (1=Won, 2=Lost)
        starting_number (Union[None, Unset, float]): Starting number
        score (Union[None, Unset, str]): Score for competitor in match
        secondary_score (Union[None, Unset, str]): Secondary score
        shoot_out_attempts (Union[None, Unset, str]): shootOut Attempts
        roster_status (Union[Unset, FixtureInsertMatchPostBodyMatchCompetitorRosterStatus]): Roster status
        is_neutral_venue (Union[Unset, bool]): Competitor is playing at a neutral venue ?
        uniform_id (Union[None, Unset, str]): The uuid of the uniform
        external_id (Union[Unset, str]): externalId
    """

    entity_id: str
    conference_id: Union[Unset, str] = UNSET
    division_id: Union[Unset, str] = UNSET
    include_in_conference_statistics: Union[Unset, bool] = UNSET
    is_home: Union[Unset, bool] = UNSET
    include_in_representation: Union[Unset, bool] = UNSET
    draw: Union[Unset, bool] = UNSET
    result_status: Union[
        Unset, FixtureInsertMatchPostBodyMatchCompetitorResultStatus
    ] = UNSET
    result_place: Union[None, Unset, float] = UNSET
    result_secondary_score_place: Union[None, Unset, float] = UNSET
    starting_number: Union[None, Unset, float] = UNSET
    score: Union[None, Unset, str] = UNSET
    secondary_score: Union[None, Unset, str] = UNSET
    shoot_out_attempts: Union[None, Unset, str] = UNSET
    roster_status: Union[
        Unset, FixtureInsertMatchPostBodyMatchCompetitorRosterStatus
    ] = UNSET
    is_neutral_venue: Union[Unset, bool] = UNSET
    uniform_id: Union[None, Unset, str] = UNSET
    external_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id = self.entity_id

        conference_id = self.conference_id

        division_id = self.division_id

        include_in_conference_statistics = self.include_in_conference_statistics

        is_home = self.is_home

        include_in_representation = self.include_in_representation

        draw = self.draw

        result_status: Union[Unset, str] = UNSET
        if not isinstance(self.result_status, Unset):
            result_status = self.result_status.value

        result_place: Union[None, Unset, float]
        if isinstance(self.result_place, Unset):
            result_place = UNSET
        else:
            result_place = self.result_place

        result_secondary_score_place: Union[None, Unset, float]
        if isinstance(self.result_secondary_score_place, Unset):
            result_secondary_score_place = UNSET
        else:
            result_secondary_score_place = self.result_secondary_score_place

        starting_number: Union[None, Unset, float]
        if isinstance(self.starting_number, Unset):
            starting_number = UNSET
        else:
            starting_number = self.starting_number

        score: Union[None, Unset, str]
        if isinstance(self.score, Unset):
            score = UNSET
        else:
            score = self.score

        secondary_score: Union[None, Unset, str]
        if isinstance(self.secondary_score, Unset):
            secondary_score = UNSET
        else:
            secondary_score = self.secondary_score

        shoot_out_attempts: Union[None, Unset, str]
        if isinstance(self.shoot_out_attempts, Unset):
            shoot_out_attempts = UNSET
        else:
            shoot_out_attempts = self.shoot_out_attempts

        roster_status: Union[Unset, str] = UNSET
        if not isinstance(self.roster_status, Unset):
            roster_status = self.roster_status.value

        is_neutral_venue = self.is_neutral_venue

        uniform_id: Union[None, Unset, str]
        if isinstance(self.uniform_id, Unset):
            uniform_id = UNSET
        else:
            uniform_id = self.uniform_id

        external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entityId": entity_id,
            }
        )
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if include_in_conference_statistics is not UNSET:
            field_dict["includeInConferenceStatistics"] = (
                include_in_conference_statistics
            )
        if is_home is not UNSET:
            field_dict["isHome"] = is_home
        if include_in_representation is not UNSET:
            field_dict["includeInRepresentation"] = include_in_representation
        if draw is not UNSET:
            field_dict["draw"] = draw
        if result_status is not UNSET:
            field_dict["resultStatus"] = result_status
        if result_place is not UNSET:
            field_dict["resultPlace"] = result_place
        if result_secondary_score_place is not UNSET:
            field_dict["resultSecondaryScorePlace"] = result_secondary_score_place
        if starting_number is not UNSET:
            field_dict["startingNumber"] = starting_number
        if score is not UNSET:
            field_dict["score"] = score
        if secondary_score is not UNSET:
            field_dict["secondaryScore"] = secondary_score
        if shoot_out_attempts is not UNSET:
            field_dict["shootOutAttempts"] = shoot_out_attempts
        if roster_status is not UNSET:
            field_dict["rosterStatus"] = roster_status
        if is_neutral_venue is not UNSET:
            field_dict["isNeutralVenue"] = is_neutral_venue
        if uniform_id is not UNSET:
            field_dict["uniformId"] = uniform_id
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        entity_id = d.pop("entityId")

        conference_id = d.pop("conferenceId", UNSET)

        division_id = d.pop("divisionId", UNSET)

        include_in_conference_statistics = d.pop("includeInConferenceStatistics", UNSET)

        is_home = d.pop("isHome", UNSET)

        include_in_representation = d.pop("includeInRepresentation", UNSET)

        draw = d.pop("draw", UNSET)

        _result_status = d.pop("resultStatus", UNSET)
        result_status: Union[
            Unset, FixtureInsertMatchPostBodyMatchCompetitorResultStatus
        ]
        if isinstance(_result_status, Unset):
            result_status = UNSET
        else:
            result_status = FixtureInsertMatchPostBodyMatchCompetitorResultStatus(
                _result_status
            )

        def _parse_result_place(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        result_place = _parse_result_place(d.pop("resultPlace", UNSET))

        def _parse_result_secondary_score_place(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        result_secondary_score_place = _parse_result_secondary_score_place(
            d.pop("resultSecondaryScorePlace", UNSET)
        )

        def _parse_starting_number(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        starting_number = _parse_starting_number(d.pop("startingNumber", UNSET))

        def _parse_score(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        score = _parse_score(d.pop("score", UNSET))

        def _parse_secondary_score(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        secondary_score = _parse_secondary_score(d.pop("secondaryScore", UNSET))

        def _parse_shoot_out_attempts(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shoot_out_attempts = _parse_shoot_out_attempts(d.pop("shootOutAttempts", UNSET))

        _roster_status = d.pop("rosterStatus", UNSET)
        roster_status: Union[
            Unset, FixtureInsertMatchPostBodyMatchCompetitorRosterStatus
        ]
        if isinstance(_roster_status, Unset):
            roster_status = UNSET
        else:
            roster_status = FixtureInsertMatchPostBodyMatchCompetitorRosterStatus(
                _roster_status
            )

        is_neutral_venue = d.pop("isNeutralVenue", UNSET)

        def _parse_uniform_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uniform_id = _parse_uniform_id(d.pop("uniformId", UNSET))

        external_id = d.pop("externalId", UNSET)

        fixture_insert_match_post_body_match_competitor = cls(
            entity_id=entity_id,
            conference_id=conference_id,
            division_id=division_id,
            include_in_conference_statistics=include_in_conference_statistics,
            is_home=is_home,
            include_in_representation=include_in_representation,
            draw=draw,
            result_status=result_status,
            result_place=result_place,
            result_secondary_score_place=result_secondary_score_place,
            starting_number=starting_number,
            score=score,
            secondary_score=secondary_score,
            shoot_out_attempts=shoot_out_attempts,
            roster_status=roster_status,
            is_neutral_venue=is_neutral_venue,
            uniform_id=uniform_id,
            external_id=external_id,
        )

        return fixture_insert_match_post_body_match_competitor
