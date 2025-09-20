from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.fps_insert_update_match_person_statistics_post_body_position_type_1 import (
    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType1,
)
from ..models.fps_insert_update_match_person_statistics_post_body_position_type_2_type_1 import (
    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType2Type1,
)
from ..models.fps_insert_update_match_person_statistics_post_body_position_type_3_type_1 import (
    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fps_insert_update_match_person_statistics_post_body_statistics import (
        FpsInsertUpdateMatchPersonStatisticsPostBodyStatistics,
    )


T = TypeVar("T", bound="FpsInsertUpdateMatchPersonStatisticsPostBody")


@_attrs_define
class FpsInsertUpdateMatchPersonStatisticsPostBody:
    """
    Attributes:
        person_id (UUID): The unique identifier of the person Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[None, UUID, Unset]): The unique identifier of the team Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        statistics (Union[Unset, FpsInsertUpdateMatchPersonStatisticsPostBodyStatistics]):
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        position (Union[FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType1,
            FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType2Type1,
            FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType3Type1, None, Unset]): Playing position
            >- None None
            >- `CB` Center Backcourt
            >- `D` Defensive Specialist
            >- `G` Goalkeeper
            >- `LB` Left Backcourt
            >- `LW` Left Wingman
            >- `P` Pivot
            >- `RB` Right Backcourt
            >- `RW` Right Wingman
             Example: G.
        did_not_play_reason (Union[None, Unset, str]): The reason the player didn't play Example: COACHES_DECISION.
        starter (Union[Unset, bool]):  Example: True.
        participated (Union[Unset, bool]): Did the person actually participate in the the match Example: True.
        is_player (Union[Unset, bool]): Is this person a player Example: True.
        is_team_official (Union[Unset, bool]): Is this person a team official Example: True.
    """

    person_id: UUID
    fixture_id: UUID
    entity_id: Union[None, UUID, Unset] = UNSET
    statistics: Union[
        Unset, "FpsInsertUpdateMatchPersonStatisticsPostBodyStatistics"
    ] = UNSET
    bib: Union[None, Unset, str] = UNSET
    position: Union[
        FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType1,
        FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType2Type1,
        FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType3Type1,
        None,
        Unset,
    ] = UNSET
    did_not_play_reason: Union[None, Unset, str] = UNSET
    starter: Union[Unset, bool] = UNSET
    participated: Union[Unset, bool] = UNSET
    is_player: Union[Unset, bool] = UNSET
    is_team_official: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        person_id = str(self.person_id)

        fixture_id = str(self.fixture_id)

        entity_id: Union[None, Unset, str]
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        bib: Union[None, Unset, str]
        if isinstance(self.bib, Unset):
            bib = UNSET
        else:
            bib = self.bib

        position: Union[None, Unset, str]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(
            self.position, FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType1
        ):
            position = self.position.value
        elif isinstance(
            self.position,
            FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType2Type1,
        ):
            position = self.position.value
        elif isinstance(
            self.position,
            FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType3Type1,
        ):
            position = self.position.value
        else:
            position = self.position

        did_not_play_reason: Union[None, Unset, str]
        if isinstance(self.did_not_play_reason, Unset):
            did_not_play_reason = UNSET
        else:
            did_not_play_reason = self.did_not_play_reason

        starter = self.starter

        participated = self.participated

        is_player = self.is_player

        is_team_official = self.is_team_official

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "personId": person_id,
                "fixtureId": fixture_id,
            }
        )
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if bib is not UNSET:
            field_dict["bib"] = bib
        if position is not UNSET:
            field_dict["position"] = position
        if did_not_play_reason is not UNSET:
            field_dict["didNotPlayReason"] = did_not_play_reason
        if starter is not UNSET:
            field_dict["starter"] = starter
        if participated is not UNSET:
            field_dict["participated"] = participated
        if is_player is not UNSET:
            field_dict["isPlayer"] = is_player
        if is_team_official is not UNSET:
            field_dict["isTeamOfficial"] = is_team_official

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fps_insert_update_match_person_statistics_post_body_statistics import (
            FpsInsertUpdateMatchPersonStatisticsPostBodyStatistics,
        )

        d = dict(src_dict)
        person_id = UUID(d.pop("personId"))

        fixture_id = UUID(d.pop("fixtureId"))

        def _parse_entity_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_id_type_0 = UUID(data)

                return entity_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        entity_id = _parse_entity_id(d.pop("entityId", UNSET))

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, FpsInsertUpdateMatchPersonStatisticsPostBodyStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = (
                FpsInsertUpdateMatchPersonStatisticsPostBodyStatistics.from_dict(
                    _statistics
                )
            )

        def _parse_bib(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bib = _parse_bib(d.pop("bib", UNSET))

        def _parse_position(
            data: object,
        ) -> Union[
            FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType1,
            FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType2Type1,
            FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_1 = (
                    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType1(data)
                )

                return position_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_2_type_1 = (
                    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType2Type1(data)
                )

                return position_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_3_type_1 = (
                    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType3Type1(data)
                )

                return position_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType1,
                    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType2Type1,
                    FpsInsertUpdateMatchPersonStatisticsPostBodyPositionType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        position = _parse_position(d.pop("position", UNSET))

        def _parse_did_not_play_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        did_not_play_reason = _parse_did_not_play_reason(
            d.pop("didNotPlayReason", UNSET)
        )

        starter = d.pop("starter", UNSET)

        participated = d.pop("participated", UNSET)

        is_player = d.pop("isPlayer", UNSET)

        is_team_official = d.pop("isTeamOfficial", UNSET)

        fps_insert_update_match_person_statistics_post_body = cls(
            person_id=person_id,
            fixture_id=fixture_id,
            entity_id=entity_id,
            statistics=statistics,
            bib=bib,
            position=position,
            did_not_play_reason=did_not_play_reason,
            starter=starter,
            participated=participated,
            is_player=is_player,
            is_team_official=is_team_official,
        )

        return fps_insert_update_match_person_statistics_post_body
