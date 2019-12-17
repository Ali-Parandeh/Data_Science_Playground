# If there are over 100 potholes, send a message with the current backlog count.
# Create the email subject to also include the current backlog counit.
# Publish message to the streets_critical Topic ARN.

import boto3
streets_v_count = 125

# Create boto3 client to S3
sns = boto3.client('sns', region_name='us-east-1', 
                         aws_access_key_id=AWS_KEY_ID, 
                         aws_secret_access_key=AWS_SECRET)

str_critical_arn = 'arn:aws:sns:us-east-1:123456789012:streets_critical'

# If there are over 100 potholes, create a message
if streets_v_count > 100:
  # The message should contain the number of potholes.
  message = "There are {} potholes!".format(streets_v_count)
  # The email subject should also contain number of potholes
  subject = "Latest pothole count is {}".format(streets_v_count)

  # Publish the email to the streets_critical topic
  sns.publish(
    TopicArn = str_critical_arn,
    # Set subject and message
    Subject = subject,
    Message = message
  )