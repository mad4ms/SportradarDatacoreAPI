import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.competition_model_age_group_type_1 import CompetitionModelAgeGroupType1
from ..models.competition_model_age_group_type_2_type_1 import CompetitionModelAgeGroupType2Type1
from ..models.competition_model_age_group_type_3_type_1 import CompetitionModelAgeGroupType3Type1
from ..models.competition_model_event_type import CompetitionModelEventType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_model_competition_historical_name import CompetitionModelCompetitionHistoricalName
    from ..models.competition_model_league import CompetitionModelLeague
    from ..models.competition_model_organization import CompetitionModelOrganization
    from ..models.competition_model_social_media import CompetitionModelSocialMedia
    from ..models.images_model import ImagesModel


T = TypeVar("T", bound="CompetitionModel")


@_attrs_define
class CompetitionModel:
    """
    Attributes:
        competition_id (Union[Unset, UUID]): The unique identifier of the competition Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, CompetitionModelOrganization]): The organization that this competition belongs to
        league_id (Union[Unset, UUID]): The unique identifier of the league Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        league (Union[Unset, CompetitionModelLeague]): The league that this competition belongs to
        international_reference (Union[None, Unset, str]): The international reference for this competition given by the
            sport governing body Example: CA3243-3.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_local (Union[Unset, str]): The name of the competition in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: Test name local.
        event_type (Union[Unset, CompetitionModelEventType]): Primary Type of Matches
            >- `FIXTURE` Fixture
            >- `PRACTICE` Practice
             Default: CompetitionModelEventType.FIXTURE. Example: FIXTURE.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the competition in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test name latin .
        social (Union['CompetitionModelSocialMedia', None, Unset]): Social Media contacts
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        historical_names (Union[None, Unset, list['CompetitionModelCompetitionHistoricalName']]): Array of competition
            historical names
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        age_group (Union[CompetitionModelAgeGroupType1, CompetitionModelAgeGroupType2Type1,
            CompetitionModelAgeGroupType3Type1, None, Unset]): The age group of the competition
            >- None None
            >- `JUNIOR` Junior
            >- `MASTERS` Masters
            >- `SENIOR` Senior
            >- `UNDER_15` Under 15
            >- `UNDER_16` Under 16
            >- `UNDER_17` Under 17
            >- `UNDER_18` Under 18
            >- `UNDER_19` Under 19
            >- `UNDER_20` Under 20
            >- `UNDER_21` Under 21
            >- `UNDER_22` Under 22
            >- `UNDER_23` Under 23
            >- `YOUTH` Youth
             Example: SENIOR.
        images (Union[Unset, list['ImagesModel']]):
    """

    competition_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "CompetitionModelOrganization"] = UNSET
    league_id: Union[Unset, UUID] = UNSET
    league: Union[Unset, "CompetitionModelLeague"] = UNSET
    international_reference: Union[None, Unset, str] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    name_local: Union[Unset, str] = UNSET
    event_type: Union[Unset, CompetitionModelEventType] = CompetitionModelEventType.FIXTURE
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    social: Union["CompetitionModelSocialMedia", None, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    historical_names: Union[None, Unset, list["CompetitionModelCompetitionHistoricalName"]] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    age_group: Union[
        CompetitionModelAgeGroupType1,
        CompetitionModelAgeGroupType2Type1,
        CompetitionModelAgeGroupType3Type1,
        None,
        Unset,
    ] = UNSET
    images: Union[Unset, list["ImagesModel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.competition_model_social_media import CompetitionModelSocialMedia

        competition_id: Union[Unset, str] = UNSET
        if not isinstance(self.competition_id, Unset):
            competition_id = str(self.competition_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        league_id: Union[Unset, str] = UNSET
        if not isinstance(self.league_id, Unset):
            league_id = str(self.league_id)

        league: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.league, Unset):
            league = self.league.to_dict()

        international_reference: Union[None, Unset, str]
        if isinstance(self.international_reference, Unset):
            international_reference = UNSET
        else:
            international_reference = self.international_reference

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        name_local = self.name_local

        event_type: Union[Unset, str] = UNSET
        if not isinstance(self.event_type, Unset):
            event_type = self.event_type.value

        abbreviation_latin: Union[None, Unset, str]
        if isinstance(self.abbreviation_latin, Unset):
            abbreviation_latin = UNSET
        else:
            abbreviation_latin = self.abbreviation_latin

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        social: Union[None, Unset, dict[str, Any]]
        if isinstance(self.social, Unset):
            social = UNSET
        elif isinstance(self.social, CompetitionModelSocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        historical_names: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.historical_names, Unset):
            historical_names = UNSET
        elif isinstance(self.historical_names, list):
            historical_names = []
            for historical_names_type_0_item_data in self.historical_names:
                historical_names_type_0_item = historical_names_type_0_item_data.to_dict()
                historical_names.append(historical_names_type_0_item)

        else:
            historical_names = self.historical_names

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        age_group: Union[None, Unset, str]
        if isinstance(self.age_group, Unset):
            age_group = UNSET
        elif isinstance(self.age_group, CompetitionModelAgeGroupType1):
            age_group = self.age_group.value
        elif isinstance(self.age_group, CompetitionModelAgeGroupType2Type1):
            age_group = self.age_group.value
        elif isinstance(self.age_group, CompetitionModelAgeGroupType3Type1):
            age_group = self.age_group.value
        else:
            age_group = self.age_group

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if competition_id is not UNSET:
            field_dict["competitionId"] = competition_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
        if league is not UNSET:
            field_dict["league"] = league
        if international_reference is not UNSET:
            field_dict["internationalReference"] = international_reference
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if social is not UNSET:
            field_dict["social"] = social
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if historical_names is not UNSET:
            field_dict["historicalNames"] = historical_names
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if age_group is not UNSET:
            field_dict["ageGroup"] = age_group
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competition_model_competition_historical_name import CompetitionModelCompetitionHistoricalName
        from ..models.competition_model_league import CompetitionModelLeague
        from ..models.competition_model_organization import CompetitionModelOrganization
        from ..models.competition_model_social_media import CompetitionModelSocialMedia
        from ..models.images_model import ImagesModel

        d = dict(src_dict)
        _competition_id = d.pop("competitionId", UNSET)
        competition_id: Union[Unset, UUID]
        if isinstance(_competition_id, Unset):
            competition_id = UNSET
        else:
            competition_id = UUID(_competition_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, CompetitionModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = CompetitionModelOrganization.from_dict(_organization)

        _league_id = d.pop("leagueId", UNSET)
        league_id: Union[Unset, UUID]
        if isinstance(_league_id, Unset):
            league_id = UNSET
        else:
            league_id = UUID(_league_id)

        _league = d.pop("league", UNSET)
        league: Union[Unset, CompetitionModelLeague]
        if isinstance(_league, Unset):
            league = UNSET
        else:
            league = CompetitionModelLeague.from_dict(_league)

        def _parse_international_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        international_reference = _parse_international_reference(d.pop("internationalReference", UNSET))

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(d.pop("abbreviationLocal", UNSET))

        name_local = d.pop("nameLocal", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, CompetitionModelEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = CompetitionModelEventType(_event_type)

        def _parse_abbreviation_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_latin = _parse_abbreviation_latin(d.pop("abbreviationLatin", UNSET))

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_social(data: object) -> Union["CompetitionModelSocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = CompetitionModelSocialMedia.from_dict(data)

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CompetitionModelSocialMedia", None, Unset], data)

        social = _parse_social(d.pop("social", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        def _parse_historical_names(
            data: object,
        ) -> Union[None, Unset, list["CompetitionModelCompetitionHistoricalName"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                historical_names_type_0 = []
                _historical_names_type_0 = data
                for historical_names_type_0_item_data in _historical_names_type_0:
                    historical_names_type_0_item = CompetitionModelCompetitionHistoricalName.from_dict(
                        historical_names_type_0_item_data
                    )

                    historical_names_type_0.append(historical_names_type_0_item)

                return historical_names_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["CompetitionModelCompetitionHistoricalName"]], data)

        historical_names = _parse_historical_names(d.pop("historicalNames", UNSET))

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

        def _parse_age_group(
            data: object,
        ) -> Union[
            CompetitionModelAgeGroupType1,
            CompetitionModelAgeGroupType2Type1,
            CompetitionModelAgeGroupType3Type1,
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
                age_group_type_1 = CompetitionModelAgeGroupType1(data)

                return age_group_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                age_group_type_2_type_1 = CompetitionModelAgeGroupType2Type1(data)

                return age_group_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                age_group_type_3_type_1 = CompetitionModelAgeGroupType3Type1(data)

                return age_group_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    CompetitionModelAgeGroupType1,
                    CompetitionModelAgeGroupType2Type1,
                    CompetitionModelAgeGroupType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        age_group = _parse_age_group(d.pop("ageGroup", UNSET))

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ImagesModel.from_dict(images_item_data)

            images.append(images_item)

        competition_model = cls(
            competition_id=competition_id,
            organization_id=organization_id,
            organization=organization,
            league_id=league_id,
            league=league,
            international_reference=international_reference,
            abbreviation_local=abbreviation_local,
            name_local=name_local,
            event_type=event_type,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            social=social,
            external_id=external_id,
            historical_names=historical_names,
            updated=updated,
            added=added,
            age_group=age_group,
            images=images,
        )

        return competition_model
