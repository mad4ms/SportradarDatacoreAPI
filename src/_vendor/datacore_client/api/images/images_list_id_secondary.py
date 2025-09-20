import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.images_list_id_secondary_base_type import ImagesListIdSecondaryBaseType
from ...models.images_list_id_secondary_image_type import ImagesListIdSecondaryImageType
from ...models.images_list_id_secondary_images_response import (
    ImagesListIdSecondaryImagesResponse,
)
from ...models.images_list_id_secondary_rating import ImagesListIdSecondaryRating
from ...models.images_list_id_secondary_response_default import (
    ImagesListIdSecondaryResponseDefault,
)
from ...models.images_list_id_secondary_secondary_type import (
    ImagesListIdSecondarySecondaryType,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    base_type: ImagesListIdSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesListIdSecondarySecondaryType,
    secondary_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListIdSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListIdSecondaryRating] = UNSET,
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
        "url": f"/handball/o/{organization_id}/images/for/{base_type}/{base_id}/in/{secondary_type}/{secondary_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]:
    if response.status_code == 200:
        response_200 = ImagesListIdSecondaryImagesResponse.from_dict(response.json())

        return response_200

    response_default = ImagesListIdSecondaryResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    base_type: ImagesListIdSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesListIdSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListIdSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListIdSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]
]:
    """Get a list of images for a specific base and secondary id

     Return a list of images for the base id for a secondary id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListIdSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesListIdSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListIdSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListIdSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
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
    base_type: ImagesListIdSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesListIdSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListIdSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListIdSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]
]:
    """Get a list of images for a specific base and secondary id

     Return a list of images for the base id for a secondary id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListIdSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesListIdSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListIdSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListIdSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
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
    base_type: ImagesListIdSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesListIdSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListIdSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListIdSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]
]:
    """Get a list of images for a specific base and secondary id

     Return a list of images for the base id for a secondary id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListIdSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesListIdSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListIdSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListIdSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
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
    base_type: ImagesListIdSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesListIdSecondarySecondaryType,
    secondary_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesListIdSecondaryImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesListIdSecondaryRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]
]:
    """Get a list of images for a specific base and secondary id

     Return a list of images for the base id for a secondary id

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesListIdSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesListIdSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesListIdSecondaryImageType]):  Example: LOGO.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesListIdSecondaryRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesListIdSecondaryImagesResponse, ImagesListIdSecondaryResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            base_type=base_type,
            base_id=base_id,
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
