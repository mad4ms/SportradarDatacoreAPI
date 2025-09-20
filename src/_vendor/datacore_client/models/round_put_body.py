from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoundPutBody")


@_attrs_define
class RoundPutBody:
    """
    Attributes:
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        round_number (Union[None, Unset, str]): The number given to the round Example: 1.
        name_local (Union[None, Unset, str]): The name of the round in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: Rivalry Round.
        name_latin (Union[None, Unset, str]): The name of the round in [latin](#section/Introduction/Character-Sets-and-
            Names) characters Example: Rivalry Round.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: RR.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: RR.
        round_order (Union[None, Unset, int]): User defined sort order of the stage Example: 1.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    pool_code: Union[None, Unset, str] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    round_number: Union[None, Unset, str] = UNSET
    name_local: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    round_order: Union[None, Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        pool_code: Union[None, Unset, str]
        if isinstance(self.pool_code, Unset):
            pool_code = UNSET
        else:
            pool_code = self.pool_code

        stage_code: Union[None, Unset, str]
        if isinstance(self.stage_code, Unset):
            stage_code = UNSET
        else:
            stage_code = self.stage_code

        round_number: Union[None, Unset, str]
        if isinstance(self.round_number, Unset):
            round_number = UNSET
        else:
            round_number = self.round_number

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

        round_order: Union[None, Unset, int]
        if isinstance(self.round_order, Unset):
            round_order = UNSET
        else:
            round_order = self.round_order

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if round_number is not UNSET:
            field_dict["roundNumber"] = round_number
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if round_order is not UNSET:
            field_dict["roundOrder"] = round_order
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        def _parse_stage_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage_code = _parse_stage_code(d.pop("stageCode", UNSET))

        def _parse_round_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_number = _parse_round_number(d.pop("roundNumber", UNSET))

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

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(d.pop("abbreviationLocal", UNSET))

        def _parse_abbreviation_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_latin = _parse_abbreviation_latin(d.pop("abbreviationLatin", UNSET))

        def _parse_round_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        round_order = _parse_round_order(d.pop("roundOrder", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        round_put_body = cls(
            pool_code=pool_code,
            stage_code=stage_code,
            round_number=round_number,
            name_local=name_local,
            name_latin=name_latin,
            abbreviation_local=abbreviation_local,
            abbreviation_latin=abbreviation_latin,
            round_order=round_order,
            external_id=external_id,
        )

        return round_put_body
