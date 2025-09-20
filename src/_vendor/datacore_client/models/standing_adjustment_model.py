import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.standing_adjustment_model_adjustment_field import StandingAdjustmentModelAdjustmentField
from ..models.standing_adjustment_model_adjustment_group import StandingAdjustmentModelAdjustmentGroup
from ..models.standing_adjustment_model_adjustment_type import StandingAdjustmentModelAdjustmentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_adjustment_model_conference import StandingAdjustmentModelConference
    from ..models.standing_adjustment_model_division import StandingAdjustmentModelDivision
    from ..models.standing_adjustment_model_entity import StandingAdjustmentModelEntity
    from ..models.standing_adjustment_model_organization import StandingAdjustmentModelOrganization
    from ..models.standing_adjustment_model_pool import StandingAdjustmentModelPool
    from ..models.standing_adjustment_model_round import StandingAdjustmentModelRound
    from ..models.standing_adjustment_model_season import StandingAdjustmentModelSeason
    from ..models.standing_adjustment_model_stage import StandingAdjustmentModelStage


T = TypeVar("T", bound="StandingAdjustmentModel")


@_attrs_define
class StandingAdjustmentModel:
    """
    Attributes:
        standing_adjustment_id (Union[Unset, UUID]): The unique identifier of the adjustment Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, StandingAdjustmentModelSeason]): The season linked to this record
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, StandingAdjustmentModelEntity]): The team information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, StandingAdjustmentModelOrganization]): The organization that this
            ~standing_adjustment~ belongs to
        round_code (Union[None, Unset, str]): A unique code for the round. (Unique for season) Example: RN1.
        round_ (Union[Unset, StandingAdjustmentModelRound]): The ~ROUND~ that is related to this record
        round_number (Union[None, Unset, str]): The number given to the round Example: 1.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        stage (Union[Unset, StandingAdjustmentModelStage]): The stage that is related to this record
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        pool (Union[Unset, StandingAdjustmentModelPool]): The pool that is related to this record
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division (Union[Unset, StandingAdjustmentModelDivision]): The division information
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference (Union[Unset, StandingAdjustmentModelConference]): The conference information
        apply_to_all_standings (Union[Unset, bool]): Apply to all generated standing types ? Example: True.
        adjustment_group (Union[Unset, StandingAdjustmentModelAdjustmentGroup]): Adjustment Group
            >- `IN_CONFERENCE` In Conference
            >- `IN_DIVISION` In Division
            >- `OUT_CONFERENCE` Out Conference
            >- `OUT_DIVISION` Out Division
            >- `OVERALL` Overall
        adjustment_type (Union[Unset, StandingAdjustmentModelAdjustmentType]): Adjustment Type
            >- `ADD_MINUS` Add/Subtract Value
            >- `SET` Set Value
        adjustment_field (Union[Unset, StandingAdjustmentModelAdjustmentField]): Adjustment field to calculate standings
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
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    standing_adjustment_id: Union[Unset, UUID] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "StandingAdjustmentModelSeason"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "StandingAdjustmentModelEntity"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "StandingAdjustmentModelOrganization"] = UNSET
    round_code: Union[None, Unset, str] = UNSET
    round_: Union[Unset, "StandingAdjustmentModelRound"] = UNSET
    round_number: Union[None, Unset, str] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    stage: Union[Unset, "StandingAdjustmentModelStage"] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    pool: Union[Unset, "StandingAdjustmentModelPool"] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    division: Union[Unset, "StandingAdjustmentModelDivision"] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    conference: Union[Unset, "StandingAdjustmentModelConference"] = UNSET
    apply_to_all_standings: Union[Unset, bool] = UNSET
    adjustment_group: Union[Unset, StandingAdjustmentModelAdjustmentGroup] = UNSET
    adjustment_type: Union[Unset, StandingAdjustmentModelAdjustmentType] = UNSET
    adjustment_field: Union[Unset, StandingAdjustmentModelAdjustmentField] = UNSET
    adjustment_value: Union[Unset, float] = UNSET
    reason_type: Union[Unset, str] = UNSET
    reason_description: Union[None, Unset, str] = UNSET
    grouping_key: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        standing_adjustment_id: Union[Unset, str] = UNSET
        if not isinstance(self.standing_adjustment_id, Unset):
            standing_adjustment_id = str(self.standing_adjustment_id)

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        round_code: Union[None, Unset, str]
        if isinstance(self.round_code, Unset):
            round_code = UNSET
        else:
            round_code = self.round_code

        round_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.round_, Unset):
            round_ = self.round_.to_dict()

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

        stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        pool_code: Union[None, Unset, str]
        if isinstance(self.pool_code, Unset):
            pool_code = UNSET
        else:
            pool_code = self.pool_code

        pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.to_dict()

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        division: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.to_dict()

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        conference: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conference, Unset):
            conference = self.conference.to_dict()

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

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if standing_adjustment_id is not UNSET:
            field_dict["standingAdjustmentId"] = standing_adjustment_id
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if round_code is not UNSET:
            field_dict["roundCode"] = round_code
        if round_ is not UNSET:
            field_dict["round"] = round_
        if round_number is not UNSET:
            field_dict["roundNumber"] = round_number
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if stage is not UNSET:
            field_dict["stage"] = stage
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if pool is not UNSET:
            field_dict["pool"] = pool
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if division is not UNSET:
            field_dict["division"] = division
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if conference is not UNSET:
            field_dict["conference"] = conference
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
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_adjustment_model_conference import StandingAdjustmentModelConference
        from ..models.standing_adjustment_model_division import StandingAdjustmentModelDivision
        from ..models.standing_adjustment_model_entity import StandingAdjustmentModelEntity
        from ..models.standing_adjustment_model_organization import StandingAdjustmentModelOrganization
        from ..models.standing_adjustment_model_pool import StandingAdjustmentModelPool
        from ..models.standing_adjustment_model_round import StandingAdjustmentModelRound
        from ..models.standing_adjustment_model_season import StandingAdjustmentModelSeason
        from ..models.standing_adjustment_model_stage import StandingAdjustmentModelStage

        d = dict(src_dict)
        _standing_adjustment_id = d.pop("standingAdjustmentId", UNSET)
        standing_adjustment_id: Union[Unset, UUID]
        if isinstance(_standing_adjustment_id, Unset):
            standing_adjustment_id = UNSET
        else:
            standing_adjustment_id = UUID(_standing_adjustment_id)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, StandingAdjustmentModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = StandingAdjustmentModelSeason.from_dict(_season)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, StandingAdjustmentModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = StandingAdjustmentModelEntity.from_dict(_entity)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, StandingAdjustmentModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = StandingAdjustmentModelOrganization.from_dict(_organization)

        def _parse_round_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_code = _parse_round_code(d.pop("roundCode", UNSET))

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, StandingAdjustmentModelRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = StandingAdjustmentModelRound.from_dict(_round_)

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

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, StandingAdjustmentModelStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = StandingAdjustmentModelStage.from_dict(_stage)

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, StandingAdjustmentModelPool]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = StandingAdjustmentModelPool.from_dict(_pool)

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

        _division = d.pop("division", UNSET)
        division: Union[Unset, StandingAdjustmentModelDivision]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = StandingAdjustmentModelDivision.from_dict(_division)

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

        _conference = d.pop("conference", UNSET)
        conference: Union[Unset, StandingAdjustmentModelConference]
        if isinstance(_conference, Unset):
            conference = UNSET
        else:
            conference = StandingAdjustmentModelConference.from_dict(_conference)

        apply_to_all_standings = d.pop("applyToAllStandings", UNSET)

        _adjustment_group = d.pop("adjustmentGroup", UNSET)
        adjustment_group: Union[Unset, StandingAdjustmentModelAdjustmentGroup]
        if isinstance(_adjustment_group, Unset):
            adjustment_group = UNSET
        else:
            adjustment_group = StandingAdjustmentModelAdjustmentGroup(_adjustment_group)

        _adjustment_type = d.pop("adjustmentType", UNSET)
        adjustment_type: Union[Unset, StandingAdjustmentModelAdjustmentType]
        if isinstance(_adjustment_type, Unset):
            adjustment_type = UNSET
        else:
            adjustment_type = StandingAdjustmentModelAdjustmentType(_adjustment_type)

        _adjustment_field = d.pop("adjustmentField", UNSET)
        adjustment_field: Union[Unset, StandingAdjustmentModelAdjustmentField]
        if isinstance(_adjustment_field, Unset):
            adjustment_field = UNSET
        else:
            adjustment_field = StandingAdjustmentModelAdjustmentField(_adjustment_field)

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

        standing_adjustment_model = cls(
            standing_adjustment_id=standing_adjustment_id,
            season_id=season_id,
            season=season,
            entity_id=entity_id,
            entity=entity,
            organization_id=organization_id,
            organization=organization,
            round_code=round_code,
            round_=round_,
            round_number=round_number,
            stage_code=stage_code,
            stage=stage,
            pool_code=pool_code,
            pool=pool,
            division_id=division_id,
            division=division,
            conference_id=conference_id,
            conference=conference,
            apply_to_all_standings=apply_to_all_standings,
            adjustment_group=adjustment_group,
            adjustment_type=adjustment_type,
            adjustment_field=adjustment_field,
            adjustment_value=adjustment_value,
            reason_type=reason_type,
            reason_description=reason_description,
            grouping_key=grouping_key,
            updated=updated,
            added=added,
        )

        return standing_adjustment_model
