package claude;

import static java.lang.System.currentTimeMillis;
import static java.lang.System.out;
import static java.lang.Thread.sleep;
import static java.util.concurrent.Executors.newFixedThreadPool;
import static software.amazon.awssdk.services.bedrockruntime.model.ContentBlock.fromText;

import java.util.concurrent.ThreadPoolExecutor;

import io.github.cdimascio.dotenv.Dotenv;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.bedrockruntime.BedrockRuntimeClient;
import software.amazon.awssdk.services.bedrockruntime.model.ConversationRole;
import software.amazon.awssdk.services.bedrockruntime.model.ConverseRequest;
import software.amazon.awssdk.services.bedrockruntime.model.ConverseResponse;
import software.amazon.awssdk.services.bedrockruntime.model.InferenceConfiguration;
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
		try {
			String inputText = "What is the capital of England.";

			Message message = Message.builder().content(fromText(inputText))
					.role(ConversationRole.USER).build();

			InferenceConfiguration cfg = InferenceConfiguration.builder()
					.maxTokens(10).build();
			var request = ConverseRequest.builder().modelId(mModelId)
					.messages(message).inferenceConfig(cfg).build();

			// out.println("tokens:" + request.inferenceConfig().maxTokens());

			ConverseResponse response = mClient.converse(request);

			String responseText = response.output().message().content().get(0)
					.text();
			out.println(responseText);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static class Batcher implements Runnable {
		int mN = 0;

		public Batcher(int n) {
			mN = n;
		}

		public void run() {
			AnthropicClient cli = new AnthropicClient();

			for (int i = 0; i < mN; i++) {
				cli.request();
			}

		}

	}

	public static void main(String[] args) {
		int vUsers = 10;
		int runs = 10;
		long start = currentTimeMillis();
		ThreadPoolExecutor svc = (ThreadPoolExecutor) newFixedThreadPool(
				vUsers);
		for (int i = 0; i < vUsers; i++) {
			svc.execute(new Batcher(runs));
		}

		while (svc.getCompletedTaskCount() < vUsers) {
			try {
				sleep(1);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		long end = currentTimeMillis();
		long dur = end - start;
		double reqs = runs * vUsers * 1000.0 / (end - start);
		System.out.println( //
				"Took: " + dur + " ms " + reqs + " req/s." //
		);

	}

}
