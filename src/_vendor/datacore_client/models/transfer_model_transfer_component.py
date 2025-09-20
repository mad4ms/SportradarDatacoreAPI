from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransferModelTransferComponent")


@_attrs_define
class TransferModelTransferComponent:
    """
    Attributes:
        person_id (Union[Unset, str]): The uuid of the person
        from_entity_group_id (Union[Unset, str]): The uuid of the source entity group
        to_entity_group_id (Union[Unset, str]): The uuid of the destination entity group
        extra_allowances (Union[Unset, str]): Details of additional allowances included in the transfer Example: Cash,
            1st Round Pick.
    """

    person_id: Union[Unset, str] = UNSET
    from_entity_group_id: Union[Unset, str] = UNSET
    to_entity_group_id: Union[Unset, str] = UNSET
    extra_allowances: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        from_entity_group_id = self.from_entity_group_id

        to_entity_group_id = self.to_entity_group_id

        extra_allowances = self.extra_allowances

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if from_entity_group_id is not UNSET:
            field_dict["fromEntityGroupId"] = from_entity_group_id
        if to_entity_group_id is not UNSET:
            field_dict["toEntityGroupId"] = to_entity_group_id
        if extra_allowances is not UNSET:
            field_dict["extraAllowances"] = extra_allowances

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = d.pop("personId", UNSET)

        from_entity_group_id = d.pop("fromEntityGroupId", UNSET)

        to_entity_group_id = d.pop("toEntityGroupId", UNSET)

        extra_allowances = d.pop("extraAllowances", UNSET)

        transfer_model_transfer_component = cls(
            person_id=person_id,
            from_entity_group_id=from_entity_group_id,
            to_entity_group_id=to_entity_group_id,
            extra_allowances=extra_allowances,
        )

        return transfer_model_transfer_component
