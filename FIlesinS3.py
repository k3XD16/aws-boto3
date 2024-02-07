import json
import boto3

s3 = boto3.client('s3')

import json
import boto3

s3 = boto3.client('s3')

bktName = 'asdqwerrr'

#Main Lambda Handler Function
def lambda_handler(event, context):



    #Creating a Bucket
    
    create = s3.create_bucket(
        Bucket= bktName,
        CreateBucketConfiguration={
            'LocationConstraint':'ap-south-1'
        })
    print(create)
    print()
    print(f"Bucket {bktName} is created Succefully")
    print()
    
    
    
    
    #Deleting a Bucket
    
    delete = s3.delete_bucket(
            Bucket = bktName
            )
    print(delete)
    print(f"{bktName} is successfully deleted!")
    
        
    #Listing All Buckets

    list_all_s3 = s3.list_buckets()
    for i in range(4):
        print(f"Bucket Name: {list_all_s3['Buckets'][i]['Name']}")
        print(f"Creation Date: {list_all_s3['Buckets'][i]['CreationDate']}")

    
        
    #Uploading File in Bucket
    
    bktName = 'newbucket-001'
    file_path='/accesskey.txt'
    key = 'accesskey.txt'

    try:
        s3.put_object(Body=file_path,Bucket=bktName,Key=key)
        print(f"File {file_path} is successfully uploaded on {bktName} bucket!")
    except Exception as e:
        print(f'Error while uploading a {file_path} to s3  : {e}')