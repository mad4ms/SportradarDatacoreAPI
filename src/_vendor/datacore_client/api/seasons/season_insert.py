from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.season_insert_response_default import SeasonInsertResponseDefault
from ...models.season_insert_season_post_body import SeasonInsertSeasonPostBody
from ...models.season_insert_seasons_response import SeasonInsertSeasonsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    competition_id: UUID,
    *,
    body: SeasonInsertSeasonPostBody,
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
        "method": "post",
        "url": f"/handball/o/{organization_id}/competitions/{competition_id}/seasons",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]:
    if response.status_code == 200:
        response_200 = SeasonInsertSeasonsResponse.from_dict(response.json())

        return response_200

    response_default = SeasonInsertResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    competition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SeasonInsertSeasonPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]]:
    """Create a new season

     Add a new season

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (SeasonInsertSeasonPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        competition_id=competition_id,
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
    competition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SeasonInsertSeasonPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]]:
    """Create a new season

     Add a new season

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (SeasonInsertSeasonPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        competition_id=competition_id,
        client=client,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    competition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SeasonInsertSeasonPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]]:
    """Create a new season

     Add a new season

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (SeasonInsertSeasonPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        competition_id=competition_id,
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
    competition_id: UUID,
    *,
    client: AuthenticatedClient,
    body: SeasonInsertSeasonPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]]:
    """Create a new season

     Add a new season

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (SeasonInsertSeasonPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonInsertResponseDefault, SeasonInsertSeasonsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            competition_id=competition_id,
            client=client,
            body=body,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
