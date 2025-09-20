import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.transfers_insert_transfer_post_body_status_type_1 import (
    TransfersInsertTransferPostBodyStatusType1,
)
from ..models.transfers_insert_transfer_post_body_status_type_2_type_1 import (
    TransfersInsertTransferPostBodyStatusType2Type1,
)
from ..models.transfers_insert_transfer_post_body_status_type_3_type_1 import (
    TransfersInsertTransferPostBodyStatusType3Type1,
)
from ..models.transfers_insert_transfer_post_body_transfer_type import (
    TransfersInsertTransferPostBodyTransferType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transfers_insert_transfer_post_body_transfer_component import (
        TransfersInsertTransferPostBodyTransferComponent,
    )


T = TypeVar("T", bound="TransfersInsertTransferPostBody")


@_attrs_define
class TransfersInsertTransferPostBody:
    """
    Attributes:
        transfer_type (TransfersInsertTransferPostBodyTransferType): Type of transfer
            >- `DROPPED` Dropped
            >- `OTHER` Other
            >- `PERMIT` Permit
            >- `TRADE` Trade
            >- `TRANSFER` Transfer
             Example: TRANSFER.
        transfer_id (Union[Unset, UUID]): The unique identifier of the transfer Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        components (Union[None, Unset, list['TransfersInsertTransferPostBodyTransferComponent']]): List of transfer
            components
        status (Union[None, TransfersInsertTransferPostBodyStatusType1, TransfersInsertTransferPostBodyStatusType2Type1,
            TransfersInsertTransferPostBodyStatusType3Type1, Unset]): Transfer Status
            >- None None
            >- `APPROVED` Approved
            >- `DECLINED` Decline
            >- `PENDING` Pending
             Example: APPROVED.
        reference (Union[Unset, str]): Transfer reference number
        date_transfer (Union[None, Unset, datetime.date]): Date of transfer Example: 1978-08-24.
        date_permit_from (Union[None, Unset, datetime.date]): Date the permit started Example: 1978-08-24.
        date_permit_to (Union[None, Unset, datetime.date]): Date the permit ended Example: 1978-08-24.
        notes (Union[None, Unset, str]): Notes
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    transfer_type: TransfersInsertTransferPostBodyTransferType
    transfer_id: Union[Unset, UUID] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    components: Union[
        None, Unset, list["TransfersInsertTransferPostBodyTransferComponent"]
    ] = UNSET
    status: Union[
        None,
        TransfersInsertTransferPostBodyStatusType1,
        TransfersInsertTransferPostBodyStatusType2Type1,
        TransfersInsertTransferPostBodyStatusType3Type1,
        Unset,
    ] = UNSET
    reference: Union[Unset, str] = UNSET
    date_transfer: Union[None, Unset, datetime.date] = UNSET
    date_permit_from: Union[None, Unset, datetime.date] = UNSET
    date_permit_to: Union[None, Unset, datetime.date] = UNSET
    notes: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        transfer_type = self.transfer_type.value

        transfer_id: Union[Unset, str] = UNSET
        if not isinstance(self.transfer_id, Unset):
            transfer_id = str(self.transfer_id)

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

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
        elif isinstance(self.status, TransfersInsertTransferPostBodyStatusType1):
            status = self.status.value
        elif isinstance(self.status, TransfersInsertTransferPostBodyStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, TransfersInsertTransferPostBodyStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        reference = self.reference

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "transferType": transfer_type,
            }
        )
        if transfer_id is not UNSET:
            field_dict["transferId"] = transfer_id
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if components is not UNSET:
            field_dict["components"] = components
        if status is not UNSET:
            field_dict["status"] = status
        if reference is not UNSET:
            field_dict["reference"] = reference
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfers_insert_transfer_post_body_transfer_component import (
            TransfersInsertTransferPostBodyTransferComponent,
        )

        d = dict(src_dict)
        transfer_type = TransfersInsertTransferPostBodyTransferType(
            d.pop("transferType")
        )

        _transfer_id = d.pop("transferId", UNSET)
        transfer_id: Union[Unset, UUID]
        if isinstance(_transfer_id, Unset):
            transfer_id = UNSET
        else:
            transfer_id = UUID(_transfer_id)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        def _parse_components(
            data: object,
        ) -> Union[
            None, Unset, list["TransfersInsertTransferPostBodyTransferComponent"]
        ]:
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
                    components_type_0_item = (
                        TransfersInsertTransferPostBodyTransferComponent.from_dict(
                            components_type_0_item_data
                        )
                    )

                    components_type_0.append(components_type_0_item)

                return components_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    list["TransfersInsertTransferPostBodyTransferComponent"],
                ],
                data,
            )

        components = _parse_components(d.pop("components", UNSET))

        def _parse_status(
            data: object,
        ) -> Union[
            None,
            TransfersInsertTransferPostBodyStatusType1,
            TransfersInsertTransferPostBodyStatusType2Type1,
            TransfersInsertTransferPostBodyStatusType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = TransfersInsertTransferPostBodyStatusType1(data)

                return status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = TransfersInsertTransferPostBodyStatusType2Type1(
                    data
                )

                return status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = TransfersInsertTransferPostBodyStatusType3Type1(
                    data
                )

                return status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    TransfersInsertTransferPostBodyStatusType1,
                    TransfersInsertTransferPostBodyStatusType2Type1,
                    TransfersInsertTransferPostBodyStatusType3Type1,
                    Unset,
                ],
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        reference = d.pop("reference", UNSET)

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

        transfers_insert_transfer_post_body = cls(
            transfer_type=transfer_type,
            transfer_id=transfer_id,
            competition_id=competition_id,
            season_id=season_id,
            components=components,
            status=status,
            reference=reference,
            date_transfer=date_transfer,
            date_permit_from=date_permit_from,
            date_permit_to=date_permit_to,
            notes=notes,
            external_id=external_id,
        )

        return transfers_insert_transfer_post_body
