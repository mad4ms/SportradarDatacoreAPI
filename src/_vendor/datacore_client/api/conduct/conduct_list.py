import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.conduct_list_conduct_status_type_1 import ConductListConductStatusType1
from ...models.conduct_list_conduct_status_type_2_type_1 import ConductListConductStatusType2Type1
from ...models.conduct_list_conduct_status_type_3_type_1 import ConductListConductStatusType3Type1
from ...models.conduct_list_conduct_type import ConductListConductType
from ...models.conduct_list_response_default import ConductListResponseDefault
from ...models.conduct_response import ConductResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    conduct_status: Union[
        ConductListConductStatusType1,
        ConductListConductStatusType2Type1,
        ConductListConductStatusType3Type1,
        None,
        Unset,
    ] = UNSET,
    conduct_type: Union[Unset, ConductListConductType] = UNSET,
    date_offence_local_end: Union[Unset, datetime.datetime] = UNSET,
    date_offence_local_start: Union[Unset, datetime.datetime] = UNSET,
    date_suspended_from_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_from_start: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_start: Union[Unset, datetime.date] = UNSET,
    entity_group_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_competition_id: Union[Unset, str] = UNSET
    if not isinstance(competition_id, Unset):
        json_competition_id = str(competition_id)
    params["competitionId"] = json_competition_id

    json_conduct_status: Union[None, Unset, str]
    if isinstance(conduct_status, Unset):
        json_conduct_status = UNSET
    elif isinstance(conduct_status, ConductListConductStatusType1):
        json_conduct_status = conduct_status.value
    elif isinstance(conduct_status, ConductListConductStatusType2Type1):
        json_conduct_status = conduct_status.value
    elif isinstance(conduct_status, ConductListConductStatusType3Type1):
        json_conduct_status = conduct_status.value
    else:
        json_conduct_status = conduct_status
    params["conductStatus"] = json_conduct_status

    json_conduct_type: Union[Unset, str] = UNSET
    if not isinstance(conduct_type, Unset):
        json_conduct_type = conduct_type.value

    params["conductType"] = json_conduct_type

    json_date_offence_local_end: Union[Unset, str] = UNSET
    if not isinstance(date_offence_local_end, Unset):
        json_date_offence_local_end = date_offence_local_end.isoformat()
    params["dateOffenceLocalEnd"] = json_date_offence_local_end

    json_date_offence_local_start: Union[Unset, str] = UNSET
    if not isinstance(date_offence_local_start, Unset):
        json_date_offence_local_start = date_offence_local_start.isoformat()
    params["dateOffenceLocalStart"] = json_date_offence_local_start

    json_date_suspended_from_end: Union[Unset, str] = UNSET
    if not isinstance(date_suspended_from_end, Unset):
        json_date_suspended_from_end = date_suspended_from_end.isoformat()
    params["dateSuspendedFromEnd"] = json_date_suspended_from_end

    json_date_suspended_from_start: Union[Unset, str] = UNSET
    if not isinstance(date_suspended_from_start, Unset):
        json_date_suspended_from_start = date_suspended_from_start.isoformat()
    params["dateSuspendedFromStart"] = json_date_suspended_from_start

    json_date_suspended_to_end: Union[Unset, str] = UNSET
    if not isinstance(date_suspended_to_end, Unset):
        json_date_suspended_to_end = date_suspended_to_end.isoformat()
    params["dateSuspendedToEnd"] = json_date_suspended_to_end

    json_date_suspended_to_start: Union[Unset, str] = UNSET
    if not isinstance(date_suspended_to_start, Unset):
        json_date_suspended_to_start = date_suspended_to_start.isoformat()
    params["dateSuspendedToStart"] = json_date_suspended_to_start

    json_entity_group_id: Union[Unset, str] = UNSET
    if not isinstance(entity_group_id, Unset):
        json_entity_group_id = str(entity_group_id)
    params["entityGroupId"] = json_entity_group_id

    json_entity_id: Union[Unset, str] = UNSET
    if not isinstance(entity_id, Unset):
        json_entity_id = str(entity_id)
    params["entityId"] = json_entity_id

    params["external"] = external

    params["fields"] = fields

    json_fixture_id: Union[Unset, str] = UNSET
    if not isinstance(fixture_id, Unset):
        json_fixture_id = str(fixture_id)
    params["fixtureId"] = json_fixture_id

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["nameFamilyLatinStartsWith"] = name_family_latin_starts_with

    params["nameFamilyLocalStartsWith"] = name_family_local_starts_with

    params["nameFullLatin"] = name_full_latin

    params["nameFullLatinContains"] = name_full_latin_contains

    params["nameFullLocal"] = name_full_local

    params["nameFullLocalContains"] = name_full_local_contains

    params["offset"] = offset

    json_person_id: Union[Unset, str] = UNSET
    if not isinstance(person_id, Unset):
        json_person_id = str(person_id)
    params["personId"] = json_person_id

    json_person_ids: Union[Unset, str] = UNSET
    if not isinstance(person_ids, Unset):
        json_person_ids = str(person_ids)
    params["personIds"] = json_person_ids

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    params["sortBy"] = sort_by

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/conduct",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ConductListResponseDefault, ConductResponse]:
    if response.status_code == 200:
        response_200 = ConductResponse.from_dict(response.json())

        return response_200

    response_default = ConductListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ConductListResponseDefault, ConductResponse]]:
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
    competition_id: Union[Unset, UUID] = UNSET,
    conduct_status: Union[
        ConductListConductStatusType1,
        ConductListConductStatusType2Type1,
        ConductListConductStatusType3Type1,
        None,
        Unset,
    ] = UNSET,
    conduct_type: Union[Unset, ConductListConductType] = UNSET,
    date_offence_local_end: Union[Unset, datetime.datetime] = UNSET,
    date_offence_local_start: Union[Unset, datetime.datetime] = UNSET,
    date_suspended_from_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_from_start: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_start: Union[Unset, datetime.date] = UNSET,
    entity_group_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ConductListResponseDefault, ConductResponse]]:
    """Get a list of conduct

     Return a list of available conduct records

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conduct_status (Union[ConductListConductStatusType1, ConductListConductStatusType2Type1,
            ConductListConductStatusType3Type1, None, Unset]):  Example: ACTIVE.
        conduct_type (Union[Unset, ConductListConductType]):  Example: SWEARING.
        date_offence_local_end (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_offence_local_start (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_suspended_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_group_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_family_latin_starts_with (Union[Unset, str]):
        name_family_local_starts_with (Union[Unset, str]):
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: -dateOffenceLocal,added.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConductListResponseDefault, ConductResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        competition_id=competition_id,
        conduct_status=conduct_status,
        conduct_type=conduct_type,
        date_offence_local_end=date_offence_local_end,
        date_offence_local_start=date_offence_local_start,
        date_suspended_from_end=date_suspended_from_end,
        date_suspended_from_start=date_suspended_from_start,
        date_suspended_to_end=date_suspended_to_end,
        date_suspended_to_start=date_suspended_to_start,
        entity_group_id=entity_group_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_id=fixture_id,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_family_latin_starts_with=name_family_latin_starts_with,
        name_family_local_starts_with=name_family_local_starts_with,
        name_full_latin=name_full_latin,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        person_id=person_id,
        person_ids=person_ids,
        season_id=season_id,
        sort_by=sort_by,
        updated=updated,
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
    competition_id: Union[Unset, UUID] = UNSET,
    conduct_status: Union[
        ConductListConductStatusType1,
        ConductListConductStatusType2Type1,
        ConductListConductStatusType3Type1,
        None,
        Unset,
    ] = UNSET,
    conduct_type: Union[Unset, ConductListConductType] = UNSET,
    date_offence_local_end: Union[Unset, datetime.datetime] = UNSET,
    date_offence_local_start: Union[Unset, datetime.datetime] = UNSET,
    date_suspended_from_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_from_start: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_start: Union[Unset, datetime.date] = UNSET,
    entity_group_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ConductListResponseDefault, ConductResponse]]:
    """Get a list of conduct

     Return a list of available conduct records

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conduct_status (Union[ConductListConductStatusType1, ConductListConductStatusType2Type1,
            ConductListConductStatusType3Type1, None, Unset]):  Example: ACTIVE.
        conduct_type (Union[Unset, ConductListConductType]):  Example: SWEARING.
        date_offence_local_end (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_offence_local_start (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_suspended_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_group_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_family_latin_starts_with (Union[Unset, str]):
        name_family_local_starts_with (Union[Unset, str]):
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: -dateOffenceLocal,added.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConductListResponseDefault, ConductResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        competition_id=competition_id,
        conduct_status=conduct_status,
        conduct_type=conduct_type,
        date_offence_local_end=date_offence_local_end,
        date_offence_local_start=date_offence_local_start,
        date_suspended_from_end=date_suspended_from_end,
        date_suspended_from_start=date_suspended_from_start,
        date_suspended_to_end=date_suspended_to_end,
        date_suspended_to_start=date_suspended_to_start,
        entity_group_id=entity_group_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_id=fixture_id,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_family_latin_starts_with=name_family_latin_starts_with,
        name_family_local_starts_with=name_family_local_starts_with,
        name_full_latin=name_full_latin,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        person_id=person_id,
        person_ids=person_ids,
        season_id=season_id,
        sort_by=sort_by,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    conduct_status: Union[
        ConductListConductStatusType1,
        ConductListConductStatusType2Type1,
        ConductListConductStatusType3Type1,
        None,
        Unset,
    ] = UNSET,
    conduct_type: Union[Unset, ConductListConductType] = UNSET,
    date_offence_local_end: Union[Unset, datetime.datetime] = UNSET,
    date_offence_local_start: Union[Unset, datetime.datetime] = UNSET,
    date_suspended_from_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_from_start: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_start: Union[Unset, datetime.date] = UNSET,
    entity_group_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ConductListResponseDefault, ConductResponse]]:
    """Get a list of conduct

     Return a list of available conduct records

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conduct_status (Union[ConductListConductStatusType1, ConductListConductStatusType2Type1,
            ConductListConductStatusType3Type1, None, Unset]):  Example: ACTIVE.
        conduct_type (Union[Unset, ConductListConductType]):  Example: SWEARING.
        date_offence_local_end (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_offence_local_start (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_suspended_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_group_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_family_latin_starts_with (Union[Unset, str]):
        name_family_local_starts_with (Union[Unset, str]):
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: -dateOffenceLocal,added.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ConductListResponseDefault, ConductResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        competition_id=competition_id,
        conduct_status=conduct_status,
        conduct_type=conduct_type,
        date_offence_local_end=date_offence_local_end,
        date_offence_local_start=date_offence_local_start,
        date_suspended_from_end=date_suspended_from_end,
        date_suspended_from_start=date_suspended_from_start,
        date_suspended_to_end=date_suspended_to_end,
        date_suspended_to_start=date_suspended_to_start,
        entity_group_id=entity_group_id,
        entity_id=entity_id,
        external=external,
        fields=fields,
        fixture_id=fixture_id,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_family_latin_starts_with=name_family_latin_starts_with,
        name_family_local_starts_with=name_family_local_starts_with,
        name_full_latin=name_full_latin,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        person_id=person_id,
        person_ids=person_ids,
        season_id=season_id,
        sort_by=sort_by,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    competition_id: Union[Unset, UUID] = UNSET,
    conduct_status: Union[
        ConductListConductStatusType1,
        ConductListConductStatusType2Type1,
        ConductListConductStatusType3Type1,
        None,
        Unset,
    ] = UNSET,
    conduct_type: Union[Unset, ConductListConductType] = UNSET,
    date_offence_local_end: Union[Unset, datetime.datetime] = UNSET,
    date_offence_local_start: Union[Unset, datetime.datetime] = UNSET,
    date_suspended_from_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_from_start: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_end: Union[Unset, datetime.date] = UNSET,
    date_suspended_to_start: Union[Unset, datetime.date] = UNSET,
    entity_group_id: Union[Unset, UUID] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    fixture_id: Union[Unset, UUID] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_id: Union[Unset, UUID] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ConductListResponseDefault, ConductResponse]]:
    """Get a list of conduct

     Return a list of available conduct records

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        competition_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        conduct_status (Union[ConductListConductStatusType1, ConductListConductStatusType2Type1,
            ConductListConductStatusType3Type1, None, Unset]):  Example: ACTIVE.
        conduct_type (Union[Unset, ConductListConductType]):  Example: SWEARING.
        date_offence_local_end (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_offence_local_start (Union[Unset, datetime.datetime]):  Example: 2018-08-16T18:00:00.
        date_suspended_from_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_from_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_end (Union[Unset, datetime.date]):  Example: 2018-08-16.
        date_suspended_to_start (Union[Unset, datetime.date]):  Example: 2018-08-16.
        entity_group_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        fixture_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_family_latin_starts_with (Union[Unset, str]):
        name_family_local_starts_with (Union[Unset, str]):
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        person_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: -dateOffenceLocal,added.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ConductListResponseDefault, ConductResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            competition_id=competition_id,
            conduct_status=conduct_status,
            conduct_type=conduct_type,
            date_offence_local_end=date_offence_local_end,
            date_offence_local_start=date_offence_local_start,
            date_suspended_from_end=date_suspended_from_end,
            date_suspended_from_start=date_suspended_from_start,
            date_suspended_to_end=date_suspended_to_end,
            date_suspended_to_start=date_suspended_to_start,
            entity_group_id=entity_group_id,
            entity_id=entity_id,
            external=external,
            fields=fields,
            fixture_id=fixture_id,
            hide_null=hide_null,
            include=include,
            limit=limit,
            name_family_latin_starts_with=name_family_latin_starts_with,
            name_family_local_starts_with=name_family_local_starts_with,
            name_full_latin=name_full_latin,
            name_full_latin_contains=name_full_latin_contains,
            name_full_local=name_full_local,
            name_full_local_contains=name_full_local_contains,
            offset=offset,
            person_id=person_id,
            person_ids=person_ids,
            season_id=season_id,
            sort_by=sort_by,
            updated=updated,
        )
    ).parsed
