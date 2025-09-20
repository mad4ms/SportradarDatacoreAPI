from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchModelEnvironmentalDetails")


@_attrs_define
class MatchModelEnvironmentalDetails:
    """Details about the environment during the fixture

    Attributes:
        surface_condition (Union[Unset, str]): Condition of surface
    """

    surface_condition: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        surface_condition = self.surface_condition

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if surface_condition is not UNSET:
            field_dict["surfaceCondition"] = surface_condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        surface_condition = d.pop("surfaceCondition", UNSET)

        match_model_environmental_details = cls(
            surface_condition=surface_condition,
        )

        return match_model_environmental_details
