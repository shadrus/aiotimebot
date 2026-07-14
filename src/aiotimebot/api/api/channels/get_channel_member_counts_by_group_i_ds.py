from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.channel_member_count_by_group import ChannelMemberCountByGroup
from ...models.get_channel_member_counts_by_group_i_ds_body import (
    GetChannelMemberCountsByGroupIDsBody,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    body: GetChannelMemberCountsByGroupIDsBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/channels/{channel_id}/groups/members/counts".format(
            channel_id=quote(str(channel_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[ChannelMemberCountByGroup] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ChannelMemberCountByGroup.from_dict(
                response_200_item_data
            )

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
) -> Response[AppError | list[ChannelMemberCountByGroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GetChannelMemberCountsByGroupIDsBody | Unset = UNSET,
) -> Response[AppError | list[ChannelMemberCountByGroup]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        channel_id=channel_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: GetChannelMemberCountsByGroupIDsBody | Unset = UNSET,
) -> AppError | list[ChannelMemberCountByGroup] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            body=body,
        )
    ).parsed
