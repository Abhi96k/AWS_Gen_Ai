---
runme:
  id: 01J90W1HYFXVQ8DG937Q4HZSRT
  version: v3
---

# Blog Generation using AWS Bedrock and S3

This project generates a 200-word blog using the meta.llama3-70b-instruct-v1:0 model hosted on AWS Bedrock and saves the blog as a text file to an S3 bucket. It leverages an AWS Lambda function to orchestrate the blog generation and storage.

### Prerequisites
Before running this project, ensure you have the following:

- AWS account with appropriate permissions to use AWS Bedrock, Lambda, and S3.
- An S3 bucket created in the ap-south-1 (Mumbai) region.
- Boto3 and botocore installed in your Lambda environment.
- API Gateway setup (optional, for invoking the Lambda function via HTTP).

Architecture Overview
This project follows the following architecture:

- **API Gateway (Optional)**: Accepts HTTP requests and triggers the Lambda function.
- **Lambda Function**: Handles the logic to generate a blog using the LLaMA model via AWS Bedrock and stores the blog in the specified S3 bucket.
- **AWS Bedrock**: Provides the foundation model (meta.llama3-70b-instruct-v1:0) to generate the blog.
- **S3 Bucket**: Stores the generated blog as a text file.

Setup and Deployment
### Step 1: Create and Deploy Lambda Function

1. Go to AWS Lambda in the ap-south-1 region.
2. Create a new Lambda function.
3. Upload your code (provided in this repository) or paste it directly in the AWS console.
4. Add necessary permissions to the Lambda function to access AWS Bedrock and S3.
5. Set up an API Gateway if you wish to trigger the Lambda function via HTTP.

Step 2: Configure API Gateway (Optional)
### Step 2: Set Up API Gateway

1. Set up an API Gateway that invokes the Lambda function on HTTP POST requests.
2. Map the Lambda function to an API Gateway endpoint (e.g., `/dev`).

Step 3: S3 Bucket Configuration
### Step 3: Create and Configure S3 Bucket

1. Create an S3 bucket in the ap-south-1 region.
2. Set up appropriate permissions to allow Lambda to write to the bucket.
3. Replace `s3_bucket` in the code with your actual bucket name.

Usage
### Request

![image](https://github.com/user-attachments/assets/3ef222e1-d8b0-4d1b-83b1-cac5ed80f47d)

![image](https://github.com/user-attachments/assets/761ca929-0b10-45ed-a80d-f2c52ef187f7)

![image](https://github.com/user-attachments/assets/b7e3e939-88fc-48a7-90f0-2c4c867c28bd)

![image](https://github.com/user-attachments/assets/34bab4d7-2187-4202-8c34-36ff2c489e54)








You can trigger the Lambda function by sending an HTTP POST request to your API Gateway endpoint (if set up) or invoking the function directly. The request body should be in JSON format:

Architecture
### Architecture Description

- **Client/Request**: The user sends a request (via API Gateway or manually) to AWS Lambda with a specified `blog_topic`.
- **Lambda Function**: Upon invocation, the Lambda function sends the prompt to the LLaMA model on AWS Bedrock to generate the blog.
- **AWS Bedrock**: Bedrock processes the request using the `meta.llama3-70b-instruct-v1:0` model and returns the blog content.
- **S3 Bucket**: The Lambda function saves the generated blog as a `.txt` file in an S3 bucket.
