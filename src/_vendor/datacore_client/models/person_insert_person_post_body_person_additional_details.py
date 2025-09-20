from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.person_insert_person_post_body_person_additional_details_dominant_foot import (
    PersonInsertPersonPostBodyPersonAdditionalDetailsDominantFoot,
)
from ..models.person_insert_person_post_body_person_additional_details_dominant_hand import (
    PersonInsertPersonPostBodyPersonAdditionalDetailsDominantHand,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PersonInsertPersonPostBodyPersonAdditionalDetails")


@_attrs_define
class PersonInsertPersonPostBodyPersonAdditionalDetails:
    """Additional person detail fields

    Attributes:
        height (Union[None, Unset, float]): Height in cms
        height_imperial (Union[None, Unset, str]): Height in feet & inches
        weight (Union[None, Unset, float]): Weight in kgs
        weight_imperial (Union[None, Unset, float]): Weight in pounds
        dominant_hand (Union[Unset, PersonInsertPersonPostBodyPersonAdditionalDetailsDominantHand]): Dominant hand
        dominant_foot (Union[Unset, PersonInsertPersonPostBodyPersonAdditionalDetailsDominantFoot]): Dominant foot
        home_town (Union[None, Unset, str]): Hometown
        school (Union[None, Unset, str]): School
        school_class (Union[None, Unset, str]): School Class
        college (Union[None, Unset, str]): College
        college_class (Union[None, Unset, str]): College Class
        representation (Union[None, Unset, str]): Representation
        junior_association_league (Union[None, Unset, str]): Junior Association / League
    """

    height: Union[None, Unset, float] = UNSET
    height_imperial: Union[None, Unset, str] = UNSET
    weight: Union[None, Unset, float] = UNSET
    weight_imperial: Union[None, Unset, float] = UNSET
    dominant_hand: Union[
        Unset, PersonInsertPersonPostBodyPersonAdditionalDetailsDominantHand
    ] = UNSET
    dominant_foot: Union[
        Unset, PersonInsertPersonPostBodyPersonAdditionalDetailsDominantFoot
    ] = UNSET
    home_town: Union[None, Unset, str] = UNSET
    school: Union[None, Unset, str] = UNSET
    school_class: Union[None, Unset, str] = UNSET
    college: Union[None, Unset, str] = UNSET
    college_class: Union[None, Unset, str] = UNSET
    representation: Union[None, Unset, str] = UNSET
    junior_association_league: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        height: Union[None, Unset, float]
        if isinstance(self.height, Unset):
            height = UNSET
        else:
            height = self.height

        height_imperial: Union[None, Unset, str]
        if isinstance(self.height_imperial, Unset):
            height_imperial = UNSET
        else:
            height_imperial = self.height_imperial

        weight: Union[None, Unset, float]
        if isinstance(self.weight, Unset):
            weight = UNSET
        else:
            weight = self.weight

        weight_imperial: Union[None, Unset, float]
        if isinstance(self.weight_imperial, Unset):
            weight_imperial = UNSET
        else:
            weight_imperial = self.weight_imperial

        dominant_hand: Union[Unset, str] = UNSET
        if not isinstance(self.dominant_hand, Unset):
            dominant_hand = self.dominant_hand.value

        dominant_foot: Union[Unset, str] = UNSET
        if not isinstance(self.dominant_foot, Unset):
            dominant_foot = self.dominant_foot.value

        home_town: Union[None, Unset, str]
        if isinstance(self.home_town, Unset):
            home_town = UNSET
        else:
            home_town = self.home_town

        school: Union[None, Unset, str]
        if isinstance(self.school, Unset):
            school = UNSET
        else:
            school = self.school

        school_class: Union[None, Unset, str]
        if isinstance(self.school_class, Unset):
            school_class = UNSET
        else:
            school_class = self.school_class

        college: Union[None, Unset, str]
        if isinstance(self.college, Unset):
            college = UNSET
        else:
            college = self.college

        college_class: Union[None, Unset, str]
        if isinstance(self.college_class, Unset):
            college_class = UNSET
        else:
            college_class = self.college_class

        representation: Union[None, Unset, str]
        if isinstance(self.representation, Unset):
            representation = UNSET
        else:
            representation = self.representation

        junior_association_league: Union[None, Unset, str]
        if isinstance(self.junior_association_league, Unset):
            junior_association_league = UNSET
        else:
            junior_association_league = self.junior_association_league

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if height is not UNSET:
            field_dict["height"] = height
        if height_imperial is not UNSET:
            field_dict["heightImperial"] = height_imperial
        if weight is not UNSET:
            field_dict["weight"] = weight
        if weight_imperial is not UNSET:
            field_dict["weightImperial"] = weight_imperial
        if dominant_hand is not UNSET:
            field_dict["dominantHand"] = dominant_hand
        if dominant_foot is not UNSET:
            field_dict["dominantFoot"] = dominant_foot
        if home_town is not UNSET:
            field_dict["homeTown"] = home_town
        if school is not UNSET:
            field_dict["school"] = school
        if school_class is not UNSET:
            field_dict["schoolClass"] = school_class
        if college is not UNSET:
            field_dict["college"] = college
        if college_class is not UNSET:
            field_dict["collegeClass"] = college_class
        if representation is not UNSET:
            field_dict["representation"] = representation
        if junior_association_league is not UNSET:
            field_dict["juniorAssociationLeague"] = junior_association_league

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_height(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        height = _parse_height(d.pop("height", UNSET))

        def _parse_height_imperial(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        height_imperial = _parse_height_imperial(d.pop("heightImperial", UNSET))

        def _parse_weight(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        weight = _parse_weight(d.pop("weight", UNSET))

        def _parse_weight_imperial(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        weight_imperial = _parse_weight_imperial(d.pop("weightImperial", UNSET))

        _dominant_hand = d.pop("dominantHand", UNSET)
        dominant_hand: Union[
            Unset, PersonInsertPersonPostBodyPersonAdditionalDetailsDominantHand
        ]
        if isinstance(_dominant_hand, Unset):
            dominant_hand = UNSET
        else:
            dominant_hand = (
                PersonInsertPersonPostBodyPersonAdditionalDetailsDominantHand(
                    _dominant_hand
                )
            )

        _dominant_foot = d.pop("dominantFoot", UNSET)
        dominant_foot: Union[
            Unset, PersonInsertPersonPostBodyPersonAdditionalDetailsDominantFoot
        ]
        if isinstance(_dominant_foot, Unset):
            dominant_foot = UNSET
        else:
            dominant_foot = (
                PersonInsertPersonPostBodyPersonAdditionalDetailsDominantFoot(
                    _dominant_foot
                )
            )

        def _parse_home_town(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        home_town = _parse_home_town(d.pop("homeTown", UNSET))

        def _parse_school(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        school = _parse_school(d.pop("school", UNSET))

        def _parse_school_class(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        school_class = _parse_school_class(d.pop("schoolClass", UNSET))

        def _parse_college(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        college = _parse_college(d.pop("college", UNSET))

        def _parse_college_class(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        college_class = _parse_college_class(d.pop("collegeClass", UNSET))

        def _parse_representation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        representation = _parse_representation(d.pop("representation", UNSET))

        def _parse_junior_association_league(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        junior_association_league = _parse_junior_association_league(
            d.pop("juniorAssociationLeague", UNSET)
        )

        person_insert_person_post_body_person_additional_details = cls(
            height=height,
            height_imperial=height_imperial,
            weight=weight,
            weight_imperial=weight_imperial,
            dominant_hand=dominant_hand,
            dominant_foot=dominant_foot,
            home_town=home_town,
            school=school,
            school_class=school_class,
            college=college,
            college_class=college_class,
            representation=representation,
            junior_association_league=junior_association_league,
        )

        return person_insert_person_post_body_person_additional_details
