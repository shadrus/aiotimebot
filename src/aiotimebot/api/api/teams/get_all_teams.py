from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.get_all_teams_response_200_type_1 import GetAllTeamsResponse200Type1
from ...models.team import Team
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    include_total_count: bool | Unset = False,
    exclude_policy_constrained: bool | Unset = False,
    can_join: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["include_total_count"] = include_total_count

    params["exclude_policy_constrained"] = exclude_policy_constrained

    params["can_join"] = can_join

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v4/teams",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | GetAllTeamsResponse200Type1 | list[Team] | None:
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> GetAllTeamsResponse200Type1 | list[Team]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = []
                _response_200_type_0 = data
                for response_200_type_0_item_data in _response_200_type_0:
                    response_200_type_0_item = Team.from_dict(
                        response_200_type_0_item_data
                    )

                    response_200_type_0.append(response_200_type_0_item)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = GetAllTeamsResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AppError.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AppError.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | GetAllTeamsResponse200Type1 | list[Team]]:
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
    include_total_count: bool | Unset = False,
    exclude_policy_constrained: bool | Unset = False,
    can_join: bool | Unset = False,
) -> Response[AppError | GetAllTeamsResponse200Type1 | list[Team]]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        include_total_count=include_total_count,
        exclude_policy_constrained=exclude_policy_constrained,
        can_join=can_join,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    page: int | Unset = 0,
    per_page: int | Unset = 60,
    include_total_count: bool | Unset = False,
    exclude_policy_constrained: bool | Unset = False,
    can_join: bool | Unset = False,
) -> AppError | GetAllTeamsResponse200Type1 | list[Team] | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            include_total_count=include_total_count,
            exclude_policy_constrained=exclude_policy_constrained,
            can_join=can_join,
        )
    ).parsed
