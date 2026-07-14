from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.email_invite_with_error import EmailInviteWithError
from ...models.invite_guests_to_team_body import InviteGuestsToTeamBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    team_id: str,
    *,
    body: InviteGuestsToTeamBody,
    graceful: bool,
    dry_run: bool | Unset = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["graceful"] = graceful

    params["dry_run"] = dry_run

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/teams/{team_id}/invite-guests/email".format(
            team_id=quote(str(team_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | list[EmailInviteWithError] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_email_invite_with_error_list_item_data in _response_200:
            componentsschemas_email_invite_with_error_list_item = (
                EmailInviteWithError.from_dict(
                    componentsschemas_email_invite_with_error_list_item_data
                )
            )

            response_200.append(componentsschemas_email_invite_with_error_list_item)

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

    if response.status_code == 413:
        response_413 = AppError.from_dict(response.json())

        return response_413

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | list[EmailInviteWithError]]:
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
    body: InviteGuestsToTeamBody,
    graceful: bool,
    dry_run: bool | Unset = False,
) -> Response[AppError | list[EmailInviteWithError]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        team_id=team_id,
        body=body,
        graceful=graceful,
        dry_run=dry_run,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    team_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InviteGuestsToTeamBody,
    graceful: bool,
    dry_run: bool | Unset = False,
) -> AppError | list[EmailInviteWithError] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            team_id=team_id,
            client=client,
            body=body,
            graceful=graceful,
            dry_run=dry_run,
        )
    ).parsed
