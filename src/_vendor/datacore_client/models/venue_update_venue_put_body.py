from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.venue_update_venue_put_body_status import VenueUpdateVenuePutBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.venue_update_venue_put_body_social_media import (
        VenueUpdateVenuePutBodySocialMedia,
    )
    from ..models.venue_update_venue_put_body_venue_address import (
        VenueUpdateVenuePutBodyVenueAddress,
    )
    from ..models.venue_update_venue_put_body_venue_historical_name import (
        VenueUpdateVenuePutBodyVenueHistoricalName,
    )


T = TypeVar("T", bound="VenueUpdateVenuePutBody")


@_attrs_define
class VenueUpdateVenuePutBody:
    """
    Attributes:
        site_id (Union[None, UUID, Unset]): The site that this venue belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_local (Union[Unset, str]): The name of the venue in the [local](#section/Introduction/Character-Sets-and-
            Names) language Example: Test name local.
        status (Union[Unset, VenueUpdateVenuePutBodyStatus]): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Default: VenueUpdateVenuePutBodyStatus.ACTIVE. Example: ACTIVE.
        alternate_name_local (Union[None, Unset, str]): The alternate name of the venue, in Local Language Example: Test
            venue.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the venue in [latin](#section/Introduction/Character-Sets-and-
            Names) characters Example: Test name latin .
        alternate_name_latin (Union[None, Unset, str]): The alternate name of the venue, in Latin characters Example:
            Test venue.
        country_code (Union[None, Unset, str]): Country code of the venue. We recommend you use ISO-3166-1:alpha3 (upper
            case) values where available. Example: USA.
        timezone (Union[Unset, str]): Timezone of the venue.  The name of the zone as defined by the IANA TZ database.
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Example: Australia/Sydney.
        address (Union['VenueUpdateVenuePutBodyVenueAddress', None, Unset]): Street Address for the venue
        social (Union['VenueUpdateVenuePutBodySocialMedia', None, Unset]): Social Media contacts
        capacity (Union[None, Unset, int]): This is the maximum number of people allowed for the venue in normal use.
            Certain events/configurations of the venue may cause this capacity to be increased/decreased - this is not
            reflected in this value. Example: 12300.
        historical_names (Union[None, Unset, list['VenueUpdateVenuePutBodyVenueHistoricalName']]): Array of venue
            historical names
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    site_id: Union[None, UUID, Unset] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    name_local: Union[Unset, str] = UNSET
    status: Union[Unset, VenueUpdateVenuePutBodyStatus] = (
        VenueUpdateVenuePutBodyStatus.ACTIVE
    )
    alternate_name_local: Union[None, Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    alternate_name_latin: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    address: Union["VenueUpdateVenuePutBodyVenueAddress", None, Unset] = UNSET
    social: Union["VenueUpdateVenuePutBodySocialMedia", None, Unset] = UNSET
    capacity: Union[None, Unset, int] = UNSET
    historical_names: Union[
        None, Unset, list["VenueUpdateVenuePutBodyVenueHistoricalName"]
    ] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.venue_update_venue_put_body_social_media import (
            VenueUpdateVenuePutBodySocialMedia,
        )
        from ..models.venue_update_venue_put_body_venue_address import (
            VenueUpdateVenuePutBodyVenueAddress,
        )

        site_id: Union[None, Unset, str]
        if isinstance(self.site_id, Unset):
            site_id = UNSET
        elif isinstance(self.site_id, UUID):
            site_id = str(self.site_id)
        else:
            site_id = self.site_id

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        name_local = self.name_local

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        alternate_name_local: Union[None, Unset, str]
        if isinstance(self.alternate_name_local, Unset):
            alternate_name_local = UNSET
        else:
            alternate_name_local = self.alternate_name_local

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

        alternate_name_latin: Union[None, Unset, str]
        if isinstance(self.alternate_name_latin, Unset):
            alternate_name_latin = UNSET
        else:
            alternate_name_latin = self.alternate_name_latin

        country_code: Union[None, Unset, str]
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        timezone = self.timezone

        address: Union[None, Unset, dict[str, Any]]
        if isinstance(self.address, Unset):
            address = UNSET
        elif isinstance(self.address, VenueUpdateVenuePutBodyVenueAddress):
            address = self.address.to_dict()
        else:
            address = self.address

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, VenueUpdateVenuePutBodySocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        capacity: Union[None, Unset, int]
        if isinstance(self.capacity, Unset):
            capacity = UNSET
        else:
            capacity = self.capacity

        historical_names: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.historical_names, Unset):
            historical_names = UNSET
        elif isinstance(self.historical_names, list):
            historical_names = []
            for historical_names_type_0_item_data in self.historical_names:
                historical_names_type_0_item = (
                    historical_names_type_0_item_data.to_dict()
                )
                historical_names.append(historical_names_type_0_item)

        else:
            historical_names = self.historical_names

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if status is not UNSET:
            field_dict["status"] = status
        if alternate_name_local is not UNSET:
            field_dict["alternateNameLocal"] = alternate_name_local
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if alternate_name_latin is not UNSET:
            field_dict["alternateNameLatin"] = alternate_name_latin
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if address is not UNSET:
            field_dict["address"] = address
        if social is not UNSET:
            field_dict["social"] = social
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if historical_names is not UNSET:
            field_dict["historicalNames"] = historical_names
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.venue_update_venue_put_body_social_media import (
            VenueUpdateVenuePutBodySocialMedia,
        )
        from ..models.venue_update_venue_put_body_venue_address import (
            VenueUpdateVenuePutBodyVenueAddress,
        )
        from ..models.venue_update_venue_put_body_venue_historical_name import (
            VenueUpdateVenuePutBodyVenueHistoricalName,
        )

        d = dict(src_dict)

        def _parse_site_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                site_id_type_0 = UUID(data)

                return site_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        site_id = _parse_site_id(d.pop("siteId", UNSET))

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(
            d.pop("abbreviationLocal", UNSET)
        )

        name_local = d.pop("nameLocal", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, VenueUpdateVenuePutBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = VenueUpdateVenuePutBodyStatus(_status)

        def _parse_alternate_name_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alternate_name_local = _parse_alternate_name_local(
            d.pop("alternateNameLocal", UNSET)
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

        def _parse_alternate_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alternate_name_latin = _parse_alternate_name_latin(
            d.pop("alternateNameLatin", UNSET)
        )

        def _parse_country_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        country_code = _parse_country_code(d.pop("countryCode", UNSET))

        timezone = d.pop("timezone", UNSET)

        def _parse_address(
            data: object,
        ) -> Union["VenueUpdateVenuePutBodyVenueAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = VenueUpdateVenuePutBodyVenueAddress.from_dict(data)

                return address_type_0
            except:  # noqa: E722
                pass
            return cast(Union["VenueUpdateVenuePutBodyVenueAddress", None, Unset], data)

        address = _parse_address(d.pop("address", UNSET))

        def _parse_social(
            data: object,
        ) -> Union["VenueUpdateVenuePutBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = VenueUpdateVenuePutBodySocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(Union["VenueUpdateVenuePutBodySocialMedia", None, Unset], data)

        social = _parse_social(d.pop("social", UNSET))

        def _parse_capacity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        capacity = _parse_capacity(d.pop("capacity", UNSET))

        def _parse_historical_names(
            data: object,
        ) -> Union[None, Unset, list["VenueUpdateVenuePutBodyVenueHistoricalName"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                historical_names_type_0 = []
                _historical_names_type_0 = data
                for historical_names_type_0_item_data in _historical_names_type_0:
                    historical_names_type_0_item = (
                        VenueUpdateVenuePutBodyVenueHistoricalName.from_dict(
                            historical_names_type_0_item_data
                        )
                    )

                    historical_names_type_0.append(historical_names_type_0_item)

                return historical_names_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[None, Unset, list["VenueUpdateVenuePutBodyVenueHistoricalName"]],
                data,
            )

        historical_names = _parse_historical_names(d.pop("historicalNames", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        venue_update_venue_put_body = cls(
            site_id=site_id,
            abbreviation_local=abbreviation_local,
            name_local=name_local,
            status=status,
            alternate_name_local=alternate_name_local,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            alternate_name_latin=alternate_name_latin,
            country_code=country_code,
            timezone=timezone,
            address=address,
            social=social,
            capacity=capacity,
            historical_names=historical_names,
            external_id=external_id,
        )

        return venue_update_venue_put_body
