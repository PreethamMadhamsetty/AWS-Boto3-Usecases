import boto3
from botocore.exceptions import ClientError

# AWS S3 bucket details
BUCKET_NAME = "<bucket name>"
AWS_REGION = "us-east-1"  # Update this to your desired region

# Initialize S3 client
s3_client = boto3.client('s3', region_name=AWS_REGION)

# Function to delete a file from S3
def delete_from_s3(s3_file_path):
    try:
        response = s3_client.delete_object(Bucket=BUCKET_NAME, Key=s3_file_path)
        print(f"Successfully deleted {s3_file_path} from S3.")
    except ClientError as e:
        print(f"Error deleting {s3_file_path} from S3: {str(e)}")

# Function to delete multiple files from S3
def delete_multiple_from_s3(file_paths):
    try:
        delete_objects = [{'Key': file_path} for file_path in file_paths]
        response = s3_client.delete_objects(Bucket=BUCKET_NAME, Delete={'Objects': delete_objects})
        deleted_files = response.get('Deleted', [])
        for deleted in deleted_files:
            print(f"Successfully deleted {deleted['Key']} from S3.")
    except ClientError as e:
        print(f"Error deleting files from S3: {str(e)}")

if __name__ == "__main__":
    # Example: Deleting a single file
    delete_from_s3('s3://sample-aws-s3/twitterdata.py') #give the file path in S3

    # Example: Deleting multiple files
    #files_to_delete = ['path/to/your/file1.txt', 'path/to/your/file2.txt', 'path/to/your/file3.txt']
    #delete_multiple_from_s3(files_to_delete)
