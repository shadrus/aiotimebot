from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.auth_config_auth_order_item import AuthConfigAuthOrderItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="AuthConfig")


@_attrs_define
class AuthConfig:
    """Generated Time Messenger API v4 model."""

    auth_order: list[AuthConfigAuthOrderItem] | Unset = UNSET
    enable_sign_up_with_email: bool | Unset = UNSET
    email_login_button_color: str | Unset = UNSET
    email_login_button_border_color: str | Unset = UNSET
    email_login_button_text_color: str | Unset = UNSET
    enable_sign_up_with_open_id: bool | Unset = UNSET
    open_id_button_color: str | Unset = UNSET
    open_id_button_text: str | Unset = UNSET
    enable_sign_up_with_saml: bool | Unset = UNSET
    enable_saml: bool | Unset = UNSET
    saml_login_button_color: str | Unset = UNSET
    saml_login_button_border_color: str | Unset = UNSET
    saml_login_button_text_color: str | Unset = UNSET
    saml_login_button_text: str | Unset = UNSET
    enable_sign_up_with_ldap: bool | Unset = UNSET
    enable_ldap: bool | Unset = UNSET
    first_name_max_length: int | Unset = UNSET
    last_name_max_length: int | Unset = UNSET
    ldap_login_button_color: str | Unset = UNSET
    ldap_login_button_border_color: str | Unset = UNSET
    ldap_login_button_text_color: str | Unset = UNSET
    ldap_login_field_name: str | Unset = UNSET
    login_minimum_length: int | Unset = UNSET
    login_maximum_length: int | Unset = UNSET
    login_regex: str | Unset = UNSET
    max_image_resolution: int | Unset = UNSET
    profile_image_min_width: int | Unset = UNSET
    profile_image_min_height: int | Unset = UNSET
    max_image_file_size: int | Unset = UNSET
    image_file_extensions: str | Unset = UNSET
    password_minimum_length: int | Unset = UNSET
    password_maximum_length: int | Unset = UNSET
    password_require_lowercase: bool | Unset = UNSET
    password_require_number: bool | Unset = UNSET
    password_require_symbol: bool | Unset = UNSET
    password_require_uppercase: bool | Unset = UNSET
    position_max_length: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auth_order: list[str] | Unset = UNSET
        if not isinstance(self.auth_order, Unset):
            auth_order = []
            for auth_order_item_data in self.auth_order:
                auth_order_item = auth_order_item_data.value
                auth_order.append(auth_order_item)

        enable_sign_up_with_email = self.enable_sign_up_with_email

        email_login_button_color = self.email_login_button_color

        email_login_button_border_color = self.email_login_button_border_color

        email_login_button_text_color = self.email_login_button_text_color

        enable_sign_up_with_open_id = self.enable_sign_up_with_open_id

        open_id_button_color = self.open_id_button_color

        open_id_button_text = self.open_id_button_text

        enable_sign_up_with_saml = self.enable_sign_up_with_saml

        enable_saml = self.enable_saml

        saml_login_button_color = self.saml_login_button_color

        saml_login_button_border_color = self.saml_login_button_border_color

        saml_login_button_text_color = self.saml_login_button_text_color

        saml_login_button_text = self.saml_login_button_text

        enable_sign_up_with_ldap = self.enable_sign_up_with_ldap

        enable_ldap = self.enable_ldap

        first_name_max_length = self.first_name_max_length

        last_name_max_length = self.last_name_max_length

        ldap_login_button_color = self.ldap_login_button_color

        ldap_login_button_border_color = self.ldap_login_button_border_color

        ldap_login_button_text_color = self.ldap_login_button_text_color

        ldap_login_field_name = self.ldap_login_field_name

        login_minimum_length = self.login_minimum_length

        login_maximum_length = self.login_maximum_length

        login_regex = self.login_regex

        max_image_resolution = self.max_image_resolution

        profile_image_min_width = self.profile_image_min_width

        profile_image_min_height = self.profile_image_min_height

        max_image_file_size = self.max_image_file_size

        image_file_extensions = self.image_file_extensions

        password_minimum_length = self.password_minimum_length

        password_maximum_length = self.password_maximum_length

        password_require_lowercase = self.password_require_lowercase

        password_require_number = self.password_require_number

        password_require_symbol = self.password_require_symbol

        password_require_uppercase = self.password_require_uppercase

        position_max_length = self.position_max_length

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auth_order is not UNSET:
            field_dict["AuthOrder"] = auth_order
        if enable_sign_up_with_email is not UNSET:
            field_dict["EnableSignUpWithEmail"] = enable_sign_up_with_email
        if email_login_button_color is not UNSET:
            field_dict["EmailLoginButtonColor"] = email_login_button_color
        if email_login_button_border_color is not UNSET:
            field_dict["EmailLoginButtonBorderColor"] = email_login_button_border_color
        if email_login_button_text_color is not UNSET:
            field_dict["EmailLoginButtonTextColor"] = email_login_button_text_color
        if enable_sign_up_with_open_id is not UNSET:
            field_dict["EnableSignUpWithOpenId"] = enable_sign_up_with_open_id
        if open_id_button_color is not UNSET:
            field_dict["OpenIdButtonColor"] = open_id_button_color
        if open_id_button_text is not UNSET:
            field_dict["OpenIdButtonText"] = open_id_button_text
        if enable_sign_up_with_saml is not UNSET:
            field_dict["EnableSignUpWithSaml"] = enable_sign_up_with_saml
        if enable_saml is not UNSET:
            field_dict["EnableSaml"] = enable_saml
        if saml_login_button_color is not UNSET:
            field_dict["SamlLoginButtonColor"] = saml_login_button_color
        if saml_login_button_border_color is not UNSET:
            field_dict["SamlLoginButtonBorderColor"] = saml_login_button_border_color
        if saml_login_button_text_color is not UNSET:
            field_dict["SamlLoginButtonTextColor"] = saml_login_button_text_color
        if saml_login_button_text is not UNSET:
            field_dict["SamlLoginButtonText"] = saml_login_button_text
        if enable_sign_up_with_ldap is not UNSET:
            field_dict["EnableSignUpWithLdap"] = enable_sign_up_with_ldap
        if enable_ldap is not UNSET:
            field_dict["EnableLdap"] = enable_ldap
        if first_name_max_length is not UNSET:
            field_dict["FirstNameMaxLength"] = first_name_max_length
        if last_name_max_length is not UNSET:
            field_dict["LastNameMaxLength"] = last_name_max_length
        if ldap_login_button_color is not UNSET:
            field_dict["LdapLoginButtonColor"] = ldap_login_button_color
        if ldap_login_button_border_color is not UNSET:
            field_dict["LdapLoginButtonBorderColor"] = ldap_login_button_border_color
        if ldap_login_button_text_color is not UNSET:
            field_dict["LdapLoginButtonTextColor"] = ldap_login_button_text_color
        if ldap_login_field_name is not UNSET:
            field_dict["LdapLoginFieldName"] = ldap_login_field_name
        if login_minimum_length is not UNSET:
            field_dict["LoginMinimumLength"] = login_minimum_length
        if login_maximum_length is not UNSET:
            field_dict["LoginMaximumLength"] = login_maximum_length
        if login_regex is not UNSET:
            field_dict["LoginRegex"] = login_regex
        if max_image_resolution is not UNSET:
            field_dict["MaxImageResolution"] = max_image_resolution
        if profile_image_min_width is not UNSET:
            field_dict["ProfileImageMinWidth"] = profile_image_min_width
        if profile_image_min_height is not UNSET:
            field_dict["ProfileImageMinHeight"] = profile_image_min_height
        if max_image_file_size is not UNSET:
            field_dict["MaxImageFileSize"] = max_image_file_size
        if image_file_extensions is not UNSET:
            field_dict["ImageFileExtensions"] = image_file_extensions
        if password_minimum_length is not UNSET:
            field_dict["PasswordMinimumLength"] = password_minimum_length
        if password_maximum_length is not UNSET:
            field_dict["PasswordMaximumLength"] = password_maximum_length
        if password_require_lowercase is not UNSET:
            field_dict["PasswordRequireLowercase"] = password_require_lowercase
        if password_require_number is not UNSET:
            field_dict["PasswordRequireNumber"] = password_require_number
        if password_require_symbol is not UNSET:
            field_dict["PasswordRequireSymbol"] = password_require_symbol
        if password_require_uppercase is not UNSET:
            field_dict["PasswordRequireUppercase"] = password_require_uppercase
        if position_max_length is not UNSET:
            field_dict["PositionMaxLength"] = position_max_length

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _auth_order = d.pop("AuthOrder", UNSET)
        auth_order: list[AuthConfigAuthOrderItem] | Unset = UNSET
        if _auth_order is not UNSET:
            auth_order = []
            for auth_order_item_data in _auth_order:
                auth_order_item = AuthConfigAuthOrderItem(auth_order_item_data)

                auth_order.append(auth_order_item)

        enable_sign_up_with_email = d.pop("EnableSignUpWithEmail", UNSET)

        email_login_button_color = d.pop("EmailLoginButtonColor", UNSET)

        email_login_button_border_color = d.pop("EmailLoginButtonBorderColor", UNSET)

        email_login_button_text_color = d.pop("EmailLoginButtonTextColor", UNSET)

        enable_sign_up_with_open_id = d.pop("EnableSignUpWithOpenId", UNSET)

        open_id_button_color = d.pop("OpenIdButtonColor", UNSET)

        open_id_button_text = d.pop("OpenIdButtonText", UNSET)

        enable_sign_up_with_saml = d.pop("EnableSignUpWithSaml", UNSET)

        enable_saml = d.pop("EnableSaml", UNSET)

        saml_login_button_color = d.pop("SamlLoginButtonColor", UNSET)

        saml_login_button_border_color = d.pop("SamlLoginButtonBorderColor", UNSET)

        saml_login_button_text_color = d.pop("SamlLoginButtonTextColor", UNSET)

        saml_login_button_text = d.pop("SamlLoginButtonText", UNSET)

        enable_sign_up_with_ldap = d.pop("EnableSignUpWithLdap", UNSET)

        enable_ldap = d.pop("EnableLdap", UNSET)

        first_name_max_length = d.pop("FirstNameMaxLength", UNSET)

        last_name_max_length = d.pop("LastNameMaxLength", UNSET)

        ldap_login_button_color = d.pop("LdapLoginButtonColor", UNSET)

        ldap_login_button_border_color = d.pop("LdapLoginButtonBorderColor", UNSET)

        ldap_login_button_text_color = d.pop("LdapLoginButtonTextColor", UNSET)

        ldap_login_field_name = d.pop("LdapLoginFieldName", UNSET)

        login_minimum_length = d.pop("LoginMinimumLength", UNSET)

        login_maximum_length = d.pop("LoginMaximumLength", UNSET)

        login_regex = d.pop("LoginRegex", UNSET)

        max_image_resolution = d.pop("MaxImageResolution", UNSET)

        profile_image_min_width = d.pop("ProfileImageMinWidth", UNSET)

        profile_image_min_height = d.pop("ProfileImageMinHeight", UNSET)

        max_image_file_size = d.pop("MaxImageFileSize", UNSET)

        image_file_extensions = d.pop("ImageFileExtensions", UNSET)

        password_minimum_length = d.pop("PasswordMinimumLength", UNSET)

        password_maximum_length = d.pop("PasswordMaximumLength", UNSET)

        password_require_lowercase = d.pop("PasswordRequireLowercase", UNSET)

        password_require_number = d.pop("PasswordRequireNumber", UNSET)

        password_require_symbol = d.pop("PasswordRequireSymbol", UNSET)

        password_require_uppercase = d.pop("PasswordRequireUppercase", UNSET)

        position_max_length = d.pop("PositionMaxLength", UNSET)

        auth_config = cls(
            auth_order=auth_order,
            enable_sign_up_with_email=enable_sign_up_with_email,
            email_login_button_color=email_login_button_color,
            email_login_button_border_color=email_login_button_border_color,
            email_login_button_text_color=email_login_button_text_color,
            enable_sign_up_with_open_id=enable_sign_up_with_open_id,
            open_id_button_color=open_id_button_color,
            open_id_button_text=open_id_button_text,
            enable_sign_up_with_saml=enable_sign_up_with_saml,
            enable_saml=enable_saml,
            saml_login_button_color=saml_login_button_color,
            saml_login_button_border_color=saml_login_button_border_color,
            saml_login_button_text_color=saml_login_button_text_color,
            saml_login_button_text=saml_login_button_text,
            enable_sign_up_with_ldap=enable_sign_up_with_ldap,
            enable_ldap=enable_ldap,
            first_name_max_length=first_name_max_length,
            last_name_max_length=last_name_max_length,
            ldap_login_button_color=ldap_login_button_color,
            ldap_login_button_border_color=ldap_login_button_border_color,
            ldap_login_button_text_color=ldap_login_button_text_color,
            ldap_login_field_name=ldap_login_field_name,
            login_minimum_length=login_minimum_length,
            login_maximum_length=login_maximum_length,
            login_regex=login_regex,
            max_image_resolution=max_image_resolution,
            profile_image_min_width=profile_image_min_width,
            profile_image_min_height=profile_image_min_height,
            max_image_file_size=max_image_file_size,
            image_file_extensions=image_file_extensions,
            password_minimum_length=password_minimum_length,
            password_maximum_length=password_maximum_length,
            password_require_lowercase=password_require_lowercase,
            password_require_number=password_require_number,
            password_require_symbol=password_require_symbol,
            password_require_uppercase=password_require_uppercase,
            position_max_length=position_max_length,
        )

        auth_config.additional_properties = d
        return auth_config

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
