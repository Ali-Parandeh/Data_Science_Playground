# Subscribe Elena's phone number to the 'streets_critical' topic.
# Print the SMS subscription ARN.
# Subscribe Elena's email to the 'streets_critical topic.
# Print the email subscription ARN.

import boto3

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

str_critical_arn = 'arn:aws:sns:us-east-1:123456789012:streets_critical'

# Subscribe Elena's phone number to streets_critical topic
resp_sms = sns.subscribe(
  TopicArn = str_critical_arn, 
  Protocol='sms', Endpoint="+16196777733")

# Print the SubscriptionArn
print(resp_sms['SubscriptionArn'])
# <script.py> output:
#     arn:aws:sns:us-east-1:123456789012:streets_critical:c000be81-cb5e-461d-aea4-6c0fa2375307

# Subscribe Elena's email to streets_critical topic.
resp_email = sns.subscribe(
  TopicArn = str_critical_arn, 
  Protocol='email', Endpoint="eblock@sandiegocity.gov")

# Print the SubscriptionArn
print(resp_email['SubscriptionArn'])

# <script.py> output:
#     arn:aws:sns:us-east-1:123456789012:streets_critical:fc8d2196-623d-46b5-a1a8-616aa4c27c5a