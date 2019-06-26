import boto3


# Create and terminate an EC2 instance
ec2 = boto3.resource('ec2')
'''
instance = ec2.create_instances(
    ImageId='ami-082b5a644766e0e6f',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)
print(instance[0].id)
'''

instance_id ='i-037cb351ddf7c9123'
instance = ec2.Instance(instance_id)
response = instance.terminate()
print(response)