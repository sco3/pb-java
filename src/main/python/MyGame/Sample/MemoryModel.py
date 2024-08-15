# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MemoryModel(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MemoryModel()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMemoryModel(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MemoryModel
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MemoryModel
    def MemoryFields(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from MyGame.Sample.MemoryField import MemoryField
            obj = MemoryField()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MemoryModel
    def MemoryFieldsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MemoryModel
    def MemoryFieldsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def MemoryModelStart(builder):
    builder.StartObject(1)

def Start(builder):
    MemoryModelStart(builder)

def MemoryModelAddMemoryFields(builder, memoryFields):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(memoryFields), 0)

def AddMemoryFields(builder, memoryFields):
    MemoryModelAddMemoryFields(builder, memoryFields)

def MemoryModelStartMemoryFieldsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMemoryFieldsVector(builder, numElems: int) -> int:
    return MemoryModelStartMemoryFieldsVector(builder, numElems)

def MemoryModelEnd(builder):
    return builder.EndObject()

def End(builder):
    return MemoryModelEnd(builder)
