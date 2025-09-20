from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fixture_profiles_detail_response_default import FixtureProfilesDetailResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    profile_id: UUID,
    *,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/fixtureProfiles/{profile_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> FixtureProfilesDetailResponseDefault:
    response_default = FixtureProfilesDetailResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[FixtureProfilesDetailResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    profile_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Response[FixtureProfilesDetailResponseDefault]:
    """Get a match profile

     Return detailed information about a specific match profile

    Args:
        organization_id (str):  Example: b1a23.
        profile_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureProfilesDetailResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        profile_id=profile_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    profile_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Optional[FixtureProfilesDetailResponseDefault]:
    """Get a match profile

     Return detailed information about a specific match profile

    Args:
        organization_id (str):  Example: b1a23.
        profile_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureProfilesDetailResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        profile_id=profile_id,
        client=client,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    profile_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Response[FixtureProfilesDetailResponseDefault]:
    """Get a match profile

     Return detailed information about a specific match profile

    Args:
        organization_id (str):  Example: b1a23.
        profile_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FixtureProfilesDetailResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        profile_id=profile_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    profile_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
) -> Optional[FixtureProfilesDetailResponseDefault]:
    """Get a match profile

     Return detailed information about a specific match profile

    Args:
        organization_id (str):  Example: b1a23.
        profile_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FixtureProfilesDetailResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            profile_id=profile_id,
            client=client,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
        )
    ).parsed
