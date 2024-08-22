import time
from typing import ClassVar
import unittest

from google.protobuf.wrappers_pb2 import BytesValue
from google.protobuf.wrappers_pb2 import BytesValue
from google.protobuf.wrappers_pb2 import BytesValue
from google.protobuf.any_pb2 import Any

import msgpack

from conversationstream.protobuf.api_pb2 import ConversationStreamMessage


class TestSerDePb(unittest.TestCase):
    CSTREAM_BIN: ClassVar[str] = "/tmp/cstream.bin"
    file_result: bool = False
    buf: bytes = b""

    def test_01_create_conversation_stream_message(self, i: int = 0) -> None:
        # Create all string and byte vector data first

        csm: ConversationStreamMessage = ConversationStreamMessage()
        csm.sequence_number = i

        bbuf: bytes = bytearray(150)
        bbuf[1] = i % 127
        content_bytes = BytesValue(value=bytes(bbuf))
        any_value: Any = Any()
        any_value.Pack(content_bytes)
        csm.content.CopyFrom(any_value)

        csm.date_time = "2024-08-15T12:34:56Z"
        csm.session_id = "session_id_123"
        csm.subscriber_id = "subscriber_id_456"
        csm.application_name = "app_name"
        csm.source = "source"
        csm.destination = "destination"
        csm.doc_source = f"doc_source{i}"
        TestSerDePb.buf = csm.SerializeToString()

    def test_02_read_conversation_stream_message(self, i: int = 0) -> None:
        msg: ConversationStreamMessage = ConversationStreamMessage()
        msg.ParseFromString(TestSerDePb.buf)
        sequence_number: int = msg.sequence_number
        assert sequence_number == i

        content = msg.content
        assert content is not None
        bytes_value = BytesValue()
        content.Unpack(bytes_value)

        # Access the actual bytes from BytesValue
        bytes_content: bytes = bytes_value.value
        bbuf: bytes = bytearray(150)
        bbuf[1] = i % 127

        assert bytes_content == bytes(bbuf)

        date_time: str = msg.date_time
        assert date_time == "2024-08-15T12:34:56Z"

        session_id = msg.session_id
        assert session_id == "session_id_123"

        subscriber_id = msg.subscriber_id
        assert subscriber_id == "subscriber_id_456"

        application_name = msg.application_name
        assert application_name == "app_name"

        source: str = msg.source
        assert source == "source"

        destination: str = msg.destination
        assert destination == "destination"

        doc_source: str = msg.doc_source
        assert doc_source == f"doc_source{i}"

    #    def test_03_read_conversation_stream_message(self, i: int = 0) -> None:
    #        msg: ConversationStreamMessage = ConversationStreamMessage()
    #        msg.ParseFromString(TestSerDePb.buf)
    #        packed_data = msgpack.packb(msg)

    def test_03_many(self, n: int = 1_000_000) -> None:
        test: TestSerDePb = TestSerDePb()
        start: int = time.time_ns()
        for i in range(n):
            test.test_01_create_conversation_stream_message(i)
            test.test_02_read_conversation_stream_message(i)

        took: int = (time.time_ns() - start) // 1_000_000
        print(
            f"Took: {took} ms {1000*n/took} msg/s "
            f" message size: {len(TestSerDePb.buf)}"
        )


if __name__ == "__main__":
    # TestSerDePb.file_result = True
    unittest.main()
