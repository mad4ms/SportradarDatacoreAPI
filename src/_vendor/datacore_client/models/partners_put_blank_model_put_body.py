from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PartnersPutBlankModelPutBody")


@_attrs_define
class PartnersPutBlankModelPutBody:
    """ """

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        partners_put_blank_model_put_body = cls()

        return partners_put_blank_model_put_body
