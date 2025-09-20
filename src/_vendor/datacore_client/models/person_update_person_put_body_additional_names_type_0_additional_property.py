from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar(
    "T", bound="PersonUpdatePersonPutBodyAdditionalNamesType0AdditionalProperty"
)


@_attrs_define
class PersonUpdatePersonPutBodyAdditionalNamesType0AdditionalProperty:
    """The *property name* here can either be `default` (for a non-language specific name) or a two letter (lower-case) ISO
    639-1 language code. eg `fr`, `es`

        Example:
            default

        Attributes:
            display (Union[None, Unset, str]):
            television (Union[None, Unset, str]): The name to be used on television
            scoreboard (Union[None, Unset, str]): The name to be used on the scoreboard
            pronunciation (Union[None, Unset, str]): The description of how to pronounce the name
            boxscore (Union[None, Unset, str]):
            jersey (Union[None, Unset, str]):
            abbreviated (Union[None, Unset, str]):
            given (Union[None, Unset, str]):
            family (Union[None, Unset, str]):
            full (Union[None, Unset, str]):
            known_as (Union[None, Unset, str]):
    """

    display: Union[None, Unset, str] = UNSET
    television: Union[None, Unset, str] = UNSET
    scoreboard: Union[None, Unset, str] = UNSET
    pronunciation: Union[None, Unset, str] = UNSET
    boxscore: Union[None, Unset, str] = UNSET
    jersey: Union[None, Unset, str] = UNSET
    abbreviated: Union[None, Unset, str] = UNSET
    given: Union[None, Unset, str] = UNSET
    family: Union[None, Unset, str] = UNSET
    full: Union[None, Unset, str] = UNSET
    known_as: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        display: Union[None, Unset, str]
        if isinstance(self.display, Unset):
            display = UNSET
        else:
            display = self.display

        television: Union[None, Unset, str]
        if isinstance(self.television, Unset):
            television = UNSET
        else:
            television = self.television

        scoreboard: Union[None, Unset, str]
        if isinstance(self.scoreboard, Unset):
            scoreboard = UNSET
        else:
            scoreboard = self.scoreboard

        pronunciation: Union[None, Unset, str]
        if isinstance(self.pronunciation, Unset):
            pronunciation = UNSET
        else:
            pronunciation = self.pronunciation

        boxscore: Union[None, Unset, str]
        if isinstance(self.boxscore, Unset):
            boxscore = UNSET
        else:
            boxscore = self.boxscore

        jersey: Union[None, Unset, str]
        if isinstance(self.jersey, Unset):
            jersey = UNSET
        else:
            jersey = self.jersey

        abbreviated: Union[None, Unset, str]
        if isinstance(self.abbreviated, Unset):
            abbreviated = UNSET
        else:
            abbreviated = self.abbreviated

        given: Union[None, Unset, str]
        if isinstance(self.given, Unset):
            given = UNSET
        else:
            given = self.given

        family: Union[None, Unset, str]
        if isinstance(self.family, Unset):
            family = UNSET
        else:
            family = self.family

        full: Union[None, Unset, str]
        if isinstance(self.full, Unset):
            full = UNSET
        else:
            full = self.full

        known_as: Union[None, Unset, str]
        if isinstance(self.known_as, Unset):
            known_as = UNSET
        else:
            known_as = self.known_as

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if display is not UNSET:
            field_dict["display"] = display
        if television is not UNSET:
            field_dict["television"] = television
        if scoreboard is not UNSET:
            field_dict["scoreboard"] = scoreboard
        if pronunciation is not UNSET:
            field_dict["pronunciation"] = pronunciation
        if boxscore is not UNSET:
            field_dict["boxscore"] = boxscore
        if jersey is not UNSET:
            field_dict["jersey"] = jersey
        if abbreviated is not UNSET:
            field_dict["abbreviated"] = abbreviated
        if given is not UNSET:
            field_dict["given"] = given
        if family is not UNSET:
            field_dict["family"] = family
        if full is not UNSET:
            field_dict["full"] = full
        if known_as is not UNSET:
            field_dict["knownAs"] = known_as

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_display(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display = _parse_display(d.pop("display", UNSET))

        def _parse_television(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        television = _parse_television(d.pop("television", UNSET))

        def _parse_scoreboard(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        scoreboard = _parse_scoreboard(d.pop("scoreboard", UNSET))

        def _parse_pronunciation(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pronunciation = _parse_pronunciation(d.pop("pronunciation", UNSET))

        def _parse_boxscore(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        boxscore = _parse_boxscore(d.pop("boxscore", UNSET))

        def _parse_jersey(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        jersey = _parse_jersey(d.pop("jersey", UNSET))

        def _parse_abbreviated(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviated = _parse_abbreviated(d.pop("abbreviated", UNSET))

        def _parse_given(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        given = _parse_given(d.pop("given", UNSET))

        def _parse_family(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        family = _parse_family(d.pop("family", UNSET))

        def _parse_full(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        full = _parse_full(d.pop("full", UNSET))

        def _parse_known_as(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        known_as = _parse_known_as(d.pop("knownAs", UNSET))

        person_update_person_put_body_additional_names_type_0_additional_property = cls(
            display=display,
            television=television,
            scoreboard=scoreboard,
            pronunciation=pronunciation,
            boxscore=boxscore,
            jersey=jersey,
            abbreviated=abbreviated,
            given=given,
            family=family,
            full=full,
            known_as=known_as,
        )

        return person_update_person_put_body_additional_names_type_0_additional_property
