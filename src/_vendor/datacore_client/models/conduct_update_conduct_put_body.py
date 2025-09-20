import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.conduct_update_conduct_put_body_conduct_type_item import (
    ConductUpdateConductPutBodyConductTypeItem,
)
from ..models.conduct_update_conduct_put_body_fine_status_type_1 import (
    ConductUpdateConductPutBodyFineStatusType1,
)
from ..models.conduct_update_conduct_put_body_fine_status_type_2_type_1 import (
    ConductUpdateConductPutBodyFineStatusType2Type1,
)
from ..models.conduct_update_conduct_put_body_fine_status_type_3_type_1 import (
    ConductUpdateConductPutBodyFineStatusType3Type1,
)
from ..models.conduct_update_conduct_put_body_hearing_status_type_1 import (
    ConductUpdateConductPutBodyHearingStatusType1,
)
from ..models.conduct_update_conduct_put_body_hearing_status_type_2_type_1 import (
    ConductUpdateConductPutBodyHearingStatusType2Type1,
)
from ..models.conduct_update_conduct_put_body_hearing_status_type_3_type_1 import (
    ConductUpdateConductPutBodyHearingStatusType3Type1,
)
from ..models.conduct_update_conduct_put_body_period_id import (
    ConductUpdateConductPutBodyPeriodId,
)
from ..models.conduct_update_conduct_put_body_role_type_1 import (
    ConductUpdateConductPutBodyRoleType1,
)
from ..models.conduct_update_conduct_put_body_role_type_2_type_1 import (
    ConductUpdateConductPutBodyRoleType2Type1,
)
from ..models.conduct_update_conduct_put_body_role_type_3_type_1 import (
    ConductUpdateConductPutBodyRoleType3Type1,
)
from ..models.conduct_update_conduct_put_body_status_type_1 import (
    ConductUpdateConductPutBodyStatusType1,
)
from ..models.conduct_update_conduct_put_body_status_type_2_type_1 import (
    ConductUpdateConductPutBodyStatusType2Type1,
)
from ..models.conduct_update_conduct_put_body_status_type_3_type_1 import (
    ConductUpdateConductPutBodyStatusType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conduct_update_conduct_put_body_conduct_penalty_result import (
        ConductUpdateConductPutBodyConductPenaltyResult,
    )


T = TypeVar("T", bound="ConductUpdateConductPutBody")


@_attrs_define
class ConductUpdateConductPutBody:
    """
    Attributes:
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group_id (Union[Unset, UUID]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        venue_id (Union[Unset, UUID]): The unique identifier of the venue Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        location_other (Union[None, Unset, str]): The location where the incident occurred Example: location.
        event_id (Union[Unset, UUID]): The ~event~ that this conduct is linked to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (Union[Unset, ConductUpdateConductPutBodyPeriodId]): The identifier for the period
            >- `1` Period 1
            >- `2` Period 2
            >- `10` Extra time 1 period 1
            >- `11` Extra time 1 period 2
            >- `12` Extra time 2 period 1
            >- `13` Extra time 2 period 2
            >- `14` Shoot Out
        section (Union[Unset, str]): The section of the period (sub-period)
        fixture_clock (Union[None, Unset, str]): Match clock when the incident occurred Example: PT9M53S.
        role (Union[ConductUpdateConductPutBodyRoleType1, ConductUpdateConductPutBodyRoleType2Type1,
            ConductUpdateConductPutBodyRoleType3Type1, None, Unset]): The role of person
            >- None None
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
        date_offence_local (Union[None, Unset, datetime.datetime]): Date & Time of the Offence in the local timezone
            Example: 1978-08-24T12:12:12.
        conduct_type (Union[Unset, list[ConductUpdateConductPutBodyConductTypeItem]]):
        conduct_notes (Union[None, Unset, str]): Notes of the Conduct incident
        date_hearing_local (Union[None, Unset, datetime.date]): Date hearing Example: 1978-08-24.
        hearing_notes (Union[None, Unset, str]): Notes from the conduct hearing
        hearing_status (Union[ConductUpdateConductPutBodyHearingStatusType1,
            ConductUpdateConductPutBodyHearingStatusType2Type1, ConductUpdateConductPutBodyHearingStatusType3Type1, None,
            Unset]): Conduct hearing status
            >- None None
            >- `FINALIZED` Finalized
            >- `PENDING` Pending
             Example: PENDING.
        life_sentence (Union[Unset, bool]): Was the result of the conduct hearing a life sentence? Example: True.
        penalty_results (Union[Unset, list[Union['ConductUpdateConductPutBodyConductPenaltyResult', None]]]):
        fine_amount (Union[Unset, float]): Conduct fine amount
        fine_currency (Union[None, Unset, str]): Fine currency Example: USD.
        fine_status (Union[ConductUpdateConductPutBodyFineStatusType1, ConductUpdateConductPutBodyFineStatusType2Type1,
            ConductUpdateConductPutBodyFineStatusType3Type1, None, Unset]): Conduct fine due status
            >- None None
            >- `CANCELLED` Cancelled
            >- `ISSUED` Issued
            >- `OTHER` Other
            >- `PAID` Paid
            >- `UNPAID` Unpaid
             Example: PAID.
        date_suspended_to (Union[None, Unset, datetime.date]): Date the suspension ended Example: 1978-08-24.
        date_suspended_from (Union[None, Unset, datetime.date]): Date the suspension started Example: 1978-08-24.
        date_fine_paid_local (Union[None, Unset, datetime.date]): Date the fine was paid Example: 1978-08-24.
        status (Union[ConductUpdateConductPutBodyStatusType1, ConductUpdateConductPutBodyStatusType2Type1,
            ConductUpdateConductPutBodyStatusType3Type1, None, Unset]): Conduct status
            >- None None
            >- `ACTIVE` Active
            >- `CLOSED` Closed
            >- `COMPLETE` Complete
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    person_id: Union[Unset, UUID] = UNSET
    entity_group_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    venue_id: Union[Unset, UUID] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    bib: Union[None, Unset, str] = UNSET
    location_other: Union[None, Unset, str] = UNSET
    event_id: Union[Unset, UUID] = UNSET
    period_id: Union[Unset, ConductUpdateConductPutBodyPeriodId] = UNSET
    section: Union[Unset, str] = UNSET
    fixture_clock: Union[None, Unset, str] = UNSET
    role: Union[
        ConductUpdateConductPutBodyRoleType1,
        ConductUpdateConductPutBodyRoleType2Type1,
        ConductUpdateConductPutBodyRoleType3Type1,
        None,
        Unset,
    ] = UNSET
    date_offence_local: Union[None, Unset, datetime.datetime] = UNSET
    conduct_type: Union[Unset, list[ConductUpdateConductPutBodyConductTypeItem]] = UNSET
    conduct_notes: Union[None, Unset, str] = UNSET
    date_hearing_local: Union[None, Unset, datetime.date] = UNSET
    hearing_notes: Union[None, Unset, str] = UNSET
    hearing_status: Union[
        ConductUpdateConductPutBodyHearingStatusType1,
        ConductUpdateConductPutBodyHearingStatusType2Type1,
        ConductUpdateConductPutBodyHearingStatusType3Type1,
        None,
        Unset,
    ] = UNSET
    life_sentence: Union[Unset, bool] = UNSET
    penalty_results: Union[
        Unset, list[Union["ConductUpdateConductPutBodyConductPenaltyResult", None]]
    ] = UNSET
    fine_amount: Union[Unset, float] = UNSET
    fine_currency: Union[None, Unset, str] = UNSET
    fine_status: Union[
        ConductUpdateConductPutBodyFineStatusType1,
        ConductUpdateConductPutBodyFineStatusType2Type1,
        ConductUpdateConductPutBodyFineStatusType3Type1,
        None,
        Unset,
    ] = UNSET
    date_suspended_to: Union[None, Unset, datetime.date] = UNSET
    date_suspended_from: Union[None, Unset, datetime.date] = UNSET
    date_fine_paid_local: Union[None, Unset, datetime.date] = UNSET
    status: Union[
        ConductUpdateConductPutBodyStatusType1,
        ConductUpdateConductPutBodyStatusType2Type1,
        ConductUpdateConductPutBodyStatusType3Type1,
        None,
        Unset,
    ] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conduct_update_conduct_put_body_conduct_penalty_result import (
            ConductUpdateConductPutBodyConductPenaltyResult,
        )

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        entity_group_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_group_id, Unset):
            entity_group_id = str(self.entity_group_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        venue_id: Union[Unset, str] = UNSET
        if not isinstance(self.venue_id, Unset):
            venue_id = str(self.venue_id)

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        bib: Union[None, Unset, str]
        if isinstance(self.bib, Unset):
            bib = UNSET
        else:
            bib = self.bib

        location_other: Union[None, Unset, str]
        if isinstance(self.location_other, Unset):
            location_other = UNSET
        else:
            location_other = self.location_other

        event_id: Union[Unset, str] = UNSET
        if not isinstance(self.event_id, Unset):
            event_id = str(self.event_id)

        period_id: Union[Unset, int] = UNSET
        if not isinstance(self.period_id, Unset):
            period_id = self.period_id.value

        section = self.section

        fixture_clock: Union[None, Unset, str]
        if isinstance(self.fixture_clock, Unset):
            fixture_clock = UNSET
        else:
            fixture_clock = self.fixture_clock

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        elif isinstance(self.role, ConductUpdateConductPutBodyRoleType1):
            role = self.role.value
        elif isinstance(self.role, ConductUpdateConductPutBodyRoleType2Type1):
            role = self.role.value
        elif isinstance(self.role, ConductUpdateConductPutBodyRoleType3Type1):
            role = self.role.value
        else:
            role = self.role

        date_offence_local: Union[None, Unset, str]
        if isinstance(self.date_offence_local, Unset):
            date_offence_local = UNSET
        elif isinstance(self.date_offence_local, datetime.datetime):
            date_offence_local = self.date_offence_local.isoformat()
        else:
            date_offence_local = self.date_offence_local

        conduct_type: Union[Unset, list[str]] = UNSET
        if not isinstance(self.conduct_type, Unset):
            conduct_type = []
            for conduct_type_item_data in self.conduct_type:
                conduct_type_item = conduct_type_item_data.value
                conduct_type.append(conduct_type_item)

        conduct_notes: Union[None, Unset, str]
        if isinstance(self.conduct_notes, Unset):
            conduct_notes = UNSET
        else:
            conduct_notes = self.conduct_notes

        date_hearing_local: Union[None, Unset, str]
        if isinstance(self.date_hearing_local, Unset):
            date_hearing_local = UNSET
        elif isinstance(self.date_hearing_local, datetime.date):
            date_hearing_local = self.date_hearing_local.isoformat()
        else:
            date_hearing_local = self.date_hearing_local

        hearing_notes: Union[None, Unset, str]
        if isinstance(self.hearing_notes, Unset):
            hearing_notes = UNSET
        else:
            hearing_notes = self.hearing_notes

        hearing_status: Union[None, Unset, str]
        if isinstance(self.hearing_status, Unset):
            hearing_status = UNSET
        elif isinstance(
            self.hearing_status, ConductUpdateConductPutBodyHearingStatusType1
        ):
            hearing_status = self.hearing_status.value
        elif isinstance(
            self.hearing_status, ConductUpdateConductPutBodyHearingStatusType2Type1
        ):
            hearing_status = self.hearing_status.value
        elif isinstance(
            self.hearing_status, ConductUpdateConductPutBodyHearingStatusType3Type1
        ):
            hearing_status = self.hearing_status.value
        else:
            hearing_status = self.hearing_status

        life_sentence = self.life_sentence

        penalty_results: Union[Unset, list[Union[None, dict[str, Any]]]] = UNSET
        if not isinstance(self.penalty_results, Unset):
            penalty_results = []
            for penalty_results_item_data in self.penalty_results:
                penalty_results_item: Union[None, dict[str, Any]]
                if isinstance(
                    penalty_results_item_data,
                    ConductUpdateConductPutBodyConductPenaltyResult,
                ):
                    penalty_results_item = penalty_results_item_data.to_dict()
                else:
                    penalty_results_item = penalty_results_item_data
                penalty_results.append(penalty_results_item)

        fine_amount = self.fine_amount

        fine_currency: Union[None, Unset, str]
        if isinstance(self.fine_currency, Unset):
            fine_currency = UNSET
        else:
            fine_currency = self.fine_currency

        fine_status: Union[None, Unset, str]
        if isinstance(self.fine_status, Unset):
            fine_status = UNSET
        elif isinstance(self.fine_status, ConductUpdateConductPutBodyFineStatusType1):
            fine_status = self.fine_status.value
        elif isinstance(
            self.fine_status, ConductUpdateConductPutBodyFineStatusType2Type1
        ):
            fine_status = self.fine_status.value
        elif isinstance(
            self.fine_status, ConductUpdateConductPutBodyFineStatusType3Type1
        ):
            fine_status = self.fine_status.value
        else:
            fine_status = self.fine_status

        date_suspended_to: Union[None, Unset, str]
        if isinstance(self.date_suspended_to, Unset):
            date_suspended_to = UNSET
        elif isinstance(self.date_suspended_to, datetime.date):
            date_suspended_to = self.date_suspended_to.isoformat()
        else:
            date_suspended_to = self.date_suspended_to

        date_suspended_from: Union[None, Unset, str]
        if isinstance(self.date_suspended_from, Unset):
            date_suspended_from = UNSET
        elif isinstance(self.date_suspended_from, datetime.date):
            date_suspended_from = self.date_suspended_from.isoformat()
        else:
            date_suspended_from = self.date_suspended_from

        date_fine_paid_local: Union[None, Unset, str]
        if isinstance(self.date_fine_paid_local, Unset):
            date_fine_paid_local = UNSET
        elif isinstance(self.date_fine_paid_local, datetime.date):
            date_fine_paid_local = self.date_fine_paid_local.isoformat()
        else:
            date_fine_paid_local = self.date_fine_paid_local

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ConductUpdateConductPutBodyStatusType1):
            status = self.status.value
        elif isinstance(self.status, ConductUpdateConductPutBodyStatusType2Type1):
            status = self.status.value
        elif isinstance(self.status, ConductUpdateConductPutBodyStatusType3Type1):
            status = self.status.value
        else:
            status = self.status

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if venue_id is not UNSET:
            field_dict["venueId"] = venue_id
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if bib is not UNSET:
            field_dict["bib"] = bib
        if location_other is not UNSET:
            field_dict["locationOther"] = location_other
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if period_id is not UNSET:
            field_dict["periodId"] = period_id
        if section is not UNSET:
            field_dict["section"] = section
        if fixture_clock is not UNSET:
            field_dict["fixtureClock"] = fixture_clock
        if role is not UNSET:
            field_dict["role"] = role
        if date_offence_local is not UNSET:
            field_dict["dateOffenceLocal"] = date_offence_local
        if conduct_type is not UNSET:
            field_dict["conductType"] = conduct_type
        if conduct_notes is not UNSET:
            field_dict["conductNotes"] = conduct_notes
        if date_hearing_local is not UNSET:
            field_dict["dateHearingLocal"] = date_hearing_local
        if hearing_notes is not UNSET:
            field_dict["hearingNotes"] = hearing_notes
        if hearing_status is not UNSET:
            field_dict["hearingStatus"] = hearing_status
        if life_sentence is not UNSET:
            field_dict["lifeSentence"] = life_sentence
        if penalty_results is not UNSET:
            field_dict["penaltyResults"] = penalty_results
        if fine_amount is not UNSET:
            field_dict["fineAmount"] = fine_amount
        if fine_currency is not UNSET:
            field_dict["fineCurrency"] = fine_currency
        if fine_status is not UNSET:
            field_dict["fineStatus"] = fine_status
        if date_suspended_to is not UNSET:
            field_dict["dateSuspendedTo"] = date_suspended_to
        if date_suspended_from is not UNSET:
            field_dict["dateSuspendedFrom"] = date_suspended_from
        if date_fine_paid_local is not UNSET:
            field_dict["dateFinePaidLocal"] = date_fine_paid_local
        if status is not UNSET:
            field_dict["status"] = status
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conduct_update_conduct_put_body_conduct_penalty_result import (
            ConductUpdateConductPutBodyConductPenaltyResult,
        )

        d = dict(src_dict)
        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _entity_group_id = d.pop("entityGroupId", UNSET)
        entity_group_id: Union[Unset, UUID]
        if isinstance(_entity_group_id, Unset):
            entity_group_id = UNSET
        else:
            entity_group_id = UUID(_entity_group_id)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _venue_id = d.pop("venueId", UNSET)
        venue_id: Union[Unset, UUID]
        if isinstance(_venue_id, Unset):
            venue_id = UNSET
        else:
            venue_id = UUID(_venue_id)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        def _parse_bib(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bib = _parse_bib(d.pop("bib", UNSET))

        def _parse_location_other(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_other = _parse_location_other(d.pop("locationOther", UNSET))

        _event_id = d.pop("eventId", UNSET)
        event_id: Union[Unset, UUID]
        if isinstance(_event_id, Unset):
            event_id = UNSET
        else:
            event_id = UUID(_event_id)

        _period_id = d.pop("periodId", UNSET)
        period_id: Union[Unset, ConductUpdateConductPutBodyPeriodId]
        if isinstance(_period_id, Unset):
            period_id = UNSET
        else:
            period_id = ConductUpdateConductPutBodyPeriodId(_period_id)

        section = d.pop("section", UNSET)

        def _parse_fixture_clock(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fixture_clock = _parse_fixture_clock(d.pop("fixtureClock", UNSET))

        def _parse_role(
            data: object,
        ) -> Union[
            ConductUpdateConductPutBodyRoleType1,
            ConductUpdateConductPutBodyRoleType2Type1,
            ConductUpdateConductPutBodyRoleType3Type1,
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
                role_type_1 = ConductUpdateConductPutBodyRoleType1(data)

                return role_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_2_type_1 = ConductUpdateConductPutBodyRoleType2Type1(data)

                return role_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                role_type_3_type_1 = ConductUpdateConductPutBodyRoleType3Type1(data)

                return role_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    ConductUpdateConductPutBodyRoleType1,
                    ConductUpdateConductPutBodyRoleType2Type1,
                    ConductUpdateConductPutBodyRoleType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        role = _parse_role(d.pop("role", UNSET))

        def _parse_date_offence_local(
            data: object,
        ) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_offence_local_type_0 = isoparse(data)

                return date_offence_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_offence_local = _parse_date_offence_local(d.pop("dateOffenceLocal", UNSET))

        conduct_type = []
        _conduct_type = d.pop("conductType", UNSET)
        for conduct_type_item_data in _conduct_type or []:
            conduct_type_item = ConductUpdateConductPutBodyConductTypeItem(
                conduct_type_item_data
            )

            conduct_type.append(conduct_type_item)

        def _parse_conduct_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        conduct_notes = _parse_conduct_notes(d.pop("conductNotes", UNSET))

        def _parse_date_hearing_local(
            data: object,
        ) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_hearing_local_type_0 = isoparse(data).date()

                return date_hearing_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_hearing_local = _parse_date_hearing_local(d.pop("dateHearingLocal", UNSET))

        def _parse_hearing_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hearing_notes = _parse_hearing_notes(d.pop("hearingNotes", UNSET))

        def _parse_hearing_status(
            data: object,
        ) -> Union[
            ConductUpdateConductPutBodyHearingStatusType1,
            ConductUpdateConductPutBodyHearingStatusType2Type1,
            ConductUpdateConductPutBodyHearingStatusType3Type1,
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
                hearing_status_type_1 = ConductUpdateConductPutBodyHearingStatusType1(
                    data
                )

                return hearing_status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hearing_status_type_2_type_1 = (
                    ConductUpdateConductPutBodyHearingStatusType2Type1(data)
                )

                return hearing_status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                hearing_status_type_3_type_1 = (
                    ConductUpdateConductPutBodyHearingStatusType3Type1(data)
                )

                return hearing_status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    ConductUpdateConductPutBodyHearingStatusType1,
                    ConductUpdateConductPutBodyHearingStatusType2Type1,
                    ConductUpdateConductPutBodyHearingStatusType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        hearing_status = _parse_hearing_status(d.pop("hearingStatus", UNSET))

        life_sentence = d.pop("lifeSentence", UNSET)

        penalty_results = []
        _penalty_results = d.pop("penaltyResults", UNSET)
        for penalty_results_item_data in _penalty_results or []:

            def _parse_penalty_results_item(
                data: object,
            ) -> Union["ConductUpdateConductPutBodyConductPenaltyResult", None]:
                if data is None:
                    return data
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    penalty_results_item_type_0 = (
                        ConductUpdateConductPutBodyConductPenaltyResult.from_dict(data)
                    )

                    return penalty_results_item_type_0
                except:  # noqa: E722
                    pass
                return cast(
                    Union["ConductUpdateConductPutBodyConductPenaltyResult", None], data
                )

            penalty_results_item = _parse_penalty_results_item(
                penalty_results_item_data
            )

            penalty_results.append(penalty_results_item)

        fine_amount = d.pop("fineAmount", UNSET)

        def _parse_fine_currency(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fine_currency = _parse_fine_currency(d.pop("fineCurrency", UNSET))

        def _parse_fine_status(
            data: object,
        ) -> Union[
            ConductUpdateConductPutBodyFineStatusType1,
            ConductUpdateConductPutBodyFineStatusType2Type1,
            ConductUpdateConductPutBodyFineStatusType3Type1,
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
                fine_status_type_1 = ConductUpdateConductPutBodyFineStatusType1(data)

                return fine_status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fine_status_type_2_type_1 = (
                    ConductUpdateConductPutBodyFineStatusType2Type1(data)
                )

                return fine_status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fine_status_type_3_type_1 = (
                    ConductUpdateConductPutBodyFineStatusType3Type1(data)
                )

                return fine_status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    ConductUpdateConductPutBodyFineStatusType1,
                    ConductUpdateConductPutBodyFineStatusType2Type1,
                    ConductUpdateConductPutBodyFineStatusType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        fine_status = _parse_fine_status(d.pop("fineStatus", UNSET))

        def _parse_date_suspended_to(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_suspended_to_type_0 = isoparse(data).date()

                return date_suspended_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_suspended_to = _parse_date_suspended_to(d.pop("dateSuspendedTo", UNSET))

        def _parse_date_suspended_from(
            data: object,
        ) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_suspended_from_type_0 = isoparse(data).date()

                return date_suspended_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_suspended_from = _parse_date_suspended_from(
            d.pop("dateSuspendedFrom", UNSET)
        )

        def _parse_date_fine_paid_local(
            data: object,
        ) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_fine_paid_local_type_0 = isoparse(data).date()

                return date_fine_paid_local_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_fine_paid_local = _parse_date_fine_paid_local(
            d.pop("dateFinePaidLocal", UNSET)
        )

        def _parse_status(
            data: object,
        ) -> Union[
            ConductUpdateConductPutBodyStatusType1,
            ConductUpdateConductPutBodyStatusType2Type1,
            ConductUpdateConductPutBodyStatusType3Type1,
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
                status_type_1 = ConductUpdateConductPutBodyStatusType1(data)

                return status_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_2_type_1 = ConductUpdateConductPutBodyStatusType2Type1(data)

                return status_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_3_type_1 = ConductUpdateConductPutBodyStatusType3Type1(data)

                return status_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    ConductUpdateConductPutBodyStatusType1,
                    ConductUpdateConductPutBodyStatusType2Type1,
                    ConductUpdateConductPutBodyStatusType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        status = _parse_status(d.pop("status", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        conduct_update_conduct_put_body = cls(
            person_id=person_id,
            entity_group_id=entity_group_id,
            entity_id=entity_id,
            venue_id=venue_id,
            fixture_id=fixture_id,
            season_id=season_id,
            competition_id=competition_id,
            bib=bib,
            location_other=location_other,
            event_id=event_id,
            period_id=period_id,
            section=section,
            fixture_clock=fixture_clock,
            role=role,
            date_offence_local=date_offence_local,
            conduct_type=conduct_type,
            conduct_notes=conduct_notes,
            date_hearing_local=date_hearing_local,
            hearing_notes=hearing_notes,
            hearing_status=hearing_status,
            life_sentence=life_sentence,
            penalty_results=penalty_results,
            fine_amount=fine_amount,
            fine_currency=fine_currency,
            fine_status=fine_status,
            date_suspended_to=date_suspended_to,
            date_suspended_from=date_suspended_from,
            date_fine_paid_local=date_fine_paid_local,
            status=status,
            external_id=external_id,
        )

        return conduct_update_conduct_put_body
