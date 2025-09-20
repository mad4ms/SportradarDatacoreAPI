import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_external_ids_model_competition import (
        CompetitionExternalIdsModelCompetition,
    )
    from ..models.competition_external_ids_model_organization import (
        CompetitionExternalIdsModelOrganization,
    )


T = TypeVar("T", bound="CompetitionExternalIdsModel")


@_attrs_define
class CompetitionExternalIdsModel:
    """
    Attributes:
        competition_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, CompetitionExternalIdsModelOrganization]): The organization that this competition
            external ids belongs to
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, CompetitionExternalIdsModelCompetition]): The competition that this season belongs to
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    competition_external_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "CompetitionExternalIdsModelOrganization"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "CompetitionExternalIdsModelCompetition"] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        competition_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_external_id, Unset):
            competition_external_id = str(self.competition_external_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        competition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

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
        if competition_external_id is not UNSET:
            field_dict["competitionExternalId"] = competition_external_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
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
        from ..models.competition_external_ids_model_competition import (
            CompetitionExternalIdsModelCompetition,
        )
        from ..models.competition_external_ids_model_organization import (
            CompetitionExternalIdsModelOrganization,
        )

        d = dict(src_dict)
        _competition_external_id = d.pop("competitionExternalId", UNSET)
        competition_external_id: Union[Unset, UUID]
        if isinstance(_competition_external_id, Unset):
            competition_external_id = UNSET
        else:
            competition_external_id = UUID(_competition_external_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, CompetitionExternalIdsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CompetitionExternalIdsModelOrganization.from_dict(
                _organization
            )

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, CompetitionExternalIdsModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = CompetitionExternalIdsModelCompetition.from_dict(_competition)

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

        competition_external_ids_model = cls(
            competition_external_id=competition_external_id,
            organization_id=organization_id,
            organization=organization,
            competition_id=competition_id,
            competition=competition,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            updated=updated,
            added=added,
        )

        return competition_external_ids_model
