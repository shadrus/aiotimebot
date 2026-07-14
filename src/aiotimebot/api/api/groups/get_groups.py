from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.group import Group
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    q: str | Unset = UNSET,
    include_member_count: bool | Unset = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: int | Unset = UNSET,
    filter_allow_reference: bool | Unset = False,
    archived: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["q"] = q

    params["include_member_count"] = include_member_count

    params["not_associated_to_team"] = not_associated_to_team

    params["not_associated_to_channel"] = not_associated_to_channel

    params["since"] = since

    params["filter_allow_reference"] = filter_allow_reference

    params["archived"] = archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[Group] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Group.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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

    if response.status_code == 501:
        response_501 = AppError.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | list[Group]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    q: str | Unset = UNSET,
    include_member_count: bool | Unset = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: int | Unset = UNSET,
    filter_allow_reference: bool | Unset = False,
    archived: bool | Unset = UNSET,
) -> Response[AppError | list[Group]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        q=q,
        include_member_count=include_member_count,
        not_associated_to_team=not_associated_to_team,
        not_associated_to_channel=not_associated_to_channel,
        since=since,
        filter_allow_reference=filter_allow_reference,
        archived=archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    q: str | Unset = UNSET,
    include_member_count: bool | Unset = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: int | Unset = UNSET,
    filter_allow_reference: bool | Unset = False,
    archived: bool | Unset = UNSET,
) -> AppError | list[Group] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            include_member_count=include_member_count,
            not_associated_to_team=not_associated_to_team,
            not_associated_to_channel=not_associated_to_channel,
            since=since,
            filter_allow_reference=filter_allow_reference,
            archived=archived,
        )
    ).parsed
