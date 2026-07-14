from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post import Post


T = TypeVar("T", bound="PostSearchResultsV2PostsItem")


@_attrs_define
class PostSearchResultsV2PostsItem:
    """Generated Time Messenger API v4 model."""

    post: Post | Unset = UNSET
    match: list[str] | Unset = UNSET
    highlight: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post, Unset):
            post = self.post.to_dict()

        match: list[str] | Unset = UNSET
        if not isinstance(self.match, Unset):
            match = self.match

        highlight: list[str] | Unset = UNSET
        if not isinstance(self.highlight, Unset):
            highlight = self.highlight

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post is not UNSET:
            field_dict["post"] = post
        if match is not UNSET:
            field_dict["match"] = match
        if highlight is not UNSET:
            field_dict["highlight"] = highlight

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post import Post

        d = dict(src_dict)
        _post = d.pop("post", UNSET)
        post: Post | Unset
        if isinstance(_post, Unset):
            post = UNSET
        else:
            post = Post.from_dict(_post)

        match = cast(list[str], d.pop("match", UNSET))

        highlight = cast(list[str], d.pop("highlight", UNSET))

        post_search_results_v2_posts_item = cls(
            post=post,
            match=match,
            highlight=highlight,
        )

        post_search_results_v2_posts_item.additional_properties = d
        return post_search_results_v2_posts_item

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
