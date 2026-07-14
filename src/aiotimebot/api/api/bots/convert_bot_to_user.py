from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.convert_bot_to_user_body import ConvertBotToUserBody
from ...models.status_ok import StatusOK
from ...types import UNSET, Response, Unset


def _get_kwargs(
    bot_user_id: str,
    *,
    body: ConvertBotToUserBody,
    set_system_admin: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["set_system_admin"] = set_system_admin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/bots/{bot_user_id}/convert_to_user".format(
            bot_user_id=quote(str(bot_user_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | StatusOK | None:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

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
) -> Response[AppError | StatusOK]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    bot_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConvertBotToUserBody,
    set_system_admin: bool | Unset = False,
) -> Response[AppError | StatusOK]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        body=body,
        set_system_admin=set_system_admin,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_user_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: ConvertBotToUserBody,
    set_system_admin: bool | Unset = False,
) -> AppError | StatusOK | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            bot_user_id=bot_user_id,
            client=client,
            body=body,
            set_system_admin=set_system_admin,
        )
    ).parsed
