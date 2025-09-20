from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.season_entities_insert_update_season_payload_season_teams_post_body_roster_status import (
    SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyRosterStatus,
)
from ..models.season_entities_insert_update_season_payload_season_teams_post_body_status import (
    SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBody")


@_attrs_define
class SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBody:
    """
    Attributes:
        season_id (UUID): The unique identifier of the season Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        roster_status (Union[Unset, SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyRosterStatus]): The status
            of the TEAM season teams
            >- `APPROVED` Approved
            >- `PENDING` Pending
            >- `REJECTED` Rejected
            >- `SUBMITTED` Submitted
            >- `UNKNOWN` Unknown
             Default: SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyRosterStatus.UNKNOWN. Example: APPROVED.
        status (Union[Unset, SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyStatus]): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        seed (Union[None, Unset, int]): Initial seeding Example: 1.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    season_id: UUID
    entity_id: Union[Unset, UUID] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    roster_status: Union[
        Unset, SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyRosterStatus
    ] = SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyRosterStatus.UNKNOWN
    status: Union[
        Unset, SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyStatus
    ] = UNSET
    seed: Union[None, Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id = str(self.season_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        roster_status: Union[Unset, str] = UNSET
        if not isinstance(self.roster_status, Unset):
            roster_status = self.roster_status.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        seed: Union[None, Unset, int]
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "seasonId": season_id,
            }
        )
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if roster_status is not UNSET:
            field_dict["rosterStatus"] = roster_status
        if status is not UNSET:
            field_dict["status"] = status
        if seed is not UNSET:
            field_dict["seed"] = seed
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season_id = UUID(d.pop("seasonId"))

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        def _parse_conference_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conference_id_type_0 = UUID(data)

                return conference_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        conference_id = _parse_conference_id(d.pop("conferenceId", UNSET))

        def _parse_division_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                division_id_type_0 = UUID(data)

                return division_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        division_id = _parse_division_id(d.pop("divisionId", UNSET))

        _roster_status = d.pop("rosterStatus", UNSET)
        roster_status: Union[
            Unset,
            SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyRosterStatus,
        ]
        if isinstance(_roster_status, Unset):
            roster_status = UNSET
        else:
            roster_status = (
                SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyRosterStatus(
                    _roster_status
                )
            )

        _status = d.pop("status", UNSET)
        status: Union[
            Unset, SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyStatus
        ]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeasonEntitiesInsertUpdateSeasonPayloadSeasonTeamsPostBodyStatus(
                _status
            )

        def _parse_seed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        season_entities_insert_update_season_payload_season_teams_post_body = cls(
            season_id=season_id,
            entity_id=entity_id,
            conference_id=conference_id,
            division_id=division_id,
            roster_status=roster_status,
            status=status,
            seed=seed,
            external_id=external_id,
        )

        return season_entities_insert_update_season_payload_season_teams_post_body
