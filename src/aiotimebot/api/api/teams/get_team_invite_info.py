from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.get_team_invite_info_response_200 import GetTeamInviteInfoResponse200
from ...types import Response


def _get_kwargs(
    invite_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/teams/invite/{invite_id}".format(
            invite_id=quote(str(invite_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | GetTeamInviteInfoResponse200 | None:
    if response.status_code == 200:
        response_200 = GetTeamInviteInfoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | GetTeamInviteInfoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    invite_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppError | GetTeamInviteInfoResponse200]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        invite_id=invite_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invite_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppError | GetTeamInviteInfoResponse200 | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            invite_id=invite_id,
            client=client,
        )
    ).parsed
