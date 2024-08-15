from . import packer as packer
from .compat import NumpyRequiredForThisFeature as NumpyRequiredForThisFeature, import_numpy as import_numpy, memoryview_type as memoryview_type
from _typeshed import Incomplete

np: Incomplete
FILE_IDENTIFIER_LENGTH: int

def Get(packer_type, buf, head): ...
def GetVectorAsNumpy(numpy_type, buf, count, offset): ...
def Write(packer_type, buf, head, n) -> None: ...
