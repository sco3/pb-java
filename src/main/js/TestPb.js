
var goog = require('google-protobuf')
//const GEN_DIR = '../../../build/generated/source/proto/main'
var testProto = require('./test_pb');

function main() {
	console.log("Aha");
	var h = new proto.sco3.Hello();
	h.setName("aha")
	console.log(h);
}

main();