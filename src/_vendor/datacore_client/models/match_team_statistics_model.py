import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_team_statistics_model_entity import MatchTeamStatisticsModelEntity
    from ..models.match_team_statistics_model_fixture import MatchTeamStatisticsModelFixture
    from ..models.match_team_statistics_model_organization import MatchTeamStatisticsModelOrganization
    from ..models.match_team_statistics_model_statistics import MatchTeamStatisticsModelStatistics


T = TypeVar("T", bound="MatchTeamStatisticsModel")


@_attrs_define
class MatchTeamStatisticsModel:
    """
    Attributes:
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, MatchTeamStatisticsModelEntity]): The team information
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, MatchTeamStatisticsModelFixture]): The match
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, MatchTeamStatisticsModelOrganization]): The organization that this match team
            statistics belongs to
        statistics (Union[Unset, MatchTeamStatisticsModelStatistics]):
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "MatchTeamStatisticsModelEntity"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "MatchTeamStatisticsModelFixture"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "MatchTeamStatisticsModelOrganization"] = UNSET
    statistics: Union[Unset, "MatchTeamStatisticsModelStatistics"] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

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
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.match_team_statistics_model_entity import MatchTeamStatisticsModelEntity
        from ..models.match_team_statistics_model_fixture import MatchTeamStatisticsModelFixture
        from ..models.match_team_statistics_model_organization import MatchTeamStatisticsModelOrganization
        from ..models.match_team_statistics_model_statistics import MatchTeamStatisticsModelStatistics

        d = dict(src_dict)
        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, MatchTeamStatisticsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = MatchTeamStatisticsModelEntity.from_dict(_entity)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, MatchTeamStatisticsModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = MatchTeamStatisticsModelFixture.from_dict(_fixture)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, MatchTeamStatisticsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = MatchTeamStatisticsModelOrganization.from_dict(_organization)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, MatchTeamStatisticsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = MatchTeamStatisticsModelStatistics.from_dict(_statistics)

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

        match_team_statistics_model = cls(
            entity_id=entity_id,
            entity=entity,
            fixture_id=fixture_id,
            fixture=fixture,
            organization_id=organization_id,
            organization=organization,
            statistics=statistics,
            updated=updated,
            added=added,
        )

        return match_team_statistics_model
