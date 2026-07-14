from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.get_groups_associated_to_channels_by_team_response_200 import (
    GetGroupsAssociatedToChannelsByTeamResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    filter_allow_reference: bool | Unset = False,
    paginate: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["filter_allow_reference"] = filter_allow_reference

    params["paginate"] = paginate

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/teams/{team_id}/groups_by_channels".format(
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | GetGroupsAssociatedToChannelsByTeamResponse200 | None:
    if response.status_code == 200:
        response_200 = GetGroupsAssociatedToChannelsByTeamResponse200.from_dict(
            response.json()
        )

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
) -> Response[AppError | GetGroupsAssociatedToChannelsByTeamResponse200]:
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
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    filter_allow_reference: bool | Unset = False,
    paginate: bool | Unset = False,
) -> Response[AppError | GetGroupsAssociatedToChannelsByTeamResponse200]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        team_id=team_id,
        page=page,
        per_page=per_page,
        filter_allow_reference=filter_allow_reference,
        paginate=paginate,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    filter_allow_reference: bool | Unset = False,
    paginate: bool | Unset = False,
) -> AppError | GetGroupsAssociatedToChannelsByTeamResponse200 | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            page=page,
            per_page=per_page,
            filter_allow_reference=filter_allow_reference,
            paginate=paginate,
        )
    ).parsed
