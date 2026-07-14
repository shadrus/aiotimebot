from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    team_id: str,
    application_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/teams/{team_id}/applications/{application_id}/install".format(
            team_id=quote(str(team_id), safe=""),
            application_id=quote(str(application_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | StatusOK | None:
    if response.status_code == 201:
        response_201 = StatusOK.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | StatusOK]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    team_id: str,
    application_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppError | StatusOK]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        team_id=team_id,
        application_id=application_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    application_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppError | StatusOK | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            team_id=team_id,
            application_id=application_id,
            client=client,
        )
    ).parsed
