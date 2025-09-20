import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.game_log_person_response import GameLogPersonResponse
from ...models.gamelog_listperson_fixture_type import GamelogListpersonFixtureType
from ...models.gamelog_listperson_home_away import GamelogListpersonHomeAway
from ...models.gamelog_listperson_response_default import GamelogListpersonResponseDefault
from ...models.gamelog_listperson_win_loss import GamelogListpersonWinLoss
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    person_id: UUID,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListpersonFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListpersonHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = True,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListpersonWinLoss] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

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

    params["starter"] = starter

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    json_win_loss: Union[Unset, str] = UNSET
    if not isinstance(win_loss, Unset):
        json_win_loss = win_loss.value

    params["winLoss"] = json_win_loss

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/person/{person_id}/in/fixtures/seasons/{season_id}/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[GameLogPersonResponse, GamelogListpersonResponseDefault]:
    if response.status_code == 200:
        response_200 = GameLogPersonResponse.from_dict(response.json())

        return response_200

    response_default = GamelogListpersonResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GameLogPersonResponse, GamelogListpersonResponseDefault]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    person_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListpersonFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListpersonHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = True,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListpersonWinLoss] = UNSET,
) -> Response[Union[GameLogPersonResponse, GamelogListpersonResponseDefault]]:
    """Match History for a person

     Return the Match History (based on statistics present) for a specific person in a season.

    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListpersonFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListpersonHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):  Default: True.
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListpersonWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GameLogPersonResponse, GamelogListpersonResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        person_id=person_id,
        season_id=season_id,
        added=added,
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
        starter=starter,
        updated=updated,
        win_loss=win_loss,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    person_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListpersonFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListpersonHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = True,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListpersonWinLoss] = UNSET,
) -> Optional[Union[GameLogPersonResponse, GamelogListpersonResponseDefault]]:
    """Match History for a person

     Return the Match History (based on statistics present) for a specific person in a season.

    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListpersonFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListpersonHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):  Default: True.
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListpersonWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GameLogPersonResponse, GamelogListpersonResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        person_id=person_id,
        season_id=season_id,
        client=client,
        added=added,
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
        starter=starter,
        updated=updated,
        win_loss=win_loss,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    person_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListpersonFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListpersonHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = True,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListpersonWinLoss] = UNSET,
) -> Response[Union[GameLogPersonResponse, GamelogListpersonResponseDefault]]:
    """Match History for a person

     Return the Match History (based on statistics present) for a specific person in a season.

    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListpersonFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListpersonHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):  Default: True.
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListpersonWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GameLogPersonResponse, GamelogListpersonResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        person_id=person_id,
        season_id=season_id,
        added=added,
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
        starter=starter,
        updated=updated,
        win_loss=win_loss,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    person_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListpersonFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListpersonHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = True,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListpersonWinLoss] = UNSET,
) -> Optional[Union[GameLogPersonResponse, GamelogListpersonResponseDefault]]:
    """Match History for a person

     Return the Match History (based on statistics present) for a specific person in a season.

    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListpersonFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListpersonHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):  Default: True.
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        starter (Union[Unset, bool]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListpersonWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GameLogPersonResponse, GamelogListpersonResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            person_id=person_id,
            season_id=season_id,
            client=client,
            added=added,
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
            starter=starter,
            updated=updated,
            win_loss=win_loss,
        )
    ).parsed
