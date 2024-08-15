// automatically generated by the FlatBuffers compiler, do not modify

package MyGame.Sample;

import com.google.flatbuffers.BaseVector;
import com.google.flatbuffers.BooleanVector;
import com.google.flatbuffers.ByteVector;
import com.google.flatbuffers.Constants;
import com.google.flatbuffers.DoubleVector;
import com.google.flatbuffers.FlatBufferBuilder;
import com.google.flatbuffers.FloatVector;
import com.google.flatbuffers.IntVector;
import com.google.flatbuffers.LongVector;
import com.google.flatbuffers.ShortVector;
import com.google.flatbuffers.StringVector;
import com.google.flatbuffers.Struct;
import com.google.flatbuffers.Table;
import com.google.flatbuffers.UnionVector;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;

@SuppressWarnings("unused")
public final class PhaseNode extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_23_5_26(); }
  public static PhaseNode getRootAsPhaseNode(ByteBuffer _bb) { return getRootAsPhaseNode(_bb, new PhaseNode()); }
  public static PhaseNode getRootAsPhaseNode(ByteBuffer _bb, PhaseNode obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public PhaseNode __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public String id() { int o = __offset(4); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer idAsByteBuffer() { return __vector_as_bytebuffer(4, 1); }
  public ByteBuffer idInByteBuffer(ByteBuffer _bb) { return __vector_in_bytebuffer(_bb, 4, 1); }
  public String name() { int o = __offset(6); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer nameAsByteBuffer() { return __vector_as_bytebuffer(6, 1); }
  public ByteBuffer nameInByteBuffer(ByteBuffer _bb) { return __vector_in_bytebuffer(_bb, 6, 1); }
  public MyGame.Sample.GoalItem goals(int j) { return goals(new MyGame.Sample.GoalItem(), j); }
  public MyGame.Sample.GoalItem goals(MyGame.Sample.GoalItem obj, int j) { int o = __offset(8); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int goalsLength() { int o = __offset(8); return o != 0 ? __vector_len(o) : 0; }
  public MyGame.Sample.GoalItem.Vector goalsVector() { return goalsVector(new MyGame.Sample.GoalItem.Vector()); }
  public MyGame.Sample.GoalItem.Vector goalsVector(MyGame.Sample.GoalItem.Vector obj) { int o = __offset(8); return o != 0 ? obj.__assign(__vector(o), 4, bb) : null; }
  public MyGame.Sample.ChecklistItem checklist(int j) { return checklist(new MyGame.Sample.ChecklistItem(), j); }
  public MyGame.Sample.ChecklistItem checklist(MyGame.Sample.ChecklistItem obj, int j) { int o = __offset(10); return o != 0 ? obj.__assign(__indirect(__vector(o) + j * 4), bb) : null; }
  public int checklistLength() { int o = __offset(10); return o != 0 ? __vector_len(o) : 0; }
  public MyGame.Sample.ChecklistItem.Vector checklistVector() { return checklistVector(new MyGame.Sample.ChecklistItem.Vector()); }
  public MyGame.Sample.ChecklistItem.Vector checklistVector(MyGame.Sample.ChecklistItem.Vector obj) { int o = __offset(10); return o != 0 ? obj.__assign(__vector(o), 4, bb) : null; }

  public static int createPhaseNode(FlatBufferBuilder builder,
      int idOffset,
      int nameOffset,
      int goalsOffset,
      int checklistOffset) {
    builder.startTable(4);
    PhaseNode.addChecklist(builder, checklistOffset);
    PhaseNode.addGoals(builder, goalsOffset);
    PhaseNode.addName(builder, nameOffset);
    PhaseNode.addId(builder, idOffset);
    return PhaseNode.endPhaseNode(builder);
  }

  public static void startPhaseNode(FlatBufferBuilder builder) { builder.startTable(4); }
  public static void addId(FlatBufferBuilder builder, int idOffset) { builder.addOffset(0, idOffset, 0); }
  public static void addName(FlatBufferBuilder builder, int nameOffset) { builder.addOffset(1, nameOffset, 0); }
  public static void addGoals(FlatBufferBuilder builder, int goalsOffset) { builder.addOffset(2, goalsOffset, 0); }
  public static int createGoalsVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startGoalsVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static void addChecklist(FlatBufferBuilder builder, int checklistOffset) { builder.addOffset(3, checklistOffset, 0); }
  public static int createChecklistVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startChecklistVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static int endPhaseNode(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public PhaseNode get(int j) { return get(new PhaseNode(), j); }
    public PhaseNode get(PhaseNode obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
  }
}

