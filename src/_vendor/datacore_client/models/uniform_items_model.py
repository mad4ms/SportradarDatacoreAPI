import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.uniform_items_model_item_type import UniformItemsModelItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images_model import ImagesModel
    from ..models.uniform_items_model_colors import UniformItemsModelColors
    from ..models.uniform_items_model_organization import UniformItemsModelOrganization
    from ..models.uniform_items_model_uniform import UniformItemsModelUniform


T = TypeVar("T", bound="UniformItemsModel")


@_attrs_define
class UniformItemsModel:
    """
    Attributes:
        uniform_item_id (Union[Unset, UUID]): The unique identifier of the Uniform Item Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        uniform_id (Union[Unset, UUID]): The unique identifier of the uniform Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        uniform (Union[Unset, UniformItemsModelUniform]): The Uniform information
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, UniformItemsModelOrganization]): The organization that this uniform_items belongs to
        item_type (Union[Unset, UniformItemsModelItemType]): The type of Uniform Item
            >- `BOTTOM` Bottom
            >- `GOALKEEPER_BOTTOM` Goal Keeper Bottom
            >- `GOALKEEPER_TOP` Goal Keeper Top
            >- `HELMET` Helmet
            >- `SOCKS` Socks
            >- `TOP` Top
            >- `WARMUP_BOTTOM` Warmup Bottom
            >- `WARMUP_TOP` Warmup Top
             Example: TOP.
        name_local (Union[Unset, str]): The name of the uniform_items in the [local](#section/Introduction/Character-
            Sets-and-Names) language Example: Test name local.
        name_latin (Union[None, Unset, str]): The name of the uniform_items in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test uniform.
        colors (Union[Unset, UniformItemsModelColors]):
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        images (Union[Unset, list['ImagesModel']]):
    """

    uniform_item_id: Union[Unset, UUID] = UNSET
    uniform_id: Union[Unset, UUID] = UNSET
    uniform: Union[Unset, "UniformItemsModelUniform"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "UniformItemsModelOrganization"] = UNSET
    item_type: Union[Unset, UniformItemsModelItemType] = UNSET
    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    colors: Union[Unset, "UniformItemsModelColors"] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    images: Union[Unset, list["ImagesModel"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        uniform_item_id: Union[Unset, str] = UNSET
        if not isinstance(self.uniform_item_id, Unset):
            uniform_item_id = str(self.uniform_item_id)

        uniform_id: Union[Unset, str] = UNSET
        if not isinstance(self.uniform_id, Unset):
            uniform_id = str(self.uniform_id)

        uniform: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.uniform, Unset):
            uniform = self.uniform.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        name_local = self.name_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        colors: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.colors, Unset):
            colors = self.colors.to_dict()

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
        if uniform_item_id is not UNSET:
            field_dict["uniformItemId"] = uniform_item_id
        if uniform_id is not UNSET:
            field_dict["uniformId"] = uniform_id
        if uniform is not UNSET:
            field_dict["uniform"] = uniform
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if colors is not UNSET:
            field_dict["colors"] = colors
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
        from ..models.uniform_items_model_colors import UniformItemsModelColors
        from ..models.uniform_items_model_organization import UniformItemsModelOrganization
        from ..models.uniform_items_model_uniform import UniformItemsModelUniform

        d = dict(src_dict)
        _uniform_item_id = d.pop("uniformItemId", UNSET)
        uniform_item_id: Union[Unset, UUID]
        if isinstance(_uniform_item_id, Unset):
            uniform_item_id = UNSET
        else:
            uniform_item_id = UUID(_uniform_item_id)

        _uniform_id = d.pop("uniformId", UNSET)
        uniform_id: Union[Unset, UUID]
        if isinstance(_uniform_id, Unset):
            uniform_id = UNSET
        else:
            uniform_id = UUID(_uniform_id)

        _uniform = d.pop("uniform", UNSET)
        uniform: Union[Unset, UniformItemsModelUniform]
        if isinstance(_uniform, Unset):
            uniform = UNSET
        else:
            uniform = UniformItemsModelUniform.from_dict(_uniform)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, UniformItemsModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = UniformItemsModelOrganization.from_dict(_organization)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, UniformItemsModelItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = UniformItemsModelItemType(_item_type)

        name_local = d.pop("nameLocal", UNSET)

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        _colors = d.pop("colors", UNSET)
        colors: Union[Unset, UniformItemsModelColors]
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = UniformItemsModelColors.from_dict(_colors)

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

        uniform_items_model = cls(
            uniform_item_id=uniform_item_id,
            uniform_id=uniform_id,
            uniform=uniform,
            organization_id=organization_id,
            organization=organization,
            item_type=item_type,
            name_local=name_local,
            name_latin=name_latin,
            colors=colors,
            updated=updated,
            added=added,
            images=images,
        )

        return uniform_items_model
