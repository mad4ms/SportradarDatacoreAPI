from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteExternalIdsPutBody")


@_attrs_define
class SiteExternalIdsPutBody:
    """
    Attributes:
        site_id (Union[Unset, UUID]): The site that this site external ids belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source (Union[Unset, str]): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (Union[Unset, str]): Source type of external Id
        source_external_id (Union[Unset, str]): Identifier of external source Example: SR:123.
    """

    site_id: Union[Unset, UUID] = UNSET
    source: Union[Unset, str] = UNSET
    source_type: Union[Unset, str] = UNSET
    source_external_id: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        site_id: Union[Unset, str] = UNSET
        if not isinstance(self.site_id, Unset):
            site_id = str(self.site_id)

        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
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
        _site_id = d.pop("siteId", UNSET)
        site_id: Union[Unset, UUID]
        if isinstance(_site_id, Unset):
            site_id = UNSET
        else:
            site_id = UUID(_site_id)

        source = d.pop("source", UNSET)

        source_type = d.pop("sourceType", UNSET)

        source_external_id = d.pop("sourceExternalId", UNSET)

        site_external_ids_put_body = cls(
            site_id=site_id,
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
        )

        return site_external_ids_put_body
