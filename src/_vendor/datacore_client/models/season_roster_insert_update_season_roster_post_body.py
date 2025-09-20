from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.season_roster_insert_update_season_roster_post_body_position_type_1 import (
    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType1,
)
from ..models.season_roster_insert_update_season_roster_post_body_position_type_2_type_1 import (
    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType2Type1,
)
from ..models.season_roster_insert_update_season_roster_post_body_position_type_3_type_1 import (
    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType3Type1,
)
from ..models.season_roster_insert_update_season_roster_post_body_status import (
    SeasonRosterInsertUpdateSeasonRosterPostBodyStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonRosterInsertUpdateSeasonRosterPostBody")


@_attrs_define
class SeasonRosterInsertUpdateSeasonRosterPostBody:
    """
    Attributes:
        status (SeasonRosterInsertUpdateSeasonRosterPostBodyStatus): Participation status
            >- `ACTIVE` Active
            >- `INJURED` Injured
            >- `OTHER_NOT_PARTICIPATING` Other Non-Participation
            >- `OUT` Out
            >- `SUSPENDED` Suspended
             Example: ACTIVE.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group_id (Union[None, UUID, Unset]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        position (Union[None, SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType1,
            SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType2Type1,
            SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType3Type1, Unset]): Playing position
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
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    status: SeasonRosterInsertUpdateSeasonRosterPostBodyStatus
    season_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    entity_group_id: Union[None, UUID, Unset] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    bib: Union[None, Unset, str] = UNSET
    position: Union[
        None,
        SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType1,
        SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType2Type1,
        SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType3Type1,
        Unset,
    ] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

        entity_group_id: Union[None, Unset, str]
        if isinstance(self.entity_group_id, Unset):
            entity_group_id = UNSET
        elif isinstance(self.entity_group_id, UUID):
            entity_group_id = str(self.entity_group_id)
        else:
            entity_group_id = self.entity_group_id

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        bib: Union[None, Unset, str]
        if isinstance(self.bib, Unset):
            bib = UNSET
        else:
            bib = self.bib

        position: Union[None, Unset, str]
        if isinstance(self.position, Unset):
            position = UNSET
        elif isinstance(
            self.position, SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType1
        ):
            position = self.position.value
        elif isinstance(
            self.position,
            SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType2Type1,
        ):
            position = self.position.value
        elif isinstance(
            self.position,
            SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType3Type1,
        ):
            position = self.position.value
        else:
            position = self.position

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if bib is not UNSET:
            field_dict["bib"] = bib
        if position is not UNSET:
            field_dict["position"] = position
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = SeasonRosterInsertUpdateSeasonRosterPostBodyStatus(d.pop("status"))

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

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

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

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
            None,
            SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType1,
            SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType2Type1,
            SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType3Type1,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_1 = (
                    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType1(data)
                )

                return position_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_2_type_1 = (
                    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType2Type1(data)
                )

                return position_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_3_type_1 = (
                    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType3Type1(data)
                )

                return position_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType1,
                    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType2Type1,
                    SeasonRosterInsertUpdateSeasonRosterPostBodyPositionType3Type1,
                    Unset,
                ],
                data,
            )

        position = _parse_position(d.pop("position", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        season_roster_insert_update_season_roster_post_body = cls(
            status=status,
            season_id=season_id,
            entity_id=entity_id,
            entity_group_id=entity_group_id,
            division_id=division_id,
            conference_id=conference_id,
            person_id=person_id,
            bib=bib,
            position=position,
            external_id=external_id,
        )

        return season_roster_insert_update_season_roster_post_body
