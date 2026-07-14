from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.post_list_posts import PostListPosts


T = TypeVar("T", bound="PostList")


@_attrs_define
class PostList:
    """Generated Time Messenger API v4 model."""

    order: list[str]
    posts: PostListPosts
    next_post_id: str
    prev_post_id: str
    has_next: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order = self.order

        posts = self.posts.to_dict()

        next_post_id = self.next_post_id

        prev_post_id = self.prev_post_id

        has_next = self.has_next

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "order": order,
                "posts": posts,
                "next_post_id": next_post_id,
                "prev_post_id": prev_post_id,
                "has_next": has_next,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_list_posts import PostListPosts

        d = dict(src_dict)
        order = cast(list[str], d.pop("order"))

        posts = PostListPosts.from_dict(d.pop("posts"))

        next_post_id = d.pop("next_post_id")

        prev_post_id = d.pop("prev_post_id")

        has_next = d.pop("has_next")

        post_list = cls(
            order=order,
            posts=posts,
            next_post_id=next_post_id,
            prev_post_id=prev_post_id,
            has_next=has_next,
        )

        post_list.additional_properties = d
        return post_list

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
