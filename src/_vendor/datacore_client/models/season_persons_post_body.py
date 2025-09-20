from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.season_persons_post_body_status import SeasonPersonsPostBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonPersonsPostBody")


@_attrs_define
class SeasonPersonsPostBody:
    """
    Attributes:
        season_id (UUID): The unique identifier of the season Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id (Union[Unset, UUID]): The unique identifier of the person Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_group_id (Union[Unset, UUID]): The club that this team belongs to Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        status (Union[Unset, SeasonPersonsPostBodyStatus]): Status
            >- `ACTIVE` Active
            >- `INACTIVE` Inactive
            >- `PENDING` Pending
             Example: ACTIVE.
        seed (Union[None, Unset, int]): Initial seeding Example: 1.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    season_id: UUID
    person_id: Union[Unset, UUID] = UNSET
    entity_group_id: Union[Unset, UUID] = UNSET
    status: Union[Unset, SeasonPersonsPostBodyStatus] = UNSET
    seed: Union[None, Unset, int] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        season_id = str(self.season_id)

        person_id: Union[Unset, str] = UNSET
        if not isinstance(self.person_id, Unset):
            person_id = str(self.person_id)

        entity_group_id: Union[Unset, str] = UNSET
        if not isinstance(self.entity_group_id, Unset):
            entity_group_id = str(self.entity_group_id)

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        seed: Union[None, Unset, int]
        if isinstance(self.seed, Unset):
            seed = UNSET
        else:
            seed = self.seed

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "seasonId": season_id,
            }
        )
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if entity_group_id is not UNSET:
            field_dict["entityGroupId"] = entity_group_id
        if status is not UNSET:
            field_dict["status"] = status
        if seed is not UNSET:
            field_dict["seed"] = seed
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        season_id = UUID(d.pop("seasonId"))

        _person_id = d.pop("personId", UNSET)
        person_id: Union[Unset, UUID]
        if isinstance(_person_id, Unset):
            person_id = UNSET
        else:
            person_id = UUID(_person_id)

        _entity_group_id = d.pop("entityGroupId", UNSET)
        entity_group_id: Union[Unset, UUID]
        if isinstance(_entity_group_id, Unset):
            entity_group_id = UNSET
        else:
            entity_group_id = UUID(_entity_group_id)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SeasonPersonsPostBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeasonPersonsPostBodyStatus(_status)

        def _parse_seed(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        seed = _parse_seed(d.pop("seed", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        season_persons_post_body = cls(
            season_id=season_id,
            person_id=person_id,
            entity_group_id=entity_group_id,
            status=status,
            seed=seed,
            external_id=external_id,
        )

        return season_persons_post_body
