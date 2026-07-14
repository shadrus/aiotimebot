from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_extended_search_parameters import PostExtendedSearchParameters
    from ..models.post_search_filters import PostSearchFilters
    from ..models.post_search_terms import PostSearchTerms


T = TypeVar("T", bound="PostSearchParameters")


@_attrs_define
class PostSearchParameters:
    """Generated Time Messenger API v4 model."""

    terms: PostSearchTerms | Unset = UNSET
    filters: PostSearchFilters | Unset = UNSET
    extended_params: PostExtendedSearchParameters | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        extended_params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extended_params, Unset):
            extended_params = self.extended_params.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if terms is not UNSET:
            field_dict["terms"] = terms
        if filters is not UNSET:
            field_dict["filters"] = filters
        if extended_params is not UNSET:
            field_dict["extended_params"] = extended_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_extended_search_parameters import (
            PostExtendedSearchParameters,
        )
        from ..models.post_search_filters import PostSearchFilters
        from ..models.post_search_terms import PostSearchTerms

        d = dict(src_dict)
        _terms = d.pop("terms", UNSET)
        terms: PostSearchTerms | Unset
        if isinstance(_terms, Unset):
            terms = UNSET
        else:
            terms = PostSearchTerms.from_dict(_terms)

        _filters = d.pop("filters", UNSET)
        filters: PostSearchFilters | Unset
        if isinstance(_filters, Unset):
            filters = UNSET
        else:
            filters = PostSearchFilters.from_dict(_filters)

        _extended_params = d.pop("extended_params", UNSET)
        extended_params: PostExtendedSearchParameters | Unset
        if isinstance(_extended_params, Unset):
            extended_params = UNSET
        else:
            extended_params = PostExtendedSearchParameters.from_dict(_extended_params)

        post_search_parameters = cls(
            terms=terms,
            filters=filters,
            extended_params=extended_params,
        )

        post_search_parameters.additional_properties = d
        return post_search_parameters

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
