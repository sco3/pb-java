import time
from typing import ClassVar
import unittest


class TestSerDe(unittest.TestCase):
    CSTREAM_BIN: ClassVar[str] = "/tmp/cstream.bin"
    file_result: bool = False
    buf: bytes = b""

    def test_01_create_conversation_stream_message(self) -> None:
        pass

    def test_02_read_conversation_stream_message(self) -> None:
        pass
