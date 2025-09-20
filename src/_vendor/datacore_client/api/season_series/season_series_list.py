import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.season_series_list_response_default import SeasonSeriesListResponseDefault
from ...models.season_series_list_series_type import SeasonSeriesListSeriesType
from ...models.season_series_response import SeasonSeriesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    series_code_contains: Union[Unset, str] = UNSET,
    series_type: Union[Unset, SeasonSeriesListSeriesType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["nameLatinContains"] = name_latin_contains

    params["nameLocalContains"] = name_local_contains

    params["offset"] = offset

    params["poolCode"] = pool_code

    params["seriesCodeContains"] = series_code_contains

    json_series_type: Union[Unset, str] = UNSET
    if not isinstance(series_type, Unset):
        json_series_type = series_type.value

    params["seriesType"] = json_series_type

    params["sortBy"] = sort_by

    params["stageCode"] = stage_code

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/seasons/{season_id}/series",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]:
    if response.status_code == 200:
        response_200 = SeasonSeriesResponse.from_dict(response.json())

        return response_200

    response_default = SeasonSeriesListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]]:
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    series_code_contains: Union[Unset, str] = UNSET,
    series_type: Union[Unset, SeasonSeriesListSeriesType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]]:
    """Get a list of series

     Return a list of series for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        series_code_contains (Union[Unset, str]):  Example: SER and seriesCode='SERIES1'.
        series_type (Union[Unset, SeasonSeriesListSeriesType]):  Example: BEST_OF.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        stage_code (Union[Unset, str]):  Example: ST1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        pool_code=pool_code,
        series_code_contains=series_code_contains,
        series_type=series_type,
        sort_by=sort_by,
        stage_code=stage_code,
        updated=updated,
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    series_code_contains: Union[Unset, str] = UNSET,
    series_type: Union[Unset, SeasonSeriesListSeriesType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]]:
    """Get a list of series

     Return a list of series for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        series_code_contains (Union[Unset, str]):  Example: SER and seriesCode='SERIES1'.
        series_type (Union[Unset, SeasonSeriesListSeriesType]):  Example: BEST_OF.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        stage_code (Union[Unset, str]):  Example: ST1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        pool_code=pool_code,
        series_code_contains=series_code_contains,
        series_type=series_type,
        sort_by=sort_by,
        stage_code=stage_code,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    series_code_contains: Union[Unset, str] = UNSET,
    series_type: Union[Unset, SeasonSeriesListSeriesType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]]:
    """Get a list of series

     Return a list of series for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        series_code_contains (Union[Unset, str]):  Example: SER and seriesCode='SERIES1'.
        series_type (Union[Unset, SeasonSeriesListSeriesType]):  Example: BEST_OF.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        stage_code (Union[Unset, str]):  Example: ST1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        pool_code=pool_code,
        series_code_contains=series_code_contains,
        series_type=series_type,
        sort_by=sort_by,
        stage_code=stage_code,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    series_code_contains: Union[Unset, str] = UNSET,
    series_type: Union[Unset, SeasonSeriesListSeriesType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]]:
    """Get a list of series

     Return a list of series for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        series_code_contains (Union[Unset, str]):  Example: SER and seriesCode='SERIES1'.
        series_type (Union[Unset, SeasonSeriesListSeriesType]):  Example: BEST_OF.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        stage_code (Union[Unset, str]):  Example: ST1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonSeriesListResponseDefault, SeasonSeriesResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            added=added,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            name_latin_contains=name_latin_contains,
            name_local_contains=name_local_contains,
            offset=offset,
            pool_code=pool_code,
            series_code_contains=series_code_contains,
            series_type=series_type,
            sort_by=sort_by,
            stage_code=stage_code,
            updated=updated,
        )
    ).parsed
