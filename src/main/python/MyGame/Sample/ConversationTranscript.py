# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Sample

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ConversationTranscript(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ConversationTranscript()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsConversationTranscript(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ConversationTranscript
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ConversationTranscript
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # ConversationTranscript
    def Conversation(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from MyGame.Sample.ConversationItem import ConversationItem
            obj = ConversationItem()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ConversationTranscript
    def ConversationLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # ConversationTranscript
    def ConversationIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def ConversationTranscriptStart(builder):
    builder.StartObject(2)

def Start(builder):
    ConversationTranscriptStart(builder)

def ConversationTranscriptAddId(builder, id):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(id), 0)

def AddId(builder, id):
    ConversationTranscriptAddId(builder, id)

def ConversationTranscriptAddConversation(builder, conversation):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(conversation), 0)

def AddConversation(builder, conversation):
    ConversationTranscriptAddConversation(builder, conversation)

def ConversationTranscriptStartConversationVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartConversationVector(builder, numElems: int) -> int:
    return ConversationTranscriptStartConversationVector(builder, numElems)

def ConversationTranscriptEnd(builder):
    return builder.EndObject()

def End(builder):
    return ConversationTranscriptEnd(builder)
