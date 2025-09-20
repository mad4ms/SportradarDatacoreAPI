from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.included_data import IncludedData
    from ..models.response_links import ResponseLinks
    from ..models.response_meta_data import ResponseMetaData
    from ..models.video_file_model import VideoFileModel


T = TypeVar("T", bound="VideoFileInsertVideoFilesResponse")


@_attrs_define
class VideoFileInsertVideoFilesResponse:
    """
    Attributes:
        meta (Union[Unset, ResponseMetaData]):
        links (Union[Unset, ResponseLinks]):
        included (Union[Unset, IncludedData]): Available if the request used the 'include' parameter.  It contains extra
            data about resources found in the data block.
        data (Union[Unset, list['VideoFileModel']]):
    """

    meta: Union[Unset, "ResponseMetaData"] = UNSET
    links: Union[Unset, "ResponseLinks"] = UNSET
    included: Union[Unset, "IncludedData"] = UNSET
    data: Union[Unset, list["VideoFileModel"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        links: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        included: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.included, Unset):
            included = self.included.to_dict()

        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if meta is not UNSET:
            field_dict["meta"] = meta
        if links is not UNSET:
            field_dict["links"] = links
        if included is not UNSET:
            field_dict["included"] = included
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.included_data import IncludedData
        from ..models.response_links import ResponseLinks
        from ..models.response_meta_data import ResponseMetaData
        from ..models.video_file_model import VideoFileModel

        d = dict(src_dict)
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResponseMetaData]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResponseMetaData.from_dict(_meta)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ResponseLinks.from_dict(_links)

        _included = d.pop("included", UNSET)
        included: Union[Unset, IncludedData]
        if isinstance(_included, Unset):
            included = UNSET
        else:
            included = IncludedData.from_dict(_included)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = VideoFileModel.from_dict(data_item_data)

            data.append(data_item)

        video_file_insert_video_files_response = cls(
            meta=meta,
            links=links,
            included=included,
            data=data,
        )

        video_file_insert_video_files_response.additional_properties = d
        return video_file_insert_video_files_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
