from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DivisionExternalIdsInsertDivisionExternalIdsPostBody")


@_attrs_define
class DivisionExternalIdsInsertDivisionExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        division_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    division_external_id: Union[Unset, UUID] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        division_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.division_external_id, Unset):
            division_external_id = str(self.division_external_id)

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if division_external_id is not UNSET:
            field_dict["divisionExternalId"] = division_external_id
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _division_external_id = d.pop("divisionExternalId", UNSET)
        division_external_id: Union[Unset, UUID]
        if isinstance(_division_external_id, Unset):
            division_external_id = UNSET
        else:
            division_external_id = UUID(_division_external_id)

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

        division_external_ids_insert_division_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            division_external_id=division_external_id,
            division_id=division_id,
        )

        return division_external_ids_insert_division_external_ids_post_body
