from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.venue_external_ids_update_response_default import (
    VenueExternalIdsUpdateResponseDefault,
)
from ...models.venue_external_ids_update_venue_external_ids_put_body import (
    VenueExternalIdsUpdateVenueExternalIdsPutBody,
)
from ...models.venue_external_ids_update_venue_external_ids_response import (
    VenueExternalIdsUpdateVenueExternalIdsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    venue_external_id: UUID,
    *,
    body: VenueExternalIdsUpdateVenueExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/handball/o/{organization_id}/venues/externalids/{venue_external_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    VenueExternalIdsUpdateResponseDefault,
    VenueExternalIdsUpdateVenueExternalIdsResponse,
]:
    if response.status_code == 200:
        response_200 = VenueExternalIdsUpdateVenueExternalIdsResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = VenueExternalIdsUpdateResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        VenueExternalIdsUpdateResponseDefault,
        VenueExternalIdsUpdateVenueExternalIdsResponse,
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
    venue_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: VenueExternalIdsUpdateVenueExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        VenueExternalIdsUpdateResponseDefault,
        VenueExternalIdsUpdateVenueExternalIdsResponse,
    ]
]:
    """Update a venue external identifier information

     Change the external identifier information of a specific venue

    Args:
        organization_id (str):  Example: b1a23.
        venue_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (VenueExternalIdsUpdateVenueExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VenueExternalIdsUpdateResponseDefault, VenueExternalIdsUpdateVenueExternalIdsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        venue_external_id=venue_external_id,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    venue_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: VenueExternalIdsUpdateVenueExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        VenueExternalIdsUpdateResponseDefault,
        VenueExternalIdsUpdateVenueExternalIdsResponse,
    ]
]:
    """Update a venue external identifier information

     Change the external identifier information of a specific venue

    Args:
        organization_id (str):  Example: b1a23.
        venue_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (VenueExternalIdsUpdateVenueExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VenueExternalIdsUpdateResponseDefault, VenueExternalIdsUpdateVenueExternalIdsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        venue_external_id=venue_external_id,
        client=client,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    venue_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: VenueExternalIdsUpdateVenueExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        VenueExternalIdsUpdateResponseDefault,
        VenueExternalIdsUpdateVenueExternalIdsResponse,
    ]
]:
    """Update a venue external identifier information

     Change the external identifier information of a specific venue

    Args:
        organization_id (str):  Example: b1a23.
        venue_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (VenueExternalIdsUpdateVenueExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VenueExternalIdsUpdateResponseDefault, VenueExternalIdsUpdateVenueExternalIdsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        venue_external_id=venue_external_id,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    venue_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: VenueExternalIdsUpdateVenueExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        VenueExternalIdsUpdateResponseDefault,
        VenueExternalIdsUpdateVenueExternalIdsResponse,
    ]
]:
    """Update a venue external identifier information

     Change the external identifier information of a specific venue

    Args:
        organization_id (str):  Example: b1a23.
        venue_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (VenueExternalIdsUpdateVenueExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VenueExternalIdsUpdateResponseDefault, VenueExternalIdsUpdateVenueExternalIdsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            venue_external_id=venue_external_id,
            client=client,
            body=body,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
