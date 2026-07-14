from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_search_results_v2_posts_item import PostSearchResultsV2PostsItem


T = TypeVar("T", bound="PostSearchResultsV2")


@_attrs_define
class PostSearchResultsV2:
    """Generated Time Messenger API v4 model."""

    posts: list[PostSearchResultsV2PostsItem] | Unset = UNSET
    total: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        posts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.posts, Unset):
            posts = []
            for posts_item_data in self.posts:
                posts_item = posts_item_data.to_dict()
                posts.append(posts_item)

        total = self.total

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posts is not UNSET:
            field_dict["posts"] = posts
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_search_results_v2_posts_item import (
            PostSearchResultsV2PostsItem,
        )

        d = dict(src_dict)
        _posts = d.pop("posts", UNSET)
        posts: list[PostSearchResultsV2PostsItem] | Unset = UNSET
        if _posts is not UNSET:
            posts = []
            for posts_item_data in _posts:
                posts_item = PostSearchResultsV2PostsItem.from_dict(posts_item_data)

                posts.append(posts_item)

        total = d.pop("total", UNSET)

        post_search_results_v2 = cls(
            posts=posts,
            total=total,
        )

        post_search_results_v2.additional_properties = d
        return post_search_results_v2

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
