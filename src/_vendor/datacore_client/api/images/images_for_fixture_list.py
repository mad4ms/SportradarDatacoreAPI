import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.images_for_fixture_list_base_type import ImagesForFixtureListBaseType
from ...models.images_for_fixture_list_image_type import ImagesForFixtureListImageType
from ...models.images_for_fixture_list_images_response import (
    ImagesForFixtureListImagesResponse,
)
from ...models.images_for_fixture_list_rating import ImagesForFixtureListRating
from ...models.images_for_fixture_list_response_default import (
    ImagesForFixtureListResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    fixture_id: UUID,
    *,
    added: Union[Unset, datetime.datetime] = UNSET,
    base_type: Union[Unset, ImagesForFixtureListBaseType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesForFixtureListImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesForFixtureListRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_added: Union[Unset, str] = UNSET
    if not isinstance(added, Unset):
        json_added = added.isoformat()
    params["added"] = json_added

    json_base_type: Union[Unset, str] = UNSET
    if not isinstance(base_type, Unset):
        json_base_type = base_type.value

    params["baseType"] = json_base_type

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
        "url": f"/handball/o/{organization_id}/images/for/FIXTURE/{fixture_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]:
    if response.status_code == 200:
        response_200 = ImagesForFixtureListImagesResponse.from_dict(response.json())

        return response_200

    response_default = ImagesForFixtureListResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]
]:
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
    base_type: Union[Unset, ImagesForFixtureListBaseType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesForFixtureListImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesForFixtureListRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]
]:
    """Get a list of images for a fixture

     Return a list of images for the fixture

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        base_type (Union[Unset, ImagesForFixtureListBaseType]):  Example: PERSON,ENTITY.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesForFixtureListImageType]):  Example: LOGO,PERSON_HEAD.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesForFixtureListRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        base_type=base_type,
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
    fixture_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    base_type: Union[Unset, ImagesForFixtureListBaseType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesForFixtureListImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesForFixtureListRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]
]:
    """Get a list of images for a fixture

     Return a list of images for the fixture

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        base_type (Union[Unset, ImagesForFixtureListBaseType]):  Example: PERSON,ENTITY.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesForFixtureListImageType]):  Example: LOGO,PERSON_HEAD.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesForFixtureListRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        fixture_id=fixture_id,
        client=client,
        added=added,
        base_type=base_type,
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
    fixture_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    base_type: Union[Unset, ImagesForFixtureListBaseType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesForFixtureListImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesForFixtureListRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Response[
    Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]
]:
    """Get a list of images for a fixture

     Return a list of images for the fixture

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        base_type (Union[Unset, ImagesForFixtureListBaseType]):  Example: PERSON,ENTITY.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesForFixtureListImageType]):  Example: LOGO,PERSON_HEAD.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesForFixtureListRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        fixture_id=fixture_id,
        added=added,
        base_type=base_type,
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
    fixture_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    added: Union[Unset, datetime.datetime] = UNSET,
    base_type: Union[Unset, ImagesForFixtureListBaseType] = UNSET,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    image_type: Union[Unset, ImagesForFixtureListImageType] = UNSET,
    include: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = UNSET,
    rating: Union[Unset, ImagesForFixtureListRating] = UNSET,
    updated: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[
    Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]
]:
    """Get a list of images for a fixture

     Return a list of images for the fixture

    Args:
        organization_id (str):  Example: b1a23.
        fixture_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        added (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:10:48.
        base_type (Union[Unset, ImagesForFixtureListBaseType]):  Example: PERSON,ENTITY.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        image_type (Union[Unset, ImagesForFixtureListImageType]):  Example: LOGO,PERSON_HEAD.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        limit (Union[Unset, int]):  Default: 10. Example: 10.
        offset (Union[Unset, int]):  Example: 10.
        rating (Union[Unset, ImagesForFixtureListRating]):  Example: UNKNOWN.
        updated (Union[Unset, datetime.datetime]):  Example: 2018-08-16T02:11:48.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesForFixtureListImagesResponse, ImagesForFixtureListResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            fixture_id=fixture_id,
            client=client,
            added=added,
            base_type=base_type,
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
