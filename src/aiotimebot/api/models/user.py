from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timezone import Timezone
    from ..models.user_notify_props import UserNotifyProps
    from ..models.user_profile import UserProfile
    from ..models.user_props import UserProps


T = TypeVar("T", bound="User")


@_attrs_define
class User:
    """Generated Time Messenger API v4 model."""

    id: str
    delete_at: int
    username: str
    first_name: str
    last_name: str
    nickname: str
    email: str
    auth_service: str
    roles: str
    locale: str
    position: str
    create_at: int | Unset = UNSET
    update_at: int | Unset = UNSET
    phone: str | Unset = UNSET
    email_verified: bool | Unset = UNSET
    notify_props: UserNotifyProps | Unset = UNSET
    props: UserProps | Unset = UNSET
    last_password_update: int | Unset = UNSET
    last_picture_update: int | Unset = UNSET
    failed_attempts: int | Unset = UNSET
    mfa_active: bool | Unset = UNSET
    timezone: Timezone | Unset = UNSET
    terms_of_service_id: str | Unset = UNSET
    terms_of_service_create_at: int | Unset = UNSET
    disable_welcome_email: bool | Unset = UNSET
    external_id: str | Unset = UNSET
    last_activity_at: int | Unset = UNSET
    is_bot: bool | Unset = UNSET
    bot_description: str | Unset = UNSET
    bot_last_icon_update: int | Unset = UNSET
    profile: UserProfile | Unset = UNSET
    is_boosted: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        delete_at = self.delete_at

        username = self.username

        first_name = self.first_name

        last_name = self.last_name

        nickname = self.nickname

        email = self.email

        auth_service = self.auth_service

        roles = self.roles

        locale = self.locale

        position = self.position

        create_at = self.create_at

        update_at = self.update_at

        phone = self.phone

        email_verified = self.email_verified

        notify_props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notify_props, Unset):
            notify_props = self.notify_props.to_dict()

        props: dict[str, Any] | Unset = UNSET
        if not isinstance(self.props, Unset):
            props = self.props.to_dict()

        last_password_update = self.last_password_update

        last_picture_update = self.last_picture_update

        failed_attempts = self.failed_attempts

        mfa_active = self.mfa_active

        timezone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.timezone, Unset):
            timezone = self.timezone.to_dict()

        terms_of_service_id = self.terms_of_service_id

        terms_of_service_create_at = self.terms_of_service_create_at

        disable_welcome_email = self.disable_welcome_email

        external_id = self.external_id

        last_activity_at = self.last_activity_at

        is_bot = self.is_bot

        bot_description = self.bot_description

        bot_last_icon_update = self.bot_last_icon_update

        profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.profile, Unset):
            profile = self.profile.to_dict()

        is_boosted = self.is_boosted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "delete_at": delete_at,
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "nickname": nickname,
                "email": email,
                "auth_service": auth_service,
                "roles": roles,
                "locale": locale,
                "position": position,
            }
        )
        if create_at is not UNSET:
            field_dict["create_at"] = create_at
        if update_at is not UNSET:
            field_dict["update_at"] = update_at
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email_verified is not UNSET:
            field_dict["email_verified"] = email_verified
        if notify_props is not UNSET:
            field_dict["notify_props"] = notify_props
        if props is not UNSET:
            field_dict["props"] = props
        if last_password_update is not UNSET:
            field_dict["last_password_update"] = last_password_update
        if last_picture_update is not UNSET:
            field_dict["last_picture_update"] = last_picture_update
        if failed_attempts is not UNSET:
            field_dict["failed_attempts"] = failed_attempts
        if mfa_active is not UNSET:
            field_dict["mfa_active"] = mfa_active
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if terms_of_service_id is not UNSET:
            field_dict["terms_of_service_id"] = terms_of_service_id
        if terms_of_service_create_at is not UNSET:
            field_dict["terms_of_service_create_at"] = terms_of_service_create_at
        if disable_welcome_email is not UNSET:
            field_dict["disable_welcome_email"] = disable_welcome_email
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if last_activity_at is not UNSET:
            field_dict["last_activity_at"] = last_activity_at
        if is_bot is not UNSET:
            field_dict["is_bot"] = is_bot
        if bot_description is not UNSET:
            field_dict["bot_description"] = bot_description
        if bot_last_icon_update is not UNSET:
            field_dict["bot_last_icon_update"] = bot_last_icon_update
        if profile is not UNSET:
            field_dict["profile"] = profile
        if is_boosted is not UNSET:
            field_dict["isBoosted"] = is_boosted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timezone import Timezone
        from ..models.user_notify_props import UserNotifyProps
        from ..models.user_profile import UserProfile
        from ..models.user_props import UserProps

        d = dict(src_dict)
        id = d.pop("id")

        delete_at = d.pop("delete_at")

        username = d.pop("username")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        nickname = d.pop("nickname")

        email = d.pop("email")

        auth_service = d.pop("auth_service")

        roles = d.pop("roles")

        locale = d.pop("locale")

        position = d.pop("position")

        create_at = d.pop("create_at", UNSET)

        update_at = d.pop("update_at", UNSET)

        phone = d.pop("phone", UNSET)

        email_verified = d.pop("email_verified", UNSET)

        _notify_props = d.pop("notify_props", UNSET)
        notify_props: UserNotifyProps | Unset
        if isinstance(_notify_props, Unset):
            notify_props = UNSET
        else:
            notify_props = UserNotifyProps.from_dict(_notify_props)

        _props = d.pop("props", UNSET)
        props: UserProps | Unset
        if isinstance(_props, Unset):
            props = UNSET
        else:
            props = UserProps.from_dict(_props)

        last_password_update = d.pop("last_password_update", UNSET)

        last_picture_update = d.pop("last_picture_update", UNSET)

        failed_attempts = d.pop("failed_attempts", UNSET)

        mfa_active = d.pop("mfa_active", UNSET)

        _timezone = d.pop("timezone", UNSET)
        timezone: Timezone | Unset
        if isinstance(_timezone, Unset):
            timezone = UNSET
        else:
            timezone = Timezone.from_dict(_timezone)

        terms_of_service_id = d.pop("terms_of_service_id", UNSET)

        terms_of_service_create_at = d.pop("terms_of_service_create_at", UNSET)

        disable_welcome_email = d.pop("disable_welcome_email", UNSET)

        external_id = d.pop("external_id", UNSET)

        last_activity_at = d.pop("last_activity_at", UNSET)

        is_bot = d.pop("is_bot", UNSET)

        bot_description = d.pop("bot_description", UNSET)

        bot_last_icon_update = d.pop("bot_last_icon_update", UNSET)

        _profile = d.pop("profile", UNSET)
        profile: UserProfile | Unset
        if isinstance(_profile, Unset):
            profile = UNSET
        else:
            profile = UserProfile.from_dict(_profile)

        is_boosted = d.pop("isBoosted", UNSET)

        user = cls(
            id=id,
            delete_at=delete_at,
            username=username,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
            email=email,
            auth_service=auth_service,
            roles=roles,
            locale=locale,
            position=position,
            create_at=create_at,
            update_at=update_at,
            phone=phone,
            email_verified=email_verified,
            notify_props=notify_props,
            props=props,
            last_password_update=last_password_update,
            last_picture_update=last_picture_update,
            failed_attempts=failed_attempts,
            mfa_active=mfa_active,
            timezone=timezone,
            terms_of_service_id=terms_of_service_id,
            terms_of_service_create_at=terms_of_service_create_at,
            disable_welcome_email=disable_welcome_email,
            external_id=external_id,
            last_activity_at=last_activity_at,
            is_bot=is_bot,
            bot_description=bot_description,
            bot_last_icon_update=bot_last_icon_update,
            profile=profile,
            is_boosted=is_boosted,
        )

        user.additional_properties = d
        return user

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
