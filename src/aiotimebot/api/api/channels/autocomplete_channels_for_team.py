from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.channel import Channel
from ...models.channel_type_for_team import ChannelTypeForTeam
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    name: str,
    channel_types: list[ChannelTypeForTeam] | Unset = UNSET,
    archived: bool | Unset = UNSET,
    boost: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["name"] = name

    json_channel_types: list[str] | Unset = UNSET
    if not isinstance(channel_types, Unset):
        json_channel_types = []
        for channel_types_item_data in channel_types:
            channel_types_item = channel_types_item_data.value
            json_channel_types.append(channel_types_item)

    params["channel_types"] = json_channel_types

    params["archived"] = archived

    params["boost"] = boost

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/teams/{team_id}/channels/autocomplete".format(
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
        for componentsschemas_channel_list_item_data in _response_200:
            componentsschemas_channel_list_item = Channel.from_dict(
                componentsschemas_channel_list_item_data
            )

            response_200.append(componentsschemas_channel_list_item)

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
) -> Response[AppError | list[Channel]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
    channel_types: list[ChannelTypeForTeam] | Unset = UNSET,
    archived: bool | Unset = UNSET,
    boost: bool | Unset = False,
) -> Response[AppError | list[Channel]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        team_id=team_id,
        name=name,
        channel_types=channel_types,
        archived=archived,
        boost=boost,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    name: str,
    channel_types: list[ChannelTypeForTeam] | Unset = UNSET,
    archived: bool | Unset = UNSET,
    boost: bool | Unset = False,
) -> AppError | list[Channel] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            name=name,
            channel_types=channel_types,
            archived=archived,
            boost=boost,
        )
    ).parsed
