# If there are over 100 water violations, publish to 'water_critical' topic.
# If there are over 300 water violations, publish to 'water_extreme' topic.

import boto3

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

vcounts = {'streets': 422, 'trash': 100, 'water': 321}

dept_arns = {'streets_critical': 'arn:aws:sns:us-east-1:123456789012:streets_critical',
 'streets_extreme': 'arn:aws:sns:us-east-1:123456789012:streets_extreme',
 'trash_critical': 'arn:aws:sns:us-east-1:123456789012:trash_critical',
 'trash_extreme': 'arn:aws:sns:us-east-1:123456789012:trash_extreme',
 'water_critical': 'arn:aws:sns:us-east-1:123456789012:water_critical',
 'water_extreme': 'arn:aws:sns:us-east-1:123456789012:water_extreme'}

if vcounts['water'] > 100:
      # If over 100 water violations, publish to water_critical
  sns.publish(
    TopicArn = dept_arns['water_critical'],
    Message = "{} water issues".format(vcounts['water']),
    Subject = "Help fix water violations NOW!")

if vcounts['water'] > 300:
  # If over 300 violations, publish to water_extreme
  sns.publish(
    TopicArn = dept_arns['water_extreme'],
    Message = "{} violations! RUN!".format(vcounts['water']),
    Subject = "THIS IS BAD.  WE ARE FLOODING!")