from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.user_thread import UserThread
from ...types import Response


def _get_kwargs(
    user_id: str,
    team_id: str,
    thread_id: str,
    post_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/users/{user_id}/teams/{team_id}/threads/{thread_id}/set_unread/{post_id}".format(
            user_id=quote(str(user_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            thread_id=quote(str(thread_id), safe=""),
            post_id=quote(str(post_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | UserThread | None:
    if response.status_code == 200:
        response_200 = UserThread.from_dict(response.json())

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

    if response.status_code == 404:
        response_404 = AppError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | UserThread]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    user_id: str,
    team_id: str,
    thread_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppError | UserThread]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        thread_id=thread_id,
        post_id=post_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    thread_id: str,
    post_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppError | UserThread | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            thread_id=thread_id,
            post_id=post_id,
            client=client,
        )
    ).parsed
