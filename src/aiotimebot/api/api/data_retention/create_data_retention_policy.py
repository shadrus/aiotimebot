from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.data_retention_policy_with_team_and_channel_counts import (
    DataRetentionPolicyWithTeamAndChannelCounts,
)
from ...models.data_retention_policy_with_team_and_channel_ids import (
    DataRetentionPolicyWithTeamAndChannelIds,
)
from ...types import Response


def _get_kwargs(
    *,
    body: DataRetentionPolicyWithTeamAndChannelIds,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/data_retention/policies",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | DataRetentionPolicyWithTeamAndChannelCounts | None:
    if response.status_code == 201:
        response_201 = DataRetentionPolicyWithTeamAndChannelCounts.from_dict(
            response.json()
        )

        return response_201

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
) -> Response[AppError | DataRetentionPolicyWithTeamAndChannelCounts]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: DataRetentionPolicyWithTeamAndChannelIds,
) -> Response[AppError | DataRetentionPolicyWithTeamAndChannelCounts]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: DataRetentionPolicyWithTeamAndChannelIds,
) -> AppError | DataRetentionPolicyWithTeamAndChannelCounts | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
