from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.reset_saml_auth_data_to_email_body import ResetSamlAuthDataToEmailBody
from ...models.reset_saml_auth_data_to_email_response_200 import (
    ResetSamlAuthDataToEmailResponse200,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ResetSamlAuthDataToEmailBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/saml/reset_auth_data",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | ResetSamlAuthDataToEmailResponse200 | None:
    if response.status_code == 200:
        response_200 = ResetSamlAuthDataToEmailResponse200.from_dict(response.json())

        return response_200

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
) -> Response[AppError | ResetSamlAuthDataToEmailResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ResetSamlAuthDataToEmailBody | Unset = UNSET,
) -> Response[AppError | ResetSamlAuthDataToEmailResponse200]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ResetSamlAuthDataToEmailBody | Unset = UNSET,
) -> AppError | ResetSamlAuthDataToEmailResponse200 | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
