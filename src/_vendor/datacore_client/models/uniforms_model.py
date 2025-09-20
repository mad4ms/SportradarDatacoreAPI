import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.uniforms_model_base_type import UniformsModelBaseType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images_model import ImagesModel
    from ..models.uniforms_model_organization import UniformsModelOrganization


T = TypeVar("T", bound="UniformsModel")


@_attrs_define
class UniformsModel:
    """
    Attributes:
        uniform_id (Union[Unset, UUID]): The unique identifier of the Uniform Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, UniformsModelOrganization]): The organization that this uniforms belongs to
        base_type (Union[Unset, UniformsModelBaseType]): The object that this uniform relates to
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
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        images (Union[Unset, list['ImagesModel']]):
    """

    uniform_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "UniformsModelOrganization"] = UNSET
    base_type: Union[Unset, UniformsModelBaseType] = UNSET
    base_id: Union[Unset, UUID] = UNSET
    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    date_from: Union[None, Unset, datetime.date] = UNSET
    date_to: Union[None, Unset, datetime.date] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    images: Union[Unset, list["ImagesModel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        uniform_id: Union[Unset, str] = UNSET
        if not isinstance(self.uniform_id, Unset):
            uniform_id = str(self.uniform_id)

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

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

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        images: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uniform_id is not UNSET:
            field_dict["uniformId"] = uniform_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
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
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.images_model import ImagesModel
        from ..models.uniforms_model_organization import UniformsModelOrganization

        d = dict(src_dict)
        _uniform_id = d.pop("uniformId", UNSET)
        uniform_id: Union[Unset, UUID]
        if isinstance(_uniform_id, Unset):
            uniform_id = UNSET
        else:
            uniform_id = UUID(_uniform_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, UniformsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = UniformsModelOrganization.from_dict(_organization)

        _base_type = d.pop("baseType", UNSET)
        base_type: Union[Unset, UniformsModelBaseType]
        if isinstance(_base_type, Unset):
            base_type = UNSET
        else:
            base_type = UniformsModelBaseType(_base_type)

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

        _updated = d.pop("updated", UNSET)
        updated: Union[Unset, datetime.datetime]
        if isinstance(_updated, Unset):
            updated = UNSET
        else:
            updated = isoparse(_updated)

        _added = d.pop("added", UNSET)
        added: Union[Unset, datetime.datetime]
        if isinstance(_added, Unset):
            added = UNSET
        else:
            added = isoparse(_added)

        images = []
        _images = d.pop("images", UNSET)
        for images_item_data in _images or []:
            images_item = ImagesModel.from_dict(images_item_data)

            images.append(images_item)

        uniforms_model = cls(
            uniform_id=uniform_id,
            organization_id=organization_id,
            organization=organization,
            base_type=base_type,
            base_id=base_id,
            name_local=name_local,
            name_latin=name_latin,
            date_from=date_from,
            date_to=date_to,
            external_id=external_id,
            updated=updated,
            added=added,
            images=images,
        )

        return uniforms_model
