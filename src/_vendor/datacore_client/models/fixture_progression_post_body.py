from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FixtureProgressionPostBody")


@_attrs_define
class FixtureProgressionPostBody:
    """
    Attributes:
        fixture_id (UUID): Source fixtureId Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_fixture_id (UUID): Destination fixtureId Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        placing_after (Union[Unset, int]): Place after source match completion Example: 1.
        is_home (Union[Unset, bool]): Will this competitor be the 'home' team in the target match? Example: True.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    fixture_id: UUID
    to_fixture_id: UUID
    season_id: Union[Unset, UUID] = UNSET
    placing_after: Union[Unset, int] = UNSET
    is_home: Union[Unset, bool] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id = str(self.fixture_id)

        to_fixture_id = str(self.to_fixture_id)

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        placing_after = self.placing_after

        is_home = self.is_home

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fixtureId": fixture_id,
                "toFixtureId": to_fixture_id,
            }
        )
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if placing_after is not UNSET:
            field_dict["placingAfter"] = placing_after
        if is_home is not UNSET:
            field_dict["isHome"] = is_home
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixture_id = UUID(d.pop("fixtureId"))

        to_fixture_id = UUID(d.pop("toFixtureId"))

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        placing_after = d.pop("placingAfter", UNSET)

        is_home = d.pop("isHome", UNSET)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        fixture_progression_post_body = cls(
            fixture_id=fixture_id,
            to_fixture_id=to_fixture_id,
            season_id=season_id,
            placing_after=placing_after,
            is_home=is_home,
            external_id=external_id,
        )

        return fixture_progression_post_body
