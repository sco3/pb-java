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


class TestCustomSerDeMp(unittest.TestCase):

    message_size: ClassVar[int] = 0

    def test_once(self, i: int = 0) -> None:

        msg: bytes = b""

        # test any data for "any" field
        bbuf: bytearray = bytearray(150)
        bbuf[0] = i % 127

        msg += msgpack.packb(i)
        msg += msgpack.packb(bbuf)
        msg += msgpack.packb(b"Hello, this is a test")
        msg += msgpack.packb("2024-08-15T12:34:56Z")
        msg += msgpack.packb("session_id_123")
        msg += msgpack.packb("subscriber_id_456")
        msg += msgpack.packb("app_name")
        msg += msgpack.packb(ComponentType.TEXT)
        msg += msgpack.packb("source")
        msg += msgpack.packb("destination")
        msg += msgpack.packb(f"doc_source{i}")

        TestCustomSerDeMp.message_size = len(msg)

        unpacker = msgpack.Unpacker()
        unpacker.feed(msg)

        sequence_number: int = unpacker.unpack()
        any: bytes = unpacker.unpack()
        content: bytes = unpacker.unpack()
        date_time: str = unpacker.unpack()
        session_id: str = unpacker.unpack()
        subscriber_id: str = unpacker.unpack()
        application_name: str = unpacker.unpack()
        message_type: ComponentType = unpacker.unpack()
        source: str = unpacker.unpack()
        destination: str = unpacker.unpack()
        doc_source: str = unpacker.unpack()

    def test_many(self, n: int = 1000000) -> None:

        start: int = time.time_ns()
        for i in range(n):
            self.test_once(i)

        took: int = (time.time_ns() - start) // 1_000_000
        print(
            f"Took: {took} ms {1000*n/took} msg/s "
            f" message size: {TestCustomSerDeMp.message_size}"
        )


# Example usage
if __name__ == "__main__":
    # test_msg_pack.run_many(1000000)
    unittest.main()
