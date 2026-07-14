from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddChannelMember")


@_attrs_define
class AddChannelMember:
    """
    Attributes:
        post_id (str):
        not_in_channel_user_ids (list[str]):
        not_in_channel_usernames (list[str]):
        not_in_groups_usernames (list[str]):
        not_in_groups_user_ids (list[str]):
    """

    post_id: str
    not_in_channel_user_ids: list[str]
    not_in_channel_usernames: list[str]
    not_in_groups_usernames: list[str]
    not_in_groups_user_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        post_id = self.post_id

        not_in_channel_user_ids = self.not_in_channel_user_ids

        not_in_channel_usernames = self.not_in_channel_usernames

        not_in_groups_usernames = self.not_in_groups_usernames

        not_in_groups_user_ids = self.not_in_groups_user_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "post_id": post_id,
                "not_in_channel_user_ids": not_in_channel_user_ids,
                "not_in_channel_usernames": not_in_channel_usernames,
                "not_in_groups_usernames": not_in_groups_usernames,
                "not_in_groups_user_ids": not_in_groups_user_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        post_id = d.pop("post_id")

        not_in_channel_user_ids = cast(list[str], d.pop("not_in_channel_user_ids"))

        not_in_channel_usernames = cast(list[str], d.pop("not_in_channel_usernames"))

        not_in_groups_usernames = cast(list[str], d.pop("not_in_groups_usernames"))

        not_in_groups_user_ids = cast(list[str], d.pop("not_in_groups_user_ids"))

        add_channel_member = cls(
            post_id=post_id,
            not_in_channel_user_ids=not_in_channel_user_ids,
            not_in_channel_usernames=not_in_channel_usernames,
            not_in_groups_usernames=not_in_groups_usernames,
            not_in_groups_user_ids=not_in_groups_user_ids,
        )

        add_channel_member.additional_properties = d
        return add_channel_member

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
