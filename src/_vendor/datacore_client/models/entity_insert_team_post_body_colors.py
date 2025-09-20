from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityInsertTeamPostBodyColors")


@_attrs_define
class EntityInsertTeamPostBodyColors:
    """
    Attributes:
        primary (Union[None, Unset, str]): Primary color of the team.  Colors are a hexadecimal string `RRGGBB` with
            `RR`(red), `GG`(green) and `BB`(blue) representing the components of the colour.  Example: FFF111.
        secondary (Union[None, Unset, str]): Secondary color of the team.  Colors are a hexadecimal string `RRGGBB` with
            `RR`(red), `GG`(green) and `BB`(blue) representing the components of the colour.  Example: FFF111.
        tertiary (Union[None, Unset, str]): Tertiary color of the team.  Colors are a hexadecimal string `RRGGBB` with
            `RR`(red), `GG`(green) and `BB`(blue) representing the components of the colour.  Example: FFF111.
    """

    primary: Union[None, Unset, str] = UNSET
    secondary: Union[None, Unset, str] = UNSET
    tertiary: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary: Union[None, Unset, str]
        if isinstance(self.primary, Unset):
            primary = UNSET
        else:
            primary = self.primary

        secondary: Union[None, Unset, str]
        if isinstance(self.secondary, Unset):
            secondary = UNSET
        else:
            secondary = self.secondary

        tertiary: Union[None, Unset, str]
        if isinstance(self.tertiary, Unset):
            tertiary = UNSET
        else:
            tertiary = self.tertiary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["primary"] = primary
        if secondary is not UNSET:
            field_dict["secondary"] = secondary
        if tertiary is not UNSET:
            field_dict["tertiary"] = tertiary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_primary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        primary = _parse_primary(d.pop("primary", UNSET))

        def _parse_secondary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        secondary = _parse_secondary(d.pop("secondary", UNSET))

        def _parse_tertiary(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tertiary = _parse_tertiary(d.pop("tertiary", UNSET))

        entity_insert_team_post_body_colors = cls(
            primary=primary,
            secondary=secondary,
            tertiary=tertiary,
        )

        entity_insert_team_post_body_colors.additional_properties = d
        return entity_insert_team_post_body_colors

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
