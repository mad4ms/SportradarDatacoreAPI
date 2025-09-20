from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.head_to_head_entity_model_competition import (
        HeadToHeadEntityModelCompetition,
    )
    from ..models.head_to_head_entity_model_fixture import HeadToHeadEntityModelFixture
    from ..models.head_to_head_entity_model_organization import (
        HeadToHeadEntityModelOrganization,
    )
    from ..models.head_to_head_entity_model_season import HeadToHeadEntityModelSeason


T = TypeVar("T", bound="HeadToHeadEntityModel")


@_attrs_define
class HeadToHeadEntityModel:
    """
    Attributes:
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, HeadToHeadEntityModelOrganization]): The organization that this head_to_head_entity
            belongs to
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        fixture (Union[Unset, HeadToHeadEntityModelFixture]): The match
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, HeadToHeadEntityModelSeason]): The season linked to this record
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competition (Union[Unset, HeadToHeadEntityModelCompetition]): The competition that this season belongs to
    """

    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "HeadToHeadEntityModelOrganization"] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    fixture: Union[Unset, "HeadToHeadEntityModelFixture"] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "HeadToHeadEntityModelSeason"] = UNSET
    competition_id: Union[Unset, UUID] = UNSET
    competition: Union[Unset, "HeadToHeadEntityModelCompetition"] = UNSET

    def to_dict(self) -> dict[str, Any]:
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

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        competition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.competition, Unset):
            competition = self.competition.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if fixture is not UNSET:
            field_dict["fixture"] = fixture
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if competition is not UNSET:
            field_dict["competition"] = competition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.head_to_head_entity_model_competition import (
            HeadToHeadEntityModelCompetition,
        )
        from ..models.head_to_head_entity_model_fixture import (
            HeadToHeadEntityModelFixture,
        )
        from ..models.head_to_head_entity_model_organization import (
            HeadToHeadEntityModelOrganization,
        )
        from ..models.head_to_head_entity_model_season import (
            HeadToHeadEntityModelSeason,
        )

        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, HeadToHeadEntityModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = HeadToHeadEntityModelOrganization.from_dict(_organization)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _fixture = d.pop("fixture", UNSET)
        fixture: Union[Unset, HeadToHeadEntityModelFixture]
        if isinstance(_fixture, Unset):
            fixture = UNSET
        else:
            fixture = HeadToHeadEntityModelFixture.from_dict(_fixture)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, HeadToHeadEntityModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = HeadToHeadEntityModelSeason.from_dict(_season)

        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        _competition = d.pop("competition", UNSET)
        competition: Union[Unset, HeadToHeadEntityModelCompetition]
        if isinstance(_competition, Unset):
            competition = UNSET
        else:
            competition = HeadToHeadEntityModelCompetition.from_dict(_competition)

        head_to_head_entity_model = cls(
            organization_id=organization_id,
            organization=organization,
            fixture_id=fixture_id,
            fixture=fixture,
            season_id=season_id,
            season=season,
            competition_id=competition_id,
            competition=competition,
        )

        return head_to_head_entity_model
