from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.psts_list_age_group import PstsListAgeGroup
from ...models.psts_list_fixture_type import PstsListFixtureType
from ...models.psts_list_representation import PstsListRepresentation
from ...models.psts_list_response_default import PstsListResponseDefault
from ...models.psts_list_season_type import PstsListSeasonType
from ...models.psts_list_standard import PstsListStandard
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    person_id: UUID,
    *,
    age_group: Union[Unset, PstsListAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, PstsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, PstsListRepresentation] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_type: Union[Unset, PstsListSeasonType] = UNSET,
    standard: Union[Unset, PstsListStandard] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_age_group: Union[Unset, str] = UNSET
    if not isinstance(age_group, Unset):
        json_age_group = age_group.value

    params["ageGroup"] = json_age_group

    json_competition_id: Union[Unset, str] = UNSET
    if not isinstance(competition_id, Unset):
        json_competition_id = str(competition_id)
    params["competitionId"] = json_competition_id

    params["external"] = external

    params["fields"] = fields

    json_fixture_type: Union[Unset, str] = UNSET
    if not isinstance(fixture_type, Unset):
        json_fixture_type = fixture_type.value

    params["fixtureType"] = json_fixture_type

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_representation: Union[Unset, str] = UNSET
    if not isinstance(representation, Unset):
        json_representation = representation.value

    params["representation"] = json_representation

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    json_season_type: Union[Unset, str] = UNSET
    if not isinstance(season_type, Unset):
        json_season_type = season_type.value

    params["seasonType"] = json_season_type

    json_standard: Union[Unset, str] = UNSET
    if not isinstance(standard, Unset):
        json_standard = standard.value

    params["standard"] = json_standard

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/person/{person_id}/in/seasons/combined",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> PstsListResponseDefault:
    response_default = PstsListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PstsListResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    person_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    age_group: Union[Unset, PstsListAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, PstsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, PstsListRepresentation] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_type: Union[Unset, PstsListSeasonType] = UNSET,
    standard: Union[Unset, PstsListStandard] = UNSET,
) -> Response[PstsListResponseDefault]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a season.
        If a person plays for multiple teams in a season then their statistics are normally
        separated out by team.
        For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        age_group (Union[Unset, PstsListAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, PstsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, PstsListRepresentation]):  Example: CLUB.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_type (Union[Unset, PstsListSeasonType]):  Example: SEASON.
        standard (Union[Unset, PstsListStandard]):  Example: ELITE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PstsListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        person_id=person_id,
        age_group=age_group,
        competition_id=competition_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        representation=representation,
        season_id=season_id,
        season_type=season_type,
        standard=standard,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    person_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    age_group: Union[Unset, PstsListAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, PstsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, PstsListRepresentation] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_type: Union[Unset, PstsListSeasonType] = UNSET,
    standard: Union[Unset, PstsListStandard] = UNSET,
) -> Optional[PstsListResponseDefault]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a season.
        If a person plays for multiple teams in a season then their statistics are normally
        separated out by team.
        For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        age_group (Union[Unset, PstsListAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, PstsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, PstsListRepresentation]):  Example: CLUB.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_type (Union[Unset, PstsListSeasonType]):  Example: SEASON.
        standard (Union[Unset, PstsListStandard]):  Example: ELITE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PstsListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        person_id=person_id,
        client=client,
        age_group=age_group,
        competition_id=competition_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        representation=representation,
        season_id=season_id,
        season_type=season_type,
        standard=standard,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    person_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    age_group: Union[Unset, PstsListAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, PstsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, PstsListRepresentation] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_type: Union[Unset, PstsListSeasonType] = UNSET,
    standard: Union[Unset, PstsListStandard] = UNSET,
) -> Response[PstsListResponseDefault]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a season.
        If a person plays for multiple teams in a season then their statistics are normally
        separated out by team.
        For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        age_group (Union[Unset, PstsListAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, PstsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, PstsListRepresentation]):  Example: CLUB.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_type (Union[Unset, PstsListSeasonType]):  Example: SEASON.
        standard (Union[Unset, PstsListStandard]):  Example: ELITE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PstsListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        person_id=person_id,
        age_group=age_group,
        competition_id=competition_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        representation=representation,
        season_id=season_id,
        season_type=season_type,
        standard=standard,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    person_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    age_group: Union[Unset, PstsListAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, PstsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, PstsListRepresentation] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    season_type: Union[Unset, PstsListSeasonType] = UNSET,
    standard: Union[Unset, PstsListStandard] = UNSET,
) -> Optional[PstsListResponseDefault]:
    """Person season statistics - combined teams


        Return a list of person statistic totals for a season.
        If a person plays for multiple teams in a season then their statistics are normally
        separated out by team.
        For this call the statistics are combined - and hence team data is not available.


    Args:
        organization_id (str):  Example: b1a23.
        person_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        age_group (Union[Unset, PstsListAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, PstsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, PstsListRepresentation]):  Example: CLUB.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        season_type (Union[Unset, PstsListSeasonType]):  Example: SEASON.
        standard (Union[Unset, PstsListStandard]):  Example: ELITE.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PstsListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            person_id=person_id,
            client=client,
            age_group=age_group,
            competition_id=competition_id,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            representation=representation,
            season_id=season_id,
            season_type=season_type,
            standard=standard,
        )
    ).parsed
