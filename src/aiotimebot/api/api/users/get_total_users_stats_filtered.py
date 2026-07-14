from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.users_stats import UsersStats
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    include_bots: bool | Unset = UNSET,
    roles: str | Unset = UNSET,
    channel_roles: str | Unset = UNSET,
    team_roles: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["in_team"] = in_team

    params["in_channel"] = in_channel

    params["include_deleted"] = include_deleted

    params["include_bots"] = include_bots

    params["roles"] = roles

    params["channel_roles"] = channel_roles

    params["team_roles"] = team_roles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/stats/filtered",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | UsersStats | None:
    if response.status_code == 200:
        response_200 = UsersStats.from_dict(response.json())

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
) -> Response[AppError | UsersStats]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    include_bots: bool | Unset = UNSET,
    roles: str | Unset = UNSET,
    channel_roles: str | Unset = UNSET,
    team_roles: str | Unset = UNSET,
) -> Response[AppError | UsersStats]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        in_team=in_team,
        in_channel=in_channel,
        include_deleted=include_deleted,
        include_bots=include_bots,
        roles=roles,
        channel_roles=channel_roles,
        team_roles=team_roles,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    include_deleted: bool | Unset = UNSET,
    include_bots: bool | Unset = UNSET,
    roles: str | Unset = UNSET,
    channel_roles: str | Unset = UNSET,
    team_roles: str | Unset = UNSET,
) -> AppError | UsersStats | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            in_team=in_team,
            in_channel=in_channel,
            include_deleted=include_deleted,
            include_bots=include_bots,
            roles=roles,
            channel_roles=channel_roles,
            team_roles=team_roles,
        )
    ).parsed
