from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.upload_temp_file_body import UploadTempFileBody
from ...models.upload_temp_file_response_201 import UploadTempFileResponse201
from ...models.upload_temp_file_source import UploadTempFileSource
from ...types import UNSET, Response, Unset


def _get_kwargs(
    source: UploadTempFileSource,
    source_id: str,
    *,
    body: UploadTempFileBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/files/{source}/{source_id}".format(
            source=quote(str(source), safe=""),
            source_id=quote(str(source_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["files"] = body.to_multipart()

    headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | UploadTempFileResponse201 | None:
    if response.status_code == 201:
        response_201 = UploadTempFileResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | UploadTempFileResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    source: UploadTempFileSource,
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadTempFileBody | Unset = UNSET,
) -> Response[AppError | UploadTempFileResponse201]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        source=source,
        source_id=source_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    source: UploadTempFileSource,
    source_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UploadTempFileBody | Unset = UNSET,
) -> AppError | UploadTempFileResponse201 | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            source=source,
            source_id=source_id,
            client=client,
            body=body,
        )
    ).parsed
