from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.standing_configurations_model_standing_configuration_head_to_head_resolution_sort_direction import (
    StandingConfigurationsModelStandingConfigurationHeadToHeadResolutionSortDirection,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="StandingConfigurationsModelStandingConfigurationHeadToHeadResolution")


@_attrs_define
class StandingConfigurationsModelStandingConfigurationHeadToHeadResolution:
    """
    Attributes:
        sort_field (Union[Unset, str]): Sort Field
        sort_direction (Union[Unset,
            StandingConfigurationsModelStandingConfigurationHeadToHeadResolutionSortDirection]): Sort direction
    """

    sort_field: Union[Unset, str] = UNSET
    sort_direction: Union[Unset, StandingConfigurationsModelStandingConfigurationHeadToHeadResolutionSortDirection] = (
        UNSET
    )

    def to_dict(self) -> dict[str, Any]:
        sort_field = self.sort_field

        sort_direction: Union[Unset, str] = UNSET
        if not isinstance(self.sort_direction, Unset):
            sort_direction = self.sort_direction.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if sort_field is not UNSET:
            field_dict["sortField"] = sort_field
        if sort_direction is not UNSET:
            field_dict["sortDirection"] = sort_direction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sort_field = d.pop("sortField", UNSET)

        _sort_direction = d.pop("sortDirection", UNSET)
        sort_direction: Union[Unset, StandingConfigurationsModelStandingConfigurationHeadToHeadResolutionSortDirection]
        if isinstance(_sort_direction, Unset):
            sort_direction = UNSET
        else:
            sort_direction = StandingConfigurationsModelStandingConfigurationHeadToHeadResolutionSortDirection(
                _sort_direction
            )

        standing_configurations_model_standing_configuration_head_to_head_resolution = cls(
            sort_field=sort_field,
            sort_direction=sort_direction,
        )

        return standing_configurations_model_standing_configuration_head_to_head_resolution
