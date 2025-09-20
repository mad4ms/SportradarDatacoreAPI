from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.fixture_roster_insert_update_base_route_match_roster_post_body_position_type_1 import (
    FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType1,
)
from ..models.fixture_roster_insert_update_base_route_match_roster_post_body_position_type_2_type_1 import (
    FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType2Type1,
)
from ..models.fixture_roster_insert_update_base_route_match_roster_post_body_position_type_3_type_1 import (
    FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FixtureRosterInsertUpdateBaseRouteMatchRosterPostBody")


@_attrs_define
class FixtureRosterInsertUpdateBaseRouteMatchRosterPostBody:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]): The unique identifier of the team Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        bib (Union[None, Unset, str]): The number displayed on the jersey Example: 34.
        position (Union[FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType1,
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType2Type1,
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType3Type1, None, Unset]): Playing position
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
        starter (Union[Unset, bool]): Did person start the match on the court Example: True.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    fixture_id: Union[Unset, UUID] = UNSET
    entity_id: Union[Unset, UUID] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    bib: Union[None, Unset, str] = UNSET
    position: Union[
        FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType1,
        FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType2Type1,
        FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType3Type1,
        None,
        Unset,
    ] = UNSET
    starter: Union[Unset, bool] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        entity_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_id, Unset):
            entity_id = str(self.entity_id)

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
            self.position,
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType1,
        ):
            position = self.position.value
        elif isinstance(
            self.position,
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType2Type1,
        ):
            position = self.position.value
        elif isinstance(
            self.position,
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType3Type1,
        ):
            position = self.position.value
        else:
            position = self.position

        starter = self.starter

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if bib is not UNSET:
            field_dict["bib"] = bib
        if position is not UNSET:
            field_dict["position"] = position
        if starter is not UNSET:
            field_dict["starter"] = starter
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _entity_id = d.pop("entityId", UNSET)
        entity_id: Union[Unset, UUID]
        if isinstance(_entity_id, Unset):
            entity_id = UNSET
        else:
            entity_id = UUID(_entity_id)

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
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType1,
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType2Type1,
            FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType3Type1,
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
                position_type_1 = (
                    FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType1(
                        data
                    )
                )

                return position_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_2_type_1 = FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType2Type1(
                    data
                )

                return position_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                position_type_3_type_1 = FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType3Type1(
                    data
                )

                return position_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType1,
                    FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType2Type1,
                    FixtureRosterInsertUpdateBaseRouteMatchRosterPostBodyPositionType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        position = _parse_position(d.pop("position", UNSET))

        starter = d.pop("starter", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        fixture_roster_insert_update_base_route_match_roster_post_body = cls(
            fixture_id=fixture_id,
            entity_id=entity_id,
            person_id=person_id,
            bib=bib,
            position=position,
            starter=starter,
            external_id=external_id,
        )

        return fixture_roster_insert_update_base_route_match_roster_post_body
