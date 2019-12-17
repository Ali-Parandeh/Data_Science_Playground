# For each department create a critical topic and store it in critical.
# For each department, create an extreme topic and store it in extreme.
# Place the created TopicArns into dept_arns.
# Print the dictionary.

import boto3

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

dept_arns = {}
departments = ['trash', 'streets', 'water']

for dept in departments:
  # For each deparment, create a critical topic
  critical = sns.create_topic(Name="{}_critical".format(dept))
  # For each department, create an extreme topic
  extreme = sns.create_topic(Name="{}_extreme".format(dept))
  # Place the created TopicARNs into a dictionary 
  dept_arns['{}_critical'.format(dept)] = critical['TopicArn']
  dept_arns['{}_extreme'.format(dept)] = extreme['TopicArn']

# Print the filled dictionary.
print(dept_arns)

# <script.py> output:
#     {'trash_critical': 'arn:aws:sns:us-east-1:123456789012:trash_critical', 
#     'trash_extreme': 'arn:aws:sns:us-east-1:123456789012:trash_extreme', 
#     'streets_critical': 'arn:aws:sns:us-east-1:123456789012:streets_critical', 
#     'streets_extreme': 'arn:aws:sns:us-east-1:123456789012:streets_extreme', 
#     'water_critical': 'arn:aws:sns:us-east-1:123456789012:water_critical', 
#     'water_extreme': 'arn:aws:sns:us-east-1:123456789012:water_extreme'}
