import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.standing_model_fixture_type import StandingModelFixtureType
from ..models.standing_model_grouping_base import StandingModelGroupingBase
from ..models.standing_model_grouping_conference_division import (
    StandingModelGroupingConferenceDivision,
)
from ..models.standing_model_grouping_stage_pool import StandingModelGroupingStagePool
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_model_calculated import StandingModelCalculated
    from ..models.standing_model_conference import StandingModelConference
    from ..models.standing_model_division import StandingModelDivision
    from ..models.standing_model_entity import StandingModelEntity
    from ..models.standing_model_organization import StandingModelOrganization
    from ..models.standing_model_points import StandingModelPoints
    from ..models.standing_model_pool import StandingModelPool
    from ..models.standing_model_round import StandingModelRound
    from ..models.standing_model_season import StandingModelSeason
    from ..models.standing_model_stage import StandingModelStage
    from ..models.standing_model_standing_configuration import (
        StandingModelStandingConfiguration,
    )


T = TypeVar("T", bound="StandingModel")


@_attrs_define
class StandingModel:
    """
    Attributes:
        standing_id (Union[Unset, UUID]): The unique identifier of the standing Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, StandingModelOrganization]): The organization that this standing belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, StandingModelSeason]): The season linked to this record
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, StandingModelEntity]): The team information
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division (Union[Unset, StandingModelDivision]): The division information
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference (Union[Unset, StandingModelConference]): The conference information
        latest (Union[Unset, bool]): Standing is part of the latest round? Example: True.
        in_progress (Union[Unset, bool]): Is the competitor in a current In-Progress match? Example: True.
        live (Union[Unset, bool]): Is this including live matches? Example: True.
        locked (Union[Unset, bool]): Has the standing been locked (to prevent editing)? Example: True.
        grouping_base (Union[Unset, StandingModelGroupingBase]): Base grouping of standings row
            >- `OVERALL` Overall
            >- `ROUND` Round
             Example: OVERALL.
        grouping_conference_division (Union[Unset, StandingModelGroupingConferenceDivision]): Conference/Division
            grouping of standings row
            >- `CONFERENCE` Conference
            >- `DIVISION` Division
            >- `OVERALL` Overall
             Example: OVERALL.
        grouping_stage_pool (Union[Unset, StandingModelGroupingStagePool]): Stage/Pool grouping of standings row
            >- `OVERALL` Overall
            >- `STAGE` Stage
            >- `STAGEPOOL` Stage/Pool
             Example: OVERALL.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        stage (Union[Unset, StandingModelStage]): The stage that is related to this record
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        pool (Union[Unset, StandingModelPool]): The pool that is related to this record
        round_code (Union[None, Unset, str]): A unique code for the round. (Unique for season) Example: RN1.
        round_ (Union[Unset, StandingModelRound]): The ~ROUND~ that is related to this record
        round_number (Union[None, Unset, str]): The number given to the round Example: 1.
        standing_configuration_id (Union[None, UUID, Unset]): The unique identifier of the ~standingConfiguration~
            Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        standing_configuration (Union[Unset, StandingModelStandingConfiguration]): The ~standingConfiguration~ that this
            season belongs to
        fixture_type (Union[Unset, StandingModelFixtureType]): Type of match
            >- `ALL_STAR` All Star
            >- `DEMONSTRATION` Demonstration
            >- `FINAL` Final
            >- `FRIENDLY` Friendly
            >- `PLAYOFF` Playoff
            >- `PRESEASON` Pre Season
            >- `REGULAR` Regular
             Example: REGULAR.
        position (Union[None, Unset, int]): Position of the competitors standing record Example: 48.
        secured_finals (Union[Unset, str]): Has competitor secured a finals position
        points (Union[Unset, StandingModelPoints]): standings points fields
        calculated (Union[Unset, StandingModelCalculated]): standings points fields
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        auto_generated (Union[Unset, bool]): Was this row auto generated? Example: True.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    standing_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "StandingModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "StandingModelSeason"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "StandingModelEntity"] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    division: Union[Unset, "StandingModelDivision"] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    conference: Union[Unset, "StandingModelConference"] = UNSET
    latest: Union[Unset, bool] = UNSET
    in_progress: Union[Unset, bool] = UNSET
    live: Union[Unset, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    grouping_base: Union[Unset, StandingModelGroupingBase] = UNSET
    grouping_conference_division: Union[
        Unset, StandingModelGroupingConferenceDivision
    ] = UNSET
    grouping_stage_pool: Union[Unset, StandingModelGroupingStagePool] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    stage: Union[Unset, "StandingModelStage"] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    pool: Union[Unset, "StandingModelPool"] = UNSET
    round_code: Union[None, Unset, str] = UNSET
    round_: Union[Unset, "StandingModelRound"] = UNSET
    round_number: Union[None, Unset, str] = UNSET
    standing_configuration_id: Union[None, UUID, Unset] = UNSET
    standing_configuration: Union[Unset, "StandingModelStandingConfiguration"] = UNSET
    fixture_type: Union[Unset, StandingModelFixtureType] = UNSET
    position: Union[None, Unset, int] = UNSET
    secured_finals: Union[Unset, str] = UNSET
    points: Union[Unset, "StandingModelPoints"] = UNSET
    calculated: Union[Unset, "StandingModelCalculated"] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    auto_generated: Union[Unset, bool] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        standing_id: Union[Unset, str] = UNSET
        if not isinstance(self.standing_id, Unset):
            standing_id = str(self.standing_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

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

        latest = self.latest

        in_progress = self.in_progress

        live = self.live

        locked = self.locked

        grouping_base: Union[Unset, str] = UNSET
        if not isinstance(self.grouping_base, Unset):
            grouping_base = self.grouping_base.value

        grouping_conference_division: Union[Unset, str] = UNSET
        if not isinstance(self.grouping_conference_division, Unset):
            grouping_conference_division = self.grouping_conference_division.value

        grouping_stage_pool: Union[Unset, str] = UNSET
        if not isinstance(self.grouping_stage_pool, Unset):
            grouping_stage_pool = self.grouping_stage_pool.value

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

        standing_configuration_id: Union[None, Unset, str]
        if isinstance(self.standing_configuration_id, Unset):
            standing_configuration_id = UNSET
        elif isinstance(self.standing_configuration_id, UUID):
            standing_configuration_id = str(self.standing_configuration_id)
        else:
            standing_configuration_id = self.standing_configuration_id

        standing_configuration: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.standing_configuration, Unset):
            standing_configuration = self.standing_configuration.to_dict()

        fixture_type: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_type, Unset):
            fixture_type = self.fixture_type.value

        position: Union[None, Unset, int]
        if isinstance(self.position, Unset):
            position = UNSET
        else:
            position = self.position

        secured_finals = self.secured_finals

        points: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.points, Unset):
            points = self.points.to_dict()

        calculated: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.calculated, Unset):
            calculated = self.calculated.to_dict()

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        auto_generated = self.auto_generated

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if standing_id is not UNSET:
            field_dict["standingId"] = standing_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if division is not UNSET:
            field_dict["division"] = division
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if conference is not UNSET:
            field_dict["conference"] = conference
        if latest is not UNSET:
            field_dict["latest"] = latest
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if live is not UNSET:
            field_dict["live"] = live
        if locked is not UNSET:
            field_dict["locked"] = locked
        if grouping_base is not UNSET:
            field_dict["groupingBase"] = grouping_base
        if grouping_conference_division is not UNSET:
            field_dict["groupingConferenceDivision"] = grouping_conference_division
        if grouping_stage_pool is not UNSET:
            field_dict["groupingStagePool"] = grouping_stage_pool
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if stage is not UNSET:
            field_dict["stage"] = stage
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if pool is not UNSET:
            field_dict["pool"] = pool
        if round_code is not UNSET:
            field_dict["roundCode"] = round_code
        if round_ is not UNSET:
            field_dict["round"] = round_
        if round_number is not UNSET:
            field_dict["roundNumber"] = round_number
        if standing_configuration_id is not UNSET:
            field_dict["standingConfigurationId"] = standing_configuration_id
        if standing_configuration is not UNSET:
            field_dict["standingConfiguration"] = standing_configuration
        if fixture_type is not UNSET:
            field_dict["fixtureType"] = fixture_type
        if position is not UNSET:
            field_dict["position"] = position
        if secured_finals is not UNSET:
            field_dict["securedFinals"] = secured_finals
        if points is not UNSET:
            field_dict["points"] = points
        if calculated is not UNSET:
            field_dict["calculated"] = calculated
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if auto_generated is not UNSET:
            field_dict["autoGenerated"] = auto_generated
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_model_calculated import StandingModelCalculated
        from ..models.standing_model_conference import StandingModelConference
        from ..models.standing_model_division import StandingModelDivision
        from ..models.standing_model_entity import StandingModelEntity
        from ..models.standing_model_organization import StandingModelOrganization
        from ..models.standing_model_points import StandingModelPoints
        from ..models.standing_model_pool import StandingModelPool
        from ..models.standing_model_round import StandingModelRound
        from ..models.standing_model_season import StandingModelSeason
        from ..models.standing_model_stage import StandingModelStage
        from ..models.standing_model_standing_configuration import (
            StandingModelStandingConfiguration,
        )

        d = dict(src_dict)
        _standing_id = d.pop("standingId", UNSET)
        standing_id: Union[Unset, UUID]
        if isinstance(_standing_id, Unset):
            standing_id = UNSET
        else:
            standing_id = UUID(_standing_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, StandingModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = StandingModelOrganization.from_dict(_organization)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, StandingModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = StandingModelSeason.from_dict(_season)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, StandingModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = StandingModelEntity.from_dict(_entity)

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
        division: Union[Unset, StandingModelDivision]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = StandingModelDivision.from_dict(_division)

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
        conference: Union[Unset, StandingModelConference]
        if isinstance(_conference, Unset):
            conference = UNSET
        else:
            conference = StandingModelConference.from_dict(_conference)

        latest = d.pop("latest", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        live = d.pop("live", UNSET)

        locked = d.pop("locked", UNSET)

        _grouping_base = d.pop("groupingBase", UNSET)
        grouping_base: Union[Unset, StandingModelGroupingBase]
        if isinstance(_grouping_base, Unset):
            grouping_base = UNSET
        else:
            grouping_base = StandingModelGroupingBase(_grouping_base)

        _grouping_conference_division = d.pop("groupingConferenceDivision", UNSET)
        grouping_conference_division: Union[
            Unset, StandingModelGroupingConferenceDivision
        ]
        if isinstance(_grouping_conference_division, Unset):
            grouping_conference_division = UNSET
        else:
            grouping_conference_division = StandingModelGroupingConferenceDivision(
                _grouping_conference_division
            )

        _grouping_stage_pool = d.pop("groupingStagePool", UNSET)
        grouping_stage_pool: Union[Unset, StandingModelGroupingStagePool]
        if isinstance(_grouping_stage_pool, Unset):
            grouping_stage_pool = UNSET
        else:
            grouping_stage_pool = StandingModelGroupingStagePool(_grouping_stage_pool)

        def _parse_stage_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage_code = _parse_stage_code(d.pop("stageCode", UNSET))

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, StandingModelStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = StandingModelStage.from_dict(_stage)

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, StandingModelPool]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = StandingModelPool.from_dict(_pool)

        def _parse_round_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_code = _parse_round_code(d.pop("roundCode", UNSET))

        _round_ = d.pop("round", UNSET)
        round_: Union[Unset, StandingModelRound]
        if isinstance(_round_, Unset):
            round_ = UNSET
        else:
            round_ = StandingModelRound.from_dict(_round_)

        def _parse_round_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        round_number = _parse_round_number(d.pop("roundNumber", UNSET))

        def _parse_standing_configuration_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                standing_configuration_id_type_0 = UUID(data)

                return standing_configuration_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        standing_configuration_id = _parse_standing_configuration_id(
            d.pop("standingConfigurationId", UNSET)
        )

        _standing_configuration = d.pop("standingConfiguration", UNSET)
        standing_configuration: Union[Unset, StandingModelStandingConfiguration]
        if isinstance(_standing_configuration, Unset):
            standing_configuration = UNSET
        else:
            standing_configuration = StandingModelStandingConfiguration.from_dict(
                _standing_configuration
            )

        _fixture_type = d.pop("fixtureType", UNSET)
        fixture_type: Union[Unset, StandingModelFixtureType]
        if isinstance(_fixture_type, Unset):
            fixture_type = UNSET
        else:
            fixture_type = StandingModelFixtureType(_fixture_type)

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        secured_finals = d.pop("securedFinals", UNSET)

        _points = d.pop("points", UNSET)
        points: Union[Unset, StandingModelPoints]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = StandingModelPoints.from_dict(_points)

        _calculated = d.pop("calculated", UNSET)
        calculated: Union[Unset, StandingModelCalculated]
        if isinstance(_calculated, Unset):
            calculated = UNSET
        else:
            calculated = StandingModelCalculated.from_dict(_calculated)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        auto_generated = d.pop("autoGenerated", UNSET)

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

        standing_model = cls(
            standing_id=standing_id,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            entity_id=entity_id,
            entity=entity,
            division_id=division_id,
            division=division,
            conference_id=conference_id,
            conference=conference,
            latest=latest,
            in_progress=in_progress,
            live=live,
            locked=locked,
            grouping_base=grouping_base,
            grouping_conference_division=grouping_conference_division,
            grouping_stage_pool=grouping_stage_pool,
            stage_code=stage_code,
            stage=stage,
            pool_code=pool_code,
            pool=pool,
            round_code=round_code,
            round_=round_,
            round_number=round_number,
            standing_configuration_id=standing_configuration_id,
            standing_configuration=standing_configuration,
            fixture_type=fixture_type,
            position=position,
            secured_finals=secured_finals,
            points=points,
            calculated=calculated,
            external_id=external_id,
            auto_generated=auto_generated,
            updated=updated,
            added=added,
        )

        return standing_model
