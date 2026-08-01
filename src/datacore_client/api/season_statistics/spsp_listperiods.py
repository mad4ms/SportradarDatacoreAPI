import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.spsp_listperiods_fixture_type import SpspListperiodsFixtureType
from ...models.spsp_listperiods_home_away import SpspListperiodsHomeAway
from ...models.spsp_listperiods_period_id import SpspListperiodsPeriodId
from ...models.spsp_listperiods_response_default import SpspListperiodsResponseDefault
from ...models.spsp_listperiods_win_loss import SpspListperiodsWinLoss
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SpspListperiodsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SpspListperiodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, SpspListperiodsPeriodId] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SpspListperiodsWinLoss] = UNSET,
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

    json_period_id: Union[Unset, int] = UNSET
    if not isinstance(period_id, Unset):
        json_period_id = period_id.value

    params["periodId"] = json_period_id

    json_person_id: Union[Unset, str] = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    params["poolCode"] = pool_code

    params["roundCode"] = round_code

    params["roundNumber"] = round_number

    params["section"] = section

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
        "url": f"/handball/o/{organization_id}/statistics/for/person/in/seasons/{season_id}/periods",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> SpspListperiodsResponseDefault:
    response_default = SpspListperiodsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SpspListperiodsResponseDefault]:
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
    fixture_type: Union[Unset, SpspListperiodsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SpspListperiodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, SpspListperiodsPeriodId] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SpspListperiodsWinLoss] = UNSET,
) -> Response[SpspListperiodsResponseDefault]:
    """Person season statistics by period

     Return a list of person statistics for a season broken down and filterable by period.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpspListperiodsFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SpspListperiodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, SpspListperiodsPeriodId]):
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        section (Union[Unset, str]):
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SpspListperiodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SpspListperiodsResponseDefault]
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
        period_id=period_id,
        person_id=person_id,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        section=section,
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
    fixture_type: Union[Unset, SpspListperiodsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SpspListperiodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, SpspListperiodsPeriodId] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SpspListperiodsWinLoss] = UNSET,
) -> Optional[SpspListperiodsResponseDefault]:
    """Person season statistics by period

     Return a list of person statistics for a season broken down and filterable by period.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpspListperiodsFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SpspListperiodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, SpspListperiodsPeriodId]):
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        section (Union[Unset, str]):
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SpspListperiodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SpspListperiodsResponseDefault
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
        period_id=period_id,
        person_id=person_id,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        section=section,
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
    fixture_type: Union[Unset, SpspListperiodsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SpspListperiodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, SpspListperiodsPeriodId] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SpspListperiodsWinLoss] = UNSET,
) -> Response[SpspListperiodsResponseDefault]:
    """Person season statistics by period

     Return a list of person statistics for a season broken down and filterable by period.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpspListperiodsFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SpspListperiodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, SpspListperiodsPeriodId]):
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        section (Union[Unset, str]):
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SpspListperiodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SpspListperiodsResponseDefault]
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
        period_id=period_id,
        person_id=person_id,
        pool_code=pool_code,
        round_code=round_code,
        round_number=round_number,
        section=section,
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
    fixture_type: Union[Unset, SpspListperiodsFixtureType] = UNSET,
    from_time_local: Union[Unset, datetime.datetime] = UNSET,
    from_time_utc: Union[Unset, datetime.datetime] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SpspListperiodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, SpspListperiodsPeriodId] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    pool_code: Union[Unset, str] = UNSET,
    round_code: Union[Unset, str] = UNSET,
    round_number: Union[Unset, str] = UNSET,
    section: Union[Unset, str] = UNSET,
    stage_code: Union[Unset, str] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    to_time_local: Union[Unset, datetime.datetime] = UNSET,
    to_time_utc: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, SpspListperiodsWinLoss] = UNSET,
) -> Optional[SpspListperiodsResponseDefault]:
    """Person season statistics by period

     Return a list of person statistics for a season broken down and filterable by period.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpspListperiodsFixtureType]):  Example: REGULAR.
        from_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        from_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SpspListperiodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, SpspListperiodsPeriodId]):
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        pool_code (Union[Unset, str]):  Example: P1.
        round_code (Union[Unset, str]):  Example: RN1.
        round_number (Union[Unset, str]):  Example: 1.
        section (Union[Unset, str]):
        stage_code (Union[Unset, str]):  Example: ST1.
        starter (Union[Unset, bool]):
        to_time_local (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        to_time_utc (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        win_loss (Union[Unset, SpspListperiodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SpspListperiodsResponseDefault
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
            period_id=period_id,
            person_id=person_id,
            pool_code=pool_code,
            round_code=round_code,
            round_number=round_number,
            section=section,
            stage_code=stage_code,
            starter=starter,
            to_time_local=to_time_local,
            to_time_utc=to_time_utc,
            win_loss=win_loss,
        )
    ).parsed
