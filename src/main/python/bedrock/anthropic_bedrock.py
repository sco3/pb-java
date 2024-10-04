import json
import os

from anthropic import AnthropicBedrock
import boto3
from botocore.response import StreamingBody
import dotenv
import time


class AnthropicClient:
    def __init__(self) -> None:
        # dotenv.load_dotenv("/app/.env")
        self.client = AnthropicBedrock(
            # Authenticate by either providing the keys below or use the default AWS credential providers, such as
            # using ~/.aws/credentials or the "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.
            aws_region="us-east-1",
        )

    def call_claude(self, prompt: str) -> str:
        result: str = ""

        try:
            message = self.client.messages.create(
                model="anthropic.claude-3-haiku-20240307-v1:0",
                max_tokens=256,
                messages=[{"role": "user", "content": prompt}],
            )
            print(message.content)

        except Exception as e:
            print(f"ERROR: {e}")

        return result


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
                "max_tokens": 10,
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


def main_boto() -> None:
    client = BedrockClient()
    result = client.call_claude_bedrock("What is the capital of France?")
    print(result)


def main_anthropic() -> None:
    client: AnthropicClient = AnthropicClient()
    start = time.time_ns()
    n = 10
    for i in range(n):
        result = client.call_claude("What is the capital of France?")
        print(result)
    end = time.time_ns()
    dur = (end - start) / 1000_000_000.0
    reqs = n / dur
    print(f"Took: {dur} s Req/s: {reqs} ")


if __name__ == "__main__":
    main_anthropic()
