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
    post_id: str,
    *,
    per_page: int | Unset = 0,
    from_post: str | Unset = "",
    from_create_at: int | Unset = 0,
    direction: str | Unset = "",
    skip_fetch_threads: bool | Unset = False,
    collapsed_threads: bool | Unset = False,
    collapsed_threads_extended: bool | Unset = False,
    fetch_prev_next_post_id: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["perPage"] = per_page

    params["fromPost"] = from_post

    params["fromCreateAt"] = from_create_at

    params["direction"] = direction

    params["skipFetchThreads"] = skip_fetch_threads

    params["collapsedThreads"] = collapsed_threads

    params["collapsedThreadsExtended"] = collapsed_threads_extended

    params["fetchPrevNextPostID"] = fetch_prev_next_post_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/posts/{post_id}/thread".format(
            post_id=quote(str(post_id), safe=""),
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
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 0,
    from_post: str | Unset = "",
    from_create_at: int | Unset = 0,
    direction: str | Unset = "",
    skip_fetch_threads: bool | Unset = False,
    collapsed_threads: bool | Unset = False,
    collapsed_threads_extended: bool | Unset = False,
    fetch_prev_next_post_id: bool | Unset = False,
) -> Response[AppError | PostList]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        post_id=post_id,
        per_page=per_page,
        from_post=from_post,
        from_create_at=from_create_at,
        direction=direction,
        skip_fetch_threads=skip_fetch_threads,
        collapsed_threads=collapsed_threads,
        collapsed_threads_extended=collapsed_threads_extended,
        fetch_prev_next_post_id=fetch_prev_next_post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
    per_page: int | Unset = 0,
    from_post: str | Unset = "",
    from_create_at: int | Unset = 0,
    direction: str | Unset = "",
    skip_fetch_threads: bool | Unset = False,
    collapsed_threads: bool | Unset = False,
    collapsed_threads_extended: bool | Unset = False,
    fetch_prev_next_post_id: bool | Unset = False,
) -> AppError | PostList | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            per_page=per_page,
            from_post=from_post,
            from_create_at=from_create_at,
            direction=direction,
            skip_fetch_threads=skip_fetch_threads,
            collapsed_threads=collapsed_threads,
            collapsed_threads_extended=collapsed_threads_extended,
            fetch_prev_next_post_id=fetch_prev_next_post_id,
        )
    ).parsed
