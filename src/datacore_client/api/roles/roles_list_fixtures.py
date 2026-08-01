import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.roles_list_fixtures_response_default import RolesListFixturesResponseDefault
from ...models.roles_list_fixtures_role import RolesListFixturesRole
from ...models.roles_list_fixtures_roles_response import RolesListFixturesRolesResponse
from ...models.roles_list_fixtures_status import RolesListFixturesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
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
    role: Union[Unset, RolesListFixturesRole] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, RolesListFixturesStatus] = UNSET,
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

    json_role: Union[Unset, str] = UNSET
    if not isinstance(role, Unset):
        json_role = role.value

    params["role"] = json_role

    json_season_id: Union[Unset, str] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = str(season_id)
    params["seasonId"] = json_season_id

    params["sortBy"] = sort_by

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/roles/in/fixtures",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]:
    if response.status_code == 200:
        response_200 = RolesListFixturesRolesResponse.from_dict(response.json())

        return response_200

    response_default = RolesListFixturesResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]]:
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
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
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
    role: Union[Unset, RolesListFixturesRole] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, RolesListFixturesStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]]:
    """Get a list of match roles

     Return a list of roles for the organization (linked to matches)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
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
        role (Union[Unset, RolesListFixturesRole]):  Example: COACH.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: role.
        status (Union[Unset, RolesListFixturesStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
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
        role=role,
        season_id=season_id,
        sort_by=sort_by,
        status=status,
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
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
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
    role: Union[Unset, RolesListFixturesRole] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, RolesListFixturesStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]]:
    """Get a list of match roles

     Return a list of roles for the organization (linked to matches)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
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
        role (Union[Unset, RolesListFixturesRole]):  Example: COACH.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: role.
        status (Union[Unset, RolesListFixturesStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
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
        role=role,
        season_id=season_id,
        sort_by=sort_by,
        status=status,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
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
    role: Union[Unset, RolesListFixturesRole] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, RolesListFixturesStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]]:
    """Get a list of match roles

     Return a list of roles for the organization (linked to matches)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
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
        role (Union[Unset, RolesListFixturesRole]):  Example: COACH.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: role.
        status (Union[Unset, RolesListFixturesStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        entity_id=entity_id,
        external=external,
        fields=fields,
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
        role=role,
        season_id=season_id,
        sort_by=sort_by,
        status=status,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    entity_id: Union[Unset, UUID] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
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
    role: Union[Unset, RolesListFixturesRole] = UNSET,
    season_id: Union[Unset, UUID] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, RolesListFixturesStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]]:
    """Get a list of match roles

     Return a list of roles for the organization (linked to matches)

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        entity_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
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
        role (Union[Unset, RolesListFixturesRole]):  Example: COACH.
        season_id (Union[Unset, UUID]):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        sort_by (Union[Unset, str]):  Example: role.
        status (Union[Unset, RolesListFixturesStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RolesListFixturesResponseDefault, RolesListFixturesRolesResponse]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            entity_id=entity_id,
            external=external,
            fields=fields,
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
            role=role,
            season_id=season_id,
            sort_by=sort_by,
            status=status,
            updated=updated,
        )
    ).parsed
