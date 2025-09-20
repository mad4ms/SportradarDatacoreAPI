import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.season_entity_list_by_multiple_seasons_response_default import (
    SeasonEntityListByMultipleSeasonsResponseDefault,
)
from ...models.season_entity_list_by_multiple_seasons_season_entities_list_response import (
    SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_ids: Union[Unset, UUID] = UNSET,
    entity_name_full_latin_contains: Union[Unset, str] = UNSET,
    entity_name_full_local_contains: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_entity_ids: Union[Unset, str] = UNSET
    if not isinstance(entity_ids, Unset):
        json_entity_ids = str(entity_ids)
    params["entityIds"] = json_entity_ids

    params["entityNameFullLatinContains"] = entity_name_full_latin_contains

    params["entityNameFullLocalContains"] = entity_name_full_local_contains

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_season_ids: Union[Unset, str] = UNSET
    if not isinstance(season_ids, Unset):
        json_season_ids = str(season_ids)
    params["seasonIds"] = json_season_ids

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/seasons/entities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    SeasonEntityListByMultipleSeasonsResponseDefault,
    SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse,
]:
    if response.status_code == 200:
        response_200 = (
            SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse.from_dict(
                response.json()
            )
        )

        return response_200

    response_default = SeasonEntityListByMultipleSeasonsResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        SeasonEntityListByMultipleSeasonsResponseDefault,
        SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse,
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
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_ids: Union[Unset, UUID] = UNSET,
    entity_name_full_latin_contains: Union[Unset, str] = UNSET,
    entity_name_full_local_contains: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        SeasonEntityListByMultipleSeasonsResponseDefault,
        SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse,
    ]
]:
    """Get a list of seasons and its participating teams

     Return a list of seasons and its participating teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        entity_name_full_latin_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLatin='David Johnson'.
        entity_name_full_local_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLocal='David Johnson'.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonEntityListByMultipleSeasonsResponseDefault, SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        entity_ids=entity_ids,
        entity_name_full_latin_contains=entity_name_full_latin_contains,
        entity_name_full_local_contains=entity_name_full_local_contains,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_ids=season_ids,
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
    entity_ids: Union[Unset, UUID] = UNSET,
    entity_name_full_latin_contains: Union[Unset, str] = UNSET,
    entity_name_full_local_contains: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        SeasonEntityListByMultipleSeasonsResponseDefault,
        SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse,
    ]
]:
    """Get a list of seasons and its participating teams

     Return a list of seasons and its participating teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        entity_name_full_latin_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLatin='David Johnson'.
        entity_name_full_local_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLocal='David Johnson'.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonEntityListByMultipleSeasonsResponseDefault, SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        entity_ids=entity_ids,
        entity_name_full_latin_contains=entity_name_full_latin_contains,
        entity_name_full_local_contains=entity_name_full_local_contains,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_ids=season_ids,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_ids: Union[Unset, UUID] = UNSET,
    entity_name_full_latin_contains: Union[Unset, str] = UNSET,
    entity_name_full_local_contains: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        SeasonEntityListByMultipleSeasonsResponseDefault,
        SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse,
    ]
]:
    """Get a list of seasons and its participating teams

     Return a list of seasons and its participating teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        entity_name_full_latin_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLatin='David Johnson'.
        entity_name_full_local_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLocal='David Johnson'.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonEntityListByMultipleSeasonsResponseDefault, SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        entity_ids=entity_ids,
        entity_name_full_latin_contains=entity_name_full_latin_contains,
        entity_name_full_local_contains=entity_name_full_local_contains,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_ids=season_ids,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_ids: Union[Unset, UUID] = UNSET,
    entity_name_full_latin_contains: Union[Unset, str] = UNSET,
    entity_name_full_local_contains: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        SeasonEntityListByMultipleSeasonsResponseDefault,
        SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse,
    ]
]:
    """Get a list of seasons and its participating teams

     Return a list of seasons and its participating teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        entity_name_full_latin_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLatin='David Johnson'.
        entity_name_full_local_contains (Union[Unset, str]):  Example: Dav and
            entityNameFullLocal='David Johnson'.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonEntityListByMultipleSeasonsResponseDefault, SeasonEntityListByMultipleSeasonsSeasonEntitiesListResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            entity_ids=entity_ids,
            entity_name_full_latin_contains=entity_name_full_latin_contains,
            entity_name_full_local_contains=entity_name_full_local_contains,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            season_ids=season_ids,
            updated=updated,
        )
    ).parsed
