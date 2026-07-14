from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigSupportSettings")


@_attrs_define
class ConfigSupportSettings:
    """
    Attributes:
        terms_of_service_link (str | Unset):
        privacy_policy_link (str | Unset):
        about_link (str | Unset):
        help_link (str | Unset):
        report_a_problem_link (str | Unset):
        support_email (str | Unset):
    """

    terms_of_service_link: str | Unset = UNSET
    privacy_policy_link: str | Unset = UNSET
    about_link: str | Unset = UNSET
    help_link: str | Unset = UNSET
    report_a_problem_link: str | Unset = UNSET
    support_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        terms_of_service_link = self.terms_of_service_link

        privacy_policy_link = self.privacy_policy_link

        about_link = self.about_link

        help_link = self.help_link

        report_a_problem_link = self.report_a_problem_link

        support_email = self.support_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terms_of_service_link is not UNSET:
            field_dict["TermsOfServiceLink"] = terms_of_service_link
        if privacy_policy_link is not UNSET:
            field_dict["PrivacyPolicyLink"] = privacy_policy_link
        if about_link is not UNSET:
            field_dict["AboutLink"] = about_link
        if help_link is not UNSET:
            field_dict["HelpLink"] = help_link
        if report_a_problem_link is not UNSET:
            field_dict["ReportAProblemLink"] = report_a_problem_link
        if support_email is not UNSET:
            field_dict["SupportEmail"] = support_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        terms_of_service_link = d.pop("TermsOfServiceLink", UNSET)

        privacy_policy_link = d.pop("PrivacyPolicyLink", UNSET)

        about_link = d.pop("AboutLink", UNSET)

        help_link = d.pop("HelpLink", UNSET)

        report_a_problem_link = d.pop("ReportAProblemLink", UNSET)

        support_email = d.pop("SupportEmail", UNSET)

        config_support_settings = cls(
            terms_of_service_link=terms_of_service_link,
            privacy_policy_link=privacy_policy_link,
            about_link=about_link,
            help_link=help_link,
            report_a_problem_link=report_a_problem_link,
            support_email=support_email,
        )

        config_support_settings.additional_properties = d
        return config_support_settings

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
