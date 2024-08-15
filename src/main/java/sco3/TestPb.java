package sco3;

import static java.lang.System.out;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;
import static sco3.Test.Hello.newBuilder;

import java.io.IOException;
import java.nio.file.Files;

import com.google.protobuf.Any;

import sco3.Test.Hello;

public class TestPb {
	private static final String PB_FILE = "/tmp/a-hello.pb";
	private static final String PYTHON_PB_FILE = "/tmp/a-hello-python.pb";

	public static void main(String[] argv) throws IOException {
		writeToFile();
		readFromFile();
		readFromPythonFile();
	}

	private static void readFromFile() throws IOException {
		byte[] b = readAllBytes(get(PB_FILE));
		Hello aHello = Hello.parseFrom(b);
		out.println("Data from file: " + PB_FILE + " -> [\n" + aHello.getName() + "]");
	}

	private static void readFromPythonFile() throws IOException {
		if (Files.exists(get(PYTHON_PB_FILE))) {
			byte[] b = readAllBytes(get(PYTHON_PB_FILE));
			Hello aHello = Hello.parseFrom(b);
			out.println("Data from python file: " + PB_FILE + " -> [\n" + aHello + "]");
		} else {
			out.println("Python file does not exist: " + PYTHON_PB_FILE);
		}
	}

	private static void writeToFile() throws IOException {
		Hello nested = newBuilder().setName("Nested").build();
		Hello aHello = newBuilder() //
				.setName("hello from java")//
				.setContent(Any.pack(nested)).build();
		out.println("Data to save -> [\n" + aHello + "]");

		byte[] b = aHello.toByteArray();
		Files.write(get(PB_FILE), b);
		out.println("Binary was saved to " + PB_FILE);
	}
}
