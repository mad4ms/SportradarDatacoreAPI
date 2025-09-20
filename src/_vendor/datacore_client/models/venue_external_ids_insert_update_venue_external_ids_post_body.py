from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="VenueExternalIdsInsertUpdateVenueExternalIdsPostBody")


@_attrs_define
class VenueExternalIdsInsertUpdateVenueExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        venue_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        venue_id (Union[Unset, UUID]): The unique identifier of the venue Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    venue_external_id: Union[Unset, UUID] = UNSET
    venue_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        venue_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.venue_external_id, Unset):
            venue_external_id = str(self.venue_external_id)

        venue_id: Union[Unset, str] = UNSET
        if not isinstance(self.venue_id, Unset):
            venue_id = str(self.venue_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if venue_external_id is not UNSET:
            field_dict["venueExternalId"] = venue_external_id
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _venue_external_id = d.pop("venueExternalId", UNSET)
        venue_external_id: Union[Unset, UUID]
        if isinstance(_venue_external_id, Unset):
            venue_external_id = UNSET
        else:
            venue_external_id = UUID(_venue_external_id)

        _venue_id = d.pop("venueId", UNSET)
        venue_id: Union[Unset, UUID]
        if isinstance(_venue_id, Unset):
            venue_id = UNSET
        else:
            venue_id = UUID(_venue_id)

        venue_external_ids_insert_update_venue_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            venue_external_id=venue_external_id,
            venue_id=venue_id,
        )

        return venue_external_ids_insert_update_venue_external_ids_post_body
