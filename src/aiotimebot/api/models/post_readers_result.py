from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_reader_entry import PostReaderEntry


T = TypeVar("T", bound="PostReadersResult")


@_attrs_define
class PostReadersResult:
    """Generated Time Messenger API v4 model."""

    post_id: str | Unset = UNSET
    read_count: int | Unset = UNSET
    total_count: int | Unset = UNSET
    readers: list[PostReaderEntry] | Unset = UNSET
    non_readers: list[PostReaderEntry] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        read_count = self.read_count

        total_count = self.total_count

        readers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.readers, Unset):
            readers = []
            for readers_item_data in self.readers:
                readers_item = readers_item_data.to_dict()
                readers.append(readers_item)

        non_readers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.non_readers, Unset):
            non_readers = []
            for non_readers_item_data in self.non_readers:
                non_readers_item = non_readers_item_data.to_dict()
                non_readers.append(non_readers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if post_id is not UNSET:
            field_dict["post_id"] = post_id
        if read_count is not UNSET:
            field_dict["read_count"] = read_count
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if readers is not UNSET:
            field_dict["readers"] = readers
        if non_readers is not UNSET:
            field_dict["non_readers"] = non_readers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_reader_entry import PostReaderEntry

        d = dict(src_dict)
        post_id = d.pop("post_id", UNSET)

        read_count = d.pop("read_count", UNSET)

        total_count = d.pop("total_count", UNSET)

        _readers = d.pop("readers", UNSET)
        readers: list[PostReaderEntry] | Unset = UNSET
        if _readers is not UNSET:
            readers = []
            for readers_item_data in _readers:
                readers_item = PostReaderEntry.from_dict(readers_item_data)

                readers.append(readers_item)

        _non_readers = d.pop("non_readers", UNSET)
        non_readers: list[PostReaderEntry] | Unset = UNSET
        if _non_readers is not UNSET:
            non_readers = []
            for non_readers_item_data in _non_readers:
                non_readers_item = PostReaderEntry.from_dict(non_readers_item_data)

                non_readers.append(non_readers_item)

        post_readers_result = cls(
            post_id=post_id,
            read_count=read_count,
            total_count=total_count,
            readers=readers,
            non_readers=non_readers,
        )

        post_readers_result.additional_properties = d
        return post_readers_result

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
