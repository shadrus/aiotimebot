from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserThreadsStats")


@_attrs_define
class UserThreadsStats:
    """Generated Time Messenger API v4 model."""

    total_unread_mentions: int | Unset = UNSET
    has_unread_treads: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_unread_mentions = self.total_unread_mentions

        has_unread_treads = self.has_unread_treads

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_unread_mentions is not UNSET:
            field_dict["total_unread_mentions"] = total_unread_mentions
        if has_unread_treads is not UNSET:
            field_dict["has_unread_treads"] = has_unread_treads

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_unread_mentions = d.pop("total_unread_mentions", UNSET)

        has_unread_treads = d.pop("has_unread_treads", UNSET)

        user_threads_stats = cls(
            total_unread_mentions=total_unread_mentions,
            has_unread_treads=has_unread_treads,
        )

        user_threads_stats.additional_properties = d
        return user_threads_stats

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
