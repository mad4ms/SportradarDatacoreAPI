import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fixture_progression_model_fixture import (
        FixtureProgressionModelFixture,
    )
    from ..models.fixture_progression_model_organization import (
        FixtureProgressionModelOrganization,
    )
    from ..models.fixture_progression_model_season import FixtureProgressionModelSeason


T = TypeVar("T", bound="FixtureProgressionModel")


@_attrs_define
class FixtureProgressionModel:
    """
    Attributes:
        fixture_id (Union[Unset, UUID]): Source fixtureId Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, FixtureProgressionModelFixture]): The match
        to_fixture_id (Union[Unset, UUID]): Destination fixtureId Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, FixtureProgressionModelOrganization]): The organization that this
            ~fixture_progression~ belongs to
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, FixtureProgressionModelSeason]): The season linked to this record
        placing_after (Union[Unset, int]): Place after source match completion Example: 1.
        is_home (Union[Unset, bool]): Will this competitor be the 'home' team in the target match? Example: True.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "FixtureProgressionModelFixture"] = UNSET
    to_fixture_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "FixtureProgressionModelOrganization"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "FixtureProgressionModelSeason"] = UNSET
    placing_after: Union[Unset, int] = UNSET
    is_home: Union[Unset, bool] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        fixture: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fixture, Unset):
            fixture = self.fixture.to_dict()

        to_fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.to_fixture_id, Unset):
            to_fixture_id = str(self.to_fixture_id)

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

        placing_after = self.placing_after

        is_home = self.is_home

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if to_fixture_id is not UNSET:
            field_dict["toFixtureId"] = to_fixture_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if placing_after is not UNSET:
            field_dict["placingAfter"] = placing_after
        if is_home is not UNSET:
            field_dict["isHome"] = is_home
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fixture_progression_model_fixture import (
            FixtureProgressionModelFixture,
        )
        from ..models.fixture_progression_model_organization import (
            FixtureProgressionModelOrganization,
        )
        from ..models.fixture_progression_model_season import (
            FixtureProgressionModelSeason,
        )

        d = dict(src_dict)
        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, FixtureProgressionModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = FixtureProgressionModelFixture.from_dict(_fixture)

        _to_fixture_id = d.pop("toFixtureId", UNSET)
        to_fixture_id: Union[Unset, UUID]
        if isinstance(_to_fixture_id, Unset):
            to_fixture_id = UNSET
        else:
            to_fixture_id = UUID(_to_fixture_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, FixtureProgressionModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = FixtureProgressionModelOrganization.from_dict(_organization)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, FixtureProgressionModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = FixtureProgressionModelSeason.from_dict(_season)

        placing_after = d.pop("placingAfter", UNSET)

        is_home = d.pop("isHome", UNSET)

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

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        fixture_progression_model = cls(
            fixture_id=fixture_id,
            fixture=fixture,
            to_fixture_id=to_fixture_id,
            organization_id=organization_id,
            organization=organization,
            season_id=season_id,
            season=season,
            placing_after=placing_after,
            is_home=is_home,
            updated=updated,
            added=added,
            external_id=external_id,
        )

        return fixture_progression_model
