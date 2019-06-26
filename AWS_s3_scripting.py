import boto3


s3 = boto3.resource('s3')
my_bucket = 'scriptingbucketpc'

try:
    response = s3.create_bucket(Bucket=my_bucket, CreateBucketConfiguration={'LocationConstraint':'us-west-2'})

except Exception as error:
    print(error)
