from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="HeadToHeadIdentification")


@_attrs_define
class HeadToHeadIdentification:
    """
    Attributes:
        check_field (Union[Unset, str]): Field to check
    """

    check_field: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        check_field = self.check_field

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if check_field is not UNSET:
            field_dict["checkField"] = check_field

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_field = d.pop("checkField", UNSET)

        head_to_head_identification = cls(
            check_field=check_field,
        )

        return head_to_head_identification
