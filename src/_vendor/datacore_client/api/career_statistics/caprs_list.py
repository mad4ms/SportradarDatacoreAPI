from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.caprs_list_age_group import CaprsListAgeGroup
from ...models.caprs_list_career_person_representational_statistics_response import (
    CaprsListCareerPersonRepresentationalStatisticsResponse,
)
from ...models.caprs_list_discipline import CaprsListDiscipline
from ...models.caprs_list_fixture_type import CaprsListFixtureType
from ...models.caprs_list_home_away import CaprsListHomeAway
from ...models.caprs_list_representation import CaprsListRepresentation
from ...models.caprs_list_representing_country import CaprsListRepresentingCountry
from ...models.caprs_list_response_default import CaprsListResponseDefault
from ...models.caprs_list_win_loss import CaprsListWinLoss
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    age_group: Union[Unset, CaprsListAgeGroup] = UNSET,
    discipline: Union[Unset, CaprsListDiscipline] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CaprsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CaprsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representation: Union[Unset, CaprsListRepresentation] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, CaprsListRepresentingCountry] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    win_loss: Union[Unset, CaprsListWinLoss] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_age_group: Union[Unset, str] = UNSET
    if not isinstance(age_group, Unset):
        json_age_group = age_group.value

    params["ageGroup"] = json_age_group

    json_discipline: Union[Unset, str] = UNSET
    if not isinstance(discipline, Unset):
        json_discipline = discipline.value

    params["discipline"] = json_discipline

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

    json_person_ids: Union[Unset, str] = UNSET
    if not isinstance(person_ids, Unset):
        json_person_ids = str(person_ids)
    params["personIds"] = json_person_ids

    json_representation: Union[Unset, str] = UNSET
    if not isinstance(representation, Unset):
        json_representation = representation.value

    params["representation"] = json_representation

    params["representing"] = representing

    json_representing_country: Union[Unset, str] = UNSET
    if not isinstance(representing_country, Unset):
        json_representing_country = representing_country.value

    params["representingCountry"] = json_representing_country

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    params["starter"] = starter

    json_win_loss: Union[Unset, str] = UNSET
    if not isinstance(win_loss, Unset):
        json_win_loss = win_loss.value

    params["winLoss"] = json_win_loss

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/person/in/career/representing",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]:
    if response.status_code == 200:
        response_200 = CaprsListCareerPersonRepresentationalStatisticsResponse.from_dict(response.json())

        return response_200

    response_default = CaprsListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]]:
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
    age_group: Union[Unset, CaprsListAgeGroup] = UNSET,
    discipline: Union[Unset, CaprsListDiscipline] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CaprsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CaprsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representation: Union[Unset, CaprsListRepresentation] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, CaprsListRepresentingCountry] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    win_loss: Union[Unset, CaprsListWinLoss] = UNSET,
) -> Response[Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]]:
    """Person career representational statistics

     Return a list of person statistic totals for their career covering all competitions, groupped by
    their
        discipline, age group, and representation

    Args:
        organization_id (str):  Example: b1a23.
        age_group (Union[Unset, CaprsListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, CaprsListDiscipline]):  Example: INDOOR.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CaprsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CaprsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representation (Union[Unset, CaprsListRepresentation]):  Example: CLUB.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, CaprsListRepresentingCountry]):
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        win_loss (Union[Unset, CaprsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        age_group=age_group,
        discipline=discipline,
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
        person_ids=person_ids,
        representation=representation,
        representing=representing,
        representing_country=representing_country,
        season_id=season_id,
        starter=starter,
        win_loss=win_loss,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    age_group: Union[Unset, CaprsListAgeGroup] = UNSET,
    discipline: Union[Unset, CaprsListDiscipline] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CaprsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CaprsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representation: Union[Unset, CaprsListRepresentation] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, CaprsListRepresentingCountry] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    win_loss: Union[Unset, CaprsListWinLoss] = UNSET,
) -> Optional[Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]]:
    """Person career representational statistics

     Return a list of person statistic totals for their career covering all competitions, groupped by
    their
        discipline, age group, and representation

    Args:
        organization_id (str):  Example: b1a23.
        age_group (Union[Unset, CaprsListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, CaprsListDiscipline]):  Example: INDOOR.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CaprsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CaprsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representation (Union[Unset, CaprsListRepresentation]):  Example: CLUB.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, CaprsListRepresentingCountry]):
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        win_loss (Union[Unset, CaprsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        age_group=age_group,
        discipline=discipline,
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
        person_ids=person_ids,
        representation=representation,
        representing=representing,
        representing_country=representing_country,
        season_id=season_id,
        starter=starter,
        win_loss=win_loss,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    age_group: Union[Unset, CaprsListAgeGroup] = UNSET,
    discipline: Union[Unset, CaprsListDiscipline] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CaprsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CaprsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representation: Union[Unset, CaprsListRepresentation] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, CaprsListRepresentingCountry] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    win_loss: Union[Unset, CaprsListWinLoss] = UNSET,
) -> Response[Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]]:
    """Person career representational statistics

     Return a list of person statistic totals for their career covering all competitions, groupped by
    their
        discipline, age group, and representation

    Args:
        organization_id (str):  Example: b1a23.
        age_group (Union[Unset, CaprsListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, CaprsListDiscipline]):  Example: INDOOR.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CaprsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CaprsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representation (Union[Unset, CaprsListRepresentation]):  Example: CLUB.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, CaprsListRepresentingCountry]):
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        win_loss (Union[Unset, CaprsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        age_group=age_group,
        discipline=discipline,
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
        person_ids=person_ids,
        representation=representation,
        representing=representing,
        representing_country=representing_country,
        season_id=season_id,
        starter=starter,
        win_loss=win_loss,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    age_group: Union[Unset, CaprsListAgeGroup] = UNSET,
    discipline: Union[Unset, CaprsListDiscipline] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, CaprsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    home_away: Union[Unset, CaprsListHomeAway] = UNSET,
    include: Union[Unset, str] = UNSET,
    is_player: Union[Unset, bool] = UNSET,
    is_team_official: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representation: Union[Unset, CaprsListRepresentation] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, CaprsListRepresentingCountry] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    starter: Union[Unset, bool] = UNSET,
    win_loss: Union[Unset, CaprsListWinLoss] = UNSET,
) -> Optional[Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]]:
    """Person career representational statistics

     Return a list of person statistic totals for their career covering all competitions, groupped by
    their
        discipline, age group, and representation

    Args:
        organization_id (str):  Example: b1a23.
        age_group (Union[Unset, CaprsListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, CaprsListDiscipline]):  Example: INDOOR.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, CaprsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        home_away (Union[Unset, CaprsListHomeAway]):
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        is_player (Union[Unset, bool]):
        is_team_official (Union[Unset, bool]):
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representation (Union[Unset, CaprsListRepresentation]):  Example: CLUB.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, CaprsListRepresentingCountry]):
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        starter (Union[Unset, bool]):
        win_loss (Union[Unset, CaprsListWinLoss]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CaprsListCareerPersonRepresentationalStatisticsResponse, CaprsListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            age_group=age_group,
            discipline=discipline,
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
            person_ids=person_ids,
            representation=representation,
            representing=representing,
            representing_country=representing_country,
            season_id=season_id,
            starter=starter,
            win_loss=win_loss,
        )
    ).parsed
