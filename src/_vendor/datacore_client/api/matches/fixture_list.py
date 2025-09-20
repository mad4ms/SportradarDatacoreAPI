import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_list_competitor_type import FixtureListCompetitorType
from ...models.fixture_list_discipline import FixtureListDiscipline
from ...models.fixture_list_fixture_type import FixtureListFixtureType
from ...models.fixture_list_response_default import FixtureListResponseDefault
from ...models.fixture_list_status import FixtureListStatus
from ...models.fixture_list_status_not import FixtureListStatusNot
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    feature_match: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    series_fixture_number: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureListStatus] = UNSET,
    status_not: Union[Unset, FixtureListStatusNot] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_competitor_type: Union[Unset, str] = UNSET
    if not isinstance(competitor_type, Unset):
        json_competitor_type = competitor_type.value

    params["competitorType"] = json_competitor_type

    json_discipline: Union[Unset, str] = UNSET
    if not isinstance(discipline, Unset):
        json_discipline = discipline.value

    params["discipline"] = json_discipline

    params["external"] = external

    params["featureMatch"] = feature_match

    params["fields"] = fields

    json_fixture_type: Union[Unset, str] = UNSET
    if not isinstance(fixture_type, Unset):
        json_fixture_type = fixture_type.value

    params["fixtureType"] = json_fixture_type

    json_from_time_local: Union[Unset, str] = UNSET
    if not isinstance(from_time_local, Unset):
        json_from_time_local = from_time_local.isoformat()
    params["fromTimeLocal"] = json_from_time_local

    json_from_time_utc: Union[Unset, str] = UNSET
    if not isinstance(from_time_utc, Unset):
        json_from_time_utc = from_time_utc.isoformat()
    params["fromTimeUTC"] = json_from_time_utc

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["liveDataAvailable"] = live_data_available

    params["liveVideoAvailable"] = live_video_available

    params["locked"] = locked

    params["offset"] = offset

    params["poolCode"] = pool_code

    params["roundCode"] = round_code

    params["roundNumber"] = round_number

    params["seriesCode"] = series_code

    params["seriesFixtureNumber"] = series_fixture_number

    params["sortBy"] = sort_by

    params["stageCode"] = stage_code

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_status_not: Union[Unset, str] = UNSET
    if not isinstance(status_not, Unset):
        json_status_not = status_not.value

    params["statusNot"] = json_status_not

    params["timesUnconfirmed"] = times_unconfirmed

    json_to_time_local: Union[Unset, str] = UNSET
    if not isinstance(to_time_local, Unset):
        json_to_time_local = to_time_local.isoformat()
    params["toTimeLocal"] = json_to_time_local

    json_to_time_utc: Union[Unset, str] = UNSET
    if not isinstance(to_time_utc, Unset):
        json_to_time_utc = to_time_utc.isoformat()
    params["toTimeUTC"] = json_to_time_utc

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    json_venue_id: Union[Unset, str] = UNSET
    if not isinstance(venue_id, Unset):
        json_venue_id = str(venue_id)
    params["venueId"] = json_venue_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/seasons/{season_id}/fixtures",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> FixtureListResponseDefault:
    response_default = FixtureListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FixtureListResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    feature_match: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    series_fixture_number: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureListStatus] = UNSET,
    status_not: Union[Unset, FixtureListStatusNot] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[FixtureListResponseDefault]:
    """Get a list of matches

     Return a list of matches for the season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        feature_match (Union[Unset, bool]):  Example: True.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        series_fixture_number (Union[Unset, int]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC,fixtureNumber.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureListStatus]):  Example: SCHEDULED.
        status_not (Union[Unset, FixtureListStatusNot]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        competitor_type=competitor_type,
        discipline=discipline,
        external=external,
        feature_match=feature_match,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        live_data_available=live_data_available,
        live_video_available=live_video_available,
        locked=locked,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        series_code=series_code,
        series_fixture_number=series_fixture_number,
        sort_by=sort_by,
        stage_code=stage_code,
        status=status,
        status_not=status_not,
        times_unconfirmed=times_unconfirmed,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        updated=updated,
        venue_id=venue_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    feature_match: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    series_fixture_number: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureListStatus] = UNSET,
    status_not: Union[Unset, FixtureListStatusNot] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[FixtureListResponseDefault]:
    """Get a list of matches

     Return a list of matches for the season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        feature_match (Union[Unset, bool]):  Example: True.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        series_fixture_number (Union[Unset, int]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC,fixtureNumber.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureListStatus]):  Example: SCHEDULED.
        status_not (Union[Unset, FixtureListStatusNot]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        added=added,
        competitor_type=competitor_type,
        discipline=discipline,
        external=external,
        feature_match=feature_match,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        live_data_available=live_data_available,
        live_video_available=live_video_available,
        locked=locked,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        series_code=series_code,
        series_fixture_number=series_fixture_number,
        sort_by=sort_by,
        stage_code=stage_code,
        status=status,
        status_not=status_not,
        times_unconfirmed=times_unconfirmed,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        updated=updated,
        venue_id=venue_id,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    feature_match: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    series_fixture_number: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureListStatus] = UNSET,
    status_not: Union[Unset, FixtureListStatusNot] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[FixtureListResponseDefault]:
    """Get a list of matches

     Return a list of matches for the season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        feature_match (Union[Unset, bool]):  Example: True.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        series_fixture_number (Union[Unset, int]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC,fixtureNumber.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureListStatus]):  Example: SCHEDULED.
        status_not (Union[Unset, FixtureListStatusNot]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        competitor_type=competitor_type,
        discipline=discipline,
        external=external,
        feature_match=feature_match,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        live_data_available=live_data_available,
        live_video_available=live_video_available,
        locked=locked,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        series_code=series_code,
        series_fixture_number=series_fixture_number,
        sort_by=sort_by,
        stage_code=stage_code,
        status=status,
        status_not=status_not,
        times_unconfirmed=times_unconfirmed,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        updated=updated,
        venue_id=venue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    feature_match: Union[Unset, bool] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    series_fixture_number: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureListStatus] = UNSET,
    status_not: Union[Unset, FixtureListStatusNot] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[FixtureListResponseDefault]:
    """Get a list of matches

     Return a list of matches for the season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        feature_match (Union[Unset, bool]):  Example: True.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        series_fixture_number (Union[Unset, int]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC,fixtureNumber.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureListStatus]):  Example: SCHEDULED.
        status_not (Union[Unset, FixtureListStatusNot]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            added=added,
            competitor_type=competitor_type,
            discipline=discipline,
            external=external,
            feature_match=feature_match,
            fields=fields,
            fixture_type=fixture_type,
            from_time_local=from_time_local,
            from_time_utc=from_time_utc,
            hide_null=hide_null,
            include=include,
            limit=limit,
            live_data_available=live_data_available,
            live_video_available=live_video_available,
            locked=locked,
            offset=offset,
            pool_code=pool_code,
            round_code=round_code,
            round_number=round_number,
            series_code=series_code,
            series_fixture_number=series_fixture_number,
            sort_by=sort_by,
            stage_code=stage_code,
            status=status,
            status_not=status_not,
            times_unconfirmed=times_unconfirmed,
            to_time_local=to_time_local,
            to_time_utc=to_time_utc,
            updated=updated,
            venue_id=venue_id,
        )
    ).parsed
