from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    in_team: str | Unset = UNSET,
    not_in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    not_in_channel: str | Unset = UNSET,
    in_group: str | Unset = UNSET,
    group_constrained: bool | Unset = UNSET,
    without_team: bool | Unset = UNSET,
    active: bool | Unset = UNSET,
    inactive: bool | Unset = UNSET,
    role: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    roles: str | Unset = UNSET,
    channel_roles: str | Unset = UNSET,
    team_roles: str | Unset = UNSET,
    with_profiles: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["in_team"] = in_team

    params["not_in_team"] = not_in_team

    params["in_channel"] = in_channel

    params["not_in_channel"] = not_in_channel

    params["in_group"] = in_group

    params["group_constrained"] = group_constrained

    params["without_team"] = without_team

    params["active"] = active

    params["inactive"] = inactive

    params["role"] = role

    params["sort"] = sort

    params["roles"] = roles

    params["channel_roles"] = channel_roles

    params["team_roles"] = team_roles

    params["with_profiles"] = with_profiles

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[User] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = User.from_dict(response_200_item_data)

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
) -> Response[AppError | list[User]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    in_team: str | Unset = UNSET,
    not_in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    not_in_channel: str | Unset = UNSET,
    in_group: str | Unset = UNSET,
    group_constrained: bool | Unset = UNSET,
    without_team: bool | Unset = UNSET,
    active: bool | Unset = UNSET,
    inactive: bool | Unset = UNSET,
    role: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    roles: str | Unset = UNSET,
    channel_roles: str | Unset = UNSET,
    team_roles: str | Unset = UNSET,
    with_profiles: bool | Unset = False,
) -> Response[AppError | list[User]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        in_team=in_team,
        not_in_team=not_in_team,
        in_channel=in_channel,
        not_in_channel=not_in_channel,
        in_group=in_group,
        group_constrained=group_constrained,
        without_team=without_team,
        active=active,
        inactive=inactive,
        role=role,
        sort=sort,
        roles=roles,
        channel_roles=channel_roles,
        team_roles=team_roles,
        with_profiles=with_profiles,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    in_team: str | Unset = UNSET,
    not_in_team: str | Unset = UNSET,
    in_channel: str | Unset = UNSET,
    not_in_channel: str | Unset = UNSET,
    in_group: str | Unset = UNSET,
    group_constrained: bool | Unset = UNSET,
    without_team: bool | Unset = UNSET,
    active: bool | Unset = UNSET,
    inactive: bool | Unset = UNSET,
    role: str | Unset = UNSET,
    sort: str | Unset = UNSET,
    roles: str | Unset = UNSET,
    channel_roles: str | Unset = UNSET,
    team_roles: str | Unset = UNSET,
    with_profiles: bool | Unset = False,
) -> AppError | list[User] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            in_team=in_team,
            not_in_team=not_in_team,
            in_channel=in_channel,
            not_in_channel=not_in_channel,
            in_group=in_group,
            group_constrained=group_constrained,
            without_team=without_team,
            active=active,
            inactive=inactive,
            role=role,
            sort=sort,
            roles=roles,
            channel_roles=channel_roles,
            team_roles=team_roles,
            with_profiles=with_profiles,
        )
    ).parsed
