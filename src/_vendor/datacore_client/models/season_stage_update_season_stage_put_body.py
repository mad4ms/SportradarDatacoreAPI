from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonStageUpdateSeasonStagePutBody")


@_attrs_define
class SeasonStageUpdateSeasonStagePutBody:
    """
    Attributes:
        name_local (Union[None, Unset, str]): The name of the season stage in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Test name local.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the season stage in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test name latin .
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        stage_order (Union[None, Unset, int]): User defined sort order of the stage Example: 1.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    name_local: Union[None, Unset, str] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    stage_order: Union[None, Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name_local: Union[None, Unset, str]
        if isinstance(self.name_local, Unset):
            name_local = UNSET
        else:
            name_local = self.name_local

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        abbreviation_latin: Union[None, Unset, str]
        if isinstance(self.abbreviation_latin, Unset):
            abbreviation_latin = UNSET
        else:
            abbreviation_latin = self.abbreviation_latin

        stage_order: Union[None, Unset, int]
        if isinstance(self.stage_order, Unset):
            stage_order = UNSET
        else:
            stage_order = self.stage_order

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if stage_order is not UNSET:
            field_dict["stageOrder"] = stage_order
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_local = _parse_name_local(d.pop("nameLocal", UNSET))

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(
            d.pop("abbreviationLocal", UNSET)
        )

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_abbreviation_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_latin = _parse_abbreviation_latin(
            d.pop("abbreviationLatin", UNSET)
        )

        def _parse_stage_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stage_order = _parse_stage_order(d.pop("stageOrder", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        season_stage_update_season_stage_put_body = cls(
            name_local=name_local,
            abbreviation_local=abbreviation_local,
            name_latin=name_latin,
            abbreviation_latin=abbreviation_latin,
            stage_order=stage_order,
            external_id=external_id,
        )

        return season_stage_update_season_stage_put_body
