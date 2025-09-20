import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.seasonperson_placings_model_organization import (
        SEASONPERSONPlacingsModelOrganization,
    )
    from ..models.seasonperson_placings_model_person import (
        SEASONPERSONPlacingsModelPerson,
    )
    from ..models.seasonperson_placings_model_season import (
        SEASONPERSONPlacingsModelSeason,
    )


T = TypeVar("T", bound="SEASONPERSONPlacingsModel")


@_attrs_define
class SEASONPERSONPlacingsModel:
    """
    Attributes:
        placing_id (Union[Unset, UUID]): The unique identifier of the SEASON PERSON placing Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SEASONPERSONPlacingsModelOrganization]): The organization that this SEASON PERSON
            placings belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SEASONPERSONPlacingsModelSeason]): The season linked to this record
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person (Union[Unset, SEASONPERSONPlacingsModelPerson]): The person information
        result_place (Union[Unset, int]): Result place Example: 1.
        points (Union[None, Unset, int]): Points awarded Example: 1.
        prize_money (Union[None, Unset, int]): Prize money awarded Example: 1.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    placing_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SEASONPERSONPlacingsModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SEASONPERSONPlacingsModelSeason"] = UNSET
    person_id: Union[Unset, UUID] = UNSET
    person: Union[Unset, "SEASONPERSONPlacingsModelPerson"] = UNSET
    result_place: Union[Unset, int] = UNSET
    points: Union[None, Unset, int] = UNSET
    prize_money: Union[None, Unset, int] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        placing_id: Union[Unset, str] = UNSET
        if not isinstance(self.placing_id, Unset):
            placing_id = str(self.placing_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        person: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        result_place = self.result_place

        points: Union[None, Unset, int]
        if isinstance(self.points, Unset):
            points = UNSET
        else:
            points = self.points

        prize_money: Union[None, Unset, int]
        if isinstance(self.prize_money, Unset):
            prize_money = UNSET
        else:
            prize_money = self.prize_money

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if placing_id is not UNSET:
            field_dict["placingId"] = placing_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person is not UNSET:
            field_dict["person"] = person
        if result_place is not UNSET:
            field_dict["resultPlace"] = result_place
        if points is not UNSET:
            field_dict["points"] = points
        if prize_money is not UNSET:
            field_dict["prizeMoney"] = prize_money
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.seasonperson_placings_model_organization import (
            SEASONPERSONPlacingsModelOrganization,
        )
        from ..models.seasonperson_placings_model_person import (
            SEASONPERSONPlacingsModelPerson,
        )
        from ..models.seasonperson_placings_model_season import (
            SEASONPERSONPlacingsModelSeason,
        )

        d = dict(src_dict)
        _placing_id = d.pop("placingId", UNSET)
        placing_id: Union[Unset, UUID]
        if isinstance(_placing_id, Unset):
            placing_id = UNSET
        else:
            placing_id = UUID(_placing_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SEASONPERSONPlacingsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SEASONPERSONPlacingsModelOrganization.from_dict(
                _organization
            )

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SEASONPERSONPlacingsModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SEASONPERSONPlacingsModelSeason.from_dict(_season)

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _person = d.pop("person", UNSET)
        person: Union[Unset, SEASONPERSONPlacingsModelPerson]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = SEASONPERSONPlacingsModelPerson.from_dict(_person)

        result_place = d.pop("resultPlace", UNSET)

        def _parse_points(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        points = _parse_points(d.pop("points", UNSET))

        def _parse_prize_money(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        prize_money = _parse_prize_money(d.pop("prizeMoney", UNSET))

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

        seasonperson_placings_model = cls(
            placing_id=placing_id,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            person_id=person_id,
            person=person,
            result_place=result_place,
            points=points,
            prize_money=prize_money,
            updated=updated,
            added=added,
        )

        return seasonperson_placings_model
