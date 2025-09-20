from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ces_list_fixture_type import CesListFixtureType
from ...models.ces_list_home_away import CesListHomeAway
from ...models.ces_list_response_default import CesListResponseDefault
from ...models.ces_list_win_loss import CesListWinLoss
from ...models.competition_entity_statistics_response import CompetitionEntityStatisticsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    competition_id: UUID,
    *,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    win_loss: Union[Unset, CesListWinLoss] = UNSET,
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

    params["limit"] = limit

    params["offset"] = offset

    json_win_loss: Union[Unset, str] = UNSET
    if not isinstance(win_loss, Unset):
        json_win_loss = win_loss.value

    params["winLoss"] = json_win_loss

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/entity/in/competitions/{competition_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]:
    if response.status_code == 200:
        response_200 = CompetitionEntityStatisticsResponse.from_dict(response.json())

        return response_200

    response_default = CesListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    competition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    win_loss: Union[Unset, CesListWinLoss] = UNSET,
) -> Response[Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]]:
    """Team statistics for a competition

     Return a list of team statistic totals for a competition

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        win_loss (Union[Unset, CesListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        competition_id=competition_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        limit=limit,
        offset=offset,
        win_loss=win_loss,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    competition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    win_loss: Union[Unset, CesListWinLoss] = UNSET,
) -> Optional[Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]]:
    """Team statistics for a competition

     Return a list of team statistic totals for a competition

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        win_loss (Union[Unset, CesListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        competition_id=competition_id,
        client=client,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        limit=limit,
        offset=offset,
        win_loss=win_loss,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    competition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    win_loss: Union[Unset, CesListWinLoss] = UNSET,
) -> Response[Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]]:
    """Team statistics for a competition

     Return a list of team statistic totals for a competition

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        win_loss (Union[Unset, CesListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        competition_id=competition_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        limit=limit,
        offset=offset,
        win_loss=win_loss,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    competition_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    win_loss: Union[Unset, CesListWinLoss] = UNSET,
) -> Optional[Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]]:
    """Team statistics for a competition

     Return a list of team statistic totals for a competition

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        win_loss (Union[Unset, CesListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CesListResponseDefault, CompetitionEntityStatisticsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            competition_id=competition_id,
            client=client,
            entity_id=entity_id,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            hide_null=hide_null,
            home_away=home_away,
            include=include,
            limit=limit,
            offset=offset,
            win_loss=win_loss,
        )
    ).parsed
