from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.post_list import PostList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    channel_id: str,
    *,
    limit_before: int | Unset = 60,
    limit_after: int | Unset = 60,
    skip_fetch_threads: bool | Unset = False,
    collapsed_threads: bool | Unset = False,
    collapsed_threads_extended: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit_before"] = limit_before

    params["limit_after"] = limit_after

    params["skipFetchThreads"] = skip_fetch_threads

    params["collapsedThreads"] = collapsed_threads

    params["collapsedThreadsExtended"] = collapsed_threads_extended

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/{user_id}/channels/{channel_id}/posts/unread".format(
            user_id=quote(str(user_id), safe=""),
            channel_id=quote(str(channel_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | PostList | None:
    if response.status_code == 200:
        response_200 = PostList.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | PostList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    user_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit_before: int | Unset = 60,
    limit_after: int | Unset = 60,
    skip_fetch_threads: bool | Unset = False,
    collapsed_threads: bool | Unset = False,
    collapsed_threads_extended: bool | Unset = False,
) -> Response[AppError | PostList]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        channel_id=channel_id,
        limit_before=limit_before,
        limit_after=limit_after,
        skip_fetch_threads=skip_fetch_threads,
        collapsed_threads=collapsed_threads,
        collapsed_threads_extended=collapsed_threads_extended,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit_before: int | Unset = 60,
    limit_after: int | Unset = 60,
    skip_fetch_threads: bool | Unset = False,
    collapsed_threads: bool | Unset = False,
    collapsed_threads_extended: bool | Unset = False,
) -> AppError | PostList | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            channel_id=channel_id,
            client=client,
            limit_before=limit_before,
            limit_after=limit_after,
            skip_fetch_threads=skip_fetch_threads,
            collapsed_threads=collapsed_threads,
            collapsed_threads_extended=collapsed_threads_extended,
        )
    ).parsed
