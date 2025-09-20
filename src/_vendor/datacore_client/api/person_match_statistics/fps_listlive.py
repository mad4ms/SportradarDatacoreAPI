import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fps_listlive_fixture_person_statistics_response import (
    FpsListliveFixturePersonStatisticsResponse,
)
from ...models.fps_listlive_response_default import FpsListliveResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    participated: Union[Unset, bool] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_entity_id: Union[Unset, str] = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = str(entity_id)
    params["entityId"] = json_entity_id

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["isPlayer"] = is_player

    params["isTeamOfficial"] = is_team_official

    params["limit"] = limit

    params["offset"] = offset

    params["participated"] = participated

    json_person_id: Union[Unset, str] = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    params["starter"] = starter

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/person/in/fixtures/{fixture_id}/live",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]:
    if response.status_code == 200:
        response_200 = FpsListliveFixturePersonStatisticsResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = FpsListliveResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]
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
    *,
    client: AuthenticatedClient,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    participated: Union[Unset, bool] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]
]:
    """Person total statistics - live


        Return a list of live person total statistics for a match. Statistics are the totals
        (all periods added together) for the match. This call will return records of matches still in-
    progress
        if available.  If the match is complete this call operates the same as the non 'live' route.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        participated (Union[Unset, bool]):  Example: True.
        person_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        participated=participated,
        person_id=person_id,
        starter=starter,
        updated=updated,
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
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    participated: Union[Unset, bool] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]
]:
    """Person total statistics - live


        Return a list of live person total statistics for a match. Statistics are the totals
        (all periods added together) for the match. This call will return records of matches still in-
    progress
        if available.  If the match is complete this call operates the same as the non 'live' route.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        participated (Union[Unset, bool]):  Example: True.
        person_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_id=fixture_id,
        client=client,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        participated=participated,
        person_id=person_id,
        starter=starter,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    participated: Union[Unset, bool] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]
]:
    """Person total statistics - live


        Return a list of live person total statistics for a match. Statistics are the totals
        (all periods added together) for the match. This call will return records of matches still in-
    progress
        if available.  If the match is complete this call operates the same as the non 'live' route.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        participated (Union[Unset, bool]):  Example: True.
        person_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        participated=participated,
        person_id=person_id,
        starter=starter,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    participated: Union[Unset, bool] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]
]:
    """Person total statistics - live


        Return a list of live person total statistics for a match. Statistics are the totals
        (all periods added together) for the match. This call will return records of matches still in-
    progress
        if available.  If the match is complete this call operates the same as the non 'live' route.

        Rate limited to 2 requests every minute - returns HTTP 429 Too Many Requests if called more
    often.


    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        participated (Union[Unset, bool]):  Example: True.
        person_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FpsListliveFixturePersonStatisticsResponse, FpsListliveResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_id=fixture_id,
            client=client,
            added=added,
            entity_id=entity_id,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            is_player=is_player,
            is_team_official=is_team_official,
            limit=limit,
            offset=offset,
            participated=participated,
            person_id=person_id,
            starter=starter,
            updated=updated,
        )
    ).parsed
