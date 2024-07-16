#!/usr/bin/env python3

import sco3fb
import flatbuffers


bld = flatbuffers.Builder(1024)
sco3.Hello.HelloStart(bld)
sco3.Hello.HelloAddName(bld, b"Hello from python!")
sco3.Hello.HelloAddSize(bld, 315)
hello = sco3.Hello.HelloEnd(bld)
bld.Finish(hello)
print(hello)

if False:
    test = test_pb2.Hello()
    test.name = "hello from python"
    print(f"{test}")
    testString = test.SerializeToString()
    with open("/tmp/a-hello-python.pb", "wb") as out_file:
        out_file.write(testString)

    with open("/tmp/a-hello.pb", "rb") as in_file:
        bytes = in_file.read()
        test2 = test_pb2.Hello()
        test2.ParseFromString(bytes)
        print(f"{test2}")
        print(f"{test2.name}")
