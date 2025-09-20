import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.uniforms_update_uniforms_put_body_base_type import (
    UniformsUpdateUniformsPutBodyBaseType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UniformsUpdateUniformsPutBody")


@_attrs_define
class UniformsUpdateUniformsPutBody:
    """
    Attributes:
        base_type (Union[Unset, UniformsUpdateUniformsPutBodyBaseType]): The object that this uniform relates to
            >- `ENTITY` Entity
            >- `ENTITYGROUP` Entity Group
            >- `PERSON` Person
             Example: entity.
        base_id (Union[Unset, UUID]): The unique identifier of the object associated with this record. If the `baseType`
            is `ENTITY` then this would be the value of `entityId`. Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name_local (Union[Unset, str]): The name of the uniforms in the [local](#section/Introduction/Character-Sets-
            and-Names) language Example: Test uniform.
        name_latin (Union[None, Unset, str]): The name of the uniforms in [latin](#section/Introduction/Character-Sets-
            and-Names) characters Example: Test uniform.
        date_from (Union[None, Unset, datetime.date]): Date the Uniform is valid from Example: 1978-08-24.
        date_to (Union[None, Unset, datetime.date]): Date the Uniform is valid until Example: 1978-08-24.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
    """

    base_type: Union[Unset, UniformsUpdateUniformsPutBodyBaseType] = UNSET
    base_id: Union[Unset, UUID] = UNSET
    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    date_from: Union[None, Unset, datetime.date] = UNSET
    date_to: Union[None, Unset, datetime.date] = UNSET
    external_id: Union[None, Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        base_type: Union[Unset, str] = UNSET
        if not isinstance(self.base_type, Unset):
            base_type = self.base_type.value

        base_id: Union[Unset, str] = UNSET
        if not isinstance(self.base_id, Unset):
            base_id = str(self.base_id)

        name_local = self.name_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        date_from: Union[None, Unset, str]
        if isinstance(self.date_from, Unset):
            date_from = UNSET
        elif isinstance(self.date_from, datetime.date):
            date_from = self.date_from.isoformat()
        else:
            date_from = self.date_from

        date_to: Union[None, Unset, str]
        if isinstance(self.date_to, Unset):
            date_to = UNSET
        elif isinstance(self.date_to, datetime.date):
            date_to = self.date_to.isoformat()
        else:
            date_to = self.date_to

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if base_type is not UNSET:
            field_dict["baseType"] = base_type
        if base_id is not UNSET:
            field_dict["baseId"] = base_id
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if date_from is not UNSET:
            field_dict["dateFrom"] = date_from
        if date_to is not UNSET:
            field_dict["dateTo"] = date_to
        if external_id is not UNSET:
            field_dict["externalId"] = external_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _base_type = d.pop("baseType", UNSET)
        base_type: Union[Unset, UniformsUpdateUniformsPutBodyBaseType]
        if isinstance(_base_type, Unset):
            base_type = UNSET
        else:
            base_type = UniformsUpdateUniformsPutBodyBaseType(_base_type)

        _base_id = d.pop("baseId", UNSET)
        base_id: Union[Unset, UUID]
        if isinstance(_base_id, Unset):
            base_id = UNSET
        else:
            base_id = UUID(_base_id)

        name_local = d.pop("nameLocal", UNSET)

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_date_from(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_type_0 = isoparse(data).date()

                return date_from_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_from = _parse_date_from(d.pop("dateFrom", UNSET))

        def _parse_date_to(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_to_type_0 = isoparse(data).date()

                return date_to_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        date_to = _parse_date_to(d.pop("dateTo", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

        uniforms_update_uniforms_put_body = cls(
            base_type=base_type,
            base_id=base_id,
            name_local=name_local,
            name_latin=name_latin,
            date_from=date_from,
            date_to=date_to,
            external_id=external_id,
        )

        return uniforms_update_uniforms_put_body
