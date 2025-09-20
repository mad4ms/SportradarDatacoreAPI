from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_resolution_for_extra_depth_h2_hs_sort_direction import (
    StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2HsSortDirection,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2Hs",
)


@_attrs_define
class StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2Hs:
    """
    Attributes:
        sort_field (Union[Unset, str]): Sort Field
        sort_direction (Union[Unset, StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadT
            oHeadResolutionForExtraDepthH2HsSortDirection]): Sort direction
    """

    sort_field: Union[Unset, str] = UNSET
    sort_direction: Union[
        Unset,
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2HsSortDirection,
    ] = UNSET

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
        sort_direction: Union[
            Unset,
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2HsSortDirection,
        ]
        if isinstance(_sort_direction, Unset):
            sort_direction = UNSET
        else:
            sort_direction = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfigurationHeadToHeadResolutionForExtraDepthH2HsSortDirection(
                _sort_direction
            )

        standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_resolution_for_extra_depth_h2_hs = cls(
            sort_field=sort_field,
            sort_direction=sort_direction,
        )

        return standing_configurations_update_standing_configurations_put_body_standing_configuration_head_to_head_resolution_for_extra_depth_h2_hs
