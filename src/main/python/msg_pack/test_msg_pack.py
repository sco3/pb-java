import msgpack
import datetime


# Define enums for the fields of ConversationStreamMessage
class MessageField:
    SEQUENCE_NUMBER = 0
    ANY = 1
    CONTENT = 2
    DATE_TIME = 3
    SESSION_ID = 4
    SUBSCRIBER_ID = 5
    APPLICATION_NAME = 6
    MESSAGE_TYPE = 7
    SOURCE = 8
    DESTINATION = 9
    DOC_SOURCE = 10


class ComponentType:
    UNKNOWN = 0
    TEXT = 1
    IMAGE = 2


# A function to serialize the structure using enums as keys (dict[int, any])
def serialize_to_msgpack(data_dict):
    # Serialize to msgpack
    return msgpack.packb(data_dict)


# A function to deserialize msgpack data back to dict[int, any]
def deserialize_from_msgpack(packed_data):
    # Unpack msgpack data
    unpacked_data = msgpack.unpackb(packed_data, strict_map_key=False)

    # The unpacked data will already be dict[int, any]
    return unpacked_data


def run_once(i: int) -> None:
    # Create a dictionary with enum values as keys (dict[int, any])
    bbuf: bytes = bytearray(150)
    bbuf[0] = 1

    original_data = {
        MessageField.SEQUENCE_NUMBER: 1,
        MessageField.ANY: bbuf,
        MessageField.CONTENT: b"Hello, this is a test",  # Stored as bytes
        MessageField.DATE_TIME: "2024-08-15T12:34:56Z",  # Matching date_time from csm
        MessageField.SESSION_ID: "session_id_123",  # Matching session_id from csm
        MessageField.SUBSCRIBER_ID: "subscriber_id_456",  # Matching subscriber_id from csm
        MessageField.APPLICATION_NAME: "app_name",  # Matching application_name from csm
        MessageField.MESSAGE_TYPE: ComponentType.TEXT,  # Enum value for TEXT remains unchanged
        MessageField.SOURCE: "source",  # Matching source from csm
        MessageField.DESTINATION: "destination",  # Matching destination from csm
        MessageField.DOC_SOURCE: "doc_source0",  # f"doc_source{i}" with i = 0 as an example
    }

    # Serialize the dictionary to msgpack format
    serialized_data = serialize_to_msgpack(original_data)
    print("Serialized data (msgpack):", len(serialized_data))

    # Deserialize the data back to dict[int, any]
    deserialized_data = deserialize_from_msgpack(serialized_data)
    print("Deserialized data (dict[int, any]):", deserialized_data)


# Example usage
if __name__ == "__main__":
    run_once(0)
