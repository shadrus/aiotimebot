from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.team_unread import TeamUnread
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    exclude_team: str | Unset = UNSET,
    include_collapsed_threads: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["exclude_team"] = exclude_team

    params["include_collapsed_threads"] = include_collapsed_threads

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/{user_id}/teams/unread".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[TeamUnread] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TeamUnread.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[AppError | list[TeamUnread]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_team: str | Unset = UNSET,
    include_collapsed_threads: bool | Unset = False,
) -> Response[AppError | list[TeamUnread]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        exclude_team=exclude_team,
        include_collapsed_threads=include_collapsed_threads,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    exclude_team: str | Unset = UNSET,
    include_collapsed_threads: bool | Unset = False,
) -> AppError | list[TeamUnread] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            exclude_team=exclude_team,
            include_collapsed_threads=include_collapsed_threads,
        )
    ).parsed
