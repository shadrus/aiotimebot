from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigClient")


@_attrs_define
class ConfigClient:
    """
    Attributes:
        websocket_port (int):
        websocket_secure_port (int):
        websocket_url (str):
        analytics_enabled (bool | Unset):
        enable_custom_terms_of_service (bool | Unset):
        enable_guest_accounts (bool | Unset):
        enable_ldap (bool | Unset):
        enable_multifactor_authentication (bool | Unset):
        enable_open_server (bool | Unset):
        enable_privacy_mode (bool | Unset):
        enable_restricted_guest_accounts (bool | Unset):
        enable_saml (bool | Unset):
        enable_sign_in_with_email (bool | Unset):
        enable_sign_in_with_username (bool | Unset):
        enable_sign_up_with_email (bool | Unset):
        enable_sign_up_with_open_id (bool | Unset):
        enable_user_creation (bool | Unset):
        plugins_enabled (bool | Unset):
        post_edit_time_limit (int | Unset):
        privacy_policy_link (str | Unset):
        terms_of_service_link (str | Unset):
        max_post_size (int | Unset):
        report_a_problem_link (str | Unset):
        mobile_cache_lifetime_hours (int | Unset):
        max_file_size (int | Unset):
    """

    websocket_port: int
    websocket_secure_port: int
    websocket_url: str
    analytics_enabled: bool | Unset = UNSET
    enable_custom_terms_of_service: bool | Unset = UNSET
    enable_guest_accounts: bool | Unset = UNSET
    enable_ldap: bool | Unset = UNSET
    enable_multifactor_authentication: bool | Unset = UNSET
    enable_open_server: bool | Unset = UNSET
    enable_privacy_mode: bool | Unset = UNSET
    enable_restricted_guest_accounts: bool | Unset = UNSET
    enable_saml: bool | Unset = UNSET
    enable_sign_in_with_email: bool | Unset = UNSET
    enable_sign_in_with_username: bool | Unset = UNSET
    enable_sign_up_with_email: bool | Unset = UNSET
    enable_sign_up_with_open_id: bool | Unset = UNSET
    enable_user_creation: bool | Unset = UNSET
    plugins_enabled: bool | Unset = UNSET
    post_edit_time_limit: int | Unset = UNSET
    privacy_policy_link: str | Unset = UNSET
    terms_of_service_link: str | Unset = UNSET
    max_post_size: int | Unset = UNSET
    report_a_problem_link: str | Unset = UNSET
    mobile_cache_lifetime_hours: int | Unset = UNSET
    max_file_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        websocket_port = self.websocket_port

        websocket_secure_port = self.websocket_secure_port

        websocket_url = self.websocket_url

        analytics_enabled = self.analytics_enabled

        enable_custom_terms_of_service = self.enable_custom_terms_of_service

        enable_guest_accounts = self.enable_guest_accounts

        enable_ldap = self.enable_ldap

        enable_multifactor_authentication = self.enable_multifactor_authentication

        enable_open_server = self.enable_open_server

        enable_privacy_mode = self.enable_privacy_mode

        enable_restricted_guest_accounts = self.enable_restricted_guest_accounts

        enable_saml = self.enable_saml

        enable_sign_in_with_email = self.enable_sign_in_with_email

        enable_sign_in_with_username = self.enable_sign_in_with_username

        enable_sign_up_with_email = self.enable_sign_up_with_email

        enable_sign_up_with_open_id = self.enable_sign_up_with_open_id

        enable_user_creation = self.enable_user_creation

        plugins_enabled = self.plugins_enabled

        post_edit_time_limit = self.post_edit_time_limit

        privacy_policy_link = self.privacy_policy_link

        terms_of_service_link = self.terms_of_service_link

        max_post_size = self.max_post_size

        report_a_problem_link = self.report_a_problem_link

        mobile_cache_lifetime_hours = self.mobile_cache_lifetime_hours

        max_file_size = self.max_file_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "WebsocketPort": websocket_port,
                "WebsocketSecurePort": websocket_secure_port,
                "WebsocketURL": websocket_url,
            }
        )
        if analytics_enabled is not UNSET:
            field_dict["AnalyticsEnabled"] = analytics_enabled
        if enable_custom_terms_of_service is not UNSET:
            field_dict["EnableCustomTermsOfService"] = enable_custom_terms_of_service
        if enable_guest_accounts is not UNSET:
            field_dict["EnableGuestAccounts"] = enable_guest_accounts
        if enable_ldap is not UNSET:
            field_dict["EnableLdap"] = enable_ldap
        if enable_multifactor_authentication is not UNSET:
            field_dict["EnableMultifactorAuthentication"] = (
                enable_multifactor_authentication
            )
        if enable_open_server is not UNSET:
            field_dict["EnableOpenServer"] = enable_open_server
        if enable_privacy_mode is not UNSET:
            field_dict["EnablePrivacyMode"] = enable_privacy_mode
        if enable_restricted_guest_accounts is not UNSET:
            field_dict["EnableRestrictedGuestAccounts"] = (
                enable_restricted_guest_accounts
            )
        if enable_saml is not UNSET:
            field_dict["EnableSaml"] = enable_saml
        if enable_sign_in_with_email is not UNSET:
            field_dict["EnableSignInWithEmail"] = enable_sign_in_with_email
        if enable_sign_in_with_username is not UNSET:
            field_dict["EnableSignInWithUsername"] = enable_sign_in_with_username
        if enable_sign_up_with_email is not UNSET:
            field_dict["EnableSignUpWithEmail"] = enable_sign_up_with_email
        if enable_sign_up_with_open_id is not UNSET:
            field_dict["EnableSignUpWithOpenId"] = enable_sign_up_with_open_id
        if enable_user_creation is not UNSET:
            field_dict["EnableUserCreation"] = enable_user_creation
        if plugins_enabled is not UNSET:
            field_dict["PluginsEnabled"] = plugins_enabled
        if post_edit_time_limit is not UNSET:
            field_dict["PostEditTimeLimit"] = post_edit_time_limit
        if privacy_policy_link is not UNSET:
            field_dict["PrivacyPolicyLink"] = privacy_policy_link
        if terms_of_service_link is not UNSET:
            field_dict["TermsOfServiceLink"] = terms_of_service_link
        if max_post_size is not UNSET:
            field_dict["MaxPostSize"] = max_post_size
        if report_a_problem_link is not UNSET:
            field_dict["ReportAProblemLink"] = report_a_problem_link
        if mobile_cache_lifetime_hours is not UNSET:
            field_dict["MobileCacheLifetimeHours"] = mobile_cache_lifetime_hours
        if max_file_size is not UNSET:
            field_dict["MaxFileSize"] = max_file_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        websocket_port = d.pop("WebsocketPort")

        websocket_secure_port = d.pop("WebsocketSecurePort")

        websocket_url = d.pop("WebsocketURL")

        analytics_enabled = d.pop("AnalyticsEnabled", UNSET)

        enable_custom_terms_of_service = d.pop("EnableCustomTermsOfService", UNSET)

        enable_guest_accounts = d.pop("EnableGuestAccounts", UNSET)

        enable_ldap = d.pop("EnableLdap", UNSET)

        enable_multifactor_authentication = d.pop(
            "EnableMultifactorAuthentication", UNSET
        )

        enable_open_server = d.pop("EnableOpenServer", UNSET)

        enable_privacy_mode = d.pop("EnablePrivacyMode", UNSET)

        enable_restricted_guest_accounts = d.pop("EnableRestrictedGuestAccounts", UNSET)

        enable_saml = d.pop("EnableSaml", UNSET)

        enable_sign_in_with_email = d.pop("EnableSignInWithEmail", UNSET)

        enable_sign_in_with_username = d.pop("EnableSignInWithUsername", UNSET)

        enable_sign_up_with_email = d.pop("EnableSignUpWithEmail", UNSET)

        enable_sign_up_with_open_id = d.pop("EnableSignUpWithOpenId", UNSET)

        enable_user_creation = d.pop("EnableUserCreation", UNSET)

        plugins_enabled = d.pop("PluginsEnabled", UNSET)

        post_edit_time_limit = d.pop("PostEditTimeLimit", UNSET)

        privacy_policy_link = d.pop("PrivacyPolicyLink", UNSET)

        terms_of_service_link = d.pop("TermsOfServiceLink", UNSET)

        max_post_size = d.pop("MaxPostSize", UNSET)

        report_a_problem_link = d.pop("ReportAProblemLink", UNSET)

        mobile_cache_lifetime_hours = d.pop("MobileCacheLifetimeHours", UNSET)

        max_file_size = d.pop("MaxFileSize", UNSET)

        config_client = cls(
            websocket_port=websocket_port,
            websocket_secure_port=websocket_secure_port,
            websocket_url=websocket_url,
            analytics_enabled=analytics_enabled,
            enable_custom_terms_of_service=enable_custom_terms_of_service,
            enable_guest_accounts=enable_guest_accounts,
            enable_ldap=enable_ldap,
            enable_multifactor_authentication=enable_multifactor_authentication,
            enable_open_server=enable_open_server,
            enable_privacy_mode=enable_privacy_mode,
            enable_restricted_guest_accounts=enable_restricted_guest_accounts,
            enable_saml=enable_saml,
            enable_sign_in_with_email=enable_sign_in_with_email,
            enable_sign_in_with_username=enable_sign_in_with_username,
            enable_sign_up_with_email=enable_sign_up_with_email,
            enable_sign_up_with_open_id=enable_sign_up_with_open_id,
            enable_user_creation=enable_user_creation,
            plugins_enabled=plugins_enabled,
            post_edit_time_limit=post_edit_time_limit,
            privacy_policy_link=privacy_policy_link,
            terms_of_service_link=terms_of_service_link,
            max_post_size=max_post_size,
            report_a_problem_link=report_a_problem_link,
            mobile_cache_lifetime_hours=mobile_cache_lifetime_hours,
            max_file_size=max_file_size,
        )

        config_client.additional_properties = d
        return config_client

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
