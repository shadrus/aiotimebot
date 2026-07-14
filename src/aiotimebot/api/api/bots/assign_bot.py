from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.bot import Bot
from ...types import Response


def _get_kwargs(
    bot_user_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/bots/{bot_user_id}/assign/{user_id}".format(
            bot_user_id=quote(str(bot_user_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | Bot | None:
    if response.status_code == 200:
        response_200 = Bot.from_dict(response.json())

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
) -> Response[AppError | Bot]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    bot_user_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[AppError | Bot]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        bot_user_id=bot_user_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    bot_user_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
) -> AppError | Bot | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            bot_user_id=bot_user_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
