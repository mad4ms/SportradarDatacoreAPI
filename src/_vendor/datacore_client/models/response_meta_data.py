import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ResponseMetaData")


@_attrs_define
class ResponseMetaData:
    """
    Attributes:
        version (Union[Unset, int]): The version of the API in use for this call Example: 1.
        code_version (Union[Unset, str]): A string indicating the version of the code that handled this request Example:
            d6cd1e2bd19e03a81132a23b2025920577f84e37.
        code (Union[Unset, int]): The HTTP response code for this request Example: 200.
        time (Union[Unset, datetime.datetime]): The date/time this request was made (in UTC). Example:
            2018-06-05T23:43:41.227Z.
        from_cache (Union[Unset, bool]): Was this request served directly from the cache?
        count (Union[Unset, int]): The number of records being returned Example: 7.
        limit (Union[Unset, int]): The record limit in place for this request Example: 10.
        offset (Union[Unset, int]): The record offset in place for this request Example: 10.
        generation_time (Union[Unset, float]): The number of seconds taken to generate this request. Example: 0.011604.
    """

    version: Union[Unset, int] = UNSET
    code_version: Union[Unset, str] = UNSET
    code: Union[Unset, int] = UNSET
    time: Union[Unset, datetime.datetime] = UNSET
    from_cache: Union[Unset, bool] = UNSET
    count: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    generation_time: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        version = self.version

        code_version = self.code_version

        code = self.code

        time: Union[Unset, str] = UNSET
        if not isinstance(self.time, Unset):
            time = self.time.isoformat()

        from_cache = self.from_cache

        count = self.count

        limit = self.limit

        offset = self.offset

        generation_time = self.generation_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if code_version is not UNSET:
            field_dict["codeVersion"] = code_version
        if code is not UNSET:
            field_dict["code"] = code
        if time is not UNSET:
            field_dict["time"] = time
        if from_cache is not UNSET:
            field_dict["fromCache"] = from_cache
        if count is not UNSET:
            field_dict["count"] = count
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if generation_time is not UNSET:
            field_dict["generationTime"] = generation_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        version = d.pop("version", UNSET)

        code_version = d.pop("codeVersion", UNSET)

        code = d.pop("code", UNSET)

        _time = d.pop("time", UNSET)
        time: Union[Unset, datetime.datetime]
        if isinstance(_time, Unset):
            time = UNSET
        else:
            time = isoparse(_time)

        from_cache = d.pop("fromCache", UNSET)

        count = d.pop("count", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        generation_time = d.pop("generationTime", UNSET)

        response_meta_data = cls(
            version=version,
            code_version=code_version,
            code=code,
            time=time,
            from_cache=from_cache,
            count=count,
            limit=limit,
            offset=offset,
            generation_time=generation_time,
        )

        response_meta_data.additional_properties = d
        return response_meta_data

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
