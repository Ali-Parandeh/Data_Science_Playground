# List subscriptions for 'streets_critical' topic.
# For each subscription, if the protocol is 'sms', unsubscribe.
# List subscriptions for 'streets_critical' topic in one line.
# Print the subscriptions

import boto3

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

str_critical_arn = 'arn:aws:sns:us-east-1:123456789012:streets_critical'

# List subscriptions for streets_critical topic.
response = sns.list_subscriptions_by_topic(
  TopicArn = str_critical_arn)

# For each subscription, if the protocol is SMS, unsubscribe
for sub in response['Subscriptions']:
  if sub['Protocol'] == 'sms':
	  sns.unsubscribe(SubscriptionArn=sub['SubscriptionArn'])

# List subscriptions for streets_critical topic in one line
subs = sns.list_subscriptions_by_topic(
  TopicArn=str_critical_arn)['Subscriptions']

# Print the subscriptions
print(subs)

# <script.py> output:
#     [{'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical:40083fcf-d3a9-42f3-87c2-5c2ab7071673', 
#     'Owner': '', 'Protocol': 'email', 'Endpoint': 'js@fake.com', 
#     'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}, 
#     {'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical:80c0b12b-bd39-42ea-9503-38c2e7811230', 
#     'Owner': '', 'Protocol': 'email', 'Endpoint': 'whoami@fake.com', 
#     'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}, 
#     {'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical:1fcba992-3862-4a92-b8d7-e9f85c607dd1', 
#     'Owner': '', 'Protocol': 'email', 'Endpoint': 'Evely@fake.com', 
#     'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}, 
#     {'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical:c4fe6ec7-1a47-494d-846b-29716dd45181', 
#     'Owner': '', 'Protocol': 'email', 'Endpoint': 'masdfsx@maksimize.com', 
#     'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}, 
#     {'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical:2709228f-9a2b-43d3-ae8d-5b0948edfb32', 
#     'Owner': '', 'Protocol': 'email', 'Endpoint': 'fanndyma3@fake.com', 
#     'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}, 
#     {'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical:566d099d-c559-4e87-99d5-1d9f33438a1e', 
#     'Owner': '', 'Protocol': 'email', 'Endpoint': 'whddsfsdoami@fake.com', 
#     'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}, 
#     {'SubscriptionArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical:5c986ec4-e697-48df-a477-e55d039b3dfb', 
#     'Owner': '', 'Protocol': 'email', 'Endpoint': 'msdfsdfsdax@maksimize.com', 
#     'TopicArn': 'arn:aws:sns:us-east-1:123456789012:streets_critical'}]