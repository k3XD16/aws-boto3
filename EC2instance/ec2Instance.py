import json
import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instancetyp = 'i-instanceid' #instances - id
    
    #Run EC2 instances
    instance = ec2.run_instances(
        ImageId = 'ami-amazonmachineimageid',   # provide ami-id 
        MinCount = 1,                           # Minimum Count
        MaxCount = 1,                           # Maximum Count
        InstanceType = 't2.micro'               # Instance type 
        )
    print(instance)
    print(f"InstanceID: {instance['Instances'][0]['InstanceID']}")
    
    
    #Stop EC2 Instances
    instance = ec2.stop_instances(
    InstanceIds=['i-instanceid'  #instances - id
        ]
    )
    # print(f"Instance {InstanceIds} is Stopped")
    
    
    #Start EC2 Instances
    instance = ec2.start_instances(
        InstanceIds=['i-instanceid'])
    # print(f"Instance {InstanceIds} is Starting Again") 
        
        
    #Terminate EC2 Instances
    instance = ec2.terminate_instances(
        
        InstanceIds=[instancetyp])
    # print(f"Instance {instancetyp} is Terminated")
    
    
    #Describe Ec2 Instances
    response = ec2.describe_instances()
    print(response)
    