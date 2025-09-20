from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DivisionExternalIdsPutBody")


@_attrs_define
class DivisionExternalIdsPutBody:
    """
    Attributes:
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
    """

    division_id: Union[None, UUID, Unset] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if source is not UNSET:
            field_dict["source"] = source
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if source_external_id is not UNSET:
            field_dict["sourceExternalId"] = source_external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        source = d.pop("source", UNSET)

        source_type = d.pop("sourceType", UNSET)

        source_external_id = d.pop("sourceExternalId", UNSET)

        division_external_ids_put_body = cls(
            division_id=division_id,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
        )

        return division_external_ids_put_body
