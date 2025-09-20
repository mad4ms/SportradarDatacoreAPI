from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.standing_adjustment_put_body_adjustment_field import StandingAdjustmentPutBodyAdjustmentField
from ..models.standing_adjustment_put_body_adjustment_group import StandingAdjustmentPutBodyAdjustmentGroup
from ..models.standing_adjustment_put_body_adjustment_type import StandingAdjustmentPutBodyAdjustmentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StandingAdjustmentPutBody")


@_attrs_define
class StandingAdjustmentPutBody:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        round_code (Union[None, Unset, str]): A unique code for the round. (Unique for season) Example: RN1.
        round_number (Union[None, Unset, str]): The number given to the round Example: 1.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        apply_to_all_standings (Union[Unset, bool]): Apply to all generated standing types ? Example: True.
        adjustment_group (Union[Unset, StandingAdjustmentPutBodyAdjustmentGroup]): Adjustment Group
            >- `IN_CONFERENCE` In Conference
            >- `IN_DIVISION` In Division
            >- `OUT_CONFERENCE` Out Conference
            >- `OUT_DIVISION` Out Division
            >- `OVERALL` Overall
        adjustment_type (Union[Unset, StandingAdjustmentPutBodyAdjustmentType]): Adjustment Type
            >- `ADD_MINUS` Add/Subtract Value
            >- `SET` Set Value
        adjustment_field (Union[Unset, StandingAdjustmentPutBodyAdjustmentField]): Adjustment field to calculate
            standings
            >- `byes` Byes
            >- `draws` Games Drawn
            >- `drawsAway` Games Drawn (Away)
            >- `drawsHome` Games Drawn (Home)
            >- `forfeitsGiven` Forfeits Given
            >- `forfeitsWonBy` Forfeits Won
            >- `highestScoreAgainst` Highest Score Against
            >- `highestScoreAgainstAway` Highest Score Against (Away)
            >- `highestScoreAgainstHome` Highest Score Against (Home)
            >- `highestScoreFor` Highest Score For
            >- `highestScoreForAway` Highest Score For (Away)
            >- `highestScoreForHome` Highest Score For (Home)
            >- `losses` Games Lost
            >- `lossesAway` Games Lost (Away)
            >- `lossesHome` Games Lost (Home)
            >- `lowestScoreAgainst` Lowest Score Against
            >- `lowestScoreAgainstAway` Lowest Score Against (Away)
            >- `lowestScoreAgainstHome` Lowest Score Against (Home)
            >- `lowestScoreFor` Lowest Score For
            >- `lowestScoreForAway` Lowest Score For (Away)
            >- `lowestScoreForHome` Lowest Score For (Home)
            >- `percentage` For versus Against Percentage
            >- `percentageAway` For versus Against Percentage (Away)
            >- `percentageHome` For versus Against Percentage (Home)
            >- `played` Games Played
            >- `playedAway` Games Played (Away)
            >- `playedHome` Games Played (Home)
            >- `pointDifference` Point Difference
            >- `pointDifferenceAway` Point Difference (Away)
            >- `pointDifferenceHome` Point Difference (Home)
            >- `position` Standings Position
            >- `scoredAgainst` Score Against
            >- `scoredAgainstAway` Score Against (Away)
            >- `scoredAgainstHome` Score Against (Home)
            >- `scoredFor` Score For
            >- `scoredForAway` Score For (Away)
            >- `scoredForHome` Score For (Home)
            >- `standingPoints` Standing Points for competitor
            >- `standingPointsAway` Standing Points for competitor (Away)
            >- `standingPointsGiven` Standing Points Given away
            >- `standingPointsHome` Standing Points for competitor (Home)
            >- `streak` Winning Streak for competitor
            >- `streakAway` Winning Streak for competitor (Away)
            >- `streakHome` Winning Streak for competitor (Home)
            >- `washouts` Washouts
            >- `winPercentage` Win Percentage
            >- `winPercentageAway` Win Percentage (Away)
            >- `winPercentageHome` Win Percentage (Home)
            >- `wins` Games Won
            >- `winsAway` Games Won (Away)
            >- `winsHome` Games Won (Home)
        adjustment_value (Union[Unset, float]): Value of the adjustment field Example: 2.3.
        reason_type (Union[Unset, str]): Reason type of the adjustment Example: DISCIPLINE.
        reason_description (Union[None, Unset, str]): Reason for the adjustment Example: Points lost due to discipline
            issues.
        grouping_key (Union[None, Unset, str]): Grouping Key to allow bulk deletions or listing by the key Example:
            KEYA123.
    """

    season_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    round_code: Union[None, Unset, str] = UNSET
    round_number: Union[None, Unset, str] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    apply_to_all_standings: Union[Unset, bool] = UNSET
    adjustment_group: Union[Unset, StandingAdjustmentPutBodyAdjustmentGroup] = UNSET
    adjustment_type: Union[Unset, StandingAdjustmentPutBodyAdjustmentType] = UNSET
    adjustment_field: Union[Unset, StandingAdjustmentPutBodyAdjustmentField] = UNSET
    adjustment_value: Union[Unset, float] = UNSET
    reason_type: Union[Unset, str] = UNSET
    reason_description: Union[None, Unset, str] = UNSET
    grouping_key: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        round_code: Union[None, Unset, str]
        if isinstance(self.round_code, Unset):
            round_code = UNSET
        else:
            round_code = self.round_code

        round_number: Union[None, Unset, str]
        if isinstance(self.round_number, Unset):
            round_number = UNSET
        else:
            round_number = self.round_number

        stage_code: Union[None, Unset, str]
        if isinstance(self.stage_code, Unset):
            stage_code = UNSET
        else:
            stage_code = self.stage_code

        pool_code: Union[None, Unset, str]
        if isinstance(self.pool_code, Unset):
            pool_code = UNSET
        else:
            pool_code = self.pool_code

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        apply_to_all_standings = self.apply_to_all_standings

        adjustment_group: Union[Unset, str] = UNSET
        if not isinstance(self.adjustment_group, Unset):
            adjustment_group = self.adjustment_group.value

        adjustment_type: Union[Unset, str] = UNSET
        if not isinstance(self.adjustment_type, Unset):
            adjustment_type = self.adjustment_type.value

        adjustment_field: Union[Unset, str] = UNSET
        if not isinstance(self.adjustment_field, Unset):
            adjustment_field = self.adjustment_field.value

        adjustment_value = self.adjustment_value

        reason_type = self.reason_type

        reason_description: Union[None, Unset, str]
        if isinstance(self.reason_description, Unset):
            reason_description = UNSET
        else:
            reason_description = self.reason_description

        grouping_key: Union[None, Unset, str]
        if isinstance(self.grouping_key, Unset):
            grouping_key = UNSET
        else:
            grouping_key = self.grouping_key

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if round_code is not UNSET:
            field_dict["roundCode"] = round_code
        if round_number is not UNSET:
            field_dict["roundNumber"] = round_number
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if apply_to_all_standings is not UNSET:
            field_dict["applyToAllStandings"] = apply_to_all_standings
        if adjustment_group is not UNSET:
            field_dict["adjustmentGroup"] = adjustment_group
        if adjustment_type is not UNSET:
            field_dict["adjustmentType"] = adjustment_type
        if adjustment_field is not UNSET:
            field_dict["adjustmentField"] = adjustment_field
        if adjustment_value is not UNSET:
            field_dict["adjustmentValue"] = adjustment_value
        if reason_type is not UNSET:
            field_dict["reasonType"] = reason_type
        if reason_description is not UNSET:
            field_dict["reasonDescription"] = reason_description
        if grouping_key is not UNSET:
            field_dict["groupingKey"] = grouping_key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        def _parse_round_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_code = _parse_round_code(d.pop("roundCode", UNSET))

        def _parse_round_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_number = _parse_round_number(d.pop("roundNumber", UNSET))

        def _parse_stage_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage_code = _parse_stage_code(d.pop("stageCode", UNSET))

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        def _parse_division_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                division_id_type_0 = UUID(data)

                return division_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        division_id = _parse_division_id(d.pop("divisionId", UNSET))

        def _parse_conference_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conference_id_type_0 = UUID(data)

                return conference_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        conference_id = _parse_conference_id(d.pop("conferenceId", UNSET))

        apply_to_all_standings = d.pop("applyToAllStandings", UNSET)

        _adjustment_group = d.pop("adjustmentGroup", UNSET)
        adjustment_group: Union[Unset, StandingAdjustmentPutBodyAdjustmentGroup]
        if isinstance(_adjustment_group, Unset):
            adjustment_group = UNSET
        else:
            adjustment_group = StandingAdjustmentPutBodyAdjustmentGroup(_adjustment_group)

        _adjustment_type = d.pop("adjustmentType", UNSET)
        adjustment_type: Union[Unset, StandingAdjustmentPutBodyAdjustmentType]
        if isinstance(_adjustment_type, Unset):
            adjustment_type = UNSET
        else:
            adjustment_type = StandingAdjustmentPutBodyAdjustmentType(_adjustment_type)

        _adjustment_field = d.pop("adjustmentField", UNSET)
        adjustment_field: Union[Unset, StandingAdjustmentPutBodyAdjustmentField]
        if isinstance(_adjustment_field, Unset):
            adjustment_field = UNSET
        else:
            adjustment_field = StandingAdjustmentPutBodyAdjustmentField(_adjustment_field)

        adjustment_value = d.pop("adjustmentValue", UNSET)

        reason_type = d.pop("reasonType", UNSET)

        def _parse_reason_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason_description = _parse_reason_description(d.pop("reasonDescription", UNSET))

        def _parse_grouping_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        grouping_key = _parse_grouping_key(d.pop("groupingKey", UNSET))

        standing_adjustment_put_body = cls(
            season_id=season_id,
            entity_id=entity_id,
            round_code=round_code,
            round_number=round_number,
            stage_code=stage_code,
            pool_code=pool_code,
            division_id=division_id,
            conference_id=conference_id,
            apply_to_all_standings=apply_to_all_standings,
            adjustment_group=adjustment_group,
            adjustment_type=adjustment_type,
            adjustment_field=adjustment_field,
            adjustment_value=adjustment_value,
            reason_type=reason_type,
            reason_description=reason_description,
            grouping_key=grouping_key,
        )

        return standing_adjustment_put_body
