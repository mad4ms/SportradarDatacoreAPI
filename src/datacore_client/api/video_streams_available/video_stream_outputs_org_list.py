import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.video_stream_outputs_org_list_content import VideoStreamOutputsOrgListContent
from ...models.video_stream_outputs_org_list_feed_type import VideoStreamOutputsOrgListFeedType
from ...models.video_stream_outputs_org_list_response_default import VideoStreamOutputsOrgListResponseDefault
from ...models.video_stream_outputs_org_list_video_stream_outputs_response import (
    VideoStreamOutputsOrgListVideoStreamOutputsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    content: Union[Unset, VideoStreamOutputsOrgListContent] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamOutputsOrgListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    master_venue_id: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_competition_id: Union[Unset, str] = UNSET
    if not isinstance(competition_id, Unset):
        json_competition_id = str(competition_id)
    params["competitionId"] = json_competition_id

    json_content: Union[Unset, str] = UNSET
    if not isinstance(content, Unset):
        json_content = content.value

    params["content"] = json_content

    params["external"] = external

    json_feed_type: Union[Unset, str] = UNSET
    if not isinstance(feed_type, Unset):
        json_feed_type = feed_type.value

    params["feedType"] = json_feed_type

    params["fields"] = fields

    json_from_time_utc: Union[Unset, str] = UNSET
    if not isinstance(from_time_utc, Unset):
        json_from_time_utc = from_time_utc.isoformat()
    params["fromTimeUTC"] = json_from_time_utc

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["locale"] = locale

    json_master_venue_id: Union[Unset, str] = UNSET
    if not isinstance(master_venue_id, Unset):
        json_master_venue_id = str(master_venue_id)
    params["masterVenueId"] = json_master_venue_id

    params["offset"] = offset

    params["provider"] = provider

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    params["sourceNumber"] = source_number

    json_to_time_utc: Union[Unset, str] = UNSET
    if not isinstance(to_time_utc, Unset):
        json_to_time_utc = to_time_utc.isoformat()
    params["toTimeUTC"] = json_to_time_utc

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    json_venue_id: Union[Unset, str] = UNSET
    if not isinstance(venue_id, Unset):
        json_venue_id = str(venue_id)
    params["venueId"] = json_venue_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/video/streams/available",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]:
    if response.status_code == 200:
        response_200 = VideoStreamOutputsOrgListVideoStreamOutputsResponse.from_dict(response.json())

        return response_200

    response_default = VideoStreamOutputsOrgListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]]:
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
    competition_id: Union[Unset, UUID] = UNSET,
    content: Union[Unset, VideoStreamOutputsOrgListContent] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamOutputsOrgListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    master_venue_id: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]]:
    """List available video streams for an organization

     Display the list of video streams for an organization. Streams for completed matches and those older
    than 12 hours, will not be displayed.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        content (Union[Unset, VideoStreamOutputsOrgListContent]):  Example: CLEAN.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamOutputsOrgListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        master_venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source_number (Union[Unset, int]):  Example: 1.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        competition_id=competition_id,
        content=content,
        external=external,
        feed_type=feed_type,
        fields=fields,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        locale=locale,
        master_venue_id=master_venue_id,
        offset=offset,
        provider=provider,
        season_id=season_id,
        source_number=source_number,
        to_time_utc=to_time_utc,
        updated=updated,
        venue_id=venue_id,
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
    competition_id: Union[Unset, UUID] = UNSET,
    content: Union[Unset, VideoStreamOutputsOrgListContent] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamOutputsOrgListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    master_venue_id: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]]:
    """List available video streams for an organization

     Display the list of video streams for an organization. Streams for completed matches and those older
    than 12 hours, will not be displayed.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        content (Union[Unset, VideoStreamOutputsOrgListContent]):  Example: CLEAN.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamOutputsOrgListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        master_venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source_number (Union[Unset, int]):  Example: 1.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        competition_id=competition_id,
        content=content,
        external=external,
        feed_type=feed_type,
        fields=fields,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        locale=locale,
        master_venue_id=master_venue_id,
        offset=offset,
        provider=provider,
        season_id=season_id,
        source_number=source_number,
        to_time_utc=to_time_utc,
        updated=updated,
        venue_id=venue_id,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    content: Union[Unset, VideoStreamOutputsOrgListContent] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamOutputsOrgListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    master_venue_id: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Response[Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]]:
    """List available video streams for an organization

     Display the list of video streams for an organization. Streams for completed matches and those older
    than 12 hours, will not be displayed.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        content (Union[Unset, VideoStreamOutputsOrgListContent]):  Example: CLEAN.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamOutputsOrgListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        master_venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source_number (Union[Unset, int]):  Example: 1.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        competition_id=competition_id,
        content=content,
        external=external,
        feed_type=feed_type,
        fields=fields,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        locale=locale,
        master_venue_id=master_venue_id,
        offset=offset,
        provider=provider,
        season_id=season_id,
        source_number=source_number,
        to_time_utc=to_time_utc,
        updated=updated,
        venue_id=venue_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    content: Union[Unset, VideoStreamOutputsOrgListContent] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamOutputsOrgListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    master_venue_id: Union[Unset, UUID] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    venue_id: Union[Unset, UUID] = UNSET,
) -> Optional[Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]]:
    """List available video streams for an organization

     Display the list of video streams for an organization. Streams for completed matches and those older
    than 12 hours, will not be displayed.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        content (Union[Unset, VideoStreamOutputsOrgListContent]):  Example: CLEAN.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamOutputsOrgListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        master_venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        source_number (Union[Unset, int]):  Example: 1.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        venue_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VideoStreamOutputsOrgListResponseDefault, VideoStreamOutputsOrgListVideoStreamOutputsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            competition_id=competition_id,
            content=content,
            external=external,
            feed_type=feed_type,
            fields=fields,
            from_time_utc=from_time_utc,
            hide_null=hide_null,
            include=include,
            limit=limit,
            locale=locale,
            master_venue_id=master_venue_id,
            offset=offset,
            provider=provider,
            season_id=season_id,
            source_number=source_number,
            to_time_utc=to_time_utc,
            updated=updated,
            venue_id=venue_id,
        )
    ).parsed
