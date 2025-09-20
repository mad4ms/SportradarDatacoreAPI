import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.season_model_seasonroster_configuration_season_roster_status_allowed_item import (
    SeasonModelSEASONROSTERConfigurationSeasonRosterStatusAllowedItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SeasonModelSEASONROSTERConfiguration")


@_attrs_define
class SeasonModelSEASONROSTERConfiguration:
    """Configuration for the SEASON ROSTER

    Attributes:
        window_open_date (Union[None, Unset, datetime.date]): What date can a SEASON ROSTER be submitted from for this
            SEASON? Example: 2023-01-01.
        window_close_date (Union[None, Unset, datetime.date]): What is the last date a SEASON ROSTER can be submitted
            from for this SEASON? Example: 2023-01-31.
        season_roster_lock (Union[None, Unset, bool]): Make SEASON ROSTERS un-editable when SEASON ROSTER Registration
            Window Close Date has elapsed. Example: True.
        fixture_roster_lock (Union[None, Unset, bool]): Make FIXTURE ROSTERS un-editable when MATCH Status is set to
            Scheduled
        fixture_bib_edit (Union[None, Unset, bool]): Allow Add/Edit of FIXTURE ROSTERS bib
        season_roster_status_allowed (Union[Unset,
            list[SeasonModelSEASONROSTERConfigurationSeasonRosterStatusAllowedItem]]): Season Roster status allowed
        publish_season_roster_roles_in_hours (Union[None, Unset, float]): How long before SEASON starts can rosters or
            roles be published (in hours) Example: True.
        publish_fixture_roster_roles_in_minutes (Union[None, Unset, float]): How long before a MATCH starts can rosters
            or roles be published (in minutes) Example: True.
    """

    window_open_date: Union[None, Unset, datetime.date] = UNSET
    window_close_date: Union[None, Unset, datetime.date] = UNSET
    season_roster_lock: Union[None, Unset, bool] = UNSET
    fixture_roster_lock: Union[None, Unset, bool] = UNSET
    fixture_bib_edit: Union[None, Unset, bool] = UNSET
    season_roster_status_allowed: Union[
        Unset, list[SeasonModelSEASONROSTERConfigurationSeasonRosterStatusAllowedItem]
    ] = UNSET
    publish_season_roster_roles_in_hours: Union[None, Unset, float] = UNSET
    publish_fixture_roster_roles_in_minutes: Union[None, Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        window_open_date: Union[None, Unset, str]
        if isinstance(self.window_open_date, Unset):
            window_open_date = UNSET
        elif isinstance(self.window_open_date, datetime.date):
            window_open_date = self.window_open_date.isoformat()
        else:
            window_open_date = self.window_open_date

        window_close_date: Union[None, Unset, str]
        if isinstance(self.window_close_date, Unset):
            window_close_date = UNSET
        elif isinstance(self.window_close_date, datetime.date):
            window_close_date = self.window_close_date.isoformat()
        else:
            window_close_date = self.window_close_date

        season_roster_lock: Union[None, Unset, bool]
        if isinstance(self.season_roster_lock, Unset):
            season_roster_lock = UNSET
        else:
            season_roster_lock = self.season_roster_lock

        fixture_roster_lock: Union[None, Unset, bool]
        if isinstance(self.fixture_roster_lock, Unset):
            fixture_roster_lock = UNSET
        else:
            fixture_roster_lock = self.fixture_roster_lock

        fixture_bib_edit: Union[None, Unset, bool]
        if isinstance(self.fixture_bib_edit, Unset):
            fixture_bib_edit = UNSET
        else:
            fixture_bib_edit = self.fixture_bib_edit

        season_roster_status_allowed: Union[Unset, list[str]] = UNSET
        if not isinstance(self.season_roster_status_allowed, Unset):
            season_roster_status_allowed = []
            for (
                season_roster_status_allowed_item_data
            ) in self.season_roster_status_allowed:
                season_roster_status_allowed_item = (
                    season_roster_status_allowed_item_data.value
                )
                season_roster_status_allowed.append(season_roster_status_allowed_item)

        publish_season_roster_roles_in_hours: Union[None, Unset, float]
        if isinstance(self.publish_season_roster_roles_in_hours, Unset):
            publish_season_roster_roles_in_hours = UNSET
        else:
            publish_season_roster_roles_in_hours = (
                self.publish_season_roster_roles_in_hours
            )

        publish_fixture_roster_roles_in_minutes: Union[None, Unset, float]
        if isinstance(self.publish_fixture_roster_roles_in_minutes, Unset):
            publish_fixture_roster_roles_in_minutes = UNSET
        else:
            publish_fixture_roster_roles_in_minutes = (
                self.publish_fixture_roster_roles_in_minutes
            )

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if window_open_date is not UNSET:
            field_dict["windowOpenDate"] = window_open_date
        if window_close_date is not UNSET:
            field_dict["windowCloseDate"] = window_close_date
        if season_roster_lock is not UNSET:
            field_dict["seasonRosterLock"] = season_roster_lock
        if fixture_roster_lock is not UNSET:
            field_dict["fixtureRosterLock"] = fixture_roster_lock
        if fixture_bib_edit is not UNSET:
            field_dict["fixtureBibEdit"] = fixture_bib_edit
        if season_roster_status_allowed is not UNSET:
            field_dict["seasonRosterStatusAllowed"] = season_roster_status_allowed
        if publish_season_roster_roles_in_hours is not UNSET:
            field_dict["publishSeasonRosterRolesInHours"] = (
                publish_season_roster_roles_in_hours
            )
        if publish_fixture_roster_roles_in_minutes is not UNSET:
            field_dict["publishFixtureRosterRolesInMinutes"] = (
                publish_fixture_roster_roles_in_minutes
            )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_window_open_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_open_date_type_0 = isoparse(data).date()

                return window_open_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        window_open_date = _parse_window_open_date(d.pop("windowOpenDate", UNSET))

        def _parse_window_close_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_close_date_type_0 = isoparse(data).date()

                return window_close_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        window_close_date = _parse_window_close_date(d.pop("windowCloseDate", UNSET))

        def _parse_season_roster_lock(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        season_roster_lock = _parse_season_roster_lock(d.pop("seasonRosterLock", UNSET))

        def _parse_fixture_roster_lock(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        fixture_roster_lock = _parse_fixture_roster_lock(
            d.pop("fixtureRosterLock", UNSET)
        )

        def _parse_fixture_bib_edit(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        fixture_bib_edit = _parse_fixture_bib_edit(d.pop("fixtureBibEdit", UNSET))

        season_roster_status_allowed = []
        _season_roster_status_allowed = d.pop("seasonRosterStatusAllowed", UNSET)
        for season_roster_status_allowed_item_data in (
            _season_roster_status_allowed or []
        ):
            season_roster_status_allowed_item = (
                SeasonModelSEASONROSTERConfigurationSeasonRosterStatusAllowedItem(
                    season_roster_status_allowed_item_data
                )
            )

            season_roster_status_allowed.append(season_roster_status_allowed_item)

        def _parse_publish_season_roster_roles_in_hours(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        publish_season_roster_roles_in_hours = (
            _parse_publish_season_roster_roles_in_hours(
                d.pop("publishSeasonRosterRolesInHours", UNSET)
            )
        )

        def _parse_publish_fixture_roster_roles_in_minutes(
            data: object,
        ) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        publish_fixture_roster_roles_in_minutes = (
            _parse_publish_fixture_roster_roles_in_minutes(
                d.pop("publishFixtureRosterRolesInMinutes", UNSET)
            )
        )

        season_model_seasonroster_configuration = cls(
            window_open_date=window_open_date,
            window_close_date=window_close_date,
            season_roster_lock=season_roster_lock,
            fixture_roster_lock=fixture_roster_lock,
            fixture_bib_edit=fixture_bib_edit,
            season_roster_status_allowed=season_roster_status_allowed,
            publish_season_roster_roles_in_hours=publish_season_roster_roles_in_hours,
            publish_fixture_roster_roles_in_minutes=publish_fixture_roster_roles_in_minutes,
        )

        return season_model_seasonroster_configuration
