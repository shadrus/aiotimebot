from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.notice import Notice
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    client_version: str,
    locale: str | Unset = UNSET,
    client_query: str,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["clientVersion"] = client_version

    params["locale"] = locale

    params["client"] = client_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/system/notices/{team_id}".format(
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[Notice] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Notice.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[AppError | list[Notice]]:
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
    client_version: str,
    locale: str | Unset = UNSET,
    client_query: str,
) -> Response[AppError | list[Notice]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        team_id=team_id,
        client_version=client_version,
        locale=locale,
        client_query=client_query,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    client_version: str,
    locale: str | Unset = UNSET,
    client_query: str,
) -> AppError | list[Notice] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            client_version=client_version,
            locale=locale,
            client_query=client_query,
        )
    ).parsed
