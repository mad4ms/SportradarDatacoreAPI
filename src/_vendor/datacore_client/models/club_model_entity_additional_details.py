from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClubModelEntityAdditionalDetails")


@_attrs_define
class ClubModelEntityAdditionalDetails:
    """Additional detail fields

    Attributes:
        founded (Union[None, Unset, float]): Year Founded
        squad_value (Union[None, Unset, float]): Value of Squad
    """

    founded: Union[None, Unset, float] = UNSET
    squad_value: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        founded: Union[None, Unset, float]
        if isinstance(self.founded, Unset):
            founded = UNSET
        else:
            founded = self.founded

        squad_value: Union[None, Unset, float]
        if isinstance(self.squad_value, Unset):
            squad_value = UNSET
        else:
            squad_value = self.squad_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if founded is not UNSET:
            field_dict["founded"] = founded
        if squad_value is not UNSET:
            field_dict["squadValue"] = squad_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_founded(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        founded = _parse_founded(d.pop("founded", UNSET))

        def _parse_squad_value(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        squad_value = _parse_squad_value(d.pop("squadValue", UNSET))

        club_model_entity_additional_details = cls(
            founded=founded,
            squad_value=squad_value,
        )

        return club_model_entity_additional_details
