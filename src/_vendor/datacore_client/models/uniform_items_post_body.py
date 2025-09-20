from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define

from ..models.uniform_items_post_body_item_type import UniformItemsPostBodyItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.uniform_items_post_body_colors import UniformItemsPostBodyColors


T = TypeVar("T", bound="UniformItemsPostBody")


@_attrs_define
class UniformItemsPostBody:
    """
    Attributes:
        uniform_id (UUID): The unique identifier of the uniform Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        item_type (UniformItemsPostBodyItemType): The type of Uniform Item
            >- `BOTTOM` Bottom
            >- `GOALKEEPER_BOTTOM` Goal Keeper Bottom
            >- `GOALKEEPER_TOP` Goal Keeper Top
            >- `HELMET` Helmet
            >- `SOCKS` Socks
            >- `TOP` Top
            >- `WARMUP_BOTTOM` Warmup Bottom
            >- `WARMUP_TOP` Warmup Top
             Example: TOP.
        uniform_item_id (Union[Unset, UUID]): The unique identifier of the Uniform Item Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        name_local (Union[Unset, str]): The name of the uniform_items in the [local](#section/Introduction/Character-
            Sets-and-Names) language Example: Test name local.
        name_latin (Union[None, Unset, str]): The name of the uniform_items in [latin](#section/Introduction/Character-
            Sets-and-Names) characters Example: Test uniform.
        colors (Union[Unset, UniformItemsPostBodyColors]):
    """

    uniform_id: UUID
    item_type: UniformItemsPostBodyItemType
    uniform_item_id: Union[Unset, UUID] = UNSET
    name_local: Union[Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    colors: Union[Unset, "UniformItemsPostBodyColors"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        uniform_id = str(self.uniform_id)

        item_type = self.item_type.value

        uniform_item_id: Union[Unset, str] = UNSET
        if not isinstance(self.uniform_item_id, Unset):
            uniform_item_id = str(self.uniform_item_id)

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

        field_dict.update(
            {
                "uniformId": uniform_id,
                "itemType": item_type,
            }
        )
        if uniform_item_id is not UNSET:
            field_dict["uniformItemId"] = uniform_item_id
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if colors is not UNSET:
            field_dict["colors"] = colors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.uniform_items_post_body_colors import UniformItemsPostBodyColors

        d = dict(src_dict)
        uniform_id = UUID(d.pop("uniformId"))

        item_type = UniformItemsPostBodyItemType(d.pop("itemType"))

        _uniform_item_id = d.pop("uniformItemId", UNSET)
        uniform_item_id: Union[Unset, UUID]
        if isinstance(_uniform_item_id, Unset):
            uniform_item_id = UNSET
        else:
            uniform_item_id = UUID(_uniform_item_id)

        name_local = d.pop("nameLocal", UNSET)

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        _colors = d.pop("colors", UNSET)
        colors: Union[Unset, UniformItemsPostBodyColors]
        if isinstance(_colors, Unset):
            colors = UNSET
        else:
            colors = UniformItemsPostBodyColors.from_dict(_colors)

        uniform_items_post_body = cls(
            uniform_id=uniform_id,
            item_type=item_type,
            uniform_item_id=uniform_item_id,
            name_local=name_local,
            name_latin=name_latin,
            colors=colors,
        )

        return uniform_items_post_body
