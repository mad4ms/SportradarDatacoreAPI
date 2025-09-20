import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_external_ids_model_organization import SeasonExternalIdsModelOrganization
    from ..models.season_external_ids_model_season import SeasonExternalIdsModelSeason


T = TypeVar("T", bound="SeasonExternalIdsModel")


@_attrs_define
class SeasonExternalIdsModel:
    """
    Attributes:
        season_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonExternalIdsModelOrganization]): The organization that this season external ids
            belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonExternalIdsModelSeason]): The season linked to this record
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    season_external_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonExternalIdsModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonExternalIdsModelSeason"] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_external_id, Unset):
            season_external_id = str(self.season_external_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

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
        if season_external_id is not UNSET:
            field_dict["seasonExternalId"] = season_external_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
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
        from ..models.season_external_ids_model_organization import SeasonExternalIdsModelOrganization
        from ..models.season_external_ids_model_season import SeasonExternalIdsModelSeason

        d = dict(src_dict)
        _season_external_id = d.pop("seasonExternalId", UNSET)
        season_external_id: Union[Unset, UUID]
        if isinstance(_season_external_id, Unset):
            season_external_id = UNSET
        else:
            season_external_id = UUID(_season_external_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonExternalIdsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonExternalIdsModelOrganization.from_dict(_organization)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonExternalIdsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonExternalIdsModelSeason.from_dict(_season)

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

        season_external_ids_model = cls(
            season_external_id=season_external_id,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            updated=updated,
            added=added,
        )

        return season_external_ids_model
