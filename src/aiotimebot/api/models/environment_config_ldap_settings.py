from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentConfigLdapSettings")


@_attrs_define
class EnvironmentConfigLdapSettings:
    """
    Attributes:
        enable (bool | Unset):
        ldap_server (bool | Unset):
        ldap_port (bool | Unset):
        connection_security (bool | Unset):
        base_dn (bool | Unset):
        bind_username (bool | Unset):
        bind_password (bool | Unset):
        user_filter (bool | Unset):
        first_name_attribute (bool | Unset):
        last_name_attribute (bool | Unset):
        email_attribute (bool | Unset):
        username_attribute (bool | Unset):
        nickname_attribute (bool | Unset):
        id_attribute (bool | Unset):
        position_attribute (bool | Unset):
        sync_interval_minutes (bool | Unset):
        skip_certificate_verification (bool | Unset):
        query_timeout (bool | Unset):
        max_page_size (bool | Unset):
        login_field_name (bool | Unset):
    """

    enable: bool | Unset = UNSET
    ldap_server: bool | Unset = UNSET
    ldap_port: bool | Unset = UNSET
    connection_security: bool | Unset = UNSET
    base_dn: bool | Unset = UNSET
    bind_username: bool | Unset = UNSET
    bind_password: bool | Unset = UNSET
    user_filter: bool | Unset = UNSET
    first_name_attribute: bool | Unset = UNSET
    last_name_attribute: bool | Unset = UNSET
    email_attribute: bool | Unset = UNSET
    username_attribute: bool | Unset = UNSET
    nickname_attribute: bool | Unset = UNSET
    id_attribute: bool | Unset = UNSET
    position_attribute: bool | Unset = UNSET
    sync_interval_minutes: bool | Unset = UNSET
    skip_certificate_verification: bool | Unset = UNSET
    query_timeout: bool | Unset = UNSET
    max_page_size: bool | Unset = UNSET
    login_field_name: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        ldap_server = self.ldap_server

        ldap_port = self.ldap_port

        connection_security = self.connection_security

        base_dn = self.base_dn

        bind_username = self.bind_username

        bind_password = self.bind_password

        user_filter = self.user_filter

        first_name_attribute = self.first_name_attribute

        last_name_attribute = self.last_name_attribute

        email_attribute = self.email_attribute

        username_attribute = self.username_attribute

        nickname_attribute = self.nickname_attribute

        id_attribute = self.id_attribute

        position_attribute = self.position_attribute

        sync_interval_minutes = self.sync_interval_minutes

        skip_certificate_verification = self.skip_certificate_verification

        query_timeout = self.query_timeout

        max_page_size = self.max_page_size

        login_field_name = self.login_field_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enable is not UNSET:
            field_dict["Enable"] = enable
        if ldap_server is not UNSET:
            field_dict["LdapServer"] = ldap_server
        if ldap_port is not UNSET:
            field_dict["LdapPort"] = ldap_port
        if connection_security is not UNSET:
            field_dict["ConnectionSecurity"] = connection_security
        if base_dn is not UNSET:
            field_dict["BaseDN"] = base_dn
        if bind_username is not UNSET:
            field_dict["BindUsername"] = bind_username
        if bind_password is not UNSET:
            field_dict["BindPassword"] = bind_password
        if user_filter is not UNSET:
            field_dict["UserFilter"] = user_filter
        if first_name_attribute is not UNSET:
            field_dict["FirstNameAttribute"] = first_name_attribute
        if last_name_attribute is not UNSET:
            field_dict["LastNameAttribute"] = last_name_attribute
        if email_attribute is not UNSET:
            field_dict["EmailAttribute"] = email_attribute
        if username_attribute is not UNSET:
            field_dict["UsernameAttribute"] = username_attribute
        if nickname_attribute is not UNSET:
            field_dict["NicknameAttribute"] = nickname_attribute
        if id_attribute is not UNSET:
            field_dict["IdAttribute"] = id_attribute
        if position_attribute is not UNSET:
            field_dict["PositionAttribute"] = position_attribute
        if sync_interval_minutes is not UNSET:
            field_dict["SyncIntervalMinutes"] = sync_interval_minutes
        if skip_certificate_verification is not UNSET:
            field_dict["SkipCertificateVerification"] = skip_certificate_verification
        if query_timeout is not UNSET:
            field_dict["QueryTimeout"] = query_timeout
        if max_page_size is not UNSET:
            field_dict["MaxPageSize"] = max_page_size
        if login_field_name is not UNSET:
            field_dict["LoginFieldName"] = login_field_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("Enable", UNSET)

        ldap_server = d.pop("LdapServer", UNSET)

        ldap_port = d.pop("LdapPort", UNSET)

        connection_security = d.pop("ConnectionSecurity", UNSET)

        base_dn = d.pop("BaseDN", UNSET)

        bind_username = d.pop("BindUsername", UNSET)

        bind_password = d.pop("BindPassword", UNSET)

        user_filter = d.pop("UserFilter", UNSET)

        first_name_attribute = d.pop("FirstNameAttribute", UNSET)

        last_name_attribute = d.pop("LastNameAttribute", UNSET)

        email_attribute = d.pop("EmailAttribute", UNSET)

        username_attribute = d.pop("UsernameAttribute", UNSET)

        nickname_attribute = d.pop("NicknameAttribute", UNSET)

        id_attribute = d.pop("IdAttribute", UNSET)

        position_attribute = d.pop("PositionAttribute", UNSET)

        sync_interval_minutes = d.pop("SyncIntervalMinutes", UNSET)

        skip_certificate_verification = d.pop("SkipCertificateVerification", UNSET)

        query_timeout = d.pop("QueryTimeout", UNSET)

        max_page_size = d.pop("MaxPageSize", UNSET)

        login_field_name = d.pop("LoginFieldName", UNSET)

        environment_config_ldap_settings = cls(
            enable=enable,
            ldap_server=ldap_server,
            ldap_port=ldap_port,
            connection_security=connection_security,
            base_dn=base_dn,
            bind_username=bind_username,
            bind_password=bind_password,
            user_filter=user_filter,
            first_name_attribute=first_name_attribute,
            last_name_attribute=last_name_attribute,
            email_attribute=email_attribute,
            username_attribute=username_attribute,
            nickname_attribute=nickname_attribute,
            id_attribute=id_attribute,
            position_attribute=position_attribute,
            sync_interval_minutes=sync_interval_minutes,
            skip_certificate_verification=skip_certificate_verification,
            query_timeout=query_timeout,
            max_page_size=max_page_size,
            login_field_name=login_field_name,
        )

        environment_config_ldap_settings.additional_properties = d
        return environment_config_ldap_settings

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
