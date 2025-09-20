from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity_merge_merge_post_body import EntityMergeMergePostBody
from ...models.entity_merge_response_default import EntityMergeResponseDefault
from ...models.entity_merge_success_response import EntityMergeSuccessResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    from_entity_id: UUID,
    to_entity_id: UUID,
    *,
    body: EntityMergeMergePostBody,
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
        "url": f"/handball/o/{organization_id}/entities/merge/from/{from_entity_id}/to/{to_entity_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]:
    if response.status_code == 200:
        response_200 = EntityMergeSuccessResponse.from_dict(response.json())

        return response_200

    response_default = EntityMergeResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    from_entity_id: UUID,
    to_entity_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EntityMergeMergePostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]]:
    """Merge two team records

     Merge the records of two teams

    Args:
        organization_id (str):  Example: b1a23.
        from_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (EntityMergeMergePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        from_entity_id=from_entity_id,
        to_entity_id=to_entity_id,
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
    from_entity_id: UUID,
    to_entity_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EntityMergeMergePostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]]:
    """Merge two team records

     Merge the records of two teams

    Args:
        organization_id (str):  Example: b1a23.
        from_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (EntityMergeMergePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        from_entity_id=from_entity_id,
        to_entity_id=to_entity_id,
        client=client,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    from_entity_id: UUID,
    to_entity_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EntityMergeMergePostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]]:
    """Merge two team records

     Merge the records of two teams

    Args:
        organization_id (str):  Example: b1a23.
        from_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (EntityMergeMergePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        from_entity_id=from_entity_id,
        to_entity_id=to_entity_id,
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
    from_entity_id: UUID,
    to_entity_id: UUID,
    *,
    client: AuthenticatedClient,
    body: EntityMergeMergePostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]]:
    """Merge two team records

     Merge the records of two teams

    Args:
        organization_id (str):  Example: b1a23.
        from_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (EntityMergeMergePostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityMergeResponseDefault, EntityMergeSuccessResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            from_entity_id=from_entity_id,
            to_entity_id=to_entity_id,
            client=client,
            body=body,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
