import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.leader_criteria_model_organization import LeaderCriteriaModelOrganization


T = TypeVar("T", bound="LeaderCriteriaModel")


@_attrs_define
class LeaderCriteriaModel:
    """
    Attributes:
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, LeaderCriteriaModelOrganization]): The organization that this LeaderCriteria belongs
            to
        leader_criteria_id (Union[Unset, UUID]): The unique identifier of the leader criteria Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name (Union[Unset, str]): The name of the criteria
    """

    added: Union[Unset, datetime.datetime] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "LeaderCriteriaModelOrganization"] = UNSET
    leader_criteria_id: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        leader_criteria_id: Union[Unset, str] = UNSET
        if not isinstance(self.leader_criteria_id, Unset):
            leader_criteria_id = str(self.leader_criteria_id)

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if added is not UNSET:
            field_dict["added"] = added
        if updated is not UNSET:
            field_dict["updated"] = updated
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if leader_criteria_id is not UNSET:
            field_dict["leaderCriteriaId"] = leader_criteria_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leader_criteria_model_organization import LeaderCriteriaModelOrganization

        d = dict(src_dict)
        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, LeaderCriteriaModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = LeaderCriteriaModelOrganization.from_dict(_organization)

        _leader_criteria_id = d.pop("leaderCriteriaId", UNSET)
        leader_criteria_id: Union[Unset, UUID]
        if isinstance(_leader_criteria_id, Unset):
            leader_criteria_id = UNSET
        else:
            leader_criteria_id = UUID(_leader_criteria_id)

        name = d.pop("name", UNSET)

        leader_criteria_model = cls(
            added=added,
            updated=updated,
            organization_id=organization_id,
            organization=organization,
            leader_criteria_id=leader_criteria_id,
            name=name,
        )

        return leader_criteria_model
