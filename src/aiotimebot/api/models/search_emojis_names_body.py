from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchEmojisNamesBody")


@_attrs_define
class SearchEmojisNamesBody:
    """Generated Time Messenger API v4 model."""

    term: str
    limit: int | Unset = UNSET
    offset: int | Unset = UNSET
    category: str | Unset = UNSET
    skin_tone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        term = self.term

        limit = self.limit

        offset = self.offset

        category = self.category

        skin_tone = self.skin_tone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "term": term,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if category is not UNSET:
            field_dict["category"] = category
        if skin_tone is not UNSET:
            field_dict["skin_tone"] = skin_tone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        term = d.pop("term")

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        category = d.pop("category", UNSET)

        skin_tone = d.pop("skin_tone", UNSET)

        search_emojis_names_body = cls(
            term=term,
            limit=limit,
            offset=offset,
            category=category,
            skin_tone=skin_tone,
        )

        search_emojis_names_body.additional_properties = d
        return search_emojis_names_body

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
