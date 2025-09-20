import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.video_stream_inputs_fixture_list_feed_type import VideoStreamInputsFixtureListFeedType
from ...models.video_stream_inputs_fixture_list_response_default import VideoStreamInputsFixtureListResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamInputsFixtureListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_input_id: Union[Unset, UUID] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    params["external"] = external

    json_feed_type: Union[Unset, str] = UNSET
    if not isinstance(feed_type, Unset):
        json_feed_type = feed_type.value

    params["feedType"] = json_feed_type

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["locale"] = locale

    params["offset"] = offset

    params["provider"] = provider

    params["sourceNumber"] = source_number

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    json_video_input_id: Union[Unset, str] = UNSET
    if not isinstance(video_input_id, Unset):
        json_video_input_id = str(video_input_id)
    params["videoInputId"] = json_video_input_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/fixtures/{fixture_id}/video/streams/inputs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> VideoStreamInputsFixtureListResponseDefault:
    response_default = VideoStreamInputsFixtureListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[VideoStreamInputsFixtureListResponseDefault]:
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
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamInputsFixtureListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_input_id: Union[Unset, UUID] = UNSET,
) -> Response[VideoStreamInputsFixtureListResponseDefault]:
    """List available video inputs for a match

     Display the list of video inputs for a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamInputsFixtureListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        source_number (Union[Unset, int]):  Example: 1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_input_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoStreamInputsFixtureListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        external=external,
        feed_type=feed_type,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        locale=locale,
        offset=offset,
        provider=provider,
        source_number=source_number,
        updated=updated,
        video_input_id=video_input_id,
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
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamInputsFixtureListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_input_id: Union[Unset, UUID] = UNSET,
) -> Optional[VideoStreamInputsFixtureListResponseDefault]:
    """List available video inputs for a match

     Display the list of video inputs for a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamInputsFixtureListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        source_number (Union[Unset, int]):  Example: 1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_input_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoStreamInputsFixtureListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_id=fixture_id,
        client=client,
        added=added,
        external=external,
        feed_type=feed_type,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        locale=locale,
        offset=offset,
        provider=provider,
        source_number=source_number,
        updated=updated,
        video_input_id=video_input_id,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamInputsFixtureListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_input_id: Union[Unset, UUID] = UNSET,
) -> Response[VideoStreamInputsFixtureListResponseDefault]:
    """List available video inputs for a match

     Display the list of video inputs for a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamInputsFixtureListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        source_number (Union[Unset, int]):  Example: 1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_input_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoStreamInputsFixtureListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        external=external,
        feed_type=feed_type,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        locale=locale,
        offset=offset,
        provider=provider,
        source_number=source_number,
        updated=updated,
        video_input_id=video_input_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: AuthenticatedClient,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    feed_type: Union[Unset, VideoStreamInputsFixtureListFeedType] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    locale: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    provider: Union[Unset, str] = UNSET,
    source_number: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_input_id: Union[Unset, UUID] = UNSET,
) -> Optional[VideoStreamInputsFixtureListResponseDefault]:
    """List available video inputs for a match

     Display the list of video inputs for a match

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        feed_type (Union[Unset, VideoStreamInputsFixtureListFeedType]):  Example: PRIMARY.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        locale (Union[Unset, str]):  Example: fr_FR.
        offset (Union[Unset, int]):  Example: 10.
        provider (Union[Unset, str]):  Example: Test Provider.
        source_number (Union[Unset, int]):  Example: 1.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_input_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoStreamInputsFixtureListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_id=fixture_id,
            client=client,
            added=added,
            external=external,
            feed_type=feed_type,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            locale=locale,
            offset=offset,
            provider=provider,
            source_number=source_number,
            updated=updated,
            video_input_id=video_input_id,
        )
    ).parsed
