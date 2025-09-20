import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.organization_list_region_type import OrganizationListRegionType
from ...models.organization_list_response_default import OrganizationListResponseDefault
from ...models.organizations_response import OrganizationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    region_type: Union[Unset, OrganizationListRegionType] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    params["countryCode"] = country_code

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_region_type: Union[Unset, str] = UNSET
    if not isinstance(region_type, Unset):
        json_region_type = region_type.value

    params["regionType"] = json_region_type

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/handball/organizations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[OrganizationListResponseDefault, OrganizationsResponse]:
    if response.status_code == 200:
        response_200 = OrganizationsResponse.from_dict(response.json())

        return response_200

    response_default = OrganizationListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[OrganizationListResponseDefault, OrganizationsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    region_type: Union[Unset, OrganizationListRegionType] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[OrganizationListResponseDefault, OrganizationsResponse]]:
    """Get a list of organizations

     Return a list of available organizations

    Args:
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        country_code (Union[Unset, str]):  Example: USA.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        region_type (Union[Unset, OrganizationListRegionType]):  Example: STATE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganizationListResponseDefault, OrganizationsResponse]]
    """

    kwargs = _get_kwargs(
        added=added,
        country_code=country_code,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        region_type=region_type,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    region_type: Union[Unset, OrganizationListRegionType] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[OrganizationListResponseDefault, OrganizationsResponse]]:
    """Get a list of organizations

     Return a list of available organizations

    Args:
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        country_code (Union[Unset, str]):  Example: USA.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        region_type (Union[Unset, OrganizationListRegionType]):  Example: STATE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganizationListResponseDefault, OrganizationsResponse]
    """

    return sync_detailed(
        client=client,
        added=added,
        country_code=country_code,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        region_type=region_type,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    region_type: Union[Unset, OrganizationListRegionType] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[OrganizationListResponseDefault, OrganizationsResponse]]:
    """Get a list of organizations

     Return a list of available organizations

    Args:
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        country_code (Union[Unset, str]):  Example: USA.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        region_type (Union[Unset, OrganizationListRegionType]):  Example: STATE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[OrganizationListResponseDefault, OrganizationsResponse]]
    """

    kwargs = _get_kwargs(
        added=added,
        country_code=country_code,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        region_type=region_type,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    country_code: Union[Unset, str] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    region_type: Union[Unset, OrganizationListRegionType] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[OrganizationListResponseDefault, OrganizationsResponse]]:
    """Get a list of organizations

     Return a list of available organizations

    Args:
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        country_code (Union[Unset, str]):  Example: USA.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        region_type (Union[Unset, OrganizationListRegionType]):  Example: STATE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[OrganizationListResponseDefault, OrganizationsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            added=added,
            country_code=country_code,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            region_type=region_type,
            updated=updated,
        )
    ).parsed
