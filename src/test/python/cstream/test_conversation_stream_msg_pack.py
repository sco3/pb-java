import datetime
import datetime
import time
import time
from typing import Any, Dict, ClassVar
import unittest

import pytest
import msgpack

from msg_pack.msg_pack_conversation_stream import ComponentType
from msg_pack.msg_pack_conversation_stream import ConversationStreamMessageField
from msg_pack.msg_pack_conversation_stream import ConversationStreamMessage


class TestSerDeMp(unittest.TestCase):

    message_size: ClassVar[int] = 0

    def test_once(self, i: int = 0) -> None:

        # test any data for "any" field
        bbuf: bytearray = bytearray(150)
        bbuf[0] = i % 127
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

        TestSerDeMp.message_size = len(serialized_data)
        if i == 0:
            assert data_dict == deserialized_data
            
    @pytest.mark.repeat(3)
    def test_many(self, n: int = 1000000) -> None:

        start: int = time.time_ns()
        for i in range(n):
            self.test_once(i)

        took: int = (time.time_ns() - start) // 1_000_000
        print(
            f"Took: {took} ms {1000*n/took} msg/s "
            f" message size: {TestSerDeMp.message_size}"
        )


# Example usage
if __name__ == "__main__":
    # test_msg_pack.run_many(1000000)
    unittest.main()
