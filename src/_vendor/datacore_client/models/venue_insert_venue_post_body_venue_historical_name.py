import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="VenueInsertVenuePostBodyVenueHistoricalName")


@_attrs_define
class VenueInsertVenuePostBodyVenueHistoricalName:
    """
    Attributes:
        date_start (Union[None, Unset, datetime.date]): Start date
        date_end (Union[None, Unset, datetime.date]): End date
        name_local (Union[None, Unset, str]): Full name in local language
        name_latin (Union[None, Unset, str]): Full name in latin characters
        alternate_name_local (Union[None, Unset, str]): Alternate name in local lanuage
        alternate_name_latin (Union[None, Unset, str]): Alternate name in latin characters
        abbreviation_local (Union[None, Unset, str]): Abbreviation in local lanuage
        abbreviation_latin (Union[None, Unset, str]): Abbreviation in latin characters
    """

    date_start: Union[None, Unset, datetime.date] = UNSET
    date_end: Union[None, Unset, datetime.date] = UNSET
    name_local: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    alternate_name_local: Union[None, Unset, str] = UNSET
    alternate_name_latin: Union[None, Unset, str] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        date_start: Union[None, Unset, str]
        if isinstance(self.date_start, Unset):
            date_start = UNSET
        elif isinstance(self.date_start, datetime.date):
            date_start = self.date_start.isoformat()
        else:
            date_start = self.date_start

        date_end: Union[None, Unset, str]
        if isinstance(self.date_end, Unset):
            date_end = UNSET
        elif isinstance(self.date_end, datetime.date):
            date_end = self.date_end.isoformat()
        else:
            date_end = self.date_end

        name_local: Union[None, Unset, str]
        if isinstance(self.name_local, Unset):
            name_local = UNSET
        else:
            name_local = self.name_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        alternate_name_local: Union[None, Unset, str]
        if isinstance(self.alternate_name_local, Unset):
            alternate_name_local = UNSET
        else:
            alternate_name_local = self.alternate_name_local

        alternate_name_latin: Union[None, Unset, str]
        if isinstance(self.alternate_name_latin, Unset):
            alternate_name_latin = UNSET
        else:
            alternate_name_latin = self.alternate_name_latin

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if date_start is not UNSET:
            field_dict["dateStart"] = date_start
        if date_end is not UNSET:
            field_dict["dateEnd"] = date_end
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if alternate_name_local is not UNSET:
            field_dict["alternateNameLocal"] = alternate_name_local
        if alternate_name_latin is not UNSET:
            field_dict["alternateNameLatin"] = alternate_name_latin
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_date_start(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_start_type_0 = isoparse(data).date()

                return date_start_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_start = _parse_date_start(d.pop("dateStart", UNSET))

        def _parse_date_end(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_end_type_0 = isoparse(data).date()

                return date_end_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_end = _parse_date_end(d.pop("dateEnd", UNSET))

        def _parse_name_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_local = _parse_name_local(d.pop("nameLocal", UNSET))

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_alternate_name_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alternate_name_local = _parse_alternate_name_local(
            d.pop("alternateNameLocal", UNSET)
        )

        def _parse_alternate_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alternate_name_latin = _parse_alternate_name_latin(
            d.pop("alternateNameLatin", UNSET)
        )

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

        venue_insert_venue_post_body_venue_historical_name = cls(
            date_start=date_start,
            date_end=date_end,
            name_local=name_local,
            name_latin=name_latin,
            alternate_name_local=alternate_name_local,
            alternate_name_latin=alternate_name_latin,
            abbreviation_local=abbreviation_local,
            abbreviation_latin=abbreviation_latin,
        )

        return venue_insert_venue_post_body_venue_historical_name
