import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.game_log_entity_response import GameLogEntityResponse
from ...models.gamelog_listentity_fixture_type import GamelogListentityFixtureType
from ...models.gamelog_listentity_home_away import GamelogListentityHomeAway
from ...models.gamelog_listentity_response_default import GamelogListentityResponseDefault
from ...models.gamelog_listentity_win_loss import GamelogListentityWinLoss
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    entity_id: UUID,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListentityFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListentityHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListentityWinLoss] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

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

    params["limit"] = limit

    params["offset"] = offset

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
        "url": f"/handball/o/{organization_id}/statistics/for/entity/{entity_id}/in/fixtures/seasons/{season_id}/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[GameLogEntityResponse, GamelogListentityResponseDefault]:
    if response.status_code == 200:
        response_200 = GameLogEntityResponse.from_dict(response.json())

        return response_200

    response_default = GamelogListentityResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GameLogEntityResponse, GamelogListentityResponseDefault]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    entity_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListentityFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListentityHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListentityWinLoss] = UNSET,
) -> Response[Union[GameLogEntityResponse, GamelogListentityResponseDefault]]:
    """Match History for a team

     Return the Match History (based on statistics present) for a specific team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListentityFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListentityHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListentityWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GameLogEntityResponse, GamelogListentityResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        entity_id=entity_id,
        season_id=season_id,
        added=added,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        limit=limit,
        offset=offset,
        updated=updated,
        win_loss=win_loss,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    entity_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListentityFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListentityHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListentityWinLoss] = UNSET,
) -> Optional[Union[GameLogEntityResponse, GamelogListentityResponseDefault]]:
    """Match History for a team

     Return the Match History (based on statistics present) for a specific team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListentityFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListentityHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListentityWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GameLogEntityResponse, GamelogListentityResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        entity_id=entity_id,
        season_id=season_id,
        client=client,
        added=added,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        limit=limit,
        offset=offset,
        updated=updated,
        win_loss=win_loss,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    entity_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListentityFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListentityHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListentityWinLoss] = UNSET,
) -> Response[Union[GameLogEntityResponse, GamelogListentityResponseDefault]]:
    """Match History for a team

     Return the Match History (based on statistics present) for a specific team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListentityFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListentityHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListentityWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GameLogEntityResponse, GamelogListentityResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        entity_id=entity_id,
        season_id=season_id,
        added=added,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        limit=limit,
        offset=offset,
        updated=updated,
        win_loss=win_loss,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    entity_id: UUID,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, GamelogListentityFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, GamelogListentityHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    win_loss: Union[Unset, GamelogListentityWinLoss] = UNSET,
) -> Optional[Union[GameLogEntityResponse, GamelogListentityResponseDefault]]:
    """Match History for a team

     Return the Match History (based on statistics present) for a specific team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, GamelogListentityFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, GamelogListentityHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        win_loss (Union[Unset, GamelogListentityWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GameLogEntityResponse, GamelogListentityResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            entity_id=entity_id,
            season_id=season_id,
            client=client,
            added=added,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            hide_null=hide_null,
            home_away=home_away,
            include=include,
            limit=limit,
            offset=offset,
            updated=updated,
            win_loss=win_loss,
        )
    ).parsed
