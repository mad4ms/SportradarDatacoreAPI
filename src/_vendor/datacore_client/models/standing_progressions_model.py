import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.standing_progressions_model_organization import StandingProgressionsModelOrganization
    from ..models.standing_progressions_model_pool import StandingProgressionsModelPool
    from ..models.standing_progressions_model_season import StandingProgressionsModelSeason
    from ..models.standing_progressions_model_stage import StandingProgressionsModelStage


T = TypeVar("T", bound="StandingProgressionsModel")


@_attrs_define
class StandingProgressionsModel:
    """
    Attributes:
        standing_progression_id (Union[Unset, UUID]): The unique identifier of the progression Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, StandingProgressionsModelOrganization]): The organization that this standing
            progressions belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, StandingProgressionsModelSeason]): The season linked to this record
        name_local (Union[None, Unset, str]): The name of the standing progressions in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Test season.
        name_latin (Union[None, Unset, str]): The name of the standing progressions in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Test season.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        stage (Union[Unset, StandingProgressionsModelStage]): The stage that is related to this record
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        pool (Union[Unset, StandingProgressionsModelPool]): The pool that is related to this record
        fixture_ids (Union[Unset, list[UUID]]):
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    standing_progression_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "StandingProgressionsModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "StandingProgressionsModelSeason"] = UNSET
    name_local: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    stage: Union[Unset, "StandingProgressionsModelStage"] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    pool: Union[Unset, "StandingProgressionsModelPool"] = UNSET
    fixture_ids: Union[Unset, list[UUID]] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        standing_progression_id: Union[Unset, str] = UNSET
        if not isinstance(self.standing_progression_id, Unset):
            standing_progression_id = str(self.standing_progression_id)

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

        name_local: Union[None, Unset, str]
        if isinstance(self.name_local, Unset):
            name_local = UNSET
        else:
            name_local = self.name_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

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

        fixture_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fixture_ids, Unset):
            fixture_ids = []
            for fixture_ids_item_data in self.fixture_ids:
                fixture_ids_item = str(fixture_ids_item_data)
                fixture_ids.append(fixture_ids_item)

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if standing_progression_id is not UNSET:
            field_dict["standingProgressionId"] = standing_progression_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if stage is not UNSET:
            field_dict["stage"] = stage
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if pool is not UNSET:
            field_dict["pool"] = pool
        if fixture_ids is not UNSET:
            field_dict["fixtureIds"] = fixture_ids
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.standing_progressions_model_organization import StandingProgressionsModelOrganization
        from ..models.standing_progressions_model_pool import StandingProgressionsModelPool
        from ..models.standing_progressions_model_season import StandingProgressionsModelSeason
        from ..models.standing_progressions_model_stage import StandingProgressionsModelStage

        d = dict(src_dict)
        _standing_progression_id = d.pop("standingProgressionId", UNSET)
        standing_progression_id: Union[Unset, UUID]
        if isinstance(_standing_progression_id, Unset):
            standing_progression_id = UNSET
        else:
            standing_progression_id = UUID(_standing_progression_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, StandingProgressionsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = StandingProgressionsModelOrganization.from_dict(_organization)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, StandingProgressionsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = StandingProgressionsModelSeason.from_dict(_season)

        def _parse_name_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_local = _parse_name_local(d.pop("nameLocal", UNSET))

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_stage_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage_code = _parse_stage_code(d.pop("stageCode", UNSET))

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, StandingProgressionsModelStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = StandingProgressionsModelStage.from_dict(_stage)

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, StandingProgressionsModelPool]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = StandingProgressionsModelPool.from_dict(_pool)

        fixture_ids = []
        _fixture_ids = d.pop("fixtureIds", UNSET)
        for fixture_ids_item_data in _fixture_ids or []:
            fixture_ids_item = UUID(fixture_ids_item_data)

            fixture_ids.append(fixture_ids_item)

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

        standing_progressions_model = cls(
            standing_progression_id=standing_progression_id,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            name_local=name_local,
            name_latin=name_latin,
            stage_code=stage_code,
            stage=stage,
            pool_code=pool_code,
            pool=pool,
            fixture_ids=fixture_ids,
            updated=updated,
            added=added,
        )

        return standing_progressions_model
