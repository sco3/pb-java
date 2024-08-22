"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ComponentType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ComponentTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ComponentType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    COMPONENT: _ComponentType.ValueType  # 0
    LLM_AGENT: _ComponentType.ValueType  # 1
    API: _ComponentType.ValueType  # 2

class ComponentType(_ComponentType, metaclass=_ComponentTypeEnumTypeWrapper): ...

COMPONENT: ComponentType.ValueType  # 0
LLM_AGENT: ComponentType.ValueType  # 1
API: ComponentType.ValueType  # 2
global___ComponentType = ComponentType

@typing.final
class SentimentAnalysis(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENT_SENTIMENT_FIELD_NUMBER: builtins.int
    TRENDING_SENTIMENT_FIELD_NUMBER: builtins.int
    TOTAL_SENTIMENT_FIELD_NUMBER: builtins.int
    MESSAGE_COUNT_FIELD_NUMBER: builtins.int
    AVERAGE_SENTIMENT_FIELD_NUMBER: builtins.int
    current_sentiment: builtins.float
    trending_sentiment: builtins.float
    total_sentiment: builtins.float
    message_count: builtins.float
    average_sentiment: builtins.float
    def __init__(
        self,
        *,
        current_sentiment: builtins.float = ...,
        trending_sentiment: builtins.float = ...,
        total_sentiment: builtins.float = ...,
        message_count: builtins.float = ...,
        average_sentiment: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["average_sentiment", b"average_sentiment", "current_sentiment", b"current_sentiment", "message_count", b"message_count", "total_sentiment", b"total_sentiment", "trending_sentiment", b"trending_sentiment"]) -> None: ...

global___SentimentAnalysis = SentimentAnalysis

@typing.final
class ConversationItem(google.protobuf.message.Message):
    """Messages"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    role: builtins.str
    content: builtins.str
    def __init__(
        self,
        *,
        role: builtins.str = ...,
        content: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "role", b"role"]) -> None: ...

global___ConversationItem = ConversationItem

@typing.final
class ConversationTranscript(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    CONVERSATION_FIELD_NUMBER: builtins.int
    id: builtins.str
    @property
    def conversation(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ConversationItem]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        conversation: collections.abc.Iterable[global___ConversationItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["conversation", b"conversation", "id", b"id"]) -> None: ...

global___ConversationTranscript = ConversationTranscript

@typing.final
class ChecklistItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    NEXT_SESSION_GOAL_FIELD_NUMBER: builtins.int
    id: builtins.str
    """UUID"""
    name: builtins.str
    description: builtins.str
    next_session_goal: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        next_session_goal: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "id", b"id", "name", b"name", "next_session_goal", b"next_session_goal"]) -> None: ...

global___ChecklistItem = ChecklistItem

@typing.final
class GoalItem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    GOAL_DESCRIPTION_FIELD_NUMBER: builtins.int
    id: builtins.str
    """UUID"""
    goal_description: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        goal_description: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["goal_description", b"goal_description", "id", b"id"]) -> None: ...

global___GoalItem = GoalItem

@typing.final
class PhaseNode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    GOALS_FIELD_NUMBER: builtins.int
    CHECKLIST_FIELD_NUMBER: builtins.int
    id: builtins.str
    """UUID"""
    name: builtins.str
    @property
    def goals(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___GoalItem]: ...
    @property
    def checklist(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ChecklistItem]: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        name: builtins.str = ...,
        goals: collections.abc.Iterable[global___GoalItem] | None = ...,
        checklist: collections.abc.Iterable[global___ChecklistItem] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["checklist", b"checklist", "goals", b"goals", "id", b"id", "name", b"name"]) -> None: ...

global___PhaseNode = PhaseNode

@typing.final
class PhaseConnection(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONNECTION_ID_FIELD_NUMBER: builtins.int
    PREV_PHASE_ID_FIELD_NUMBER: builtins.int
    NEXT_PHASE_ID_FIELD_NUMBER: builtins.int
    connection_id: builtins.str
    """UUID"""
    prev_phase_id: builtins.str
    """UUID"""
    next_phase_id: builtins.str
    """UUID"""
    def __init__(
        self,
        *,
        connection_id: builtins.str = ...,
        prev_phase_id: builtins.str = ...,
        next_phase_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["connection_id", b"connection_id", "next_phase_id", b"next_phase_id", "prev_phase_id", b"prev_phase_id"]) -> None: ...

global___PhaseConnection = PhaseConnection

@typing.final
class PhaseInformation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    START_PHASE_ID_FIELD_NUMBER: builtins.int
    PHASE_NODES_FIELD_NUMBER: builtins.int
    PHASE_CONNECTIONS_FIELD_NUMBER: builtins.int
    start_phase_id: builtins.str
    """UUID"""
    @property
    def phase_nodes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PhaseNode]: ...
    @property
    def phase_connections(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PhaseConnection]: ...
    def __init__(
        self,
        *,
        start_phase_id: builtins.str = ...,
        phase_nodes: collections.abc.Iterable[global___PhaseNode] | None = ...,
        phase_connections: collections.abc.Iterable[global___PhaseConnection] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["phase_connections", b"phase_connections", "phase_nodes", b"phase_nodes", "start_phase_id", b"start_phase_id"]) -> None: ...

global___PhaseInformation = PhaseInformation

@typing.final
class MemoryField(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELD_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    CONTEXT_WORDS_FIELD_NUMBER: builtins.int
    field_name: builtins.str
    description: builtins.str
    content: builtins.str
    @property
    def context_words(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        field_name: builtins.str = ...,
        description: builtins.str = ...,
        content: builtins.str = ...,
        context_words: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "context_words", b"context_words", "description", b"description", "field_name", b"field_name"]) -> None: ...

global___MemoryField = MemoryField

@typing.final
class MemoryModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MEMORY_FIELDS_FIELD_NUMBER: builtins.int
    @property
    def memory_fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___MemoryField]: ...
    def __init__(
        self,
        *,
        memory_fields: collections.abc.Iterable[global___MemoryField] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["memory_fields", b"memory_fields"]) -> None: ...

global___MemoryModel = MemoryModel

@typing.final
class UserModel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CURRENT_USER_PHASE_FIELD_NUMBER: builtins.int
    CURRENT_USER_CHECKLIST_FIELD_NUMBER: builtins.int
    LAST_SESSION_SUMMARY_FIELD_NUMBER: builtins.int
    CLIENT_PROFILE_ASSESSMENT_FIELD_NUMBER: builtins.int
    NEXT_SESSION_GOALS_FIELD_NUMBER: builtins.int
    LAST_OBSERVER_ACCESS_TIMESTAMP_FIELD_NUMBER: builtins.int
    LAST_REMOVED_CHECKLIST_ITEMS_FIELD_NUMBER: builtins.int
    GOAL_REVIEW_CHECK_FIELD_NUMBER: builtins.int
    MEMORIES_FIELD_NUMBER: builtins.int
    CONVERSATION_TRANSCRIPT_FIELD_NUMBER: builtins.int
    SENTIMENT_ANALYSIS_FIELD_NUMBER: builtins.int
    current_user_phase: builtins.str
    last_session_summary: builtins.str
    client_profile_assessment: builtins.str
    next_session_goals: builtins.str
    last_observer_access_timestamp: builtins.int
    """Timestamp"""
    goal_review_check: builtins.bool
    @property
    def current_user_checklist(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ChecklistItem]: ...
    @property
    def last_removed_checklist_items(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def memories(self) -> global___MemoryModel: ...
    @property
    def conversation_transcript(self) -> global___ConversationTranscript: ...
    @property
    def sentiment_analysis(self) -> global___SentimentAnalysis: ...
    def __init__(
        self,
        *,
        current_user_phase: builtins.str = ...,
        current_user_checklist: collections.abc.Iterable[global___ChecklistItem] | None = ...,
        last_session_summary: builtins.str = ...,
        client_profile_assessment: builtins.str = ...,
        next_session_goals: builtins.str = ...,
        last_observer_access_timestamp: builtins.int = ...,
        last_removed_checklist_items: collections.abc.Iterable[builtins.str] | None = ...,
        goal_review_check: builtins.bool = ...,
        memories: global___MemoryModel | None = ...,
        conversation_transcript: global___ConversationTranscript | None = ...,
        sentiment_analysis: global___SentimentAnalysis | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_conversation_transcript", b"_conversation_transcript", "_sentiment_analysis", b"_sentiment_analysis", "conversation_transcript", b"conversation_transcript", "memories", b"memories", "sentiment_analysis", b"sentiment_analysis"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_conversation_transcript", b"_conversation_transcript", "_sentiment_analysis", b"_sentiment_analysis", "client_profile_assessment", b"client_profile_assessment", "conversation_transcript", b"conversation_transcript", "current_user_checklist", b"current_user_checklist", "current_user_phase", b"current_user_phase", "goal_review_check", b"goal_review_check", "last_observer_access_timestamp", b"last_observer_access_timestamp", "last_removed_checklist_items", b"last_removed_checklist_items", "last_session_summary", b"last_session_summary", "memories", b"memories", "next_session_goals", b"next_session_goals", "sentiment_analysis", b"sentiment_analysis"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_conversation_transcript", b"_conversation_transcript"]) -> typing.Literal["conversation_transcript"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_sentiment_analysis", b"_sentiment_analysis"]) -> typing.Literal["sentiment_analysis"] | None: ...

global___UserModel = UserModel

@typing.final
class ConversationStreamMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_NUMBER_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    DATE_TIME_FIELD_NUMBER: builtins.int
    SESSION_ID_FIELD_NUMBER: builtins.int
    SUBSCRIBER_ID_FIELD_NUMBER: builtins.int
    APPLICATION_NAME_FIELD_NUMBER: builtins.int
    MESSAGE_TYPE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    DESTINATION_FIELD_NUMBER: builtins.int
    DOC_SOURCE_FIELD_NUMBER: builtins.int
    sequence_number: builtins.int
    date_time: builtins.str
    session_id: builtins.str
    subscriber_id: builtins.str
    application_name: builtins.str
    message_type: global___ComponentType.ValueType
    source: builtins.str
    destination: builtins.str
    doc_source: builtins.str
    @property
    def content(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        sequence_number: builtins.int = ...,
        content: google.protobuf.any_pb2.Any | None = ...,
        date_time: builtins.str = ...,
        session_id: builtins.str = ...,
        subscriber_id: builtins.str = ...,
        application_name: builtins.str = ...,
        message_type: global___ComponentType.ValueType = ...,
        source: builtins.str = ...,
        destination: builtins.str = ...,
        doc_source: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["content", b"content"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["application_name", b"application_name", "content", b"content", "date_time", b"date_time", "destination", b"destination", "doc_source", b"doc_source", "message_type", b"message_type", "sequence_number", b"sequence_number", "session_id", b"session_id", "source", b"source", "subscriber_id", b"subscriber_id"]) -> None: ...

global___ConversationStreamMessage = ConversationStreamMessage