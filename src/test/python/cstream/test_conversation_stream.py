import unittest

import flatbuffers
from MyGame.Sample.ComponentType import ComponentType
from MyGame.Sample import ConversationStreamMessage as csm
from MyGame.Sample.ConversationStreamMessage import ConversationStreamMessage
from typing import ClassVar
from numpy import ndarray


class TestSerDe(unittest.TestCase):
    CSTREAM_BIN: ClassVar[str] = "/tmp/cstream.bin"

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

        with open(TestSerDe.CSTREAM_BIN, "wb") as f:
            f.write(buf)

    def test_02_read_conversation_stream_message(self) -> None:
        with open(TestSerDe.CSTREAM_BIN, "rb") as f:
            buf: bytes = f.read()

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


if __name__ == "__main__":
    unittest.main()
