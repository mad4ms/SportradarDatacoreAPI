from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_pbp_external_delete_period_id import FixturePbpExternalDeletePeriodId
from ...models.fixture_pbp_external_delete_response_default import FixturePbpExternalDeleteResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpExternalDeletePeriodId,
    *,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["external"] = external

    params["fields"] = fields

    params["forceDelete"] = force_delete

    params["hideNull"] = hide_null

    params["include"] = include

    params["section"] = section

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/handball/o/{organization_id}/fixtures/{fixture_id}/periods/{period_id}/playbyplay/external",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> FixturePbpExternalDeleteResponseDefault:
    response_default = FixturePbpExternalDeleteResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FixturePbpExternalDeleteResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpExternalDeletePeriodId,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Response[FixturePbpExternalDeleteResponseDefault]:
    """Delete a match play-by-play external

     Delete a specific period play-by-play external from a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpExternalDeletePeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        section (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixturePbpExternalDeleteResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        period_id=period_id,
        external=external,
        fields=fields,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
        section=section,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpExternalDeletePeriodId,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Optional[FixturePbpExternalDeleteResponseDefault]:
    """Delete a match play-by-play external

     Delete a specific period play-by-play external from a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpExternalDeletePeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        section (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixturePbpExternalDeleteResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_id=fixture_id,
        period_id=period_id,
        client=client,
        external=external,
        fields=fields,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
        section=section,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpExternalDeletePeriodId,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Response[FixturePbpExternalDeleteResponseDefault]:
    """Delete a match play-by-play external

     Delete a specific period play-by-play external from a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpExternalDeletePeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        section (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixturePbpExternalDeleteResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        period_id=period_id,
        external=external,
        fields=fields,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
        section=section,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    fixture_id: UUID,
    period_id: FixturePbpExternalDeletePeriodId,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
) -> Optional[FixturePbpExternalDeleteResponseDefault]:
    """Delete a match play-by-play external

     Delete a specific period play-by-play external from a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        period_id (FixturePbpExternalDeletePeriodId):
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        section (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixturePbpExternalDeleteResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_id=fixture_id,
            period_id=period_id,
            client=client,
            external=external,
            fields=fields,
            force_delete=force_delete,
            hide_null=hide_null,
            include=include,
            section=section,
        )
    ).parsed
