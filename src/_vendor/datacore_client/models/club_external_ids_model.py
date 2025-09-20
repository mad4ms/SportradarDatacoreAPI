import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.club_external_ids_model_entity_group import (
        ClubExternalIdsModelEntityGroup,
    )
    from ..models.club_external_ids_model_organization import (
        ClubExternalIdsModelOrganization,
    )


T = TypeVar("T", bound="ClubExternalIdsModel")


@_attrs_define
class ClubExternalIdsModel:
    """
    Attributes:
        entity_group_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, ClubExternalIdsModelOrganization]): The organization that this club external ids
            belongs to
        entity_group_id (Union[Unset, UUID]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group (Union[Unset, ClubExternalIdsModelEntityGroup]): The club that this team belongs to
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    entity_group_external_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "ClubExternalIdsModelOrganization"] = UNSET
    entity_group_id: Union[Unset, UUID] = UNSET
    entity_group: Union[Unset, "ClubExternalIdsModelEntityGroup"] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_group_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_group_external_id, Unset):
            entity_group_external_id = str(self.entity_group_external_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        entity_group_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_group_id, Unset):
            entity_group_id = str(self.entity_group_id)

        entity_group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity_group, Unset):
            entity_group = self.entity_group.to_dict()

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
        if entity_group_external_id is not UNSET:
            field_dict["entityGroupExternalId"] = entity_group_external_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_group is not UNSET:
            field_dict["entityGroup"] = entity_group
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
        from ..models.club_external_ids_model_entity_group import (
            ClubExternalIdsModelEntityGroup,
        )
        from ..models.club_external_ids_model_organization import (
            ClubExternalIdsModelOrganization,
        )

        d = dict(src_dict)
        _entity_group_external_id = d.pop("entityGroupExternalId", UNSET)
        entity_group_external_id: Union[Unset, UUID]
        if isinstance(_entity_group_external_id, Unset):
            entity_group_external_id = UNSET
        else:
            entity_group_external_id = UUID(_entity_group_external_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, ClubExternalIdsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = ClubExternalIdsModelOrganization.from_dict(_organization)

        _entity_group_id = d.pop("entityGroupId", UNSET)
        entity_group_id: Union[Unset, UUID]
        if isinstance(_entity_group_id, Unset):
            entity_group_id = UNSET
        else:
            entity_group_id = UUID(_entity_group_id)

        _entity_group = d.pop("entityGroup", UNSET)
        entity_group: Union[Unset, ClubExternalIdsModelEntityGroup]
        if isinstance(_entity_group, Unset):
            entity_group = UNSET
        else:
            entity_group = ClubExternalIdsModelEntityGroup.from_dict(_entity_group)

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

        club_external_ids_model = cls(
            entity_group_external_id=entity_group_external_id,
            organization_id=organization_id,
            organization=organization,
            entity_group_id=entity_group_id,
            entity_group=entity_group,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            updated=updated,
            added=added,
        )

        return club_external_ids_model
