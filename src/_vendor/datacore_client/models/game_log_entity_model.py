import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.game_log_entity_model_period_id import GameLogEntityModelPeriodId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_log_entity_model_entity import GameLogEntityModelEntity
    from ..models.game_log_entity_model_fixture import GameLogEntityModelFixture
    from ..models.game_log_entity_model_organization import (
        GameLogEntityModelOrganization,
    )
    from ..models.game_log_entity_model_statistics import GameLogEntityModelStatistics


T = TypeVar("T", bound="GameLogEntityModel")


@_attrs_define
class GameLogEntityModel:
    """
    Attributes:
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, GameLogEntityModelOrganization]): The organization that this game_log_entity belongs
            to
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, GameLogEntityModelFixture]): The match
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, GameLogEntityModelEntity]): The team information
        statistics (Union[Unset, GameLogEntityModelStatistics]):
        period_id (Union[Unset, GameLogEntityModelPeriodId]): The identifier for the period
            >- `1` Period 1
            >- `2` Period 2
            >- `10` Extra time 1 period 1
            >- `11` Extra time 1 period 2
            >- `12` Extra time 2 period 1
            >- `13` Extra time 2 period 2
            >- `14` Shoot Out
        section (Union[Unset, str]): The section of the period (sub-period)
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "GameLogEntityModelOrganization"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "GameLogEntityModelFixture"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "GameLogEntityModelEntity"] = UNSET
    statistics: Union[Unset, "GameLogEntityModelStatistics"] = UNSET
    period_id: Union[Unset, GameLogEntityModelPeriodId] = UNSET
    section: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        period_id: Union[Unset, int] = UNSET
        if not isinstance(self.period_id, Unset):
            period_id = self.period_id.value

        section = self.section

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if period_id is not UNSET:
            field_dict["periodId"] = period_id
        if section is not UNSET:
            field_dict["section"] = section
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_log_entity_model_entity import GameLogEntityModelEntity
        from ..models.game_log_entity_model_fixture import GameLogEntityModelFixture
        from ..models.game_log_entity_model_organization import (
            GameLogEntityModelOrganization,
        )
        from ..models.game_log_entity_model_statistics import (
            GameLogEntityModelStatistics,
        )

        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, GameLogEntityModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = GameLogEntityModelOrganization.from_dict(_organization)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, GameLogEntityModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = GameLogEntityModelFixture.from_dict(_fixture)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, GameLogEntityModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = GameLogEntityModelEntity.from_dict(_entity)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GameLogEntityModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GameLogEntityModelStatistics.from_dict(_statistics)

        _period_id = d.pop("periodId", UNSET)
        period_id: Union[Unset, GameLogEntityModelPeriodId]
        if isinstance(_period_id, Unset):
            period_id = UNSET
        else:
            period_id = GameLogEntityModelPeriodId(_period_id)

        section = d.pop("section", UNSET)

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

        game_log_entity_model = cls(
            organization_id=organization_id,
            organization=organization,
            fixture_id=fixture_id,
            fixture=fixture,
            entity_id=entity_id,
            entity=entity,
            statistics=statistics,
            period_id=period_id,
            section=section,
            updated=updated,
            added=added,
        )

        return game_log_entity_model
