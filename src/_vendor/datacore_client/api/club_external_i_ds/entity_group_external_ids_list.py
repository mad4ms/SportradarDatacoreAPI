import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity_group_external_ids_list_response_default import EntityGroupExternalIdsListResponseDefault
from ...models.entity_group_external_ids_response import EntityGroupExternalIdsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_group_id: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_external_id: Union[Unset, str] = UNSET,
    source_type: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    params["entityGroupId"] = entity_group_id

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    params["source"] = source

    params["sourceExternalId"] = source_external_id

    params["sourceType"] = source_type

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/entityGroups/externalids",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]:
    if response.status_code == 200:
        response_200 = EntityGroupExternalIdsResponse.from_dict(response.json())

        return response_200

    response_default = EntityGroupExternalIdsListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]]:
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
    entity_group_id: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_external_id: Union[Unset, str] = UNSET,
    source_type: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]]:
    """Get a list of a club external ids

     A list of club external ids

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_group_id (Union[Unset, str]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        source (Union[Unset, str]):
        source_external_id (Union[Unset, str]):
        source_type (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        entity_group_id=entity_group_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        source=source,
        source_external_id=source_external_id,
        source_type=source_type,
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
    entity_group_id: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_external_id: Union[Unset, str] = UNSET,
    source_type: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]]:
    """Get a list of a club external ids

     A list of club external ids

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_group_id (Union[Unset, str]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        source (Union[Unset, str]):
        source_external_id (Union[Unset, str]):
        source_type (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        entity_group_id=entity_group_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        source=source,
        source_external_id=source_external_id,
        source_type=source_type,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_group_id: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_external_id: Union[Unset, str] = UNSET,
    source_type: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]]:
    """Get a list of a club external ids

     A list of club external ids

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_group_id (Union[Unset, str]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        source (Union[Unset, str]):
        source_external_id (Union[Unset, str]):
        source_type (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        entity_group_id=entity_group_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        source=source,
        source_external_id=source_external_id,
        source_type=source_type,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_group_id: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    source: Union[Unset, str] = UNSET,
    source_external_id: Union[Unset, str] = UNSET,
    source_type: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]]:
    """Get a list of a club external ids

     A list of club external ids

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_group_id (Union[Unset, str]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        source (Union[Unset, str]):
        source_external_id (Union[Unset, str]):
        source_type (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityGroupExternalIdsListResponseDefault, EntityGroupExternalIdsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            entity_group_id=entity_group_id,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            source=source,
            source_external_id=source_external_id,
            source_type=source_type,
            updated=updated,
        )
    ).parsed
