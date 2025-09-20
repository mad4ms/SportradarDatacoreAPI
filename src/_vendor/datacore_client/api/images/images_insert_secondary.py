from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ...client import AuthenticatedClient, Client
from ...models.images_insert_secondary_base_type import ImagesInsertSecondaryBaseType
from ...models.images_insert_secondary_image_type import ImagesInsertSecondaryImageType
from ...models.images_insert_secondary_images_response import (
    ImagesInsertSecondaryImagesResponse,
)
from ...models.images_insert_secondary_response_default import (
    ImagesInsertSecondaryResponseDefault,
)
from ...models.images_insert_secondary_secondary_type import (
    ImagesInsertSecondarySecondaryType,
)
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    organization_id: str,
    base_type: ImagesInsertSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesInsertSecondarySecondaryType,
    secondary_id: UUID,
    image_type: ImagesInsertSecondaryImageType,
    *,
    body: File,
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
        "url": f"/handball/o/{organization_id}/images/for/{base_type}/{base_id}/in/{secondary_type}/{secondary_id}/{image_type}",
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]:
    if response.status_code == 200:
        response_200 = ImagesInsertSecondaryImagesResponse.from_dict(response.json())

        return response_200

    response_default = ImagesInsertSecondaryResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    base_type: ImagesInsertSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesInsertSecondarySecondaryType,
    secondary_id: UUID,
    image_type: ImagesInsertSecondaryImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]
]:
    """Upload a new image in a secondary type

     Add a new image for a type in a secondary type.
    You can upload the image in one of two ways:

    - A binary blob in the POST data
    - A 'file' field in a multipart/form-data


    **Binary Blob**

    Upload the image by supplying the image as binary in the POST data.

    The HTTP request would look like

        POST /v1/handball/o/b1a23/images/for/PERSON/81814d2c-d640-11e8-9f8b-f2801f1b9fd1/PERSON_HEAD
        Host: example.com
        Authorization: Bearer some-token
        Content-Length: 808
        Content-Type: image/png

        [file content goes there]


    **Multi-part form**

    Upload the image by supplying it as a 'file' field in a multipart form.
    The file field must be called `filedata` and the content-type must be set to `multipart/form-data`

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesInsertSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertSecondaryImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
        secondary_type=secondary_type,
        secondary_id=secondary_id,
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
    base_type: ImagesInsertSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesInsertSecondarySecondaryType,
    secondary_id: UUID,
    image_type: ImagesInsertSecondaryImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]
]:
    """Upload a new image in a secondary type

     Add a new image for a type in a secondary type.
    You can upload the image in one of two ways:

    - A binary blob in the POST data
    - A 'file' field in a multipart/form-data


    **Binary Blob**

    Upload the image by supplying the image as binary in the POST data.

    The HTTP request would look like

        POST /v1/handball/o/b1a23/images/for/PERSON/81814d2c-d640-11e8-9f8b-f2801f1b9fd1/PERSON_HEAD
        Host: example.com
        Authorization: Bearer some-token
        Content-Length: 808
        Content-Type: image/png

        [file content goes there]


    **Multi-part form**

    Upload the image by supplying it as a 'file' field in a multipart form.
    The file field must be called `filedata` and the content-type must be set to `multipart/form-data`

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesInsertSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertSecondaryImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]
    """

    return sync_detailed(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
        secondary_type=secondary_type,
        secondary_id=secondary_id,
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
    base_type: ImagesInsertSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesInsertSecondarySecondaryType,
    secondary_id: UUID,
    image_type: ImagesInsertSecondaryImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]
]:
    """Upload a new image in a secondary type

     Add a new image for a type in a secondary type.
    You can upload the image in one of two ways:

    - A binary blob in the POST data
    - A 'file' field in a multipart/form-data


    **Binary Blob**

    Upload the image by supplying the image as binary in the POST data.

    The HTTP request would look like

        POST /v1/handball/o/b1a23/images/for/PERSON/81814d2c-d640-11e8-9f8b-f2801f1b9fd1/PERSON_HEAD
        Host: example.com
        Authorization: Bearer some-token
        Content-Length: 808
        Content-Type: image/png

        [file content goes there]


    **Multi-part form**

    Upload the image by supplying it as a 'file' field in a multipart form.
    The file field must be called `filedata` and the content-type must be set to `multipart/form-data`

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesInsertSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertSecondaryImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        base_type=base_type,
        base_id=base_id,
        secondary_type=secondary_type,
        secondary_id=secondary_id,
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
    base_type: ImagesInsertSecondaryBaseType,
    base_id: UUID,
    secondary_type: ImagesInsertSecondarySecondaryType,
    secondary_id: UUID,
    image_type: ImagesInsertSecondaryImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]
]:
    """Upload a new image in a secondary type

     Add a new image for a type in a secondary type.
    You can upload the image in one of two ways:

    - A binary blob in the POST data
    - A 'file' field in a multipart/form-data


    **Binary Blob**

    Upload the image by supplying the image as binary in the POST data.

    The HTTP request would look like

        POST /v1/handball/o/b1a23/images/for/PERSON/81814d2c-d640-11e8-9f8b-f2801f1b9fd1/PERSON_HEAD
        Host: example.com
        Authorization: Bearer some-token
        Content-Length: 808
        Content-Type: image/png

        [file content goes there]


    **Multi-part form**

    Upload the image by supplying it as a 'file' field in a multipart form.
    The file field must be called `filedata` and the content-type must be set to `multipart/form-data`

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        base_type (ImagesInsertSecondaryBaseType):  Example: PERSON.
        base_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        secondary_type (ImagesInsertSecondarySecondaryType):  Example: ENTITY.
        secondary_id (UUID):  Example: 009e9276-5c80-11e8-9c2d-fa7ae01bbebc.
        image_type (ImagesInsertSecondaryImageType):  Example: LOGO.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesInsertSecondaryImagesResponse, ImagesInsertSecondaryResponseDefault]
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            base_type=base_type,
            base_id=base_id,
            secondary_type=secondary_type,
            secondary_id=secondary_id,
            image_type=image_type,
            client=client,
            body=body,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
