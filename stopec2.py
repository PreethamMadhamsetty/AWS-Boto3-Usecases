import boto3

# Create EC2 client
ec2 = boto3.client('ec2')


def stop_running_instances():
    try:
        # Describe instances to find running instances
        response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )

        # Extract instance IDs of the running instances
        instance_ids = []
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_ids.append(instance['InstanceId'])

        # If there are running instances, stop them
        if instance_ids:
            ec2.stop_instances(InstanceIds=instance_ids)
            print(f"Successfully stopped the following instances: {instance_ids}")
        else:
            print("No running instances found.")

    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function to stop running instances
stop_running_instances()
