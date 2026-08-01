from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_model import ErrorModel
    from ..models.response_meta_data import ResponseMetaData


T = TypeVar("T", bound="CesListentityResponseDefault")


@_attrs_define
class CesListentityResponseDefault:
    """
    Attributes:
        meta (Union[Unset, ResponseMetaData]):
        error (Union[Unset, ErrorModel]):
    """

    meta: Union[Unset, "ResponseMetaData"] = UNSET
    error: Union[Unset, "ErrorModel"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        error: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_model import ErrorModel
        from ..models.response_meta_data import ResponseMetaData

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMetaData]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetaData.from_dict(_meta)

        _error = d.pop("error", UNSET)
        error: Union[Unset, ErrorModel]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ErrorModel.from_dict(_error)

        ces_listentity_response_default = cls(
            meta=meta,
            error=error,
        )

        ces_listentity_response_default.additional_properties = d
        return ces_listentity_response_default

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
