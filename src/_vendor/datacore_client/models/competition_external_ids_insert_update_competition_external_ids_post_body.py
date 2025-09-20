from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="CompetitionExternalIdsInsertUpdateCompetitionExternalIdsPostBody"
)


@_attrs_define
class CompetitionExternalIdsInsertUpdateCompetitionExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        competition_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    competition_external_id: Union[Unset, UUID] = UNSET
    competition_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        competition_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_external_id, Unset):
            competition_external_id = str(self.competition_external_id)

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if competition_external_id is not UNSET:
            field_dict["competitionExternalId"] = competition_external_id
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _competition_external_id = d.pop("competitionExternalId", UNSET)
        competition_external_id: Union[Unset, UUID]
        if isinstance(_competition_external_id, Unset):
            competition_external_id = UNSET
        else:
            competition_external_id = UUID(_competition_external_id)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        competition_external_ids_insert_update_competition_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            competition_external_id=competition_external_id,
            competition_id=competition_id,
        )

        return competition_external_ids_insert_update_competition_external_ids_post_body
