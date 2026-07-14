from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_feed import ActivityFeed
from ...models.app_error import AppError
from ...models.get_activity_feed_sort_by import GetActivityFeedSortBy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    limit: int | Unset = 20,
    sort_by: GetActivityFeedSortBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_sort_by: str | Unset = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by.value

    params["sort_by"] = json_sort_by

    params["page_token"] = page_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/{user_id}/sidebar/activity".format(
            user_id=quote(str(user_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivityFeed | AppError | None:
    if response.status_code == 200:
        response_200 = ActivityFeed.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ActivityFeed | AppError]:
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
    limit: int | Unset = 20,
    sort_by: GetActivityFeedSortBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> Response[ActivityFeed | AppError]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        limit=limit,
        sort_by=sort_by,
        page_token=page_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 20,
    sort_by: GetActivityFeedSortBy | Unset = UNSET,
    page_token: str | Unset = UNSET,
) -> ActivityFeed | AppError | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            limit=limit,
            sort_by=sort_by,
            page_token=page_token,
        )
    ).parsed
