from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SEASONTEAMPlacingsPutBody")


@_attrs_define
class SEASONTEAMPlacingsPutBody:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        result_place (Union[Unset, int]): Result place Example: 1.
        points (Union[None, Unset, int]): Points awarded Example: 1.
        prize_money (Union[None, Unset, int]): Prize money awarded Example: 1.
    """

    season_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    result_place: Union[Unset, int] = UNSET
    points: Union[None, Unset, int] = UNSET
    prize_money: Union[None, Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        result_place = self.result_place

        points: Union[None, Unset, int]
        if isinstance(self.points, Unset):
            points = UNSET
        else:
            points = self.points

        prize_money: Union[None, Unset, int]
        if isinstance(self.prize_money, Unset):
            prize_money = UNSET
        else:
            prize_money = self.prize_money

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if result_place is not UNSET:
            field_dict["resultPlace"] = result_place
        if points is not UNSET:
            field_dict["points"] = points
        if prize_money is not UNSET:
            field_dict["prizeMoney"] = prize_money

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

        result_place = d.pop("resultPlace", UNSET)

        def _parse_points(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        points = _parse_points(d.pop("points", UNSET))

        def _parse_prize_money(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        prize_money = _parse_prize_money(d.pop("prizeMoney", UNSET))

        seasonteam_placings_put_body = cls(
            season_id=season_id,
            entity_id=entity_id,
            result_place=result_place,
            points=points,
            prize_money=prize_money,
        )

        return seasonteam_placings_put_body
