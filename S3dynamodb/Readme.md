# JSon to DynamoDB

### This Lambda Function denotes, when you;ve a JSON file of key value pair of data which can be converted into db you can use this lambda script to send the JSON into DynamoDB.

### Step-by-Step Procedure:

- **Set up AWS Resources:**
  
Create an S3 Bucket: If you haven't already, create an S3 bucket where your JSON file is stored.

Create a DynamoDB Table: Similarly, create a DynamoDB table where you want to store the data from the JSON file. Make sure to define the table schema (Primary Key, Attributes, etc.) based on the structure of your JSON data.

- **Create a Lambda Function:**
  
Go to Lambda Console: Navigate to the AWS Lambda console.

Create a New Lambda Function: Click on "Create function" and choose "Author from scratch".

- **Configure the Function:**

Function Name: Choose a name for your Lambda function.
Runtime: Select Python as the runtime.
Execution Role: Create or choose an existing role with permissions to access both S3 and DynamoDB.


- **Configure Trigger:**
  
Add S3 Trigger: Once your Lambda function is created, go to the "Designer" section and click on "Add trigger".

Configure S3 Trigger: Choose the S3 bucket where your JSON file is stored and configure the event type (e.g., Object Created).

- **Save and Test**
  
Save Configuration: Make sure to save the Lambda function configuration after adding the trigger.

Test the Function: You can test the function by uploading a JSON file into the S3 bucket. The Lambda function should automatically trigger and insert the data into the DynamoDB table.
