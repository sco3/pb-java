#!/usr/bin/env python3

import test_pb2
from typing import reveal_type, Any
import inspect

print (dir(test_pb2.Hello))

test = test_pb2.Hello()
test.name = 'hello from python'
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
