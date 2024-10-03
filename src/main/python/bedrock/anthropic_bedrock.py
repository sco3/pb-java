import boto3
import json
import dotenv
import os
from botocore.response import StreamingBody


class BedrockClient:
    def __init__(self) -> None:
        # Initialize Bedrock client using boto3
        self.bedrock_client = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1",
            aws_access_key_id=os.getenv(
                "AWS_ACCESS_KEY_ID"
            ),  # Use None as default
            aws_secret_access_key=os.getenv(
                "AWS_SECRET_ACCESS_KEY"
            ),  # Use None as default
        )

    def call_claude_bedrock(self, prompt: str) -> str:
        result: str = ""
        try:
            model_id: str = "anthropic.claude-3-haiku-20240307-v1:0"

            data: dict = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 512,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0,
                "top_p": 0,
            }

            request: str = json.dumps(data)

            response: dict = self.bedrock_client.invoke_model(
                modelId=model_id, body=request
            )
            response_body_stream: StreamingBody = response["body"]
            response_data: str = response_body_stream.read().decode("utf-8")
            out_data: dict = json.loads(response_data)
            for item in out_data.get("content", []):
                text: str = item.get("text", "")
                # print(text)
                result += text + " "

        except Exception as e:
            print(f"ERROR: {e}")

        return result


def main() -> None:
    dotenv.load_dotenv()  # Load environment variables from .env file
    client = BedrockClient()

    # Call the model and print the result
    result = client.call_claude_bedrock("What is the capital of France?")
    print(result)


if __name__ == "__main__":
    main()
