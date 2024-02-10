import json
import boto3

db = boto3.client('dynamodb')
def lambda_handler(event, context):
    
#Create Table

    # response = db.create_table(AttributeDefinitions=[
    #     {
    #         'AttributeName': 'EmpID',
    #         'AttributeType': 'S'
    #     },
    #     {
    #         'AttributeName': 'EmpName',
    #         'AttributeType': 'S'
    #     }
    # ],
    # TableName='EmployeeDetails',
    # KeySchema=[
    #     {
    #         'AttributeName': 'EmpID',
    #         'KeyType': 'HASH'
    #     },
    #     {
    #         'AttributeName': 'EmpName',
    #         'KeyType': 'RANGE'
    #     }
    # ],ProvisionedThroughput={
    #     'ReadCapacityUnits': 1,
    #     'WriteCapacityUnits': 1
    # })
    
    # print(response)

#Put Items in table

    response = db.put_item(
        TableName='EmployeeDetails',
        Item={
            'EmpID': {
                'S': '1001',
            },
            'EmpName': {
                'S': 'YourFullName',
            },
            'Skills': {
                'SS': ['Python' ,'Javascript','Java','AWS','GCP','Docker'],
            },
            'Experiences': {
                'N': '7',
            },
        }
    )
    print(response)