from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TeamExternalIdsPostBody")


@_attrs_define
class TeamExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        entity_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    entity_external_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        entity_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_external_id, Unset):
            entity_external_id = str(self.entity_external_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if entity_external_id is not UNSET:
            field_dict["entityExternalId"] = entity_external_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _entity_external_id = d.pop("entityExternalId", UNSET)
        entity_external_id: Union[Unset, UUID]
        if isinstance(_entity_external_id, Unset):
            entity_external_id = UNSET
        else:
            entity_external_id = UUID(_entity_external_id)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        team_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            entity_external_id=entity_external_id,
            entity_id=entity_id,
        )

        return team_external_ids_post_body
