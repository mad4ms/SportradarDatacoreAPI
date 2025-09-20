from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_person_statistics_model import SeasonPersonStatisticsModel


T = TypeVar("T", bound="SeasonLeaderSummaryModel")


@_attrs_define
class SeasonLeaderSummaryModel:
    """
    Attributes:
        stat_name (Union[Unset, list['SeasonPersonStatisticsModel']]): There will be an element/object here for each
            statistic you have requested. The 'statName' key will be the name of the statistics. eg `points`
    """

    stat_name: Union[Unset, list["SeasonPersonStatisticsModel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        stat_name: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.stat_name, Unset):
            stat_name = []
            for stat_name_item_data in self.stat_name:
                stat_name_item = stat_name_item_data.to_dict()
                stat_name.append(stat_name_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if stat_name is not UNSET:
            field_dict["statName"] = stat_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_person_statistics_model import SeasonPersonStatisticsModel

        d = dict(src_dict)
        stat_name = []
        _stat_name = d.pop("statName", UNSET)
        for stat_name_item_data in _stat_name or []:
            stat_name_item = SeasonPersonStatisticsModel.from_dict(stat_name_item_data)

            stat_name.append(stat_name_item)

        season_leader_summary_model = cls(
            stat_name=stat_name,
        )

        return season_leader_summary_model
