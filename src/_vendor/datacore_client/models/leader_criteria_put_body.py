from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderCriteriaPutBody")


@_attrs_define
class LeaderCriteriaPutBody:
    """
    Attributes:
        name (Union[Unset, str]): The name of the criteria
    """

    name: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        leader_criteria_put_body = cls(
            name=name,
        )

        return leader_criteria_put_body
