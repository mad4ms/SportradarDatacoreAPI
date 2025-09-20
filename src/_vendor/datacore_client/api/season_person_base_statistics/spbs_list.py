import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.season_person_base_statistics_response import SeasonPersonBaseStatisticsResponse
from ...models.spbs_list_competitor_type import SpbsListCompetitorType
from ...models.spbs_list_fixture_type import SpbsListFixtureType
from ...models.spbs_list_representing_country import SpbsListRepresentingCountry
from ...models.spbs_list_response_default import SpbsListResponseDefault
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, SpbsListCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SpbsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, SpbsListRepresentingCountry] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_competitor_type: Union[Unset, str] = UNSET
    if not isinstance(competitor_type, Unset):
        json_competitor_type = competitor_type.value

    params["competitorType"] = json_competitor_type

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

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_person_id: Union[Unset, str] = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    params["representing"] = representing

    json_representing_country: Union[Unset, str] = UNSET
    if not isinstance(representing_country, Unset):
        json_representing_country = representing_country.value

    params["representingCountry"] = json_representing_country

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/base/for/person/in/seasons/{season_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]:
    if response.status_code == 200:
        response_200 = SeasonPersonBaseStatisticsResponse.from_dict(response.json())

        return response_200

    response_default = SpbsListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]]:
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
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, SpbsListCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SpbsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, SpbsListRepresentingCountry] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]]:
    """Person season base statistics

     Return a list of person base statistics for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, SpbsListCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpbsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, SpbsListRepresentingCountry]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        competitor_type=competitor_type,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        representing=representing,
        representing_country=representing_country,
        updated=updated,
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
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, SpbsListCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SpbsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, SpbsListRepresentingCountry] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]]:
    """Person season base statistics

     Return a list of person base statistics for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, SpbsListCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpbsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, SpbsListRepresentingCountry]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        added=added,
        competitor_type=competitor_type,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        representing=representing,
        representing_country=representing_country,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, SpbsListCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SpbsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, SpbsListRepresentingCountry] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]]:
    """Person season base statistics

     Return a list of person base statistics for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, SpbsListCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpbsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, SpbsListRepresentingCountry]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        added=added,
        competitor_type=competitor_type,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        person_id=person_id,
        representing=representing,
        representing_country=representing_country,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    season_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competitor_type: Union[Unset, SpbsListCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SpbsListFixtureType] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, SpbsListRepresentingCountry] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]]:
    """Person season base statistics

     Return a list of person base statistics for a season

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competitor_type (Union[Unset, SpbsListCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SpbsListFixtureType]):  Example: REGULAR.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, SpbsListRepresentingCountry]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonPersonBaseStatisticsResponse, SpbsListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            added=added,
            competitor_type=competitor_type,
            entity_id=entity_id,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            person_id=person_id,
            representing=representing,
            representing_country=representing_country,
            updated=updated,
        )
    ).parsed
