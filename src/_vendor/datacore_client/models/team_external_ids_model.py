import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.team_external_ids_model_entity import TeamExternalIdsModelEntity
    from ..models.team_external_ids_model_organization import (
        TeamExternalIdsModelOrganization,
    )


T = TypeVar("T", bound="TeamExternalIdsModel")


@_attrs_define
class TeamExternalIdsModel:
    """
    Attributes:
        entity_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, TeamExternalIdsModelOrganization]): The organization that this team external ids
            belongs to
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, TeamExternalIdsModelEntity]): The team information
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    entity_external_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "TeamExternalIdsModelOrganization"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "TeamExternalIdsModelEntity"] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_external_id, Unset):
            entity_external_id = str(self.entity_external_id)

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

        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entity_external_id is not UNSET:
            field_dict["entityExternalId"] = entity_external_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if source is not UNSET:
            field_dict["source"] = source
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if source_external_id is not UNSET:
            field_dict["sourceExternalId"] = source_external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.team_external_ids_model_entity import TeamExternalIdsModelEntity
        from ..models.team_external_ids_model_organization import (
            TeamExternalIdsModelOrganization,
        )

        d = dict(src_dict)
        _entity_external_id = d.pop("entityExternalId", UNSET)
        entity_external_id: Union[Unset, UUID]
        if isinstance(_entity_external_id, Unset):
            entity_external_id = UNSET
        else:
            entity_external_id = UUID(_entity_external_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, TeamExternalIdsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = TeamExternalIdsModelOrganization.from_dict(_organization)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, TeamExternalIdsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = TeamExternalIdsModelEntity.from_dict(_entity)

        source = d.pop("source", UNSET)

        source_type = d.pop("sourceType", UNSET)

        source_external_id = d.pop("sourceExternalId", UNSET)

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

        team_external_ids_model = cls(
            entity_external_id=entity_external_id,
            organization_id=organization_id,
            organization=organization,
            entity_id=entity_id,
            entity=entity,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            updated=updated,
            added=added,
        )

        return team_external_ids_model
