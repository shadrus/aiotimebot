from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.group_syncable_team import GroupSyncableTeam
from ...types import Response


def _get_kwargs(
    group_id: str,
    team_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/groups/{group_id}/teams/{team_id}/link".format(
            group_id=quote(str(group_id), safe=""),
            team_id=quote(str(team_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | GroupSyncableTeam | None:
    if response.status_code == 201:
        response_201 = GroupSyncableTeam.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AppError.from_dict(response.json())

        return response_403

    if response.status_code == 501:
        response_501 = AppError.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | GroupSyncableTeam]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    group_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppError | GroupSyncableTeam]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        group_id=group_id,
        team_id=team_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppError | GroupSyncableTeam | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            group_id=group_id,
            team_id=team_id,
            client=client,
        )
    ).parsed
