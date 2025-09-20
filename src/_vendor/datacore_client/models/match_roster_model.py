import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.match_roster_model_position_type_1 import MatchRosterModelPositionType1
from ..models.match_roster_model_position_type_2_type_1 import (
    MatchRosterModelPositionType2Type1,
)
from ..models.match_roster_model_position_type_3_type_1 import (
    MatchRosterModelPositionType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_roster_model_entity import MatchRosterModelEntity
    from ..models.match_roster_model_fixture import MatchRosterModelFixture
    from ..models.match_roster_model_organization import MatchRosterModelOrganization
    from ..models.match_roster_model_person import MatchRosterModelPerson


T = TypeVar("T", bound="MatchRosterModel")


@_attrs_define
class MatchRosterModel:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, MatchRosterModelFixture]): The match
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, MatchRosterModelOrganization]): The organization that this match roster belongs to
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, MatchRosterModelEntity]): The team information
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, MatchRosterModelPerson]): The person information
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        position (Union[MatchRosterModelPositionType1, MatchRosterModelPositionType2Type1,
            MatchRosterModelPositionType3Type1, None, Unset]): Playing position
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
        starter (Union[Unset, bool]): Did person start the match on the court Example: True.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "MatchRosterModelFixture"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "MatchRosterModelOrganization"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "MatchRosterModelEntity"] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "MatchRosterModelPerson"] = UNSET
    bib: Union[None, Unset, str] = UNSET
    position: Union[
        MatchRosterModelPositionType1,
        MatchRosterModelPositionType2Type1,
        MatchRosterModelPositionType3Type1,
        None,
        Unset,
    ] = UNSET
    starter: Union[Unset, bool] = UNSET
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
        elif isinstance(self.position, MatchRosterModelPositionType1):
            position = self.position.value
        elif isinstance(self.position, MatchRosterModelPositionType2Type1):
            position = self.position.value
        elif isinstance(self.position, MatchRosterModelPositionType3Type1):
            position = self.position.value
        else:
            position = self.position

        starter = self.starter

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
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
        if bib is not UNSET:
            field_dict["bib"] = bib
        if position is not UNSET:
            field_dict["position"] = position
        if starter is not UNSET:
            field_dict["starter"] = starter
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_roster_model_entity import MatchRosterModelEntity
        from ..models.match_roster_model_fixture import MatchRosterModelFixture
        from ..models.match_roster_model_organization import (
            MatchRosterModelOrganization,
        )
        from ..models.match_roster_model_person import MatchRosterModelPerson

        d = dict(src_dict)
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, MatchRosterModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = MatchRosterModelFixture.from_dict(_fixture)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, MatchRosterModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = MatchRosterModelOrganization.from_dict(_organization)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, MatchRosterModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = MatchRosterModelEntity.from_dict(_entity)

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, MatchRosterModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = MatchRosterModelPerson.from_dict(_person)

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
            MatchRosterModelPositionType1,
            MatchRosterModelPositionType2Type1,
            MatchRosterModelPositionType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_1 = MatchRosterModelPositionType1(data)

                return position_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_2_type_1 = MatchRosterModelPositionType2Type1(data)

                return position_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_3_type_1 = MatchRosterModelPositionType3Type1(data)

                return position_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    MatchRosterModelPositionType1,
                    MatchRosterModelPositionType2Type1,
                    MatchRosterModelPositionType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        position = _parse_position(d.pop("position", UNSET))

        starter = d.pop("starter", UNSET)

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

        match_roster_model = cls(
            fixture_id=fixture_id,
            fixture=fixture,
            organization_id=organization_id,
            organization=organization,
            entity_id=entity_id,
            entity=entity,
            person_id=person_id,
            person=person,
            bib=bib,
            position=position,
            starter=starter,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return match_roster_model
