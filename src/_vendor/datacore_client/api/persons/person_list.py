import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.person_list_gender import PersonListGender
from ...models.person_list_persons_response import PersonListPersonsResponse
from ...models.person_list_representing_country import PersonListRepresentingCountry
from ...models.person_list_response_default import PersonListResponseDefault
from ...models.person_list_status import PersonListStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, PersonListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    nationality: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, PersonListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, PersonListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    params["external"] = external

    params["fields"] = fields

    json_gender: Union[Unset, str] = UNSET
    if not isinstance(gender, Unset):
        json_gender = gender.value

    params["gender"] = json_gender

    params["hideNull"] = hide_null

    params["include"] = include

    params["limit"] = limit

    params["nameFamilyLatinStartsWith"] = name_family_latin_starts_with

    params["nameFamilyLocalStartsWith"] = name_family_local_starts_with

    params["nameFullLatin"] = name_full_latin

    params["nameFullLatinContains"] = name_full_latin_contains

    params["nameFullLocal"] = name_full_local

    params["nameFullLocalContains"] = name_full_local_contains

    params["nationality"] = nationality

    params["offset"] = offset

    json_person_ids: Union[Unset, str] = UNSET
    if not isinstance(person_ids, Unset):
        json_person_ids = str(person_ids)
    params["personIds"] = json_person_ids

    params["representing"] = representing

    json_representing_country: Union[Unset, str] = UNSET
    if not isinstance(representing_country, Unset):
        json_representing_country = representing_country.value

    params["representingCountry"] = json_representing_country

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
        "url": f"/handball/o/{organization_id}/persons",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[PersonListPersonsResponse, PersonListResponseDefault]:
    if response.status_code == 200:
        response_200 = PersonListPersonsResponse.from_dict(response.json())

        return response_200

    response_default = PersonListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PersonListPersonsResponse, PersonListResponseDefault]]:
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, PersonListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    nationality: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, PersonListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, PersonListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[PersonListPersonsResponse, PersonListResponseDefault]]:
    """Get a list of persons

     Return a list of available persons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, PersonListGender]):  Example: MALE.
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
        nationality (Union[Unset, str]):  Example: AUS.
        offset (Union[Unset, int]):  Example: 10.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, PersonListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, PersonListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PersonListPersonsResponse, PersonListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_family_latin_starts_with=name_family_latin_starts_with,
        name_family_local_starts_with=name_family_local_starts_with,
        name_full_latin=name_full_latin,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        nationality=nationality,
        offset=offset,
        person_ids=person_ids,
        representing=representing,
        representing_country=representing_country,
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, PersonListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    nationality: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, PersonListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, PersonListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[PersonListPersonsResponse, PersonListResponseDefault]]:
    """Get a list of persons

     Return a list of available persons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, PersonListGender]):  Example: MALE.
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
        nationality (Union[Unset, str]):  Example: AUS.
        offset (Union[Unset, int]):  Example: 10.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, PersonListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, PersonListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PersonListPersonsResponse, PersonListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        added=added,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_family_latin_starts_with=name_family_latin_starts_with,
        name_family_local_starts_with=name_family_local_starts_with,
        name_full_latin=name_full_latin,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        nationality=nationality,
        offset=offset,
        person_ids=person_ids,
        representing=representing,
        representing_country=representing_country,
        sort_by=sort_by,
        status=status,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, PersonListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    nationality: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, PersonListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, PersonListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[PersonListPersonsResponse, PersonListResponseDefault]]:
    """Get a list of persons

     Return a list of available persons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, PersonListGender]):  Example: MALE.
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
        nationality (Union[Unset, str]):  Example: AUS.
        offset (Union[Unset, int]):  Example: 10.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, PersonListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, PersonListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PersonListPersonsResponse, PersonListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        added=added,
        external=external,
        fields=fields,
        gender=gender,
        hide_null=hide_null,
        include=include,
        limit=limit,
        name_family_latin_starts_with=name_family_latin_starts_with,
        name_family_local_starts_with=name_family_local_starts_with,
        name_full_latin=name_full_latin,
        name_full_latin_contains=name_full_latin_contains,
        name_full_local=name_full_local,
        name_full_local_contains=name_full_local_contains,
        nationality=nationality,
        offset=offset,
        person_ids=person_ids,
        representing=representing,
        representing_country=representing_country,
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
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    gender: Union[Unset, PersonListGender] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    name_family_latin_starts_with: Union[Unset, str] = UNSET,
    name_family_local_starts_with: Union[Unset, str] = UNSET,
    name_full_latin: Union[Unset, str] = UNSET,
    name_full_latin_contains: Union[Unset, str] = UNSET,
    name_full_local: Union[Unset, str] = UNSET,
    name_full_local_contains: Union[Unset, str] = UNSET,
    nationality: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    person_ids: Union[Unset, UUID] = UNSET,
    representing: Union[Unset, str] = UNSET,
    representing_country: Union[Unset, PersonListRepresentingCountry] = UNSET,
    sort_by: Union[Unset, str] = UNSET,
    status: Union[Unset, PersonListStatus] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[PersonListPersonsResponse, PersonListResponseDefault]]:
    """Get a list of persons

     Return a list of available persons

    Args:
        organization_id (str):  Example: b1a23.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        gender (Union[Unset, PersonListGender]):  Example: MALE.
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
        nationality (Union[Unset, str]):  Example: AUS.
        offset (Union[Unset, int]):  Example: 10.
        person_ids (Union[Unset, UUID]):  Example:
            009e9276-5c80-11e8-9c2d-fa7ae01bbebc,de83c6a8-3b29-11eb-bdb7-0242ac130005.
        representing (Union[Unset, str]):  Example: AUSTRALIA.
        representing_country (Union[Unset, PersonListRepresentingCountry]):
        sort_by (Union[Unset, str]):  Example: -nameFullLocal,nameFullLatin.
        status (Union[Unset, PersonListStatus]):  Example: ACTIVE.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PersonListPersonsResponse, PersonListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            added=added,
            external=external,
            fields=fields,
            gender=gender,
            hide_null=hide_null,
            include=include,
            limit=limit,
            name_family_latin_starts_with=name_family_latin_starts_with,
            name_family_local_starts_with=name_family_local_starts_with,
            name_full_latin=name_full_latin,
            name_full_latin_contains=name_full_latin_contains,
            name_full_local=name_full_local,
            name_full_local_contains=name_full_local_contains,
            nationality=nationality,
            offset=offset,
            person_ids=person_ids,
            representing=representing,
            representing_country=representing_country,
            sort_by=sort_by,
            status=status,
            updated=updated,
        )
    ).parsed
