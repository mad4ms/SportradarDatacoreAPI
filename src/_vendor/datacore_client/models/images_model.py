import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.images_model_base_type import ImagesModelBaseType
from ..models.images_model_file_type import ImagesModelFileType
from ..models.images_model_image_type import ImagesModelImageType
from ..models.images_model_rating import ImagesModelRating
from ..models.images_model_secondary_type_type_1 import ImagesModelSecondaryTypeType1
from ..models.images_model_secondary_type_type_2_type_1 import (
    ImagesModelSecondaryTypeType2Type1,
)
from ..models.images_model_secondary_type_type_3_type_1 import (
    ImagesModelSecondaryTypeType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.images_model_organization import ImagesModelOrganization


T = TypeVar("T", bound="ImagesModel")


@_attrs_define
class ImagesModel:
    """
    Attributes:
        image_id (Union[Unset, UUID]): The unique identifier of the image record Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, ImagesModelOrganization]): The organization that this images belongs to
        base_type (Union[Unset, ImagesModelBaseType]): The object that this image relates to
            >- `COMPETITION` Competition
            >- `CONFERENCE` Conference
            >- `DIVISION` Division
            >- `ENTITY` Entity
            >- `ENTITYGROUP` Entity Group
            >- `LEAGUE` League
            >- `ORGANIZATION` Organization
            >- `PERSON` Person
            >- `SEASON` Season
            >- `UNIFORM` Uniform
            >- `UNIFORM_ITEM` Uniform Item
             Example: entity.
        base_id (Union[Unset, UUID]): The unique identifier of the object associated with this image's record. If the
            `baseType` is `PERSON` then this would be the value of `personId`. Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        file_type (Union[Unset, ImagesModelFileType]): The type of file
            >- `JPG` jpg
            >- `PNG` png
            >- `SVG` svg
             Example: png.
        image_type (Union[Unset, ImagesModelImageType]): Upload Type
            >- `LOGO` Logo - Not valid for 'PERSON' baseType
            >- `LOGO_ALTERNATE` Logo (alternate) - Not valid for 'PERSON' baseType
            >- `LOGO_BACKGROUND` Stylised logo for background purposes - Not valid for 'PERSON' baseType
            >- `PERSON_HEAD` Head shot (shoulders and head) - Only valid for 'PERSON' baseType
            >- `PERSON_POSE` Person posing - Only valid for 'PERSON' baseType
            >- `PERSON_WAIST` Head shot from the waist up - Only valid for 'PERSON' baseType
            >- `TEAM_PHOTO` Team Photo - Only valid for 'ENTITY' baseType
            >- `UNIFORM` Uniform
            >- `UNIFORM_ITEM` Uniform Item
             Example: LOGO.
        secondary_type (Union[ImagesModelSecondaryTypeType1, ImagesModelSecondaryTypeType2Type1,
            ImagesModelSecondaryTypeType3Type1, None, Unset]): If the image relates to a secondary object. Such as a photo
            of a person in a team, then baseType would be PERSON and secondaryType would be TEAM.
            >- None None
            >- `COMPETITION` Competition
            >- `CONFERENCE` Conference
            >- `DIVISION` Division
            >- `ENTITY` Entity
            >- `ENTITYGROUP` Entity Group
            >- `LEAGUE` League
            >- `SEASON` Season
             Example: entity.
        secondary_id (Union[Unset, UUID]): The unique identifier of the object associated with the secondaryType
            Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        rating (Union[Unset, ImagesModelRating]): The rating given to the quality of the image.  All images are LOW by
            default but are set ad MEDIUM if they are large enough and have transparency.  Images are only marked as HIGH if
            they have been manually reviewed.  You should take your use-case into account when you go to use the image.
            >- `HIGH` High
            >- `LOW` Low
            >- `MEDIUM` Medium
             Example: LOW.
        url (Union[Unset, str]): The URL of the image. See [Images](#section/Introduction/Images) for more information.
        maximum_height (Union[Unset, int]): The maximum height (in pixels) of this image. Example: 200.
        maximum_width (Union[Unset, int]): The maximum width (in pixels) of this image. Example: 200.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
    """

    image_id: Union[Unset, UUID] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "ImagesModelOrganization"] = UNSET
    base_type: Union[Unset, ImagesModelBaseType] = UNSET
    base_id: Union[Unset, UUID] = UNSET
    file_type: Union[Unset, ImagesModelFileType] = UNSET
    image_type: Union[Unset, ImagesModelImageType] = UNSET
    secondary_type: Union[
        ImagesModelSecondaryTypeType1,
        ImagesModelSecondaryTypeType2Type1,
        ImagesModelSecondaryTypeType3Type1,
        None,
        Unset,
    ] = UNSET
    secondary_id: Union[Unset, UUID] = UNSET
    rating: Union[Unset, ImagesModelRating] = UNSET
    url: Union[Unset, str] = UNSET
    maximum_height: Union[Unset, int] = UNSET
    maximum_width: Union[Unset, int] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET

    def to_dict(self) -> dict[str, Any]:
        image_id: Union[Unset, str] = UNSET
        if not isinstance(self.image_id, Unset):
            image_id = str(self.image_id)

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

        file_type: Union[Unset, str] = UNSET
        if not isinstance(self.file_type, Unset):
            file_type = self.file_type.value

        image_type: Union[Unset, str] = UNSET
        if not isinstance(self.image_type, Unset):
            image_type = self.image_type.value

        secondary_type: Union[None, Unset, str]
        if isinstance(self.secondary_type, Unset):
            secondary_type = UNSET
        elif isinstance(self.secondary_type, ImagesModelSecondaryTypeType1):
            secondary_type = self.secondary_type.value
        elif isinstance(self.secondary_type, ImagesModelSecondaryTypeType2Type1):
            secondary_type = self.secondary_type.value
        elif isinstance(self.secondary_type, ImagesModelSecondaryTypeType3Type1):
            secondary_type = self.secondary_type.value
        else:
            secondary_type = self.secondary_type

        secondary_id: Union[Unset, str] = UNSET
        if not isinstance(self.secondary_id, Unset):
            secondary_id = str(self.secondary_id)

        rating: Union[Unset, str] = UNSET
        if not isinstance(self.rating, Unset):
            rating = self.rating.value

        url = self.url

        maximum_height = self.maximum_height

        maximum_width = self.maximum_width

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if base_type is not UNSET:
            field_dict["baseType"] = base_type
        if base_id is not UNSET:
            field_dict["baseId"] = base_id
        if file_type is not UNSET:
            field_dict["fileType"] = file_type
        if image_type is not UNSET:
            field_dict["imageType"] = image_type
        if secondary_type is not UNSET:
            field_dict["secondaryType"] = secondary_type
        if secondary_id is not UNSET:
            field_dict["secondaryId"] = secondary_id
        if rating is not UNSET:
            field_dict["rating"] = rating
        if url is not UNSET:
            field_dict["url"] = url
        if maximum_height is not UNSET:
            field_dict["maximumHeight"] = maximum_height
        if maximum_width is not UNSET:
            field_dict["maximumWidth"] = maximum_width
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.images_model_organization import ImagesModelOrganization

        d = dict(src_dict)
        _image_id = d.pop("imageId", UNSET)
        image_id: Union[Unset, UUID]
        if isinstance(_image_id, Unset):
            image_id = UNSET
        else:
            image_id = UUID(_image_id)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, ImagesModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = ImagesModelOrganization.from_dict(_organization)

        _base_type = d.pop("baseType", UNSET)
        base_type: Union[Unset, ImagesModelBaseType]
        if isinstance(_base_type, Unset):
            base_type = UNSET
        else:
            base_type = ImagesModelBaseType(_base_type)

        _base_id = d.pop("baseId", UNSET)
        base_id: Union[Unset, UUID]
        if isinstance(_base_id, Unset):
            base_id = UNSET
        else:
            base_id = UUID(_base_id)

        _file_type = d.pop("fileType", UNSET)
        file_type: Union[Unset, ImagesModelFileType]
        if isinstance(_file_type, Unset):
            file_type = UNSET
        else:
            file_type = ImagesModelFileType(_file_type)

        _image_type = d.pop("imageType", UNSET)
        image_type: Union[Unset, ImagesModelImageType]
        if isinstance(_image_type, Unset):
            image_type = UNSET
        else:
            image_type = ImagesModelImageType(_image_type)

        def _parse_secondary_type(
            data: object,
        ) -> Union[
            ImagesModelSecondaryTypeType1,
            ImagesModelSecondaryTypeType2Type1,
            ImagesModelSecondaryTypeType3Type1,
            None,
            Unset,
        ]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secondary_type_type_1 = ImagesModelSecondaryTypeType1(data)

                return secondary_type_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secondary_type_type_2_type_1 = ImagesModelSecondaryTypeType2Type1(data)

                return secondary_type_type_2_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                secondary_type_type_3_type_1 = ImagesModelSecondaryTypeType3Type1(data)

                return secondary_type_type_3_type_1
            except:  # noqa: E722
                pass
            return cast(
                Union[
                    ImagesModelSecondaryTypeType1,
                    ImagesModelSecondaryTypeType2Type1,
                    ImagesModelSecondaryTypeType3Type1,
                    None,
                    Unset,
                ],
                data,
            )

        secondary_type = _parse_secondary_type(d.pop("secondaryType", UNSET))

        _secondary_id = d.pop("secondaryId", UNSET)
        secondary_id: Union[Unset, UUID]
        if isinstance(_secondary_id, Unset):
            secondary_id = UNSET
        else:
            secondary_id = UUID(_secondary_id)

        _rating = d.pop("rating", UNSET)
        rating: Union[Unset, ImagesModelRating]
        if isinstance(_rating, Unset):
            rating = UNSET
        else:
            rating = ImagesModelRating(_rating)

        url = d.pop("url", UNSET)

        maximum_height = d.pop("maximumHeight", UNSET)

        maximum_width = d.pop("maximumWidth", UNSET)

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

        images_model = cls(
            image_id=image_id,
            organization_id=organization_id,
            organization=organization,
            base_type=base_type,
            base_id=base_id,
            file_type=file_type,
            image_type=image_type,
            secondary_type=secondary_type,
            secondary_id=secondary_id,
            rating=rating,
            url=url,
            maximum_height=maximum_height,
            maximum_width=maximum_width,
            updated=updated,
            added=added,
        )

        return images_model
