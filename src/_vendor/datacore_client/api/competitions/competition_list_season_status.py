import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.competition_list_season_status_age_group import CompetitionListSeasonStatusAgeGroup
from ...models.competition_list_season_status_response_default import CompetitionListSeasonStatusResponseDefault
from ...models.competition_list_season_status_season_status import CompetitionListSeasonStatusSeasonStatus
from ...models.competition_list_season_status_season_video_production import (
    CompetitionListSeasonStatusSeasonVideoProduction,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, CompetitionListSeasonStatusAgeGroup] = UNSET,
    comp_season_updated: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_status: Union[Unset, CompetitionListSeasonStatusSeasonStatus] = UNSET,
    season_updated: Union[Unset, datetime.datetime] = UNSET,
    season_video_production: Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_age_group: Union[Unset, str] = UNSET
    if not isinstance(age_group, Unset):
        json_age_group = age_group.value

    params["ageGroup"] = json_age_group

    json_comp_season_updated: Union[Unset, str] = UNSET
    if not isinstance(comp_season_updated, Unset):
        json_comp_season_updated = comp_season_updated.isoformat()
    params["compSeasonUpdated"] = json_comp_season_updated

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_season_status: Union[Unset, str] = UNSET
    if not isinstance(season_status, Unset):
        json_season_status = season_status.value

    params["seasonStatus"] = json_season_status

    json_season_updated: Union[Unset, str] = UNSET
    if not isinstance(season_updated, Unset):
        json_season_updated = season_updated.isoformat()
    params["seasonUpdated"] = json_season_updated

    json_season_video_production: Union[Unset, str] = UNSET
    if not isinstance(season_video_production, Unset):
        json_season_video_production = season_video_production.value

    params["seasonVideoProduction"] = json_season_video_production

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/competitions/seasonStatus",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> CompetitionListSeasonStatusResponseDefault:
    response_default = CompetitionListSeasonStatusResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CompetitionListSeasonStatusResponseDefault]:
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
    age_group: Union[Unset, CompetitionListSeasonStatusAgeGroup] = UNSET,
    comp_season_updated: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_status: Union[Unset, CompetitionListSeasonStatusSeasonStatus] = UNSET,
    season_updated: Union[Unset, datetime.datetime] = UNSET,
    season_video_production: Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[CompetitionListSeasonStatusResponseDefault]:
    """Get a list of competitions that have active seasons

     Return a list of available competitions that have active seasons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, CompetitionListSeasonStatusAgeGroup]):  Example: SENIOR.
        comp_season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_status (Union[Unset, CompetitionListSeasonStatusSeasonStatus]):  Example: ACTIVE.
        season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        season_video_production (Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction]):
            Example: NONE,AUTOMATED.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompetitionListSeasonStatusResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        age_group=age_group,
        comp_season_updated=comp_season_updated,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_status=season_status,
        season_updated=season_updated,
        season_video_production=season_video_production,
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
    age_group: Union[Unset, CompetitionListSeasonStatusAgeGroup] = UNSET,
    comp_season_updated: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_status: Union[Unset, CompetitionListSeasonStatusSeasonStatus] = UNSET,
    season_updated: Union[Unset, datetime.datetime] = UNSET,
    season_video_production: Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[CompetitionListSeasonStatusResponseDefault]:
    """Get a list of competitions that have active seasons

     Return a list of available competitions that have active seasons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, CompetitionListSeasonStatusAgeGroup]):  Example: SENIOR.
        comp_season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_status (Union[Unset, CompetitionListSeasonStatusSeasonStatus]):  Example: ACTIVE.
        season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        season_video_production (Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction]):
            Example: NONE,AUTOMATED.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompetitionListSeasonStatusResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        age_group=age_group,
        comp_season_updated=comp_season_updated,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_status=season_status,
        season_updated=season_updated,
        season_video_production=season_video_production,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, CompetitionListSeasonStatusAgeGroup] = UNSET,
    comp_season_updated: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_status: Union[Unset, CompetitionListSeasonStatusSeasonStatus] = UNSET,
    season_updated: Union[Unset, datetime.datetime] = UNSET,
    season_video_production: Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[CompetitionListSeasonStatusResponseDefault]:
    """Get a list of competitions that have active seasons

     Return a list of available competitions that have active seasons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, CompetitionListSeasonStatusAgeGroup]):  Example: SENIOR.
        comp_season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_status (Union[Unset, CompetitionListSeasonStatusSeasonStatus]):  Example: ACTIVE.
        season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        season_video_production (Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction]):
            Example: NONE,AUTOMATED.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CompetitionListSeasonStatusResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        age_group=age_group,
        comp_season_updated=comp_season_updated,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_status=season_status,
        season_updated=season_updated,
        season_video_production=season_video_production,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, CompetitionListSeasonStatusAgeGroup] = UNSET,
    comp_season_updated: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_status: Union[Unset, CompetitionListSeasonStatusSeasonStatus] = UNSET,
    season_updated: Union[Unset, datetime.datetime] = UNSET,
    season_video_production: Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[CompetitionListSeasonStatusResponseDefault]:
    """Get a list of competitions that have active seasons

     Return a list of available competitions that have active seasons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, CompetitionListSeasonStatusAgeGroup]):  Example: SENIOR.
        comp_season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_status (Union[Unset, CompetitionListSeasonStatusSeasonStatus]):  Example: ACTIVE.
        season_updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        season_video_production (Union[Unset, CompetitionListSeasonStatusSeasonVideoProduction]):
            Example: NONE,AUTOMATED.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CompetitionListSeasonStatusResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            age_group=age_group,
            comp_season_updated=comp_season_updated,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            season_status=season_status,
            season_updated=season_updated,
            season_video_production=season_video_production,
            updated=updated,
        )
    ).parsed
