from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.league_external_ids_model_organization_resource_type import (
    LeagueExternalIdsModelOrganizationResourceType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="LeagueExternalIdsModelOrganization")


@_attrs_define
class LeagueExternalIdsModelOrganization:
    """The organization that this league external ids belongs to

    Attributes:
        resource_type (Union[Unset, LeagueExternalIdsModelOrganizationResourceType]):
        id (Union[Unset, str]): Unique identifier for this resource Example: 9.
    """

    resource_type: Union[Unset, LeagueExternalIdsModelOrganizationResourceType] = UNSET
    id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_type: Union[Unset, str] = UNSET
        if not isinstance(self.resource_type, Unset):
            resource_type = self.resource_type.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resource_type is not UNSET:
            field_dict["resourceType"] = resource_type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _resource_type = d.pop("resourceType", UNSET)
        resource_type: Union[Unset, LeagueExternalIdsModelOrganizationResourceType]
        if isinstance(_resource_type, Unset):
            resource_type = UNSET
        else:
            resource_type = LeagueExternalIdsModelOrganizationResourceType(
                _resource_type
            )

        id = d.pop("id", UNSET)

        league_external_ids_model_organization = cls(
            resource_type=resource_type,
            id=id,
        )

        league_external_ids_model_organization.additional_properties = d
        return league_external_ids_model_organization

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
