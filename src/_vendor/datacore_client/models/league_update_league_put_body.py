from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.league_update_league_put_body_region_type import (
    LeagueUpdateLeaguePutBodyRegionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.league_update_league_put_body_social_media import (
        LeagueUpdateLeaguePutBodySocialMedia,
    )


T = TypeVar("T", bound="LeagueUpdateLeaguePutBody")


@_attrs_define
class LeagueUpdateLeaguePutBody:
    """
    Attributes:
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_local (Union[Unset, str]): The name of the league in the [local](#section/Introduction/Character-Sets-and-
            Names) language Example: Test name local.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the league in [latin](#section/Introduction/Character-Sets-
            and-Names) characters Example: Test name latin .
        country_code (Union[None, Unset, str]): Country code of the league. We recommend you use ISO-3166-1:alpha3
            (upper case) values where available. Example: USA.
        region_type (Union[Unset, LeagueUpdateLeaguePutBodyRegionType]): How geographically relevant is this league
            >- `INTERNATIONAL` Multiple countries
            >- `INTERSTATE` Cross state
            >- `LOCAL` Local area
            >- `NATIONAL` One country
            >- `STATE` One state
             Example: STATE.
        social (Union['LeagueUpdateLeaguePutBodySocialMedia', None, Unset]): Social Media contacts
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    abbreviation_local: Union[None, Unset, str] = UNSET
    name_local: Union[Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    country_code: Union[None, Unset, str] = UNSET
    region_type: Union[Unset, LeagueUpdateLeaguePutBodyRegionType] = UNSET
    social: Union["LeagueUpdateLeaguePutBodySocialMedia", None, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.league_update_league_put_body_social_media import (
            LeagueUpdateLeaguePutBodySocialMedia,
        )

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

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, LeagueUpdateLeaguePutBodySocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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
        if social is not UNSET:
            field_dict["social"] = social
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.league_update_league_put_body_social_media import (
            LeagueUpdateLeaguePutBodySocialMedia,
        )

        d = dict(src_dict)

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

        _region_type = d.pop("regionType", UNSET)
        region_type: Union[Unset, LeagueUpdateLeaguePutBodyRegionType]
        if isinstance(_region_type, Unset):
            region_type = UNSET
        else:
            region_type = LeagueUpdateLeaguePutBodyRegionType(_region_type)

        def _parse_social(
            data: object,
        ) -> Union["LeagueUpdateLeaguePutBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = LeagueUpdateLeaguePutBodySocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["LeagueUpdateLeaguePutBodySocialMedia", None, Unset], data
            )

        social = _parse_social(d.pop("social", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        league_update_league_put_body = cls(
            abbreviation_local=abbreviation_local,
            name_local=name_local,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            country_code=country_code,
            region_type=region_type,
            social=social,
            external_id=external_id,
        )

        return league_update_league_put_body
