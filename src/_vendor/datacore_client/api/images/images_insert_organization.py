from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.images_insert_organization_base_type import ImagesInsertOrganizationBaseType
from ...models.images_insert_organization_image_type import ImagesInsertOrganizationImageType
from ...models.images_insert_organization_response_default import ImagesInsertOrganizationResponseDefault
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    organization_id: str,
    image_type: ImagesInsertOrganizationImageType,
    *,
    body: File,
    base_type: Union[Unset, ImagesInsertOrganizationBaseType] = ImagesInsertOrganizationBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_base_type: Union[Unset, str] = UNSET
    if not isinstance(base_type, Unset):
        json_base_type = base_type.value

    params["baseType"] = json_base_type

    params["external"] = external

    params["fields"] = fields

    params["hideNull"] = hide_null

    params["include"] = include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/handball/o/{organization_id}/images/for/ORGANIZATION/{image_type}",
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> ImagesInsertOrganizationResponseDefault:
    response_default = ImagesInsertOrganizationResponseDefault.from_dict(response.json())

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ImagesInsertOrganizationResponseDefault]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    image_type: ImagesInsertOrganizationImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    base_type: Union[Unset, ImagesInsertOrganizationBaseType] = ImagesInsertOrganizationBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[ImagesInsertOrganizationResponseDefault]:
    """Upload a new image for the organization

     Add a new image for the organization.
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
        image_type (ImagesInsertOrganizationImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationBaseType]):  Default:
            ImagesInsertOrganizationBaseType.ORGANIZATION. Example: PERSON.
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
        Response[ImagesInsertOrganizationResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        image_type=image_type,
        body=body,
        base_type=base_type,
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
    image_type: ImagesInsertOrganizationImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    base_type: Union[Unset, ImagesInsertOrganizationBaseType] = ImagesInsertOrganizationBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[ImagesInsertOrganizationResponseDefault]:
    """Upload a new image for the organization

     Add a new image for the organization.
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
        image_type (ImagesInsertOrganizationImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationBaseType]):  Default:
            ImagesInsertOrganizationBaseType.ORGANIZATION. Example: PERSON.
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
        ImagesInsertOrganizationResponseDefault
    """

    return sync_detailed(
        organization_id=organization_id,
        image_type=image_type,
        client=client,
        body=body,
        base_type=base_type,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    image_type: ImagesInsertOrganizationImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    base_type: Union[Unset, ImagesInsertOrganizationBaseType] = ImagesInsertOrganizationBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[ImagesInsertOrganizationResponseDefault]:
    """Upload a new image for the organization

     Add a new image for the organization.
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
        image_type (ImagesInsertOrganizationImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationBaseType]):  Default:
            ImagesInsertOrganizationBaseType.ORGANIZATION. Example: PERSON.
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
        Response[ImagesInsertOrganizationResponseDefault]
    """

    kwargs = _get_kwargs(
        organization_id=organization_id,
        image_type=image_type,
        body=body,
        base_type=base_type,
        external=external,
        fields=fields,
        hide_null=hide_null,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    image_type: ImagesInsertOrganizationImageType,
    *,
    client: AuthenticatedClient,
    body: File,
    base_type: Union[Unset, ImagesInsertOrganizationBaseType] = ImagesInsertOrganizationBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[ImagesInsertOrganizationResponseDefault]:
    """Upload a new image for the organization

     Add a new image for the organization.
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
        image_type (ImagesInsertOrganizationImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationBaseType]):  Default:
            ImagesInsertOrganizationBaseType.ORGANIZATION. Example: PERSON.
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
        ImagesInsertOrganizationResponseDefault
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            image_type=image_type,
            client=client,
            body=body,
            base_type=base_type,
            external=external,
            fields=fields,
            hide_null=hide_null,
            include=include,
        )
    ).parsed
