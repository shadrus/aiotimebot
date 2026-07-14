from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type import ChannelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post import Post


T = TypeVar("T", bound="PostEmbedData")


@_attrs_define
class PostEmbedData:
    """
    Attributes:
        post_id (str | Unset):
        post (Post | Unset):
        team_name (str | Unset):
        channel_display_name (str | Unset):
        channel_type (ChannelType | Unset):
        channel_id (str | Unset):
    """

    post_id: str | Unset = UNSET
    post: Post | Unset = UNSET
    team_name: str | Unset = UNSET
    channel_display_name: str | Unset = UNSET
    channel_type: ChannelType | Unset = UNSET
    channel_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        post: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        team_name = self.team_name

        channel_display_name = self.channel_display_name

        channel_type: str | Unset = UNSET
        if not isinstance(self.channel_type, Unset):
            channel_type = self.channel_type.value

        channel_id = self.channel_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if post is not UNSET:
            field_dict["post"] = post
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if channel_display_name is not UNSET:
            field_dict["channel_display_name"] = channel_display_name
        if channel_type is not UNSET:
            field_dict["channel_type"] = channel_type
        if channel_id is not UNSET:
            field_dict["channel_id"] = channel_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post import Post

        d = dict(src_dict)
        post_id = d.pop("post_id", UNSET)

        _post = d.pop("post", UNSET)
        post: Post | Unset
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = Post.from_dict(_post)

        team_name = d.pop("team_name", UNSET)

        channel_display_name = d.pop("channel_display_name", UNSET)

        _channel_type = d.pop("channel_type", UNSET)
        channel_type: ChannelType | Unset
        if isinstance(_channel_type, Unset):
            channel_type = UNSET
        else:
            channel_type = ChannelType(_channel_type)

        channel_id = d.pop("channel_id", UNSET)

        post_embed_data = cls(
            post_id=post_id,
            post=post,
            team_name=team_name,
            channel_display_name=channel_display_name,
            channel_type=channel_type,
            channel_id=channel_id,
        )

        post_embed_data.additional_properties = d
        return post_embed_data

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
