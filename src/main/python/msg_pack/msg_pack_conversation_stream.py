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


class ConversationStreamMessage:
    def __init__(
        self,
        sequence_number: int = 0, 
        content: bytes = b"",
        date_time: str = "", 
        session_id: str = "",
        subscriber_id: str = "", 
        application_name: str = "",  
        message_type: ComponentType = ComponentType.UNKNOWN,
        source: str = "",  
        destination: str = "",
        doc_source: str = ""  
    ) -> None:
        # Initialize the instance variables
        self.sequence_number = sequence_number
        self.content = content
        self.date_time = date_time
        self.session_id = session_id
        self.subscriber_id = subscriber_id
        self.application_name = application_name
        self.message_type = message_type
        self.source = source
        self.destination = destination
        self.doc_source = doc_source



class ComponentType:
    UNKNOWN: ClassVar[int] = 0
    TEXT: ClassVar[int] = 1
    IMAGE: ClassVar[int] = 2
