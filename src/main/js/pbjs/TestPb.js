

const minimal = require('protobufjs/minimal')
const proto = require('./test_pbjs');

const A_HELLO_PB = '/tmp/a-hello.pb'

function main() {
	const fs = require('fs');
	try {
		var stats = fs.statSync(A_HELLO_PB);
		var fd = fs.openSync(A_HELLO_PB, 'r');
		var buffer = Buffer.alloc(stats.size);
		fs.readSync(fd, buffer, 0, stats.size, 0);
		var h = proto.sco3.Hello.decode(buffer);
		console.log(h.name);
		console.log(h);
	} catch (e) {
		console.log("Problem: " + e);
	}
}

if (require.main === module) {
	main();
}