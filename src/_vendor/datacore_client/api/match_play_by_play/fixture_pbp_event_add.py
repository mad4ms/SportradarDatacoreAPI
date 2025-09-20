from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_pbp_event_add_fixture_pbp_event_post_body import (
    FixturePbpEventAddFixturePBPEventPostBody,
)
from ...models.fixture_pbp_event_add_fixture_pbp_event_response import (
    FixturePbpEventAddFixturePbpEventResponse,
)
from ...models.fixture_pbp_event_add_period_id import FixturePbpEventAddPeriodId
from ...models.fixture_pbp_event_add_response_default import (
    FixturePbpEventAddResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpEventAddPeriodId,
    *,
    body: FixturePbpEventAddFixturePBPEventPostBody,
    external: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["external"] = external

    params["section"] = section

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/handball/o/{organization_id}/fixtures/{fixture_id}/periods/{period_id}/playbyplay",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault
]:
    if response.status_code == 200:
        response_200 = FixturePbpEventAddFixturePbpEventResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = FixturePbpEventAddResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpEventAddPeriodId,
    *,
    client: AuthenticatedClient,
    body: FixturePbpEventAddFixturePBPEventPostBody,
    external: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Response[
    Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]
]:
    """Add an individual a match play-by-play event

     Add a specific period play-by-play from a match event

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpEventAddPeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        section (Union[Unset, str]):
        body (FixturePbpEventAddFixturePBPEventPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        period_id=period_id,
        body=body,
        external=external,
        section=section,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpEventAddPeriodId,
    *,
    client: AuthenticatedClient,
    body: FixturePbpEventAddFixturePBPEventPostBody,
    external: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Optional[
    Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]
]:
    """Add an individual a match play-by-play event

     Add a specific period play-by-play from a match event

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpEventAddPeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        section (Union[Unset, str]):
        body (FixturePbpEventAddFixturePBPEventPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_id=fixture_id,
        period_id=period_id,
        client=client,
        body=body,
        external=external,
        section=section,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpEventAddPeriodId,
    *,
    client: AuthenticatedClient,
    body: FixturePbpEventAddFixturePBPEventPostBody,
    external: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Response[
    Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]
]:
    """Add an individual a match play-by-play event

     Add a specific period play-by-play from a match event

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpEventAddPeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        section (Union[Unset, str]):
        body (FixturePbpEventAddFixturePBPEventPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        period_id=period_id,
        body=body,
        external=external,
        section=section,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpEventAddPeriodId,
    *,
    client: AuthenticatedClient,
    body: FixturePbpEventAddFixturePBPEventPostBody,
    external: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Optional[
    Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]
]:
    """Add an individual a match play-by-play event

     Add a specific period play-by-play from a match event

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpEventAddPeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        section (Union[Unset, str]):
        body (FixturePbpEventAddFixturePBPEventPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FixturePbpEventAddFixturePbpEventResponse, FixturePbpEventAddResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_id=fixture_id,
            period_id=period_id,
            client=client,
            body=body,
            external=external,
            section=section,
        )
    ).parsed
