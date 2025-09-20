from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_configurations_insert_standing_configurations_post_body_standing_building import (
        StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding,
    )
    from ..models.standing_configurations_insert_standing_configurations_post_body_standing_configuration import (
        StandingConfigurationsInsertStandingConfigurationsPostBodyStandingConfiguration,
    )


T = TypeVar("T", bound="StandingConfigurationsInsertStandingConfigurationsPostBody")


@_attrs_define
class StandingConfigurationsInsertStandingConfigurationsPostBody:
    """
    Attributes:
        name_local (str): The name of the ~standing_configurations~ in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: Test season.
        standing_configuration_id (Union[Unset, UUID]): The unique identifier of the configuration Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name_latin (Union[None, Unset, str]): The name of the ~standing_configurations~ in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Test season.
        build_rules (Union[Unset, StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding]): Suilding
            definitions
        configuration (Union[Unset, StandingConfigurationsInsertStandingConfigurationsPostBodyStandingConfiguration]):
            Configuration definitions
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    name_local: str
    standing_configuration_id: Union[Unset, UUID] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    build_rules: Union[
        Unset,
        "StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding",
    ] = UNSET
    configuration: Union[
        Unset,
        "StandingConfigurationsInsertStandingConfigurationsPostBodyStandingConfiguration",
    ] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name_local = self.name_local

        standing_configuration_id: Union[Unset, str] = UNSET
        if not isinstance(self.standing_configuration_id, Unset):
            standing_configuration_id = str(self.standing_configuration_id)

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

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "nameLocal": name_local,
            }
        )
        if standing_configuration_id is not UNSET:
            field_dict["standingConfigurationId"] = standing_configuration_id
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if build_rules is not UNSET:
            field_dict["buildRules"] = build_rules
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_configurations_insert_standing_configurations_post_body_standing_building import (
            StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding,
        )
        from ..models.standing_configurations_insert_standing_configurations_post_body_standing_configuration import (
            StandingConfigurationsInsertStandingConfigurationsPostBodyStandingConfiguration,
        )

        d = dict(src_dict)
        name_local = d.pop("nameLocal")

        _standing_configuration_id = d.pop("standingConfigurationId", UNSET)
        standing_configuration_id: Union[Unset, UUID]
        if isinstance(_standing_configuration_id, Unset):
            standing_configuration_id = UNSET
        else:
            standing_configuration_id = UUID(_standing_configuration_id)

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        _build_rules = d.pop("buildRules", UNSET)
        build_rules: Union[
            Unset,
            StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding,
        ]
        if isinstance(_build_rules, Unset):
            build_rules = UNSET
        else:
            build_rules = StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding.from_dict(
                _build_rules
            )

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[
            Unset,
            StandingConfigurationsInsertStandingConfigurationsPostBodyStandingConfiguration,
        ]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = StandingConfigurationsInsertStandingConfigurationsPostBodyStandingConfiguration.from_dict(
                _configuration
            )

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        standing_configurations_insert_standing_configurations_post_body = cls(
            name_local=name_local,
            standing_configuration_id=standing_configuration_id,
            name_latin=name_latin,
            build_rules=build_rules,
            configuration=configuration,
            external_id=external_id,
        )

        return standing_configurations_insert_standing_configurations_post_body
