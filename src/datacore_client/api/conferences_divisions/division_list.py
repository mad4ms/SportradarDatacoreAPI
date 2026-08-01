import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.division_list_divisions_response import DivisionListDivisionsResponse
from ...models.division_list_response_default import DivisionListResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    conference_id: UUID,
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
    sort_by: Union[Unset, str] = UNSET,
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

    params["sortBy"] = sort_by

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/conferences/{conference_id}/divisions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[DivisionListDivisionsResponse, DivisionListResponseDefault]:
    if response.status_code == 200:
        response_200 = DivisionListDivisionsResponse.from_dict(response.json())

        return response_200

    response_default = DivisionListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[DivisionListDivisionsResponse, DivisionListResponseDefault]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    conference_id: UUID,
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
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[DivisionListDivisionsResponse, DivisionListResponseDefault]]:
    """Get a list of divisions

     Return a list of available divisions for a specific conference

    Args:
        organization_id (str):  Example: b1a23.
        conference_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
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
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DivisionListDivisionsResponse, DivisionListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        conference_id=conference_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
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
    conference_id: UUID,
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
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[DivisionListDivisionsResponse, DivisionListResponseDefault]]:
    """Get a list of divisions

     Return a list of available divisions for a specific conference

    Args:
        organization_id (str):  Example: b1a23.
        conference_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
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
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DivisionListDivisionsResponse, DivisionListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        conference_id=conference_id,
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
        sort_by=sort_by,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    conference_id: UUID,
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
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[DivisionListDivisionsResponse, DivisionListResponseDefault]]:
    """Get a list of divisions

     Return a list of available divisions for a specific conference

    Args:
        organization_id (str):  Example: b1a23.
        conference_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
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
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DivisionListDivisionsResponse, DivisionListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        conference_id=conference_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
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
    conference_id: UUID,
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
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[DivisionListDivisionsResponse, DivisionListResponseDefault]]:
    """Get a list of divisions

     Return a list of available divisions for a specific conference

    Args:
        organization_id (str):  Example: b1a23.
        conference_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
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
        sort_by (Union[Unset, str]):  Example: nameLocal.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DivisionListDivisionsResponse, DivisionListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            conference_id=conference_id,
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
            sort_by=sort_by,
            updated=updated,
        )
    ).parsed
