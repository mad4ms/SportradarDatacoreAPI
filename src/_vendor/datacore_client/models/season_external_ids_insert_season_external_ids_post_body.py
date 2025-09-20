from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonExternalIdsInsertSeasonExternalIdsPostBody")


@_attrs_define
class SeasonExternalIdsInsertSeasonExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        season_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    season_external_id: Union[Unset, UUID] = UNSET
    season_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        season_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_external_id, Unset):
            season_external_id = str(self.season_external_id)

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if season_external_id is not UNSET:
            field_dict["seasonExternalId"] = season_external_id
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _season_external_id = d.pop("seasonExternalId", UNSET)
        season_external_id: Union[Unset, UUID]
        if isinstance(_season_external_id, Unset):
            season_external_id = UNSET
        else:
            season_external_id = UUID(_season_external_id)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        season_external_ids_insert_season_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            season_external_id=season_external_id,
            season_id=season_id,
        )

        return season_external_ids_insert_season_external_ids_post_body
