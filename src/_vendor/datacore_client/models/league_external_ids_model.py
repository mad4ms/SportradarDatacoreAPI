import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.league_external_ids_model_league import LeagueExternalIdsModelLeague
    from ..models.league_external_ids_model_organization import LeagueExternalIdsModelOrganization


T = TypeVar("T", bound="LeagueExternalIdsModel")


@_attrs_define
class LeagueExternalIdsModel:
    """
    Attributes:
        league_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, LeagueExternalIdsModelOrganization]): The organization that this league external ids
            belongs to
        league_id (Union[Unset, UUID]): The unique identifier of the league Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        league (Union[Unset, LeagueExternalIdsModelLeague]): The league that this league external ids belongs to
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    league_external_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "LeagueExternalIdsModelOrganization"] = UNSET
    league_id: Union[Unset, UUID] = UNSET
    league: Union[Unset, "LeagueExternalIdsModelLeague"] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        league_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.league_external_id, Unset):
            league_external_id = str(self.league_external_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        league_id: Union[Unset, str] = UNSET
        if not isinstance(self.league_id, Unset):
            league_id = str(self.league_id)

        league: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

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
        if league_external_id is not UNSET:
            field_dict["leagueExternalId"] = league_external_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
        if league is not UNSET:
            field_dict["league"] = league
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
        from ..models.league_external_ids_model_league import LeagueExternalIdsModelLeague
        from ..models.league_external_ids_model_organization import LeagueExternalIdsModelOrganization

        d = dict(src_dict)
        _league_external_id = d.pop("leagueExternalId", UNSET)
        league_external_id: Union[Unset, UUID]
        if isinstance(_league_external_id, Unset):
            league_external_id = UNSET
        else:
            league_external_id = UUID(_league_external_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, LeagueExternalIdsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = LeagueExternalIdsModelOrganization.from_dict(_organization)

        _league_id = d.pop("leagueId", UNSET)
        league_id: Union[Unset, UUID]
        if isinstance(_league_id, Unset):
            league_id = UNSET
        else:
            league_id = UUID(_league_id)

        _league = d.pop("league", UNSET)
        league: Union[Unset, LeagueExternalIdsModelLeague]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = LeagueExternalIdsModelLeague.from_dict(_league)

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

        league_external_ids_model = cls(
            league_external_id=league_external_id,
            organization_id=organization_id,
            organization=organization,
            league_id=league_id,
            league=league,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            updated=updated,
            added=added,
        )

        return league_external_ids_model
