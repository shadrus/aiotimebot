from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.autocomplete_users_source import AutocompleteUsersSource
from ...models.user_autocomplete import UserAutocomplete
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    name: str,
    allow_inactive: bool | Unset = False,
    role: str | Unset = UNSET,
    is_bot: bool | Unset = UNSET,
    limit: int | Unset = 100,
    boost: bool | Unset = False,
    with_profiles: bool | Unset = False,
    source: AutocompleteUsersSource | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["in_team"] = in_team

    params["in_channel"] = in_channel

    params["name"] = name

    params["allow_inactive"] = allow_inactive

    params["role"] = role

    params["is_bot"] = is_bot

    params["limit"] = limit

    params["boost"] = boost

    params["with_profiles"] = with_profiles

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/autocomplete",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | UserAutocomplete | None:
    if response.status_code == 200:
        response_200 = UserAutocomplete.from_dict(response.json())

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
) -> Response[AppError | UserAutocomplete]:
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
    name: str,
    allow_inactive: bool | Unset = False,
    role: str | Unset = UNSET,
    is_bot: bool | Unset = UNSET,
    limit: int | Unset = 100,
    boost: bool | Unset = False,
    with_profiles: bool | Unset = False,
    source: AutocompleteUsersSource | Unset = UNSET,
) -> Response[AppError | UserAutocomplete]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        in_team=in_team,
        in_channel=in_channel,
        name=name,
        allow_inactive=allow_inactive,
        role=role,
        is_bot=is_bot,
        limit=limit,
        boost=boost,
        with_profiles=with_profiles,
        source=source,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    name: str,
    allow_inactive: bool | Unset = False,
    role: str | Unset = UNSET,
    is_bot: bool | Unset = UNSET,
    limit: int | Unset = 100,
    boost: bool | Unset = False,
    with_profiles: bool | Unset = False,
    source: AutocompleteUsersSource | Unset = UNSET,
) -> AppError | UserAutocomplete | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            in_team=in_team,
            in_channel=in_channel,
            name=name,
            allow_inactive=allow_inactive,
            role=role,
            is_bot=is_bot,
            limit=limit,
            boost=boost,
            with_profiles=with_profiles,
            source=source,
        )
    ).parsed
