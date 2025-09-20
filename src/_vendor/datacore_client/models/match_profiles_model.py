import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_profiles_model_match_profile_configuration import MatchProfilesModelMatchProfileConfiguration
    from ..models.match_profiles_model_organization import MatchProfilesModelOrganization


T = TypeVar("T", bound="MatchProfilesModel")


@_attrs_define
class MatchProfilesModel:
    """
    Attributes:
        profile_id (Union[Unset, UUID]): The unique identifier of the profile Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, MatchProfilesModelOrganization]): The organization that this match profiles belongs
            to
        name (Union[Unset, str]): Name of the match profile
        profile (Union[Unset, MatchProfilesModelMatchProfileConfiguration]): Match Profile Configuration
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        default_profile (Union[Unset, bool]): Is this the default profile for the organization?
    """

    profile_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "MatchProfilesModelOrganization"] = UNSET
    name: Union[Unset, str] = UNSET
    profile: Union[Unset, "MatchProfilesModelMatchProfileConfiguration"] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    default_profile: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        profile_id: Union[Unset, str] = UNSET
        if not isinstance(self.profile_id, Unset):
            profile_id = str(self.profile_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        name = self.name

        profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        default_profile = self.default_profile

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if profile_id is not UNSET:
            field_dict["profileId"] = profile_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if name is not UNSET:
            field_dict["name"] = name
        if profile is not UNSET:
            field_dict["profile"] = profile
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if default_profile is not UNSET:
            field_dict["defaultProfile"] = default_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_profiles_model_match_profile_configuration import (
            MatchProfilesModelMatchProfileConfiguration,
        )
        from ..models.match_profiles_model_organization import MatchProfilesModelOrganization

        d = dict(src_dict)
        _profile_id = d.pop("profileId", UNSET)
        profile_id: Union[Unset, UUID]
        if isinstance(_profile_id, Unset):
            profile_id = UNSET
        else:
            profile_id = UUID(_profile_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, MatchProfilesModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = MatchProfilesModelOrganization.from_dict(_organization)

        name = d.pop("name", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[Unset, MatchProfilesModelMatchProfileConfiguration]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = MatchProfilesModelMatchProfileConfiguration.from_dict(_profile)

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        default_profile = d.pop("defaultProfile", UNSET)

        match_profiles_model = cls(
            profile_id=profile_id,
            organization_id=organization_id,
            organization=organization,
            name=name,
            profile=profile,
            updated=updated,
            added=added,
            external_id=external_id,
            default_profile=default_profile,
        )

        return match_profiles_model
