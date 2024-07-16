package sco3;

import static java.nio.file.Paths.get;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.file.Files;

import com.google.flatbuffers.FlatBufferBuilder;

import sco3fb.Hello;

public class TestFb {
	private static final String JAVA_FB_FILE = "/tmp/hello-java.fb";
	private static final String PYTHON_FB_FILE = "/tmp/hello-python.fb";

	public static void main(String[] argv) throws IOException {
		writeToFile();
		readFromFile();
		readFromPythonFile();
	}

	private static void readFromFile() throws IOException {
		if (Files.exists(get(JAVA_FB_FILE))) {
			byte[] b = Files.readAllBytes(get(JAVA_FB_FILE));
			Hello hello = Hello.getRootAsHello(ByteBuffer.wrap(b));
			System.out.println("" //
					+ "From " + JAVA_FB_FILE + " " //
					+ hello.name() + " " + hello.size()//
			);
		}
	}

	private static void readFromPythonFile() throws IOException {
		if (Files.exists(get(PYTHON_FB_FILE))) {
			byte[] b = Files.readAllBytes(get(PYTHON_FB_FILE));
			Hello hello = Hello.getRootAsHello(ByteBuffer.wrap(b));
			System.out.println("" //
					+ "From " + PYTHON_FB_FILE + " " //
					+ hello.name() + " " + hello.size()//
			);
		}
	}

	private static void writeToFile() throws IOException {
		FlatBufferBuilder bld = new FlatBufferBuilder(1024);
		int offset = bld.createString("Hello");
		Hello.startHello(bld);
		Hello.addName(bld, offset);
		Hello.addSize(bld, 314);
		offset = Hello.endHello(bld);
		bld.finish(offset);
		byte[] buf = bld.sizedByteArray();

		Files.write(get(JAVA_FB_FILE), buf);

	}

}
