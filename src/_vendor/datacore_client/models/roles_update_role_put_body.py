import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.roles_update_role_put_body_role import RolesUpdateRolePutBodyRole
from ..models.roles_update_role_put_body_status import RolesUpdateRolePutBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="RolesUpdateRolePutBody")


@_attrs_define
class RolesUpdateRolePutBody:
    """
    Attributes:
        entity_group_id (Union[None, UUID, Unset]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[None, UUID, Unset]): The unique identifier of the team Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[None, UUID, Unset]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (Union[None, UUID, Unset]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        status (Union[Unset, RolesUpdateRolePutBodyStatus]): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        date_from (Union[None, Unset, datetime.date]): Date the role started (Not for a role within a match) Example:
            1978-08-24.
        date_to (Union[None, Unset, datetime.date]): Date the role ended (Not for a role within a match) Example:
            1978-08-24.
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        role_number (Union[None, Unset, int]): Number within the role. eg: Assistant Coach 2 Example: 1.
        role (Union[Unset, RolesUpdateRolePutBodyRole]): Role
            >- `ASSISTANT_REFEREE_1` Assistant Referee 1
            >- `ASSISTANT_REFEREE_2` Assistant Referee 2
            >- `CLUB_IT_OFFICER` Club IT Officer
            >- `CLUB_OFFICIAL` Club Official
            >- `CLUB_OFFICIAL_ASSISTANT` Substitute for contact person of club
            >- `COACH` Coach
            >- `COACH_ASSISTANT` Coach Assistant
            >- `COACH_HEAD` Coach Head
            >- `DELEGATE` Delegate
            >- `DIRECTOR` Director
            >- `LIAISON_OFFICER` Liaison Officer
            >- `MATCH_LIAISON` Match Liaison
            >- `MATCH_SUPERVISOR` Match Supervisor
            >- `MEDIA_OFFICER` Media Officer
            >- `OFFICE_STAFF` Office Staff
            >- `OFFICIAL_A` Official A
            >- `OFFICIAL_B` Official B
            >- `OFFICIAL_C` Official C
            >- `OFFICIAL_D` Official D
            >- `OFFICIAL_E` Official E
            >- `PLAYER_CONTRACT_MANAGER` Player Contract Manager
            >- `REFEREE` Referee
            >- `REFEREE_LIAISON` Referee Liaison
            >- `REFEREE_OBSERVER` Referee Observer
            >- `REFEREE_OBSERVER_LIAISON` Referee Observer Liaison
            >- `SCOREKEEPER` Scorekeeper
            >- `SCOUT_1` Scout 1
            >- `SCOUT_2` Scout 2
            >- `SCOUT_3` Scout 3
            >- `SCOUT_SUPERVISOR` Scout Supervisor
            >- `SECRETARY` Secretary
            >- `SPORT_DIRECTOR` Sporting Director
            >- `TEAM_COORDINATOR` Team Coordinator
            >- `TIMEKEEPER` Timekeeper
            >- `TRAINER` Trainer
            >- `YOUTH_COORDINATOR` Youth Coordinator
             Example: COACH.
        role_sub_type (Union[None, Unset, str]): Role sub type Example: Offensive Coach.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    entity_group_id: Union[None, UUID, Unset] = UNSET
    entity_id: Union[None, UUID, Unset] = UNSET
    season_id: Union[None, UUID, Unset] = UNSET
    fixture_id: Union[None, UUID, Unset] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    status: Union[Unset, RolesUpdateRolePutBodyStatus] = UNSET
    date_from: Union[None, Unset, datetime.date] = UNSET
    date_to: Union[None, Unset, datetime.date] = UNSET
    bib: Union[None, Unset, str] = UNSET
    role_number: Union[None, Unset, int] = UNSET
    role: Union[Unset, RolesUpdateRolePutBodyRole] = UNSET
    role_sub_type: Union[None, Unset, str] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        entity_group_id: Union[None, Unset, str]
        if isinstance(self.entity_group_id, Unset):
            entity_group_id = UNSET
        elif isinstance(self.entity_group_id, UUID):
            entity_group_id = str(self.entity_group_id)
        else:
            entity_group_id = self.entity_group_id

        entity_id: Union[None, Unset, str]
        if isinstance(self.entity_id, Unset):
            entity_id = UNSET
        elif isinstance(self.entity_id, UUID):
            entity_id = str(self.entity_id)
        else:
            entity_id = self.entity_id

        season_id: Union[None, Unset, str]
        if isinstance(self.season_id, Unset):
            season_id = UNSET
        elif isinstance(self.season_id, UUID):
            season_id = str(self.season_id)
        else:
            season_id = self.season_id

        fixture_id: Union[None, Unset, str]
        if isinstance(self.fixture_id, Unset):
            fixture_id = UNSET
        elif isinstance(self.fixture_id, UUID):
            fixture_id = str(self.fixture_id)
        else:
            fixture_id = self.fixture_id

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        date_from: Union[None, Unset, str]
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        elif isinstance(self.date_from, datetime.date):
            date_from = self.date_from.isoformat()
        else:
            date_from = self.date_from

        date_to: Union[None, Unset, str]
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        elif isinstance(self.date_to, datetime.date):
            date_to = self.date_to.isoformat()
        else:
            date_to = self.date_to

        bib: Union[None, Unset, str]
        if isinstance(self.bib, Unset):
            bib = UNSET
        else:
            bib = self.bib

        role_number: Union[None, Unset, int]
        if isinstance(self.role_number, Unset):
            role_number = UNSET
        else:
            role_number = self.role_number

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        role_sub_type: Union[None, Unset, str]
        if isinstance(self.role_sub_type, Unset):
            role_sub_type = UNSET
        else:
            role_sub_type = self.role_sub_type

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if status is not UNSET:
            field_dict["status"] = status
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if bib is not UNSET:
            field_dict["bib"] = bib
        if role_number is not UNSET:
            field_dict["roleNumber"] = role_number
        if role is not UNSET:
            field_dict["role"] = role
        if role_sub_type is not UNSET:
            field_dict["roleSubType"] = role_sub_type
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_entity_group_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                entity_group_id_type_0 = UUID(data)

                return entity_group_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        entity_group_id = _parse_entity_group_id(d.pop("entityGroupId", UNSET))

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

        def _parse_season_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                season_id_type_0 = UUID(data)

                return season_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        season_id = _parse_season_id(d.pop("seasonId", UNSET))

        def _parse_fixture_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fixture_id_type_0 = UUID(data)

                return fixture_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        fixture_id = _parse_fixture_id(d.pop("fixtureId", UNSET))

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _status = d.pop("status", UNSET)
        status: Union[Unset, RolesUpdateRolePutBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = RolesUpdateRolePutBodyStatus(_status)

        def _parse_date_from(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_type_0 = isoparse(data).date()

                return date_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_from = _parse_date_from(d.pop("dateFrom", UNSET))

        def _parse_date_to(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_to_type_0 = isoparse(data).date()

                return date_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_to = _parse_date_to(d.pop("dateTo", UNSET))

        def _parse_bib(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bib = _parse_bib(d.pop("bib", UNSET))

        def _parse_role_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        role_number = _parse_role_number(d.pop("roleNumber", UNSET))

        _role = d.pop("role", UNSET)
        role: Union[Unset, RolesUpdateRolePutBodyRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = RolesUpdateRolePutBodyRole(_role)

        def _parse_role_sub_type(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role_sub_type = _parse_role_sub_type(d.pop("roleSubType", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        roles_update_role_put_body = cls(
            entity_group_id=entity_group_id,
            entity_id=entity_id,
            season_id=season_id,
            fixture_id=fixture_id,
            person_id=person_id,
            status=status,
            date_from=date_from,
            date_to=date_to,
            bib=bib,
            role_number=role_number,
            role=role,
            role_sub_type=role_sub_type,
            external_id=external_id,
        )

        return roles_update_role_put_body
