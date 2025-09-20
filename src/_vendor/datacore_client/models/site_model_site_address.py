from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteModelSiteAddress")


@_attrs_define
class SiteModelSiteAddress:
    """Street Address for the site

    Attributes:
        address1 (Union[None, Unset, str]): First line of the address
        address2 (Union[None, Unset, str]): Second line of the address
        address3 (Union[None, Unset, str]): Third line of the address
        city (Union[None, Unset, str]): The city/suburb of the address
        state (Union[None, Unset, str]): The state of the address
        postal_code (Union[None, Unset, str]): The postal code for the address
        country_code (Union[None, Unset, str]): ISO Country code of the address.  We recommend you use ISO-3166-1:alpha3
            (upper case) values where available.
        longitude (Union[None, Unset, float]):
        latitude (Union[None, Unset, float]):
    """

    address1: Union[None, Unset, str] = UNSET
    address2: Union[None, Unset, str] = UNSET
    address3: Union[None, Unset, str] = UNSET
    city: Union[None, Unset, str] = UNSET
    state: Union[None, Unset, str] = UNSET
    postal_code: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    latitude: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        address1: Union[None, Unset, str]
        if isinstance(self.address1, Unset):
            address1 = UNSET
        else:
            address1 = self.address1

        address2: Union[None, Unset, str]
        if isinstance(self.address2, Unset):
            address2 = UNSET
        else:
            address2 = self.address2

        address3: Union[None, Unset, str]
        if isinstance(self.address3, Unset):
            address3 = UNSET
        else:
            address3 = self.address3

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state: Union[None, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        else:
            state = self.state

        postal_code: Union[None, Unset, str]
        if isinstance(self.postal_code, Unset):
            postal_code = UNSET
        else:
            postal_code = self.postal_code

        country_code: Union[None, Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if address3 is not UNSET:
            field_dict["address3"] = address3
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if latitude is not UNSET:
            field_dict["latitude"] = latitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_address1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address1 = _parse_address1(d.pop("address1", UNSET))

        def _parse_address2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address2 = _parse_address2(d.pop("address2", UNSET))

        def _parse_address3(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address3 = _parse_address3(d.pop("address3", UNSET))

        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))

        def _parse_state(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        state = _parse_state(d.pop("state", UNSET))

        def _parse_postal_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postal_code = _parse_postal_code(d.pop("postalCode", UNSET))

        def _parse_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        site_model_site_address = cls(
            address1=address1,
            address2=address2,
            address3=address3,
            city=city,
            state=state,
            postal_code=postal_code,
            country_code=country_code,
            longitude=longitude,
            latitude=latitude,
        )

        return site_model_site_address
