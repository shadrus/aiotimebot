from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sidebar_category_sorting import SidebarCategorySorting
from ..models.sidebar_category_type import SidebarCategoryType

T = TypeVar("T", bound="SidebarCategoryWithChannels")


@_attrs_define
class SidebarCategoryWithChannels:
    """Generated Time Messenger API v4 model."""

    id: str
    user_id: str
    team_id: str
    sort_order: int
    sorting: SidebarCategorySorting
    type_: SidebarCategoryType
    display_name: str
    muted: bool
    collapsed: bool
    channel_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        team_id = self.team_id

        sort_order = self.sort_order

        sorting = self.sorting.value

        type_ = self.type_.value

        display_name = self.display_name

        muted = self.muted

        collapsed = self.collapsed

        channel_ids = self.channel_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "team_id": team_id,
                "sort_order": sort_order,
                "sorting": sorting,
                "type": type_,
                "display_name": display_name,
                "muted": muted,
                "collapsed": collapsed,
                "channel_ids": channel_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        user_id = d.pop("user_id")

        team_id = d.pop("team_id")

        sort_order = d.pop("sort_order")

        sorting = SidebarCategorySorting(d.pop("sorting"))

        type_ = SidebarCategoryType(d.pop("type"))

        display_name = d.pop("display_name")

        muted = d.pop("muted")

        collapsed = d.pop("collapsed")

        channel_ids = cast(list[str], d.pop("channel_ids"))

        sidebar_category_with_channels = cls(
            id=id,
            user_id=user_id,
            team_id=team_id,
            sort_order=sort_order,
            sorting=sorting,
            type_=type_,
            display_name=display_name,
            muted=muted,
            collapsed=collapsed,
            channel_ids=channel_ids,
        )

        sidebar_category_with_channels.additional_properties = d
        return sidebar_category_with_channels

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
