from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConferenceExternalIdsPutBody")


@_attrs_define
class ConferenceExternalIdsPutBody:
    """
    Attributes:
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
    """

    conference_id: Union[None, UUID, Unset] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
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

        source = d.pop("source", UNSET)

        source_type = d.pop("sourceType", UNSET)

        source_external_id = d.pop("sourceExternalId", UNSET)

        conference_external_ids_put_body = cls(
            conference_id=conference_id,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
        )

        return conference_external_ids_put_body
