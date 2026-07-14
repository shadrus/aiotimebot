from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.config_analytics_settings import ConfigAnalyticsSettings
    from ..models.config_cluster_settings import ConfigClusterSettings
    from ..models.config_compliance_settings import ConfigComplianceSettings
    from ..models.config_email_settings import ConfigEmailSettings
    from ..models.config_file_settings import ConfigFileSettings
    from ..models.config_ldap_settings import ConfigLdapSettings
    from ..models.config_localization_settings import ConfigLocalizationSettings
    from ..models.config_log_settings import ConfigLogSettings
    from ..models.config_metrics_settings import ConfigMetricsSettings
    from ..models.config_native_app_settings import ConfigNativeAppSettings
    from ..models.config_password_settings import ConfigPasswordSettings
    from ..models.config_privacy_settings import ConfigPrivacySettings
    from ..models.config_rate_limit_settings import ConfigRateLimitSettings
    from ..models.config_saml_settings import ConfigSamlSettings
    from ..models.config_service_settings import ConfigServiceSettings
    from ..models.config_sql_settings import ConfigSqlSettings
    from ..models.config_support_settings import ConfigSupportSettings
    from ..models.config_team_settings import ConfigTeamSettings


T = TypeVar("T", bound="Config")


@_attrs_define
class Config:
    """
    Attributes:
        service_settings (ConfigServiceSettings | Unset):
        team_settings (ConfigTeamSettings | Unset):
        sql_settings (ConfigSqlSettings | Unset):
        log_settings (ConfigLogSettings | Unset):
        password_settings (ConfigPasswordSettings | Unset):
        file_settings (ConfigFileSettings | Unset):
        email_settings (ConfigEmailSettings | Unset):
        rate_limit_settings (ConfigRateLimitSettings | Unset):
        privacy_settings (ConfigPrivacySettings | Unset):
        support_settings (ConfigSupportSettings | Unset):
        ldap_settings (ConfigLdapSettings | Unset):
        compliance_settings (ConfigComplianceSettings | Unset):
        localization_settings (ConfigLocalizationSettings | Unset):
        saml_settings (ConfigSamlSettings | Unset):
        native_app_settings (ConfigNativeAppSettings | Unset):
        cluster_settings (ConfigClusterSettings | Unset):
        metrics_settings (ConfigMetricsSettings | Unset):
        analytics_settings (ConfigAnalyticsSettings | Unset):
    """

    service_settings: ConfigServiceSettings | Unset = UNSET
    team_settings: ConfigTeamSettings | Unset = UNSET
    sql_settings: ConfigSqlSettings | Unset = UNSET
    log_settings: ConfigLogSettings | Unset = UNSET
    password_settings: ConfigPasswordSettings | Unset = UNSET
    file_settings: ConfigFileSettings | Unset = UNSET
    email_settings: ConfigEmailSettings | Unset = UNSET
    rate_limit_settings: ConfigRateLimitSettings | Unset = UNSET
    privacy_settings: ConfigPrivacySettings | Unset = UNSET
    support_settings: ConfigSupportSettings | Unset = UNSET
    ldap_settings: ConfigLdapSettings | Unset = UNSET
    compliance_settings: ConfigComplianceSettings | Unset = UNSET
    localization_settings: ConfigLocalizationSettings | Unset = UNSET
    saml_settings: ConfigSamlSettings | Unset = UNSET
    native_app_settings: ConfigNativeAppSettings | Unset = UNSET
    cluster_settings: ConfigClusterSettings | Unset = UNSET
    metrics_settings: ConfigMetricsSettings | Unset = UNSET
    analytics_settings: ConfigAnalyticsSettings | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service_settings, Unset):
            service_settings = self.service_settings.to_dict()

        team_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.team_settings, Unset):
            team_settings = self.team_settings.to_dict()

        sql_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sql_settings, Unset):
            sql_settings = self.sql_settings.to_dict()

        log_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.log_settings, Unset):
            log_settings = self.log_settings.to_dict()

        password_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.password_settings, Unset):
            password_settings = self.password_settings.to_dict()

        file_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file_settings, Unset):
            file_settings = self.file_settings.to_dict()

        email_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email_settings, Unset):
            email_settings = self.email_settings.to_dict()

        rate_limit_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rate_limit_settings, Unset):
            rate_limit_settings = self.rate_limit_settings.to_dict()

        privacy_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.privacy_settings, Unset):
            privacy_settings = self.privacy_settings.to_dict()

        support_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.support_settings, Unset):
            support_settings = self.support_settings.to_dict()

        ldap_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ldap_settings, Unset):
            ldap_settings = self.ldap_settings.to_dict()

        compliance_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.compliance_settings, Unset):
            compliance_settings = self.compliance_settings.to_dict()

        localization_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.localization_settings, Unset):
            localization_settings = self.localization_settings.to_dict()

        saml_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.saml_settings, Unset):
            saml_settings = self.saml_settings.to_dict()

        native_app_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.native_app_settings, Unset):
            native_app_settings = self.native_app_settings.to_dict()

        cluster_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cluster_settings, Unset):
            cluster_settings = self.cluster_settings.to_dict()

        metrics_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics_settings, Unset):
            metrics_settings = self.metrics_settings.to_dict()

        analytics_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.analytics_settings, Unset):
            analytics_settings = self.analytics_settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if service_settings is not UNSET:
            field_dict["ServiceSettings"] = service_settings
        if team_settings is not UNSET:
            field_dict["TeamSettings"] = team_settings
        if sql_settings is not UNSET:
            field_dict["SqlSettings"] = sql_settings
        if log_settings is not UNSET:
            field_dict["LogSettings"] = log_settings
        if password_settings is not UNSET:
            field_dict["PasswordSettings"] = password_settings
        if file_settings is not UNSET:
            field_dict["FileSettings"] = file_settings
        if email_settings is not UNSET:
            field_dict["EmailSettings"] = email_settings
        if rate_limit_settings is not UNSET:
            field_dict["RateLimitSettings"] = rate_limit_settings
        if privacy_settings is not UNSET:
            field_dict["PrivacySettings"] = privacy_settings
        if support_settings is not UNSET:
            field_dict["SupportSettings"] = support_settings
        if ldap_settings is not UNSET:
            field_dict["LdapSettings"] = ldap_settings
        if compliance_settings is not UNSET:
            field_dict["ComplianceSettings"] = compliance_settings
        if localization_settings is not UNSET:
            field_dict["LocalizationSettings"] = localization_settings
        if saml_settings is not UNSET:
            field_dict["SamlSettings"] = saml_settings
        if native_app_settings is not UNSET:
            field_dict["NativeAppSettings"] = native_app_settings
        if cluster_settings is not UNSET:
            field_dict["ClusterSettings"] = cluster_settings
        if metrics_settings is not UNSET:
            field_dict["MetricsSettings"] = metrics_settings
        if analytics_settings is not UNSET:
            field_dict["AnalyticsSettings"] = analytics_settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.config_analytics_settings import ConfigAnalyticsSettings
        from ..models.config_cluster_settings import ConfigClusterSettings
        from ..models.config_compliance_settings import ConfigComplianceSettings
        from ..models.config_email_settings import ConfigEmailSettings
        from ..models.config_file_settings import ConfigFileSettings
        from ..models.config_ldap_settings import ConfigLdapSettings
        from ..models.config_localization_settings import ConfigLocalizationSettings
        from ..models.config_log_settings import ConfigLogSettings
        from ..models.config_metrics_settings import ConfigMetricsSettings
        from ..models.config_native_app_settings import ConfigNativeAppSettings
        from ..models.config_password_settings import ConfigPasswordSettings
        from ..models.config_privacy_settings import ConfigPrivacySettings
        from ..models.config_rate_limit_settings import ConfigRateLimitSettings
        from ..models.config_saml_settings import ConfigSamlSettings
        from ..models.config_service_settings import ConfigServiceSettings
        from ..models.config_sql_settings import ConfigSqlSettings
        from ..models.config_support_settings import ConfigSupportSettings
        from ..models.config_team_settings import ConfigTeamSettings

        d = dict(src_dict)
        _service_settings = d.pop("ServiceSettings", UNSET)
        service_settings: ConfigServiceSettings | Unset
        if isinstance(_service_settings, Unset):
            service_settings = UNSET
        else:
            service_settings = ConfigServiceSettings.from_dict(_service_settings)

        _team_settings = d.pop("TeamSettings", UNSET)
        team_settings: ConfigTeamSettings | Unset
        if isinstance(_team_settings, Unset):
            team_settings = UNSET
        else:
            team_settings = ConfigTeamSettings.from_dict(_team_settings)

        _sql_settings = d.pop("SqlSettings", UNSET)
        sql_settings: ConfigSqlSettings | Unset
        if isinstance(_sql_settings, Unset):
            sql_settings = UNSET
        else:
            sql_settings = ConfigSqlSettings.from_dict(_sql_settings)

        _log_settings = d.pop("LogSettings", UNSET)
        log_settings: ConfigLogSettings | Unset
        if isinstance(_log_settings, Unset):
            log_settings = UNSET
        else:
            log_settings = ConfigLogSettings.from_dict(_log_settings)

        _password_settings = d.pop("PasswordSettings", UNSET)
        password_settings: ConfigPasswordSettings | Unset
        if isinstance(_password_settings, Unset):
            password_settings = UNSET
        else:
            password_settings = ConfigPasswordSettings.from_dict(_password_settings)

        _file_settings = d.pop("FileSettings", UNSET)
        file_settings: ConfigFileSettings | Unset
        if isinstance(_file_settings, Unset):
            file_settings = UNSET
        else:
            file_settings = ConfigFileSettings.from_dict(_file_settings)

        _email_settings = d.pop("EmailSettings", UNSET)
        email_settings: ConfigEmailSettings | Unset
        if isinstance(_email_settings, Unset):
            email_settings = UNSET
        else:
            email_settings = ConfigEmailSettings.from_dict(_email_settings)

        _rate_limit_settings = d.pop("RateLimitSettings", UNSET)
        rate_limit_settings: ConfigRateLimitSettings | Unset
        if isinstance(_rate_limit_settings, Unset):
            rate_limit_settings = UNSET
        else:
            rate_limit_settings = ConfigRateLimitSettings.from_dict(
                _rate_limit_settings
            )

        _privacy_settings = d.pop("PrivacySettings", UNSET)
        privacy_settings: ConfigPrivacySettings | Unset
        if isinstance(_privacy_settings, Unset):
            privacy_settings = UNSET
        else:
            privacy_settings = ConfigPrivacySettings.from_dict(_privacy_settings)

        _support_settings = d.pop("SupportSettings", UNSET)
        support_settings: ConfigSupportSettings | Unset
        if isinstance(_support_settings, Unset):
            support_settings = UNSET
        else:
            support_settings = ConfigSupportSettings.from_dict(_support_settings)

        _ldap_settings = d.pop("LdapSettings", UNSET)
        ldap_settings: ConfigLdapSettings | Unset
        if isinstance(_ldap_settings, Unset):
            ldap_settings = UNSET
        else:
            ldap_settings = ConfigLdapSettings.from_dict(_ldap_settings)

        _compliance_settings = d.pop("ComplianceSettings", UNSET)
        compliance_settings: ConfigComplianceSettings | Unset
        if isinstance(_compliance_settings, Unset):
            compliance_settings = UNSET
        else:
            compliance_settings = ConfigComplianceSettings.from_dict(
                _compliance_settings
            )

        _localization_settings = d.pop("LocalizationSettings", UNSET)
        localization_settings: ConfigLocalizationSettings | Unset
        if isinstance(_localization_settings, Unset):
            localization_settings = UNSET
        else:
            localization_settings = ConfigLocalizationSettings.from_dict(
                _localization_settings
            )

        _saml_settings = d.pop("SamlSettings", UNSET)
        saml_settings: ConfigSamlSettings | Unset
        if isinstance(_saml_settings, Unset):
            saml_settings = UNSET
        else:
            saml_settings = ConfigSamlSettings.from_dict(_saml_settings)

        _native_app_settings = d.pop("NativeAppSettings", UNSET)
        native_app_settings: ConfigNativeAppSettings | Unset
        if isinstance(_native_app_settings, Unset):
            native_app_settings = UNSET
        else:
            native_app_settings = ConfigNativeAppSettings.from_dict(
                _native_app_settings
            )

        _cluster_settings = d.pop("ClusterSettings", UNSET)
        cluster_settings: ConfigClusterSettings | Unset
        if isinstance(_cluster_settings, Unset):
            cluster_settings = UNSET
        else:
            cluster_settings = ConfigClusterSettings.from_dict(_cluster_settings)

        _metrics_settings = d.pop("MetricsSettings", UNSET)
        metrics_settings: ConfigMetricsSettings | Unset
        if isinstance(_metrics_settings, Unset):
            metrics_settings = UNSET
        else:
            metrics_settings = ConfigMetricsSettings.from_dict(_metrics_settings)

        _analytics_settings = d.pop("AnalyticsSettings", UNSET)
        analytics_settings: ConfigAnalyticsSettings | Unset
        if isinstance(_analytics_settings, Unset):
            analytics_settings = UNSET
        else:
            analytics_settings = ConfigAnalyticsSettings.from_dict(_analytics_settings)

        config = cls(
            service_settings=service_settings,
            team_settings=team_settings,
            sql_settings=sql_settings,
            log_settings=log_settings,
            password_settings=password_settings,
            file_settings=file_settings,
            email_settings=email_settings,
            rate_limit_settings=rate_limit_settings,
            privacy_settings=privacy_settings,
            support_settings=support_settings,
            ldap_settings=ldap_settings,
            compliance_settings=compliance_settings,
            localization_settings=localization_settings,
            saml_settings=saml_settings,
            native_app_settings=native_app_settings,
            cluster_settings=cluster_settings,
            metrics_settings=metrics_settings,
            analytics_settings=analytics_settings,
        )

        config.additional_properties = d
        return config

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
