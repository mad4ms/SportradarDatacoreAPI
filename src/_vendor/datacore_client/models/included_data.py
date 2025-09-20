from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.included_data_resources import IncludedDataResources


T = TypeVar("T", bound="IncludedData")


@_attrs_define
class IncludedData:
    """Available if the request used the 'include' parameter.  It contains extra data about resources found in the data
    block.

        Attributes:
            resources (Union[Unset, IncludedDataResources]):
    """

    resources: Union[Unset, "IncludedDataResources"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resources: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.included_data_resources import IncludedDataResources

        d = dict(src_dict)
        _resources = d.pop("resources", UNSET)
        resources: Union[Unset, IncludedDataResources]
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = IncludedDataResources.from_dict(_resources)

        included_data = cls(
            resources=resources,
        )

        included_data.additional_properties = d
        return included_data

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
