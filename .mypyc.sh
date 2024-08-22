#!/usr/bin/env -S bash

set -xueo pipefail



   stubs=$(readlink -f .stubs)
   cd src

   python=$(poetry env info --path)/bin/python
   dirs=$(find . -name *.py -exec dirname \{\} \;  | grep -v 'conversationstream/protobuf' | grep -v 'src/build'  ) 
   MYPYPATH="$stubs" $python -m mypyc --python-executable $python "$1"


