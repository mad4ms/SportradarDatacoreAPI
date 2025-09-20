from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="Model")


@_attrs_define
class Model:
    """
    Attributes:
        success (Union[Unset, bool]): Was the call a success? Example: True.
    """

    success: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success", UNSET)

        model = cls(
            success=success,
        )

        return model
