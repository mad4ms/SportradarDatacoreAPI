import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity_list_age_group import EntityListAgeGroup
from ...models.entity_list_discipline import EntityListDiscipline
from ...models.entity_list_gender import EntityListGender
from ...models.entity_list_representing_country import EntityListRepresentingCountry
from ...models.entity_list_response_default import EntityListResponseDefault
from ...models.entity_list_standard import EntityListStandard
from ...models.entity_list_status import EntityListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, EntityListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, EntityListStandard] = UNSET,
    status: Union[Unset, EntityListStatus] = UNSET,
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

    params["nameFullLatinContains"] = name_full_latin_contains

    params["nameFullLocal"] = name_full_local

    params["nameFullLocalContains"] = name_full_local_contains

    params["offset"] = offset

    params["representing"] = representing

    json_representing_country: Union[Unset, str] = UNSET
    if not isinstance(representing_country, Unset):
        json_representing_country = representing_country.value

    params["representingCountry"] = json_representing_country

    params["sortBy"] = sort_by

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
        "url": f"/handball/o/{organization_id}/entities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> EntityListResponseDefault:
    response_default = EntityListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EntityListResponseDefault]:
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
    age_group: Union[Unset, EntityListAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, EntityListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, EntityListStandard] = UNSET,
    status: Union[Unset, EntityListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[EntityListResponseDefault]:
    """Get a list of teams

     Return a list of available teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, EntityListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        standard (Union[Unset, EntityListStandard]):  Example: ELITE.
        status (Union[Unset, EntityListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
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
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        representing=representing,
        representing_country=representing_country,
        sort_by=sort_by,
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
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, EntityListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, EntityListStandard] = UNSET,
    status: Union[Unset, EntityListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[EntityListResponseDefault]:
    """Get a list of teams

     Return a list of available teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, EntityListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        standard (Union[Unset, EntityListStandard]):  Example: ELITE.
        status (Union[Unset, EntityListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityListResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
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
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        representing=representing,
        representing_country=representing_country,
        sort_by=sort_by,
        standard=standard,
        status=status,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    age_group: Union[Unset, EntityListAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, EntityListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, EntityListStandard] = UNSET,
    status: Union[Unset, EntityListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[EntityListResponseDefault]:
    """Get a list of teams

     Return a list of available teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, EntityListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        standard (Union[Unset, EntityListStandard]):  Example: ELITE.
        status (Union[Unset, EntityListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EntityListResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
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
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        offset=offset,
        representing=representing,
        representing_country=representing_country,
        sort_by=sort_by,
        standard=standard,
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
    age_group: Union[Unset, EntityListAgeGroup] = UNSET,
    discipline: Union[Unset, EntityListDiscipline] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, EntityListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, EntityListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    standard: Union[Unset, EntityListStandard] = UNSET,
    status: Union[Unset, EntityListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[EntityListResponseDefault]:
    """Get a list of teams

     Return a list of available teams

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        age_group (Union[Unset, EntityListAgeGroup]):  Example: SENIOR.
        discipline (Union[Unset, EntityListDiscipline]):  Example: INDOOR.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, EntityListGender]):  Example: MALE.
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        name_full_latin (Union[Unset, str]):
        name_full_latin_contains (Union[Unset, str]):  Example: Dav and nameFullLatin='David
            Johnson'.
        name_full_local (Union[Unset, str]):
        name_full_local_contains (Union[Unset, str]):  Example: Dav and nameFullLocal='David
            Johnson'.
        offset (Union[Unset, int]):  Example: 10.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, EntityListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        standard (Union[Unset, EntityListStandard]):  Example: ELITE.
        status (Union[Unset, EntityListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EntityListResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
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
            name_full_latin_contains=name_full_latin_contains,
            name_full_local=name_full_local,
            name_full_local_contains=name_full_local_contains,
            offset=offset,
            representing=representing,
            representing_country=representing_country,
            sort_by=sort_by,
            standard=standard,
            status=status,
            updated=updated,
        )
    ).parsed
