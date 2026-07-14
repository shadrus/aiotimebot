from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_thread import UserThread


T = TypeVar("T", bound="UserThreads")


@_attrs_define
class UserThreads:
    """Generated Time Messenger API v4 model."""

    total: int
    total_unread_threads: int
    unread_threads_o_channel: int
    unread_threads_p_channel: int
    unread_threads_d_channel: int
    unread_threads_g_channel: int
    total_unread_mentions: int
    unread_mentions_o_channel: int
    unread_mentions_p_channel: int
    unread_mentions_d_channel: int
    unread_mentions_g_channel: int
    threads: list[UserThread]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        total_unread_threads = self.total_unread_threads

        unread_threads_o_channel = self.unread_threads_o_channel

        unread_threads_p_channel = self.unread_threads_p_channel

        unread_threads_d_channel = self.unread_threads_d_channel

        unread_threads_g_channel = self.unread_threads_g_channel

        total_unread_mentions = self.total_unread_mentions

        unread_mentions_o_channel = self.unread_mentions_o_channel

        unread_mentions_p_channel = self.unread_mentions_p_channel

        unread_mentions_d_channel = self.unread_mentions_d_channel

        unread_mentions_g_channel = self.unread_mentions_g_channel

        threads = []
        for threads_item_data in self.threads:
            threads_item = threads_item_data.to_dict()
            threads.append(threads_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "total_unread_threads": total_unread_threads,
                "unread_threads_o_channel": unread_threads_o_channel,
                "unread_threads_p_channel": unread_threads_p_channel,
                "unread_threads_d_channel": unread_threads_d_channel,
                "unread_threads_g_channel": unread_threads_g_channel,
                "total_unread_mentions": total_unread_mentions,
                "unread_mentions_o_channel": unread_mentions_o_channel,
                "unread_mentions_p_channel": unread_mentions_p_channel,
                "unread_mentions_d_channel": unread_mentions_d_channel,
                "unread_mentions_g_channel": unread_mentions_g_channel,
                "threads": threads,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_thread import UserThread

        d = dict(src_dict)
        total = d.pop("total")

        total_unread_threads = d.pop("total_unread_threads")

        unread_threads_o_channel = d.pop("unread_threads_o_channel")

        unread_threads_p_channel = d.pop("unread_threads_p_channel")

        unread_threads_d_channel = d.pop("unread_threads_d_channel")

        unread_threads_g_channel = d.pop("unread_threads_g_channel")

        total_unread_mentions = d.pop("total_unread_mentions")

        unread_mentions_o_channel = d.pop("unread_mentions_o_channel")

        unread_mentions_p_channel = d.pop("unread_mentions_p_channel")

        unread_mentions_d_channel = d.pop("unread_mentions_d_channel")

        unread_mentions_g_channel = d.pop("unread_mentions_g_channel")

        threads = []
        _threads = d.pop("threads")
        for threads_item_data in _threads:
            threads_item = UserThread.from_dict(threads_item_data)

            threads.append(threads_item)

        user_threads = cls(
            total=total,
            total_unread_threads=total_unread_threads,
            unread_threads_o_channel=unread_threads_o_channel,
            unread_threads_p_channel=unread_threads_p_channel,
            unread_threads_d_channel=unread_threads_d_channel,
            unread_threads_g_channel=unread_threads_g_channel,
            total_unread_mentions=total_unread_mentions,
            unread_mentions_o_channel=unread_mentions_o_channel,
            unread_mentions_p_channel=unread_mentions_p_channel,
            unread_mentions_d_channel=unread_mentions_d_channel,
            unread_mentions_g_channel=unread_mentions_g_channel,
            threads=threads,
        )

        user_threads.additional_properties = d
        return user_threads

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
