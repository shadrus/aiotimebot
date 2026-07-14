from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.user_threads import UserThreads
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    page_size: int | Unset = UNSET,
    extended: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    since: int | Unset = UNSET,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    unread: bool | Unset = UNSET,
    skip_total: bool | Unset = UNSET,
    totals_only: bool | Unset = UNSET,
    threads_only: bool | Unset = UNSET,
    team_only: bool | Unset = UNSET,
    disable_channel_type_group: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["pageSize"] = page_size

    params["extended"] = extended

    params["deleted"] = deleted

    params["since"] = since

    params["before"] = before

    params["after"] = after

    params["unread"] = unread

    params["skipTotal"] = skip_total

    params["totalsOnly"] = totals_only

    params["threadsOnly"] = threads_only

    params["teamOnly"] = team_only

    params["disable_channel_type_group"] = disable_channel_type_group

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/users/{user_id}/teams/{team_id}/threads".format(
            user_id=quote(str(user_id), safe=""),
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | UserThreads | None:
    if response.status_code == 200:
        response_200 = UserThreads.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = AppError.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | UserThreads]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    user_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    extended: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    since: int | Unset = UNSET,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    unread: bool | Unset = UNSET,
    skip_total: bool | Unset = UNSET,
    totals_only: bool | Unset = UNSET,
    threads_only: bool | Unset = UNSET,
    team_only: bool | Unset = UNSET,
    disable_channel_type_group: bool | Unset = UNSET,
) -> Response[AppError | UserThreads]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        page_size=page_size,
        extended=extended,
        deleted=deleted,
        since=since,
        before=before,
        after=after,
        unread=unread,
        skip_total=skip_total,
        totals_only=totals_only,
        threads_only=threads_only,
        team_only=team_only,
        disable_channel_type_group=disable_channel_type_group,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    page_size: int | Unset = UNSET,
    extended: bool | Unset = UNSET,
    deleted: bool | Unset = UNSET,
    since: int | Unset = UNSET,
    before: str | Unset = UNSET,
    after: str | Unset = UNSET,
    unread: bool | Unset = UNSET,
    skip_total: bool | Unset = UNSET,
    totals_only: bool | Unset = UNSET,
    threads_only: bool | Unset = UNSET,
    team_only: bool | Unset = UNSET,
    disable_channel_type_group: bool | Unset = UNSET,
) -> AppError | UserThreads | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            client=client,
            page_size=page_size,
            extended=extended,
            deleted=deleted,
            since=since,
            before=before,
            after=after,
            unread=unread,
            skip_total=skip_total,
            totals_only=totals_only,
            threads_only=threads_only,
            team_only=team_only,
            disable_channel_type_group=disable_channel_type_group,
        )
    ).parsed
