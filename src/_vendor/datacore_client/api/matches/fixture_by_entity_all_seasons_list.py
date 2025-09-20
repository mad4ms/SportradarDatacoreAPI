import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_by_entity_all_seasons_list_competitor_type import (
    FixtureByEntityAllSeasonsListCompetitorType,
)
from ...models.fixture_by_entity_all_seasons_list_fixture_type import (
    FixtureByEntityAllSeasonsListFixtureType,
)
from ...models.fixture_by_entity_all_seasons_list_response_default import (
    FixtureByEntityAllSeasonsListResponseDefault,
)
from ...models.fixture_by_entity_all_seasons_list_status import (
    FixtureByEntityAllSeasonsListStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    entity_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityAllSeasonsListCompetitorType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityAllSeasonsListFixtureType] = UNSET,
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
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityAllSeasonsListStatus] = UNSET,
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

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

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
        "url": f"/handball/o/{organization_id}/entities/{entity_id}/fixtures",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> FixtureByEntityAllSeasonsListResponseDefault:
    response_default = FixtureByEntityAllSeasonsListResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FixtureByEntityAllSeasonsListResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityAllSeasonsListCompetitorType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityAllSeasonsListFixtureType] = UNSET,
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
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityAllSeasonsListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[FixtureByEntityAllSeasonsListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityAllSeasonsListCompetitorType]):  Example:
            PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityAllSeasonsListFixtureType]):  Example: REGULAR.
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
        season_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityAllSeasonsListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureByEntityAllSeasonsListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        entity_id=entity_id,
        added=added,
        competitor_type=competitor_type,
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
        season_id=season_id,
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
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityAllSeasonsListCompetitorType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityAllSeasonsListFixtureType] = UNSET,
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
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityAllSeasonsListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[FixtureByEntityAllSeasonsListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityAllSeasonsListCompetitorType]):  Example:
            PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityAllSeasonsListFixtureType]):  Example: REGULAR.
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
        season_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityAllSeasonsListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureByEntityAllSeasonsListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        entity_id=entity_id,
        client=client,
        added=added,
        competitor_type=competitor_type,
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
        season_id=season_id,
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
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityAllSeasonsListCompetitorType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityAllSeasonsListFixtureType] = UNSET,
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
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityAllSeasonsListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[FixtureByEntityAllSeasonsListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityAllSeasonsListCompetitorType]):  Example:
            PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityAllSeasonsListFixtureType]):  Example: REGULAR.
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
        season_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityAllSeasonsListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureByEntityAllSeasonsListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        entity_id=entity_id,
        added=added,
        competitor_type=competitor_type,
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
        season_id=season_id,
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
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, FixtureByEntityAllSeasonsListCompetitorType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, FixtureByEntityAllSeasonsListFixtureType] = UNSET,
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
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    status: Union[Unset, FixtureByEntityAllSeasonsListStatus] = UNSET,
    times_unconfirmed: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[FixtureByEntityAllSeasonsListResponseDefault]:
    """Get a list of matches for a Team

     Return a list of matches, for a specific Team

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, FixtureByEntityAllSeasonsListCompetitorType]):  Example:
            PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, FixtureByEntityAllSeasonsListFixtureType]):  Example: REGULAR.
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
        season_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        sort_by (Union[Unset, str]):  Example: -startTimeUTC.
        stage_code (Union[Unset, str]):  Example: ST1.
        status (Union[Unset, FixtureByEntityAllSeasonsListStatus]):  Example: SCHEDULED.
        times_unconfirmed (Union[Unset, bool]):  Example: True.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureByEntityAllSeasonsListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            entity_id=entity_id,
            client=client,
            added=added,
            competitor_type=competitor_type,
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
            season_id=season_id,
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
