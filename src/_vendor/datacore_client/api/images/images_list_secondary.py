import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.images_list_secondary_base_type import ImagesListSecondaryBaseType
from ...models.images_list_secondary_image_type import ImagesListSecondaryImageType
from ...models.images_list_secondary_rating import ImagesListSecondaryRating
from ...models.images_list_secondary_response_default import ImagesListSecondaryResponseDefault
from ...models.images_list_secondary_secondary_type import ImagesListSecondarySecondaryType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    base_type: ImagesListSecondaryBaseType,
    secondary_type: ImagesListSecondarySecondaryType,
    secondary_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    json_image_type: Union[Unset, str] = UNSET
    if not isinstance(image_type, Unset):
        json_image_type = image_type.value

    params["imageType"] = json_image_type

    params["include"] = include

    params["limit"] = limit

    params["offset"] = offset

    json_rating: Union[Unset, str] = UNSET
    if not isinstance(rating, Unset):
        json_rating = rating.value

    params["rating"] = json_rating

    json_updated: Union[Unset, str] = UNSET
    if not isinstance(updated, Unset):
        json_updated = updated.isoformat()
    params["updated"] = json_updated

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/handball/o/{organization_id}/images/for/{base_type}/in/{secondary_type}/{secondary_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> ImagesListSecondaryResponseDefault:
    response_default = ImagesListSecondaryResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ImagesListSecondaryResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    base_type: ImagesListSecondaryBaseType,
    secondary_type: ImagesListSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[ImagesListSecondaryResponseDefault]:
    """Get a list of images for a type in a secondary Type

     Return a list of images assigned to type for a secondary type and Id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListSecondaryBaseType):  Example: PERSON.
        secondary_type (ImagesListSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImagesListSecondaryResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        secondary_type=secondary_type,
        secondary_id=secondary_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        image_type=image_type,
        include=include,
        limit=limit,
        offset=offset,
        rating=rating,
        updated=updated,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    base_type: ImagesListSecondaryBaseType,
    secondary_type: ImagesListSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[ImagesListSecondaryResponseDefault]:
    """Get a list of images for a type in a secondary Type

     Return a list of images assigned to type for a secondary type and Id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListSecondaryBaseType):  Example: PERSON.
        secondary_type (ImagesListSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImagesListSecondaryResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        base_type=base_type,
        secondary_type=secondary_type,
        secondary_id=secondary_id,
        client=client,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        image_type=image_type,
        include=include,
        limit=limit,
        offset=offset,
        rating=rating,
        updated=updated,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    base_type: ImagesListSecondaryBaseType,
    secondary_type: ImagesListSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[ImagesListSecondaryResponseDefault]:
    """Get a list of images for a type in a secondary Type

     Return a list of images assigned to type for a secondary type and Id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListSecondaryBaseType):  Example: PERSON.
        secondary_type (ImagesListSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImagesListSecondaryResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        secondary_type=secondary_type,
        secondary_id=secondary_id,
        added=added,
        external=external,
        fields=fields,
        hide_null=hide_null,
        image_type=image_type,
        include=include,
        limit=limit,
        offset=offset,
        rating=rating,
        updated=updated,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    base_type: ImagesListSecondaryBaseType,
    secondary_type: ImagesListSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[ImagesListSecondaryResponseDefault]:
    """Get a list of images for a type in a secondary Type

     Return a list of images assigned to type for a secondary type and Id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListSecondaryBaseType):  Example: PERSON.
        secondary_type (ImagesListSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImagesListSecondaryResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            base_type=base_type,
            secondary_type=secondary_type,
            secondary_id=secondary_id,
            client=client,
            added=added,
            external=external,
            fields=fields,
            hide_null=hide_null,
            image_type=image_type,
            include=include,
            limit=limit,
            offset=offset,
            rating=rating,
            updated=updated,
        )
    ).parsed
