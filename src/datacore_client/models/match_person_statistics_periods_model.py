import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.match_person_statistics_periods_model_period_id import MatchPersonStatisticsPeriodsModelPeriodId
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_person_statistics_periods_model_entity import MatchPersonStatisticsPeriodsModelEntity
    from ..models.match_person_statistics_periods_model_fixture import MatchPersonStatisticsPeriodsModelFixture
    from ..models.match_person_statistics_periods_model_organization import (
        MatchPersonStatisticsPeriodsModelOrganization,
    )
    from ..models.match_person_statistics_periods_model_person import MatchPersonStatisticsPeriodsModelPerson
    from ..models.match_person_statistics_periods_model_statistics import MatchPersonStatisticsPeriodsModelStatistics


T = TypeVar("T", bound="MatchPersonStatisticsPeriodsModel")


@_attrs_define
class MatchPersonStatisticsPeriodsModel:
    """
    Attributes:
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, MatchPersonStatisticsPeriodsModelPerson]): The person information
        entity_id (Union[None, UUID, Unset]): The unique identifier of the team Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, MatchPersonStatisticsPeriodsModelEntity]): The team information
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, MatchPersonStatisticsPeriodsModelFixture]): The match
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, MatchPersonStatisticsPeriodsModelOrganization]): The organization that this match
            person statistics periods belongs to
        statistics (Union[Unset, MatchPersonStatisticsPeriodsModelStatistics]):
        period_id (Union[Unset, MatchPersonStatisticsPeriodsModelPeriodId]): The identifier for the period
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

    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "MatchPersonStatisticsPeriodsModelPerson"] = UNSET
    entity_id: Union[None, UUID, Unset] = UNSET
    entity: Union[Unset, "MatchPersonStatisticsPeriodsModelEntity"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "MatchPersonStatisticsPeriodsModelFixture"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "MatchPersonStatisticsPeriodsModelOrganization"] = UNSET
    statistics: Union[Unset, "MatchPersonStatisticsPeriodsModelStatistics"] = UNSET
    period_id: Union[Unset, MatchPersonStatisticsPeriodsModelPeriodId] = UNSET
    section: Union[Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        person: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        entity_id: Union[None, Unset, str]
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

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
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
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
        from ..models.match_person_statistics_periods_model_entity import MatchPersonStatisticsPeriodsModelEntity
        from ..models.match_person_statistics_periods_model_fixture import MatchPersonStatisticsPeriodsModelFixture
        from ..models.match_person_statistics_periods_model_organization import (
            MatchPersonStatisticsPeriodsModelOrganization,
        )
        from ..models.match_person_statistics_periods_model_person import MatchPersonStatisticsPeriodsModelPerson
        from ..models.match_person_statistics_periods_model_statistics import (
            MatchPersonStatisticsPeriodsModelStatistics,
        )

        d = dict(src_dict)
        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, MatchPersonStatisticsPeriodsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = MatchPersonStatisticsPeriodsModelPerson.from_dict(_person)

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

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, MatchPersonStatisticsPeriodsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = MatchPersonStatisticsPeriodsModelEntity.from_dict(_entity)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, MatchPersonStatisticsPeriodsModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = MatchPersonStatisticsPeriodsModelFixture.from_dict(_fixture)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, MatchPersonStatisticsPeriodsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = MatchPersonStatisticsPeriodsModelOrganization.from_dict(_organization)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, MatchPersonStatisticsPeriodsModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = MatchPersonStatisticsPeriodsModelStatistics.from_dict(_statistics)

        _period_id = d.pop("periodId", UNSET)
        period_id: Union[Unset, MatchPersonStatisticsPeriodsModelPeriodId]
        if isinstance(_period_id, Unset):
            period_id = UNSET
        else:
            period_id = MatchPersonStatisticsPeriodsModelPeriodId(_period_id)

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

        match_person_statistics_periods_model = cls(
            person_id=person_id,
            person=person,
            entity_id=entity_id,
            entity=entity,
            fixture_id=fixture_id,
            fixture=fixture,
            organization_id=organization_id,
            organization=organization,
            statistics=statistics,
            period_id=period_id,
            section=section,
            updated=updated,
            added=added,
        )

        return match_person_statistics_periods_model
