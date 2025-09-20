from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_list_model_reason import ErrorListModelReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="ErrorListModel")


@_attrs_define
class ErrorListModel:
    """
    Attributes:
        code (Union[Unset, int]): HTTP Error code indicating the type of error. Example: 400.
        reason (Union[Unset, ErrorListModelReason]): A short code indicating the type of error Example: INVALID_DATA.
        message (Union[Unset, str]): A message indicating the reason for the error Example: Field 'dob' must contain a
            valid date.
        row_number (Union[Unset, int]): The row number of the payload that cause the error Example: 1.
    """

    code: Union[Unset, int] = UNSET
    reason: Union[Unset, ErrorListModelReason] = UNSET
    message: Union[Unset, str] = UNSET
    row_number: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        reason: Union[Unset, str] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.value

        message = self.message

        row_number = self.row_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if reason is not UNSET:
            field_dict["reason"] = reason
        if message is not UNSET:
            field_dict["message"] = message
        if row_number is not UNSET:
            field_dict["rowNumber"] = row_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, ErrorListModelReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = ErrorListModelReason(_reason)

        message = d.pop("message", UNSET)

        row_number = d.pop("rowNumber", UNSET)

        error_list_model = cls(
            code=code,
            reason=reason,
            message=message,
            row_number=row_number,
        )

        error_list_model.additional_properties = d
        return error_list_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
