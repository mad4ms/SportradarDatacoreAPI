import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.match_teams_model_result_status import MatchTeamsModelResultStatus
from ..models.match_teams_model_roster_status import MatchTeamsModelRosterStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_teams_model_conference import MatchTeamsModelConference
    from ..models.match_teams_model_division import MatchTeamsModelDivision
    from ..models.match_teams_model_entity import MatchTeamsModelEntity
    from ..models.match_teams_model_fixture import MatchTeamsModelFixture
    from ..models.match_teams_model_organization import MatchTeamsModelOrganization
    from ..models.match_teams_model_uniform import MatchTeamsModelUniform


T = TypeVar("T", bound="MatchTeamsModel")


@_attrs_define
class MatchTeamsModel:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, MatchTeamsModelFixture]): The match
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, MatchTeamsModelOrganization]): The organization that this match teams belongs to
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, MatchTeamsModelEntity]): The team information
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference (Union[Unset, MatchTeamsModelConference]): The conference information
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division (Union[Unset, MatchTeamsModelDivision]): The division information
        include_in_conference_statistics (Union[Unset, bool]): Include the statistics for this competitors in the
            conference statistics? Example: True.
        is_home (Union[Unset, bool]): Is competitor the home team ? Example: True.
        draw (Union[Unset, bool]): Result for this competitor was a draw ? Example: True.
        result_status (Union[Unset, MatchTeamsModelResultStatus]): Result status
            >- `CONFIRMED` Confirmed
            >- `DID_NOT_FINISH` Did Not Finish
            >- `DID_NOT_START` Did Not Start
            >- `DISQUALIFIED` Disqualified
            >- `FORFEITED` Forfeited
            >- `IN_PROGRESS` In Progress
            >- `SCHEDULED` Scheduled
            >- `WITHDRAWN` Withdrawn
            >- `WON_BY_FORFEIT` Won By Forfeit
             Example: CONFIRMED.
        result_place (Union[None, Unset, int]): Result placing (1=Won, 2=Lost) Example: 1.
        result_secondary_score_place (Union[None, Unset, int]): Result placing (1=Won, 2=Lost) of the Shoot Out Example:
            1.
        starting_number (Union[None, Unset, int]): Starting number Example: 1.
        score (Union[None, Unset, str]): Score for competitor in match Example: 98.
        secondary_score (Union[None, Unset, str]): Secondary score (used for shoot-outs) Example: 3v3.
        shoot_out_attempts (Union[None, Unset, str]): Result of shoot-out attempts (1 or 0 per attempt). Example: 11011.
        is_neutral_venue (Union[Unset, bool]): Competitor is playing at a neutral venue ? Example: True.
        include_in_representation (Union[Unset, bool]): Include this match in represented statistics? Default: True.
            Example: True.
        roster_status (Union[Unset, MatchTeamsModelRosterStatus]): The status of the TEAM match teams
            >- `APPROVED` Approved
            >- `PENDING` Pending
            >- `REJECTED` Rejected
            >- `SUBMITTED` Submitted
            >- `UNKNOWN` Unknown
             Default: MatchTeamsModelRosterStatus.UNKNOWN. Example: APPROVED.
        uniform_id (Union[None, UUID, Unset]): The unique identifier of the uniform Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        uniform (Union[Unset, MatchTeamsModelUniform]): The Uniform information
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "MatchTeamsModelFixture"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "MatchTeamsModelOrganization"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "MatchTeamsModelEntity"] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    conference: Union[Unset, "MatchTeamsModelConference"] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    division: Union[Unset, "MatchTeamsModelDivision"] = UNSET
    include_in_conference_statistics: Union[Unset, bool] = UNSET
    is_home: Union[Unset, bool] = UNSET
    draw: Union[Unset, bool] = UNSET
    result_status: Union[Unset, MatchTeamsModelResultStatus] = UNSET
    result_place: Union[None, Unset, int] = UNSET
    result_secondary_score_place: Union[None, Unset, int] = UNSET
    starting_number: Union[None, Unset, int] = UNSET
    score: Union[None, Unset, str] = UNSET
    secondary_score: Union[None, Unset, str] = UNSET
    shoot_out_attempts: Union[None, Unset, str] = UNSET
    is_neutral_venue: Union[Unset, bool] = UNSET
    include_in_representation: Union[Unset, bool] = True
    roster_status: Union[Unset, MatchTeamsModelRosterStatus] = MatchTeamsModelRosterStatus.UNKNOWN
    uniform_id: Union[None, UUID, Unset] = UNSET
    uniform: Union[Unset, "MatchTeamsModelUniform"] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        conference: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conference, Unset):
            conference = self.conference.to_dict()

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        division: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.to_dict()

        include_in_conference_statistics = self.include_in_conference_statistics

        is_home = self.is_home

        draw = self.draw

        result_status: Union[Unset, str] = UNSET
        if not isinstance(self.result_status, Unset):
            result_status = self.result_status.value

        result_place: Union[None, Unset, int]
        if isinstance(self.result_place, Unset):
            result_place = UNSET
        else:
            result_place = self.result_place

        result_secondary_score_place: Union[None, Unset, int]
        if isinstance(self.result_secondary_score_place, Unset):
            result_secondary_score_place = UNSET
        else:
            result_secondary_score_place = self.result_secondary_score_place

        starting_number: Union[None, Unset, int]
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

        is_neutral_venue = self.is_neutral_venue

        include_in_representation = self.include_in_representation

        roster_status: Union[Unset, str] = UNSET
        if not isinstance(self.roster_status, Unset):
            roster_status = self.roster_status.value

        uniform_id: Union[None, Unset, str]
        if isinstance(self.uniform_id, Unset):
            uniform_id = UNSET
        elif isinstance(self.uniform_id, UUID):
            uniform_id = str(self.uniform_id)
        else:
            uniform_id = self.uniform_id

        uniform: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uniform, Unset):
            uniform = self.uniform.to_dict()

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if conference is not UNSET:
            field_dict["conference"] = conference
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if division is not UNSET:
            field_dict["division"] = division
        if include_in_conference_statistics is not UNSET:
            field_dict["includeInConferenceStatistics"] = include_in_conference_statistics
        if is_home is not UNSET:
            field_dict["isHome"] = is_home
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
        if is_neutral_venue is not UNSET:
            field_dict["isNeutralVenue"] = is_neutral_venue
        if include_in_representation is not UNSET:
            field_dict["includeInRepresentation"] = include_in_representation
        if roster_status is not UNSET:
            field_dict["rosterStatus"] = roster_status
        if uniform_id is not UNSET:
            field_dict["uniformId"] = uniform_id
        if uniform is not UNSET:
            field_dict["uniform"] = uniform
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_teams_model_conference import MatchTeamsModelConference
        from ..models.match_teams_model_division import MatchTeamsModelDivision
        from ..models.match_teams_model_entity import MatchTeamsModelEntity
        from ..models.match_teams_model_fixture import MatchTeamsModelFixture
        from ..models.match_teams_model_organization import MatchTeamsModelOrganization
        from ..models.match_teams_model_uniform import MatchTeamsModelUniform

        d = dict(src_dict)
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, MatchTeamsModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = MatchTeamsModelFixture.from_dict(_fixture)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, MatchTeamsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = MatchTeamsModelOrganization.from_dict(_organization)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, MatchTeamsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = MatchTeamsModelEntity.from_dict(_entity)

        def _parse_conference_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conference_id_type_0 = UUID(data)

                return conference_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        conference_id = _parse_conference_id(d.pop("conferenceId", UNSET))

        _conference = d.pop("conference", UNSET)
        conference: Union[Unset, MatchTeamsModelConference]
        if isinstance(_conference, Unset):
            conference = UNSET
        else:
            conference = MatchTeamsModelConference.from_dict(_conference)

        def _parse_division_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                division_id_type_0 = UUID(data)

                return division_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        division_id = _parse_division_id(d.pop("divisionId", UNSET))

        _division = d.pop("division", UNSET)
        division: Union[Unset, MatchTeamsModelDivision]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = MatchTeamsModelDivision.from_dict(_division)

        include_in_conference_statistics = d.pop("includeInConferenceStatistics", UNSET)

        is_home = d.pop("isHome", UNSET)

        draw = d.pop("draw", UNSET)

        _result_status = d.pop("resultStatus", UNSET)
        result_status: Union[Unset, MatchTeamsModelResultStatus]
        if isinstance(_result_status, Unset):
            result_status = UNSET
        else:
            result_status = MatchTeamsModelResultStatus(_result_status)

        def _parse_result_place(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        result_place = _parse_result_place(d.pop("resultPlace", UNSET))

        def _parse_result_secondary_score_place(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        result_secondary_score_place = _parse_result_secondary_score_place(d.pop("resultSecondaryScorePlace", UNSET))

        def _parse_starting_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

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

        is_neutral_venue = d.pop("isNeutralVenue", UNSET)

        include_in_representation = d.pop("includeInRepresentation", UNSET)

        _roster_status = d.pop("rosterStatus", UNSET)
        roster_status: Union[Unset, MatchTeamsModelRosterStatus]
        if isinstance(_roster_status, Unset):
            roster_status = UNSET
        else:
            roster_status = MatchTeamsModelRosterStatus(_roster_status)

        def _parse_uniform_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                uniform_id_type_0 = UUID(data)

                return uniform_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        uniform_id = _parse_uniform_id(d.pop("uniformId", UNSET))

        _uniform = d.pop("uniform", UNSET)
        uniform: Union[Unset, MatchTeamsModelUniform]
        if isinstance(_uniform, Unset):
            uniform = UNSET
        else:
            uniform = MatchTeamsModelUniform.from_dict(_uniform)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        match_teams_model = cls(
            fixture_id=fixture_id,
            fixture=fixture,
            organization_id=organization_id,
            organization=organization,
            entity_id=entity_id,
            entity=entity,
            conference_id=conference_id,
            conference=conference,
            division_id=division_id,
            division=division,
            include_in_conference_statistics=include_in_conference_statistics,
            is_home=is_home,
            draw=draw,
            result_status=result_status,
            result_place=result_place,
            result_secondary_score_place=result_secondary_score_place,
            starting_number=starting_number,
            score=score,
            secondary_score=secondary_score,
            shoot_out_attempts=shoot_out_attempts,
            is_neutral_venue=is_neutral_venue,
            include_in_representation=include_in_representation,
            roster_status=roster_status,
            uniform_id=uniform_id,
            uniform=uniform,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return match_teams_model
