import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

def terminate_all_instances():
    """Terminate all EC2 instances irrespective of their state"""
    try:
        # Describe instances to get all instances (irrespective of state)
        response = ec2.describe_instances()

        # Get the instance IDs of all instances
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])

        if instance_ids:
            # Terminate the instances
            terminate_response = ec2.terminate_instances(InstanceIds=instance_ids)
            terminated_instances = [instance['InstanceId'] for instance in terminate_response['TerminatingInstances']]
            print(f"Successfully terminated the following instances: {terminated_instances}")
        else:
            print("No instances found.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Terminate all instances
terminate_all_instances()
