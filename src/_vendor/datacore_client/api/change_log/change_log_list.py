import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.change_log_list_change_type import ChangeLogListChangeType
from ...models.change_log_list_response_default import ChangeLogListResponseDefault
from ...models.change_log_response import ChangeLogResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    change_type: Union[Unset, ChangeLogListChangeType] = UNSET,
    child_type: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    primary_id: Union[Unset, UUID] = UNSET,
    primary_type: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_change_type: Union[Unset, str] = UNSET
    if not isinstance(change_type, Unset):
        json_change_type = change_type.value

    params["changeType"] = json_change_type

    params["childType"] = child_type

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_primary_id: Union[Unset, str] = UNSET
    if not isinstance(primary_id, Unset):
        json_primary_id = str(primary_id)
    params["primaryId"] = json_primary_id

    params["primaryType"] = primary_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/changeLog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ChangeLogListResponseDefault, ChangeLogResponse]:
    if response.status_code == 200:
        response_200 = ChangeLogResponse.from_dict(response.json())

        return response_200

    response_default = ChangeLogListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ChangeLogListResponseDefault, ChangeLogResponse]]:
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
    change_type: Union[Unset, ChangeLogListChangeType] = UNSET,
    child_type: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    primary_id: Union[Unset, UUID] = UNSET,
    primary_type: Union[Unset, str] = UNSET,
) -> Response[Union[ChangeLogListResponseDefault, ChangeLogResponse]]:
    """Get a list of changes

     Return a list of available changes

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        change_type (Union[Unset, ChangeLogListChangeType]):  Example: delete.
        child_type (Union[Unset, str]):  Example: fixture_roster.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        primary_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        primary_type (Union[Unset, str]):  Example: fixtures.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChangeLogListResponseDefault, ChangeLogResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        change_type=change_type,
        child_type=child_type,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        primary_id=primary_id,
        primary_type=primary_type,
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
    change_type: Union[Unset, ChangeLogListChangeType] = UNSET,
    child_type: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    primary_id: Union[Unset, UUID] = UNSET,
    primary_type: Union[Unset, str] = UNSET,
) -> Optional[Union[ChangeLogListResponseDefault, ChangeLogResponse]]:
    """Get a list of changes

     Return a list of available changes

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        change_type (Union[Unset, ChangeLogListChangeType]):  Example: delete.
        child_type (Union[Unset, str]):  Example: fixture_roster.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        primary_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        primary_type (Union[Unset, str]):  Example: fixtures.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChangeLogListResponseDefault, ChangeLogResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        change_type=change_type,
        child_type=child_type,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        primary_id=primary_id,
        primary_type=primary_type,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    change_type: Union[Unset, ChangeLogListChangeType] = UNSET,
    child_type: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    primary_id: Union[Unset, UUID] = UNSET,
    primary_type: Union[Unset, str] = UNSET,
) -> Response[Union[ChangeLogListResponseDefault, ChangeLogResponse]]:
    """Get a list of changes

     Return a list of available changes

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        change_type (Union[Unset, ChangeLogListChangeType]):  Example: delete.
        child_type (Union[Unset, str]):  Example: fixture_roster.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        primary_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        primary_type (Union[Unset, str]):  Example: fixtures.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChangeLogListResponseDefault, ChangeLogResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        change_type=change_type,
        child_type=child_type,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        primary_id=primary_id,
        primary_type=primary_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    change_type: Union[Unset, ChangeLogListChangeType] = UNSET,
    child_type: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    primary_id: Union[Unset, UUID] = UNSET,
    primary_type: Union[Unset, str] = UNSET,
) -> Optional[Union[ChangeLogListResponseDefault, ChangeLogResponse]]:
    """Get a list of changes

     Return a list of available changes

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        change_type (Union[Unset, ChangeLogListChangeType]):  Example: delete.
        child_type (Union[Unset, str]):  Example: fixture_roster.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        primary_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        primary_type (Union[Unset, str]):  Example: fixtures.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChangeLogListResponseDefault, ChangeLogResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            change_type=change_type,
            child_type=child_type,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            primary_id=primary_id,
            primary_type=primary_type,
        )
    ).parsed
