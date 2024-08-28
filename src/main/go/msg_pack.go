package main

import (
	"bytes"
	"fmt"
	"time"

	"github.com/vmihailenco/msgpack/v5"
)

type ConversationStreamMessageField int
type ComponentType int

const (
	SEQUENCE_NUMBER ConversationStreamMessageField = iota
	ANY
	CONTENT
	DATE_TIME
	SESSION_ID
	SUBSCRIBER_ID
	APPLICATION_NAME
	MESSAGE_TYPE
	SOURCE
	DESTINATION
	DOC_SOURCE
)

const (
	UNKNOWN ComponentType = iota
	TEXT
	IMAGE
)

type MessageData struct {
	SequenceNumber  int           `msgpack:"0"`
	Any             []byte        `msgpack:"1"`
	Content         string        `msgpack:"2"`
	DateTime        string        `msgpack:"3"`
	SessionID       string        `msgpack:"4"`
	SubscriberID    string        `msgpack:"5"`
	ApplicationName string        `msgpack:"6"`
	MessageType     ComponentType `msgpack:"7"`
	Source          string        `msgpack:"8"`
	Destination     string        `msgpack:"9"`
	DocSource       string        `msgpack:"10"`
}

var messageSize int

func testOnce(i int) {
	bbuf := make([]byte, 150)
	bbuf[0] = byte(i % 127)

	data := MessageData{
		SequenceNumber:  i,
		Any:             bbuf,
		Content:         "Hello, this is a test",
		DateTime:        "2024-08-15T12:34:56Z",
		SessionID:       "session_id_123",
		SubscriberID:    "subscriber_id_456",
		ApplicationName: "app_name",
		MessageType:     TEXT,
		Source:          "source",
		Destination:     "destination",
		DocSource:       fmt.Sprintf("doc_source%d", i),
	}

	var buf bytes.Buffer
	enc := msgpack.NewEncoder(&buf)
	err := enc.Encode(data)
	if err != nil {
		fmt.Printf("Failed to serialize: %v", err)
	}

	serializedData := buf.Bytes()
	messageSize = len(serializedData)

	var deserializedData MessageData
	dec := msgpack.NewDecoder(bytes.NewReader(serializedData))
	err = dec.Decode(&deserializedData)
	if err != nil {
		fmt.Printf("Failed to deserialize: %v", err)
	}

}

func testMany(n int) {
	start := time.Now()
	for i := 0; i < n; i++ {
		testOnce(i)
	}
	took := time.Since(start).Milliseconds()
	fmt.Printf("Took: %d ms, %d msg/s, message size: %d bytes\n", took, 1000*n/int(took), messageSize)
}

func TestSerDeMp() {
	testOnce(0)
	testMany(1000000)
}

func main() {
	TestSerDeMp()
}
