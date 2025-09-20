from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.images_put_body_rating import ImagesPutBodyRating
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImagesPutBody")


@_attrs_define
class ImagesPutBody:
    """
    Attributes:
        rating (Union[Unset, ImagesPutBodyRating]): The rating given to the quality of the image.  All images are LOW by
            default but are set ad MEDIUM if they are large enough and have transparency.  Images are only marked as HIGH if
            they have been manually reviewed.  You should take your use-case into account when you go to use the image.
            >- `HIGH` High
            >- `LOW` Low
            >- `MEDIUM` Medium
             Example: LOW.
    """

    rating: Union[Unset, ImagesPutBodyRating] = UNSET

    def to_dict(self) -> dict[str, Any]:
        rating: Union[Unset, str] = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _rating = d.pop("rating", UNSET)
        rating: Union[Unset, ImagesPutBodyRating]
        if isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = ImagesPutBodyRating(_rating)

        images_put_body = cls(
            rating=rating,
        )

        return images_put_body
