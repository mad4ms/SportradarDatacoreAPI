import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity_group_list_response_default import EntityGroupListResponseDefault
from ...models.entity_group_list_status import EntityGroupListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, EntityGroupListStatus] = UNSET,
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

    params["nameFullLatinContains"] = name_full_latin_contains

    params["nameFullLocalContains"] = name_full_local_contains

    params["offset"] = offset

    params["sortBy"] = sort_by

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/entityGroups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> EntityGroupListResponseDefault:
    response_default = EntityGroupListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EntityGroupListResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, EntityGroupListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[EntityGroupListResponseDefault]:
    """Get a list of clubs

     Return a list of available clubs

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, EntityGroupListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityGroupListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        sort_by=sort_by,
        status=status,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, EntityGroupListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[EntityGroupListResponseDefault]:
    """Get a list of clubs

     Return a list of available clubs

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, EntityGroupListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityGroupListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        sort_by=sort_by,
        status=status,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, EntityGroupListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[EntityGroupListResponseDefault]:
    """Get a list of clubs

     Return a list of available clubs

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, EntityGroupListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityGroupListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        sort_by=sort_by,
        status=status,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, EntityGroupListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[EntityGroupListResponseDefault]:
    """Get a list of clubs

     Return a list of available clubs

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, EntityGroupListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityGroupListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            name_full_latin_contains=name_full_latin_contains,
            name_full_local_contains=name_full_local_contains,
            offset=offset,
            sort_by=sort_by,
            status=status,
            updated=updated,
        )
    ).parsed
