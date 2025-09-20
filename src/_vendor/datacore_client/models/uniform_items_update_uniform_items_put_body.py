from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.uniform_items_update_uniform_items_put_body_item_type import (
    UniformItemsUpdateUniformItemsPutBodyItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.uniform_items_update_uniform_items_put_body_colors import (
        UniformItemsUpdateUniformItemsPutBodyColors,
    )


T = TypeVar("T", bound="UniformItemsUpdateUniformItemsPutBody")


@_attrs_define
class UniformItemsUpdateUniformItemsPutBody:
    """
    Attributes:
        uniform_id (Union[Unset, UUID]): The unique identifier of the uniform Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        item_type (Union[Unset, UniformItemsUpdateUniformItemsPutBodyItemType]): The type of Uniform Item
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
        colors (Union[Unset, UniformItemsUpdateUniformItemsPutBodyColors]):
    """

    uniform_id: Union[Unset, UUID] = UNSET
    item_type: Union[Unset, UniformItemsUpdateUniformItemsPutBodyItemType] = UNSET
    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    colors: Union[Unset, "UniformItemsUpdateUniformItemsPutBodyColors"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        uniform_id: Union[Unset, str] = UNSET
        if not isinstance(self.uniform_id, Unset):
            uniform_id = str(self.uniform_id)

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

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if uniform_id is not UNSET:
            field_dict["uniformId"] = uniform_id
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if colors is not UNSET:
            field_dict["colors"] = colors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.uniform_items_update_uniform_items_put_body_colors import (
            UniformItemsUpdateUniformItemsPutBodyColors,
        )

        d = dict(src_dict)
        _uniform_id = d.pop("uniformId", UNSET)
        uniform_id: Union[Unset, UUID]
        if isinstance(_uniform_id, Unset):
            uniform_id = UNSET
        else:
            uniform_id = UUID(_uniform_id)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, UniformItemsUpdateUniformItemsPutBodyItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = UniformItemsUpdateUniformItemsPutBodyItemType(_item_type)

        name_local = d.pop("nameLocal", UNSET)

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        _colors = d.pop("colors", UNSET)
        colors: Union[Unset, UniformItemsUpdateUniformItemsPutBodyColors]
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = UniformItemsUpdateUniformItemsPutBodyColors.from_dict(_colors)

        uniform_items_update_uniform_items_put_body = cls(
            uniform_id=uniform_id,
            item_type=item_type,
            name_local=name_local,
            name_latin=name_latin,
            colors=colors,
        )

        return uniform_items_update_uniform_items_put_body
