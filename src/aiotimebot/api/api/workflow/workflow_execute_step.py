from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.app_error import AppError
from ...models.workflow_execute_step_body import WorkflowExecuteStepBody
from ...models.workflow_execute_step_response_200 import WorkflowExecuteStepResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    workflow_id: str,
    action: str,
    step_id: str,
    *,
    body: WorkflowExecuteStepBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/plugins/ru.tinkoff.mm.workflow/{channel_id}/{workflow_id}/{action}/{step_id}".format(
            channel_id=quote(str(channel_id), safe=""),
            workflow_id=quote(str(workflow_id), safe=""),
            action=quote(str(action), safe=""),
            step_id=quote(str(step_id), safe=""),
        ),
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AppError | WorkflowExecuteStepResponse200 | None:
    if response.status_code == 200:
        response_200 = WorkflowExecuteStepResponse200.from_dict(response.json())

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

    if response.status_code == 501:
        response_501 = AppError.from_dict(response.json())

        return response_501

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppError | WorkflowExecuteStepResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )






async def asyncio_detailed(
    channel_id: str,
    workflow_id: str,
    action: str,
    step_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkflowExecuteStepBody | Unset = UNSET,
) -> Response[AppError | WorkflowExecuteStepResponse200]:
    """Call this Time Messenger API v4 operation asynchronously."""

    kwargs = _get_kwargs(
        channel_id=channel_id,
        workflow_id=workflow_id,
        action=action,
        step_id=step_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    workflow_id: str,
    action: str,
    step_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: WorkflowExecuteStepBody | Unset = UNSET,
) -> AppError | WorkflowExecuteStepResponse200 | None:
    """Call this Time Messenger API v4 operation asynchronously."""

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            workflow_id=workflow_id,
            action=action,
            step_id=step_id,
            client=client,
            body=body,
        )
    ).parsed
