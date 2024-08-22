import msgpack
from enum import Enum
import datetime


# Define enums for the fields of ConversationStreamMessage
class MessageField(Enum):
    SEQUENCE_NUMBER = 1
    CONTENT = 2
    DATE_TIME = 3
    SESSION_ID = 4
    SUBSCRIBER_ID = 5
    APPLICATION_NAME = 6
    MESSAGE_TYPE = 7
    SOURCE = 8
    DESTINATION = 9
    DOC_SOURCE = 10


class ComponentType(Enum):
    UNKNOWN = 0
    TEXT = 1
    IMAGE = 2


# A function to serialize the structure using enums as keys (dict[int, any])
def serialize_to_msgpack(data_dict):
    # Replace field names with enum values and pack into msgpack format
    packed_data = {
        MessageField.SEQUENCE_NUMBER: data_dict.get(
            MessageField.SEQUENCE_NUMBER
        ),
        MessageField.CONTENT: data_dict.get(MessageField.CONTENT),
        MessageField.DATE_TIME: data_dict.get(MessageField.DATE_TIME),
        MessageField.SESSION_ID: data_dict.get(MessageField.SESSION_ID),
        MessageField.SUBSCRIBER_ID: data_dict.get(MessageField.SUBSCRIBER_ID),
        MessageField.APPLICATION_NAME: data_dict.get(
            MessageField.APPLICATION_NAME
        ),
        MessageField.MESSAGE_TYPE: data_dict.get(MessageField.MESSAGE_TYPE),
        MessageField.SOURCE: data_dict.get(MessageField.SOURCE),
        MessageField.DESTINATION: data_dict.get(MessageField.DESTINATION),
        MessageField.DOC_SOURCE: data_dict.get(MessageField.DOC_SOURCE),
    }

    # Serialize to msgpack
    return msgpack.packb(packed_data)


# A function to deserialize msgpack data back to dict[int, any]
def deserialize_from_msgpack(packed_data):
    # Unpack msgpack data
    unpacked_data = msgpack.unpackb(packed_data, strict_map_key=False)

    # The unpacked data will already be dict[int, any]
    return unpacked_data


# Example usage
if __name__ == "__main__":
    # Create a dictionary with enum values as keys (dict[int, any])
    original_data = {
        MessageField.SEQUENCE_NUMBER: 1,
        MessageField.CONTENT: b"Hello, this is a test",  # Stored as bytes
        MessageField.DATE_TIME: datetime.datetime.now().isoformat(),
        MessageField.SESSION_ID: "session123",
        MessageField.SUBSCRIBER_ID: "subscriber456",
        MessageField.APPLICATION_NAME: "MyApp",
        MessageField.MESSAGE_TYPE: ComponentType.TEXT,  # Enum value for TEXT
        MessageField.SOURCE: "source_a",
        MessageField.DESTINATION: "destination_b",
        MessageField.DOC_SOURCE: "doc_src_001",
    }

    # Serialize the dictionary to msgpack format
    serialized_data = serialize_to_msgpack(original_data)
    print("Serialized data (msgpack):", len(serialized_data))

    # Deserialize the data back to dict[int, any]
    deserialized_data = deserialize_from_msgpack(serialized_data)
    print("Deserialized data (dict[int, any]):", deserialized_data)
