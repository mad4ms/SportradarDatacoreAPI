import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.video_subscription_list_response_default import VideoSubscriptionListResponseDefault
from ...models.video_subscriptions_response import VideoSubscriptionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    only_upcoming: Union[Unset, bool] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    params["external"] = external

    params["fields"] = fields

    json_fixture_id: Union[Unset, str] = UNSET
    if not isinstance(fixture_id, Unset):
        json_fixture_id = str(fixture_id)
    params["fixtureId"] = json_fixture_id

    json_from_time_utc: Union[Unset, str] = UNSET
    if not isinstance(from_time_utc, Unset):
        json_from_time_utc = from_time_utc.isoformat()
    params["fromTimeUTC"] = json_from_time_utc

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    params["onlyUpcoming"] = only_upcoming

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    json_to_time_utc: Union[Unset, str] = UNSET
    if not isinstance(to_time_utc, Unset):
        json_to_time_utc = to_time_utc.isoformat()
    params["toTimeUTC"] = json_to_time_utc

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/video/streams/subscriptions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]:
    if response.status_code == 200:
        response_200 = VideoSubscriptionsResponse.from_dict(response.json())

        return response_200

    response_default = VideoSubscriptionListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]]:
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    only_upcoming: Union[Unset, bool] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]]:
    """List video stream subscriptions

     Display the list of video stream subscriptions for fixtures.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        only_upcoming (Union[Unset, bool]):  Example: True.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        external=external,
        fields=fields,
        fixture_id=fixture_id,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        only_upcoming=only_upcoming,
        season_id=season_id,
        to_time_utc=to_time_utc,
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    only_upcoming: Union[Unset, bool] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]]:
    """List video stream subscriptions

     Display the list of video stream subscriptions for fixtures.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        only_upcoming (Union[Unset, bool]):  Example: True.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        external=external,
        fields=fields,
        fixture_id=fixture_id,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        only_upcoming=only_upcoming,
        season_id=season_id,
        to_time_utc=to_time_utc,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    only_upcoming: Union[Unset, bool] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]]:
    """List video stream subscriptions

     Display the list of video stream subscriptions for fixtures.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        only_upcoming (Union[Unset, bool]):  Example: True.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        external=external,
        fields=fields,
        fixture_id=fixture_id,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        only_upcoming=only_upcoming,
        season_id=season_id,
        to_time_utc=to_time_utc,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    only_upcoming: Union[Unset, bool] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]]:
    """List video stream subscriptions

     Display the list of video stream subscriptions for fixtures.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        only_upcoming (Union[Unset, bool]):  Example: True.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VideoSubscriptionListResponseDefault, VideoSubscriptionsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            external=external,
            fields=fields,
            fixture_id=fixture_id,
            from_time_utc=from_time_utc,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            only_upcoming=only_upcoming,
            season_id=season_id,
            to_time_utc=to_time_utc,
            updated=updated,
        )
    ).parsed
