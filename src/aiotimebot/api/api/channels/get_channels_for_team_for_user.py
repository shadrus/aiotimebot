from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.channel import Channel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    include_deleted: bool | Unset = False,
    last_delete_at: int | Unset = 0,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_deleted"] = include_deleted

    params["last_delete_at"] = last_delete_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/{user_id}/teams/{team_id}/channels".format(
            user_id=quote(str(user_id), safe=""),
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[Channel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Channel.from_dict(response_200_item_data)

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

    if response.status_code == 404:
        response_404 = AppError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | list[Channel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    user_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = False,
    last_delete_at: int | Unset = 0,
) -> Response[AppError | list[Channel]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        include_deleted=include_deleted,
        last_delete_at=last_delete_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    include_deleted: bool | Unset = False,
    last_delete_at: int | Unset = 0,
) -> AppError | list[Channel] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            client=client,
            include_deleted=include_deleted,
            last_delete_at=last_delete_at,
        )
    ).parsed
