from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.retention_policy_for_channel_list import RetentionPolicyForChannelList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/{user_id}/data_retention/channel_policies".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | RetentionPolicyForChannelList | None:
    if response.status_code == 200:
        response_200 = RetentionPolicyForChannelList.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AppError.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if response.status_code == 501:
        response_501 = AppError.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | RetentionPolicyForChannelList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
) -> Response[AppError | RetentionPolicyForChannelList]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        page=page,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
) -> AppError | RetentionPolicyForChannelList | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
