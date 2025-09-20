from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.sebs_delete_all_competitor_type import SebsDeleteAllCompetitorType
from ...models.sebs_delete_all_fixture_type import SebsDeleteAllFixtureType
from ...models.sebs_delete_all_response_default import SebsDeleteAllResponseDefault
from ...models.sebs_delete_all_season_entity_base_statistics_response import (
    SebsDeleteAllSeasonEntityBaseStatisticsResponse,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    season_id: UUID,
    *,
    competitor_type: Union[Unset, SebsDeleteAllCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SebsDeleteAllFixtureType] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    params["forceDelete"] = force_delete

    params["hideNull"] = hide_null

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/handball/o/{organization_id}/statistics/base/for/entity/in/seasons/{season_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse
]:
    if response.status_code == 200:
        response_200 = SebsDeleteAllSeasonEntityBaseStatisticsResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = SebsDeleteAllResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]
]:
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
    client: AuthenticatedClient,
    competitor_type: Union[Unset, SebsDeleteAllCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SebsDeleteAllFixtureType] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]
]:
    """Delete season team base statistics

     Delete a base statistic record for a team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competitor_type (Union[Unset, SebsDeleteAllCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SebsDeleteAllFixtureType]):  Example: REGULAR.
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        competitor_type=competitor_type,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    season_id: UUID,
    *,
    client: AuthenticatedClient,
    competitor_type: Union[Unset, SebsDeleteAllCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SebsDeleteAllFixtureType] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]
]:
    """Delete season team base statistics

     Delete a base statistic record for a team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competitor_type (Union[Unset, SebsDeleteAllCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SebsDeleteAllFixtureType]):  Example: REGULAR.
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        season_id=season_id,
        client=client,
        competitor_type=competitor_type,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    season_id: UUID,
    *,
    client: AuthenticatedClient,
    competitor_type: Union[Unset, SebsDeleteAllCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SebsDeleteAllFixtureType] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]
]:
    """Delete season team base statistics

     Delete a base statistic record for a team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competitor_type (Union[Unset, SebsDeleteAllCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SebsDeleteAllFixtureType]):  Example: REGULAR.
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        season_id=season_id,
        competitor_type=competitor_type,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_type=fixture_type,
        force_delete=force_delete,
        hide_null=hide_null,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    season_id: UUID,
    *,
    client: AuthenticatedClient,
    competitor_type: Union[Unset, SebsDeleteAllCompetitorType] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_type: Union[Unset, SebsDeleteAllFixtureType] = UNSET,
    force_delete: Union[Unset, bool] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]
]:
    """Delete season team base statistics

     Delete a base statistic record for a team in a season.

    Args:
        organization_id (str):  Example: b1a23.
        season_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        competitor_type (Union[Unset, SebsDeleteAllCompetitorType]):  Example: PERSON.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_type (Union[Unset, SebsDeleteAllFixtureType]):  Example: REGULAR.
        force_delete (Union[Unset, bool]):  Example: True.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SebsDeleteAllResponseDefault, SebsDeleteAllSeasonEntityBaseStatisticsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            season_id=season_id,
            client=client,
            competitor_type=competitor_type,
            entity_id=entity_id,
            external=external,
            fields=fields,
            fixture_type=fixture_type,
            force_delete=force_delete,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
