from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchExternalIdsPutBody")


@_attrs_define
class MatchExternalIdsPutBody:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
    """

    fixture_id: Union[Unset, UUID] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
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
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        source = d.pop("source", UNSET)

        source_type = d.pop("sourceType", UNSET)

        source_external_id = d.pop("sourceExternalId", UNSET)

        match_external_ids_put_body = cls(
            fixture_id=fixture_id,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
        )

        return match_external_ids_put_body
