from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.career_person_season_statistics_model_entity import (
        CareerPersonSeasonStatisticsModelEntity,
    )
    from ..models.career_person_season_statistics_model_organization import (
        CareerPersonSeasonStatisticsModelOrganization,
    )
    from ..models.career_person_season_statistics_model_person import (
        CareerPersonSeasonStatisticsModelPerson,
    )
    from ..models.career_person_season_statistics_model_season import (
        CareerPersonSeasonStatisticsModelSeason,
    )
    from ..models.career_person_season_statistics_model_statistics import (
        CareerPersonSeasonStatisticsModelStatistics,
    )


T = TypeVar("T", bound="CareerPersonSeasonStatisticsModel")


@_attrs_define
class CareerPersonSeasonStatisticsModel:
    """
    Attributes:
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, CareerPersonSeasonStatisticsModelPerson]): The person information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, CareerPersonSeasonStatisticsModelOrganization]): The organization that this career
            person season statistics belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, CareerPersonSeasonStatisticsModelSeason]): The season linked to this record
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, CareerPersonSeasonStatisticsModelEntity]): The team information
        statistics (Union[Unset, CareerPersonSeasonStatisticsModelStatistics]):
    """

    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "CareerPersonSeasonStatisticsModelPerson"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "CareerPersonSeasonStatisticsModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "CareerPersonSeasonStatisticsModelSeason"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "CareerPersonSeasonStatisticsModelEntity"] = UNSET
    statistics: Union[Unset, "CareerPersonSeasonStatisticsModelStatistics"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        person: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

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

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
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
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.career_person_season_statistics_model_entity import (
            CareerPersonSeasonStatisticsModelEntity,
        )
        from ..models.career_person_season_statistics_model_organization import (
            CareerPersonSeasonStatisticsModelOrganization,
        )
        from ..models.career_person_season_statistics_model_person import (
            CareerPersonSeasonStatisticsModelPerson,
        )
        from ..models.career_person_season_statistics_model_season import (
            CareerPersonSeasonStatisticsModelSeason,
        )
        from ..models.career_person_season_statistics_model_statistics import (
            CareerPersonSeasonStatisticsModelStatistics,
        )

        d = dict(src_dict)
        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, CareerPersonSeasonStatisticsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = CareerPersonSeasonStatisticsModelPerson.from_dict(_person)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, CareerPersonSeasonStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CareerPersonSeasonStatisticsModelOrganization.from_dict(
                _organization
            )

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, CareerPersonSeasonStatisticsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = CareerPersonSeasonStatisticsModelSeason.from_dict(_season)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, CareerPersonSeasonStatisticsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = CareerPersonSeasonStatisticsModelEntity.from_dict(_entity)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CareerPersonSeasonStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CareerPersonSeasonStatisticsModelStatistics.from_dict(
                _statistics
            )

        career_person_season_statistics_model = cls(
            person_id=person_id,
            person=person,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            entity_id=entity_id,
            entity=entity,
            statistics=statistics,
        )

        return career_person_season_statistics_model
