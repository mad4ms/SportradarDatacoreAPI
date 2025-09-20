from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.standing_configurations_insert_standing_configurations_post_body_standing_building_build_type import (
    StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingBuildType,
)
from ..models.standing_configurations_insert_standing_configurations_post_body_standing_building_fixture_types_item import (
    StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingFixtureTypesItem,
)
from ..models.standing_configurations_insert_standing_configurations_post_body_standing_building_grouping import (
    StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingGrouping,
)
from ..types import UNSET, Unset

T = TypeVar(
    "T",
    bound="StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding",
)


@_attrs_define
class StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuilding:
    """Suilding definitions

    Attributes:
        build_type (StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingBuildType): Overall
            standing Type (ROUND not used on live Standings) Example: OVERALL.
        grouping (StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingGrouping): How to Group
            Example: NONE.
        fixture_types
            (list[StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingFixtureTypesItem]):
        build_overall (Union[Unset, bool]): Build overall standings
        build_conferences (Union[Unset, bool]): Build standings by conference
        build_divisions (Union[Unset, bool]): Build standings by division
        blank_standing (Union[Unset, bool]): Give team blank row if no played
        include_live_fixtures (Union[Unset, bool]): Include live matches
        generate_live_standings (Union[Unset, bool]): Generate live matches
        validate_entities_structure (Union[Unset, bool]): Validate Entities against Fixture structure?
        decimal_places (Union[Unset, float]): Number of decimal places for percentage calculations Default: 4.0.
        skip_latest_flag (Union[Unset, bool]): Skip setting latest=True for ROUND standings?
        skip_clean_round_flag (Union[Unset, bool]): Skip cleaning future blank rounds?
        force_head_to_head (Union[Unset, bool]): Set to true in order to force head-to-head resolution even when there
            aren't enough mutual fixtures between entities in a h2h group
    """

    build_type: StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingBuildType
    grouping: StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingGrouping
    fixture_types: list[
        StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingFixtureTypesItem
    ]
    build_overall: Union[Unset, bool] = UNSET
    build_conferences: Union[Unset, bool] = UNSET
    build_divisions: Union[Unset, bool] = UNSET
    blank_standing: Union[Unset, bool] = UNSET
    include_live_fixtures: Union[Unset, bool] = UNSET
    generate_live_standings: Union[Unset, bool] = UNSET
    validate_entities_structure: Union[Unset, bool] = UNSET
    decimal_places: Union[Unset, float] = 4.0
    skip_latest_flag: Union[Unset, bool] = UNSET
    skip_clean_round_flag: Union[Unset, bool] = UNSET
    force_head_to_head: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        build_type = self.build_type.value

        grouping = self.grouping.value

        fixture_types = []
        for fixture_types_item_data in self.fixture_types:
            fixture_types_item = fixture_types_item_data.value
            fixture_types.append(fixture_types_item)

        build_overall = self.build_overall

        build_conferences = self.build_conferences

        build_divisions = self.build_divisions

        blank_standing = self.blank_standing

        include_live_fixtures = self.include_live_fixtures

        generate_live_standings = self.generate_live_standings

        validate_entities_structure = self.validate_entities_structure

        decimal_places = self.decimal_places

        skip_latest_flag = self.skip_latest_flag

        skip_clean_round_flag = self.skip_clean_round_flag

        force_head_to_head = self.force_head_to_head

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "buildType": build_type,
                "grouping": grouping,
                "fixtureTypes": fixture_types,
            }
        )
        if build_overall is not UNSET:
            field_dict["buildOverall"] = build_overall
        if build_conferences is not UNSET:
            field_dict["buildConferences"] = build_conferences
        if build_divisions is not UNSET:
            field_dict["buildDivisions"] = build_divisions
        if blank_standing is not UNSET:
            field_dict["blankStanding"] = blank_standing
        if include_live_fixtures is not UNSET:
            field_dict["includeLiveFixtures"] = include_live_fixtures
        if generate_live_standings is not UNSET:
            field_dict["generateLiveStandings"] = generate_live_standings
        if validate_entities_structure is not UNSET:
            field_dict["validateEntitiesStructure"] = validate_entities_structure
        if decimal_places is not UNSET:
            field_dict["decimalPlaces"] = decimal_places
        if skip_latest_flag is not UNSET:
            field_dict["skipLatestFlag"] = skip_latest_flag
        if skip_clean_round_flag is not UNSET:
            field_dict["skipCleanRoundFlag"] = skip_clean_round_flag
        if force_head_to_head is not UNSET:
            field_dict["forceHeadToHead"] = force_head_to_head

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        build_type = StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingBuildType(
            d.pop("buildType")
        )

        grouping = StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingGrouping(
            d.pop("grouping")
        )

        fixture_types = []
        _fixture_types = d.pop("fixtureTypes")
        for fixture_types_item_data in _fixture_types:
            fixture_types_item = StandingConfigurationsInsertStandingConfigurationsPostBodyStandingBuildingFixtureTypesItem(
                fixture_types_item_data
            )

            fixture_types.append(fixture_types_item)

        build_overall = d.pop("buildOverall", UNSET)

        build_conferences = d.pop("buildConferences", UNSET)

        build_divisions = d.pop("buildDivisions", UNSET)

        blank_standing = d.pop("blankStanding", UNSET)

        include_live_fixtures = d.pop("includeLiveFixtures", UNSET)

        generate_live_standings = d.pop("generateLiveStandings", UNSET)

        validate_entities_structure = d.pop("validateEntitiesStructure", UNSET)

        decimal_places = d.pop("decimalPlaces", UNSET)

        skip_latest_flag = d.pop("skipLatestFlag", UNSET)

        skip_clean_round_flag = d.pop("skipCleanRoundFlag", UNSET)

        force_head_to_head = d.pop("forceHeadToHead", UNSET)

        standing_configurations_insert_standing_configurations_post_body_standing_building = cls(
            build_type=build_type,
            grouping=grouping,
            fixture_types=fixture_types,
            build_overall=build_overall,
            build_conferences=build_conferences,
            build_divisions=build_divisions,
            blank_standing=blank_standing,
            include_live_fixtures=include_live_fixtures,
            generate_live_standings=generate_live_standings,
            validate_entities_structure=validate_entities_structure,
            decimal_places=decimal_places,
            skip_latest_flag=skip_latest_flag,
            skip_clean_round_flag=skip_clean_round_flag,
            force_head_to_head=force_head_to_head,
        )

        return standing_configurations_insert_standing_configurations_post_body_standing_building
