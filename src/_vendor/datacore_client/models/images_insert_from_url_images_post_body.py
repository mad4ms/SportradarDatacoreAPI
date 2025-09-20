from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ImagesInsertFromUrlImagesPostBody")


@_attrs_define
class ImagesInsertFromUrlImagesPostBody:
    """
    Attributes:
        url (str): The URL of the image Example: http://www.example.com/images/image1.png.
    """

    url: str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        images_insert_from_url_images_post_body = cls(
            url=url,
        )

        return images_insert_from_url_images_post_body
