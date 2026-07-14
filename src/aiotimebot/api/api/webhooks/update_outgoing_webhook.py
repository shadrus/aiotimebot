from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.outgoing_webhook import OutgoingWebhook
from ...models.update_outgoing_webhook_body import UpdateOutgoingWebhookBody
from ...types import Response


def _get_kwargs(
    hook_id: str,
    *,
    body: UpdateOutgoingWebhookBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v4/hooks/outgoing/{hook_id}".format(
            hook_id=quote(str(hook_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | OutgoingWebhook | None:
    if response.status_code == 200:
        response_200 = OutgoingWebhook.from_dict(response.json())

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
) -> Response[AppError | OutgoingWebhook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    hook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOutgoingWebhookBody,
) -> Response[AppError | OutgoingWebhook]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        hook_id=hook_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hook_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateOutgoingWebhookBody,
) -> AppError | OutgoingWebhook | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            hook_id=hook_id,
            client=client,
            body=body,
        )
    ).parsed
