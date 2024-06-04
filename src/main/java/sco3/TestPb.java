package sco3;

import static java.lang.System.out;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;
import static sco3.Test.Hello.newBuilder;

import java.io.IOException;
import java.nio.file.Files;

import sco3.Test.Hello;

public class TestPb {
	private static final String PB_FILE = "/tmp/a-hello.pb";

	public static void main(String[] argv) throws IOException {
		writeToFile();
		readFromFile();
	}

	private static void readFromFile() throws IOException {
		byte[] b = readAllBytes(get(PB_FILE));
		Hello aHello = Hello.parseFrom(b);
		out.println("Data from file: " + PB_FILE + " -> [\n" + aHello + "]");
	}

	private static void writeToFile() throws IOException {
		Hello aHello = newBuilder().setName("asdf").build();
		out.println("Data to save -> [\n" + aHello + "]");

		byte[] b = aHello.toByteArray();
		Files.write(get(PB_FILE), b);
		out.println("Binary was saved to " + PB_FILE);
	}
}
