import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.fes_listperiod_period_id import FesListperiodPeriodId
from ...models.fes_listperiod_response_default import FesListperiodResponseDefault
from ...models.fixture_entity_statistics_periods_response import FixtureEntityStatisticsPeriodsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, FesListperiodPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
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

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_period_id: Union[Unset, int] = UNSET
    if not isinstance(period_id, Unset):
        json_period_id = period_id.value

    params["periodId"] = json_period_id

    params["section"] = section

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/statistics/for/entity/in/fixtures/{fixture_id}/periods",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]:
    if response.status_code == 200:
        response_200 = FixtureEntityStatisticsPeriodsResponse.from_dict(response.json())

        return response_200

    response_default = FesListperiodResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, FesListperiodPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]]:
    """Team period statistics

     Return a list of team statistics for a match broken down by period

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, FesListperiodPeriodId]):
        section (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        period_id=period_id,
        section=section,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, FesListperiodPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]]:
    """Team period statistics

     Return a list of team statistics for a match broken down by period

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, FesListperiodPeriodId]):
        section (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_id=fixture_id,
        client=client,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        period_id=period_id,
        section=section,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, FesListperiodPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]]:
    """Team period statistics

     Return a list of team statistics for a match broken down by period

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, FesListperiodPeriodId]):
        section (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
        limit=limit,
        offset=offset,
        period_id=period_id,
        section=section,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    fixture_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    period_id: Union[Unset, FesListperiodPeriodId] = UNSET,
    section: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]]:
    """Team period statistics

     Return a list of team statistics for a match broken down by period

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        period_id (Union[Unset, FesListperiodPeriodId]):
        section (Union[Unset, str]):
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[FesListperiodResponseDefault, FixtureEntityStatisticsPeriodsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_id=fixture_id,
            client=client,
            added=added,
            entity_id=entity_id,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
            limit=limit,
            offset=offset,
            period_id=period_id,
            section=section,
            updated=updated,
        )
    ).parsed
