import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity_list_by_entity_group_age_group import (
    EntityListByEntityGroupAgeGroup,
)
from ...models.entity_list_by_entity_group_discipline import (
    EntityListByEntityGroupDiscipline,
)
from ...models.entity_list_by_entity_group_entities_response import (
    EntityListByEntityGroupEntitiesResponse,
)
from ...models.entity_list_by_entity_group_gender import EntityListByEntityGroupGender
from ...models.entity_list_by_entity_group_response_default import (
    EntityListByEntityGroupResponseDefault,
)
from ...models.entity_list_by_entity_group_standard import (
    EntityListByEntityGroupStandard,
)
from ...models.entity_list_by_entity_group_status import EntityListByEntityGroupStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    entity_group_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListByEntityGroupAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListByEntityGroupDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListByEntityGroupGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    standard: Union[Unset, EntityListByEntityGroupStandard] = UNSET,
    status: Union[Unset, EntityListByEntityGroupStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
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

    json_discipline: Union[Unset, str] = UNSET
    if not isinstance(discipline, Unset):
        json_discipline = discipline.value

    params["discipline"] = json_discipline

    params["external"] = external

    params["fields"] = fields

    json_gender: Union[Unset, str] = UNSET
    if not isinstance(gender, Unset):
        json_gender = gender.value

    params["gender"] = json_gender

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["nameFullLatin"] = name_full_latin

    params["nameFullLocal"] = name_full_local

    params["offset"] = offset

    json_standard: Union[Unset, str] = UNSET
    if not isinstance(standard, Unset):
        json_standard = standard.value

    params["standard"] = json_standard

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
        "url": f"/handball/o/{organization_id}/entityGroups/{entity_group_id}/entities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault
]:
    if response.status_code == 200:
        response_200 = EntityListByEntityGroupEntitiesResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = EntityListByEntityGroupResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    entity_group_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListByEntityGroupAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListByEntityGroupDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListByEntityGroupGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    standard: Union[Unset, EntityListByEntityGroupStandard] = UNSET,
    status: Union[Unset, EntityListByEntityGroupStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault
    ]
]:
    """Get a list of teams for a club

     Return a list of available teams linked to a specific club

    Args:
        organization_id (str):  Example: b1a23.
        entity_group_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListByEntityGroupAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListByEntityGroupDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListByEntityGroupGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_local (Union[Unset, str]):
        offset (Union[Unset, int]):  Example: 10.
        standard (Union[Unset, EntityListByEntityGroupStandard]):  Example: ELITE.
        status (Union[Unset, EntityListByEntityGroupStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        entity_group_id=entity_group_id,
        added=added,
        age_group=age_group,
        discipline=discipline,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_full_latin=name_full_latin,
        name_full_local=name_full_local,
        offset=offset,
        standard=standard,
        status=status,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    entity_group_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListByEntityGroupAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListByEntityGroupDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListByEntityGroupGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    standard: Union[Unset, EntityListByEntityGroupStandard] = UNSET,
    status: Union[Unset, EntityListByEntityGroupStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault
    ]
]:
    """Get a list of teams for a club

     Return a list of available teams linked to a specific club

    Args:
        organization_id (str):  Example: b1a23.
        entity_group_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListByEntityGroupAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListByEntityGroupDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListByEntityGroupGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_local (Union[Unset, str]):
        offset (Union[Unset, int]):  Example: 10.
        standard (Union[Unset, EntityListByEntityGroupStandard]):  Example: ELITE.
        status (Union[Unset, EntityListByEntityGroupStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        entity_group_id=entity_group_id,
        client=client,
        added=added,
        age_group=age_group,
        discipline=discipline,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_full_latin=name_full_latin,
        name_full_local=name_full_local,
        offset=offset,
        standard=standard,
        status=status,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    entity_group_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListByEntityGroupAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListByEntityGroupDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListByEntityGroupGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    standard: Union[Unset, EntityListByEntityGroupStandard] = UNSET,
    status: Union[Unset, EntityListByEntityGroupStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[
        EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault
    ]
]:
    """Get a list of teams for a club

     Return a list of available teams linked to a specific club

    Args:
        organization_id (str):  Example: b1a23.
        entity_group_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListByEntityGroupAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListByEntityGroupDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListByEntityGroupGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_local (Union[Unset, str]):
        offset (Union[Unset, int]):  Example: 10.
        standard (Union[Unset, EntityListByEntityGroupStandard]):  Example: ELITE.
        status (Union[Unset, EntityListByEntityGroupStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        entity_group_id=entity_group_id,
        added=added,
        age_group=age_group,
        discipline=discipline,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_full_latin=name_full_latin,
        name_full_local=name_full_local,
        offset=offset,
        standard=standard,
        status=status,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    entity_group_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListByEntityGroupAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListByEntityGroupDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListByEntityGroupGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    standard: Union[Unset, EntityListByEntityGroupStandard] = UNSET,
    status: Union[Unset, EntityListByEntityGroupStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[
        EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault
    ]
]:
    """Get a list of teams for a club

     Return a list of available teams linked to a specific club

    Args:
        organization_id (str):  Example: b1a23.
        entity_group_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListByEntityGroupAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListByEntityGroupDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListByEntityGroupGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_local (Union[Unset, str]):
        offset (Union[Unset, int]):  Example: 10.
        standard (Union[Unset, EntityListByEntityGroupStandard]):  Example: ELITE.
        status (Union[Unset, EntityListByEntityGroupStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[EntityListByEntityGroupEntitiesResponse, EntityListByEntityGroupResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            entity_group_id=entity_group_id,
            client=client,
            added=added,
            age_group=age_group,
            discipline=discipline,
            external=external,
            fields=fields,
            gender=gender,
            hide_null=hide_null,
            include=include,
            limit=limit,
            name_full_latin=name_full_latin,
            name_full_local=name_full_local,
            offset=offset,
            standard=standard,
            status=status,
            updated=updated,
        )
    ).parsed
