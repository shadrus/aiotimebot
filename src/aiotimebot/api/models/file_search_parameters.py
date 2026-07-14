from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.file_extended_search_parameters import FileExtendedSearchParameters
    from ..models.file_search_filters import FileSearchFilters
    from ..models.file_search_terms import FileSearchTerms


T = TypeVar("T", bound="FileSearchParameters")


@_attrs_define
class FileSearchParameters:
    """Generated Time Messenger API v4 model."""

    terms: FileSearchTerms
    filters: FileSearchFilters
    extended_params: FileExtendedSearchParameters
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        terms = self.terms.to_dict()

        filters = self.filters.to_dict()

        extended_params = self.extended_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "terms": terms,
                "filters": filters,
                "extended_params": extended_params,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_extended_search_parameters import (
            FileExtendedSearchParameters,
        )
        from ..models.file_search_filters import FileSearchFilters
        from ..models.file_search_terms import FileSearchTerms

        d = dict(src_dict)
        terms = FileSearchTerms.from_dict(d.pop("terms"))

        filters = FileSearchFilters.from_dict(d.pop("filters"))

        extended_params = FileExtendedSearchParameters.from_dict(
            d.pop("extended_params")
        )

        file_search_parameters = cls(
            terms=terms,
            filters=filters,
            extended_params=extended_params,
        )

        file_search_parameters.additional_properties = d
        return file_search_parameters

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
