import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.division_external_ids_model_division import (
        DivisionExternalIdsModelDivision,
    )
    from ..models.division_external_ids_model_organization import (
        DivisionExternalIdsModelOrganization,
    )


T = TypeVar("T", bound="DivisionExternalIdsModel")


@_attrs_define
class DivisionExternalIdsModel:
    """
    Attributes:
        division_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, DivisionExternalIdsModelOrganization]): The organization that this division external
            ids belongs to
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division (Union[Unset, DivisionExternalIdsModelDivision]): The division information
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    division_external_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "DivisionExternalIdsModelOrganization"] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    division: Union[Unset, "DivisionExternalIdsModelDivision"] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        division_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.division_external_id, Unset):
            division_external_id = str(self.division_external_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

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
        if division_external_id is not UNSET:
            field_dict["divisionExternalId"] = division_external_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if division is not UNSET:
            field_dict["division"] = division
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
        from ..models.division_external_ids_model_division import (
            DivisionExternalIdsModelDivision,
        )
        from ..models.division_external_ids_model_organization import (
            DivisionExternalIdsModelOrganization,
        )

        d = dict(src_dict)
        _division_external_id = d.pop("divisionExternalId", UNSET)
        division_external_id: Union[Unset, UUID]
        if isinstance(_division_external_id, Unset):
            division_external_id = UNSET
        else:
            division_external_id = UUID(_division_external_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, DivisionExternalIdsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = DivisionExternalIdsModelOrganization.from_dict(_organization)

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
        division: Union[Unset, DivisionExternalIdsModelDivision]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = DivisionExternalIdsModelDivision.from_dict(_division)

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

        division_external_ids_model = cls(
            division_external_id=division_external_id,
            organization_id=organization_id,
            organization=organization,
            division_id=division_id,
            division=division,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            updated=updated,
            added=added,
        )

        return division_external_ids_model
