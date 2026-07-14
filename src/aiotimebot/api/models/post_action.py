from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_action_data_source import PostActionDataSource
from ..models.post_action_style import PostActionStyle
from ..models.post_action_type import PostActionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_action_integration import PostActionIntegration
    from ..models.post_action_options import PostActionOptions


T = TypeVar("T", bound="PostAction")


@_attrs_define
class PostAction:
    """
    Attributes:
        id (str | Unset):
        type_ (PostActionType | Unset):
        name (str | Unset):
        disabled (bool | Unset):
        style (PostActionStyle | Unset):
        data_source (PostActionDataSource | Unset):
        options (list[PostActionOptions] | Unset):
        default_option (str | Unset):
        integrations (PostActionIntegration | Unset):
    """

    id: str | Unset = UNSET
    type_: PostActionType | Unset = UNSET
    name: str | Unset = UNSET
    disabled: bool | Unset = UNSET
    style: PostActionStyle | Unset = UNSET
    data_source: PostActionDataSource | Unset = UNSET
    options: list[PostActionOptions] | Unset = UNSET
    default_option: str | Unset = UNSET
    integrations: PostActionIntegration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        name = self.name

        disabled = self.disabled

        style: str | Unset = UNSET
        if not isinstance(self.style, Unset):
            style = self.style.value

        data_source: str | Unset = UNSET
        if not isinstance(self.data_source, Unset):
            data_source = self.data_source.value

        options: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = []
            for options_item_data in self.options:
                options_item = options_item_data.to_dict()
                options.append(options_item)

        default_option = self.default_option

        integrations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integrations, Unset):
            integrations = self.integrations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if style is not UNSET:
            field_dict["style"] = style
        if data_source is not UNSET:
            field_dict["data_source"] = data_source
        if options is not UNSET:
            field_dict["options"] = options
        if default_option is not UNSET:
            field_dict["default_option"] = default_option
        if integrations is not UNSET:
            field_dict["integrations"] = integrations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_action_integration import PostActionIntegration
        from ..models.post_action_options import PostActionOptions

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PostActionType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PostActionType(_type_)

        name = d.pop("name", UNSET)

        disabled = d.pop("disabled", UNSET)

        _style = d.pop("style", UNSET)
        style: PostActionStyle | Unset
        if isinstance(_style, Unset):
            style = UNSET
        else:
            style = PostActionStyle(_style)

        _data_source = d.pop("data_source", UNSET)
        data_source: PostActionDataSource | Unset
        if isinstance(_data_source, Unset):
            data_source = UNSET
        else:
            data_source = PostActionDataSource(_data_source)

        _options = d.pop("options", UNSET)
        options: list[PostActionOptions] | Unset = UNSET
        if _options is not UNSET:
            options = []
            for options_item_data in _options:
                options_item = PostActionOptions.from_dict(options_item_data)

                options.append(options_item)

        default_option = d.pop("default_option", UNSET)

        _integrations = d.pop("integrations", UNSET)
        integrations: PostActionIntegration | Unset
        if isinstance(_integrations, Unset):
            integrations = UNSET
        else:
            integrations = PostActionIntegration.from_dict(_integrations)

        post_action = cls(
            id=id,
            type_=type_,
            name=name,
            disabled=disabled,
            style=style,
            data_source=data_source,
            options=options,
            default_option=default_option,
            integrations=integrations,
        )

        post_action.additional_properties = d
        return post_action

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
