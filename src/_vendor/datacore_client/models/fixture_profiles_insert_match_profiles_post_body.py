from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fixture_profiles_insert_match_profiles_post_body_match_profile_configuration import (
        FixtureProfilesInsertMatchProfilesPostBodyMatchProfileConfiguration,
    )


T = TypeVar("T", bound="FixtureProfilesInsertMatchProfilesPostBody")


@_attrs_define
class FixtureProfilesInsertMatchProfilesPostBody:
    """
    Attributes:
        profile_id (Union[Unset, UUID]): The unique identifier of the profile Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name (Union[Unset, str]): Name of the match profile
        profile (Union[Unset, FixtureProfilesInsertMatchProfilesPostBodyMatchProfileConfiguration]): Match Profile
            Configuration
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        default_profile (Union[Unset, bool]): Is this the default profile for the organization?
    """

    profile_id: Union[Unset, UUID] = UNSET
    name: Union[Unset, str] = UNSET
    profile: Union[
        Unset, "FixtureProfilesInsertMatchProfilesPostBodyMatchProfileConfiguration"
    ] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    default_profile: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        profile_id: Union[Unset, str] = UNSET
        if not isinstance(self.profile_id, Unset):
            profile_id = str(self.profile_id)

        name = self.name

        profile: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

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
        if name is not UNSET:
            field_dict["name"] = name
        if profile is not UNSET:
            field_dict["profile"] = profile
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if default_profile is not UNSET:
            field_dict["defaultProfile"] = default_profile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fixture_profiles_insert_match_profiles_post_body_match_profile_configuration import (
            FixtureProfilesInsertMatchProfilesPostBodyMatchProfileConfiguration,
        )

        d = dict(src_dict)
        _profile_id = d.pop("profileId", UNSET)
        profile_id: Union[Unset, UUID]
        if isinstance(_profile_id, Unset):
            profile_id = UNSET
        else:
            profile_id = UUID(_profile_id)

        name = d.pop("name", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: Union[
            Unset, FixtureProfilesInsertMatchProfilesPostBodyMatchProfileConfiguration
        ]
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = FixtureProfilesInsertMatchProfilesPostBodyMatchProfileConfiguration.from_dict(
                _profile
            )

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        default_profile = d.pop("defaultProfile", UNSET)

        fixture_profiles_insert_match_profiles_post_body = cls(
            profile_id=profile_id,
            name=name,
            profile=profile,
            external_id=external_id,
            default_profile=default_profile,
        )

        return fixture_profiles_insert_match_profiles_post_body
