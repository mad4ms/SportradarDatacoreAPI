import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_teams_model_roster_status import SeasonTeamsModelRosterStatus
from ..models.season_teams_model_status import SeasonTeamsModelStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.season_teams_model_conference import SeasonTeamsModelConference
    from ..models.season_teams_model_division import SeasonTeamsModelDivision
    from ..models.season_teams_model_entity import SeasonTeamsModelEntity
    from ..models.season_teams_model_organization import SeasonTeamsModelOrganization
    from ..models.season_teams_model_season import SeasonTeamsModelSeason


T = TypeVar("T", bound="SeasonTeamsModel")


@_attrs_define
class SeasonTeamsModel:
    """
    Attributes:
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeasonTeamsModelSeason]): The season linked to this record
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeasonTeamsModelOrganization]): The organization that this season teams belongs to
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity (Union[Unset, SeasonTeamsModelEntity]): The team information
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference (Union[Unset, SeasonTeamsModelConference]): The conference information
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division (Union[Unset, SeasonTeamsModelDivision]): The division information
        roster_status (Union[Unset, SeasonTeamsModelRosterStatus]): The status of the TEAM season teams
            >- `APPROVED` Approved
            >- `PENDING` Pending
            >- `REJECTED` Rejected
            >- `SUBMITTED` Submitted
            >- `UNKNOWN` Unknown
             Default: SeasonTeamsModelRosterStatus.UNKNOWN. Example: APPROVED.
        status (Union[Unset, SeasonTeamsModelStatus]): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        seed (Union[None, Unset, int]): Initial seeding Example: 1.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeasonTeamsModelSeason"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeasonTeamsModelOrganization"] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity: Union[Unset, "SeasonTeamsModelEntity"] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    conference: Union[Unset, "SeasonTeamsModelConference"] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    division: Union[Unset, "SeasonTeamsModelDivision"] = UNSET
    roster_status: Union[Unset, SeasonTeamsModelRosterStatus] = (
        SeasonTeamsModelRosterStatus.UNKNOWN
    )
    status: Union[Unset, SeasonTeamsModelStatus] = UNSET
    seed: Union[None, Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        conference: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conference, Unset):
            conference = self.conference.to_dict()

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        division: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.to_dict()

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
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity is not UNSET:
            field_dict["entity"] = entity
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if conference is not UNSET:
            field_dict["conference"] = conference
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if division is not UNSET:
            field_dict["division"] = division
        if roster_status is not UNSET:
            field_dict["rosterStatus"] = roster_status
        if status is not UNSET:
            field_dict["status"] = status
        if seed is not UNSET:
            field_dict["seed"] = seed
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_teams_model_conference import SeasonTeamsModelConference
        from ..models.season_teams_model_division import SeasonTeamsModelDivision
        from ..models.season_teams_model_entity import SeasonTeamsModelEntity
        from ..models.season_teams_model_organization import (
            SeasonTeamsModelOrganization,
        )
        from ..models.season_teams_model_season import SeasonTeamsModelSeason

        d = dict(src_dict)
        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeasonTeamsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeasonTeamsModelSeason.from_dict(_season)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeasonTeamsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeasonTeamsModelOrganization.from_dict(_organization)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, SeasonTeamsModelEntity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = SeasonTeamsModelEntity.from_dict(_entity)

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

        _conference = d.pop("conference", UNSET)
        conference: Union[Unset, SeasonTeamsModelConference]
        if isinstance(_conference, Unset):
            conference = UNSET
        else:
            conference = SeasonTeamsModelConference.from_dict(_conference)

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

        _division = d.pop("division", UNSET)
        division: Union[Unset, SeasonTeamsModelDivision]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = SeasonTeamsModelDivision.from_dict(_division)

        _roster_status = d.pop("rosterStatus", UNSET)
        roster_status: Union[Unset, SeasonTeamsModelRosterStatus]
        if isinstance(_roster_status, Unset):
            roster_status = UNSET
        else:
            roster_status = SeasonTeamsModelRosterStatus(_roster_status)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SeasonTeamsModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeasonTeamsModelStatus(_status)

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

        season_teams_model = cls(
            season_id=season_id,
            season=season,
            organization_id=organization_id,
            organization=organization,
            entity_id=entity_id,
            entity=entity,
            conference_id=conference_id,
            conference=conference,
            division_id=division_id,
            division=division,
            roster_status=roster_status,
            status=status,
            seed=seed,
            external_id=external_id,
            updated=updated,
            added=added,
        )

        return season_teams_model
