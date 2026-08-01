from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_entity_statistics_model_competition import CompetitionEntityStatisticsModelCompetition
    from ..models.competition_entity_statistics_model_entity import CompetitionEntityStatisticsModelEntity
    from ..models.competition_entity_statistics_model_organization import CompetitionEntityStatisticsModelOrganization
    from ..models.competition_entity_statistics_model_statistics import CompetitionEntityStatisticsModelStatistics


T = TypeVar("T", bound="CompetitionEntityStatisticsModel")


@_attrs_define
class CompetitionEntityStatisticsModel:
    """
    Attributes:
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, CompetitionEntityStatisticsModelEntity]): The team information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, CompetitionEntityStatisticsModelOrganization]): The organization that this
            competition entity statistics belongs to
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, CompetitionEntityStatisticsModelCompetition]): The competition that this season
            belongs to
        statistics (Union[Unset, CompetitionEntityStatisticsModelStatistics]):
    """

    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "CompetitionEntityStatisticsModelEntity"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "CompetitionEntityStatisticsModelOrganization"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "CompetitionEntityStatisticsModelCompetition"] = UNSET
    statistics: Union[Unset, "CompetitionEntityStatisticsModelStatistics"] = UNSET

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

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        competition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

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
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competition_entity_statistics_model_competition import CompetitionEntityStatisticsModelCompetition
        from ..models.competition_entity_statistics_model_entity import CompetitionEntityStatisticsModelEntity
        from ..models.competition_entity_statistics_model_organization import (
            CompetitionEntityStatisticsModelOrganization,
        )
        from ..models.competition_entity_statistics_model_statistics import CompetitionEntityStatisticsModelStatistics

        d = dict(src_dict)
        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, CompetitionEntityStatisticsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = CompetitionEntityStatisticsModelEntity.from_dict(_entity)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, CompetitionEntityStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CompetitionEntityStatisticsModelOrganization.from_dict(_organization)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, CompetitionEntityStatisticsModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = CompetitionEntityStatisticsModelCompetition.from_dict(_competition)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CompetitionEntityStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CompetitionEntityStatisticsModelStatistics.from_dict(_statistics)

        competition_entity_statistics_model = cls(
            entity_id=entity_id,
            entity=entity,
            organization_id=organization_id,
            organization=organization,
            competition_id=competition_id,
            competition=competition,
            statistics=statistics,
        )

        return competition_entity_statistics_model
