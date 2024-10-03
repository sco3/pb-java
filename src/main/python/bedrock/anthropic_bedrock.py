import boto3
import json

# Initialize Bedrock client using boto3
bedrock_client = boto3.client('bedrock-runtime', region_name='us-east-1')

def call_claude_bedrock(prompt):
    response = bedrock_client.invoke_model(
        modelId='anthropic.claude-v2', 
        body=json.dumps({
            "prompt": prompt,
            "max_tokens_to_sample": 100
        }),
        contentType='application/json'
    )
    # Parse the response
    response_body = json.loads(response['body'])
    return response_body['completion']