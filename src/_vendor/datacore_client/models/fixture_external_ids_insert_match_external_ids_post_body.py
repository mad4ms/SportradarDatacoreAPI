from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FixtureExternalIdsInsertMatchExternalIdsPostBody")


@_attrs_define
class FixtureExternalIdsInsertMatchExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        fixture_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    fixture_external_id: Union[Unset, UUID] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        fixture_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_external_id, Unset):
            fixture_external_id = str(self.fixture_external_id)

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if fixture_external_id is not UNSET:
            field_dict["fixtureExternalId"] = fixture_external_id
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _fixture_external_id = d.pop("fixtureExternalId", UNSET)
        fixture_external_id: Union[Unset, UUID]
        if isinstance(_fixture_external_id, Unset):
            fixture_external_id = UNSET
        else:
            fixture_external_id = UUID(_fixture_external_id)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        fixture_external_ids_insert_match_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            fixture_external_id=fixture_external_id,
            fixture_id=fixture_id,
        )

        return fixture_external_ids_insert_match_external_ids_post_body
