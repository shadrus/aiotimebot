from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.channel_with_team_data import ChannelWithTeamData
from ...models.search_all_channels_body import SearchAllChannelsBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchAllChannelsBody,
    system_console: bool | Unset = True,
    boost: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["system_console"] = system_console

    params["boost"] = boost

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/channels/search",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[ChannelWithTeamData] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_channel_list_with_team_data_item_data in _response_200:
            componentsschemas_channel_list_with_team_data_item = (
                ChannelWithTeamData.from_dict(
                    componentsschemas_channel_list_with_team_data_item_data
                )
            )

            response_200.append(componentsschemas_channel_list_with_team_data_item)

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | list[ChannelWithTeamData]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAllChannelsBody,
    system_console: bool | Unset = True,
    boost: bool | Unset = False,
) -> Response[AppError | list[ChannelWithTeamData]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        body=body,
        system_console=system_console,
        boost=boost,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: SearchAllChannelsBody,
    system_console: bool | Unset = True,
    boost: bool | Unset = False,
) -> AppError | list[ChannelWithTeamData] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            system_console=system_console,
            boost=boost,
        )
    ).parsed
