from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.leader_criteria_list_response_default import LeaderCriteriaListResponseDefault
from ...models.leader_criteria_response import LeaderCriteriaResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["name"] = name

    params["nameContains"] = name_contains

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/leaders/criteria",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]:
    if response.status_code == 200:
        response_200 = LeaderCriteriaResponse.from_dict(response.json())

        return response_200

    response_default = LeaderCriteriaListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]]:
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]]:
    """Get a list of leader criteria sets

     Return a list of leader criteria sets

    Args:
        organization_id (str):  Example: b1a23.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):  Example: Dav and name='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name=name,
        name_contains=name_contains,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]]:
    """Get a list of leader criteria sets

     Return a list of leader criteria sets

    Args:
        organization_id (str):  Example: b1a23.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):  Example: Dav and name='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name=name,
        name_contains=name_contains,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]]:
    """Get a list of leader criteria sets

     Return a list of leader criteria sets

    Args:
        organization_id (str):  Example: b1a23.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):  Example: Dav and name='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name=name,
        name_contains=name_contains,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name: Union[Unset, str] = UNSET,
    name_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]]:
    """Get a list of leader criteria sets

     Return a list of leader criteria sets

    Args:
        organization_id (str):  Example: b1a23.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name (Union[Unset, str]):
        name_contains (Union[Unset, str]):  Example: Dav and name='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LeaderCriteriaListResponseDefault, LeaderCriteriaResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            name=name,
            name_contains=name_contains,
            offset=offset,
        )
    ).parsed
