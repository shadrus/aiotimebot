from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.sidebar_category_with_channels import SidebarCategoryWithChannels
from ...types import Response


def _get_kwargs(
    user_id: str,
    team_id: str,
    category_id: str,
    *,
    body: SidebarCategoryWithChannels,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v4/users/{user_id}/teams/{team_id}/channels/categories/{category_id}".format(
            user_id=quote(str(user_id), safe=""),
            team_id=quote(str(team_id), safe=""),
            category_id=quote(str(category_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | SidebarCategoryWithChannels | None:
    if response.status_code == 200:
        response_200 = SidebarCategoryWithChannels.from_dict(response.json())

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
) -> Response[AppError | SidebarCategoryWithChannels]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    user_id: str,
    team_id: str,
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SidebarCategoryWithChannels,
) -> Response[AppError | SidebarCategoryWithChannels]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        category_id=category_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    category_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: SidebarCategoryWithChannels,
) -> AppError | SidebarCategoryWithChannels | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            category_id=category_id,
            client=client,
            body=body,
        )
    ).parsed
