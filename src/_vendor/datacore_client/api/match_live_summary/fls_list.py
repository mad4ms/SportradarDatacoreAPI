from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_live_summary_response import FixtureLiveSummaryResponse
from ...models.fls_list_response_default import FlsListResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_id: UUID,
    *,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/fixtures/{fixture_id}/summary/live",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[FixtureLiveSummaryResponse, FlsListResponseDefault]:
    if response.status_code == 200:
        response_200 = FixtureLiveSummaryResponse.from_dict(response.json())

        return response_200

    response_default = FlsListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[FixtureLiveSummaryResponse, FlsListResponseDefault]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[FixtureLiveSummaryResponse, FlsListResponseDefault]]:
    """Match Live Summary


        Return summary data for a match currently in progress on the streaming API.  This call will only
    return data
        when the match is in progress - not post match.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FixtureLiveSummaryResponse, FlsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[FixtureLiveSummaryResponse, FlsListResponseDefault]]:
    """Match Live Summary


        Return summary data for a match currently in progress on the streaming API.  This call will only
    return data
        when the match is in progress - not post match.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FixtureLiveSummaryResponse, FlsListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_id=fixture_id,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Response[Union[FixtureLiveSummaryResponse, FlsListResponseDefault]]:
    """Match Live Summary


        Return summary data for a match currently in progress on the streaming API.  This call will only
    return data
        when the match is in progress - not post match.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FixtureLiveSummaryResponse, FlsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Optional[Union[FixtureLiveSummaryResponse, FlsListResponseDefault]]:
    """Match Live Summary


        Return summary data for a match currently in progress on the streaming API.  This call will only
    return data
        when the match is in progress - not post match.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FixtureLiveSummaryResponse, FlsListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_id=fixture_id,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
