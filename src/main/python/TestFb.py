#!/usr/bin/env -s poetry run python

import os
import sco3fb.Hello as Hello
import flatbuffers

PYTHON_FB = "/tmp/hello-python.fb"
JAVA_FB = "/tmp/hello-java.fb"

bld = flatbuffers.Builder(1024)
name = bld.CreateString("Hello")
Hello.Start(bld)
Hello.AddSize(bld, 314)
Hello.AddName(bld, name)
offset: int = Hello.End(bld)
h = bld.Finish(offset)
buf = bld.Output()

with open(PYTHON_FB, "wb") as out_file:
    out_file.write(buf)

if os.path.exists(JAVA_FB):
    with open(JAVA_FB, "rb") as in_file:
        bytes = in_file.read()
        h = Hello.Hello.GetRootAs(bytes, 0)
        print(h.Name().decode("utf-8"), h.Size())
