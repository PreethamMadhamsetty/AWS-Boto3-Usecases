import boto3

# Create EC2 client
ec2 = boto3.client('ec2')


def create_multiple_ec2_instances(num_instances, instance_type, ami_id,
                                  key_name):
    """Launch multiple EC2 instances"""
    try:
        # Launch the specified number of EC2 instances
        response = ec2.run_instances(
            ImageId=ami_id,  # AMI ID to use for the instances
            InstanceType=instance_type,  # Instance type (e.g., t2.micro, t2.medium, etc.)
            MinCount=num_instances,  # Minimum number of instances to launch
            MaxCount=num_instances,  # Maximum number of instances to launch (same as MinCount for fixed count)
            KeyName=key_name,  # Key pair name for SSH access
            SecurityGroupIds=['sg-0af730bcb08b72c84'],  # Security group IDs (replace with your own)
            SubnetId='subnet-0892db00a6420eadc',  # Subnet ID (replace with your own)
        )

        # Print the instance IDs of the newly created instances
        instance_ids = [instance['InstanceId'] for instance in response['Instances']]
        print(f"Successfully launched {num_instances} EC2 instance(s): {instance_ids}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Create 3 EC2 instances (customize num_instances, instance_type, ami_id, key_name, etc.)
create_multiple_ec2_instances(num_instances=2, instance_type='t2.micro', ami_id='ami-0ac4dfaf1c5c0cce9',
                              key_name='My tutorial')
