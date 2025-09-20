from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.leader_qualifiers_update_leader_qualifier_put_body_comparison_type import (
    LeaderQualifiersUpdateLeaderQualifierPutBodyComparisonType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderQualifiersUpdateLeaderQualifierPutBody")


@_attrs_define
class LeaderQualifiersUpdateLeaderQualifierPutBody:
    """
    Attributes:
        leader_criteria_id (Union[Unset, UUID]): The unique identifier of the ~LeaderCriteria~ Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        statistic_field (Union[Unset, str]): The statistic field that this qualifier is for.
        comparison_field (Union[Unset, str]): The statistic field to compare against.
        comparison_type (Union[Unset, LeaderQualifiersUpdateLeaderQualifierPutBodyComparisonType]): Comparison type for
            the qualifier
            >- `EQUAL` Equal
            >- `GREATER_THAN` Greater than
            >- `GREATER_THAN_EQUAL` Greater than or equal
            >- `LESS_THAN` Less than
            >- `LESS_THAN_EQUAL` Less than or equal
             Example: GREATER_THAN.
        comparison_value (Union[Unset, float]): Comparison value for the qualifier
    """

    leader_criteria_id: Union[Unset, UUID] = UNSET
    statistic_field: Union[Unset, str] = UNSET
    comparison_field: Union[Unset, str] = UNSET
    comparison_type: Union[
        Unset, LeaderQualifiersUpdateLeaderQualifierPutBodyComparisonType
    ] = UNSET
    comparison_value: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        leader_criteria_id: Union[Unset, str] = UNSET
        if not isinstance(self.leader_criteria_id, Unset):
            leader_criteria_id = str(self.leader_criteria_id)

        statistic_field = self.statistic_field

        comparison_field = self.comparison_field

        comparison_type: Union[Unset, str] = UNSET
        if not isinstance(self.comparison_type, Unset):
            comparison_type = self.comparison_type.value

        comparison_value = self.comparison_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if leader_criteria_id is not UNSET:
            field_dict["leaderCriteriaId"] = leader_criteria_id
        if statistic_field is not UNSET:
            field_dict["statisticField"] = statistic_field
        if comparison_field is not UNSET:
            field_dict["comparisonField"] = comparison_field
        if comparison_type is not UNSET:
            field_dict["comparisonType"] = comparison_type
        if comparison_value is not UNSET:
            field_dict["comparisonValue"] = comparison_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _leader_criteria_id = d.pop("leaderCriteriaId", UNSET)
        leader_criteria_id: Union[Unset, UUID]
        if isinstance(_leader_criteria_id, Unset):
            leader_criteria_id = UNSET
        else:
            leader_criteria_id = UUID(_leader_criteria_id)

        statistic_field = d.pop("statisticField", UNSET)

        comparison_field = d.pop("comparisonField", UNSET)

        _comparison_type = d.pop("comparisonType", UNSET)
        comparison_type: Union[
            Unset, LeaderQualifiersUpdateLeaderQualifierPutBodyComparisonType
        ]
        if isinstance(_comparison_type, Unset):
            comparison_type = UNSET
        else:
            comparison_type = (
                LeaderQualifiersUpdateLeaderQualifierPutBodyComparisonType(
                    _comparison_type
                )
            )

        comparison_value = d.pop("comparisonValue", UNSET)

        leader_qualifiers_update_leader_qualifier_put_body = cls(
            leader_criteria_id=leader_criteria_id,
            statistic_field=statistic_field,
            comparison_field=comparison_field,
            comparison_type=comparison_type,
            comparison_value=comparison_value,
        )

        return leader_qualifiers_update_leader_qualifier_put_body
