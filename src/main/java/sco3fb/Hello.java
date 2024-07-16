// automatically generated by the FlatBuffers compiler, do not modify

package sco3fb;

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
public final class Hello extends Table {
  public static void ValidateVersion() { Constants.FLATBUFFERS_23_5_26(); }
  public static Hello getRootAsHello(ByteBuffer _bb) { return getRootAsHello(_bb, new Hello()); }
  public static Hello getRootAsHello(ByteBuffer _bb, Hello obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__assign(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public void __init(int _i, ByteBuffer _bb) { __reset(_i, _bb); }
  public Hello __assign(int _i, ByteBuffer _bb) { __init(_i, _bb); return this; }

  public String name() { int o = __offset(4); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer nameAsByteBuffer() { return __vector_as_bytebuffer(4, 1); }
  public ByteBuffer nameInByteBuffer(ByteBuffer _bb) { return __vector_in_bytebuffer(_bb, 4, 1); }
  public long size() { int o = __offset(6); return o != 0 ? (long)bb.getInt(o + bb_pos) & 0xFFFFFFFFL : 0L; }

  public static int createHello(FlatBufferBuilder builder,
      int nameOffset,
      long size) {
    builder.startTable(2);
    Hello.addSize(builder, size);
    Hello.addName(builder, nameOffset);
    return Hello.endHello(builder);
  }

  public static void startHello(FlatBufferBuilder builder) { builder.startTable(2); }
  public static void addName(FlatBufferBuilder builder, int nameOffset) { builder.addOffset(0, nameOffset, 0); }
  public static void addSize(FlatBufferBuilder builder, long size) { builder.addInt(1, (int) size, (int) 0L); }
  public static int endHello(FlatBufferBuilder builder) {
    int o = builder.endTable();
    return o;
  }
  public static void finishHelloBuffer(FlatBufferBuilder builder, int offset) { builder.finish(offset); }
  public static void finishSizePrefixedHelloBuffer(FlatBufferBuilder builder, int offset) { builder.finishSizePrefixed(offset); }

  public static final class Vector extends BaseVector {
    public Vector __assign(int _vector, int _element_size, ByteBuffer _bb) { __reset(_vector, _element_size, _bb); return this; }

    public Hello get(int j) { return get(new Hello(), j); }
    public Hello get(Hello obj, int j) {  return obj.__assign(__indirect(__element(j), bb), bb); }
  }
}
