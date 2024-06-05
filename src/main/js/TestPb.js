
var goog = require('google-protobuf')
const GEN_DIR = '../../../build/generated/source/proto/main'
var testProto = require(GEN_DIR + '/js/test_pb');

function main() {
	console.log("Aha");
	var h = new proto.sco3.Hello();
	h.setName("aha")
	console.log(h);
}

main();