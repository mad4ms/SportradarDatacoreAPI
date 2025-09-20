import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.organization_model_region_type import OrganizationModelRegionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images_model import ImagesModel


T = TypeVar("T", bound="OrganizationModel")


@_attrs_define
class OrganizationModel:
    """
    Attributes:
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: b1a23.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_local (Union[Unset, str]): The name of the organization in the [local](#section/Introduction/Character-
            Sets-and-Names) language Example: Test name local.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the organization in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test name latin .
        country_code (Union[None, Unset, str]): Country code of the organization. We recommend you use ISO-3166-1:alpha3
            (upper case) values where available. Example: USA.
        region_type (Union[Unset, OrganizationModelRegionType]): How geographically relevant is this organization
            >- `INTERNATIONAL` Multiple countries
            >- `INTERSTATE` Cross state
            >- `LOCAL` Local area
            >- `NATIONAL` One country
            >- `STATE` One state
             Example: STATE.
        default_locale (Union[Unset, str]): The locale of the video Example: fr-FR.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        images (Union[Unset, list['ImagesModel']]):
    """

    organization_id: Union[Unset, str] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    name_local: Union[Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    region_type: Union[Unset, OrganizationModelRegionType] = UNSET
    default_locale: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    images: Union[Unset, list["ImagesModel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        name_local = self.name_local

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

        region_type: Union[Unset, str] = UNSET
        if not isinstance(self.region_type, Unset):
            region_type = self.region_type.value

        default_locale = self.default_locale

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if region_type is not UNSET:
            field_dict["regionType"] = region_type
        if default_locale is not UNSET:
            field_dict["defaultLocale"] = default_locale
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.images_model import ImagesModel

        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(d.pop("abbreviationLocal", UNSET))

        name_local = d.pop("nameLocal", UNSET)

        def _parse_abbreviation_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_latin = _parse_abbreviation_latin(d.pop("abbreviationLatin", UNSET))

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

        _region_type = d.pop("regionType", UNSET)
        region_type: Union[Unset, OrganizationModelRegionType]
        if isinstance(_region_type, Unset):
            region_type = UNSET
        else:
            region_type = OrganizationModelRegionType(_region_type)

        default_locale = d.pop("defaultLocale", UNSET)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ImagesModel.from_dict(images_item_data)

            images.append(images_item)

        organization_model = cls(
            organization_id=organization_id,
            abbreviation_local=abbreviation_local,
            name_local=name_local,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            country_code=country_code,
            region_type=region_type,
            default_locale=default_locale,
            updated=updated,
            added=added,
            images=images,
        )

        return organization_model
