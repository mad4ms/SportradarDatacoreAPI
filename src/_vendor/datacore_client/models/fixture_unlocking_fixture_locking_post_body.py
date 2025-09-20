from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FixtureUnlockingFixtureLockingPostBody")


@_attrs_define
class FixtureUnlockingFixtureLockingPostBody:
    """ """

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        fixture_unlocking_fixture_locking_post_body = cls()

        return fixture_unlocking_fixture_locking_post_body
