from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.fixture_persons_insert_update_match_persons_post_body_result_status import (
    FixturePersonsInsertUpdateMatchPersonsPostBodyResultStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FixturePersonsInsertUpdateMatchPersonsPostBody")


@_attrs_define
class FixturePersonsInsertUpdateMatchPersonsPostBody:
    """
    Attributes:
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id (UUID): The unique identifier of the person Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        result_status (FixturePersonsInsertUpdateMatchPersonsPostBodyResultStatus): Result status
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
        entity_group_id (Union[None, UUID, Unset]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        is_home (Union[Unset, bool]): Is competitor the home person ? Example: True.
        draw (Union[Unset, bool]): Result for this competitor was a draw ? Example: True.
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
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    fixture_id: UUID
    person_id: UUID
    result_status: FixturePersonsInsertUpdateMatchPersonsPostBodyResultStatus
    entity_group_id: Union[None, UUID, Unset] = UNSET
    is_home: Union[Unset, bool] = UNSET
    draw: Union[Unset, bool] = UNSET
    result_place: Union[None, Unset, int] = UNSET
    result_secondary_score_place: Union[None, Unset, int] = UNSET
    starting_number: Union[None, Unset, int] = UNSET
    score: Union[None, Unset, str] = UNSET
    secondary_score: Union[None, Unset, str] = UNSET
    is_neutral_venue: Union[Unset, bool] = UNSET
    include_in_representation: Union[Unset, bool] = True
    uniform_id: Union[None, UUID, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id = str(self.fixture_id)

        person_id = str(self.person_id)

        result_status = self.result_status.value

        entity_group_id: Union[None, Unset, str]
        if isinstance(self.entity_group_id, Unset):
            entity_group_id = UNSET
        elif isinstance(self.entity_group_id, UUID):
            entity_group_id = str(self.entity_group_id)
        else:
            entity_group_id = self.entity_group_id

        is_home = self.is_home

        draw = self.draw

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

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fixtureId": fixture_id,
                "personId": person_id,
                "resultStatus": result_status,
            }
        )
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if is_home is not UNSET:
            field_dict["isHome"] = is_home
        if draw is not UNSET:
            field_dict["draw"] = draw
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
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixture_id = UUID(d.pop("fixtureId"))

        person_id = UUID(d.pop("personId"))

        result_status = FixturePersonsInsertUpdateMatchPersonsPostBodyResultStatus(
            d.pop("resultStatus")
        )

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

        is_home = d.pop("isHome", UNSET)

        draw = d.pop("draw", UNSET)

        def _parse_result_place(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        result_place = _parse_result_place(d.pop("resultPlace", UNSET))

        def _parse_result_secondary_score_place(
            data: object,
        ) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        result_secondary_score_place = _parse_result_secondary_score_place(
            d.pop("resultSecondaryScorePlace", UNSET)
        )

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

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        fixture_persons_insert_update_match_persons_post_body = cls(
            fixture_id=fixture_id,
            person_id=person_id,
            result_status=result_status,
            entity_group_id=entity_group_id,
            is_home=is_home,
            draw=draw,
            result_place=result_place,
            result_secondary_score_place=result_secondary_score_place,
            starting_number=starting_number,
            score=score,
            secondary_score=secondary_score,
            is_neutral_venue=is_neutral_venue,
            include_in_representation=include_in_representation,
            uniform_id=uniform_id,
            external_id=external_id,
        )

        return fixture_persons_insert_update_match_persons_post_body
