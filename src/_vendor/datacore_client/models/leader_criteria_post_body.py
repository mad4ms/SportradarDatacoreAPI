from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderCriteriaPostBody")


@_attrs_define
class LeaderCriteriaPostBody:
    """
    Attributes:
        name (str): The name of the criteria
        leader_criteria_id (Union[Unset, UUID]): The unique identifier of the leader criteria Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
    """

    name: str
    leader_criteria_id: Union[Unset, UUID] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        leader_criteria_id: Union[Unset, str] = UNSET
        if not isinstance(self.leader_criteria_id, Unset):
            leader_criteria_id = str(self.leader_criteria_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
            }
        )
        if leader_criteria_id is not UNSET:
            field_dict["leaderCriteriaId"] = leader_criteria_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _leader_criteria_id = d.pop("leaderCriteriaId", UNSET)
        leader_criteria_id: Union[Unset, UUID]
        if isinstance(_leader_criteria_id, Unset):
            leader_criteria_id = UNSET
        else:
            leader_criteria_id = UUID(_leader_criteria_id)

        leader_criteria_post_body = cls(
            name=name,
            leader_criteria_id=leader_criteria_id,
        )

        return leader_criteria_post_body
