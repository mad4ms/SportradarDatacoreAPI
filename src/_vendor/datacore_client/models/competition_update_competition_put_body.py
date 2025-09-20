from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.competition_update_competition_put_body_age_group_type_1 import (
    CompetitionUpdateCompetitionPutBodyAgeGroupType1,
)
from ..models.competition_update_competition_put_body_age_group_type_2_type_1 import (
    CompetitionUpdateCompetitionPutBodyAgeGroupType2Type1,
)
from ..models.competition_update_competition_put_body_age_group_type_3_type_1 import (
    CompetitionUpdateCompetitionPutBodyAgeGroupType3Type1,
)
from ..models.competition_update_competition_put_body_event_type import (
    CompetitionUpdateCompetitionPutBodyEventType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.competition_update_competition_put_body_competition_historical_name import (
        CompetitionUpdateCompetitionPutBodyCompetitionHistoricalName,
    )
    from ..models.competition_update_competition_put_body_social_media import (
        CompetitionUpdateCompetitionPutBodySocialMedia,
    )


T = TypeVar("T", bound="CompetitionUpdateCompetitionPutBody")


@_attrs_define
class CompetitionUpdateCompetitionPutBody:
    """
    Attributes:
        league_id (Union[Unset, UUID]): The unique identifier of the league Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        international_reference (Union[None, Unset, str]): The international reference for this competition given by the
            sport governing body Example: CA3243-3.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_local (Union[Unset, str]): The name of the competition in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: Test name local.
        event_type (Union[Unset, CompetitionUpdateCompetitionPutBodyEventType]): Primary Type of Matches
            >- `FIXTURE` Fixture
            >- `PRACTICE` Practice
             Default: CompetitionUpdateCompetitionPutBodyEventType.FIXTURE. Example: FIXTURE.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the competition in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test name latin .
        social (Union['CompetitionUpdateCompetitionPutBodySocialMedia', None, Unset]): Social Media contacts
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        historical_names (Union[None, Unset, list['CompetitionUpdateCompetitionPutBodyCompetitionHistoricalName']]):
            Array of competition historical names
        age_group (Union[CompetitionUpdateCompetitionPutBodyAgeGroupType1,
            CompetitionUpdateCompetitionPutBodyAgeGroupType2Type1, CompetitionUpdateCompetitionPutBodyAgeGroupType3Type1,
            None, Unset]): The age group of the competition
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
    """

    league_id: Union[Unset, UUID] = UNSET
    international_reference: Union[None, Unset, str] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    name_local: Union[Unset, str] = UNSET
    event_type: Union[Unset, CompetitionUpdateCompetitionPutBodyEventType] = (
        CompetitionUpdateCompetitionPutBodyEventType.FIXTURE
    )
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    social: Union["CompetitionUpdateCompetitionPutBodySocialMedia", None, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    historical_names: Union[
        None,
        Unset,
        list["CompetitionUpdateCompetitionPutBodyCompetitionHistoricalName"],
    ] = UNSET
    age_group: Union[
        CompetitionUpdateCompetitionPutBodyAgeGroupType1,
        CompetitionUpdateCompetitionPutBodyAgeGroupType2Type1,
        CompetitionUpdateCompetitionPutBodyAgeGroupType3Type1,
        None,
        Unset,
    ] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.competition_update_competition_put_body_social_media import (
            CompetitionUpdateCompetitionPutBodySocialMedia,
        )

        league_id: Union[Unset, str] = UNSET
        if not isinstance(self.league_id, Unset):
            league_id = str(self.league_id)

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
        elif isinstance(self.social, CompetitionUpdateCompetitionPutBodySocialMedia):
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
                historical_names_type_0_item = (
                    historical_names_type_0_item_data.to_dict()
                )
                historical_names.append(historical_names_type_0_item)

        else:
            historical_names = self.historical_names

        age_group: Union[None, Unset, str]
        if isinstance(self.age_group, Unset):
            age_group = UNSET
        elif isinstance(
            self.age_group, CompetitionUpdateCompetitionPutBodyAgeGroupType1
        ):
            age_group = self.age_group.value
        elif isinstance(
            self.age_group, CompetitionUpdateCompetitionPutBodyAgeGroupType2Type1
        ):
            age_group = self.age_group.value
        elif isinstance(
            self.age_group, CompetitionUpdateCompetitionPutBodyAgeGroupType3Type1
        ):
            age_group = self.age_group.value
        else:
            age_group = self.age_group

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if league_id is not UNSET:
            field_dict["leagueId"] = league_id
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
        if age_group is not UNSET:
            field_dict["ageGroup"] = age_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.competition_update_competition_put_body_competition_historical_name import (
            CompetitionUpdateCompetitionPutBodyCompetitionHistoricalName,
        )
        from ..models.competition_update_competition_put_body_social_media import (
            CompetitionUpdateCompetitionPutBodySocialMedia,
        )

        d = dict(src_dict)
        _league_id = d.pop("leagueId", UNSET)
        league_id: Union[Unset, UUID]
        if isinstance(_league_id, Unset):
            league_id = UNSET
        else:
            league_id = UUID(_league_id)

        def _parse_international_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        international_reference = _parse_international_reference(
            d.pop("internationalReference", UNSET)
        )

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(
            d.pop("abbreviationLocal", UNSET)
        )

        name_local = d.pop("nameLocal", UNSET)

        _event_type = d.pop("eventType", UNSET)
        event_type: Union[Unset, CompetitionUpdateCompetitionPutBodyEventType]
        if isinstance(_event_type, Unset):
            event_type = UNSET
        else:
            event_type = CompetitionUpdateCompetitionPutBodyEventType(_event_type)

        def _parse_abbreviation_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_latin = _parse_abbreviation_latin(
            d.pop("abbreviationLatin", UNSET)
        )

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_social(
            data: object,
        ) -> Union["CompetitionUpdateCompetitionPutBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = (
                    CompetitionUpdateCompetitionPutBodySocialMedia.from_dict(data)
                )

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["CompetitionUpdateCompetitionPutBodySocialMedia", None, Unset],
                data,
            )

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
        ) -> Union[
            None,
            Unset,
            list["CompetitionUpdateCompetitionPutBodyCompetitionHistoricalName"],
        ]:
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
                    historical_names_type_0_item = CompetitionUpdateCompetitionPutBodyCompetitionHistoricalName.from_dict(
                        historical_names_type_0_item_data
                    )

                    historical_names_type_0.append(historical_names_type_0_item)

                return historical_names_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    None,
                    Unset,
                    list[
                        "CompetitionUpdateCompetitionPutBodyCompetitionHistoricalName"
                    ],
                ],
                data,
            )

        historical_names = _parse_historical_names(d.pop("historicalNames", UNSET))

        def _parse_age_group(
            data: object,
        ) -> Union[
            CompetitionUpdateCompetitionPutBodyAgeGroupType1,
            CompetitionUpdateCompetitionPutBodyAgeGroupType2Type1,
            CompetitionUpdateCompetitionPutBodyAgeGroupType3Type1,
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
                age_group_type_1 = CompetitionUpdateCompetitionPutBodyAgeGroupType1(
                    data
                )

                return age_group_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                age_group_type_2_type_1 = (
                    CompetitionUpdateCompetitionPutBodyAgeGroupType2Type1(data)
                )

                return age_group_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                age_group_type_3_type_1 = (
                    CompetitionUpdateCompetitionPutBodyAgeGroupType3Type1(data)
                )

                return age_group_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    CompetitionUpdateCompetitionPutBodyAgeGroupType1,
                    CompetitionUpdateCompetitionPutBodyAgeGroupType2Type1,
                    CompetitionUpdateCompetitionPutBodyAgeGroupType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        age_group = _parse_age_group(d.pop("ageGroup", UNSET))

        competition_update_competition_put_body = cls(
            league_id=league_id,
            international_reference=international_reference,
            abbreviation_local=abbreviation_local,
            name_local=name_local,
            event_type=event_type,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            social=social,
            external_id=external_id,
            historical_names=historical_names,
            age_group=age_group,
        )

        return competition_update_competition_put_body
