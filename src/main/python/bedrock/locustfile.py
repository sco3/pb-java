import json
import os
import dotenv
import argparse
from botocore.response import StreamingBody
import boto3
from locust import HttpUser, task

class BedrockClient:
    def __init__(self) -> None:
        # Initialize Bedrock client using boto3
        self.bedrock_client = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1",
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),  # Use None as default
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),  # Use None as default
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
                result += text + " "

        except Exception as e:
            print(f"ERROR: {e}")

        return result


class ClaudeUser(HttpUser):
    wait_time = 0  # Set wait time to 0 to make requests without waiting

    def on_start(self):
        """Called when a simulated user starts running"""
        dotenv.load_dotenv()  # Load environment variables
        self.client = BedrockClient()  # Initialize BedrockClient

        # Get prompts from command line arguments
        self.prompts = self.get_prompts()

    def get_prompts(self):
        """Retrieve prompts from command line arguments."""
        parser = argparse.ArgumentParser(description="Load test the Bedrock model with specified prompts.")
        parser.add_argument(
            '--prompts', type=str, nargs='+', required=True,
            help="List of prompts to send to the model"
        )
        args = parser.parse_args()
        return args.prompts

    @task
    def send_request(self):
        """Task that simulates sending a request to the model"""
        for prompt in self.prompts:
            result = self.client.call_claude_bedrock(prompt)
            print(f"Prompt: {prompt}, Response: {result}")  # Output the result to the console for visibility


if __name__ == "__main__":
    # Run the Locust user class
    dotenv.load_dotenv()  # Load environment variables
    import sys
    sys.argv = sys.argv[:1]  # Remove any additional arguments from sys.argv to avoid argparse conflict
    ClaudeUser().on_start()  # Call the on_start method for testing

# locust -f locustfile.py --host=http://localhost --prompts "What is the capital of France?" "Tell me about the Great Wall of China." "Explain quantum computing."
