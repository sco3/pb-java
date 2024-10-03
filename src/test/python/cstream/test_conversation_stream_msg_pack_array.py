""" test for msgpack """

import time
from typing import Any, Dict, ClassVar
import unittest

import msgpack

from msg_pack.msg_pack_conversation_stream import ComponentType
from msg_pack.msg_pack_conversation_stream import ConversationStreamMessageField


class TestSerDeMp(unittest.TestCase):
    """test msgpack with unittest single time and many times for benchmark"""

    message_size: ClassVar[int] = 0

    def test_once(self, i: int = 0) -> None:
        """test a single conversion to and from msg pack format"""
        # test any data for "any" field
        bbuf: bytearray = bytearray(150)
        bbuf[0] = i % 127
        # Create a dictionary with enum values as keys (dict[int, Any])
        data_dict: list[Any] = [None] * (
            ConversationStreamMessageField.DOC_SOURCE + 1
        )
        data_dict[ConversationStreamMessageField.SEQUENCE_NUMBER] = i
        data_dict[ConversationStreamMessageField.ANY] = bbuf
        data_dict[ConversationStreamMessageField.CONTENT] = (
            b"Hello, this is a test"
        )
        data_dict[ConversationStreamMessageField.DATE_TIME] = (
            "2024-08-15T12:34:56Z"
        )
        data_dict[ConversationStreamMessageField.SESSION_ID] = "session_id_123"
        data_dict[ConversationStreamMessageField.SUBSCRIBER_ID] = (
            "subscriber_id_456"
        )
        data_dict[ConversationStreamMessageField.APPLICATION_NAME] = "app_name"
        data_dict[ConversationStreamMessageField.MESSAGE_TYPE] = (
            ComponentType.TEXT
        )
        data_dict[ConversationStreamMessageField.SOURCE] = "source"
        data_dict[ConversationStreamMessageField.DESTINATION] = "destination"
        data_dict[ConversationStreamMessageField.DOC_SOURCE] = f"doc_source{i}"

        # Serialize the dictionary to msgpack format
        serialized_data: bytes = msgpack.packb(data_dict)
        # print("Serialized data (msgpack):", len(serialized_data))

        # Deserialize the data back to dict[int, Any]
        deserialized_data: list[Any] = msgpack.unpackb(
            serialized_data, strict_map_key=False
        )
        # print("Deserialized data (dict[int, Any]):", deserialized_data)

        TestSerDeMp.message_size = len(serialized_data)
        if i == 0:
            assert data_dict == deserialized_data

    def test_many(self, n: int = 1000000) -> None:
        """benchmark test"""
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
