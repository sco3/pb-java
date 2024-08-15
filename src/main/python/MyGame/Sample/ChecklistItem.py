# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from typing import Optional
np = import_numpy()

class ChecklistItem(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ChecklistItem()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsChecklistItem(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ChecklistItem
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ChecklistItem
    def Id(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ChecklistItem
    def Name(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ChecklistItem
    def Description(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ChecklistItem
    def NextSessionGoal(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ChecklistItemStart(builder: flatbuffers.Builder):
    builder.StartObject(4)

def Start(builder: flatbuffers.Builder):
    ChecklistItemStart(builder)

def ChecklistItemAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder: flatbuffers.Builder, id: int):
    ChecklistItemAddId(builder, id)

def ChecklistItemAddName(builder: flatbuffers.Builder, name: int):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder: flatbuffers.Builder, name: int):
    ChecklistItemAddName(builder, name)

def ChecklistItemAddDescription(builder: flatbuffers.Builder, description: int):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(description), 0)

def AddDescription(builder: flatbuffers.Builder, description: int):
    ChecklistItemAddDescription(builder, description)

def ChecklistItemAddNextSessionGoal(builder: flatbuffers.Builder, nextSessionGoal: int):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(nextSessionGoal), 0)

def AddNextSessionGoal(builder: flatbuffers.Builder, nextSessionGoal: int):
    ChecklistItemAddNextSessionGoal(builder, nextSessionGoal)

def ChecklistItemEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return ChecklistItemEnd(builder)
