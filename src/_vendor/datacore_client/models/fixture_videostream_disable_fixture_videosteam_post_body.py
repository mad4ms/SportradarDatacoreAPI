from collections.abc import Mapping
from typing import Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..models.fixture_videostream_disable_fixture_videosteam_post_body_platform_provider import (
    FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="FixtureVideostreamDisableFixtureVideosteamPostBody")


@_attrs_define
class FixtureVideostreamDisableFixtureVideosteamPostBody:
    """
    Attributes:
        fixture_id (UUID): The unique identifier of the match Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        locale (Union[Unset, str]): The locale of the video Example: fr-FR.
        platform_provider (Union[Unset, FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider]): Video
            Provider platform
            >- `5STREAM` 5Stream
            >- `AV_SPORTRADAR` AV Sportradar
             Default: FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider.VALUE_0. Example: 5STREAM.
    """

    fixture_id: UUID
    locale: Union[Unset, str] = UNSET
    platform_provider: Union[
        Unset, FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider
    ] = FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider.VALUE_0

    def to_dict(self) -> dict[str, Any]:
        fixture_id = str(self.fixture_id)

        locale = self.locale

        platform_provider: Union[Unset, str] = UNSET
        if not isinstance(self.platform_provider, Unset):
            platform_provider = self.platform_provider.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "fixtureId": fixture_id,
            }
        )
        if locale is not UNSET:
            field_dict["locale"] = locale
        if platform_provider is not UNSET:
            field_dict["platformProvider"] = platform_provider

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixture_id = UUID(d.pop("fixtureId"))

        locale = d.pop("locale", UNSET)

        _platform_provider = d.pop("platformProvider", UNSET)
        platform_provider: Union[
            Unset, FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider
        ]
        if isinstance(_platform_provider, Unset):
            platform_provider = UNSET
        else:
            platform_provider = (
                FixtureVideostreamDisableFixtureVideosteamPostBodyPlatformProvider(
                    _platform_provider
                )
            )

        fixture_videostream_disable_fixture_videosteam_post_body = cls(
            fixture_id=fixture_id,
            locale=locale,
            platform_provider=platform_provider,
        )

        return fixture_videostream_disable_fixture_videosteam_post_body
