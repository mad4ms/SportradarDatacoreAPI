import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.uniform_items_by_season_list_item_type import (
    UniformItemsBySeasonListItemType,
)
from ...models.uniform_items_by_season_list_response_default import (
    UniformItemsBySeasonListResponseDefault,
)
from ...models.uniform_items_by_season_list_uniform_items_response import (
    UniformItemsBySeasonListUniformItemsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    item_type: Union[Unset, UniformItemsBySeasonListItemType] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_date_from_end: Union[Unset, str] = UNSET
    if not isinstance(date_from_end, Unset):
        json_date_from_end = date_from_end.isoformat()
    params["dateFromEnd"] = json_date_from_end

    json_date_from_start: Union[Unset, str] = UNSET
    if not isinstance(date_from_start, Unset):
        json_date_from_start = date_from_start.isoformat()
    params["dateFromStart"] = json_date_from_start

    json_date_to_end: Union[Unset, str] = UNSET
    if not isinstance(date_to_end, Unset):
        json_date_to_end = date_to_end.isoformat()
    params["dateToEnd"] = json_date_to_end

    json_date_to_start: Union[Unset, str] = UNSET
    if not isinstance(date_to_start, Unset):
        json_date_to_start = date_to_start.isoformat()
    params["dateToStart"] = json_date_to_start

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    json_item_type: Union[Unset, str] = UNSET
    if not isinstance(item_type, Unset):
        json_item_type = item_type.value

    params["itemType"] = json_item_type

    params["limit"] = limit

    params["nameLatinContains"] = name_latin_contains

    params["nameLocalContains"] = name_local_contains

    params["offset"] = offset

    params["sortBy"] = sort_by

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/seasons/{season_id}/uniforms/items",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    UniformItemsBySeasonListResponseDefault,
    UniformItemsBySeasonListUniformItemsResponse,
]:
    if response.status_code == 200:
        response_200 = UniformItemsBySeasonListUniformItemsResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = UniformItemsBySeasonListResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        UniformItemsBySeasonListResponseDefault,
        UniformItemsBySeasonListUniformItemsResponse,
    ]
]:
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
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    item_type: Union[Unset, UniformItemsBySeasonListItemType] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        UniformItemsBySeasonListResponseDefault,
        UniformItemsBySeasonListUniformItemsResponse,
    ]
]:
    """Get a list of Uniform Items for a season

     Return a list of Uniform Items for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        item_type (Union[Unset, UniformItemsBySeasonListItemType]):  Example: JERSEY.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UniformItemsBySeasonListResponseDefault, UniformItemsBySeasonListUniformItemsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        date_from_end=date_from_end,
        date_from_start=date_from_start,
        date_to_end=date_to_end,
        date_to_start=date_to_start,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        item_type=item_type,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        sort_by=sort_by,
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
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    item_type: Union[Unset, UniformItemsBySeasonListItemType] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        UniformItemsBySeasonListResponseDefault,
        UniformItemsBySeasonListUniformItemsResponse,
    ]
]:
    """Get a list of Uniform Items for a season

     Return a list of Uniform Items for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        item_type (Union[Unset, UniformItemsBySeasonListItemType]):  Example: JERSEY.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UniformItemsBySeasonListResponseDefault, UniformItemsBySeasonListUniformItemsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        added=added,
        date_from_end=date_from_end,
        date_from_start=date_from_start,
        date_to_end=date_to_end,
        date_to_start=date_to_start,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        item_type=item_type,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        sort_by=sort_by,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    item_type: Union[Unset, UniformItemsBySeasonListItemType] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        UniformItemsBySeasonListResponseDefault,
        UniformItemsBySeasonListUniformItemsResponse,
    ]
]:
    """Get a list of Uniform Items for a season

     Return a list of Uniform Items for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        item_type (Union[Unset, UniformItemsBySeasonListItemType]):  Example: JERSEY.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UniformItemsBySeasonListResponseDefault, UniformItemsBySeasonListUniformItemsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        date_from_end=date_from_end,
        date_from_start=date_from_start,
        date_to_end=date_to_end,
        date_to_start=date_to_start,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        item_type=item_type,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        sort_by=sort_by,
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
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    item_type: Union[Unset, UniformItemsBySeasonListItemType] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        UniformItemsBySeasonListResponseDefault,
        UniformItemsBySeasonListUniformItemsResponse,
    ]
]:
    """Get a list of Uniform Items for a season

     Return a list of Uniform Items for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        item_type (Union[Unset, UniformItemsBySeasonListItemType]):  Example: JERSEY.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UniformItemsBySeasonListResponseDefault, UniformItemsBySeasonListUniformItemsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            added=added,
            date_from_end=date_from_end,
            date_from_start=date_from_start,
            date_to_end=date_to_end,
            date_to_start=date_to_start,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            item_type=item_type,
            limit=limit,
            name_latin_contains=name_latin_contains,
            name_local_contains=name_local_contains,
            offset=offset,
            sort_by=sort_by,
            updated=updated,
        )
    ).parsed
