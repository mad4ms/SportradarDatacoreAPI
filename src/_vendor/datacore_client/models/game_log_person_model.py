import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.game_log_person_model_period_id import GameLogPersonModelPeriodId
from ..models.game_log_person_model_position_type_1 import (
    GameLogPersonModelPositionType1,
)
from ..models.game_log_person_model_position_type_2_type_1 import (
    GameLogPersonModelPositionType2Type1,
)
from ..models.game_log_person_model_position_type_3_type_1 import (
    GameLogPersonModelPositionType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.game_log_person_model_entity import GameLogPersonModelEntity
    from ..models.game_log_person_model_fixture import GameLogPersonModelFixture
    from ..models.game_log_person_model_organization import (
        GameLogPersonModelOrganization,
    )
    from ..models.game_log_person_model_person import GameLogPersonModelPerson
    from ..models.game_log_person_model_statistics import GameLogPersonModelStatistics


T = TypeVar("T", bound="GameLogPersonModel")


@_attrs_define
class GameLogPersonModel:
    """
    Attributes:
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, GameLogPersonModelPerson]): The person information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, GameLogPersonModelOrganization]): The organization that this game_log_person belongs
            to
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, GameLogPersonModelFixture]): The match
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, GameLogPersonModelEntity]): The team information
        statistics (Union[Unset, GameLogPersonModelStatistics]):
        period_id (Union[Unset, GameLogPersonModelPeriodId]): The identifier for the period
            >- `1` Period 1
            >- `2` Period 2
            >- `10` Extra time 1 period 1
            >- `11` Extra time 1 period 2
            >- `12` Extra time 2 period 1
            >- `13` Extra time 2 period 2
            >- `14` Shoot Out
        section (Union[Unset, str]): The section of the period (sub-period)
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        position (Union[GameLogPersonModelPositionType1, GameLogPersonModelPositionType2Type1,
            GameLogPersonModelPositionType3Type1, None, Unset]): Playing position
            >- None None
            >- `CB` Center Backcourt
            >- `D` Defensive Specialist
            >- `G` Goalkeeper
            >- `LB` Left Backcourt
            >- `LW` Left Wingman
            >- `P` Pivot
            >- `RB` Right Backcourt
            >- `RW` Right Wingman
             Example: G.
        did_not_play_reason (Union[None, Unset, str]): The reason the player didn't play Example: COACHES_DECISION.
        starter (Union[Unset, bool]):  Example: True.
        participated (Union[Unset, bool]): Did the person actually participate in the the match Example: True.
        is_player (Union[Unset, bool]): Is this person a player Example: True.
        is_team_official (Union[Unset, bool]): Is this person a team official Example: True.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "GameLogPersonModelPerson"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "GameLogPersonModelOrganization"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "GameLogPersonModelFixture"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "GameLogPersonModelEntity"] = UNSET
    statistics: Union[Unset, "GameLogPersonModelStatistics"] = UNSET
    period_id: Union[Unset, GameLogPersonModelPeriodId] = UNSET
    section: Union[Unset, str] = UNSET
    bib: Union[None, Unset, str] = UNSET
    position: Union[
        GameLogPersonModelPositionType1,
        GameLogPersonModelPositionType2Type1,
        GameLogPersonModelPositionType3Type1,
        None,
        Unset,
    ] = UNSET
    did_not_play_reason: Union[None, Unset, str] = UNSET
    starter: Union[Unset, bool] = UNSET
    participated: Union[Unset, bool] = UNSET
    is_player: Union[Unset, bool] = UNSET
    is_team_official: Union[Unset, bool] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

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

        bib: Union[None, Unset, str]
        if isinstance(self.bib, Unset):
            bib = UNSET
        else:
            bib = self.bib

        position: Union[None, Unset, str]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(self.position, GameLogPersonModelPositionType1):
            position = self.position.value
        elif isinstance(self.position, GameLogPersonModelPositionType2Type1):
            position = self.position.value
        elif isinstance(self.position, GameLogPersonModelPositionType3Type1):
            position = self.position.value
        else:
            position = self.position

        did_not_play_reason: Union[None, Unset, str]
        if isinstance(self.did_not_play_reason, Unset):
            did_not_play_reason = UNSET
        else:
            did_not_play_reason = self.did_not_play_reason

        starter = self.starter

        participated = self.participated

        is_player = self.is_player

        is_team_official = self.is_team_official

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
        if bib is not UNSET:
            field_dict["bib"] = bib
        if position is not UNSET:
            field_dict["position"] = position
        if did_not_play_reason is not UNSET:
            field_dict["didNotPlayReason"] = did_not_play_reason
        if starter is not UNSET:
            field_dict["starter"] = starter
        if participated is not UNSET:
            field_dict["participated"] = participated
        if is_player is not UNSET:
            field_dict["isPlayer"] = is_player
        if is_team_official is not UNSET:
            field_dict["isTeamOfficial"] = is_team_official
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.game_log_person_model_entity import GameLogPersonModelEntity
        from ..models.game_log_person_model_fixture import GameLogPersonModelFixture
        from ..models.game_log_person_model_organization import (
            GameLogPersonModelOrganization,
        )
        from ..models.game_log_person_model_person import GameLogPersonModelPerson
        from ..models.game_log_person_model_statistics import (
            GameLogPersonModelStatistics,
        )

        d = dict(src_dict)
        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, GameLogPersonModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = GameLogPersonModelPerson.from_dict(_person)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, GameLogPersonModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = GameLogPersonModelOrganization.from_dict(_organization)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, GameLogPersonModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = GameLogPersonModelFixture.from_dict(_fixture)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, GameLogPersonModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = GameLogPersonModelEntity.from_dict(_entity)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, GameLogPersonModelStatistics]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = GameLogPersonModelStatistics.from_dict(_statistics)

        _period_id = d.pop("periodId", UNSET)
        period_id: Union[Unset, GameLogPersonModelPeriodId]
        if isinstance(_period_id, Unset):
            period_id = UNSET
        else:
            period_id = GameLogPersonModelPeriodId(_period_id)

        section = d.pop("section", UNSET)

        def _parse_bib(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bib = _parse_bib(d.pop("bib", UNSET))

        def _parse_position(
            data: object,
        ) -> Union[
            GameLogPersonModelPositionType1,
            GameLogPersonModelPositionType2Type1,
            GameLogPersonModelPositionType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_1 = GameLogPersonModelPositionType1(data)

                return position_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_2_type_1 = GameLogPersonModelPositionType2Type1(data)

                return position_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_3_type_1 = GameLogPersonModelPositionType3Type1(data)

                return position_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    GameLogPersonModelPositionType1,
                    GameLogPersonModelPositionType2Type1,
                    GameLogPersonModelPositionType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        position = _parse_position(d.pop("position", UNSET))

        def _parse_did_not_play_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        did_not_play_reason = _parse_did_not_play_reason(
            d.pop("didNotPlayReason", UNSET)
        )

        starter = d.pop("starter", UNSET)

        participated = d.pop("participated", UNSET)

        is_player = d.pop("isPlayer", UNSET)

        is_team_official = d.pop("isTeamOfficial", UNSET)

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

        game_log_person_model = cls(
            person_id=person_id,
            person=person,
            organization_id=organization_id,
            organization=organization,
            fixture_id=fixture_id,
            fixture=fixture,
            entity_id=entity_id,
            entity=entity,
            statistics=statistics,
            period_id=period_id,
            section=section,
            bib=bib,
            position=position,
            did_not_play_reason=did_not_play_reason,
            starter=starter,
            participated=participated,
            is_player=is_player,
            is_team_official=is_team_official,
            updated=updated,
            added=added,
        )

        return game_log_person_model
