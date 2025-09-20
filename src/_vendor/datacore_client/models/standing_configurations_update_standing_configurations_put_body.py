from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_configurations_update_standing_configurations_put_body_standing_building import (
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingBuilding,
    )
    from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration import (
        StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration,
    )


T = TypeVar("T", bound="StandingConfigurationsUpdateStandingConfigurationsPutBody")


@_attrs_define
class StandingConfigurationsUpdateStandingConfigurationsPutBody:
    """
    Attributes:
        name_local (Union[Unset, str]): The name of the ~standing_configurations~ in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Test season.
        name_latin (Union[None, Unset, str]): The name of the ~standing_configurations~ in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Test season.
        build_rules (Union[Unset, StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingBuilding]): Suilding
            definitions
        configuration (Union[Unset, StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration]):
            Configuration definitions
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    build_rules: Union[
        Unset,
        "StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingBuilding",
    ] = UNSET
    configuration: Union[
        Unset,
        "StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration",
    ] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_configurations_update_standing_configurations_put_body_standing_building import (
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingBuilding,
        )
        from ..models.standing_configurations_update_standing_configurations_put_body_standing_configuration import (
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration,
        )

        d = dict(src_dict)
        name_local = d.pop("nameLocal", UNSET)

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
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingBuilding,
        ]
        if isinstance(_build_rules, Unset):
            build_rules = UNSET
        else:
            build_rules = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingBuilding.from_dict(
                _build_rules
            )

        _configuration = d.pop("configuration", UNSET)
        configuration: Union[
            Unset,
            StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration,
        ]
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = StandingConfigurationsUpdateStandingConfigurationsPutBodyStandingConfiguration.from_dict(
                _configuration
            )

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        standing_configurations_update_standing_configurations_put_body = cls(
            name_local=name_local,
            name_latin=name_latin,
            build_rules=build_rules,
            configuration=configuration,
            external_id=external_id,
        )

        return standing_configurations_update_standing_configurations_put_body
