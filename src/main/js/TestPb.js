

const goog = require('google-protobuf')
const testProto = require('./test_pb');

const A_HELLO_PB = '/tmp/a-hello.pb'

function main() {
	const fs = require('fs');
	try {
		var stats = fs.statSync(A_HELLO_PB);
		var fd = fs.openSync(A_HELLO_PB, 'r');
		var buffer = Buffer.alloc(stats.size);
		fs.readSync(fd, buffer, 0, stats.size, 0);
		var h = proto.sco3.Hello.deserializeBinary(buffer);
		console.log(h.getName());
		console.log(h);
	} catch (e) {
		console.log("Problem: " + e);
	}
}

if (require.main === module) {
	main();
}