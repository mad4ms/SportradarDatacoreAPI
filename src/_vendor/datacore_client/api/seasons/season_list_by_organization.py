import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.season_list_by_organization_age_group import SeasonListByOrganizationAgeGroup
from ...models.season_list_by_organization_discipline import SeasonListByOrganizationDiscipline
from ...models.season_list_by_organization_event_type import SeasonListByOrganizationEventType
from ...models.season_list_by_organization_gender import SeasonListByOrganizationGender
from ...models.season_list_by_organization_representation import SeasonListByOrganizationRepresentation
from ...models.season_list_by_organization_response_default import SeasonListByOrganizationResponseDefault
from ...models.season_list_by_organization_season_type import SeasonListByOrganizationSeasonType
from ...models.season_list_by_organization_seasons_response import SeasonListByOrganizationSeasonsResponse
from ...models.season_list_by_organization_standard import SeasonListByOrganizationStandard
from ...models.season_list_by_organization_status import SeasonListByOrganizationStatus
from ...models.season_list_by_organization_video_production import SeasonListByOrganizationVideoProduction
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, SeasonListByOrganizationAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    discipline: Union[Unset, SeasonListByOrganizationDiscipline] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    event_type: Union[Unset, SeasonListByOrganizationEventType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, SeasonListByOrganizationGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, SeasonListByOrganizationRepresentation] = UNSET,
    season_type: Union[Unset, SeasonListByOrganizationSeasonType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, SeasonListByOrganizationStandard] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, SeasonListByOrganizationStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_production: Union[Unset, SeasonListByOrganizationVideoProduction] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_age_group: Union[Unset, str] = UNSET
    if not isinstance(age_group, Unset):
        json_age_group = age_group.value

    params["ageGroup"] = json_age_group

    json_competition_id: Union[Unset, str] = UNSET
    if not isinstance(competition_id, Unset):
        json_competition_id = str(competition_id)
    params["competitionId"] = json_competition_id

    json_discipline: Union[Unset, str] = UNSET
    if not isinstance(discipline, Unset):
        json_discipline = discipline.value

    params["discipline"] = json_discipline

    json_end_date: Union[Unset, str] = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["endDate"] = json_end_date

    json_event_type: Union[Unset, str] = UNSET
    if not isinstance(event_type, Unset):
        json_event_type = event_type.value

    params["eventType"] = json_event_type

    params["external"] = external

    params["fields"] = fields

    json_gender: Union[Unset, str] = UNSET
    if not isinstance(gender, Unset):
        json_gender = gender.value

    params["gender"] = json_gender

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["nameLatinContains"] = name_latin_contains

    params["nameLocalContains"] = name_local_contains

    params["offset"] = offset

    json_representation: Union[Unset, str] = UNSET
    if not isinstance(representation, Unset):
        json_representation = representation.value

    params["representation"] = json_representation

    json_season_type: Union[Unset, str] = UNSET
    if not isinstance(season_type, Unset):
        json_season_type = season_type.value

    params["seasonType"] = json_season_type

    params["sortBy"] = sort_by

    json_standard: Union[Unset, str] = UNSET
    if not isinstance(standard, Unset):
        json_standard = standard.value

    params["standard"] = json_standard

    json_start_date: Union[Unset, str] = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["startDate"] = json_start_date

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    json_video_production: Union[Unset, str] = UNSET
    if not isinstance(video_production, Unset):
        json_video_production = video_production.value

    params["videoProduction"] = json_video_production

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/seasons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]:
    if response.status_code == 200:
        response_200 = SeasonListByOrganizationSeasonsResponse.from_dict(response.json())

        return response_200

    response_default = SeasonListByOrganizationResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]]:
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
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, SeasonListByOrganizationAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    discipline: Union[Unset, SeasonListByOrganizationDiscipline] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    event_type: Union[Unset, SeasonListByOrganizationEventType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, SeasonListByOrganizationGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, SeasonListByOrganizationRepresentation] = UNSET,
    season_type: Union[Unset, SeasonListByOrganizationSeasonType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, SeasonListByOrganizationStandard] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, SeasonListByOrganizationStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_production: Union[Unset, SeasonListByOrganizationVideoProduction] = UNSET,
) -> Response[Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]]:
    """Get a list of seasons for an organization

     Return a list of seasons in an organization.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, SeasonListByOrganizationAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        discipline (Union[Unset, SeasonListByOrganizationDiscipline]):  Example: INDOOR.
        end_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        event_type (Union[Unset, SeasonListByOrganizationEventType]):  Example: FIXTURE.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, SeasonListByOrganizationGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, SeasonListByOrganizationRepresentation]):  Example: CLUB.
        season_type (Union[Unset, SeasonListByOrganizationSeasonType]):  Example: SEASON.
        sort_by (Union[Unset, str]):  Example: -nameLocal.
        standard (Union[Unset, SeasonListByOrganizationStandard]):  Example: ELITE.
        start_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        status (Union[Unset, SeasonListByOrganizationStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_production (Union[Unset, SeasonListByOrganizationVideoProduction]):  Example:
            NONE,AUTOMATED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        age_group=age_group,
        competition_id=competition_id,
        discipline=discipline,
        end_date=end_date,
        event_type=event_type,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        representation=representation,
        season_type=season_type,
        sort_by=sort_by,
        standard=standard,
        start_date=start_date,
        status=status,
        updated=updated,
        video_production=video_production,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, SeasonListByOrganizationAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    discipline: Union[Unset, SeasonListByOrganizationDiscipline] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    event_type: Union[Unset, SeasonListByOrganizationEventType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, SeasonListByOrganizationGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, SeasonListByOrganizationRepresentation] = UNSET,
    season_type: Union[Unset, SeasonListByOrganizationSeasonType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, SeasonListByOrganizationStandard] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, SeasonListByOrganizationStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_production: Union[Unset, SeasonListByOrganizationVideoProduction] = UNSET,
) -> Optional[Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]]:
    """Get a list of seasons for an organization

     Return a list of seasons in an organization.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, SeasonListByOrganizationAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        discipline (Union[Unset, SeasonListByOrganizationDiscipline]):  Example: INDOOR.
        end_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        event_type (Union[Unset, SeasonListByOrganizationEventType]):  Example: FIXTURE.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, SeasonListByOrganizationGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, SeasonListByOrganizationRepresentation]):  Example: CLUB.
        season_type (Union[Unset, SeasonListByOrganizationSeasonType]):  Example: SEASON.
        sort_by (Union[Unset, str]):  Example: -nameLocal.
        standard (Union[Unset, SeasonListByOrganizationStandard]):  Example: ELITE.
        start_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        status (Union[Unset, SeasonListByOrganizationStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_production (Union[Unset, SeasonListByOrganizationVideoProduction]):  Example:
            NONE,AUTOMATED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        age_group=age_group,
        competition_id=competition_id,
        discipline=discipline,
        end_date=end_date,
        event_type=event_type,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        representation=representation,
        season_type=season_type,
        sort_by=sort_by,
        standard=standard,
        start_date=start_date,
        status=status,
        updated=updated,
        video_production=video_production,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, SeasonListByOrganizationAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    discipline: Union[Unset, SeasonListByOrganizationDiscipline] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    event_type: Union[Unset, SeasonListByOrganizationEventType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, SeasonListByOrganizationGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, SeasonListByOrganizationRepresentation] = UNSET,
    season_type: Union[Unset, SeasonListByOrganizationSeasonType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, SeasonListByOrganizationStandard] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, SeasonListByOrganizationStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_production: Union[Unset, SeasonListByOrganizationVideoProduction] = UNSET,
) -> Response[Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]]:
    """Get a list of seasons for an organization

     Return a list of seasons in an organization.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, SeasonListByOrganizationAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        discipline (Union[Unset, SeasonListByOrganizationDiscipline]):  Example: INDOOR.
        end_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        event_type (Union[Unset, SeasonListByOrganizationEventType]):  Example: FIXTURE.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, SeasonListByOrganizationGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, SeasonListByOrganizationRepresentation]):  Example: CLUB.
        season_type (Union[Unset, SeasonListByOrganizationSeasonType]):  Example: SEASON.
        sort_by (Union[Unset, str]):  Example: -nameLocal.
        standard (Union[Unset, SeasonListByOrganizationStandard]):  Example: ELITE.
        start_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        status (Union[Unset, SeasonListByOrganizationStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_production (Union[Unset, SeasonListByOrganizationVideoProduction]):  Example:
            NONE,AUTOMATED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        age_group=age_group,
        competition_id=competition_id,
        discipline=discipline,
        end_date=end_date,
        event_type=event_type,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_latin_contains=name_latin_contains,
        name_local_contains=name_local_contains,
        offset=offset,
        representation=representation,
        season_type=season_type,
        sort_by=sort_by,
        standard=standard,
        start_date=start_date,
        status=status,
        updated=updated,
        video_production=video_production,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, SeasonListByOrganizationAgeGroup] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    discipline: Union[Unset, SeasonListByOrganizationDiscipline] = UNSET,
    end_date: Union[Unset, datetime.date] = UNSET,
    event_type: Union[Unset, SeasonListByOrganizationEventType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, SeasonListByOrganizationGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_latin_contains: Union[Unset, str] = UNSET,
    name_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representation: Union[Unset, SeasonListByOrganizationRepresentation] = UNSET,
    season_type: Union[Unset, SeasonListByOrganizationSeasonType] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, SeasonListByOrganizationStandard] = UNSET,
    start_date: Union[Unset, datetime.date] = UNSET,
    status: Union[Unset, SeasonListByOrganizationStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
    video_production: Union[Unset, SeasonListByOrganizationVideoProduction] = UNSET,
) -> Optional[Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]]:
    """Get a list of seasons for an organization

     Return a list of seasons in an organization.

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, SeasonListByOrganizationAgeGroup]):  Example: SENIOR.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        discipline (Union[Unset, SeasonListByOrganizationDiscipline]):  Example: INDOOR.
        end_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        event_type (Union[Unset, SeasonListByOrganizationEventType]):  Example: FIXTURE.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, SeasonListByOrganizationGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_latin_contains (Union[Unset, str]):  Example: Dav and nameLatin='David Johnson'.
        name_local_contains (Union[Unset, str]):  Example: Dav and nameLocal='David Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representation (Union[Unset, SeasonListByOrganizationRepresentation]):  Example: CLUB.
        season_type (Union[Unset, SeasonListByOrganizationSeasonType]):  Example: SEASON.
        sort_by (Union[Unset, str]):  Example: -nameLocal.
        standard (Union[Unset, SeasonListByOrganizationStandard]):  Example: ELITE.
        start_date (Union[Unset, datetime.date]):  Example: 2018-08-16.
        status (Union[Unset, SeasonListByOrganizationStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.
        video_production (Union[Unset, SeasonListByOrganizationVideoProduction]):  Example:
            NONE,AUTOMATED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SeasonListByOrganizationResponseDefault, SeasonListByOrganizationSeasonsResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            age_group=age_group,
            competition_id=competition_id,
            discipline=discipline,
            end_date=end_date,
            event_type=event_type,
            external=external,
            fields=fields,
            gender=gender,
            hide_null=hide_null,
            include=include,
            limit=limit,
            name_latin_contains=name_latin_contains,
            name_local_contains=name_local_contains,
            offset=offset,
            representation=representation,
            season_type=season_type,
            sort_by=sort_by,
            standard=standard,
            start_date=start_date,
            status=status,
            updated=updated,
            video_production=video_production,
        )
    ).parsed
