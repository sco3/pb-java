package msgpack;

import org.junit.jupiter.api.Test;
import org.msgpack.core.MessagePack;
import org.msgpack.core.MessageUnpacker;
import org.msgpack.core.MessageBufferPacker;

import java.io.IOException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

public class TestMsgPack {

    private static int messageSize;

    public enum ConversationStreamMessageField {
        SEQUENCE_NUMBER,
        ANY,
        CONTENT,
        DATE_TIME,
        SESSION_ID,
        SUBSCRIBER_ID,
        APPLICATION_NAME,
        MESSAGE_TYPE,
        SOURCE,
        DESTINATION,
        DOC_SOURCE
    }

    public enum ComponentType {
        UNKNOWN,
        TEXT,
        IMAGE
    }

    public static void testOnce(int i) throws IOException {
        // Prepare byte buffer
        byte[] bbuf = new byte[150];
        bbuf[0] = (byte) (i % 127);

        // Create a dictionary with enum values as keys
        Map<ConversationStreamMessageField, Object> dataMap = new HashMap<>();
        dataMap.put(ConversationStreamMessageField.SEQUENCE_NUMBER, i);
        dataMap.put(ConversationStreamMessageField.ANY, bbuf);
        dataMap.put(ConversationStreamMessageField.CONTENT, "Hello, this is a test");
        dataMap.put(ConversationStreamMessageField.DATE_TIME, "2024-08-15T12:34:56Z");
        dataMap.put(ConversationStreamMessageField.SESSION_ID, "session_id_123");
        dataMap.put(ConversationStreamMessageField.SUBSCRIBER_ID, "subscriber_id_456");
        dataMap.put(ConversationStreamMessageField.APPLICATION_NAME, "app_name");
        dataMap.put(ConversationStreamMessageField.MESSAGE_TYPE, ComponentType.TEXT.ordinal());
        dataMap.put(ConversationStreamMessageField.SOURCE, "source");
        dataMap.put(ConversationStreamMessageField.DESTINATION, "destination");
        dataMap.put(ConversationStreamMessageField.DOC_SOURCE, "doc_source" + i);

        // Serialize the map to msgpack format
        MessageBufferPacker packer = MessagePack.newDefaultBufferPacker();
        packMap(packer, dataMap);
        byte[] serializedData = packer.toByteArray();
        packer.close();

        messageSize = serializedData.length;

        // Deserialize the data back to map
        MessageUnpacker unpacker = MessagePack.newDefaultUnpacker(serializedData);
        Map<ConversationStreamMessageField, Object> deserializedData = unpackMap(unpacker);
        unpacker.close();

//        if (i == 0) {
//            assertEquals(dataMap, deserializedData);
//        }
    }

    public static void testMany(int n) throws IOException {
        long start = System.nanoTime();
        for (int i = 0; i < n; i++) {
            testOnce(i);
        }
        long took = (System.nanoTime() - start) / 1_000_000;
        System.out.printf("Took: %d ms %d msg/s message size: %d bytes%n",
                took, 1000L * n / took, messageSize);
    }

    @Test
    public void testSerDe() throws IOException {
        testOnce(0);
        testMany(1_000_000);
    }

    private static void packMap(MessageBufferPacker packer, Map<ConversationStreamMessageField, Object> map) throws IOException {
        packer.packMapHeader(map.size());
        for (Map.Entry<ConversationStreamMessageField, Object> entry : map.entrySet()) {
            packer.packInt(entry.getKey().ordinal());
            if (entry.getValue() instanceof byte[]) {
                packer.packBinaryHeader(((byte[]) entry.getValue()).length);
                packer.writePayload((byte[]) entry.getValue());
            } else if (entry.getValue() instanceof Integer) {
                packer.packInt((Integer) entry.getValue());
            } else if (entry.getValue() instanceof String) {
                packer.packString((String) entry.getValue());
            } else {
                fail("Unexpected value type");
            }
        }
    }

    private static Map<ConversationStreamMessageField, Object> unpackMap(MessageUnpacker unpacker) throws IOException {
        int mapSize = unpacker.unpackMapHeader();
        Map<ConversationStreamMessageField, Object> map = new HashMap<>();
        for (int i = 0; i < mapSize; i++) {
            ConversationStreamMessageField key = ConversationStreamMessageField.values()[unpacker.unpackInt()];
            switch (key) {
                case ANY:
                    int length = unpacker.unpackBinaryHeader();
                    byte[] bbuf = new byte[length];
                    unpacker.readPayload(bbuf);
                    map.put(key, bbuf);
                    break;
                case SEQUENCE_NUMBER:
                case MESSAGE_TYPE:
                    map.put(key, unpacker.unpackInt());
                    break;
                default:
                    map.put(key, unpacker.unpackString());
                    break;
            }
        }
        return map;
    }

    public static void main(String[] args) throws IOException {
        TestMsgPack tester = new TestMsgPack();
        tester.testSerDe();
    }
}
