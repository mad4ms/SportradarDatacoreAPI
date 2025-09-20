import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.standing_live_list_fixture_type import StandingLiveListFixtureType
from ...models.standing_live_list_grouping_base import StandingLiveListGroupingBase
from ...models.standing_live_list_grouping_conference_division import StandingLiveListGroupingConferenceDivision
from ...models.standing_live_list_grouping_stage_pool import StandingLiveListGroupingStagePool
from ...models.standing_live_list_response_default import StandingLiveListResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    conference_id: Union[Unset, UUID] = UNSET,
    division_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, StandingLiveListFixtureType] = UNSET,
    grouping_base: Union[Unset, StandingLiveListGroupingBase] = UNSET,
    grouping_conference_division: Union[Unset, StandingLiveListGroupingConferenceDivision] = UNSET,
    grouping_stage_pool: Union[Unset, StandingLiveListGroupingStagePool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    in_progress: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    latest: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    standing_configuration_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_conference_id: Union[Unset, str] = UNSET
    if not isinstance(conference_id, Unset):
        json_conference_id = str(conference_id)
    params["conferenceId"] = json_conference_id

    json_division_id: Union[Unset, str] = UNSET
    if not isinstance(division_id, Unset):
        json_division_id = str(division_id)
    params["divisionId"] = json_division_id

    json_entity_id: Union[Unset, str] = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = str(entity_id)
    params["entityId"] = json_entity_id

    params["external"] = external

    params["fields"] = fields

    json_fixture_type: Union[Unset, str] = UNSET
    if not isinstance(fixture_type, Unset):
        json_fixture_type = fixture_type.value

    params["fixtureType"] = json_fixture_type

    json_grouping_base: Union[Unset, str] = UNSET
    if not isinstance(grouping_base, Unset):
        json_grouping_base = grouping_base.value

    params["groupingBase"] = json_grouping_base

    json_grouping_conference_division: Union[Unset, str] = UNSET
    if not isinstance(grouping_conference_division, Unset):
        json_grouping_conference_division = grouping_conference_division.value

    params["groupingConferenceDivision"] = json_grouping_conference_division

    json_grouping_stage_pool: Union[Unset, str] = UNSET
    if not isinstance(grouping_stage_pool, Unset):
        json_grouping_stage_pool = grouping_stage_pool.value

    params["groupingStagePool"] = json_grouping_stage_pool

    params["hideNull"] = hide_null

    params["inProgress"] = in_progress

    params["include"] = include

    params["latest"] = latest

    params["limit"] = limit

    params["offset"] = offset

    params["poolCode"] = pool_code

    params["roundCode"] = round_code

    params["roundNumber"] = round_number

    params["sortBy"] = sort_by

    params["stageCode"] = stage_code

    json_standing_configuration_id: Union[Unset, str] = UNSET
    if not isinstance(standing_configuration_id, Unset):
        json_standing_configuration_id = str(standing_configuration_id)
    params["standingConfigurationId"] = json_standing_configuration_id

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/seasons/{season_id}/standings/live",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> StandingLiveListResponseDefault:
    response_default = StandingLiveListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[StandingLiveListResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    conference_id: Union[Unset, UUID] = UNSET,
    division_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, StandingLiveListFixtureType] = UNSET,
    grouping_base: Union[Unset, StandingLiveListGroupingBase] = UNSET,
    grouping_conference_division: Union[Unset, StandingLiveListGroupingConferenceDivision] = UNSET,
    grouping_stage_pool: Union[Unset, StandingLiveListGroupingStagePool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    in_progress: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    latest: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    standing_configuration_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[StandingLiveListResponseDefault]:
    """Get a list of live standings

     Return a list of live standings for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        conference_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, StandingLiveListFixtureType]):  Example: REGULAR.
        grouping_base (Union[Unset, StandingLiveListGroupingBase]):  Example: OVERALL.
        grouping_conference_division (Union[Unset, StandingLiveListGroupingConferenceDivision]):
            Example: OVERALL.
        grouping_stage_pool (Union[Unset, StandingLiveListGroupingStagePool]):  Example: OVERALL.
        hide_null (Union[Unset, bool]):  Example: True.
        in_progress (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        latest (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: conferenceId,divisionId,-position.
        stage_code (Union[Unset, str]):  Example: ST1.
        standing_configuration_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandingLiveListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        conference_id=conference_id,
        division_id=division_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        grouping_base=grouping_base,
        grouping_conference_division=grouping_conference_division,
        grouping_stage_pool=grouping_stage_pool,
        hide_null=hide_null,
        in_progress=in_progress,
        include=include,
        latest=latest,
        limit=limit,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        sort_by=sort_by,
        stage_code=stage_code,
        standing_configuration_id=standing_configuration_id,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    conference_id: Union[Unset, UUID] = UNSET,
    division_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, StandingLiveListFixtureType] = UNSET,
    grouping_base: Union[Unset, StandingLiveListGroupingBase] = UNSET,
    grouping_conference_division: Union[Unset, StandingLiveListGroupingConferenceDivision] = UNSET,
    grouping_stage_pool: Union[Unset, StandingLiveListGroupingStagePool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    in_progress: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    latest: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    standing_configuration_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[StandingLiveListResponseDefault]:
    """Get a list of live standings

     Return a list of live standings for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        conference_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, StandingLiveListFixtureType]):  Example: REGULAR.
        grouping_base (Union[Unset, StandingLiveListGroupingBase]):  Example: OVERALL.
        grouping_conference_division (Union[Unset, StandingLiveListGroupingConferenceDivision]):
            Example: OVERALL.
        grouping_stage_pool (Union[Unset, StandingLiveListGroupingStagePool]):  Example: OVERALL.
        hide_null (Union[Unset, bool]):  Example: True.
        in_progress (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        latest (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: conferenceId,divisionId,-position.
        stage_code (Union[Unset, str]):  Example: ST1.
        standing_configuration_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandingLiveListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        added=added,
        conference_id=conference_id,
        division_id=division_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        grouping_base=grouping_base,
        grouping_conference_division=grouping_conference_division,
        grouping_stage_pool=grouping_stage_pool,
        hide_null=hide_null,
        in_progress=in_progress,
        include=include,
        latest=latest,
        limit=limit,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        sort_by=sort_by,
        stage_code=stage_code,
        standing_configuration_id=standing_configuration_id,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    conference_id: Union[Unset, UUID] = UNSET,
    division_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, StandingLiveListFixtureType] = UNSET,
    grouping_base: Union[Unset, StandingLiveListGroupingBase] = UNSET,
    grouping_conference_division: Union[Unset, StandingLiveListGroupingConferenceDivision] = UNSET,
    grouping_stage_pool: Union[Unset, StandingLiveListGroupingStagePool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    in_progress: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    latest: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    standing_configuration_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[StandingLiveListResponseDefault]:
    """Get a list of live standings

     Return a list of live standings for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        conference_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, StandingLiveListFixtureType]):  Example: REGULAR.
        grouping_base (Union[Unset, StandingLiveListGroupingBase]):  Example: OVERALL.
        grouping_conference_division (Union[Unset, StandingLiveListGroupingConferenceDivision]):
            Example: OVERALL.
        grouping_stage_pool (Union[Unset, StandingLiveListGroupingStagePool]):  Example: OVERALL.
        hide_null (Union[Unset, bool]):  Example: True.
        in_progress (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        latest (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: conferenceId,divisionId,-position.
        stage_code (Union[Unset, str]):  Example: ST1.
        standing_configuration_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StandingLiveListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        conference_id=conference_id,
        division_id=division_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        grouping_base=grouping_base,
        grouping_conference_division=grouping_conference_division,
        grouping_stage_pool=grouping_stage_pool,
        hide_null=hide_null,
        in_progress=in_progress,
        include=include,
        latest=latest,
        limit=limit,
        offset=offset,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        sort_by=sort_by,
        stage_code=stage_code,
        standing_configuration_id=standing_configuration_id,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    conference_id: Union[Unset, UUID] = UNSET,
    division_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, StandingLiveListFixtureType] = UNSET,
    grouping_base: Union[Unset, StandingLiveListGroupingBase] = UNSET,
    grouping_conference_division: Union[Unset, StandingLiveListGroupingConferenceDivision] = UNSET,
    grouping_stage_pool: Union[Unset, StandingLiveListGroupingStagePool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    in_progress: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    latest: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    standing_configuration_id: Union[Unset, UUID] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[StandingLiveListResponseDefault]:
    """Get a list of live standings

     Return a list of live standings for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        conference_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        division_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, StandingLiveListFixtureType]):  Example: REGULAR.
        grouping_base (Union[Unset, StandingLiveListGroupingBase]):  Example: OVERALL.
        grouping_conference_division (Union[Unset, StandingLiveListGroupingConferenceDivision]):
            Example: OVERALL.
        grouping_stage_pool (Union[Unset, StandingLiveListGroupingStagePool]):  Example: OVERALL.
        hide_null (Union[Unset, bool]):  Example: True.
        in_progress (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        latest (Union[Unset, bool]):  Example: True.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        sort_by (Union[Unset, str]):  Example: conferenceId,divisionId,-position.
        stage_code (Union[Unset, str]):  Example: ST1.
        standing_configuration_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StandingLiveListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            added=added,
            conference_id=conference_id,
            division_id=division_id,
            entity_id=entity_id,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            grouping_base=grouping_base,
            grouping_conference_division=grouping_conference_division,
            grouping_stage_pool=grouping_stage_pool,
            hide_null=hide_null,
            in_progress=in_progress,
            include=include,
            latest=latest,
            limit=limit,
            offset=offset,
            pool_code=pool_code,
            round_code=round_code,
            round_number=round_number,
            sort_by=sort_by,
            stage_code=stage_code,
            standing_configuration_id=standing_configuration_id,
            updated=updated,
        )
    ).parsed
