import os
import time
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# AWS S3 bucket details
BUCKET_NAME = "preetham-aws-s3"
LOCAL_DIRECTORY = r"C:\Users\Preetham Madhamsetty\OneDrive\Documents\Docs\New resumes\SDE"
AWS_REGION = "us-east-1"  # Update this to your desired region

# Initialize S3 client
s3_client = boto3.client('s3', region_name=AWS_REGION)

# Function to get the S3 file's last modified time
def get_s3_file_last_modified(s3_file_path):
    try:
        response = s3_client.head_object(Bucket=BUCKET_NAME, Key=s3_file_path)
        return response['LastModified']
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchKey':
            return None
        else:
            print(f"Error retrieving file info from S3: {str(e)}")
            return None

# Function to upload files to S3
def upload_to_s3(local_file_path, s3_file_path):
    try:
        s3_client.upload_file(local_file_path, BUCKET_NAME, s3_file_path)
        print(f"Successfully uploaded {local_file_path} to {s3_file_path}")
    except FileNotFoundError:
        print(f"File {local_file_path} not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except Exception as e:
        print(f"Error uploading {local_file_path}: {str(e)}")

# Function to sync files from local directory to S3 (only new/modified files)
def sync_files_to_s3():
    # Walk through the local directory
    for root, dirs, files in os.walk(LOCAL_DIRECTORY):
        for file in files:
            local_file_path = os.path.join(root, file)
            s3_file_path = os.path.relpath(local_file_path, LOCAL_DIRECTORY)

            # Get the last modified time of the local file
            local_file_modified_time = os.path.getmtime(local_file_path)

            # Get the last modified time of the file in S3 (if exists)
            s3_last_modified_time = get_s3_file_last_modified(s3_file_path)

            # If the file doesn't exist in S3 or has been modified locally, upload it
            if s3_last_modified_time is None or local_file_modified_time > s3_last_modified_time.timestamp():
                upload_to_s3(local_file_path, s3_file_path)
            else:
                print(f"Skipping {local_file_path}, no changes detected.")

# Function to run the backup every 5 minutes
def run_backup():
    while True:
        print(f"Starting backup at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        sync_files_to_s3()
        print("Backup completed. Waiting for 5 minutes...")
        time.sleep(300)  # Wait for 5 minutes (300 seconds)

if __name__ == "__main__":
    run_backup()
