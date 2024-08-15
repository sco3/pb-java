import time
from typing import ClassVar
import unittest

import flatbuffers
from numpy import ndarray

from MyGame.Sample import ConversationStreamMessage as csm
from MyGame.Sample.ComponentType import ComponentType
from MyGame.Sample.ConversationStreamMessage import ConversationStreamMessage


class TestSerDe(unittest.TestCase):
    CSTREAM_BIN: ClassVar[str] = "/tmp/cstream.bin"
    file_result: bool = False
    buf: bytes = b""

    def test_01_create_conversation_stream_message(self) -> None:
        builder = flatbuffers.Builder(1024)

        # Create all string and byte vector data first
        sequence_number = 1
        content = builder.CreateByteVector(b"\x01\x02\x03")
        date_time = builder.CreateString("2024-08-15T12:34:56Z")
        session_id = builder.CreateString("session_id_123")
        subscriber_id = builder.CreateString("subscriber_id_456")
        application_name = builder.CreateString("app_name")
        source = builder.CreateString("source")
        destination = builder.CreateString("destination")
        doc_source = builder.CreateString("doc_source")

        # Start building the ConversationStreamMessage
        csm.Start(builder)
        csm.AddSequenceNumber(builder, sequence_number)
        csm.AddContent(builder, content)
        csm.AddDateTime(builder, date_time)
        csm.AddSessionId(builder, session_id)
        csm.AddSubscriberId(builder, subscriber_id)
        csm.AddApplicationName(builder, application_name)
        csm.AddMessageType(builder, ComponentType.COMPONENT)
        csm.AddSource(builder, source)
        csm.AddDestination(builder, destination)
        csm.AddDocSource(builder, doc_source)

        message = csm.End(builder)

        builder.Finish(message)
        buf: bytes = builder.Output()

        if TestSerDe.file_result:
            with open(TestSerDe.CSTREAM_BIN, "wb") as f:
                f.write(buf)
        else:
            TestSerDe.buf = buf

    def test_02_read_conversation_stream_message(self) -> None:
        buf: bytes = []
        if TestSerDe.file_result:
            with open(TestSerDe.CSTREAM_BIN, "rb") as f:
                buf = f.read()
        else:
            buf = TestSerDe.buf

        msg: ConversationStreamMessage = (
            ConversationStreamMessage.GetRootAsConversationStreamMessage(buf, 0)
        )

        sequence_number: int = msg.SequenceNumber()
        assert sequence_number == 1

        content: ndarray = msg.ContentAsNumpy()
        assert content is not None
        bytes_content: bytes = content.tobytes()
        assert bytes_content == b"\x01\x02\x03"

        date_time: str = msg.DateTime().decode()
        assert date_time == "2024-08-15T12:34:56Z"

        session_id = msg.SessionId().decode()
        assert session_id == "session_id_123"

        subscriber_id = msg.SubscriberId().decode()
        assert subscriber_id == "subscriber_id_456"

        application_name = msg.ApplicationName().decode()
        assert application_name == "app_name"

        source: str = msg.Source().decode()
        assert source == "source"

        destination: str = msg.Destination().decode()
        assert destination == "destination"

        doc_source: str = msg.DocSource().decode()
        assert doc_source == "doc_source"


def run_many(n: int) -> None:
    test: TestSerDe = TestSerDe()
    start: int = time.time_ns()
    for _ in range(n):
        test.test_01_create_conversation_stream_message()
        test.test_02_read_conversation_stream_message()

    took: int = (time.time_ns() - start) // 1_000_000
    print(
        f"Took: {took} ms {1000*n/took} msg/s "
        f" message size:{len(TestSerDe.buf)}"
    )


if __name__ == "__main__":
    run_many(100_000)
    TestSerDe.file_result = True
    unittest.main()
