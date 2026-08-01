import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.head_to_head_list_fixtures_mulitple_competitions_fixture_type import (
    HeadToHeadListFixturesMulitpleCompetitionsFixtureType,
)
from ...models.head_to_head_list_fixtures_mulitple_competitions_head_to_head_entity_response import (
    HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse,
)
from ...models.head_to_head_list_fixtures_mulitple_competitions_response_default import (
    HeadToHeadListFixturesMulitpleCompetitionsResponseDefault,
)
from ...models.head_to_head_list_fixtures_mulitple_competitions_status import (
    HeadToHeadListFixturesMulitpleCompetitionsStatus,
)
from ...models.head_to_head_list_fixtures_mulitple_competitions_status_not import (
    HeadToHeadListFixturesMulitpleCompetitionsStatusNot,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    person_id_1: UUID,
    person_id_2: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_ids: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    status: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus] = UNSET,
    status_not: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_competition_ids: Union[Unset, str] = UNSET
    if not isinstance(competition_ids, Unset):
        json_competition_ids = str(competition_ids)
    params["competitionIds"] = json_competition_ids

    params["external"] = external

    params["fields"] = fields

    json_fixture_type: Union[Unset, str] = UNSET
    if not isinstance(fixture_type, Unset):
        json_fixture_type = fixture_type.value

    params["fixtureType"] = json_fixture_type

    json_from_time_local: Union[Unset, str] = UNSET
    if not isinstance(from_time_local, Unset):
        json_from_time_local = from_time_local.isoformat()
    params["fromTimeLocal"] = json_from_time_local

    json_from_time_utc: Union[Unset, str] = UNSET
    if not isinstance(from_time_utc, Unset):
        json_from_time_utc = from_time_utc.isoformat()
    params["fromTimeUTC"] = json_from_time_utc

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    json_season_ids: Union[Unset, str] = UNSET
    if not isinstance(season_ids, Unset):
        json_season_ids = str(season_ids)
    params["seasonIds"] = json_season_ids

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_status_not: Union[Unset, str] = UNSET
    if not isinstance(status_not, Unset):
        json_status_not = status_not.value

    params["statusNot"] = json_status_not

    json_to_time_local: Union[Unset, str] = UNSET
    if not isinstance(to_time_local, Unset):
        json_to_time_local = to_time_local.isoformat()
    params["toTimeLocal"] = json_to_time_local

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
        "url": f"/handball/o/{organization_id}/headToHead/fixtures/persons/{person_id_1}/{person_id_2}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse,
    HeadToHeadListFixturesMulitpleCompetitionsResponseDefault,
]:
    if response.status_code == 200:
        response_200 = HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse.from_dict(response.json())

        return response_200

    response_default = HeadToHeadListFixturesMulitpleCompetitionsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse,
        HeadToHeadListFixturesMulitpleCompetitionsResponseDefault,
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
    person_id_1: UUID,
    person_id_2: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_ids: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    status: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus] = UNSET,
    status_not: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse,
        HeadToHeadListFixturesMulitpleCompetitionsResponseDefault,
    ]
]:
    """Match History for head-to-head of two teams across multiple seasons or competitions

     Return the Matches for a two specific teams in multiple seasons or competitions.

    Args:
        organization_id (str):  Example: b1a23.
        person_id_1 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id_2 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType]):
            Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        status (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus]):  Example:
            SCHEDULED.
        status_not (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot]):  Example:
            SCHEDULED.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse, HeadToHeadListFixturesMulitpleCompetitionsResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        person_id_1=person_id_1,
        person_id_2=person_id_2,
        added=added,
        competition_ids=competition_ids,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_id=season_id,
        season_ids=season_ids,
        status=status,
        status_not=status_not,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    person_id_1: UUID,
    person_id_2: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_ids: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    status: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus] = UNSET,
    status_not: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse,
        HeadToHeadListFixturesMulitpleCompetitionsResponseDefault,
    ]
]:
    """Match History for head-to-head of two teams across multiple seasons or competitions

     Return the Matches for a two specific teams in multiple seasons or competitions.

    Args:
        organization_id (str):  Example: b1a23.
        person_id_1 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id_2 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType]):
            Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        status (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus]):  Example:
            SCHEDULED.
        status_not (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot]):  Example:
            SCHEDULED.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse, HeadToHeadListFixturesMulitpleCompetitionsResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        person_id_1=person_id_1,
        person_id_2=person_id_2,
        client=client,
        added=added,
        competition_ids=competition_ids,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_id=season_id,
        season_ids=season_ids,
        status=status,
        status_not=status_not,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    person_id_1: UUID,
    person_id_2: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_ids: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    status: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus] = UNSET,
    status_not: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse,
        HeadToHeadListFixturesMulitpleCompetitionsResponseDefault,
    ]
]:
    """Match History for head-to-head of two teams across multiple seasons or competitions

     Return the Matches for a two specific teams in multiple seasons or competitions.

    Args:
        organization_id (str):  Example: b1a23.
        person_id_1 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id_2 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType]):
            Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        status (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus]):  Example:
            SCHEDULED.
        status_not (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot]):  Example:
            SCHEDULED.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse, HeadToHeadListFixturesMulitpleCompetitionsResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        person_id_1=person_id_1,
        person_id_2=person_id_2,
        added=added,
        competition_ids=competition_ids,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        season_id=season_id,
        season_ids=season_ids,
        status=status,
        status_not=status_not,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    person_id_1: UUID,
    person_id_2: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_ids: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_ids: Union[Unset, UUID] = UNSET,
    status: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus] = UNSET,
    status_not: Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse,
        HeadToHeadListFixturesMulitpleCompetitionsResponseDefault,
    ]
]:
    """Match History for head-to-head of two teams across multiple seasons or competitions

     Return the Matches for a two specific teams in multiple seasons or competitions.

    Args:
        organization_id (str):  Example: b1a23.
        person_id_1 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_id_2 (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsFixtureType]):
            Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        status (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatus]):  Example:
            SCHEDULED.
        status_not (Union[Unset, HeadToHeadListFixturesMulitpleCompetitionsStatusNot]):  Example:
            SCHEDULED.
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HeadToHeadListFixturesMulitpleCompetitionsHeadToHeadEntityResponse, HeadToHeadListFixturesMulitpleCompetitionsResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            person_id_1=person_id_1,
            person_id_2=person_id_2,
            client=client,
            added=added,
            competition_ids=competition_ids,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            from_time_local=from_time_local,
            from_time_utc=from_time_utc,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            season_id=season_id,
            season_ids=season_ids,
            status=status,
            status_not=status_not,
            to_time_local=to_time_local,
            to_time_utc=to_time_utc,
            updated=updated,
        )
    ).parsed
