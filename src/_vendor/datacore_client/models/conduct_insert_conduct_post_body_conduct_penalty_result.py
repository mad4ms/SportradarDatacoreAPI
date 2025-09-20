from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.conduct_insert_conduct_post_body_conduct_penalty_result_penalty_type import (
    ConductInsertConductPostBodyConductPenaltyResultPenaltyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConductInsertConductPostBodyConductPenaltyResult")


@_attrs_define
class ConductInsertConductPostBodyConductPenaltyResult:
    """
    Attributes:
        penalty_type (Union[Unset, ConductInsertConductPostBodyConductPenaltyResultPenaltyType]): Penalty type Example:
            WEEK.
        penalty_value (Union[None, Unset, int]): Penalty value Example: 6.
    """

    penalty_type: Union[
        Unset, ConductInsertConductPostBodyConductPenaltyResultPenaltyType
    ] = UNSET
    penalty_value: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        penalty_type: Union[Unset, str] = UNSET
        if not isinstance(self.penalty_type, Unset):
            penalty_type = self.penalty_type.value

        penalty_value: Union[None, Unset, int]
        if isinstance(self.penalty_value, Unset):
            penalty_value = UNSET
        else:
            penalty_value = self.penalty_value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if penalty_type is not UNSET:
            field_dict["penaltyType"] = penalty_type
        if penalty_value is not UNSET:
            field_dict["penaltyValue"] = penalty_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _penalty_type = d.pop("penaltyType", UNSET)
        penalty_type: Union[
            Unset, ConductInsertConductPostBodyConductPenaltyResultPenaltyType
        ]
        if isinstance(_penalty_type, Unset):
            penalty_type = UNSET
        else:
            penalty_type = ConductInsertConductPostBodyConductPenaltyResultPenaltyType(
                _penalty_type
            )

        def _parse_penalty_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        penalty_value = _parse_penalty_value(d.pop("penaltyValue", UNSET))

        conduct_insert_conduct_post_body_conduct_penalty_result = cls(
            penalty_type=penalty_type,
            penalty_value=penalty_value,
        )

        return conduct_insert_conduct_post_body_conduct_penalty_result
