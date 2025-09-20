import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonInsertPersonPostBodyPersonHistoricalName")


@_attrs_define
class PersonInsertPersonPostBodyPersonHistoricalName:
    """
    Attributes:
        date_start (Union[None, Unset, datetime.date]): Start date
        date_end (Union[None, Unset, datetime.date]): End date
        name_full_local (Union[None, Unset, str]): The full name of the person in
            [local](#section/Introduction/Character-Sets-and-Names) language
        name_given_local (Union[None, Unset, str]): Given name of the person in [local](#section/Introduction/Character-
            Sets-and-Names) language
        name_family_local (Union[None, Unset, str]): Family name of the person in
            [local](#section/Introduction/Character-Sets-and-Names) language
        name_full_latin (Union[None, Unset, str]): The full name of the person in
            [latin](##section/Introduction/Character-Sets-and-Names) characters
        name_given_latin (Union[None, Unset, str]): Given name of the person in [latin](#section/Introduction/Character-
            Sets-and-Names) characters
        name_family_latin (Union[None, Unset, str]): Family name of the person in
            [latin](#section/Introduction/Character-Sets-and-Names) characters
    """

    date_start: Union[None, Unset, datetime.date] = UNSET
    date_end: Union[None, Unset, datetime.date] = UNSET
    name_full_local: Union[None, Unset, str] = UNSET
    name_given_local: Union[None, Unset, str] = UNSET
    name_family_local: Union[None, Unset, str] = UNSET
    name_full_latin: Union[None, Unset, str] = UNSET
    name_given_latin: Union[None, Unset, str] = UNSET
    name_family_latin: Union[None, Unset, str] = UNSET

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

        name_given_local: Union[None, Unset, str]
        if isinstance(self.name_given_local, Unset):
            name_given_local = UNSET
        else:
            name_given_local = self.name_given_local

        name_family_local: Union[None, Unset, str]
        if isinstance(self.name_family_local, Unset):
            name_family_local = UNSET
        else:
            name_family_local = self.name_family_local

        name_full_latin: Union[None, Unset, str]
        if isinstance(self.name_full_latin, Unset):
            name_full_latin = UNSET
        else:
            name_full_latin = self.name_full_latin

        name_given_latin: Union[None, Unset, str]
        if isinstance(self.name_given_latin, Unset):
            name_given_latin = UNSET
        else:
            name_given_latin = self.name_given_latin

        name_family_latin: Union[None, Unset, str]
        if isinstance(self.name_family_latin, Unset):
            name_family_latin = UNSET
        else:
            name_family_latin = self.name_family_latin

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if date_start is not UNSET:
            field_dict["dateStart"] = date_start
        if date_end is not UNSET:
            field_dict["dateEnd"] = date_end
        if name_full_local is not UNSET:
            field_dict["nameFullLocal"] = name_full_local
        if name_given_local is not UNSET:
            field_dict["nameGivenLocal"] = name_given_local
        if name_family_local is not UNSET:
            field_dict["nameFamilyLocal"] = name_family_local
        if name_full_latin is not UNSET:
            field_dict["nameFullLatin"] = name_full_latin
        if name_given_latin is not UNSET:
            field_dict["nameGivenLatin"] = name_given_latin
        if name_family_latin is not UNSET:
            field_dict["nameFamilyLatin"] = name_family_latin

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

        def _parse_name_given_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_given_local = _parse_name_given_local(d.pop("nameGivenLocal", UNSET))

        def _parse_name_family_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_family_local = _parse_name_family_local(d.pop("nameFamilyLocal", UNSET))

        def _parse_name_full_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_full_latin = _parse_name_full_latin(d.pop("nameFullLatin", UNSET))

        def _parse_name_given_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_given_latin = _parse_name_given_latin(d.pop("nameGivenLatin", UNSET))

        def _parse_name_family_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_family_latin = _parse_name_family_latin(d.pop("nameFamilyLatin", UNSET))

        person_insert_person_post_body_person_historical_name = cls(
            date_start=date_start,
            date_end=date_end,
            name_full_local=name_full_local,
            name_given_local=name_given_local,
            name_family_local=name_family_local,
            name_full_latin=name_full_latin,
            name_given_latin=name_given_latin,
            name_family_latin=name_family_latin,
        )

        return person_insert_person_post_body_person_historical_name
