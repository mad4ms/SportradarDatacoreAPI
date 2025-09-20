import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.award_post_body_award import AwardPostBodyAward
from ..types import UNSET, Unset

T = TypeVar("T", bound="AwardPostBody")


@_attrs_define
class AwardPostBody:
    """
    Attributes:
        person_id (UUID): The person that this award is for Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        award (AwardPostBodyAward): Award
            >- `ALL_TEAM` All first team
            >- `COACH` Coach Award
            >- `DEFENSIVE` Defensive Player
            >- `DEFENSIVE_TEAM` Defensive team
            >- `HALL` Hall of Fame
            >- `HONOUR` Honoured
            >- `MIP` Most Improved Player
            >- `MVP` Most Valuable Player
            >- `OTHER` Other
            >- `ROOKIE` Rookie
             Example: MVP.
        award_id (Union[Unset, UUID]): The unique identifier of the award Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group_id (Union[Unset, UUID]): The club that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The team that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition_id (Union[Unset, UUID]): The competition that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]): The season that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (Union[Unset, UUID]): The match that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        votes (Union[None, Unset, int]): Number of votes Example: 1.
        date_from (Union[None, Unset, datetime.date]): Date the award is from Example: 1978-08-24.
        date_to (Union[None, Unset, datetime.date]): Date the award is until Example: 1978-08-24.
        award_sub_type (Union[None, Unset, str]): Award sub type Example: 1st Team.
        notes (Union[None, Unset, str]): Award Notes
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    person_id: UUID
    award: AwardPostBodyAward
    award_id: Union[Unset, UUID] = UNSET
    entity_group_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    votes: Union[None, Unset, int] = UNSET
    date_from: Union[None, Unset, datetime.date] = UNSET
    date_to: Union[None, Unset, datetime.date] = UNSET
    award_sub_type: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        person_id = str(self.person_id)

        award = self.award.value

        award_id: Union[Unset, str] = UNSET
        if not isinstance(self.award_id, Unset):
            award_id = str(self.award_id)

        entity_group_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_group_id, Unset):
            entity_group_id = str(self.entity_group_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        votes: Union[None, Unset, int]
        if isinstance(self.votes, Unset):
            votes = UNSET
        else:
            votes = self.votes

        date_from: Union[None, Unset, str]
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        elif isinstance(self.date_from, datetime.date):
            date_from = self.date_from.isoformat()
        else:
            date_from = self.date_from

        date_to: Union[None, Unset, str]
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        elif isinstance(self.date_to, datetime.date):
            date_to = self.date_to.isoformat()
        else:
            date_to = self.date_to

        award_sub_type: Union[None, Unset, str]
        if isinstance(self.award_sub_type, Unset):
            award_sub_type = UNSET
        else:
            award_sub_type = self.award_sub_type

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "award": award,
            }
        )
        if award_id is not UNSET:
            field_dict["awardId"] = award_id
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if votes is not UNSET:
            field_dict["votes"] = votes
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if award_sub_type is not UNSET:
            field_dict["awardSubType"] = award_sub_type
        if notes is not UNSET:
            field_dict["notes"] = notes
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = UUID(d.pop("personId"))

        award = AwardPostBodyAward(d.pop("award"))

        _award_id = d.pop("awardId", UNSET)
        award_id: Union[Unset, UUID]
        if isinstance(_award_id, Unset):
            award_id = UNSET
        else:
            award_id = UUID(_award_id)

        _entity_group_id = d.pop("entityGroupId", UNSET)
        entity_group_id: Union[Unset, UUID]
        if isinstance(_entity_group_id, Unset):
            entity_group_id = UNSET
        else:
            entity_group_id = UUID(_entity_group_id)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        def _parse_votes(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        votes = _parse_votes(d.pop("votes", UNSET))

        def _parse_date_from(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_type_0 = isoparse(data).date()

                return date_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_from = _parse_date_from(d.pop("dateFrom", UNSET))

        def _parse_date_to(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_to_type_0 = isoparse(data).date()

                return date_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_to = _parse_date_to(d.pop("dateTo", UNSET))

        def _parse_award_sub_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        award_sub_type = _parse_award_sub_type(d.pop("awardSubType", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        award_post_body = cls(
            person_id=person_id,
            award=award,
            award_id=award_id,
            entity_group_id=entity_group_id,
            entity_id=entity_id,
            competition_id=competition_id,
            season_id=season_id,
            fixture_id=fixture_id,
            votes=votes,
            date_from=date_from,
            date_to=date_to,
            award_sub_type=award_sub_type,
            notes=notes,
            external_id=external_id,
        )

        return award_post_body
