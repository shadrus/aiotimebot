from __future__ import annotations

import json

import httpx
import pytest

from aiotimebot.api.api.reactions import save_reaction
from aiotimebot.api.models.reaction import Reaction
from aiotimebot.client import TimeClient


@pytest.mark.parametrize("status_code", [200, 201])
async def test_save_reaction_accepts_time_success_statuses(status_code: int) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            status_code,
            json={
                "user_id": "user-1",
                "post_id": "post-1",
                "emoji_name": "white_check_mark",
                "create_at": 1,
            },
            request=request,
        )

    client = TimeClient(
        "https://time.example",
        "secret",
        transport=httpx.MockTransport(respond),
    )
    body = Reaction(
        user_id="user-1",
        post_id="post-1",
        emoji_name="white_check_mark",
        create_at=0,
    )

    async with client:
        result = await save_reaction.asyncio(client=client.api, body=body)

    assert isinstance(result, Reaction)
    assert result.post_id == "post-1"
    assert json.loads(requests[0].content) == body.to_dict()
