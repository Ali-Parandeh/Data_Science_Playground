# Initialize boto3 client for SNS
sns = boto3.client('sns', 
                   region_name='us-east-1', 
                   aws_access_key_id=AWS_KEY_ID, 
                   aws_secret_access_key=AWS_SECRET)

# Create the city_alerts topic
response = sns.create_topic(Name="city_alerts")
c_alerts_arn = response['TopicArn']

# Re-create the city_alerts topic using a oneliner
c_alerts_arn_1 = sns.create_topic(Name='city_alerts')['TopicArn']

# Compare the two to make sure they match
print(c_alerts_arn == c_alerts_arn_1)

# <script.py> output:
#     True