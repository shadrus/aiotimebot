from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.system_status_response import SystemStatusResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    get_server_status: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["get_server_status"] = get_server_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/system/ping",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> SystemStatusResponse | None:
    if response.status_code == 200:
        response_200 = SystemStatusResponse.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = SystemStatusResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[SystemStatusResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    get_server_status: str | Unset = UNSET,
) -> Response[SystemStatusResponse]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        get_server_status=get_server_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    get_server_status: str | Unset = UNSET,
) -> SystemStatusResponse | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            get_server_status=get_server_status,
        )
    ).parsed
