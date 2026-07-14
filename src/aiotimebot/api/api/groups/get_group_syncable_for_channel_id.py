from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.group_syncable_channel import GroupSyncableChannel
from ...types import Response


def _get_kwargs(
    group_id: str,
    channel_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/groups/{group_id}/channels/{channel_id}".format(
            group_id=quote(str(group_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | GroupSyncableChannel | None:
    if response.status_code == 200:
        response_200 = GroupSyncableChannel.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AppError.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if response.status_code == 501:
        response_501 = AppError.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | GroupSyncableChannel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    group_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppError | GroupSyncableChannel]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        group_id=group_id,
        channel_id=channel_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppError | GroupSyncableChannel | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            group_id=group_id,
            channel_id=channel_id,
            client=client,
        )
    ).parsed
