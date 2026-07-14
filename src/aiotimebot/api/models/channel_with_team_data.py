from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.channel_type import ChannelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ChannelWithTeamData")


@_attrs_define
class ChannelWithTeamData:
    """Generated Time Messenger API v4 model."""

    id: str
    create_at: int
    update_at: int
    delete_at: int
    team_id: str
    type_: ChannelType
    display_name: str
    name: str
    header: str
    purpose: str
    last_post_at: int
    total_msg_count: int
    extra_update_at: int
    creator_id: str
    total_msg_count_root: int
    last_root_post_at: int
    read_receipts: bool | None | Unset = UNSET
    is_boosted: bool | Unset = UNSET
    team_display_name: str | Unset = UNSET
    team_name: str | Unset = UNSET
    team_update_at: int | Unset = UNSET
    policy_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        create_at = self.create_at

        update_at = self.update_at

        delete_at = self.delete_at

        team_id = self.team_id

        type_ = self.type_.value

        display_name = self.display_name

        name = self.name

        header = self.header

        purpose = self.purpose

        last_post_at = self.last_post_at

        total_msg_count = self.total_msg_count

        extra_update_at = self.extra_update_at

        creator_id = self.creator_id

        total_msg_count_root = self.total_msg_count_root

        last_root_post_at = self.last_root_post_at

        read_receipts: bool | None | Unset
        if isinstance(self.read_receipts, Unset):
            read_receipts = UNSET
        else:
            read_receipts = self.read_receipts

        is_boosted = self.is_boosted

        team_display_name = self.team_display_name

        team_name = self.team_name

        team_update_at = self.team_update_at

        policy_id = self.policy_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "create_at": create_at,
                "update_at": update_at,
                "delete_at": delete_at,
                "team_id": team_id,
                "type": type_,
                "display_name": display_name,
                "name": name,
                "header": header,
                "purpose": purpose,
                "last_post_at": last_post_at,
                "total_msg_count": total_msg_count,
                "extra_update_at": extra_update_at,
                "creator_id": creator_id,
                "total_msg_count_root": total_msg_count_root,
                "last_root_post_at": last_root_post_at,
            }
        )
        if read_receipts is not UNSET:
            field_dict["read_receipts"] = read_receipts
        if is_boosted is not UNSET:
            field_dict["isBoosted"] = is_boosted
        if team_display_name is not UNSET:
            field_dict["team_display_name"] = team_display_name
        if team_name is not UNSET:
            field_dict["team_name"] = team_name
        if team_update_at is not UNSET:
            field_dict["team_update_at"] = team_update_at
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        create_at = d.pop("create_at")

        update_at = d.pop("update_at")

        delete_at = d.pop("delete_at")

        team_id = d.pop("team_id")

        type_ = ChannelType(d.pop("type"))

        display_name = d.pop("display_name")

        name = d.pop("name")

        header = d.pop("header")

        purpose = d.pop("purpose")

        last_post_at = d.pop("last_post_at")

        total_msg_count = d.pop("total_msg_count")

        extra_update_at = d.pop("extra_update_at")

        creator_id = d.pop("creator_id")

        total_msg_count_root = d.pop("total_msg_count_root")

        last_root_post_at = d.pop("last_root_post_at")

        def _parse_read_receipts(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        read_receipts = _parse_read_receipts(d.pop("read_receipts", UNSET))

        is_boosted = d.pop("isBoosted", UNSET)

        team_display_name = d.pop("team_display_name", UNSET)

        team_name = d.pop("team_name", UNSET)

        team_update_at = d.pop("team_update_at", UNSET)

        policy_id = d.pop("policy_id", UNSET)

        channel_with_team_data = cls(
            id=id,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
            team_id=team_id,
            type_=type_,
            display_name=display_name,
            name=name,
            header=header,
            purpose=purpose,
            last_post_at=last_post_at,
            total_msg_count=total_msg_count,
            extra_update_at=extra_update_at,
            creator_id=creator_id,
            total_msg_count_root=total_msg_count_root,
            last_root_post_at=last_root_post_at,
            read_receipts=read_receipts,
            is_boosted=is_boosted,
            team_display_name=team_display_name,
            team_name=team_name,
            team_update_at=team_update_at,
            policy_id=policy_id,
        )

        channel_with_team_data.additional_properties = d
        return channel_with_team_data

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
