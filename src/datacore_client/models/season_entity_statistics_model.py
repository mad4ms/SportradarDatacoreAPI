from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.season_entity_statistics_model_period_id import SeasonEntityStatisticsModelPeriodId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_entity_statistics_model_competition import SeasonEntityStatisticsModelCompetition
    from ..models.season_entity_statistics_model_entity import SeasonEntityStatisticsModelEntity
    from ..models.season_entity_statistics_model_organization import SeasonEntityStatisticsModelOrganization
    from ..models.season_entity_statistics_model_season import SeasonEntityStatisticsModelSeason
    from ..models.season_entity_statistics_model_statistics import SeasonEntityStatisticsModelStatistics


T = TypeVar("T", bound="SeasonEntityStatisticsModel")


@_attrs_define
class SeasonEntityStatisticsModel:
    """
    Attributes:
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, SeasonEntityStatisticsModelEntity]): The team information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonEntityStatisticsModelOrganization]): The organization that this season entity
            statistics belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonEntityStatisticsModelSeason]): The season linked to this record
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, SeasonEntityStatisticsModelCompetition]): The competition that this season belongs to
        period_id (Union[Unset, SeasonEntityStatisticsModelPeriodId]): The identifier for the period
            >- `1` Period 1
            >- `2` Period 2
            >- `10` Extra time 1 period 1
            >- `11` Extra time 1 period 2
            >- `12` Extra time 2 period 1
            >- `13` Extra time 2 period 2
            >- `14` Shoot Out
        statistics (Union[Unset, SeasonEntityStatisticsModelStatistics]):
    """

    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "SeasonEntityStatisticsModelEntity"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonEntityStatisticsModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonEntityStatisticsModelSeason"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "SeasonEntityStatisticsModelCompetition"] = UNSET
    period_id: Union[Unset, SeasonEntityStatisticsModelPeriodId] = UNSET
    statistics: Union[Unset, "SeasonEntityStatisticsModelStatistics"] = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        competition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        period_id: Union[Unset, int] = UNSET
        if not isinstance(self.period_id, Unset):
            period_id = self.period_id.value

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
        if period_id is not UNSET:
            field_dict["periodId"] = period_id
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_entity_statistics_model_competition import SeasonEntityStatisticsModelCompetition
        from ..models.season_entity_statistics_model_entity import SeasonEntityStatisticsModelEntity
        from ..models.season_entity_statistics_model_organization import SeasonEntityStatisticsModelOrganization
        from ..models.season_entity_statistics_model_season import SeasonEntityStatisticsModelSeason
        from ..models.season_entity_statistics_model_statistics import SeasonEntityStatisticsModelStatistics

        d = dict(src_dict)
        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, SeasonEntityStatisticsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = SeasonEntityStatisticsModelEntity.from_dict(_entity)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonEntityStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonEntityStatisticsModelOrganization.from_dict(_organization)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonEntityStatisticsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonEntityStatisticsModelSeason.from_dict(_season)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, SeasonEntityStatisticsModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = SeasonEntityStatisticsModelCompetition.from_dict(_competition)

        _period_id = d.pop("periodId", UNSET)
        period_id: Union[Unset, SeasonEntityStatisticsModelPeriodId]
        if isinstance(_period_id, Unset):
            period_id = UNSET
        else:
            period_id = SeasonEntityStatisticsModelPeriodId(_period_id)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SeasonEntityStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SeasonEntityStatisticsModelStatistics.from_dict(_statistics)

        season_entity_statistics_model = cls(
            entity_id=entity_id,
            entity=entity,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            competition_id=competition_id,
            competition=competition,
            period_id=period_id,
            statistics=statistics,
        )

        return season_entity_statistics_model
