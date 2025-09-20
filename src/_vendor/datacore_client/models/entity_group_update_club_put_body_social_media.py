from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityGroupUpdateClubPutBodySocialMedia")


@_attrs_define
class EntityGroupUpdateClubPutBodySocialMedia:
    """Social Media contacts

    Attributes:
        website (Union[None, Unset, str]):  Example: http://www.example.com.
        facebook (Union[None, Unset, str]):  Example: https://www.facebook.com/example.
        twitter (Union[None, Unset, str]):  Example: https://www.twitter.com/example.
        wikipedia (Union[None, Unset, str]):  Example: https://en.wikipedia.org/wiki/example.
        instagram (Union[None, Unset, str]):  Example: https://www.instagram.com/example.
    """

    website: Union[None, Unset, str] = UNSET
    facebook: Union[None, Unset, str] = UNSET
    twitter: Union[None, Unset, str] = UNSET
    wikipedia: Union[None, Unset, str] = UNSET
    instagram: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        website: Union[None, Unset, str]
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        facebook: Union[None, Unset, str]
        if isinstance(self.facebook, Unset):
            facebook = UNSET
        else:
            facebook = self.facebook

        twitter: Union[None, Unset, str]
        if isinstance(self.twitter, Unset):
            twitter = UNSET
        else:
            twitter = self.twitter

        wikipedia: Union[None, Unset, str]
        if isinstance(self.wikipedia, Unset):
            wikipedia = UNSET
        else:
            wikipedia = self.wikipedia

        instagram: Union[None, Unset, str]
        if isinstance(self.instagram, Unset):
            instagram = UNSET
        else:
            instagram = self.instagram

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if website is not UNSET:
            field_dict["website"] = website
        if facebook is not UNSET:
            field_dict["facebook"] = facebook
        if twitter is not UNSET:
            field_dict["twitter"] = twitter
        if wikipedia is not UNSET:
            field_dict["wikipedia"] = wikipedia
        if instagram is not UNSET:
            field_dict["instagram"] = instagram

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_website(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        website = _parse_website(d.pop("website", UNSET))

        def _parse_facebook(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        facebook = _parse_facebook(d.pop("facebook", UNSET))

        def _parse_twitter(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        twitter = _parse_twitter(d.pop("twitter", UNSET))

        def _parse_wikipedia(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        wikipedia = _parse_wikipedia(d.pop("wikipedia", UNSET))

        def _parse_instagram(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        instagram = _parse_instagram(d.pop("instagram", UNSET))

        entity_group_update_club_put_body_social_media = cls(
            website=website,
            facebook=facebook,
            twitter=twitter,
            wikipedia=wikipedia,
            instagram=instagram,
        )

        return entity_group_update_club_put_body_social_media
