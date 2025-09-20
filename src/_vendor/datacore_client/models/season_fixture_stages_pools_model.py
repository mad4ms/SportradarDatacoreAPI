from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.season_fixture_stages_pools_model_fixture_type import SeasonFixtureStagesPoolsModelFixtureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_fixture_stages_pools_model_organization import SeasonFixtureStagesPoolsModelOrganization
    from ..models.season_fixture_stages_pools_model_pool import SeasonFixtureStagesPoolsModelPool
    from ..models.season_fixture_stages_pools_model_season import SeasonFixtureStagesPoolsModelSeason
    from ..models.season_fixture_stages_pools_model_stage import SeasonFixtureStagesPoolsModelStage


T = TypeVar("T", bound="SeasonFixtureStagesPoolsModel")


@_attrs_define
class SeasonFixtureStagesPoolsModel:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonFixtureStagesPoolsModelSeason]): The season linked to this record
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonFixtureStagesPoolsModelOrganization]): The organization that this season
            fixture stages pools belongs to
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        stage (Union[Unset, SeasonFixtureStagesPoolsModelStage]): The stage that is related to this record
        pool_code (Union[Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        pool (Union[Unset, SeasonFixtureStagesPoolsModelPool]): The pool that is related to this record
        fixture_type (Union[Unset, SeasonFixtureStagesPoolsModelFixtureType]): Type of match
            >- `ALL_STAR` All Star
            >- `DEMONSTRATION` Demonstration
            >- `FINAL` Final
            >- `FRIENDLY` Friendly
            >- `PLAYOFF` Playoff
            >- `PRESEASON` Pre Season
            >- `REGULAR` Regular
             Example: REGULAR.
    """

    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonFixtureStagesPoolsModelSeason"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonFixtureStagesPoolsModelOrganization"] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    stage: Union[Unset, "SeasonFixtureStagesPoolsModelStage"] = UNSET
    pool_code: Union[Unset, str] = UNSET
    pool: Union[Unset, "SeasonFixtureStagesPoolsModelPool"] = UNSET
    fixture_type: Union[Unset, SeasonFixtureStagesPoolsModelFixtureType] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        stage_code: Union[None, Unset, str]
        if isinstance(self.stage_code, Unset):
            stage_code = UNSET
        else:
            stage_code = self.stage_code

        stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        pool_code = self.pool_code

        pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.to_dict()

        fixture_type: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_type, Unset):
            fixture_type = self.fixture_type.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if stage is not UNSET:
            field_dict["stage"] = stage
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if pool is not UNSET:
            field_dict["pool"] = pool
        if fixture_type is not UNSET:
            field_dict["fixtureType"] = fixture_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_fixture_stages_pools_model_organization import SeasonFixtureStagesPoolsModelOrganization
        from ..models.season_fixture_stages_pools_model_pool import SeasonFixtureStagesPoolsModelPool
        from ..models.season_fixture_stages_pools_model_season import SeasonFixtureStagesPoolsModelSeason
        from ..models.season_fixture_stages_pools_model_stage import SeasonFixtureStagesPoolsModelStage

        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonFixtureStagesPoolsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonFixtureStagesPoolsModelSeason.from_dict(_season)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonFixtureStagesPoolsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonFixtureStagesPoolsModelOrganization.from_dict(_organization)

        def _parse_stage_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage_code = _parse_stage_code(d.pop("stageCode", UNSET))

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, SeasonFixtureStagesPoolsModelStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = SeasonFixtureStagesPoolsModelStage.from_dict(_stage)

        pool_code = d.pop("poolCode", UNSET)

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, SeasonFixtureStagesPoolsModelPool]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = SeasonFixtureStagesPoolsModelPool.from_dict(_pool)

        _fixture_type = d.pop("fixtureType", UNSET)
        fixture_type: Union[Unset, SeasonFixtureStagesPoolsModelFixtureType]
        if isinstance(_fixture_type, Unset):
            fixture_type = UNSET
        else:
            fixture_type = SeasonFixtureStagesPoolsModelFixtureType(_fixture_type)

        season_fixture_stages_pools_model = cls(
            season_id=season_id,
            season=season,
            organization_id=organization_id,
            organization=organization,
            stage_code=stage_code,
            stage=stage,
            pool_code=pool_code,
            pool=pool,
            fixture_type=fixture_type,
        )

        return season_fixture_stages_pools_model
