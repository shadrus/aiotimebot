from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_user_body_props import CreateUserBodyProps
    from ..models.timezone import Timezone
    from ..models.user_notify_props import UserNotifyProps


T = TypeVar("T", bound="CreateUserBody")


@_attrs_define
class CreateUserBody:
    """Generated Time Messenger API v4 model."""

    email: str
    username: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    nickname: str | Unset = UNSET
    auth_data: str | Unset = UNSET
    auth_service: str | Unset = UNSET
    email_verified: bool | Unset = UNSET
    password: str | Unset = UNSET
    locale: str | Unset = UNSET
    phone: str | Unset = UNSET
    position: str | Unset = UNSET
    timezone: Timezone | Unset = UNSET
    allow_marketing: bool | Unset = UNSET
    disable_welcome_email: bool | Unset = UNSET
    props: CreateUserBodyProps | Unset = UNSET
    notify_props: UserNotifyProps | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        nickname = self.nickname

        auth_data = self.auth_data

        auth_service = self.auth_service

        email_verified = self.email_verified

        password = self.password

        locale = self.locale

        phone = self.phone

        position = self.position

        timezone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.to_dict()

        allow_marketing = self.allow_marketing

        disable_welcome_email = self.disable_welcome_email

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        notify_props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notify_props, Unset):
            notify_props = self.notify_props.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "username": username,
            }
        )
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if auth_data is not UNSET:
            field_dict["auth_data"] = auth_data
        if auth_service is not UNSET:
            field_dict["auth_service"] = auth_service
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if password is not UNSET:
            field_dict["password"] = password
        if locale is not UNSET:
            field_dict["locale"] = locale
        if phone is not UNSET:
            field_dict["phone"] = phone
        if position is not UNSET:
            field_dict["position"] = position
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if allow_marketing is not UNSET:
            field_dict["allow_marketing"] = allow_marketing
        if disable_welcome_email is not UNSET:
            field_dict["disable_welcome_email"] = disable_welcome_email
        if props is not UNSET:
            field_dict["props"] = props
        if notify_props is not UNSET:
            field_dict["notify_props"] = notify_props

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_user_body_props import CreateUserBodyProps
        from ..models.timezone import Timezone
        from ..models.user_notify_props import UserNotifyProps

        d = dict(src_dict)
        email = d.pop("email")

        username = d.pop("username")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        nickname = d.pop("nickname", UNSET)

        auth_data = d.pop("auth_data", UNSET)

        auth_service = d.pop("auth_service", UNSET)

        email_verified = d.pop("email_verified", UNSET)

        password = d.pop("password", UNSET)

        locale = d.pop("locale", UNSET)

        phone = d.pop("phone", UNSET)

        position = d.pop("position", UNSET)

        _timezone = d.pop("timezone", UNSET)
        timezone: Timezone | Unset
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = Timezone.from_dict(_timezone)

        allow_marketing = d.pop("allow_marketing", UNSET)

        disable_welcome_email = d.pop("disable_welcome_email", UNSET)

        _props = d.pop("props", UNSET)
        props: CreateUserBodyProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = CreateUserBodyProps.from_dict(_props)

        _notify_props = d.pop("notify_props", UNSET)
        notify_props: UserNotifyProps | Unset
        if isinstance(_notify_props, Unset):
            notify_props = UNSET
        else:
            notify_props = UserNotifyProps.from_dict(_notify_props)

        create_user_body = cls(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            auth_data=auth_data,
            auth_service=auth_service,
            email_verified=email_verified,
            password=password,
            locale=locale,
            phone=phone,
            position=position,
            timezone=timezone,
            allow_marketing=allow_marketing,
            disable_welcome_email=disable_welcome_email,
            props=props,
            notify_props=notify_props,
        )

        create_user_body.additional_properties = d
        return create_user_body

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
