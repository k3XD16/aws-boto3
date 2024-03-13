import json
import boto3

s3 = boto3.client('s3')
bktName = 'Bucketname-001'

def lambda_handler(event, context):
    # resource = s3.create_bucket(
    #     Bucket= bktName,
    #     CreateBucketConfiguration={
    #     'LocationConstraint':'ap-south-1'}
    #     )
    # print(resource)
    # print(f"Bucket {bktName} is Created Successfully!")
    
    file_path='/accesskey.txt'
    key = 'accesskey.txt'

    try:
        s3.put_object(Body=file_path,Bucket=bktName,Key=key)
        print(f"File {file_path} is successfully uploaded on {bktName} bucket!")
    except Exception as e:
        print(f'Error while uploading a {file_path} to s3  : {e}')
