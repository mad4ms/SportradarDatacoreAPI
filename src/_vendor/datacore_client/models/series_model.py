import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.series_model_series_type import SeriesModelSeriesType
from ..models.series_model_status import SeriesModelStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.series_model_conference import SeriesModelConference
    from ..models.series_model_division import SeriesModelDivision
    from ..models.series_model_organization import SeriesModelOrganization
    from ..models.series_model_pool import SeriesModelPool
    from ..models.series_model_season import SeriesModelSeason
    from ..models.series_model_season_series_competitor import SeriesModelSeasonSeriesCompetitor
    from ..models.series_model_stage import SeriesModelStage


T = TypeVar("T", bound="SeriesModel")


@_attrs_define
class SeriesModel:
    """
    Attributes:
        series_code (Union[Unset, str]): A unique code for the season series. (Unique for season) Example: ST1.
        season_id (Union[Unset, UUID]): The unique identifier of the season Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season (Union[Unset, SeriesModelSeason]): The season linked to this record
        organization_id (Union[Unset, str]): The unique identifier of the organization Example: 9.
        organization (Union[Unset, SeriesModelOrganization]): The organization that this series belongs to
        conference_id (Union[None, UUID, Unset]): The unique identifier of the conference Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conference (Union[Unset, SeriesModelConference]): The conference information
        division_id (Union[None, UUID, Unset]): The unique identifier of the division Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division (Union[Unset, SeriesModelDivision]): The division information
        name_local (Union[Unset, str]): The name of the series in the [local](#section/Introduction/Character-Sets-and-
            Names) language Example: Test name local.
        abbreviation_local (Union[None, Unset, str]): An abbreviation/short name in the
            [local](#section/Introduction/Character-Sets-and-Names) language Example: NFA.
        name_latin (Union[None, Unset, str]): The name of the series in [latin](#section/Introduction/Character-Sets-
            and-Names) characters Example: Test name latin .
        abbreviation_latin (Union[None, Unset, str]): An abbreviation/short name in
            [latin](#section/Introduction/Character-Sets-and-Names) characters Example: NFA.
        status (Union[Unset, SeriesModelStatus]): Status
            >- `ACTIVE` Active
            >- `COMPLETE` Complete
            >- `NOT_STARTED` Not Started
             Example: COMPLETE.
        series_type (Union[Unset, SeriesModelSeriesType]): The type of series
            >- `BEST_OF` Best of
            >- `HOME_AND_AWAY` Home and Away
            >- `KNOCKOUT` Knockout
             Example: BEST_OF.
        auto_calculated (Union[Unset, bool]): Is the winner auto calculated? Example: True.
        best_of (Union[None, Unset, int]): Best of number Example: 1.
        series_number (Union[None, Unset, int]): User defined series number Example: 1.
        max_fixtures_number (Union[None, Unset, int]): The maximum number of games within a playoff series Example: 1.
        winner (Union[None, UUID, Unset]): The unique identifier of the winner, person or entity Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        series_order (Union[None, Unset, int]): User defined sort order of the series Example: 1.
        stage_code (Union[None, Unset, str]): A unique code for the stage. (Unique for season) Example: ST1.
        stage (Union[Unset, SeriesModelStage]): The stage that is related to this record
        pool_code (Union[None, Unset, str]): A unique code for the pool. (Unique for season) Example: P1.
        pool (Union[Unset, SeriesModelPool]): The pool that is related to this record
        start_date (Union[None, Unset, datetime.date]): Series start date Example: 2016-09-08.
        end_date (Union[None, Unset, datetime.date]): Series end date Example: 2016-09-08.
        external_id (Union[None, Unset, str]): The Id of the data as set by the provider of the data Example: A123.
        updated (Union[Unset, datetime.datetime]): Date/time last modified. In UTC
        added (Union[Unset, datetime.datetime]): Date/time added. In UTC
        competitors (Union[None, Unset, list['SeriesModelSeasonSeriesCompetitor']]): Array of competitors in the series.
            A competitor may have a results and a ranking
    """

    series_code: Union[Unset, str] = UNSET
    season_id: Union[Unset, UUID] = UNSET
    season: Union[Unset, "SeriesModelSeason"] = UNSET
    organization_id: Union[Unset, str] = UNSET
    organization: Union[Unset, "SeriesModelOrganization"] = UNSET
    conference_id: Union[None, UUID, Unset] = UNSET
    conference: Union[Unset, "SeriesModelConference"] = UNSET
    division_id: Union[None, UUID, Unset] = UNSET
    division: Union[Unset, "SeriesModelDivision"] = UNSET
    name_local: Union[Unset, str] = UNSET
    abbreviation_local: Union[None, Unset, str] = UNSET
    name_latin: Union[None, Unset, str] = UNSET
    abbreviation_latin: Union[None, Unset, str] = UNSET
    status: Union[Unset, SeriesModelStatus] = UNSET
    series_type: Union[Unset, SeriesModelSeriesType] = UNSET
    auto_calculated: Union[Unset, bool] = UNSET
    best_of: Union[None, Unset, int] = UNSET
    series_number: Union[None, Unset, int] = UNSET
    max_fixtures_number: Union[None, Unset, int] = UNSET
    winner: Union[None, UUID, Unset] = UNSET
    series_order: Union[None, Unset, int] = UNSET
    stage_code: Union[None, Unset, str] = UNSET
    stage: Union[Unset, "SeriesModelStage"] = UNSET
    pool_code: Union[None, Unset, str] = UNSET
    pool: Union[Unset, "SeriesModelPool"] = UNSET
    start_date: Union[None, Unset, datetime.date] = UNSET
    end_date: Union[None, Unset, datetime.date] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    updated: Union[Unset, datetime.datetime] = UNSET
    added: Union[Unset, datetime.datetime] = UNSET
    competitors: Union[None, Unset, list["SeriesModelSeasonSeriesCompetitor"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        series_code = self.series_code

        season_id: Union[Unset, str] = UNSET
        if not isinstance(self.season_id, Unset):
            season_id = str(self.season_id)

        season: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.season, Unset):
            season = self.season.to_dict()

        organization_id = self.organization_id

        organization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        conference_id: Union[None, Unset, str]
        if isinstance(self.conference_id, Unset):
            conference_id = UNSET
        elif isinstance(self.conference_id, UUID):
            conference_id = str(self.conference_id)
        else:
            conference_id = self.conference_id

        conference: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.conference, Unset):
            conference = self.conference.to_dict()

        division_id: Union[None, Unset, str]
        if isinstance(self.division_id, Unset):
            division_id = UNSET
        elif isinstance(self.division_id, UUID):
            division_id = str(self.division_id)
        else:
            division_id = self.division_id

        division: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.division, Unset):
            division = self.division.to_dict()

        name_local = self.name_local

        abbreviation_local: Union[None, Unset, str]
        if isinstance(self.abbreviation_local, Unset):
            abbreviation_local = UNSET
        else:
            abbreviation_local = self.abbreviation_local

        name_latin: Union[None, Unset, str]
        if isinstance(self.name_latin, Unset):
            name_latin = UNSET
        else:
            name_latin = self.name_latin

        abbreviation_latin: Union[None, Unset, str]
        if isinstance(self.abbreviation_latin, Unset):
            abbreviation_latin = UNSET
        else:
            abbreviation_latin = self.abbreviation_latin

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        series_type: Union[Unset, str] = UNSET
        if not isinstance(self.series_type, Unset):
            series_type = self.series_type.value

        auto_calculated = self.auto_calculated

        best_of: Union[None, Unset, int]
        if isinstance(self.best_of, Unset):
            best_of = UNSET
        else:
            best_of = self.best_of

        series_number: Union[None, Unset, int]
        if isinstance(self.series_number, Unset):
            series_number = UNSET
        else:
            series_number = self.series_number

        max_fixtures_number: Union[None, Unset, int]
        if isinstance(self.max_fixtures_number, Unset):
            max_fixtures_number = UNSET
        else:
            max_fixtures_number = self.max_fixtures_number

        winner: Union[None, Unset, str]
        if isinstance(self.winner, Unset):
            winner = UNSET
        elif isinstance(self.winner, UUID):
            winner = str(self.winner)
        else:
            winner = self.winner

        series_order: Union[None, Unset, int]
        if isinstance(self.series_order, Unset):
            series_order = UNSET
        else:
            series_order = self.series_order

        stage_code: Union[None, Unset, str]
        if isinstance(self.stage_code, Unset):
            stage_code = UNSET
        else:
            stage_code = self.stage_code

        stage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.stage, Unset):
            stage = self.stage.to_dict()

        pool_code: Union[None, Unset, str]
        if isinstance(self.pool_code, Unset):
            pool_code = UNSET
        else:
            pool_code = self.pool_code

        pool: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pool, Unset):
            pool = self.pool.to_dict()

        start_date: Union[None, Unset, str]
        if isinstance(self.start_date, Unset):
            start_date = UNSET
        elif isinstance(self.start_date, datetime.date):
            start_date = self.start_date.isoformat()
        else:
            start_date = self.start_date

        end_date: Union[None, Unset, str]
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.date):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        updated: Union[Unset, str] = UNSET
        if not isinstance(self.updated, Unset):
            updated = self.updated.isoformat()

        added: Union[Unset, str] = UNSET
        if not isinstance(self.added, Unset):
            added = self.added.isoformat()

        competitors: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.competitors, Unset):
            competitors = UNSET
        elif isinstance(self.competitors, list):
            competitors = []
            for competitors_type_0_item_data in self.competitors:
                competitors_type_0_item = competitors_type_0_item_data.to_dict()
                competitors.append(competitors_type_0_item)

        else:
            competitors = self.competitors

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if series_code is not UNSET:
            field_dict["seriesCode"] = series_code
        if season_id is not UNSET:
            field_dict["seasonId"] = season_id
        if season is not UNSET:
            field_dict["season"] = season
        if organization_id is not UNSET:
            field_dict["organizationId"] = organization_id
        if organization is not UNSET:
            field_dict["organization"] = organization
        if conference_id is not UNSET:
            field_dict["conferenceId"] = conference_id
        if conference is not UNSET:
            field_dict["conference"] = conference
        if division_id is not UNSET:
            field_dict["divisionId"] = division_id
        if division is not UNSET:
            field_dict["division"] = division
        if name_local is not UNSET:
            field_dict["nameLocal"] = name_local
        if abbreviation_local is not UNSET:
            field_dict["abbreviationLocal"] = abbreviation_local
        if name_latin is not UNSET:
            field_dict["nameLatin"] = name_latin
        if abbreviation_latin is not UNSET:
            field_dict["abbreviationLatin"] = abbreviation_latin
        if status is not UNSET:
            field_dict["status"] = status
        if series_type is not UNSET:
            field_dict["seriesType"] = series_type
        if auto_calculated is not UNSET:
            field_dict["autoCalculated"] = auto_calculated
        if best_of is not UNSET:
            field_dict["bestOf"] = best_of
        if series_number is not UNSET:
            field_dict["seriesNumber"] = series_number
        if max_fixtures_number is not UNSET:
            field_dict["maxFixturesNumber"] = max_fixtures_number
        if winner is not UNSET:
            field_dict["winner"] = winner
        if series_order is not UNSET:
            field_dict["seriesOrder"] = series_order
        if stage_code is not UNSET:
            field_dict["stageCode"] = stage_code
        if stage is not UNSET:
            field_dict["stage"] = stage
        if pool_code is not UNSET:
            field_dict["poolCode"] = pool_code
        if pool is not UNSET:
            field_dict["pool"] = pool
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if updated is not UNSET:
            field_dict["updated"] = updated
        if added is not UNSET:
            field_dict["added"] = added
        if competitors is not UNSET:
            field_dict["competitors"] = competitors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.series_model_conference import SeriesModelConference
        from ..models.series_model_division import SeriesModelDivision
        from ..models.series_model_organization import SeriesModelOrganization
        from ..models.series_model_pool import SeriesModelPool
        from ..models.series_model_season import SeriesModelSeason
        from ..models.series_model_season_series_competitor import SeriesModelSeasonSeriesCompetitor
        from ..models.series_model_stage import SeriesModelStage

        d = dict(src_dict)
        series_code = d.pop("seriesCode", UNSET)

        _season_id = d.pop("seasonId", UNSET)
        season_id: Union[Unset, UUID]
        if isinstance(_season_id, Unset):
            season_id = UNSET
        else:
            season_id = UUID(_season_id)

        _season = d.pop("season", UNSET)
        season: Union[Unset, SeriesModelSeason]
        if isinstance(_season, Unset):
            season = UNSET
        else:
            season = SeriesModelSeason.from_dict(_season)

        organization_id = d.pop("organizationId", UNSET)

        _organization = d.pop("organization", UNSET)
        organization: Union[Unset, SeriesModelOrganization]
        if isinstance(_organization, Unset):
            organization = UNSET
        else:
            organization = SeriesModelOrganization.from_dict(_organization)

        def _parse_conference_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                conference_id_type_0 = UUID(data)

                return conference_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        conference_id = _parse_conference_id(d.pop("conferenceId", UNSET))

        _conference = d.pop("conference", UNSET)
        conference: Union[Unset, SeriesModelConference]
        if isinstance(_conference, Unset):
            conference = UNSET
        else:
            conference = SeriesModelConference.from_dict(_conference)

        def _parse_division_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                division_id_type_0 = UUID(data)

                return division_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        division_id = _parse_division_id(d.pop("divisionId", UNSET))

        _division = d.pop("division", UNSET)
        division: Union[Unset, SeriesModelDivision]
        if isinstance(_division, Unset):
            division = UNSET
        else:
            division = SeriesModelDivision.from_dict(_division)

        name_local = d.pop("nameLocal", UNSET)

        def _parse_abbreviation_local(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_local = _parse_abbreviation_local(d.pop("abbreviationLocal", UNSET))

        def _parse_name_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name_latin = _parse_name_latin(d.pop("nameLatin", UNSET))

        def _parse_abbreviation_latin(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        abbreviation_latin = _parse_abbreviation_latin(d.pop("abbreviationLatin", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, SeriesModelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SeriesModelStatus(_status)

        _series_type = d.pop("seriesType", UNSET)
        series_type: Union[Unset, SeriesModelSeriesType]
        if isinstance(_series_type, Unset):
            series_type = UNSET
        else:
            series_type = SeriesModelSeriesType(_series_type)

        auto_calculated = d.pop("autoCalculated", UNSET)

        def _parse_best_of(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        best_of = _parse_best_of(d.pop("bestOf", UNSET))

        def _parse_series_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        series_number = _parse_series_number(d.pop("seriesNumber", UNSET))

        def _parse_max_fixtures_number(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_fixtures_number = _parse_max_fixtures_number(d.pop("maxFixturesNumber", UNSET))

        def _parse_winner(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                winner_type_0 = UUID(data)

                return winner_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        winner = _parse_winner(d.pop("winner", UNSET))

        def _parse_series_order(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        series_order = _parse_series_order(d.pop("seriesOrder", UNSET))

        def _parse_stage_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stage_code = _parse_stage_code(d.pop("stageCode", UNSET))

        _stage = d.pop("stage", UNSET)
        stage: Union[Unset, SeriesModelStage]
        if isinstance(_stage, Unset):
            stage = UNSET
        else:
            stage = SeriesModelStage.from_dict(_stage)

        def _parse_pool_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        pool_code = _parse_pool_code(d.pop("poolCode", UNSET))

        _pool = d.pop("pool", UNSET)
        pool: Union[Unset, SeriesModelPool]
        if isinstance(_pool, Unset):
            pool = UNSET
        else:
            pool = SeriesModelPool.from_dict(_pool)

        def _parse_start_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_date_type_0 = isoparse(data).date()

                return start_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        start_date = _parse_start_date(d.pop("startDate", UNSET))

        def _parse_end_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data).date()

                return end_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        end_date = _parse_end_date(d.pop("endDate", UNSET))

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("externalId", UNSET))

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

        def _parse_competitors(data: object) -> Union[None, Unset, list["SeriesModelSeasonSeriesCompetitor"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                competitors_type_0 = []
                _competitors_type_0 = data
                for competitors_type_0_item_data in _competitors_type_0:
                    competitors_type_0_item = SeriesModelSeasonSeriesCompetitor.from_dict(competitors_type_0_item_data)

                    competitors_type_0.append(competitors_type_0_item)

                return competitors_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["SeriesModelSeasonSeriesCompetitor"]], data)

        competitors = _parse_competitors(d.pop("competitors", UNSET))

        series_model = cls(
            series_code=series_code,
            season_id=season_id,
            season=season,
            organization_id=organization_id,
            organization=organization,
            conference_id=conference_id,
            conference=conference,
            division_id=division_id,
            division=division,
            name_local=name_local,
            abbreviation_local=abbreviation_local,
            name_latin=name_latin,
            abbreviation_latin=abbreviation_latin,
            status=status,
            series_type=series_type,
            auto_calculated=auto_calculated,
            best_of=best_of,
            series_number=series_number,
            max_fixtures_number=max_fixtures_number,
            winner=winner,
            series_order=series_order,
            stage_code=stage_code,
            stage=stage,
            pool_code=pool_code,
            pool=pool,
            start_date=start_date,
            end_date=end_date,
            external_id=external_id,
            updated=updated,
            added=added,
            competitors=competitors,
        )

        return series_model
