import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.venue_external_ids_model_organization import (
        VenueExternalIdsModelOrganization,
    )
    from ..models.venue_external_ids_model_venue import VenueExternalIdsModelVenue


T = TypeVar("T", bound="VenueExternalIdsModel")


@_attrs_define
class VenueExternalIdsModel:
    """
    Attributes:
        venue_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, VenueExternalIdsModelOrganization]): The organization that this venue external ids
            belongs to
        venue_id (Union[Unset, UUID]): The unique identifier of the venue Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        venue (Union[Unset, VenueExternalIdsModelVenue]): The venue that this match belongs to
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    venue_external_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "VenueExternalIdsModelOrganization"] = UNSET
    venue_id: Union[Unset, UUID] = UNSET
    venue: Union[Unset, "VenueExternalIdsModelVenue"] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        venue_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.venue_external_id, Unset):
            venue_external_id = str(self.venue_external_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        venue_id: Union[Unset, str] = UNSET
        if not isinstance(self.venue_id, Unset):
            venue_id = str(self.venue_id)

        venue: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.venue, Unset):
            venue = self.venue.to_dict()

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
        if venue_external_id is not UNSET:
            field_dict["venueExternalId"] = venue_external_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id
        if venue is not UNSET:
            field_dict["venue"] = venue
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
        from ..models.venue_external_ids_model_organization import (
            VenueExternalIdsModelOrganization,
        )
        from ..models.venue_external_ids_model_venue import VenueExternalIdsModelVenue

        d = dict(src_dict)
        _venue_external_id = d.pop("venueExternalId", UNSET)
        venue_external_id: Union[Unset, UUID]
        if isinstance(_venue_external_id, Unset):
            venue_external_id = UNSET
        else:
            venue_external_id = UUID(_venue_external_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, VenueExternalIdsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = VenueExternalIdsModelOrganization.from_dict(_organization)

        _venue_id = d.pop("venueId", UNSET)
        venue_id: Union[Unset, UUID]
        if isinstance(_venue_id, Unset):
            venue_id = UNSET
        else:
            venue_id = UUID(_venue_id)

        _venue = d.pop("venue", UNSET)
        venue: Union[Unset, VenueExternalIdsModelVenue]
        if isinstance(_venue, Unset):
            venue = UNSET
        else:
            venue = VenueExternalIdsModelVenue.from_dict(_venue)

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

        venue_external_ids_model = cls(
            venue_external_id=venue_external_id,
            organization_id=organization_id,
            organization=organization,
            venue_id=venue_id,
            venue=venue,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            updated=updated,
            added=added,
        )

        return venue_external_ids_model
