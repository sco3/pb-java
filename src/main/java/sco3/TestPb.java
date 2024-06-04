package sco3;

import static java.lang.System.out;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

import sco3.Test.Hello;

public class TestPb {
	public static void main(String[] argv) throws IOException {
		Hello aHello = Hello.newBuilder().setName("asdf").build();
		out.println(aHello);
		byte[] b = aHello.toByteArray();
		Files.write(Paths.get("/tmp/a-hello.pb"), b);
	}
}
