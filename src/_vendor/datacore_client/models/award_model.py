import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.award_model_award import AwardModelAward
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.award_model_competition import AwardModelCompetition
    from ..models.award_model_entity import AwardModelEntity
    from ..models.award_model_entity_group import AwardModelEntityGroup
    from ..models.award_model_fixture import AwardModelFixture
    from ..models.award_model_organization import AwardModelOrganization
    from ..models.award_model_person import AwardModelPerson
    from ..models.award_model_season import AwardModelSeason


T = TypeVar("T", bound="AwardModel")


@_attrs_define
class AwardModel:
    """
    Attributes:
        award_id (Union[Unset, UUID]): The unique identifier of the award Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, AwardModelOrganization]): The organization that this ~award~ belongs to
        person_id (Union[Unset, UUID]): The person that this award is for Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, AwardModelPerson]): The person information
        entity_group_id (Union[Unset, UUID]): The club that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group (Union[Unset, AwardModelEntityGroup]): The club that this team belongs to
        entity_id (Union[Unset, UUID]): The team that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, AwardModelEntity]): The team information
        competition_id (Union[Unset, UUID]): The competition that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, AwardModelCompetition]): The competition that this season belongs to
        season_id (Union[Unset, UUID]): The season that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, AwardModelSeason]): The season linked to this record
        fixture_id (Union[Unset, UUID]): The match that this award is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, AwardModelFixture]): The match
        votes (Union[None, Unset, int]): Number of votes Example: 1.
        date_from (Union[None, Unset, datetime.date]): Date the award is from Example: 1978-08-24.
        date_to (Union[None, Unset, datetime.date]): Date the award is until Example: 1978-08-24.
        award (Union[Unset, AwardModelAward]): Award
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
        award_sub_type (Union[None, Unset, str]): Award sub type Example: 1st Team.
        notes (Union[None, Unset, str]): Award Notes
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    award_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "AwardModelOrganization"] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "AwardModelPerson"] = UNSET
    entity_group_id: Union[Unset, UUID] = UNSET
    entity_group: Union[Unset, "AwardModelEntityGroup"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "AwardModelEntity"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "AwardModelCompetition"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "AwardModelSeason"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "AwardModelFixture"] = UNSET
    votes: Union[None, Unset, int] = UNSET
    date_from: Union[None, Unset, datetime.date] = UNSET
    date_to: Union[None, Unset, datetime.date] = UNSET
    award: Union[Unset, AwardModelAward] = UNSET
    award_sub_type: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        award_id: Union[Unset, str] = UNSET
        if not isinstance(self.award_id, Unset):
            award_id = str(self.award_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        person: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        entity_group_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_group_id, Unset):
            entity_group_id = str(self.entity_group_id)

        entity_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_group, Unset):
            entity_group = self.entity_group.to_dict()

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        competition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

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

        award: Union[Unset, str] = UNSET
        if not isinstance(self.award, Unset):
            award = self.award.value

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

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if award_id is not UNSET:
            field_dict["awardId"] = award_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_group is not UNSET:
            field_dict["entityGroup"] = entity_group
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if votes is not UNSET:
            field_dict["votes"] = votes
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if award is not UNSET:
            field_dict["award"] = award
        if award_sub_type is not UNSET:
            field_dict["awardSubType"] = award_sub_type
        if notes is not UNSET:
            field_dict["notes"] = notes
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.award_model_competition import AwardModelCompetition
        from ..models.award_model_entity import AwardModelEntity
        from ..models.award_model_entity_group import AwardModelEntityGroup
        from ..models.award_model_fixture import AwardModelFixture
        from ..models.award_model_organization import AwardModelOrganization
        from ..models.award_model_person import AwardModelPerson
        from ..models.award_model_season import AwardModelSeason

        d = dict(src_dict)
        _award_id = d.pop("awardId", UNSET)
        award_id: Union[Unset, UUID]
        if isinstance(_award_id, Unset):
            award_id = UNSET
        else:
            award_id = UUID(_award_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, AwardModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = AwardModelOrganization.from_dict(_organization)

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, AwardModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = AwardModelPerson.from_dict(_person)

        _entity_group_id = d.pop("entityGroupId", UNSET)
        entity_group_id: Union[Unset, UUID]
        if isinstance(_entity_group_id, Unset):
            entity_group_id = UNSET
        else:
            entity_group_id = UUID(_entity_group_id)

        _entity_group = d.pop("entityGroup", UNSET)
        entity_group: Union[Unset, AwardModelEntityGroup]
        if isinstance(_entity_group, Unset):
            entity_group = UNSET
        else:
            entity_group = AwardModelEntityGroup.from_dict(_entity_group)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, AwardModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = AwardModelEntity.from_dict(_entity)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, AwardModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = AwardModelCompetition.from_dict(_competition)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, AwardModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = AwardModelSeason.from_dict(_season)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, AwardModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = AwardModelFixture.from_dict(_fixture)

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

        _award = d.pop("award", UNSET)
        award: Union[Unset, AwardModelAward]
        if isinstance(_award, Unset):
            award = UNSET
        else:
            award = AwardModelAward(_award)

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

        award_model = cls(
            award_id=award_id,
            organization_id=organization_id,
            organization=organization,
            person_id=person_id,
            person=person,
            entity_group_id=entity_group_id,
            entity_group=entity_group,
            entity_id=entity_id,
            entity=entity,
            competition_id=competition_id,
            competition=competition,
            season_id=season_id,
            season=season,
            fixture_id=fixture_id,
            fixture=fixture,
            votes=votes,
            date_from=date_from,
            date_to=date_to,
            award=award,
            award_sub_type=award_sub_type,
            notes=notes,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return award_model
