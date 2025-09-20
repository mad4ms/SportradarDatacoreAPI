from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.leader_qualifier_post_body_comparison_type import LeaderQualifierPostBodyComparisonType
from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderQualifierPostBody")


@_attrs_define
class LeaderQualifierPostBody:
    """
    Attributes:
        leader_criteria_id (UUID): The unique identifier of the ~LeaderCriteria~ Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        statistic_field (str): The statistic field that this qualifier is for.
        comparison_field (str): The statistic field to compare against.
        comparison_type (LeaderQualifierPostBodyComparisonType): Comparison type for the qualifier
            >- `EQUAL` Equal
            >- `GREATER_THAN` Greater than
            >- `GREATER_THAN_EQUAL` Greater than or equal
            >- `LESS_THAN` Less than
            >- `LESS_THAN_EQUAL` Less than or equal
             Example: GREATER_THAN.
        comparison_value (float): Comparison value for the qualifier
        qualifier_id (Union[Unset, UUID]): The unique identifier of the leader qualifier Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    leader_criteria_id: UUID
    statistic_field: str
    comparison_field: str
    comparison_type: LeaderQualifierPostBodyComparisonType
    comparison_value: float
    qualifier_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        leader_criteria_id = str(self.leader_criteria_id)

        statistic_field = self.statistic_field

        comparison_field = self.comparison_field

        comparison_type = self.comparison_type.value

        comparison_value = self.comparison_value

        qualifier_id: Union[Unset, str] = UNSET
        if not isinstance(self.qualifier_id, Unset):
            qualifier_id = str(self.qualifier_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "leaderCriteriaId": leader_criteria_id,
                "statisticField": statistic_field,
                "comparisonField": comparison_field,
                "comparisonType": comparison_type,
                "comparisonValue": comparison_value,
            }
        )
        if qualifier_id is not UNSET:
            field_dict["qualifierId"] = qualifier_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        leader_criteria_id = UUID(d.pop("leaderCriteriaId"))

        statistic_field = d.pop("statisticField")

        comparison_field = d.pop("comparisonField")

        comparison_type = LeaderQualifierPostBodyComparisonType(d.pop("comparisonType"))

        comparison_value = d.pop("comparisonValue")

        _qualifier_id = d.pop("qualifierId", UNSET)
        qualifier_id: Union[Unset, UUID]
        if isinstance(_qualifier_id, Unset):
            qualifier_id = UNSET
        else:
            qualifier_id = UUID(_qualifier_id)

        leader_qualifier_post_body = cls(
            leader_criteria_id=leader_criteria_id,
            statistic_field=statistic_field,
            comparison_field=comparison_field,
            comparison_type=comparison_type,
            comparison_value=comparison_value,
            qualifier_id=qualifier_id,
        )

        return leader_qualifier_post_body
