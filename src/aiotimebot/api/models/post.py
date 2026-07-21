from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_metadata import PostMetadata
    from ..models.post_participant import PostParticipant
    from ..models.post_props import PostProps


T = TypeVar("T", bound="Post")


@_attrs_define
class Post:
    """Generated Time Messenger API v4 model."""

    id: str
    create_at: int
    update_at: int
    edit_at: int
    delete_at: int
    is_pinned: bool
    user_id: str
    channel_id: str
    root_id: str
    original_id: str
    message: str
    type_: str
    props: PostProps
    hashtags: str
    pending_post_id: str
    idempotency_key: str
    reply_count: int
    last_reply_at: int
    peer: str | Unset = UNSET
    message_source: str | Unset = UNSET
    file_ids: list[str] | Unset = UNSET
    has_reactions: bool | Unset = UNSET
    remote_id: str | Unset = UNSET
    participants: list[PostParticipant] | None | Unset = UNSET
    is_following: bool | Unset = UNSET
    metadata: PostMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        create_at = self.create_at

        update_at = self.update_at

        edit_at = self.edit_at

        delete_at = self.delete_at

        is_pinned = self.is_pinned

        user_id = self.user_id

        channel_id = self.channel_id

        root_id = self.root_id

        original_id = self.original_id

        message = self.message

        type_ = self.type_

        props = self.props.to_dict()

        hashtags = self.hashtags

        pending_post_id = self.pending_post_id

        idempotency_key = self.idempotency_key

        reply_count = self.reply_count

        last_reply_at = self.last_reply_at

        peer = self.peer

        message_source = self.message_source

        file_ids: list[str] | Unset = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        has_reactions = self.has_reactions

        remote_id = self.remote_id

        participants: list[dict[str, Any]] | None | Unset
        if isinstance(self.participants, Unset):
            participants = UNSET
        elif isinstance(self.participants, list):
            participants = []
            for participants_type_0_item_data in self.participants:
                participants_type_0_item = participants_type_0_item_data.to_dict()
                participants.append(participants_type_0_item)

        else:
            participants = self.participants

        is_following = self.is_following

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "create_at": create_at,
                "update_at": update_at,
                "edit_at": edit_at,
                "delete_at": delete_at,
                "is_pinned": is_pinned,
                "user_id": user_id,
                "channel_id": channel_id,
                "root_id": root_id,
                "original_id": original_id,
                "message": message,
                "type": type_,
                "props": props,
                "hashtags": hashtags,
                "pending_post_id": pending_post_id,
                "idempotency_key": idempotency_key,
                "reply_count": reply_count,
                "last_reply_at": last_reply_at,
            }
        )
        if peer is not UNSET:
            field_dict["peer"] = peer
        if message_source is not UNSET:
            field_dict["message_source"] = message_source
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if has_reactions is not UNSET:
            field_dict["has_reactions"] = has_reactions
        if remote_id is not UNSET:
            field_dict["remote_id"] = remote_id
        if participants is not UNSET:
            field_dict["participants"] = participants
        if is_following is not UNSET:
            field_dict["is_following"] = is_following
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_metadata import PostMetadata
        from ..models.post_participant import PostParticipant
        from ..models.post_props import PostProps

        d = dict(src_dict)
        id = d.pop("id")

        create_at = d.pop("create_at")

        update_at = d.pop("update_at")

        edit_at = d.pop("edit_at")

        delete_at = d.pop("delete_at")

        is_pinned = d.pop("is_pinned")

        user_id = d.pop("user_id")

        channel_id = d.pop("channel_id")

        root_id = d.pop("root_id")

        original_id = d.pop("original_id")

        message = d.pop("message")

        type_ = d.pop("type")

        props = PostProps.from_dict(d.pop("props"))

        hashtags = d.pop("hashtags")

        pending_post_id = d.pop("pending_post_id")

        idempotency_key = d.pop("idempotency_key")

        reply_count = d.pop("reply_count")

        last_reply_at = d.pop("last_reply_at")

        peer = d.pop("peer", UNSET)

        message_source = d.pop("message_source", UNSET)

        file_ids = cast(list[str], d.pop("file_ids", UNSET))

        has_reactions = d.pop("has_reactions", UNSET)

        remote_id = d.pop("remote_id", UNSET)

        def _parse_participants(data: object) -> list[PostParticipant] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                participants_type_0 = []
                _participants_type_0 = data
                for participants_type_0_item_data in _participants_type_0:
                    participants_type_0_item = PostParticipant.from_dict(
                        participants_type_0_item_data
                    )

                    participants_type_0.append(participants_type_0_item)

                return participants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PostParticipant] | None | Unset, data)

        participants = _parse_participants(d.pop("participants", UNSET))

        is_following = d.pop("is_following", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: PostMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = PostMetadata.from_dict(_metadata)

        post = cls(
            id=id,
            create_at=create_at,
            update_at=update_at,
            edit_at=edit_at,
            delete_at=delete_at,
            is_pinned=is_pinned,
            user_id=user_id,
            channel_id=channel_id,
            root_id=root_id,
            original_id=original_id,
            message=message,
            type_=type_,
            props=props,
            hashtags=hashtags,
            pending_post_id=pending_post_id,
            idempotency_key=idempotency_key,
            reply_count=reply_count,
            last_reply_at=last_reply_at,
            peer=peer,
            message_source=message_source,
            file_ids=file_ids,
            has_reactions=has_reactions,
            remote_id=remote_id,
            participants=participants,
            is_following=is_following,
            metadata=metadata,
        )

        post.additional_properties = d
        return post

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
