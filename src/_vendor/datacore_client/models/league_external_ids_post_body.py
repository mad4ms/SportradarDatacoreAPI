from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeagueExternalIdsPostBody")


@_attrs_define
class LeagueExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        league_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        league_id (Union[Unset, UUID]): The unique identifier of the league Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    league_external_id: Union[Unset, UUID] = UNSET
    league_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        league_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.league_external_id, Unset):
            league_external_id = str(self.league_external_id)

        league_id: Union[Unset, str] = UNSET
        if not isinstance(self.league_id, Unset):
            league_id = str(self.league_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if league_external_id is not UNSET:
            field_dict["leagueExternalId"] = league_external_id
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _league_external_id = d.pop("leagueExternalId", UNSET)
        league_external_id: Union[Unset, UUID]
        if isinstance(_league_external_id, Unset):
            league_external_id = UNSET
        else:
            league_external_id = UUID(_league_external_id)

        _league_id = d.pop("leagueId", UNSET)
        league_id: Union[Unset, UUID]
        if isinstance(_league_id, Unset):
            league_id = UNSET
        else:
            league_id = UUID(_league_id)

        league_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            league_external_id=league_external_id,
            league_id=league_id,
        )

        return league_external_ids_post_body
