import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.match_persons_model_result_status import MatchPersonsModelResultStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_persons_model_entity_group import MatchPersonsModelEntityGroup
    from ..models.match_persons_model_fixture import MatchPersonsModelFixture
    from ..models.match_persons_model_organization import MatchPersonsModelOrganization
    from ..models.match_persons_model_person import MatchPersonsModelPerson
    from ..models.match_persons_model_uniform import MatchPersonsModelUniform


T = TypeVar("T", bound="MatchPersonsModel")


@_attrs_define
class MatchPersonsModel:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, MatchPersonsModelFixture]): The match
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, MatchPersonsModelPerson]): The person information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, MatchPersonsModelOrganization]): The organization that this match persons belongs to
        entity_group_id (Union[None, UUID, Unset]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group (Union[Unset, MatchPersonsModelEntityGroup]): The club that this team belongs to
        is_home (Union[Unset, bool]): Is competitor the home person ? Example: True.
        draw (Union[Unset, bool]): Result for this competitor was a draw ? Example: True.
        result_status (Union[Unset, MatchPersonsModelResultStatus]): Result status
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
        secondary_score (Union[None, Unset, str]): Secondary score Example: 3v3.
        is_neutral_venue (Union[Unset, bool]): Competitor is playing at a neutral venue ? Example: True.
        include_in_representation (Union[Unset, bool]): Include this match in represented statistics? Default: True.
            Example: True.
        uniform_id (Union[None, UUID, Unset]): The unique identifier of the uniform Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        uniform (Union[Unset, MatchPersonsModelUniform]): The Uniform information
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "MatchPersonsModelFixture"] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "MatchPersonsModelPerson"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "MatchPersonsModelOrganization"] = UNSET
    entity_group_id: Union[None, UUID, Unset] = UNSET
    entity_group: Union[Unset, "MatchPersonsModelEntityGroup"] = UNSET
    is_home: Union[Unset, bool] = UNSET
    draw: Union[Unset, bool] = UNSET
    result_status: Union[Unset, MatchPersonsModelResultStatus] = UNSET
    result_place: Union[None, Unset, int] = UNSET
    result_secondary_score_place: Union[None, Unset, int] = UNSET
    starting_number: Union[None, Unset, int] = UNSET
    score: Union[None, Unset, str] = UNSET
    secondary_score: Union[None, Unset, str] = UNSET
    is_neutral_venue: Union[Unset, bool] = UNSET
    include_in_representation: Union[Unset, bool] = True
    uniform_id: Union[None, UUID, Unset] = UNSET
    uniform: Union[Unset, "MatchPersonsModelUniform"] = UNSET
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

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        person: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        entity_group_id: Union[None, Unset, str]
        if isinstance(self.entity_group_id, Unset):
            entity_group_id = UNSET
        elif isinstance(self.entity_group_id, UUID):
            entity_group_id = str(self.entity_group_id)
        else:
            entity_group_id = self.entity_group_id

        entity_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_group, Unset):
            entity_group = self.entity_group.to_dict()

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

        is_neutral_venue = self.is_neutral_venue

        include_in_representation = self.include_in_representation

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
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_group is not UNSET:
            field_dict["entityGroup"] = entity_group
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
        if is_neutral_venue is not UNSET:
            field_dict["isNeutralVenue"] = is_neutral_venue
        if include_in_representation is not UNSET:
            field_dict["includeInRepresentation"] = include_in_representation
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
        from ..models.match_persons_model_entity_group import MatchPersonsModelEntityGroup
        from ..models.match_persons_model_fixture import MatchPersonsModelFixture
        from ..models.match_persons_model_organization import MatchPersonsModelOrganization
        from ..models.match_persons_model_person import MatchPersonsModelPerson
        from ..models.match_persons_model_uniform import MatchPersonsModelUniform

        d = dict(src_dict)
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, MatchPersonsModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = MatchPersonsModelFixture.from_dict(_fixture)

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, MatchPersonsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = MatchPersonsModelPerson.from_dict(_person)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, MatchPersonsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = MatchPersonsModelOrganization.from_dict(_organization)

        def _parse_entity_group_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_group_id_type_0 = UUID(data)

                return entity_group_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        entity_group_id = _parse_entity_group_id(d.pop("entityGroupId", UNSET))

        _entity_group = d.pop("entityGroup", UNSET)
        entity_group: Union[Unset, MatchPersonsModelEntityGroup]
        if isinstance(_entity_group, Unset):
            entity_group = UNSET
        else:
            entity_group = MatchPersonsModelEntityGroup.from_dict(_entity_group)

        is_home = d.pop("isHome", UNSET)

        draw = d.pop("draw", UNSET)

        _result_status = d.pop("resultStatus", UNSET)
        result_status: Union[Unset, MatchPersonsModelResultStatus]
        if isinstance(_result_status, Unset):
            result_status = UNSET
        else:
            result_status = MatchPersonsModelResultStatus(_result_status)

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

        is_neutral_venue = d.pop("isNeutralVenue", UNSET)

        include_in_representation = d.pop("includeInRepresentation", UNSET)

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
        uniform: Union[Unset, MatchPersonsModelUniform]
        if isinstance(_uniform, Unset):
            uniform = UNSET
        else:
            uniform = MatchPersonsModelUniform.from_dict(_uniform)

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

        match_persons_model = cls(
            fixture_id=fixture_id,
            fixture=fixture,
            person_id=person_id,
            person=person,
            organization_id=organization_id,
            organization=organization,
            entity_group_id=entity_group_id,
            entity_group=entity_group,
            is_home=is_home,
            draw=draw,
            result_status=result_status,
            result_place=result_place,
            result_secondary_score_place=result_secondary_score_place,
            starting_number=starting_number,
            score=score,
            secondary_score=secondary_score,
            is_neutral_venue=is_neutral_venue,
            include_in_representation=include_in_representation,
            uniform_id=uniform_id,
            uniform=uniform,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return match_persons_model
