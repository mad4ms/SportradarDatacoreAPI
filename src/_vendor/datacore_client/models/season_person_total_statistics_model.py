from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_person_total_statistics_model_competition import (
        SeasonPersonTotalStatisticsModelCompetition,
    )
    from ..models.season_person_total_statistics_model_organization import (
        SeasonPersonTotalStatisticsModelOrganization,
    )
    from ..models.season_person_total_statistics_model_person import (
        SeasonPersonTotalStatisticsModelPerson,
    )
    from ..models.season_person_total_statistics_model_season import (
        SeasonPersonTotalStatisticsModelSeason,
    )
    from ..models.season_person_total_statistics_model_statistics import (
        SeasonPersonTotalStatisticsModelStatistics,
    )


T = TypeVar("T", bound="SeasonPersonTotalStatisticsModel")


@_attrs_define
class SeasonPersonTotalStatisticsModel:
    """
    Attributes:
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, SeasonPersonTotalStatisticsModelPerson]): The person information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonPersonTotalStatisticsModelOrganization]): The organization that this season
            person total statistics belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonPersonTotalStatisticsModelSeason]): The season linked to this record
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, SeasonPersonTotalStatisticsModelCompetition]): The competition that this season
            belongs to
        statistics (Union[Unset, SeasonPersonTotalStatisticsModelStatistics]):
    """

    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "SeasonPersonTotalStatisticsModelPerson"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonPersonTotalStatisticsModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonPersonTotalStatisticsModelSeason"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "SeasonPersonTotalStatisticsModelCompetition"] = UNSET
    statistics: Union[Unset, "SeasonPersonTotalStatisticsModelStatistics"] = UNSET

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
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_person_total_statistics_model_competition import (
            SeasonPersonTotalStatisticsModelCompetition,
        )
        from ..models.season_person_total_statistics_model_organization import (
            SeasonPersonTotalStatisticsModelOrganization,
        )
        from ..models.season_person_total_statistics_model_person import (
            SeasonPersonTotalStatisticsModelPerson,
        )
        from ..models.season_person_total_statistics_model_season import (
            SeasonPersonTotalStatisticsModelSeason,
        )
        from ..models.season_person_total_statistics_model_statistics import (
            SeasonPersonTotalStatisticsModelStatistics,
        )

        d = dict(src_dict)
        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, SeasonPersonTotalStatisticsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = SeasonPersonTotalStatisticsModelPerson.from_dict(_person)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonPersonTotalStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonPersonTotalStatisticsModelOrganization.from_dict(
                _organization
            )

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonPersonTotalStatisticsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonPersonTotalStatisticsModelSeason.from_dict(_season)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, SeasonPersonTotalStatisticsModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = SeasonPersonTotalStatisticsModelCompetition.from_dict(
                _competition
            )

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, SeasonPersonTotalStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = SeasonPersonTotalStatisticsModelStatistics.from_dict(
                _statistics
            )

        season_person_total_statistics_model = cls(
            person_id=person_id,
            person=person,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            competition_id=competition_id,
            competition=competition,
            statistics=statistics,
        )

        return season_person_total_statistics_model
