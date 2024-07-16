package sco3;

import static java.lang.System.out;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;
import sco3fb.Hello;

import java.io.IOException;
import java.nio.file.Files;

import com.google.flatbuffers.FlatBufferBuilder;

public class TestFb {
	private static final String JAVA_FB_FILE = "/tmp/java.fb";
	private static final String PYTHON_FB_FILE = "/tmp/python.fb";

	public static void main(String[] argv) throws IOException {
		writeToFile();
		readFromFile();
		readFromPythonFile();
	}

	private static void readFromFile() throws IOException {
//		byte[] b = readAllBytes(get(JAVA_FB_FILE));
//		Hello aHello = Hello.parseFrom(b);
//		out.println("Data from file: " + JAVA_FB_FILE + " -> [\n" + aHello.getName() + "]");
	}

	private static void readFromPythonFile() throws IOException {
//		if (Files.exists(get(PYTHON_FB_FILE))) {
//			byte[] b = readAllBytes(get(PYTHON_FB_FILE));
//			Hello aHello = Hello.parseFrom(b);
//			out.println("Data from python file: " + JAVA_FB_FILE + " -> [\n" + aHello + "]");
//		} else {
//			out.println("Python file does not exist: " + PYTHON_FB_FILE);
//		}
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
