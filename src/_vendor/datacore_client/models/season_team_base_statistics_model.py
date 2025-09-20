import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_team_base_statistics_model_competitor_type import SeasonTeamBaseStatisticsModelCompetitorType
from ..models.season_team_base_statistics_model_fixture_type import SeasonTeamBaseStatisticsModelFixtureType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_team_base_statistics_model_entity import SeasonTeamBaseStatisticsModelEntity
    from ..models.season_team_base_statistics_model_organization import SeasonTeamBaseStatisticsModelOrganization
    from ..models.season_team_base_statistics_model_season import SeasonTeamBaseStatisticsModelSeason
    from ..models.season_team_base_statistics_model_statistics import SeasonTeamBaseStatisticsModelStatistics


T = TypeVar("T", bound="SeasonTeamBaseStatisticsModel")


@_attrs_define
class SeasonTeamBaseStatisticsModel:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonTeamBaseStatisticsModelSeason]): The season linked to this record
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, SeasonTeamBaseStatisticsModelEntity]): The team information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonTeamBaseStatisticsModelOrganization]): The organization that this season team
            base statistics belongs to
        fixture_type (Union[Unset, SeasonTeamBaseStatisticsModelFixtureType]): Type of match
            >- `ALL_STAR` All Star
            >- `DEMONSTRATION` Demonstration
            >- `FINAL` Final
            >- `FRIENDLY` Friendly
            >- `PLAYOFF` Playoff
            >- `PRESEASON` Pre Season
            >- `REGULAR` Regular
             Example: REGULAR.
        competitor_type (Union[Unset, SeasonTeamBaseStatisticsModelCompetitorType]): The type of competitors in this
            match
            >- `ENTITY` Entity
            >- `PERSON` Person
             Example: ENTITY.
        representing (Union[Unset, str]): Who was being represented for the season base statistics Example: AUSTRALIA.
        statistics (Union[Unset, SeasonTeamBaseStatisticsModelStatistics]):
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonTeamBaseStatisticsModelSeason"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "SeasonTeamBaseStatisticsModelEntity"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonTeamBaseStatisticsModelOrganization"] = UNSET
    fixture_type: Union[Unset, SeasonTeamBaseStatisticsModelFixtureType] = UNSET
    competitor_type: Union[Unset, SeasonTeamBaseStatisticsModelCompetitorType] = UNSET
    representing: Union[Unset, str] = UNSET
    statistics: Union[Unset, "SeasonTeamBaseStatisticsModelStatistics"] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        fixture_type: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_type, Unset):
            fixture_type = self.fixture_type.value

        competitor_type: Union[Unset, str] = UNSET
        if not isinstance(self.competitor_type, Unset):
            competitor_type = self.competitor_type.value

        representing = self.representing

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if fixture_type is not UNSET:
            field_dict["fixtureType"] = fixture_type
        if competitor_type is not UNSET:
            field_dict["competitorType"] = competitor_type
        if representing is not UNSET:
            field_dict["representing"] = representing
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_team_base_statistics_model_entity import SeasonTeamBaseStatisticsModelEntity
        from ..models.season_team_base_statistics_model_organization import SeasonTeamBaseStatisticsModelOrganization
        from ..models.season_team_base_statistics_model_season import SeasonTeamBaseStatisticsModelSeason
        from ..models.season_team_base_statistics_model_statistics import SeasonTeamBaseStatisticsModelStatistics

        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonTeamBaseStatisticsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonTeamBaseStatisticsModelSeason.from_dict(_season)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, SeasonTeamBaseStatisticsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = SeasonTeamBaseStatisticsModelEntity.from_dict(_entity)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonTeamBaseStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonTeamBaseStatisticsModelOrganization.from_dict(_organization)

        _fixture_type = d.pop("fixtureType", UNSET)
        fixture_type: Union[Unset, SeasonTeamBaseStatisticsModelFixtureType]
        if isinstance(_fixture_type, Unset):
            fixture_type = UNSET
        else:
            fixture_type = SeasonTeamBaseStatisticsModelFixtureType(_fixture_type)

        _competitor_type = d.pop("competitorType", UNSET)
        competitor_type: Union[Unset, SeasonTeamBaseStatisticsModelCompetitorType]
        if isinstance(_competitor_type, Unset):
            competitor_type = UNSET
        else:
            competitor_type = SeasonTeamBaseStatisticsModelCompetitorType(_competitor_type)

        representing = d.pop("representing", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SeasonTeamBaseStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SeasonTeamBaseStatisticsModelStatistics.from_dict(_statistics)

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

        season_team_base_statistics_model = cls(
            season_id=season_id,
            season=season,
            entity_id=entity_id,
            entity=entity,
            organization_id=organization_id,
            organization=organization,
            fixture_type=fixture_type,
            competitor_type=competitor_type,
            representing=representing,
            statistics=statistics,
            updated=updated,
            added=added,
        )

        return season_team_base_statistics_model
