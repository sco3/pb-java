package sco3;

import static java.lang.System.out;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import sco3.Test.Hello;

public class TestPb {
	private static final String PB_FILE = "/tmp/a-hello.pb";

	public static void main(String[] argv) throws IOException {
		Hello aHello = Hello.newBuilder().setName("asdf").build();
		out.println("Data: " + aHello);
		byte[] b = aHello.toByteArray();
		Files.write(Paths.get(PB_FILE), b);
		out.println("Binary was saved to " + PB_FILE);
	}
}
