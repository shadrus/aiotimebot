from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.regen_command_token_response_200 import RegenCommandTokenResponse200
from ...types import Response


def _get_kwargs(
    command_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v4/commands/{command_id}/regen_token".format(
            command_id=quote(str(command_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | RegenCommandTokenResponse200 | None:
    if response.status_code == 200:
        response_200 = RegenCommandTokenResponse200.from_dict(response.json())

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
) -> Response[AppError | RegenCommandTokenResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    command_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppError | RegenCommandTokenResponse200]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        command_id=command_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    command_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppError | RegenCommandTokenResponse200 | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            command_id=command_id,
            client=client,
        )
    ).parsed
