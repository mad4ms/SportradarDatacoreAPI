from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_external_ids_update_fixture_external_ids_response import (
    FixtureExternalIdsUpdateFixtureExternalIdsResponse,
)
from ...models.fixture_external_ids_update_match_external_ids_put_body import (
    FixtureExternalIdsUpdateMatchExternalIdsPutBody,
)
from ...models.fixture_external_ids_update_response_default import (
    FixtureExternalIdsUpdateResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_external_id: UUID,
    *,
    body: FixtureExternalIdsUpdateMatchExternalIdsPutBody,
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
        "url": f"/handball/o/{organization_id}/fixtures/externalids/{fixture_external_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    FixtureExternalIdsUpdateFixtureExternalIdsResponse,
    FixtureExternalIdsUpdateResponseDefault,
]:
    if response.status_code == 200:
        response_200 = FixtureExternalIdsUpdateFixtureExternalIdsResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = FixtureExternalIdsUpdateResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        FixtureExternalIdsUpdateFixtureExternalIdsResponse,
        FixtureExternalIdsUpdateResponseDefault,
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
    fixture_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FixtureExternalIdsUpdateMatchExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        FixtureExternalIdsUpdateFixtureExternalIdsResponse,
        FixtureExternalIdsUpdateResponseDefault,
    ]
]:
    """Update a match external identifier information

     Change the external identifier information of a specific match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (FixtureExternalIdsUpdateMatchExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FixtureExternalIdsUpdateFixtureExternalIdsResponse, FixtureExternalIdsUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_external_id=fixture_external_id,
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
    fixture_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FixtureExternalIdsUpdateMatchExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        FixtureExternalIdsUpdateFixtureExternalIdsResponse,
        FixtureExternalIdsUpdateResponseDefault,
    ]
]:
    """Update a match external identifier information

     Change the external identifier information of a specific match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (FixtureExternalIdsUpdateMatchExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FixtureExternalIdsUpdateFixtureExternalIdsResponse, FixtureExternalIdsUpdateResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_external_id=fixture_external_id,
        client=client,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    fixture_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FixtureExternalIdsUpdateMatchExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        FixtureExternalIdsUpdateFixtureExternalIdsResponse,
        FixtureExternalIdsUpdateResponseDefault,
    ]
]:
    """Update a match external identifier information

     Change the external identifier information of a specific match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (FixtureExternalIdsUpdateMatchExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FixtureExternalIdsUpdateFixtureExternalIdsResponse, FixtureExternalIdsUpdateResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_external_id=fixture_external_id,
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
    fixture_external_id: UUID,
    *,
    client: AuthenticatedClient,
    body: FixtureExternalIdsUpdateMatchExternalIdsPutBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        FixtureExternalIdsUpdateFixtureExternalIdsResponse,
        FixtureExternalIdsUpdateResponseDefault,
    ]
]:
    """Update a match external identifier information

     Change the external identifier information of a specific match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_external_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (FixtureExternalIdsUpdateMatchExternalIdsPutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FixtureExternalIdsUpdateFixtureExternalIdsResponse, FixtureExternalIdsUpdateResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_external_id=fixture_external_id,
            client=client,
            body=body,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
