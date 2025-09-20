import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_venues_model_organization import SeasonVenuesModelOrganization
    from ..models.season_venues_model_season import SeasonVenuesModelSeason
    from ..models.season_venues_model_season_venues_address import (
        SeasonVenuesModelSeasonVenuesAddress,
    )
    from ..models.season_venues_model_site import SeasonVenuesModelSite
    from ..models.season_venues_model_social_media import SeasonVenuesModelSocialMedia


T = TypeVar("T", bound="SeasonVenuesModel")


@_attrs_define
class SeasonVenuesModel:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonVenuesModelSeason]): The season linked to this record
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonVenuesModelOrganization]): The organization that this season venues belongs to
        venue_id (Union[Unset, UUID]): The unique identifier of the venue Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        site_id (Union[None, UUID, Unset]): The site that this season venues belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        site (Union[Unset, SeasonVenuesModelSite]): The site that this season venues belongs to
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_local (Union[Unset, str]): The name of the season venues in the [local](#section/Introduction/Character-
            Sets-and-Names) language Example: Test name local.
        alternate_name_local (Union[None, Unset, str]): The alternate name of the venue, in Local Language Example: Test
            venue.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the season venues in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test name latin .
        alternate_name_latin (Union[None, Unset, str]): The alternate name of the venue, in Latin characters Example:
            Test venue.
        country_code (Union[None, Unset, str]): Country code of the season venues. We recommend you use
            ISO-3166-1:alpha3 (upper case) values where available. Example: USA.
        timezone (Union[Unset, str]): Timezone of the venue.  The name of the zone as defined by the IANA TZ database.
            https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Example: Australia/Sydney.
        address (Union['SeasonVenuesModelSeasonVenuesAddress', None, Unset]): Street Address for the season venues
        social (Union['SeasonVenuesModelSocialMedia', None, Unset]): Social Media contacts
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonVenuesModelSeason"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonVenuesModelOrganization"] = UNSET
    venue_id: Union[Unset, UUID] = UNSET
    site_id: Union[None, UUID, Unset] = UNSET
    site: Union[Unset, "SeasonVenuesModelSite"] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    name_local: Union[Unset, str] = UNSET
    alternate_name_local: Union[None, Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    alternate_name_latin: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    timezone: Union[Unset, str] = UNSET
    address: Union["SeasonVenuesModelSeasonVenuesAddress", None, Unset] = UNSET
    social: Union["SeasonVenuesModelSocialMedia", None, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.season_venues_model_season_venues_address import (
            SeasonVenuesModelSeasonVenuesAddress,
        )
        from ..models.season_venues_model_social_media import (
            SeasonVenuesModelSocialMedia,
        )

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        venue_id: Union[Unset, str] = UNSET
        if not isinstance(self.venue_id, Unset):
            venue_id = str(self.venue_id)

        site_id: Union[None, Unset, str]
        if isinstance(self.site_id, Unset):
            site_id = UNSET
        elif isinstance(self.site_id, UUID):
            site_id = str(self.site_id)
        else:
            site_id = self.site_id

        site: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.site, Unset):
            site = self.site.to_dict()

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        name_local = self.name_local

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
        elif isinstance(self.address, SeasonVenuesModelSeasonVenuesAddress):
            address = self.address.to_dict()
        else:
            address = self.address

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, SeasonVenuesModelSocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id
        if site_id is not UNSET:
            field_dict["siteId"] = site_id
        if site is not UNSET:
            field_dict["site"] = site
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
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
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_venues_model_organization import (
            SeasonVenuesModelOrganization,
        )
        from ..models.season_venues_model_season import SeasonVenuesModelSeason
        from ..models.season_venues_model_season_venues_address import (
            SeasonVenuesModelSeasonVenuesAddress,
        )
        from ..models.season_venues_model_site import SeasonVenuesModelSite
        from ..models.season_venues_model_social_media import (
            SeasonVenuesModelSocialMedia,
        )

        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonVenuesModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonVenuesModelSeason.from_dict(_season)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonVenuesModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonVenuesModelOrganization.from_dict(_organization)

        _venue_id = d.pop("venueId", UNSET)
        venue_id: Union[Unset, UUID]
        if isinstance(_venue_id, Unset):
            venue_id = UNSET
        else:
            venue_id = UUID(_venue_id)

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

        _site = d.pop("site", UNSET)
        site: Union[Unset, SeasonVenuesModelSite]
        if isinstance(_site, Unset):
            site = UNSET
        else:
            site = SeasonVenuesModelSite.from_dict(_site)

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
        ) -> Union["SeasonVenuesModelSeasonVenuesAddress", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                address_type_0 = SeasonVenuesModelSeasonVenuesAddress.from_dict(data)

                return address_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["SeasonVenuesModelSeasonVenuesAddress", None, Unset], data
            )

        address = _parse_address(d.pop("address", UNSET))

        def _parse_social(
            data: object,
        ) -> Union["SeasonVenuesModelSocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = SeasonVenuesModelSocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(Union["SeasonVenuesModelSocialMedia", None, Unset], data)

        social = _parse_social(d.pop("social", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        season_venues_model = cls(
            season_id=season_id,
            season=season,
            organization_id=organization_id,
            organization=organization,
            venue_id=venue_id,
            site_id=site_id,
            site=site,
            abbreviation_local=abbreviation_local,
            name_local=name_local,
            alternate_name_local=alternate_name_local,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            alternate_name_latin=alternate_name_latin,
            country_code=country_code,
            timezone=timezone,
            address=address,
            social=social,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return season_venues_model
