from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityInsertTeamPostBodyAdditionalNames")


@_attrs_define
class EntityInsertTeamPostBodyAdditionalNames:
    """
    Attributes:
        name_short_local (Union[None, Unset, str]): The short name of the team in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Armadillos.
        name_place_local (Union[None, Unset, str]): The name of the place associated with the team in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Los Angeles.
        name_short_latin (Union[None, Unset, str]): The short name of the team using
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Armadillos.
        name_place_latin (Union[None, Unset, str]): The name of the place associated with the team using
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Los Angeles.
    """

    name_short_local: Union[None, Unset, str] = UNSET
    name_place_local: Union[None, Unset, str] = UNSET
    name_short_latin: Union[None, Unset, str] = UNSET
    name_place_latin: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name_short_local: Union[None, Unset, str]
        if isinstance(self.name_short_local, Unset):
            name_short_local = UNSET
        else:
            name_short_local = self.name_short_local

        name_place_local: Union[None, Unset, str]
        if isinstance(self.name_place_local, Unset):
            name_place_local = UNSET
        else:
            name_place_local = self.name_place_local

        name_short_latin: Union[None, Unset, str]
        if isinstance(self.name_short_latin, Unset):
            name_short_latin = UNSET
        else:
            name_short_latin = self.name_short_latin

        name_place_latin: Union[None, Unset, str]
        if isinstance(self.name_place_latin, Unset):
            name_place_latin = UNSET
        else:
            name_place_latin = self.name_place_latin

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_short_local is not UNSET:
            field_dict["nameShortLocal"] = name_short_local
        if name_place_local is not UNSET:
            field_dict["namePlaceLocal"] = name_place_local
        if name_short_latin is not UNSET:
            field_dict["nameShortLatin"] = name_short_latin
        if name_place_latin is not UNSET:
            field_dict["namePlaceLatin"] = name_place_latin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_name_short_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_short_local = _parse_name_short_local(d.pop("nameShortLocal", UNSET))

        def _parse_name_place_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_place_local = _parse_name_place_local(d.pop("namePlaceLocal", UNSET))

        def _parse_name_short_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_short_latin = _parse_name_short_latin(d.pop("nameShortLatin", UNSET))

        def _parse_name_place_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_place_latin = _parse_name_place_latin(d.pop("namePlaceLatin", UNSET))

        entity_insert_team_post_body_additional_names = cls(
            name_short_local=name_short_local,
            name_place_local=name_place_local,
            name_short_latin=name_short_latin,
            name_place_latin=name_place_latin,
        )

        entity_insert_team_post_body_additional_names.additional_properties = d
        return entity_insert_team_post_body_additional_names

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
