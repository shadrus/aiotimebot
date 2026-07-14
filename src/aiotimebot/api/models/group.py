from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.group_source import GroupSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """
    Attributes:
        id (str):
        display_name (str):
        description (str):
        source (GroupSource):
        create_at (int):
        update_at (int):
        delete_at (int):
        has_syncables (bool):
        allow_reference (bool):
        name (str | Unset):
        remote_id (str | Unset):
        member_count (int | Unset):
    """

    id: str
    display_name: str
    description: str
    source: GroupSource
    create_at: int
    update_at: int
    delete_at: int
    has_syncables: bool
    allow_reference: bool
    name: str | Unset = UNSET
    remote_id: str | Unset = UNSET
    member_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        description = self.description

        source = self.source.value

        create_at = self.create_at

        update_at = self.update_at

        delete_at = self.delete_at

        has_syncables = self.has_syncables

        allow_reference = self.allow_reference

        name = self.name

        remote_id = self.remote_id

        member_count = self.member_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "display_name": display_name,
                "description": description,
                "source": source,
                "create_at": create_at,
                "update_at": update_at,
                "delete_at": delete_at,
                "has_syncables": has_syncables,
                "allow_reference": allow_reference,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if member_count is not UNSET:
            field_dict["member_count"] = member_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        description = d.pop("description")

        source = GroupSource(d.pop("source"))

        create_at = d.pop("create_at")

        update_at = d.pop("update_at")

        delete_at = d.pop("delete_at")

        has_syncables = d.pop("has_syncables")

        allow_reference = d.pop("allow_reference")

        name = d.pop("name", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        member_count = d.pop("member_count", UNSET)

        group = cls(
            id=id,
            display_name=display_name,
            description=description,
            source=source,
            create_at=create_at,
            update_at=update_at,
            delete_at=delete_at,
            has_syncables=has_syncables,
            allow_reference=allow_reference,
            name=name,
            remote_id=remote_id,
            member_count=member_count,
        )

        group.additional_properties = d
        return group

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
