import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_building import StandingBuilding
    from ..models.standing_configuration import StandingConfiguration
    from ..models.standing_configurations_model_organization import StandingConfigurationsModelOrganization


T = TypeVar("T", bound="StandingConfigurationsModel")


@_attrs_define
class StandingConfigurationsModel:
    """
    Attributes:
        standing_configuration_id (Union[Unset, UUID]): The unique identifier of the configuration Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, StandingConfigurationsModelOrganization]): The organization that this
            ~standing_configurations~ belongs to
        name_local (Union[Unset, str]): The name of the ~standing_configurations~ in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Test season.
        name_latin (Union[None, Unset, str]): The name of the ~standing_configurations~ in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Test season.
        build_rules (Union[Unset, StandingBuilding]): Suilding definitions
        configuration (Union[Unset, StandingConfiguration]): Configuration definitions
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    standing_configuration_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "StandingConfigurationsModelOrganization"] = UNSET
    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    build_rules: Union[Unset, "StandingBuilding"] = UNSET
    configuration: Union[Unset, "StandingConfiguration"] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        standing_configuration_id: Union[Unset, str] = UNSET
        if not isinstance(self.standing_configuration_id, Unset):
            standing_configuration_id = str(self.standing_configuration_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        name_local = self.name_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        build_rules: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.build_rules, Unset):
            build_rules = self.build_rules.to_dict()

        configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if standing_configuration_id is not UNSET:
            field_dict["standingConfigurationId"] = standing_configuration_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if build_rules is not UNSET:
            field_dict["buildRules"] = build_rules
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_building import StandingBuilding
        from ..models.standing_configuration import StandingConfiguration
        from ..models.standing_configurations_model_organization import StandingConfigurationsModelOrganization

        d = dict(src_dict)
        _standing_configuration_id = d.pop("standingConfigurationId", UNSET)
        standing_configuration_id: Union[Unset, UUID]
        if isinstance(_standing_configuration_id, Unset):
            standing_configuration_id = UNSET
        else:
            standing_configuration_id = UUID(_standing_configuration_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, StandingConfigurationsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = StandingConfigurationsModelOrganization.from_dict(_organization)

        name_local = d.pop("nameLocal", UNSET)

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        _build_rules = d.pop("buildRules", UNSET)
        build_rules: Union[Unset, StandingBuilding]
        if isinstance(_build_rules, Unset):
            build_rules = UNSET
        else:
            build_rules = StandingBuilding.from_dict(_build_rules)

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[Unset, StandingConfiguration]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = StandingConfiguration.from_dict(_configuration)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        standing_configurations_model = cls(
            standing_configuration_id=standing_configuration_id,
            organization_id=organization_id,
            organization=organization,
            name_local=name_local,
            name_latin=name_latin,
            build_rules=build_rules,
            configuration=configuration,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return standing_configurations_model
