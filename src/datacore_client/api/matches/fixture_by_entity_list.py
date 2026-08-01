import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_by_entity_list_competitor_type import FixtureByEntityListCompetitorType
from ...models.fixture_by_entity_list_discipline import FixtureByEntityListDiscipline
from ...models.fixture_by_entity_list_fixture_type import FixtureByEntityListFixtureType
from ...models.fixture_by_entity_list_response_default import FixtureByEntityListResponseDefault
from ...models.fixture_by_entity_list_status import FixtureByEntityListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    entity_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureByEntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_home: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityListStatus] = UNSET,
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

    params["isHome"] = is_home

    params["limit"] = limit

    params["liveDataAvailable"] = live_data_available

    params["liveVideoAvailable"] = live_video_available

    params["locked"] = locked

    params["offset"] = offset

    params["poolCode"] = pool_code

    params["roundCode"] = round_code

    params["roundNumber"] = round_number

    params["seriesCode"] = series_code

    params["sortBy"] = sort_by

    params["stageCode"] = stage_code

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

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
        "url": f"/handball/o/{organization_id}/seasons/{season_id}/entities/{entity_id}/fixtures",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> FixtureByEntityListResponseDefault:
    response_default = FixtureByEntityListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FixtureByEntityListResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    season_id: UUID,
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureByEntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_home: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[FixtureByEntityListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, within ~seasonprefix~ season, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureByEntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_home (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureByEntityListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        entity_id=entity_id,
        added=added,
        competitor_type=competitor_type,
        discipline=discipline,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        is_home=is_home,
        limit=limit,
        live_data_available=live_data_available,
        live_video_available=live_video_available,
        locked=locked,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        series_code=series_code,
        sort_by=sort_by,
        stage_code=stage_code,
        status=status,
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
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureByEntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_home: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[FixtureByEntityListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, within ~seasonprefix~ season, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureByEntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_home (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureByEntityListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        entity_id=entity_id,
        client=client,
        added=added,
        competitor_type=competitor_type,
        discipline=discipline,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        is_home=is_home,
        limit=limit,
        live_data_available=live_data_available,
        live_video_available=live_video_available,
        locked=locked,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        series_code=series_code,
        sort_by=sort_by,
        stage_code=stage_code,
        status=status,
        times_unconfirmed=times_unconfirmed,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        updated=updated,
        venue_id=venue_id,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureByEntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_home: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[FixtureByEntityListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, within ~seasonprefix~ season, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureByEntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_home (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureByEntityListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        entity_id=entity_id,
        added=added,
        competitor_type=competitor_type,
        discipline=discipline,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        is_home=is_home,
        limit=limit,
        live_data_available=live_data_available,
        live_video_available=live_video_available,
        locked=locked,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        series_code=series_code,
        sort_by=sort_by,
        stage_code=stage_code,
        status=status,
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
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityListCompetitorType] = UNSET,
    discipline: Union[Unset, FixtureByEntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_home: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    live_data_available: Union[Unset, bool] = UNSET,
    live_video_available: Union[Unset, bool] = UNSET,
    locked: Union[Unset, bool] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    series_code: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[FixtureByEntityListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, within ~seasonprefix~ season, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityListCompetitorType]):  Example: PERSON.
        discipline (Union[Unset, FixtureByEntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_home (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        live_data_available (Union[Unset, bool]):  Example: True.
        live_video_available (Union[Unset, bool]):  Example: True.
        locked (Union[Unset, bool]):  Example: True.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        series_code (Union[Unset, str]):  Example: WC1.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureByEntityListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            entity_id=entity_id,
            client=client,
            added=added,
            competitor_type=competitor_type,
            discipline=discipline,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            from_time_local=from_time_local,
            from_time_utc=from_time_utc,
            hide_null=hide_null,
            include=include,
            is_home=is_home,
            limit=limit,
            live_data_available=live_data_available,
            live_video_available=live_video_available,
            locked=locked,
            offset=offset,
            pool_code=pool_code,
            round_code=round_code,
            round_number=round_number,
            series_code=series_code,
            sort_by=sort_by,
            stage_code=stage_code,
            status=status,
            times_unconfirmed=times_unconfirmed,
            to_time_local=to_time_local,
            to_time_utc=to_time_utc,
            updated=updated,
            venue_id=venue_id,
        )
    ).parsed
