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
public final class GoalItem extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_23_5_26(); }
  public static GoalItem getRootAsGoalItem(ByteBuffer _bb) { return getRootAsGoalItem(_bb, new GoalItem()); }
  public static GoalItem getRootAsGoalItem(ByteBuffer _bb, GoalItem obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public GoalItem __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public String id() { int o = __offset(4); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer idAsByteBuffer() { return __vector_as_bytebuffer(4, 1); }
  public ByteBuffer idInByteBuffer(ByteBuffer _bb) { return __vector_in_bytebuffer(_bb, 4, 1); }
  public String goalDescription() { int o = __offset(6); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer goalDescriptionAsByteBuffer() { return __vector_as_bytebuffer(6, 1); }
  public ByteBuffer goalDescriptionInByteBuffer(ByteBuffer _bb) { return __vector_in_bytebuffer(_bb, 6, 1); }

  public static int createGoalItem(FlatBufferBuilder builder,
      int idOffset,
      int goalDescriptionOffset) {
    builder.startTable(2);
    GoalItem.addGoalDescription(builder, goalDescriptionOffset);
    GoalItem.addId(builder, idOffset);
    return GoalItem.endGoalItem(builder);
  }

  public static void startGoalItem(FlatBufferBuilder builder) { builder.startTable(2); }
  public static void addId(FlatBufferBuilder builder, int idOffset) { builder.addOffset(0, idOffset, 0); }
  public static void addGoalDescription(FlatBufferBuilder builder, int goalDescriptionOffset) { builder.addOffset(1, goalDescriptionOffset, 0); }
  public static int endGoalItem(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public GoalItem get(int j) { return get(new GoalItem(), j); }
    public GoalItem get(GoalItem obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
  }
}
