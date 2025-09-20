from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.sl_list_summary_fixture_type import SlListSummaryFixtureType
from ...models.sl_list_summary_home_away import SlListSummaryHomeAway
from ...models.sl_list_summary_leader_summary_response import SlListSummaryLeaderSummaryResponse
from ...models.sl_list_summary_response_default import SlListSummaryResponseDefault
from ...models.sl_list_summary_win_loss import SlListSummaryWinLoss
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SlListSummaryFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SlListSummaryHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    statistics: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, SlListSummaryWinLoss] = UNSET,
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

    params["starter"] = starter

    params["statistics"] = statistics

    json_win_loss: Union[Unset, str] = UNSET
    if not isinstance(win_loss, Unset):
        json_win_loss = win_loss.value

    params["winLoss"] = json_win_loss

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/leaders/in/seasons/{season_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]:
    if response.status_code == 200:
        response_200 = SlListSummaryLeaderSummaryResponse.from_dict(response.json())

        return response_200

    response_default = SlListSummaryResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]]:
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
    fixture_type: Union[Unset, SlListSummaryFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SlListSummaryHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    statistics: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, SlListSummaryWinLoss] = UNSET,
) -> Response[Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]]:
    """Season statistical leader summary

     Return a summary of the leading persons for a number of statistics in a season.

    This call allows you to specify multiple statistics at the same time.  It will return objects for
    each statistic.  In the 'statistics' object only the requested statistic will be returned, not all
    available statistics.

    This call also applies the qualification criteria (defined in the leaders qualification api calls)
    to each person.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SlListSummaryFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SlListSummaryHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        statistics (Union[Unset, str]):  Example: points,minutes.
        win_loss (Union[Unset, SlListSummaryWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        person_id=person_id,
        starter=starter,
        statistics=statistics,
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
    fixture_type: Union[Unset, SlListSummaryFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SlListSummaryHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    statistics: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, SlListSummaryWinLoss] = UNSET,
) -> Optional[Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]]:
    """Season statistical leader summary

     Return a summary of the leading persons for a number of statistics in a season.

    This call allows you to specify multiple statistics at the same time.  It will return objects for
    each statistic.  In the 'statistics' object only the requested statistic will be returned, not all
    available statistics.

    This call also applies the qualification criteria (defined in the leaders qualification api calls)
    to each person.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SlListSummaryFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SlListSummaryHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        statistics (Union[Unset, str]):  Example: points,minutes.
        win_loss (Union[Unset, SlListSummaryWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        person_id=person_id,
        starter=starter,
        statistics=statistics,
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
    fixture_type: Union[Unset, SlListSummaryFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SlListSummaryHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    statistics: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, SlListSummaryWinLoss] = UNSET,
) -> Response[Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]]:
    """Season statistical leader summary

     Return a summary of the leading persons for a number of statistics in a season.

    This call allows you to specify multiple statistics at the same time.  It will return objects for
    each statistic.  In the 'statistics' object only the requested statistic will be returned, not all
    available statistics.

    This call also applies the qualification criteria (defined in the leaders qualification api calls)
    to each person.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SlListSummaryFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SlListSummaryHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        statistics (Union[Unset, str]):  Example: points,minutes.
        win_loss (Union[Unset, SlListSummaryWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        is_player=is_player,
        is_team_official=is_team_official,
        limit=limit,
        offset=offset,
        person_id=person_id,
        starter=starter,
        statistics=statistics,
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
    fixture_type: Union[Unset, SlListSummaryFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, SlListSummaryHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    statistics: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, SlListSummaryWinLoss] = UNSET,
) -> Optional[Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]]:
    """Season statistical leader summary

     Return a summary of the leading persons for a number of statistics in a season.

    This call allows you to specify multiple statistics at the same time.  It will return objects for
    each statistic.  In the 'statistics' object only the requested statistic will be returned, not all
    available statistics.

    This call also applies the qualification criteria (defined in the leaders qualification api calls)
    to each person.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SlListSummaryFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, SlListSummaryHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        statistics (Union[Unset, str]):  Example: points,minutes.
        win_loss (Union[Unset, SlListSummaryWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SlListSummaryLeaderSummaryResponse, SlListSummaryResponseDefault]
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
            hide_null=hide_null,
            home_away=home_away,
            include=include,
            is_player=is_player,
            is_team_official=is_team_official,
            limit=limit,
            offset=offset,
            person_id=person_id,
            starter=starter,
            statistics=statistics,
            win_loss=win_loss,
        )
    ).parsed
