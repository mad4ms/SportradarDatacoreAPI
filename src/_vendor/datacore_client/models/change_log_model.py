import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.change_log_model_change_type import ChangeLogModelChangeType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.change_log_model_organization import ChangeLogModelOrganization


T = TypeVar("T", bound="ChangeLogModel")


@_attrs_define
class ChangeLogModel:
    """
    Attributes:
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, ChangeLogModelOrganization]): The organization that this change_log belongs to
        change_type (Union[Unset, ChangeLogModelChangeType]): The type of change
            >- `delete` Record Deleted
            >- `fixture_change` Fixture schedule Change
            >- `fixture_reset` Fixture Reset
            >- `fixture_videostream_disable` Enable Video Stream
            >- `fixture_videostream_enable` Enable Video Stream
            >- `move` Record Moved
            >- `post` Record Created
            >- `put` Record Changed
            >- `update` Record Updated
             Example: delete.
        primary_type (Union[Unset, str]): The primary table changed Example: fixtures.
        primary_id (Union[Unset, UUID]): The unique identifier of the primaryType Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        child_type (Union[Unset, str]): The child table changed Example: fixture_roster.
        change_message (Union[Unset, Any]):
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "ChangeLogModelOrganization"] = UNSET
    change_type: Union[Unset, ChangeLogModelChangeType] = UNSET
    primary_type: Union[Unset, str] = UNSET
    primary_id: Union[Unset, UUID] = UNSET
    child_type: Union[Unset, str] = UNSET
    change_message: Union[Unset, Any] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        change_type: Union[Unset, str] = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        primary_type = self.primary_type

        primary_id: Union[Unset, str] = UNSET
        if not isinstance(self.primary_id, Unset):
            primary_id = str(self.primary_id)

        child_type = self.child_type

        change_message = self.change_message

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if change_type is not UNSET:
            field_dict["changeType"] = change_type
        if primary_type is not UNSET:
            field_dict["primaryType"] = primary_type
        if primary_id is not UNSET:
            field_dict["primaryId"] = primary_id
        if child_type is not UNSET:
            field_dict["childType"] = child_type
        if change_message is not UNSET:
            field_dict["changeMessage"] = change_message
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_log_model_organization import ChangeLogModelOrganization

        d = dict(src_dict)
        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, ChangeLogModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = ChangeLogModelOrganization.from_dict(_organization)

        _change_type = d.pop("changeType", UNSET)
        change_type: Union[Unset, ChangeLogModelChangeType]
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = ChangeLogModelChangeType(_change_type)

        primary_type = d.pop("primaryType", UNSET)

        _primary_id = d.pop("primaryId", UNSET)
        primary_id: Union[Unset, UUID]
        if isinstance(_primary_id, Unset):
            primary_id = UNSET
        else:
            primary_id = UUID(_primary_id)

        child_type = d.pop("childType", UNSET)

        change_message = d.pop("changeMessage", UNSET)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        change_log_model = cls(
            organization_id=organization_id,
            organization=organization,
            change_type=change_type,
            primary_type=primary_type,
            primary_id=primary_id,
            child_type=child_type,
            change_message=change_message,
            added=added,
        )

        return change_log_model
