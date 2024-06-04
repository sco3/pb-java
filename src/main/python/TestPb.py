#!/usr/bin/env python3

import test_pb2 
from typing import reveal_type

test  = test_pb2.Hello()
reveal_type (test)
test.name = 'asdf'
print (f"{test}")




