from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.emoji import Emoji
    from ..models.file_info import FileInfo
    from ..models.post_metadata_embeds_item import PostMetadataEmbedsItem
    from ..models.post_metadata_images import PostMetadataImages
    from ..models.reaction import Reaction


T = TypeVar("T", bound="PostMetadata")


@_attrs_define
class PostMetadata:
    """Generated Time Messenger API v4 model."""

    embeds: list[PostMetadataEmbedsItem] | Unset = UNSET
    emojis: list[Emoji] | Unset = UNSET
    files: list[FileInfo] | Unset = UNSET
    images: PostMetadataImages | Unset = UNSET
    reactions: list[Reaction] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        embeds: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.embeds, Unset):
            embeds = []
            for embeds_item_data in self.embeds:
                embeds_item = embeds_item_data.to_dict()
                embeds.append(embeds_item)

        emojis: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emojis, Unset):
            emojis = []
            for emojis_item_data in self.emojis:
                emojis_item = emojis_item_data.to_dict()
                emojis.append(emojis_item)

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        images: dict[str, Any] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = self.images.to_dict()

        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if embeds is not UNSET:
            field_dict["embeds"] = embeds
        if emojis is not UNSET:
            field_dict["emojis"] = emojis
        if files is not UNSET:
            field_dict["files"] = files
        if images is not UNSET:
            field_dict["images"] = images
        if reactions is not UNSET:
            field_dict["reactions"] = reactions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.emoji import Emoji
        from ..models.file_info import FileInfo
        from ..models.post_metadata_embeds_item import PostMetadataEmbedsItem
        from ..models.post_metadata_images import PostMetadataImages
        from ..models.reaction import Reaction

        d = dict(src_dict)
        _embeds = d.pop("embeds", UNSET)
        embeds: list[PostMetadataEmbedsItem] | Unset = UNSET
        if _embeds is not UNSET:
            embeds = []
            for embeds_item_data in _embeds:
                embeds_item = PostMetadataEmbedsItem.from_dict(embeds_item_data)

                embeds.append(embeds_item)

        _emojis = d.pop("emojis", UNSET)
        emojis: list[Emoji] | Unset = UNSET
        if _emojis is not UNSET:
            emojis = []
            for emojis_item_data in _emojis:
                emojis_item = Emoji.from_dict(emojis_item_data)

                emojis.append(emojis_item)

        _files = d.pop("files", UNSET)
        files: list[FileInfo] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FileInfo.from_dict(files_item_data)

                files.append(files_item)

        _images = d.pop("images", UNSET)
        images: PostMetadataImages | Unset
        if isinstance(_images, Unset):
            images = UNSET
        else:
            images = PostMetadataImages.from_dict(_images)

        _reactions = d.pop("reactions", UNSET)
        reactions: list[Reaction] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = Reaction.from_dict(reactions_item_data)

                reactions.append(reactions_item)

        post_metadata = cls(
            embeds=embeds,
            emojis=emojis,
            files=files,
            images=images,
            reactions=reactions,
        )

        post_metadata.additional_properties = d
        return post_metadata

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
