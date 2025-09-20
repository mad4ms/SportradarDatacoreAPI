from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_list_model import ErrorListModel


T = TypeVar("T", bound="ErrorModel")


@_attrs_define
class ErrorModel:
    """
    Attributes:
        code (Union[Unset, int]): HTTP Error code indicating the type of error.  If there are multiple errors, then this
            will be the code of the first one. Example: 400.
        message (Union[Unset, str]): A message indicating the reason for the error. If there are multiple errors, then
            this is the message for the first one. Example: Field 'dob' must contain a valid date.
        errors (Union[Unset, list['ErrorListModel']]):
    """

    code: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    errors: Union[Unset, list["ErrorListModel"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        errors: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_list_model import ErrorListModel

        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = ErrorListModel.from_dict(errors_item_data)

            errors.append(errors_item)

        error_model = cls(
            code=code,
            message=message,
            errors=errors,
        )

        error_model.additional_properties = d
        return error_model

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
