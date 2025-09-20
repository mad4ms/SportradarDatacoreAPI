import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.transfer_model_status_type_1 import TransferModelStatusType1
from ..models.transfer_model_status_type_2_type_1 import TransferModelStatusType2Type1
from ..models.transfer_model_status_type_3_type_1 import TransferModelStatusType3Type1
from ..models.transfer_model_transfer_type import TransferModelTransferType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfer_model_competition import TransferModelCompetition
    from ..models.transfer_model_organization import TransferModelOrganization
    from ..models.transfer_model_season import TransferModelSeason
    from ..models.transfer_model_transfer_component import TransferModelTransferComponent


T = TypeVar("T", bound="TransferModel")


@_attrs_define
class TransferModel:
    """
    Attributes:
        transfer_id (Union[Unset, UUID]): The unique identifier of the transfer Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, TransferModelOrganization]): The organization that this ~transfer~ belongs to
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, TransferModelCompetition]): The competition that this season belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, TransferModelSeason]): The season linked to this record
        components (Union[None, Unset, list['TransferModelTransferComponent']]): List of transfer components
        status (Union[None, TransferModelStatusType1, TransferModelStatusType2Type1, TransferModelStatusType3Type1,
            Unset]): Transfer Status
            >- None None
            >- `APPROVED` Approved
            >- `DECLINED` Decline
            >- `PENDING` Pending
             Example: APPROVED.
        reference (Union[Unset, str]): Transfer reference number
        transfer_type (Union[Unset, TransferModelTransferType]): Type of transfer
            >- `DROPPED` Dropped
            >- `OTHER` Other
            >- `PERMIT` Permit
            >- `TRADE` Trade
            >- `TRANSFER` Transfer
             Example: TRANSFER.
        date_transfer (Union[None, Unset, datetime.date]): Date of transfer Example: 1978-08-24.
        date_permit_from (Union[None, Unset, datetime.date]): Date the permit started Example: 1978-08-24.
        date_permit_to (Union[None, Unset, datetime.date]): Date the permit ended Example: 1978-08-24.
        notes (Union[None, Unset, str]): Notes
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    transfer_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "TransferModelOrganization"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "TransferModelCompetition"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "TransferModelSeason"] = UNSET
    components: Union[None, Unset, list["TransferModelTransferComponent"]] = UNSET
    status: Union[
        None, TransferModelStatusType1, TransferModelStatusType2Type1, TransferModelStatusType3Type1, Unset
    ] = UNSET
    reference: Union[Unset, str] = UNSET
    transfer_type: Union[Unset, TransferModelTransferType] = UNSET
    date_transfer: Union[None, Unset, datetime.date] = UNSET
    date_permit_from: Union[None, Unset, datetime.date] = UNSET
    date_permit_to: Union[None, Unset, datetime.date] = UNSET
    notes: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        transfer_id: Union[Unset, str] = UNSET
        if not isinstance(self.transfer_id, Unset):
            transfer_id = str(self.transfer_id)

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

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        components: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.components, Unset):
            components = UNSET
        elif isinstance(self.components, list):
            components = []
            for components_type_0_item_data in self.components:
                components_type_0_item = components_type_0_item_data.to_dict()
                components.append(components_type_0_item)

        else:
            components = self.components

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, TransferModelStatusType1):
            status = self.status.value
        elif isinstance(self.status, TransferModelStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, TransferModelStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        reference = self.reference

        transfer_type: Union[Unset, str] = UNSET
        if not isinstance(self.transfer_type, Unset):
            transfer_type = self.transfer_type.value

        date_transfer: Union[None, Unset, str]
        if isinstance(self.date_transfer, Unset):
            date_transfer = UNSET
        elif isinstance(self.date_transfer, datetime.date):
            date_transfer = self.date_transfer.isoformat()
        else:
            date_transfer = self.date_transfer

        date_permit_from: Union[None, Unset, str]
        if isinstance(self.date_permit_from, Unset):
            date_permit_from = UNSET
        elif isinstance(self.date_permit_from, datetime.date):
            date_permit_from = self.date_permit_from.isoformat()
        else:
            date_permit_from = self.date_permit_from

        date_permit_to: Union[None, Unset, str]
        if isinstance(self.date_permit_to, Unset):
            date_permit_to = UNSET
        elif isinstance(self.date_permit_to, datetime.date):
            date_permit_to = self.date_permit_to.isoformat()
        else:
            date_permit_to = self.date_permit_to

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

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
        if transfer_id is not UNSET:
            field_dict["transferId"] = transfer_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if components is not UNSET:
            field_dict["components"] = components
        if status is not UNSET:
            field_dict["status"] = status
        if reference is not UNSET:
            field_dict["reference"] = reference
        if transfer_type is not UNSET:
            field_dict["transferType"] = transfer_type
        if date_transfer is not UNSET:
            field_dict["dateTransfer"] = date_transfer
        if date_permit_from is not UNSET:
            field_dict["datePermitFrom"] = date_permit_from
        if date_permit_to is not UNSET:
            field_dict["datePermitTo"] = date_permit_to
        if notes is not UNSET:
            field_dict["notes"] = notes
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_model_competition import TransferModelCompetition
        from ..models.transfer_model_organization import TransferModelOrganization
        from ..models.transfer_model_season import TransferModelSeason
        from ..models.transfer_model_transfer_component import TransferModelTransferComponent

        d = dict(src_dict)
        _transfer_id = d.pop("transferId", UNSET)
        transfer_id: Union[Unset, UUID]
        if isinstance(_transfer_id, Unset):
            transfer_id = UNSET
        else:
            transfer_id = UUID(_transfer_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, TransferModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = TransferModelOrganization.from_dict(_organization)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, TransferModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = TransferModelCompetition.from_dict(_competition)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, TransferModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = TransferModelSeason.from_dict(_season)

        def _parse_components(data: object) -> Union[None, Unset, list["TransferModelTransferComponent"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                components_type_0 = []
                _components_type_0 = data
                for components_type_0_item_data in _components_type_0:
                    components_type_0_item = TransferModelTransferComponent.from_dict(components_type_0_item_data)

                    components_type_0.append(components_type_0_item)

                return components_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["TransferModelTransferComponent"]], data)

        components = _parse_components(d.pop("components", UNSET))

        def _parse_status(
            data: object,
        ) -> Union[None, TransferModelStatusType1, TransferModelStatusType2Type1, TransferModelStatusType3Type1, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = TransferModelStatusType1(data)

                return status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = TransferModelStatusType2Type1(data)

                return status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = TransferModelStatusType3Type1(data)

                return status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None, TransferModelStatusType1, TransferModelStatusType2Type1, TransferModelStatusType3Type1, Unset
                ],
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        reference = d.pop("reference", UNSET)

        _transfer_type = d.pop("transferType", UNSET)
        transfer_type: Union[Unset, TransferModelTransferType]
        if isinstance(_transfer_type, Unset):
            transfer_type = UNSET
        else:
            transfer_type = TransferModelTransferType(_transfer_type)

        def _parse_date_transfer(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_transfer_type_0 = isoparse(data).date()

                return date_transfer_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_transfer = _parse_date_transfer(d.pop("dateTransfer", UNSET))

        def _parse_date_permit_from(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_permit_from_type_0 = isoparse(data).date()

                return date_permit_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_permit_from = _parse_date_permit_from(d.pop("datePermitFrom", UNSET))

        def _parse_date_permit_to(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_permit_to_type_0 = isoparse(data).date()

                return date_permit_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_permit_to = _parse_date_permit_to(d.pop("datePermitTo", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

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

        transfer_model = cls(
            transfer_id=transfer_id,
            organization_id=organization_id,
            organization=organization,
            competition_id=competition_id,
            competition=competition,
            season_id=season_id,
            season=season,
            components=components,
            status=status,
            reference=reference,
            transfer_type=transfer_type,
            date_transfer=date_transfer,
            date_permit_from=date_permit_from,
            date_permit_to=date_permit_to,
            notes=notes,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return transfer_model
