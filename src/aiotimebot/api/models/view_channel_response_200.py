from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.view_channel_response_200_last_viewed_at_times import (
        ViewChannelResponse200LastViewedAtTimes,
    )


T = TypeVar("T", bound="ViewChannelResponse200")


@_attrs_define
class ViewChannelResponse200:
    """Generated Time Messenger API v4 model."""

    status: str
    last_viewed_at_times: ViewChannelResponse200LastViewedAtTimes
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status

        last_viewed_at_times = self.last_viewed_at_times.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "last_viewed_at_times": last_viewed_at_times,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.view_channel_response_200_last_viewed_at_times import (
            ViewChannelResponse200LastViewedAtTimes,
        )

        d = dict(src_dict)
        status = d.pop("status")

        last_viewed_at_times = ViewChannelResponse200LastViewedAtTimes.from_dict(
            d.pop("last_viewed_at_times")
        )

        view_channel_response_200 = cls(
            status=status,
            last_viewed_at_times=last_viewed_at_times,
        )

        view_channel_response_200.additional_properties = d
        return view_channel_response_200

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
