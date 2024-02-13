import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    # instancetyp = 'i-instancetype'
    
    #Run EC2 instances
    instance = ec2.run_instances(
        ImageId = 'ami-imageID',
        MinCount = 1,
        MaxCount = 1,
        InstanceType = 't2.micro'
        )
    print(instance)
    print(f"InstanceID: {instance['Instances'][0]['InstanceId']}")
  