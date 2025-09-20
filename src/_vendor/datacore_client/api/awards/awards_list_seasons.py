import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.awards_list_seasons_award import AwardsListSeasonsAward
from ...models.awards_list_seasons_response_default import AwardsListSeasonsResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    award: Union[Unset, AwardsListSeasonsAward] = UNSET,
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_award: Union[Unset, str] = UNSET
    if not isinstance(award, Unset):
        json_award = award.value

    params["award"] = json_award

    json_date_from_end: Union[Unset, str] = UNSET
    if not isinstance(date_from_end, Unset):
        json_date_from_end = date_from_end.isoformat()
    params["dateFromEnd"] = json_date_from_end

    json_date_from_start: Union[Unset, str] = UNSET
    if not isinstance(date_from_start, Unset):
        json_date_from_start = date_from_start.isoformat()
    params["dateFromStart"] = json_date_from_start

    json_date_to_end: Union[Unset, str] = UNSET
    if not isinstance(date_to_end, Unset):
        json_date_to_end = date_to_end.isoformat()
    params["dateToEnd"] = json_date_to_end

    json_date_to_start: Union[Unset, str] = UNSET
    if not isinstance(date_to_start, Unset):
        json_date_to_start = date_to_start.isoformat()
    params["dateToStart"] = json_date_to_start

    json_entity_id: Union[Unset, str] = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = str(entity_id)
    params["entityId"] = json_entity_id

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

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/awards/in/seasons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> AwardsListSeasonsResponseDefault:
    response_default = AwardsListSeasonsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AwardsListSeasonsResponseDefault]:
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
    added: Union[Unset, datetime.datetime] = UNSET,
    award: Union[Unset, AwardsListSeasonsAward] = UNSET,
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[AwardsListSeasonsResponseDefault]:
    """Get a list of season awards

     Return a list of awards for the organization (linked to seasons)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        award (Union[Unset, AwardsListSeasonsAward]):  Example: MVP.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AwardsListSeasonsResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        award=award,
        date_from_end=date_from_end,
        date_from_start=date_from_start,
        date_to_end=date_to_end,
        date_to_start=date_to_start,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        season_id=season_id,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    award: Union[Unset, AwardsListSeasonsAward] = UNSET,
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[AwardsListSeasonsResponseDefault]:
    """Get a list of season awards

     Return a list of awards for the organization (linked to seasons)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        award (Union[Unset, AwardsListSeasonsAward]):  Example: MVP.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AwardsListSeasonsResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        award=award,
        date_from_end=date_from_end,
        date_from_start=date_from_start,
        date_to_end=date_to_end,
        date_to_start=date_to_start,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        season_id=season_id,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    award: Union[Unset, AwardsListSeasonsAward] = UNSET,
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[AwardsListSeasonsResponseDefault]:
    """Get a list of season awards

     Return a list of awards for the organization (linked to seasons)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        award (Union[Unset, AwardsListSeasonsAward]):  Example: MVP.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AwardsListSeasonsResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        award=award,
        date_from_end=date_from_end,
        date_from_start=date_from_start,
        date_to_end=date_to_end,
        date_to_start=date_to_start,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        season_id=season_id,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    award: Union[Unset, AwardsListSeasonsAward] = UNSET,
    date_from_end: Union[Unset, datetime.date] = UNSET,
    date_from_start: Union[Unset, datetime.date] = UNSET,
    date_to_end: Union[Unset, datetime.date] = UNSET,
    date_to_start: Union[Unset, datetime.date] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[AwardsListSeasonsResponseDefault]:
    """Get a list of season awards

     Return a list of awards for the organization (linked to seasons)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        award (Union[Unset, AwardsListSeasonsAward]):  Example: MVP.
        date_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AwardsListSeasonsResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            award=award,
            date_from_end=date_from_end,
            date_from_start=date_from_start,
            date_to_end=date_to_end,
            date_to_start=date_to_start,
            entity_id=entity_id,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            person_id=person_id,
            season_id=season_id,
            updated=updated,
        )
    ).parsed
