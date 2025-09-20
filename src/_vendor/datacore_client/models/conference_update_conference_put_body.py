from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conference_update_conference_put_body_social_media import (
        ConferenceUpdateConferencePutBodySocialMedia,
    )


T = TypeVar("T", bound="ConferenceUpdateConferencePutBody")


@_attrs_define
class ConferenceUpdateConferencePutBody:
    """
    Attributes:
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_local (Union[Unset, str]): The name of the conference in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: Test name local.
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the conference in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test name latin .
        social (Union['ConferenceUpdateConferencePutBodySocialMedia', None, Unset]): Social Media contacts
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    abbreviation_local: Union[None, Unset, str] = UNSET
    name_local: Union[Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    social: Union["ConferenceUpdateConferencePutBodySocialMedia", None, Unset] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.conference_update_conference_put_body_social_media import (
            ConferenceUpdateConferencePutBodySocialMedia,
        )

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        name_local = self.name_local

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
        elif isinstance(self.social, ConferenceUpdateConferencePutBodySocialMedia):
            social = self.social.to_dict()
        else:
            social = self.social

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if social is not UNSET:
            field_dict["social"] = social
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.conference_update_conference_put_body_social_media import (
            ConferenceUpdateConferencePutBodySocialMedia,
        )

        d = dict(src_dict)

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
        ) -> Union["ConferenceUpdateConferencePutBodySocialMedia", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                social_type_0 = ConferenceUpdateConferencePutBodySocialMedia.from_dict(
                    data
                )

                return social_type_0
            except:  # noqa: E722
                pass
            return cast(
                Union["ConferenceUpdateConferencePutBodySocialMedia", None, Unset], data
            )

        social = _parse_social(d.pop("social", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        conference_update_conference_put_body = cls(
            abbreviation_local=abbreviation_local,
            name_local=name_local,
            abbreviation_latin=abbreviation_latin,
            name_latin=name_latin,
            social=social,
            external_id=external_id,
        )

        return conference_update_conference_put_body
