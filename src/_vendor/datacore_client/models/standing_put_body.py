from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.standing_put_body_fixture_type import StandingPutBodyFixtureType
from ..models.standing_put_body_grouping_base import StandingPutBodyGroupingBase
from ..models.standing_put_body_grouping_conference_division import StandingPutBodyGroupingConferenceDivision
from ..models.standing_put_body_grouping_stage_pool import StandingPutBodyGroupingStagePool
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_put_body_calculated import StandingPutBodyCalculated
    from ..models.standing_put_body_points import StandingPutBodyPoints


T = TypeVar("T", bound="StandingPutBody")


@_attrs_define
class StandingPutBody:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        latest (Union[Unset, bool]): Standing is part of the latest round? Example: True.
        in_progress (Union[Unset, bool]): Is the competitor in a current In-Progress match? Example: True.
        live (Union[Unset, bool]): Is this including live matches? Example: True.
        locked (Union[Unset, bool]): Has the standing been locked (to prevent editing)? Example: True.
        grouping_base (Union[Unset, StandingPutBodyGroupingBase]): Base grouping of standings row
            >- `OVERALL` Overall
            >- `ROUND` Round
             Example: OVERALL.
        grouping_conference_division (Union[Unset, StandingPutBodyGroupingConferenceDivision]): Conference/Division
            grouping of standings row
            >- `CONFERENCE` Conference
            >- `DIVISION` Division
            >- `OVERALL` Overall
             Example: OVERALL.
        grouping_stage_pool (Union[Unset, StandingPutBodyGroupingStagePool]): Stage/Pool grouping of standings row
            >- `OVERALL` Overall
            >- `STAGE` Stage
            >- `STAGEPOOL` Stage/Pool
             Example: OVERALL.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        round_code (Union[None, Unset, str]): A unique code for the round. (Unique for season) Example: RN1.
        round_number (Union[None, Unset, str]): The number given to the round Example: 1.
        standing_configuration_id (Union[None, UUID, Unset]): The unique identifier of the ~standingConfiguration~
            Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_type (Union[Unset, StandingPutBodyFixtureType]): Type of match
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
        points (Union[Unset, StandingPutBodyPoints]): standings points fields
        calculated (Union[Unset, StandingPutBodyCalculated]): standings points fields
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    season_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    latest: Union[Unset, bool] = UNSET
    in_progress: Union[Unset, bool] = UNSET
    live: Union[Unset, bool] = UNSET
    locked: Union[Unset, bool] = UNSET
    grouping_base: Union[Unset, StandingPutBodyGroupingBase] = UNSET
    grouping_conference_division: Union[Unset, StandingPutBodyGroupingConferenceDivision] = UNSET
    grouping_stage_pool: Union[Unset, StandingPutBodyGroupingStagePool] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    round_code: Union[None, Unset, str] = UNSET
    round_number: Union[None, Unset, str] = UNSET
    standing_configuration_id: Union[None, UUID, Unset] = UNSET
    fixture_type: Union[Unset, StandingPutBodyFixtureType] = UNSET
    position: Union[None, Unset, int] = UNSET
    secured_finals: Union[Unset, str] = UNSET
    points: Union[Unset, "StandingPutBodyPoints"] = UNSET
    calculated: Union[Unset, "StandingPutBodyCalculated"] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

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

        pool_code: Union[None, Unset, str]
        if isinstance(self.pool_code, Unset):
            pool_code = UNSET
        else:
            pool_code = self.pool_code

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

        standing_configuration_id: Union[None, Unset, str]
        if isinstance(self.standing_configuration_id, Unset):
            standing_configuration_id = UNSET
        elif isinstance(self.standing_configuration_id, UUID):
            standing_configuration_id = str(self.standing_configuration_id)
        else:
            standing_configuration_id = self.standing_configuration_id

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
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
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if round_code is not UNSET:
            field_dict["roundCode"] = round_code
        if round_number is not UNSET:
            field_dict["roundNumber"] = round_number
        if standing_configuration_id is not UNSET:
            field_dict["standingConfigurationId"] = standing_configuration_id
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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_put_body_calculated import StandingPutBodyCalculated
        from ..models.standing_put_body_points import StandingPutBodyPoints

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

        latest = d.pop("latest", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        live = d.pop("live", UNSET)

        locked = d.pop("locked", UNSET)

        _grouping_base = d.pop("groupingBase", UNSET)
        grouping_base: Union[Unset, StandingPutBodyGroupingBase]
        if isinstance(_grouping_base, Unset):
            grouping_base = UNSET
        else:
            grouping_base = StandingPutBodyGroupingBase(_grouping_base)

        _grouping_conference_division = d.pop("groupingConferenceDivision", UNSET)
        grouping_conference_division: Union[Unset, StandingPutBodyGroupingConferenceDivision]
        if isinstance(_grouping_conference_division, Unset):
            grouping_conference_division = UNSET
        else:
            grouping_conference_division = StandingPutBodyGroupingConferenceDivision(_grouping_conference_division)

        _grouping_stage_pool = d.pop("groupingStagePool", UNSET)
        grouping_stage_pool: Union[Unset, StandingPutBodyGroupingStagePool]
        if isinstance(_grouping_stage_pool, Unset):
            grouping_stage_pool = UNSET
        else:
            grouping_stage_pool = StandingPutBodyGroupingStagePool(_grouping_stage_pool)

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

        standing_configuration_id = _parse_standing_configuration_id(d.pop("standingConfigurationId", UNSET))

        _fixture_type = d.pop("fixtureType", UNSET)
        fixture_type: Union[Unset, StandingPutBodyFixtureType]
        if isinstance(_fixture_type, Unset):
            fixture_type = UNSET
        else:
            fixture_type = StandingPutBodyFixtureType(_fixture_type)

        def _parse_position(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position = _parse_position(d.pop("position", UNSET))

        secured_finals = d.pop("securedFinals", UNSET)

        _points = d.pop("points", UNSET)
        points: Union[Unset, StandingPutBodyPoints]
        if isinstance(_points, Unset):
            points = UNSET
        else:
            points = StandingPutBodyPoints.from_dict(_points)

        _calculated = d.pop("calculated", UNSET)
        calculated: Union[Unset, StandingPutBodyCalculated]
        if isinstance(_calculated, Unset):
            calculated = UNSET
        else:
            calculated = StandingPutBodyCalculated.from_dict(_calculated)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        standing_put_body = cls(
            season_id=season_id,
            entity_id=entity_id,
            division_id=division_id,
            conference_id=conference_id,
            latest=latest,
            in_progress=in_progress,
            live=live,
            locked=locked,
            grouping_base=grouping_base,
            grouping_conference_division=grouping_conference_division,
            grouping_stage_pool=grouping_stage_pool,
            stage_code=stage_code,
            pool_code=pool_code,
            round_code=round_code,
            round_number=round_number,
            standing_configuration_id=standing_configuration_id,
            fixture_type=fixture_type,
            position=position,
            secured_finals=secured_finals,
            points=points,
            calculated=calculated,
            external_id=external_id,
        )

        return standing_put_body
