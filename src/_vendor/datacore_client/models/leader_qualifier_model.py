import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.leader_qualifier_model_comparison_type import (
    LeaderQualifierModelComparisonType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leader_qualifier_model_leaders_criteria import (
        LeaderQualifierModelLeadersCriteria,
    )
    from ..models.leader_qualifier_model_organization import (
        LeaderQualifierModelOrganization,
    )


T = TypeVar("T", bound="LeaderQualifierModel")


@_attrs_define
class LeaderQualifierModel:
    """
    Attributes:
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        qualifier_id (Union[Unset, UUID]): The unique identifier of the leader qualifier Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, LeaderQualifierModelOrganization]): The organization that this LeaderQualifier
            belongs to
        leader_criteria_id (Union[Unset, UUID]): The unique identifier of the ~LeaderCriteria~ Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        leaders_criteria (Union[Unset, LeaderQualifierModelLeadersCriteria]): The ~LeaderCriteria~ linked to this record
        statistic_field (Union[Unset, str]): The statistic field that this qualifier is for.
        comparison_field (Union[Unset, str]): The statistic field to compare against.
        comparison_type (Union[Unset, LeaderQualifierModelComparisonType]): Comparison type for the qualifier
            >- `EQUAL` Equal
            >- `GREATER_THAN` Greater than
            >- `GREATER_THAN_EQUAL` Greater than or equal
            >- `LESS_THAN` Less than
            >- `LESS_THAN_EQUAL` Less than or equal
             Example: GREATER_THAN.
        comparison_value (Union[Unset, float]): Comparison value for the qualifier
    """

    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    qualifier_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "LeaderQualifierModelOrganization"] = UNSET
    leader_criteria_id: Union[Unset, UUID] = UNSET
    leaders_criteria: Union[Unset, "LeaderQualifierModelLeadersCriteria"] = UNSET
    statistic_field: Union[Unset, str] = UNSET
    comparison_field: Union[Unset, str] = UNSET
    comparison_type: Union[Unset, LeaderQualifierModelComparisonType] = UNSET
    comparison_value: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        qualifier_id: Union[Unset, str] = UNSET
        if not isinstance(self.qualifier_id, Unset):
            qualifier_id = str(self.qualifier_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        leader_criteria_id: Union[Unset, str] = UNSET
        if not isinstance(self.leader_criteria_id, Unset):
            leader_criteria_id = str(self.leader_criteria_id)

        leaders_criteria: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.leaders_criteria, Unset):
            leaders_criteria = self.leaders_criteria.to_dict()

        statistic_field = self.statistic_field

        comparison_field = self.comparison_field

        comparison_type: Union[Unset, str] = UNSET
        if not isinstance(self.comparison_type, Unset):
            comparison_type = self.comparison_type.value

        comparison_value = self.comparison_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if qualifier_id is not UNSET:
            field_dict["qualifierId"] = qualifier_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if leader_criteria_id is not UNSET:
            field_dict["leaderCriteriaId"] = leader_criteria_id
        if leaders_criteria is not UNSET:
            field_dict["leadersCriteria"] = leaders_criteria
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
        from ..models.leader_qualifier_model_leaders_criteria import (
            LeaderQualifierModelLeadersCriteria,
        )
        from ..models.leader_qualifier_model_organization import (
            LeaderQualifierModelOrganization,
        )

        d = dict(src_dict)
        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        _qualifier_id = d.pop("qualifierId", UNSET)
        qualifier_id: Union[Unset, UUID]
        if isinstance(_qualifier_id, Unset):
            qualifier_id = UNSET
        else:
            qualifier_id = UUID(_qualifier_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, LeaderQualifierModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = LeaderQualifierModelOrganization.from_dict(_organization)

        _leader_criteria_id = d.pop("leaderCriteriaId", UNSET)
        leader_criteria_id: Union[Unset, UUID]
        if isinstance(_leader_criteria_id, Unset):
            leader_criteria_id = UNSET
        else:
            leader_criteria_id = UUID(_leader_criteria_id)

        _leaders_criteria = d.pop("leadersCriteria", UNSET)
        leaders_criteria: Union[Unset, LeaderQualifierModelLeadersCriteria]
        if isinstance(_leaders_criteria, Unset):
            leaders_criteria = UNSET
        else:
            leaders_criteria = LeaderQualifierModelLeadersCriteria.from_dict(
                _leaders_criteria
            )

        statistic_field = d.pop("statisticField", UNSET)

        comparison_field = d.pop("comparisonField", UNSET)

        _comparison_type = d.pop("comparisonType", UNSET)
        comparison_type: Union[Unset, LeaderQualifierModelComparisonType]
        if isinstance(_comparison_type, Unset):
            comparison_type = UNSET
        else:
            comparison_type = LeaderQualifierModelComparisonType(_comparison_type)

        comparison_value = d.pop("comparisonValue", UNSET)

        leader_qualifier_model = cls(
            updated=updated,
            added=added,
            qualifier_id=qualifier_id,
            organization_id=organization_id,
            organization=organization,
            leader_criteria_id=leader_criteria_id,
            leaders_criteria=leaders_criteria,
            statistic_field=statistic_field,
            comparison_field=comparison_field,
            comparison_type=comparison_type,
            comparison_value=comparison_value,
        )

        return leader_qualifier_model
