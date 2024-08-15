#!/usr/bin/env poetry run python

import test_pb2
from test_pb2 import Hello
from typing import reveal_type, Any
import inspect

from pathlib import Path


def main() -> None:
    A_HELLO_PB: str = "/tmp/a-hello.pb"

    print(dir(Hello))

    test = Hello()
    test.name = "hello from python"
    print(f"{test}")
    testString = test.SerializeToString()

    with open("/tmp/a-hello-python.pb", "wb") as out_file:
        out_file.write(testString)

    if Path(A_HELLO_PB).exists():
        with open(A_HELLO_PB, "rb") as in_file:
            bytes = in_file.read()
            test2 = Hello()
            test2.ParseFromString(bytes)
            print(f"{test2}")
            print(f"{test2.name}")


if __name__ == "__main__":
    main()
