from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.site_insert_site_post_body_site_address import (
        SiteInsertSitePostBodySiteAddress,
    )
    from ..models.site_insert_site_post_body_social_media import (
        SiteInsertSitePostBodySocialMedia,
    )


T = TypeVar("T", bound="SiteInsertSitePostBody")


@_attrs_define
class SiteInsertSitePostBody:
    """
    Attributes:
        name_local (str): The name of the site in the [local](#section/Introduction/Character-Sets-and-Names) language
            Example: Test name local.
        site_id (Union[Unset, UUID]): The unique identifier of the site Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the site in [latin](#section/Introduction/Character-Sets-and-
            Names) characters Example: Test name latin .
        country_code (Union[None, Unset, str]): Country code of the site. We recommend you use ISO-3166-1:alpha3 (upper
            case) values where available. Example: USA.
        address (Union['SiteInsertSitePostBodySiteAddress', None, Unset]): Street Address for the site
        social (Union['SiteInsertSitePostBodySocialMedia', None, Unset]): Social Media contacts
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    name_local: str
    site_id: Union[Unset, UUID] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    address: Union["SiteInsertSitePostBodySiteAddress", None, Unset] = UNSET
    social: Union["SiteInsertSitePostBodySocialMedia", None, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.site_insert_site_post_body_site_address import (
            SiteInsertSitePostBodySiteAddress,
        )
        from ..models.site_insert_site_post_body_social_media import (
            SiteInsertSitePostBodySocialMedia,
        )

        name_local = self.name_local

        site_id: Union[Unset, str] = UNSET
        if not isinstance(self.site_id, Unset):
            site_id = str(self.site_id)

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        abbreviation_latin: Union[None, Unset, str]
        if isinstance(self.abbreviation_latin, Unset):
            abbreviation_latin = UNSET
        else:
            abbreviation_latin = self.abbreviation_latin

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        country_code: Union[None, Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, SiteInsertSitePostBodySiteAddress):
            address = self.address.to_dict()
        else:
            address = self.address

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, SiteInsertSitePostBodySocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "nameLocal": name_local,
            }
        )
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if address is not UNSET:
            field_dict["address"] = address
        if social is not UNSET:
            field_dict["social"] = social
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_insert_site_post_body_site_address import (
            SiteInsertSitePostBodySiteAddress,
        )
        from ..models.site_insert_site_post_body_social_media import (
            SiteInsertSitePostBodySocialMedia,
        )

        d = dict(src_dict)
        name_local = d.pop("nameLocal")

        _site_id = d.pop("siteId", UNSET)
        site_id: Union[Unset, UUID]
        if isinstance(_site_id, Unset):
            site_id = UNSET
        else:
            site_id = UUID(_site_id)

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(
            d.pop("abbreviationLocal", UNSET)
        )

        def _parse_abbreviation_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_latin = _parse_abbreviation_latin(
            d.pop("abbreviationLatin", UNSET)
        )

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_address(
            data: object,
        ) -> Union["SiteInsertSitePostBodySiteAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = SiteInsertSitePostBodySiteAddress.from_dict(data)

                return address_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SiteInsertSitePostBodySiteAddress", None, Unset], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_social(
            data: object,
        ) -> Union["SiteInsertSitePostBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = SiteInsertSitePostBodySocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SiteInsertSitePostBodySocialMedia", None, Unset], data)

        social = _parse_social(d.pop("social", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        site_insert_site_post_body = cls(
            name_local=name_local,
            site_id=site_id,
            abbreviation_local=abbreviation_local,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            country_code=country_code,
            address=address,
            social=social,
            external_id=external_id,
        )

        return site_insert_site_post_body
