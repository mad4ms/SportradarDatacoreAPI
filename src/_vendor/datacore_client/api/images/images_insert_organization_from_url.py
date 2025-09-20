from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ...client import AuthenticatedClient, Client
from ...models.images_insert_organization_from_url_base_type import (
    ImagesInsertOrganizationFromUrlBaseType,
)
from ...models.images_insert_organization_from_url_image_type import (
    ImagesInsertOrganizationFromUrlImageType,
)
from ...models.images_insert_organization_from_url_images_post_body import (
    ImagesInsertOrganizationFromUrlImagesPostBody,
)
from ...models.images_insert_organization_from_url_images_response import (
    ImagesInsertOrganizationFromUrlImagesResponse,
)
from ...models.images_insert_organization_from_url_response_default import (
    ImagesInsertOrganizationFromUrlResponseDefault,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    organization_id: str,
    image_type: ImagesInsertOrganizationFromUrlImageType,
    *,
    body: ImagesInsertOrganizationFromUrlImagesPostBody,
    base_type: Union[
        Unset, ImagesInsertOrganizationFromUrlBaseType
    ] = ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION,
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
        "url": f"/handball/o/{organization_id}/images/for/ORGANIZATION/{image_type}/fromURL",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Union[
    ImagesInsertOrganizationFromUrlImagesResponse,
    ImagesInsertOrganizationFromUrlResponseDefault,
]:
    if response.status_code == 200:
        response_200 = ImagesInsertOrganizationFromUrlImagesResponse.from_dict(
            response.json()
        )

        return response_200

    response_default = ImagesInsertOrganizationFromUrlResponseDefault.from_dict(
        response.json()
    )

    return response_default


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ImagesInsertOrganizationFromUrlImagesResponse,
        ImagesInsertOrganizationFromUrlResponseDefault,
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
    image_type: ImagesInsertOrganizationFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertOrganizationFromUrlImagesPostBody,
    base_type: Union[
        Unset, ImagesInsertOrganizationFromUrlBaseType
    ] = ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ImagesInsertOrganizationFromUrlImagesResponse,
        ImagesInsertOrganizationFromUrlResponseDefault,
    ]
]:
    """Upload a new image for the organization from a URL

     This method allows a new image to be uploaded against the organization type by providing a URL where
    the image can be downloaded from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        image_type (ImagesInsertOrganizationFromUrlImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationFromUrlBaseType]):  Default:
            ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION. Example: PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertOrganizationFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesInsertOrganizationFromUrlImagesResponse, ImagesInsertOrganizationFromUrlResponseDefault]]
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
    image_type: ImagesInsertOrganizationFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertOrganizationFromUrlImagesPostBody,
    base_type: Union[
        Unset, ImagesInsertOrganizationFromUrlBaseType
    ] = ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ImagesInsertOrganizationFromUrlImagesResponse,
        ImagesInsertOrganizationFromUrlResponseDefault,
    ]
]:
    """Upload a new image for the organization from a URL

     This method allows a new image to be uploaded against the organization type by providing a URL where
    the image can be downloaded from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        image_type (ImagesInsertOrganizationFromUrlImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationFromUrlBaseType]):  Default:
            ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION. Example: PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertOrganizationFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesInsertOrganizationFromUrlImagesResponse, ImagesInsertOrganizationFromUrlResponseDefault]
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
    image_type: ImagesInsertOrganizationFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertOrganizationFromUrlImagesPostBody,
    base_type: Union[
        Unset, ImagesInsertOrganizationFromUrlBaseType
    ] = ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ImagesInsertOrganizationFromUrlImagesResponse,
        ImagesInsertOrganizationFromUrlResponseDefault,
    ]
]:
    """Upload a new image for the organization from a URL

     This method allows a new image to be uploaded against the organization type by providing a URL where
    the image can be downloaded from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        image_type (ImagesInsertOrganizationFromUrlImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationFromUrlBaseType]):  Default:
            ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION. Example: PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertOrganizationFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ImagesInsertOrganizationFromUrlImagesResponse, ImagesInsertOrganizationFromUrlResponseDefault]]
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
    image_type: ImagesInsertOrganizationFromUrlImageType,
    *,
    client: AuthenticatedClient,
    body: ImagesInsertOrganizationFromUrlImagesPostBody,
    base_type: Union[
        Unset, ImagesInsertOrganizationFromUrlBaseType
    ] = ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION,
    external: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    hide_null: Union[Unset, bool] = UNSET,
    include: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ImagesInsertOrganizationFromUrlImagesResponse,
        ImagesInsertOrganizationFromUrlResponseDefault,
    ]
]:
    """Upload a new image for the organization from a URL

     This method allows a new image to be uploaded against the organization type by providing a URL where
    the image can be downloaded from.

    **Note**: By uploading the image you confirm that you have the legal right to do so and to allow
    this image to be distributed.

    Args:
        organization_id (str):  Example: b1a23.
        image_type (ImagesInsertOrganizationFromUrlImageType):  Example: LOGO.
        base_type (Union[Unset, ImagesInsertOrganizationFromUrlBaseType]):  Default:
            ImagesInsertOrganizationFromUrlBaseType.ORGANIZATION. Example: PERSON.
        external (Union[Unset, str]):  Example: entityId,personId.
        fields (Union[Unset, str]):  Example: dob,firstName,organization(id),organizations[name],
            teams[name,details/metrics/*,tags(id)].
        hide_null (Union[Unset, bool]):  Example: True.
        include (Union[Unset, str]):  Example: organizations,fixtures,entities.
        body (ImagesInsertOrganizationFromUrlImagesPostBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ImagesInsertOrganizationFromUrlImagesResponse, ImagesInsertOrganizationFromUrlResponseDefault]
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
