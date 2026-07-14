from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_channel_member import AddChannelMember
    from ..models.post_props_channel_mentions import PostPropsChannelMentions
    from ..models.slack_attachment import SlackAttachment


T = TypeVar("T", bound="PostProps")


@_attrs_define
class PostProps:
    """
    Attributes:
        attachments (list[SlackAttachment] | Unset):
        channel_mentions (PostPropsChannelMentions | Unset):
        previewed_post (str | Unset):
        quote_post_id (str | Unset):
        team_id (str | Unset):
        from_bot (str | Unset):
        from_plugin (str | Unset):
        from_webhook (str | Unset):
        add_channel_member (AddChannelMember | Unset):
    """

    attachments: list[SlackAttachment] | Unset = UNSET
    channel_mentions: PostPropsChannelMentions | Unset = UNSET
    previewed_post: str | Unset = UNSET
    quote_post_id: str | Unset = UNSET
    team_id: str | Unset = UNSET
    from_bot: str | Unset = UNSET
    from_plugin: str | Unset = UNSET
    from_webhook: str | Unset = UNSET
    add_channel_member: AddChannelMember | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        channel_mentions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.channel_mentions, Unset):
            channel_mentions = self.channel_mentions.to_dict()

        previewed_post = self.previewed_post

        quote_post_id = self.quote_post_id

        team_id = self.team_id

        from_bot = self.from_bot

        from_plugin = self.from_plugin

        from_webhook = self.from_webhook

        add_channel_member: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_channel_member, Unset):
            add_channel_member = self.add_channel_member.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if channel_mentions is not UNSET:
            field_dict["channel_mentions"] = channel_mentions
        if previewed_post is not UNSET:
            field_dict["previewed_post"] = previewed_post
        if quote_post_id is not UNSET:
            field_dict["quote_post_id"] = quote_post_id
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if from_bot is not UNSET:
            field_dict["from_bot"] = from_bot
        if from_plugin is not UNSET:
            field_dict["from_plugin"] = from_plugin
        if from_webhook is not UNSET:
            field_dict["from_webhook"] = from_webhook
        if add_channel_member is not UNSET:
            field_dict["add_channel_member"] = add_channel_member

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_channel_member import AddChannelMember
        from ..models.post_props_channel_mentions import PostPropsChannelMentions
        from ..models.slack_attachment import SlackAttachment

        d = dict(src_dict)
        _attachments = d.pop("attachments", UNSET)
        attachments: list[SlackAttachment] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = SlackAttachment.from_dict(attachments_item_data)

                attachments.append(attachments_item)

        _channel_mentions = d.pop("channel_mentions", UNSET)
        channel_mentions: PostPropsChannelMentions | Unset
        if isinstance(_channel_mentions, Unset):
            channel_mentions = UNSET
        else:
            channel_mentions = PostPropsChannelMentions.from_dict(_channel_mentions)

        previewed_post = d.pop("previewed_post", UNSET)

        quote_post_id = d.pop("quote_post_id", UNSET)

        team_id = d.pop("team_id", UNSET)

        from_bot = d.pop("from_bot", UNSET)

        from_plugin = d.pop("from_plugin", UNSET)

        from_webhook = d.pop("from_webhook", UNSET)

        _add_channel_member = d.pop("add_channel_member", UNSET)
        add_channel_member: AddChannelMember | Unset
        if isinstance(_add_channel_member, Unset):
            add_channel_member = UNSET
        else:
            add_channel_member = AddChannelMember.from_dict(_add_channel_member)

        post_props = cls(
            attachments=attachments,
            channel_mentions=channel_mentions,
            previewed_post=previewed_post,
            quote_post_id=quote_post_id,
            team_id=team_id,
            from_bot=from_bot,
            from_plugin=from_plugin,
            from_webhook=from_webhook,
            add_channel_member=add_channel_member,
        )

        post_props.additional_properties = d
        return post_props

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
