from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.video_subscription_delete_response_default import (
    VideoSubscriptionDeleteResponseDefault,
)
from ...models.video_subscription_delete_video_subscriptions_response import (
    VideoSubscriptionDeleteVideoSubscriptionsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    subscription_id: UUID,
    *,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["external"] = external

    params["fields"] = fields

    params["forceDelete"] = force_delete

    params["hideNull"] = hide_null

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/handball/o/{organization_id}/video/streams/subscriptions/{subscription_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    VideoSubscriptionDeleteResponseDefault,
    VideoSubscriptionDeleteVideoSubscriptionsResponse,
]:
    if response.status_code == 200:
        response_200 = VideoSubscriptionDeleteVideoSubscriptionsResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = VideoSubscriptionDeleteResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        VideoSubscriptionDeleteResponseDefault,
        VideoSubscriptionDeleteVideoSubscriptionsResponse,
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
    subscription_id: UUID,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        VideoSubscriptionDeleteResponseDefault,
        VideoSubscriptionDeleteVideoSubscriptionsResponse,
    ]
]:
    """Delete a video stream subscription

     Delete an existing subscription

    Args:
        organization_id (str):  Example: b1a23.
        subscription_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VideoSubscriptionDeleteResponseDefault, VideoSubscriptionDeleteVideoSubscriptionsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        subscription_id=subscription_id,
        external=external,
        fields=fields,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    subscription_id: UUID,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        VideoSubscriptionDeleteResponseDefault,
        VideoSubscriptionDeleteVideoSubscriptionsResponse,
    ]
]:
    """Delete a video stream subscription

     Delete an existing subscription

    Args:
        organization_id (str):  Example: b1a23.
        subscription_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VideoSubscriptionDeleteResponseDefault, VideoSubscriptionDeleteVideoSubscriptionsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        subscription_id=subscription_id,
        client=client,
        external=external,
        fields=fields,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    subscription_id: UUID,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        VideoSubscriptionDeleteResponseDefault,
        VideoSubscriptionDeleteVideoSubscriptionsResponse,
    ]
]:
    """Delete a video stream subscription

     Delete an existing subscription

    Args:
        organization_id (str):  Example: b1a23.
        subscription_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VideoSubscriptionDeleteResponseDefault, VideoSubscriptionDeleteVideoSubscriptionsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        subscription_id=subscription_id,
        external=external,
        fields=fields,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    subscription_id: UUID,
    *,
    client: AuthenticatedClient,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        VideoSubscriptionDeleteResponseDefault,
        VideoSubscriptionDeleteVideoSubscriptionsResponse,
    ]
]:
    """Delete a video stream subscription

     Delete an existing subscription

    Args:
        organization_id (str):  Example: b1a23.
        subscription_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VideoSubscriptionDeleteResponseDefault, VideoSubscriptionDeleteVideoSubscriptionsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            subscription_id=subscription_id,
            client=client,
            external=external,
            fields=fields,
            force_delete=force_delete,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
