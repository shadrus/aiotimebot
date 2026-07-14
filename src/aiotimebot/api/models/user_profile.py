from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserProfile")


@_attrs_define
class UserProfile:
    """Generated Time Messenger API v4 model."""

    user_id: str
    hide_additional_contact: bool
    hide_schedule: bool
    birthday: str
    phone: str | Unset = UNSET
    is_public_phone: bool | Unset = UNSET
    additional_contact_name: str | Unset = UNSET
    additional_contact: str | Unset = UNSET
    schedule: str | Unset = UNSET
    work_place: str | Unset = UNSET
    work_scheme: str | Unset = UNSET
    department: str | Unset = UNSET
    position: str | Unset = UNSET
    profile_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        hide_additional_contact = self.hide_additional_contact

        hide_schedule = self.hide_schedule

        birthday = self.birthday

        phone = self.phone

        is_public_phone = self.is_public_phone

        additional_contact_name = self.additional_contact_name

        additional_contact = self.additional_contact

        schedule = self.schedule

        work_place = self.work_place

        work_scheme = self.work_scheme

        department = self.department

        position = self.position

        profile_url = self.profile_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "hide_additional_contact": hide_additional_contact,
                "hide_schedule": hide_schedule,
                "birthday": birthday,
            }
        )
        if phone is not UNSET:
            field_dict["phone"] = phone
        if is_public_phone is not UNSET:
            field_dict["is_public_phone"] = is_public_phone
        if additional_contact_name is not UNSET:
            field_dict["additional_contact_name"] = additional_contact_name
        if additional_contact is not UNSET:
            field_dict["additional_contact"] = additional_contact
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if work_place is not UNSET:
            field_dict["work_place"] = work_place
        if work_scheme is not UNSET:
            field_dict["work_scheme"] = work_scheme
        if department is not UNSET:
            field_dict["department"] = department
        if position is not UNSET:
            field_dict["position"] = position
        if profile_url is not UNSET:
            field_dict["profile_url"] = profile_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id")

        hide_additional_contact = d.pop("hide_additional_contact")

        hide_schedule = d.pop("hide_schedule")

        birthday = d.pop("birthday")

        phone = d.pop("phone", UNSET)

        is_public_phone = d.pop("is_public_phone", UNSET)

        additional_contact_name = d.pop("additional_contact_name", UNSET)

        additional_contact = d.pop("additional_contact", UNSET)

        schedule = d.pop("schedule", UNSET)

        work_place = d.pop("work_place", UNSET)

        work_scheme = d.pop("work_scheme", UNSET)

        department = d.pop("department", UNSET)

        position = d.pop("position", UNSET)

        profile_url = d.pop("profile_url", UNSET)

        user_profile = cls(
            user_id=user_id,
            hide_additional_contact=hide_additional_contact,
            hide_schedule=hide_schedule,
            birthday=birthday,
            phone=phone,
            is_public_phone=is_public_phone,
            additional_contact_name=additional_contact_name,
            additional_contact=additional_contact,
            schedule=schedule,
            work_place=work_place,
            work_scheme=work_scheme,
            department=department,
            position=position,
            profile_url=profile_url,
        )

        user_profile.additional_properties = d
        return user_profile

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
