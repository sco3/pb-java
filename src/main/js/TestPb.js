

const goog = require('google-protobuf')
const testProto = require('./test_pb');

const A_HELLO_PB = '/tmp/a-hello.pb'

function main() {
	const fs = require('fs');
	if (fs.existsSync(A_HELLO_PB)) {
		var stats = fs.statSync(A_HELLO_PB);
		fs.open(A_HELLO_PB, 'r', function(status, fd) {
			if (status) {
				console.log(status.message);
				return;
			}
			var buffer = Buffer.alloc(stats.size);
			fs.read(fd, buffer, 0, stats.size, 0, function(err, num) {
				var h = proto.sco3.Hello.deserializeBinary(buffer)
				console.log(h.getName());
			});
		});
	}
}

if (require.main === module) {
	main();
}