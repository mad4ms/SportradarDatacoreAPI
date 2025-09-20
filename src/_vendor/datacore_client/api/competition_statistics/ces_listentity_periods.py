from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.ces_listentity_periods_competition_entity_statistics_response import (
    CesListentityPeriodsCompetitionEntityStatisticsResponse,
)
from ...models.ces_listentity_periods_fixture_type import CesListentityPeriodsFixtureType
from ...models.ces_listentity_periods_home_away import CesListentityPeriodsHomeAway
from ...models.ces_listentity_periods_period_id import CesListentityPeriodsPeriodId
from ...models.ces_listentity_periods_response_default import CesListentityPeriodsResponseDefault
from ...models.ces_listentity_periods_win_loss import CesListentityPeriodsWinLoss
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    competition_id: UUID,
    entity_id: UUID,
    *,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListentityPeriodsFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListentityPeriodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, CesListentityPeriodsPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, CesListentityPeriodsWinLoss] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    json_period_id: Union[Unset, int] = UNSET
    if not isinstance(period_id, Unset):
        json_period_id = period_id.value

    params["periodId"] = json_period_id

    params["section"] = section

    json_win_loss: Union[Unset, str] = UNSET
    if not isinstance(win_loss, Unset):
        json_win_loss = win_loss.value

    params["winLoss"] = json_win_loss

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/entity/in/competitions/{competition_id}/entities/{entity_id}/periods",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]:
    if response.status_code == 200:
        response_200 = CesListentityPeriodsCompetitionEntityStatisticsResponse.from_dict(response.json())

        return response_200

    response_default = CesListentityPeriodsResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    competition_id: UUID,
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListentityPeriodsFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListentityPeriodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, CesListentityPeriodsPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, CesListentityPeriodsWinLoss] = UNSET,
) -> Response[Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]]:
    """Statistics for a team in a competition

     Return the statistics for a specific team in a competition.

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListentityPeriodsFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListentityPeriodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, CesListentityPeriodsPeriodId]):
        section (Union[Unset, str]):
        win_loss (Union[Unset, CesListentityPeriodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]]
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
        period_id=period_id,
        section=section,
        win_loss=win_loss,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    competition_id: UUID,
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListentityPeriodsFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListentityPeriodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, CesListentityPeriodsPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, CesListentityPeriodsWinLoss] = UNSET,
) -> Optional[Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]]:
    """Statistics for a team in a competition

     Return the statistics for a specific team in a competition.

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListentityPeriodsFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListentityPeriodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, CesListentityPeriodsPeriodId]):
        section (Union[Unset, str]):
        win_loss (Union[Unset, CesListentityPeriodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        competition_id=competition_id,
        entity_id=entity_id,
        client=client,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        home_away=home_away,
        include=include,
        limit=limit,
        offset=offset,
        period_id=period_id,
        section=section,
        win_loss=win_loss,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    competition_id: UUID,
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListentityPeriodsFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListentityPeriodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, CesListentityPeriodsPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, CesListentityPeriodsWinLoss] = UNSET,
) -> Response[Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]]:
    """Statistics for a team in a competition

     Return the statistics for a specific team in a competition.

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListentityPeriodsFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListentityPeriodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, CesListentityPeriodsPeriodId]):
        section (Union[Unset, str]):
        win_loss (Union[Unset, CesListentityPeriodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]]
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
        period_id=period_id,
        section=section,
        win_loss=win_loss,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    competition_id: UUID,
    entity_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CesListentityPeriodsFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CesListentityPeriodsHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, CesListentityPeriodsPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    win_loss: Union[Unset, CesListentityPeriodsWinLoss] = UNSET,
) -> Optional[Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]]:
    """Statistics for a team in a competition

     Return the statistics for a specific team in a competition.

    Args:
        organization_id (str):  Example: b1a23.
        competition_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CesListentityPeriodsFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CesListentityPeriodsHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, CesListentityPeriodsPeriodId]):
        section (Union[Unset, str]):
        win_loss (Union[Unset, CesListentityPeriodsWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CesListentityPeriodsCompetitionEntityStatisticsResponse, CesListentityPeriodsResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            competition_id=competition_id,
            entity_id=entity_id,
            client=client,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            hide_null=hide_null,
            home_away=home_away,
            include=include,
            limit=limit,
            offset=offset,
            period_id=period_id,
            section=section,
            win_loss=win_loss,
        )
    ).parsed
