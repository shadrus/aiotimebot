from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.boosted_user_or_channel import BoostedUserOrChannel
from ...models.multi_search_users_channels_channel_types_item import (
    MultiSearchUsersChannelsChannelTypesItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    team_id: str,
    term: str,
    channel_types: list[MultiSearchUsersChannelsChannelTypesItem] | Unset = UNSET,
    archived_channels: bool | Unset = UNSET,
    archived_users: bool | Unset = UNSET,
    limit: int | Unset = 150,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["team_id"] = team_id

    params["term"] = term

    json_channel_types: list[str] | Unset = UNSET
    if not isinstance(channel_types, Unset):
        json_channel_types = []
        for channel_types_item_data in channel_types:
            channel_types_item = channel_types_item_data.value
            json_channel_types.append(channel_types_item)

    params["channel_types"] = json_channel_types

    params["archived_channels"] = archived_channels

    params["archived_users"] = archived_users

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/multi_search/users_channels",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[BoostedUserOrChannel] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = BoostedUserOrChannel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AppError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | list[BoostedUserOrChannel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    team_id: str,
    term: str,
    channel_types: list[MultiSearchUsersChannelsChannelTypesItem] | Unset = UNSET,
    archived_channels: bool | Unset = UNSET,
    archived_users: bool | Unset = UNSET,
    limit: int | Unset = 150,
) -> Response[AppError | list[BoostedUserOrChannel]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        team_id=team_id,
        term=term,
        channel_types=channel_types,
        archived_channels=archived_channels,
        archived_users=archived_users,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    team_id: str,
    term: str,
    channel_types: list[MultiSearchUsersChannelsChannelTypesItem] | Unset = UNSET,
    archived_channels: bool | Unset = UNSET,
    archived_users: bool | Unset = UNSET,
    limit: int | Unset = 150,
) -> AppError | list[BoostedUserOrChannel] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            team_id=team_id,
            term=term,
            channel_types=channel_types,
            archived_channels=archived_channels,
            archived_users=archived_users,
            limit=limit,
        )
    ).parsed
