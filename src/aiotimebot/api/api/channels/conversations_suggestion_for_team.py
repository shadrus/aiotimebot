from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.channel_suggestion import ChannelSuggestion
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    limit: int | Unset = 20,
    with_profiles: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["with_profiles"] = with_profiles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/teams/{team_id}/channels/conversations/suggestion".format(
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[ChannelSuggestion] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_channel_suggestion_list_item_data in _response_200:
            componentsschemas_channel_suggestion_list_item = (
                ChannelSuggestion.from_dict(
                    componentsschemas_channel_suggestion_list_item_data
                )
            )

            response_200.append(componentsschemas_channel_suggestion_list_item)

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
) -> Response[AppError | list[ChannelSuggestion]]:
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
    limit: int | Unset = 20,
    with_profiles: bool | Unset = False,
) -> Response[AppError | list[ChannelSuggestion]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        team_id=team_id,
        limit=limit,
        with_profiles=with_profiles,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    with_profiles: bool | Unset = False,
) -> AppError | list[ChannelSuggestion] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            limit=limit,
            with_profiles=with_profiles,
        )
    ).parsed
