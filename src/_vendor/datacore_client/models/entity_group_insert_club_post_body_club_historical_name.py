import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityGroupInsertClubPostBodyClubHistoricalName")


@_attrs_define
class EntityGroupInsertClubPostBodyClubHistoricalName:
    """
    Attributes:
        date_start (Union[None, Unset, datetime.date]): Start date
        date_end (Union[None, Unset, datetime.date]): End date
        name_full_local (Union[None, Unset, str]): Full name in local language
        name_full_latin (Union[None, Unset, str]): Full name in latin characters
        name_short_local (Union[None, Unset, str]): Short name in local language
        name_short_latin (Union[None, Unset, str]): Short name in latin characters
        name_place_local (Union[None, Unset, str]): Place name in latin characters
    """

    date_start: Union[None, Unset, datetime.date] = UNSET
    date_end: Union[None, Unset, datetime.date] = UNSET
    name_full_local: Union[None, Unset, str] = UNSET
    name_full_latin: Union[None, Unset, str] = UNSET
    name_short_local: Union[None, Unset, str] = UNSET
    name_short_latin: Union[None, Unset, str] = UNSET
    name_place_local: Union[None, Unset, str] = UNSET

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

        name_full_local: Union[None, Unset, str]
        if isinstance(self.name_full_local, Unset):
            name_full_local = UNSET
        else:
            name_full_local = self.name_full_local

        name_full_latin: Union[None, Unset, str]
        if isinstance(self.name_full_latin, Unset):
            name_full_latin = UNSET
        else:
            name_full_latin = self.name_full_latin

        name_short_local: Union[None, Unset, str]
        if isinstance(self.name_short_local, Unset):
            name_short_local = UNSET
        else:
            name_short_local = self.name_short_local

        name_short_latin: Union[None, Unset, str]
        if isinstance(self.name_short_latin, Unset):
            name_short_latin = UNSET
        else:
            name_short_latin = self.name_short_latin

        name_place_local: Union[None, Unset, str]
        if isinstance(self.name_place_local, Unset):
            name_place_local = UNSET
        else:
            name_place_local = self.name_place_local

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if date_start is not UNSET:
            field_dict["dateStart"] = date_start
        if date_end is not UNSET:
            field_dict["dateEnd"] = date_end
        if name_full_local is not UNSET:
            field_dict["nameFullLocal"] = name_full_local
        if name_full_latin is not UNSET:
            field_dict["nameFullLatin"] = name_full_latin
        if name_short_local is not UNSET:
            field_dict["nameShortLocal"] = name_short_local
        if name_short_latin is not UNSET:
            field_dict["nameShortLatin"] = name_short_latin
        if name_place_local is not UNSET:
            field_dict["namePlaceLocal"] = name_place_local

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

        def _parse_name_full_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_full_local = _parse_name_full_local(d.pop("nameFullLocal", UNSET))

        def _parse_name_full_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_full_latin = _parse_name_full_latin(d.pop("nameFullLatin", UNSET))

        def _parse_name_short_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_short_local = _parse_name_short_local(d.pop("nameShortLocal", UNSET))

        def _parse_name_short_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_short_latin = _parse_name_short_latin(d.pop("nameShortLatin", UNSET))

        def _parse_name_place_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_place_local = _parse_name_place_local(d.pop("namePlaceLocal", UNSET))

        entity_group_insert_club_post_body_club_historical_name = cls(
            date_start=date_start,
            date_end=date_end,
            name_full_local=name_full_local,
            name_full_latin=name_full_latin,
            name_short_local=name_short_local,
            name_short_latin=name_short_latin,
            name_place_local=name_place_local,
        )

        return entity_group_insert_club_post_body_club_historical_name
