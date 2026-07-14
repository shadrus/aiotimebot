from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostSearchTerms")


@_attrs_define
class PostSearchTerms:
    """Generated Time Messenger API v4 model."""

    terms: str | Unset = UNSET
    excluded_terms: str | Unset = UNSET
    hashtags: str | Unset = UNSET
    excluded_hashtags: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        terms = self.terms

        excluded_terms = self.excluded_terms

        hashtags = self.hashtags

        excluded_hashtags = self.excluded_hashtags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terms is not UNSET:
            field_dict["terms"] = terms
        if excluded_terms is not UNSET:
            field_dict["excluded_terms"] = excluded_terms
        if hashtags is not UNSET:
            field_dict["hashtags"] = hashtags
        if excluded_hashtags is not UNSET:
            field_dict["excluded_hashtags"] = excluded_hashtags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        terms = d.pop("terms", UNSET)

        excluded_terms = d.pop("excluded_terms", UNSET)

        hashtags = d.pop("hashtags", UNSET)

        excluded_hashtags = d.pop("excluded_hashtags", UNSET)

        post_search_terms = cls(
            terms=terms,
            excluded_terms=excluded_terms,
            hashtags=hashtags,
            excluded_hashtags=excluded_hashtags,
        )

        post_search_terms.additional_properties = d
        return post_search_terms

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
