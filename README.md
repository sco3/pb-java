

In order to generate mypy stubs for python protobuf install mypy-protobuf

```
python -m pip install mypy-protobuf

ln -s ~/.local/bin/protoc-gen-mypy ~/bin
```


Generate pb classes:
```
gradle clean generateProto

```
