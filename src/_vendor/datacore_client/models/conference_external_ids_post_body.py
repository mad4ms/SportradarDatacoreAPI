from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConferenceExternalIdsPostBody")


@_attrs_define
class ConferenceExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        conference_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    conference_external_id: Union[Unset, UUID] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        conference_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.conference_external_id, Unset):
            conference_external_id = str(self.conference_external_id)

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if conference_external_id is not UNSET:
            field_dict["conferenceExternalId"] = conference_external_id
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _conference_external_id = d.pop("conferenceExternalId", UNSET)
        conference_external_id: Union[Unset, UUID]
        if isinstance(_conference_external_id, Unset):
            conference_external_id = UNSET
        else:
            conference_external_id = UUID(_conference_external_id)

        def _parse_conference_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conference_id_type_0 = UUID(data)

                return conference_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        conference_id = _parse_conference_id(d.pop("conferenceId", UNSET))

        conference_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            conference_external_id=conference_external_id,
            conference_id=conference_id,
        )

        return conference_external_ids_post_body
