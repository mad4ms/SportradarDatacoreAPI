from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseLinks")


@_attrs_define
class ResponseLinks:
    """
    Attributes:
        self_ (Union[Unset, str]): The URI referencing this request.
        next_ (Union[Unset, str]): The URI referencing the 'next' page, if more data is available.
        previous (Union[Unset, str]): The URI referencing the 'previous' page, if the request is not on the first page.
    """

    self_: Union[Unset, str] = UNSET
    next_: Union[Unset, str] = UNSET
    previous: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        next_ = self.next_

        previous = self.previous

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if next_ is not UNSET:
            field_dict["next"] = next_
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        self_ = d.pop("self", UNSET)

        next_ = d.pop("next", UNSET)

        previous = d.pop("previous", UNSET)

        response_links = cls(
            self_=self_,
            next_=next_,
            previous=previous,
        )

        response_links.additional_properties = d
        return response_links

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
