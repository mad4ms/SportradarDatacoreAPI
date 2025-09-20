from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="StandingProgressionsInsertStandingProgressionsPostBody")


@_attrs_define
class StandingProgressionsInsertStandingProgressionsPostBody:
    """
    Attributes:
        season_id (UUID): The unique identifier of the season Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        standing_progression_id (Union[Unset, UUID]): The unique identifier of the progression Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name_local (Union[None, Unset, str]): The name of the standing progressions in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: Test season.
        name_latin (Union[None, Unset, str]): The name of the standing progressions in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: Test season.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        fixture_ids (Union[Unset, list[UUID]]):
    """

    season_id: UUID
    standing_progression_id: Union[Unset, UUID] = UNSET
    name_local: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    fixture_ids: Union[Unset, list[UUID]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id = str(self.season_id)

        standing_progression_id: Union[Unset, str] = UNSET
        if not isinstance(self.standing_progression_id, Unset):
            standing_progression_id = str(self.standing_progression_id)

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

        pool_code: Union[None, Unset, str]
        if isinstance(self.pool_code, Unset):
            pool_code = UNSET
        else:
            pool_code = self.pool_code

        fixture_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.fixture_ids, Unset):
            fixture_ids = []
            for fixture_ids_item_data in self.fixture_ids:
                fixture_ids_item = str(fixture_ids_item_data)
                fixture_ids.append(fixture_ids_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "seasonId": season_id,
            }
        )
        if standing_progression_id is not UNSET:
            field_dict["standingProgressionId"] = standing_progression_id
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if fixture_ids is not UNSET:
            field_dict["fixtureIds"] = fixture_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season_id = UUID(d.pop("seasonId"))

        _standing_progression_id = d.pop("standingProgressionId", UNSET)
        standing_progression_id: Union[Unset, UUID]
        if isinstance(_standing_progression_id, Unset):
            standing_progression_id = UNSET
        else:
            standing_progression_id = UUID(_standing_progression_id)

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

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        fixture_ids = []
        _fixture_ids = d.pop("fixtureIds", UNSET)
        for fixture_ids_item_data in _fixture_ids or []:
            fixture_ids_item = UUID(fixture_ids_item_data)

            fixture_ids.append(fixture_ids_item)

        standing_progressions_insert_standing_progressions_post_body = cls(
            season_id=season_id,
            standing_progression_id=standing_progression_id,
            name_local=name_local,
            name_latin=name_latin,
            stage_code=stage_code,
            pool_code=pool_code,
            fixture_ids=fixture_ids,
        )

        return standing_progressions_insert_standing_progressions_post_body
