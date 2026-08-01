from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.match_model_broadcasts_broadcast_type import MatchModelBroadcastsBroadcastType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchModelBroadcasts")


@_attrs_define
class MatchModelBroadcasts:
    """
    Attributes:
        broadcast_type (Union[Unset, MatchModelBroadcastsBroadcastType]): Broadcast Type Example: TV.
        broadcaster (Union[Unset, str]): Broadcaster Name Local Example: XYZ Network.
        broadcaster_url (Union[Unset, str]): Broadcaster Home URL Example: www.XYZNetwork.com.
        broadcast_url (Union[Unset, str]): Fixture Broadcast URL Example: www.XYZNetwork.com/fixture/123.
        broadcast_timezone (Union[Unset, str]): Timezone of the broadcast Example: Australia/Sydney.
        locale (Union[Unset, str]): Locale of the broadcast Example: en-EN.
        start_time_local (Union[Unset, Any]): Start Time of the broadcast Example: 2023-01-01.
    """

    broadcast_type: Union[Unset, MatchModelBroadcastsBroadcastType] = UNSET
    broadcaster: Union[Unset, str] = UNSET
    broadcaster_url: Union[Unset, str] = UNSET
    broadcast_url: Union[Unset, str] = UNSET
    broadcast_timezone: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    start_time_local: Union[Unset, Any] = UNSET

    def to_dict(self) -> dict[str, Any]:
        broadcast_type: Union[Unset, str] = UNSET
        if not isinstance(self.broadcast_type, Unset):
            broadcast_type = self.broadcast_type.value

        broadcaster = self.broadcaster

        broadcaster_url = self.broadcaster_url

        broadcast_url = self.broadcast_url

        broadcast_timezone = self.broadcast_timezone

        locale = self.locale

        start_time_local = self.start_time_local

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if broadcast_type is not UNSET:
            field_dict["broadcastType"] = broadcast_type
        if broadcaster is not UNSET:
            field_dict["broadcaster"] = broadcaster
        if broadcaster_url is not UNSET:
            field_dict["broadcasterURL"] = broadcaster_url
        if broadcast_url is not UNSET:
            field_dict["broadcastURL"] = broadcast_url
        if broadcast_timezone is not UNSET:
            field_dict["broadcastTimezone"] = broadcast_timezone
        if locale is not UNSET:
            field_dict["locale"] = locale
        if start_time_local is not UNSET:
            field_dict["startTimeLocal"] = start_time_local

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _broadcast_type = d.pop("broadcastType", UNSET)
        broadcast_type: Union[Unset, MatchModelBroadcastsBroadcastType]
        if isinstance(_broadcast_type, Unset):
            broadcast_type = UNSET
        else:
            broadcast_type = MatchModelBroadcastsBroadcastType(_broadcast_type)

        broadcaster = d.pop("broadcaster", UNSET)

        broadcaster_url = d.pop("broadcasterURL", UNSET)

        broadcast_url = d.pop("broadcastURL", UNSET)

        broadcast_timezone = d.pop("broadcastTimezone", UNSET)

        locale = d.pop("locale", UNSET)

        start_time_local = d.pop("startTimeLocal", UNSET)

        match_model_broadcasts = cls(
            broadcast_type=broadcast_type,
            broadcaster=broadcaster,
            broadcaster_url=broadcaster_url,
            broadcast_url=broadcast_url,
            broadcast_timezone=broadcast_timezone,
            locale=locale,
            start_time_local=start_time_local,
        )

        return match_model_broadcasts
