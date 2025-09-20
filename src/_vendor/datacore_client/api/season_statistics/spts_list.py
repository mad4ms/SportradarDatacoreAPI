import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.season_person_total_statistics_response import SeasonPersonTotalStatisticsResponse
from ...models.spts_list_fixture_type import SptsListFixtureType
from ...models.spts_list_home_away import SptsListHomeAway
from ...models.spts_list_response_default import SptsListResponseDefault
from ...models.spts_list_win_loss import SptsListWinLoss
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SptsListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SptsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SptsListWinLoss] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_from_time_local: Union[Unset, str] = UNSET
    if not isinstance(from_time_local, Unset):
        json_from_time_local = from_time_local.isoformat()
    params["fromTimeLocal"] = json_from_time_local

    json_from_time_utc: Union[Unset, str] = UNSET
    if not isinstance(from_time_utc, Unset):
        json_from_time_utc = from_time_utc.isoformat()
    params["fromTimeUTC"] = json_from_time_utc

    params["hideNull"] = hide_null

    json_home_away: Union[Unset, str] = UNSET
    if not isinstance(home_away, Unset):
        json_home_away = home_away.value

    params["homeAway"] = json_home_away

    params["include"] = include

    params["isPlayer"] = is_player

    params["isTeamOfficial"] = is_team_official

    params["limit"] = limit

    params["offset"] = offset

    json_person_id: Union[Unset, str] = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    params["poolCode"] = pool_code

    params["roundCode"] = round_code

    params["roundNumber"] = round_number

    params["stageCode"] = stage_code

    params["starter"] = starter

    json_to_time_local: Union[Unset, str] = UNSET
    if not isinstance(to_time_local, Unset):
        json_to_time_local = to_time_local.isoformat()
    params["toTimeLocal"] = json_to_time_local

    json_to_time_utc: Union[Unset, str] = UNSET
    if not isinstance(to_time_utc, Unset):
        json_to_time_utc = to_time_utc.isoformat()
    params["toTimeUTC"] = json_to_time_utc

    json_win_loss: Union[Unset, str] = UNSET
    if not isinstance(win_loss, Unset):
        json_win_loss = win_loss.value

    params["winLoss"] = json_win_loss

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/person/in/seasons/{season_id}/combined",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]:
    if response.status_code == 200:
        response_200 = SeasonPersonTotalStatisticsResponse.from_dict(response.json())

        return response_200

    response_default = SptsListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]]:
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
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SptsListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SptsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SptsListWinLoss] = UNSET,
) -> Response[Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a person over multiple seasons.
        If a person plays for multiple teams in a season then their statistics are normally separated
        out by team. For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SptsListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SptsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SptsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        person_id=person_id,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        stage_code=stage_code,
        starter=starter,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        win_loss=win_loss,
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
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SptsListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SptsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SptsListWinLoss] = UNSET,
) -> Optional[Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a person over multiple seasons.
        If a person plays for multiple teams in a season then their statistics are normally separated
        out by team. For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SptsListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SptsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SptsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        person_id=person_id,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        stage_code=stage_code,
        starter=starter,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        win_loss=win_loss,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SptsListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SptsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SptsListWinLoss] = UNSET,
) -> Response[Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a person over multiple seasons.
        If a person plays for multiple teams in a season then their statistics are normally separated
        out by team. For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SptsListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SptsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SptsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        from_time_local=from_time_local,
        from_time_utc=from_time_utc,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        person_id=person_id,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        stage_code=stage_code,
        starter=starter,
        to_time_local=to_time_local,
        to_time_utc=to_time_utc,
        win_loss=win_loss,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SptsListFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SptsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SptsListWinLoss] = UNSET,
) -> Optional[Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a person over multiple seasons.
        If a person plays for multiple teams in a season then their statistics are normally separated
        out by team. For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SptsListFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SptsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SptsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonPersonTotalStatisticsResponse, SptsListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            entity_id=entity_id,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            from_time_local=from_time_local,
            from_time_utc=from_time_utc,
            hide_null=hide_null,
            home_away=home_away,
            include=include,
            is_player=is_player,
            is_team_official=is_team_official,
            limit=limit,
            offset=offset,
            person_id=person_id,
            pool_code=pool_code,
            round_code=round_code,
            round_number=round_number,
            stage_code=stage_code,
            starter=starter,
            to_time_local=to_time_local,
            to_time_utc=to_time_utc,
            win_loss=win_loss,
        )
    ).parsed
