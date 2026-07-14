from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.regen_application_token_response_200_type_0 import (
    RegenApplicationTokenResponse200Type0,
)
from ...models.regen_application_token_response_200_type_1 import (
    RegenApplicationTokenResponse200Type1,
)
from ...models.regen_application_token_token_type import RegenApplicationTokenTokenType
from ...types import Response


def _get_kwargs(
    application_id: str,
    token_type: RegenApplicationTokenTokenType,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v4/applications/{application_id}/regen_token/{token_type}".format(
            application_id=quote(str(application_id), safe=""),
            token_type=quote(str(token_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AppError
    | RegenApplicationTokenResponse200Type0
    | RegenApplicationTokenResponse200Type1
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            RegenApplicationTokenResponse200Type0
            | RegenApplicationTokenResponse200Type1
        ):
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RegenApplicationTokenResponse200Type0.from_dict(
                    data
                )

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = RegenApplicationTokenResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

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

    if response.status_code == 500:
        response_500 = AppError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AppError
    | RegenApplicationTokenResponse200Type0
    | RegenApplicationTokenResponse200Type1
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    application_id: str,
    token_type: RegenApplicationTokenTokenType,
    *,
    client: AuthenticatedClient | Client,
) -> Response[
    AppError
    | RegenApplicationTokenResponse200Type0
    | RegenApplicationTokenResponse200Type1
]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        application_id=application_id,
        token_type=token_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    application_id: str,
    token_type: RegenApplicationTokenTokenType,
    *,
    client: AuthenticatedClient | Client,
) -> (
    AppError
    | RegenApplicationTokenResponse200Type0
    | RegenApplicationTokenResponse200Type1
    | None
):
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            application_id=application_id,
            token_type=token_type,
            client=client,
        )
    ).parsed
