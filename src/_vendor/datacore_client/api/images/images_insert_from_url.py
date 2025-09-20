from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.images_insert_from_url_base_type import ImagesInsertFromUrlBaseType
from ...models.images_insert_from_url_image_type import ImagesInsertFromUrlImageType
from ...models.images_insert_from_url_images_post_body import (
    ImagesInsertFromUrlImagesPostBody,
)
from ...models.images_insert_from_url_images_response import (
    ImagesInsertFromUrlImagesResponse,
)
from ...models.images_insert_from_url_response_default import (
    ImagesInsertFromUrlResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    base_type: ImagesInsertFromUrlBaseType,
    base_id: UUID,
    image_type: ImagesInsertFromUrlImageType,
    *,
    body: ImagesInsertFromUrlImagesPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/handball/o/{organization_id}/images/for/{base_type}/{base_id}/{image_type}/fromURL",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]:
    if response.status_code == 200:
        response_200 = ImagesInsertFromUrlImagesResponse.from_dict(response.json())

        return response_200

    response_default = ImagesInsertFromUrlResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    base_type: ImagesInsertFromUrlBaseType,
    base_id: UUID,
    image_type: ImagesInsertFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertFromUrlImagesPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]
]:
    """Upload a new image from a URL

     This method allows a new image to uploaded by providing a URL where the image can be downloaded
    from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertFromUrlBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertFromUrlImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
        image_type=image_type,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    base_type: ImagesInsertFromUrlBaseType,
    base_id: UUID,
    image_type: ImagesInsertFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertFromUrlImagesPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]
]:
    """Upload a new image from a URL

     This method allows a new image to uploaded by providing a URL where the image can be downloaded
    from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertFromUrlBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertFromUrlImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
        image_type=image_type,
        client=client,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    base_type: ImagesInsertFromUrlBaseType,
    base_id: UUID,
    image_type: ImagesInsertFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertFromUrlImagesPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]
]:
    """Upload a new image from a URL

     This method allows a new image to uploaded by providing a URL where the image can be downloaded
    from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertFromUrlBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertFromUrlImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
        image_type=image_type,
        body=body,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    base_type: ImagesInsertFromUrlBaseType,
    base_id: UUID,
    image_type: ImagesInsertFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertFromUrlImagesPostBody,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]
]:
    """Upload a new image from a URL

     This method allows a new image to uploaded by providing a URL where the image can be downloaded
    from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertFromUrlBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertFromUrlImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesInsertFromUrlImagesResponse, ImagesInsertFromUrlResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            base_type=base_type,
            base_id=base_id,
            image_type=image_type,
            client=client,
            body=body,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
