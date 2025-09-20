import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_roster_model_position_type_1 import SeasonRosterModelPositionType1
from ..models.season_roster_model_position_type_2_type_1 import (
    SeasonRosterModelPositionType2Type1,
)
from ..models.season_roster_model_position_type_3_type_1 import (
    SeasonRosterModelPositionType3Type1,
)
from ..models.season_roster_model_status import SeasonRosterModelStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_roster_model_conference import SeasonRosterModelConference
    from ..models.season_roster_model_division import SeasonRosterModelDivision
    from ..models.season_roster_model_entity import SeasonRosterModelEntity
    from ..models.season_roster_model_entity_group import SeasonRosterModelEntityGroup
    from ..models.season_roster_model_organization import SeasonRosterModelOrganization
    from ..models.season_roster_model_person import SeasonRosterModelPerson
    from ..models.season_roster_model_season import SeasonRosterModelSeason


T = TypeVar("T", bound="SeasonRosterModel")


@_attrs_define
class SeasonRosterModel:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonRosterModelSeason]): The season linked to this record
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonRosterModelOrganization]): The organization that this season roster belongs to
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, SeasonRosterModelEntity]): The team information
        entity_group_id (Union[None, UUID, Unset]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group (Union[Unset, SeasonRosterModelEntityGroup]): The club that this team belongs to
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division (Union[Unset, SeasonRosterModelDivision]): The division information
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference (Union[Unset, SeasonRosterModelConference]): The conference information
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, SeasonRosterModelPerson]): The person information
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        position (Union[None, SeasonRosterModelPositionType1, SeasonRosterModelPositionType2Type1,
            SeasonRosterModelPositionType3Type1, Unset]): Playing position
            >- None None
            >- `CB` Center Backcourt
            >- `D` Defensive Specialist
            >- `G` Goalkeeper
            >- `LB` Left Backcourt
            >- `LW` Left Wingman
            >- `P` Pivot
            >- `RB` Right Backcourt
            >- `RW` Right Wingman
             Example: G.
        status (Union[Unset, SeasonRosterModelStatus]): Participation status
            >- `ACTIVE` Active
            >- `INJURED` Injured
            >- `OTHER_NOT_PARTICIPATING` Other Non-Participation
            >- `OUT` Out
            >- `SUSPENDED` Suspended
             Example: ACTIVE.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonRosterModelSeason"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonRosterModelOrganization"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "SeasonRosterModelEntity"] = UNSET
    entity_group_id: Union[None, UUID, Unset] = UNSET
    entity_group: Union[Unset, "SeasonRosterModelEntityGroup"] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    division: Union[Unset, "SeasonRosterModelDivision"] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    conference: Union[Unset, "SeasonRosterModelConference"] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "SeasonRosterModelPerson"] = UNSET
    bib: Union[None, Unset, str] = UNSET
    position: Union[
        None,
        SeasonRosterModelPositionType1,
        SeasonRosterModelPositionType2Type1,
        SeasonRosterModelPositionType3Type1,
        Unset,
    ] = UNSET
    status: Union[Unset, SeasonRosterModelStatus] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

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

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        person: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        bib: Union[None, Unset, str]
        if isinstance(self.bib, Unset):
            bib = UNSET
        else:
            bib = self.bib

        position: Union[None, Unset, str]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, SeasonRosterModelPositionType1):
            position = self.position.value
        elif isinstance(self.position, SeasonRosterModelPositionType2Type1):
            position = self.position.value
        elif isinstance(self.position, SeasonRosterModelPositionType3Type1):
            position = self.position.value
        else:
            position = self.position

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_group is not UNSET:
            field_dict["entityGroup"] = entity_group
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if division is not UNSET:
            field_dict["division"] = division
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if conference is not UNSET:
            field_dict["conference"] = conference
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
        if bib is not UNSET:
            field_dict["bib"] = bib
        if position is not UNSET:
            field_dict["position"] = position
        if status is not UNSET:
            field_dict["status"] = status
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_roster_model_conference import SeasonRosterModelConference
        from ..models.season_roster_model_division import SeasonRosterModelDivision
        from ..models.season_roster_model_entity import SeasonRosterModelEntity
        from ..models.season_roster_model_entity_group import (
            SeasonRosterModelEntityGroup,
        )
        from ..models.season_roster_model_organization import (
            SeasonRosterModelOrganization,
        )
        from ..models.season_roster_model_person import SeasonRosterModelPerson
        from ..models.season_roster_model_season import SeasonRosterModelSeason

        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonRosterModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonRosterModelSeason.from_dict(_season)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonRosterModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonRosterModelOrganization.from_dict(_organization)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, SeasonRosterModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = SeasonRosterModelEntity.from_dict(_entity)

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
        entity_group: Union[Unset, SeasonRosterModelEntityGroup]
        if isinstance(_entity_group, Unset):
            entity_group = UNSET
        else:
            entity_group = SeasonRosterModelEntityGroup.from_dict(_entity_group)

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
        division: Union[Unset, SeasonRosterModelDivision]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = SeasonRosterModelDivision.from_dict(_division)

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
        conference: Union[Unset, SeasonRosterModelConference]
        if isinstance(_conference, Unset):
            conference = UNSET
        else:
            conference = SeasonRosterModelConference.from_dict(_conference)

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, SeasonRosterModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = SeasonRosterModelPerson.from_dict(_person)

        def _parse_bib(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bib = _parse_bib(d.pop("bib", UNSET))

        def _parse_position(
            data: object,
        ) -> Union[
            None,
            SeasonRosterModelPositionType1,
            SeasonRosterModelPositionType2Type1,
            SeasonRosterModelPositionType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_1 = SeasonRosterModelPositionType1(data)

                return position_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_2_type_1 = SeasonRosterModelPositionType2Type1(data)

                return position_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_3_type_1 = SeasonRosterModelPositionType3Type1(data)

                return position_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    SeasonRosterModelPositionType1,
                    SeasonRosterModelPositionType2Type1,
                    SeasonRosterModelPositionType3Type1,
                    Unset,
                ],
                data,
            )

        position = _parse_position(d.pop("position", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, SeasonRosterModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeasonRosterModelStatus(_status)

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

        season_roster_model = cls(
            season_id=season_id,
            season=season,
            organization_id=organization_id,
            organization=organization,
            entity_id=entity_id,
            entity=entity,
            entity_group_id=entity_group_id,
            entity_group=entity_group,
            division_id=division_id,
            division=division,
            conference_id=conference_id,
            conference=conference,
            person_id=person_id,
            person=person,
            bib=bib,
            position=position,
            status=status,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return season_roster_model
