""" 
example of usage of message pack library with the structures for 
conversation stream

in order to compile with mypyc one needs msgpack-types

For instance:

poetry add msgpack-types [--dev] 

"""

import msgpack
import datetime
from typing import Any, Dict, ClassVar
import time

size: int = 0

# Define enums for the fields of ConversationStreamMessage
class ConversationStreamMessageField:
    SEQUENCE_NUMBER: ClassVar[int] = 0
    ANY: ClassVar[int] = 1
    CONTENT: ClassVar[int] = 2
    DATE_TIME: ClassVar[int] = 3
    SESSION_ID: ClassVar[int] = 4
    SUBSCRIBER_ID: ClassVar[int] = 5
    APPLICATION_NAME: ClassVar[int] = 6
    MESSAGE_TYPE: ClassVar[int] = 7
    SOURCE: ClassVar[int] = 8
    DESTINATION: ClassVar[int] = 9
    DOC_SOURCE: ClassVar[int] = 10


class ComponentType:
    UNKNOWN: ClassVar[int] = 0
    TEXT: ClassVar[int] = 1
    IMAGE: ClassVar[int] = 2


def run_once(i: int) -> None:

    # test any data for "any" field
    bbuf: bytearray = bytearray(150)
    bbuf[0] = 1
    # Create a dictionary with enum values as keys (dict[int, Any])
    data_dict: Dict[int, Any] = {
        ConversationStreamMessageField.SEQUENCE_NUMBER: i,
        ConversationStreamMessageField.ANY: bbuf,
        ConversationStreamMessageField.CONTENT: b"Hello, this is a test",
        ConversationStreamMessageField.DATE_TIME: "2024-08-15T12:34:56Z",
        ConversationStreamMessageField.SESSION_ID: "session_id_123",
        ConversationStreamMessageField.SUBSCRIBER_ID: "subscriber_id_456",
        ConversationStreamMessageField.APPLICATION_NAME: "app_name",
        ConversationStreamMessageField.MESSAGE_TYPE: ComponentType.TEXT,
        ConversationStreamMessageField.SOURCE: "source",
        ConversationStreamMessageField.DESTINATION: "destination",
        ConversationStreamMessageField.DOC_SOURCE: f"doc_source{i}",
    }

    # Serialize the dictionary to msgpack format
    serialized_data: bytes = msgpack.packb(data_dict)
    # print("Serialized data (msgpack):", len(serialized_data))

    # Deserialize the data back to dict[int, Any]
    deserialized_data: dict[int, Any] = msgpack.unpackb(
        serialized_data, strict_map_key=False
    )
    # print("Deserialized data (dict[int, Any]):", deserialized_data)

    global size
    size = len(serialized_data)


def run_many(n: int) -> None:

    start: int = time.time_ns()
    for i in range(n):
        run_once(i)

    time.sleep(0.001)
    took: int = (time.time_ns() - start) // 1_000_000
    print(f"Took: {took} ms {1000*n/took} msg/s " f" message size: {size}")
