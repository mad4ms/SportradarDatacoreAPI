import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_persons_model_status import SeasonPersonsModelStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_persons_model_entity_group import SeasonPersonsModelEntityGroup
    from ..models.season_persons_model_organization import SeasonPersonsModelOrganization
    from ..models.season_persons_model_person import SeasonPersonsModelPerson
    from ..models.season_persons_model_season import SeasonPersonsModelSeason


T = TypeVar("T", bound="SeasonPersonsModel")


@_attrs_define
class SeasonPersonsModel:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonPersonsModelSeason]): The season linked to this record
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonPersonsModelOrganization]): The organization that this season persons belongs
            to
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, SeasonPersonsModelPerson]): The person information
        entity_group_id (Union[Unset, UUID]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group (Union[Unset, SeasonPersonsModelEntityGroup]): The club that this team belongs to
        status (Union[Unset, SeasonPersonsModelStatus]): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        seed (Union[Unset, int]): Initial seeding
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonPersonsModelSeason"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonPersonsModelOrganization"] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "SeasonPersonsModelPerson"] = UNSET
    entity_group_id: Union[Unset, UUID] = UNSET
    entity_group: Union[Unset, "SeasonPersonsModelEntityGroup"] = UNSET
    status: Union[Unset, SeasonPersonsModelStatus] = UNSET
    seed: Union[Unset, int] = UNSET
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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        seed = self.seed

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
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_group is not UNSET:
            field_dict["entityGroup"] = entity_group
        if status is not UNSET:
            field_dict["status"] = status
        if seed is not UNSET:
            field_dict["seed"] = seed
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_persons_model_entity_group import SeasonPersonsModelEntityGroup
        from ..models.season_persons_model_organization import SeasonPersonsModelOrganization
        from ..models.season_persons_model_person import SeasonPersonsModelPerson
        from ..models.season_persons_model_season import SeasonPersonsModelSeason

        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonPersonsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonPersonsModelSeason.from_dict(_season)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonPersonsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonPersonsModelOrganization.from_dict(_organization)

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, SeasonPersonsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = SeasonPersonsModelPerson.from_dict(_person)

        _entity_group_id = d.pop("entityGroupId", UNSET)
        entity_group_id: Union[Unset, UUID]
        if isinstance(_entity_group_id, Unset):
            entity_group_id = UNSET
        else:
            entity_group_id = UUID(_entity_group_id)

        _entity_group = d.pop("entityGroup", UNSET)
        entity_group: Union[Unset, SeasonPersonsModelEntityGroup]
        if isinstance(_entity_group, Unset):
            entity_group = UNSET
        else:
            entity_group = SeasonPersonsModelEntityGroup.from_dict(_entity_group)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SeasonPersonsModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeasonPersonsModelStatus(_status)

        seed = d.pop("seed", UNSET)

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

        season_persons_model = cls(
            season_id=season_id,
            season=season,
            organization_id=organization_id,
            organization=organization,
            person_id=person_id,
            person=person,
            entity_group_id=entity_group_id,
            entity_group=entity_group,
            status=status,
            seed=seed,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return season_persons_model
