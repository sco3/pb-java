package claude;

import static java.lang.System.currentTimeMillis;
import static software.amazon.awssdk.services.bedrockruntime.model.ContentBlock.fromText;

import io.github.cdimascio.dotenv.Dotenv;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.bedrockruntime.BedrockRuntimeClient;
import software.amazon.awssdk.services.bedrockruntime.model.ConversationRole;
import software.amazon.awssdk.services.bedrockruntime.model.ConverseResponse;
import software.amazon.awssdk.services.bedrockruntime.model.Message;

public class AnthropicClient {

	private BedrockRuntimeClient mClient;
	private static final String mModelId = "anthropic.claude-3-haiku-20240307-v1:0";

	public AnthropicClient() {
		// Specify the credentials
		Dotenv dotenv = Dotenv.load();
		String awsAccessKeyId = dotenv.get("AWS_ACCESS_KEY_ID");
		String awsSecretAccessKey = dotenv.get("AWS_SECRET_ACCESS_KEY");

		AwsBasicCredentials awsCreds = AwsBasicCredentials //
				.create(awsAccessKeyId, awsSecretAccessKey);

		mClient = BedrockRuntimeClient //
				.builder() //
				.credentialsProvider(//
						StaticCredentialsProvider.create(awsCreds)//
				).region(Region.US_EAST_1) //
				.build();

	}

	public void request() {
		String inputText = "What is the capital of France.";

		Message message = Message.builder()//
				.content(fromText(inputText))//
				.role(ConversationRole.USER)//
				.build();

		ConverseResponse response = mClient.converse(//
				request -> request.modelId(mModelId).messages(message)//
		);

		String responseText = response.output().message().content().get(0)
				.text();
		System.out.println(responseText);

	}

	public static void main(String[] args) {
		AnthropicClient cli = new AnthropicClient();
		long start = currentTimeMillis();
		int n = 10;
		for (int i = 0; i < n; i++) {
			cli.request();
		}

		long end = currentTimeMillis();
		long dur = end - start;
		double reqs = n * 1000.0 / (end - start);
		System.out.println( //
				"Took: " + dur + " ms " + reqs + " req/s." //
		);
	}
}
