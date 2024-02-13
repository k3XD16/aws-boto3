# EC2Automation

### Steps to be followed:

- Set up AWS Environment:

Ensure you have an AWS account.
Access the AWS Management Console.


- Create an IAM Role for Lambda:

Go to the IAM service in the AWS Management Console.
Create a new IAM role with permissions to perform necessary actions like EC2 instance creation, logging, and EventBridge invocation. Assign the AWSLambdaBasicExecutionRole and AmazonEC2FullAccess policies.


- Create a Lambda Function:

Go to the Lambda service in the AWS Management Console.
Create a new Lambda function.
Choose the runtime as per your preference (e.g., Python).
Assign the IAM role created in the previous step to the Lambda function.
Write the function code to create a new EC2 instance based on your requirements. This function will be triggered when an EC2 instance termination event occurs via EventBridge.


- Set up EventBridge Rule:

Go to the EventBridge service in the AWS Management Console.
Create a new rule.
Define the event pattern to capture EC2 instance termination events. You can specify filters based on events like AWS::EC2::InstanceTerminated.
Configure the target of the rule to be the Lambda function created in the previous step.


- Testing and Monitoring:

Test the setup by manually terminating an EC2 instance. Ensure that the Lambda function gets triggered and creates a new instance seamlessly.
Monitor the system for any issues and fine-tune the Lambda function and EventBridge rule if necessary.
Set up CloudWatch alarms for critical events or failures.


- Additional Considerations:

Ensure that your Lambda function and EventBridge rule are configured properly for security and scalability.
Implement error handling and logging in your Lambda function to capture any failures during instance creation.
Consider using AWS SDKs or automation tools like AWS CloudFormation or AWS CDK for infrastructure as code to manage your resources more efficiently.
