from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.clock_information import ClockInformation
    from ..models.information_per_entity import InformationPerEntity
    from ..models.status_information import StatusInformation


T = TypeVar("T", bound="FixtureLiveSummaryModel")


@_attrs_define
class FixtureLiveSummaryModel:
    """
    Attributes:
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: b1a23.
        fixture_id (Union[Unset, UUID]): The unique identifier of the match Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entities (Union[Unset, InformationPerEntity]): Entity information: scores, person information, etc.
        clock (Union[Unset, ClockInformation]): Clock information
        status (Union[Unset, StatusInformation]): Status information
    """

    organization_id: Union[Unset, str] = UNSET
    fixture_id: Union[Unset, UUID] = UNSET
    entities: Union[Unset, "InformationPerEntity"] = UNSET
    clock: Union[Unset, "ClockInformation"] = UNSET
    status: Union[Unset, "StatusInformation"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        fixture_id: Union[Unset, str] = UNSET
        if not isinstance(self.fixture_id, Unset):
            fixture_id = str(self.fixture_id)

        entities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entities, Unset):
            entities = self.entities.to_dict()

        clock: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.clock, Unset):
            clock = self.clock.to_dict()

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if fixture_id is not UNSET:
            field_dict["fixtureId"] = fixture_id
        if entities is not UNSET:
            field_dict["entities"] = entities
        if clock is not UNSET:
            field_dict["clock"] = clock
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.clock_information import ClockInformation
        from ..models.information_per_entity import InformationPerEntity
        from ..models.status_information import StatusInformation

        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        _fixture_id = d.pop("fixtureId", UNSET)
        fixture_id: Union[Unset, UUID]
        if isinstance(_fixture_id, Unset):
            fixture_id = UNSET
        else:
            fixture_id = UUID(_fixture_id)

        _entities = d.pop("entities", UNSET)
        entities: Union[Unset, InformationPerEntity]
        if isinstance(_entities, Unset):
            entities = UNSET
        else:
            entities = InformationPerEntity.from_dict(_entities)

        _clock = d.pop("clock", UNSET)
        clock: Union[Unset, ClockInformation]
        if isinstance(_clock, Unset):
            clock = UNSET
        else:
            clock = ClockInformation.from_dict(_clock)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusInformation]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusInformation.from_dict(_status)

        fixture_live_summary_model = cls(
            organization_id=organization_id,
            fixture_id=fixture_id,
            entities=entities,
            clock=clock,
            status=status,
        )

        return fixture_live_summary_model
