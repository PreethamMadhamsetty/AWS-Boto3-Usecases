import logging
import boto3
from botocore.exceptions import ClientError
import os

# Let's use Amazon S3
s3 = boto3.resource('s3')
# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket"""

    if object_name is None:
        object_name = os.path.basename(file_name)

    s3_client = boto3.client('s3')

    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(f"File '{file_name}' uploaded successfully to bucket '{bucket}' as '{object_name}'")
        return True
    except ClientError as e:
        logging.error(e)
        print(f"Error: {e}")
        return False

# Call function with correct path
file_path = r"C:\Users\Preetham Madhamsetty\OneDrive\Documents\Docs\New resumes\SDE\PreethamMadhamsetty.pdf"
bucket_name = "preetham-aws-s3"
object_name = "PreethamMadhamsetty.pdf"

upload_file(file_path, bucket_name, object_name)

