from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.get_invite_brief_info_response_200 import GetInviteBriefInfoResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    t: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["t"] = t

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/teams/invite-info",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | GetInviteBriefInfoResponse200 | None:
    if response.status_code == 200:
        response_200 = GetInviteBriefInfoResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | GetInviteBriefInfoResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    t: str,
) -> Response[AppError | GetInviteBriefInfoResponse200]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        t=t,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    t: str,
) -> AppError | GetInviteBriefInfoResponse200 | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            t=t,
        )
    ).parsed
