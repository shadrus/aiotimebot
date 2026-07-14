from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post import Post


T = TypeVar("T", bound="ActivityFeedItemsItemItem")


@_attrs_define
class ActivityFeedItemsItemItem:
    """Generated Time Messenger API v4 model."""

    team_id: str | Unset = UNSET
    post: Post | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        team_id = self.team_id

        post: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if post is not UNSET:
            field_dict["post"] = post

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post import Post

        d = dict(src_dict)
        team_id = d.pop("team_id", UNSET)

        _post = d.pop("post", UNSET)
        post: Post | Unset
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = Post.from_dict(_post)

        activity_feed_items_item_item = cls(
            team_id=team_id,
            post=post,
        )

        activity_feed_items_item_item.additional_properties = d
        return activity_feed_items_item_item

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
