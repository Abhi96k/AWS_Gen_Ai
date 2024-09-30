import boto3
import botocore.config
import json
from datetime import datetime


def blog_generate_using_bedrock(blogtopic: str) -> str:
    prompt = f"""<s>[INST]Human: Write a 200 words blog on the topic {blogtopic}
    Assistant:[/INST]
    """

    body = {
        "prompt": prompt,
        "max_gen_len": 512,
        "temperature": 0.5,
        "top_p": 0.9
    }

    try:
        # Set region_name to ap-south-1 (Mumbai)
        bedrock = boto3.client("bedrock-runtime", region_name="ap-south-1",
                               config=botocore.config.Config(read_timeout=300, retries={'max_attempts': 3}))

        response = bedrock.invoke_model(
            modelId="meta.llama3-70b-instruct-v1:0",
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body)
        )

        response_content = response.get('body').read()
        response_data = json.loads(response_content)
        print(response_data)
        blog_details = response_data.get('generation')
        return blog_details
    except Exception as e:
        print(f"Error generating the blog: {e}")
        return ""

def save_blog_details_s3(s3_key, s3_bucket, generate_blog):
    # Set region_name to ap-south-1 (Mumbai)
    s3 = boto3.client('s3', region_name="ap-south-1")

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print("Blog saved to S3")
    except Exception as e:
        print(f"Error when saving the blog to S3: {e}")

def lambda_handler(event, context):
    # TODO implement
    event = json.loads(event['body'])
    blogtopic = event['blog_topic']

    generate_blog = blog_generate_using_bedrock(blogtopic=blogtopic)

    if generate_blog:
        current_time = datetime.now().strftime('%H%M%S')
        s3_key = f"blog-output/{current_time}.txt"
        s3_bucket = 'awsbedrockcoursegneai'
        save_blog_details_s3(s3_key, s3_bucket, generate_blog)
    else:
        print("No blog was generated")

    return {
        'statusCode': 200,
        'body': json.dumps('Blog Generation is completed')
    }


#https://6ia491vch4.execute-api.ap-south-1.amazonaws.com/dev



