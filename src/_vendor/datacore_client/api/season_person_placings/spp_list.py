import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.season_person_placings_response import SeasonPersonPlacingsResponse
from ...models.spp_list_response_default import SppListResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
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

    params["offset"] = offset

    json_person_id: Union[Unset, str] = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/seasons/{season_id}/persons/placings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[SeasonPersonPlacingsResponse, SppListResponseDefault]:
    if response.status_code == 200:
        response_200 = SeasonPersonPlacingsResponse.from_dict(response.json())

        return response_200

    response_default = SppListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SeasonPersonPlacingsResponse, SppListResponseDefault]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[SeasonPersonPlacingsResponse, SppListResponseDefault]]:
    """Get a list of placings for persons in a season

     Return a list of final placings for a person in a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonPersonPlacingsResponse, SppListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[SeasonPersonPlacingsResponse, SppListResponseDefault]]:
    """Get a list of placings for persons in a season

     Return a list of final placings for a person in a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonPersonPlacingsResponse, SppListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[SeasonPersonPlacingsResponse, SppListResponseDefault]]:
    """Get a list of placings for persons in a season

     Return a list of final placings for a person in a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonPersonPlacingsResponse, SppListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[SeasonPersonPlacingsResponse, SppListResponseDefault]]:
    """Get a list of placings for persons in a season

     Return a list of final placings for a person in a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonPersonPlacingsResponse, SppListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            added=added,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            person_id=person_id,
            updated=updated,
        )
    ).parsed
