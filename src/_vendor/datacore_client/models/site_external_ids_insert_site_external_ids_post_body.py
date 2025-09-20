from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteExternalIdsInsertSiteExternalIdsPostBody")


@_attrs_define
class SiteExternalIdsInsertSiteExternalIdsPostBody:
    """
    Attributes:
        source (str): The source of the external Id Example: urn:sources:sportradar.com.
        source_type (str): Source type of external Id
        source_external_id (str): Identifier of external source Example: SR:123.
        site_external_id (Union[Unset, UUID]): The unique identifier of the external ids Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        site_id (Union[Unset, UUID]): The site that this site external ids belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    source: str
    source_type: str
    source_external_id: str
    site_external_id: Union[Unset, UUID] = UNSET
    site_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        source_type = self.source_type

        source_external_id = self.source_external_id

        site_external_id: Union[Unset, str] = UNSET
        if not isinstance(self.site_external_id, Unset):
            site_external_id = str(self.site_external_id)

        site_id: Union[Unset, str] = UNSET
        if not isinstance(self.site_id, Unset):
            site_id = str(self.site_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "source": source,
                "sourceType": source_type,
                "sourceExternalId": source_external_id,
            }
        )
        if site_external_id is not UNSET:
            field_dict["siteExternalId"] = site_external_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source")

        source_type = d.pop("sourceType")

        source_external_id = d.pop("sourceExternalId")

        _site_external_id = d.pop("siteExternalId", UNSET)
        site_external_id: Union[Unset, UUID]
        if isinstance(_site_external_id, Unset):
            site_external_id = UNSET
        else:
            site_external_id = UUID(_site_external_id)

        _site_id = d.pop("siteId", UNSET)
        site_id: Union[Unset, UUID]
        if isinstance(_site_id, Unset):
            site_id = UNSET
        else:
            site_id = UUID(_site_id)

        site_external_ids_insert_site_external_ids_post_body = cls(
            source=source,
            source_type=source_type,
            source_external_id=source_external_id,
            site_external_id=site_external_id,
            site_id=site_id,
        )

        return site_external_ids_insert_site_external_ids_post_body
